# Appendix E: The Laws of the Desk

> **Prerequisites.** None. This appendix is a map, not a road. Each law points at the section where it was built, and that section carries its own prerequisites.

## E.0 Cold Open: Sixteen Piles

*Friday, 6:15 p.m.* The Edition 2 proofs came back at four. By six Theo Marsh had scissors, a roll of tape and every Desk Debrief in the book cut into strips: 228 bullets from 29 debriefs, spread across three desks like a ransom note drafted by committee.

"I want to tape the important ones to the monitor," he said. "The monitor is fourteen inches wide."

An hour earlier ROBO had been asked to "list the rules of the desk." It returned all 228 bullets as 228 rules, then appended a 229th: *by Rule 12 of this list, the desk has tried 228 rules and should deflate the Sharpe ratio of each.* Nobody could find the flaw.

Ines Okafor picked up three strips that said the same thing in three chapters' voices. "A law isn't a good sentence. A law is a sentence that cost somebody money three separate times. Once is an anecdote, twice is a coincidence. Three hands in three different games is how the table actually plays."

"And it needs an equation," said Kaz Lind, "or it's a horoscope." Kaz held up the strip from Chapter 13: *One word can be the whole loss.* "This one has no equation. It has a word." A pause. "Which word?"

"'Open,'" said Mags Dunleavy, without looking up. "Followed by 'market.' Two hundred and sixty-one million dollars before interest. Back in my day we had one law: never buy from the guy who called you." She pointed at the strips. "That's your Law 5. Your Law 15 is the exception: unless a rule made him call."

Theo had started sorting. One pile said "strip the beta first." One said "which measure?" One refused, in nine different ways, to use 40%. By seven there were sixteen piles and a handful of orphans.

"Sixteen sentences, sixteen equations, and for each one the list of places in the book where it was paid for," he said. "If a new hire reads only this, what do they still get wrong?"

"Everything," said Mags. "But faster, and they'll know which page to read next."

**Which sixteen sentences, each carrying one equation, hold the desk's hard-won lessons, and where in the book was each one earned?**

By the end of this appendix you will be able to state each law in a sentence short enough to tape to a monitor, write the equation it compresses, name the section where it was derived and the sections where it changes a number, and audit a single live ticket against all sixteen in under five minutes (§E.6). You will also be able to tag any Desk Debrief bullet with its law numbers by hand or with the linter in §E.8.

*Used in:* the Preface ("How a chapter is built"), `00_01_tape_to_your_monitor.md`, and every Desk Debrief, whose bullets carry law tags such as `[L6]`.

## E.1 How to Read, Cite and Grow the Laws

**The admission rule.** A sentence becomes a Law of the Desk when it passes three tests. (i) It recurs, in substance, in at least three Desk Debriefs of Edition 1. (ii) It compresses an equation that the book derives somewhere, so that the sentence can be checked rather than merely believed. (iii) Somewhere in the book, breaking it has a price attached: a dated case, a worked loss or a backtest that died. Sixteen sentences passed. The orphans, and the two near-misses that are waiting for a third debrief, are in §E.7.

**The anatomy of an entry.** Each law has five parts:

1. **The statement**, in bold, sized for the monitor.
2. **The equation** it compresses, in the book's notation (Appendix A).
3. **Why it holds**: the derivation in four or five lines, with the full version left to the section that owns it.
4. **Earned in / Bites in**: *earned in* lists the sections that derive or establish the law, and the canonical home comes first; *bites in* lists the sections where the law changes a number, a hedge or a decision.
5. **The violation**: what breaking the law looks like, usually in the cast's own words.

**Citing a law.** A Desk Debrief bullet ends with its tags in square brackets: `[L6]`, or `[L4, L7]` when one bullet carries two laws. Body text cites the law by number and section on first use ("charge the jump once (Law 6, §18.6)"). There is one exception. Law 1 is also the desk motto, and Edition 1 printed it 46 times, so Edition 2 rations it: it appears once per chapter, by name, in the Debrief, and everywhere else it is `[L1]`.

**Numbering is permanent.** A new law gets the next number and an old law is never renumbered, for the same reason a CUSIP is never reissued: other documents point at it. A law that stops being true is struck through and kept, with the date and the section that killed it.

**Four families.** The laws come in four groups of four, and each group answers one question you should ask of every number on the desk.

- **The Ruler (Laws 1–4)**, §E.2: what is this number measured against?
- **The Table (Laws 5–8)**, §E.3: what must this price survive before it is a price?
- **The Tape (Laws 9–12)**, §E.4: what are the data and the backtest hiding?
- **The Clock (Laws 13–16)**, §E.5: when does the outcome arrive, and who decides it?

**Quick reference.** The last column lists the chapters whose Desk Debriefs already state the law in substance (B is Appendix B). Those are the three-or-more appearances that earned admission.

| # | Law | The equation it compresses | Earned in | Debriefs |
| :-- | :-- | :-- | :-- | :-- |
| 1 | IDO or it didn't happen | $\epsilon_{i,t} = r^{\text{ex}}_{i,t} - s_i\Delta t - \sum_k \beta_{i,k}F_{k,t}$ | §8.1, §8.8, §3.3 | 1, 3, 6, 8, 10, 11, 15, 17, 18, 19, 20, 22, 28, B |
| 2 | Bonds are not bets; issuers are | $BR_{\text{eff}} = N/(1+(m-1)\rho)$ | §4.3, §7.6, §28.2 | 4, 7, 9, 11, 28 |
| 3 | DTS is the unit of credit beta | $\beta_i = \text{DTS}_i/\text{DTS}_m$ | §8.4, §9.2 | 1, 7, 8, 9, 10, 12 |
| 4 | Say which measure you are in | $s - \lambda^{\mathbb{P}}L \approx (\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})L$ | §6.3, §6.8 | 1, 4, 6, 12, 13, 14, 15, 18 |
| 5 | A bid is a posterior, and winning is information | $b = \mathbb{E}^{\mathbb{P}}[V \mid \text{sell}] = m - \pi\sigma_V$ | §1.3, §3.2, §18.3 | 1, 2, 3, 18, 19 |
| 6 | Charge the jump once | $\text{Var} \ni q(1-q)J^2$; drift $\ni -(\lambda^{\mathbb{P}}-\lambda^{\mathbb{Q}})J\tau$ | §5.1, §18.6 | 5, 10, 11, 16, 18, 23, 24, 28 |
| 7 | Default is a menu and recovery is a U | $\lambda = \lambda_H + \lambda_D$; $f_R = w f_{\text{in}} + (1-w) f_{\text{out}}$ | §5.5, §5.6, §14.1–14.4 | 5, 6, 12, 13, 14, 24 |
| 8 | Every clause is a payoff function | $\Delta_j(V) = W^{\text{post}}_j(V) - W^{\text{pre}}_j(V)$ | §13.3, §15.1, §25.3 | 3, 6, 13, 15, 16, 21, 24, 25, 27 |
| 9 | A mark is a moving average of the truth | $\sigma_o = \sigma\sqrt{\sum_k\theta_k^2}$, $\beta^o_0 = \theta_0\beta$ | §8.5, §17.2 | 7, 8, 10, 12, 17, 19, 20, 21, 28, B |
| 10 | Costs decide and capacity is a square | $T_{\max} = \alpha/2\bar c$; $\alpha(A^*) = g/3$ | §2.9, §4.7, §4.8 | 2, 4, 9, 11, 12, 24, 28 |
| 11 | Label every number | $x = (v, u, \mathbb{M}, g, \ell, \tfrac{\text{num}}{\text{den}}, t^{\text{known}}, \text{src})$ | §4.5, §27.3, App B | 2, 4, 7, 14, 25, 26, 27, B |
| 12 | Count your trials | $\mathbb{E}[\max_{k\le K}\widehat{SR}_k] \approx \sqrt V\,z_K$ | §7.8, §26.7 | 1, 4, 7, 9, 26 |
| 13 | The label is the model | $F_k(t) \le 1 - \widehat{KM}_k(t)$ | §7.4, §11.5, §14.2 | 7, 11, 14, 15 |
| 14 | Censoring is the signal | $\mathcal{L} = \prod f(Q_i)\prod[1-F(\bar q)]$ | §2.2, §18.8, §22.2 | 2, 3, 5, 17, 18, 22, B |
| 15 | Forced selling is a supply schedule | $dQ = -\theta Q\,dt$, $p = v - \kappa Q/M$ | §16.2, §21.4, §1.8 | 1, 11, 16, 20, 21, 24 |
| 16 | The court is a random variable with timestamps | $\operatorname{logit}\theta_w(t) = \alpha_w + \sum_r J_{r,w}\mathbf{1}\{t\ge t_r\}$ | §14.6, §13.9, §16.1 | 3, 13, 14, 16, 22, 25, 27 |

Two patterns in the table are worth a sentence each. First, the laws with the longest debrief lists (1, 8, 9) are the ones about what a number *is*, not what it predicts. The desk loses more money to mislabeled quantities than to wrong forecasts. Second, almost every expensive mistake in the book breaks two laws at once: the excluded Serta lender broke 8 and 16, the private-credit Sharpe ratio breaks 9 and 11, the 3,000-configuration backtest breaks 10 and 12, and the "market is underpricing default" note breaks 4 and 7. When you find one violation, look for its partner.

*Used in:* the Preface (the Laws list and the tag legend); every Desk Debrief; `00_01_tape_to_your_monitor.md`, which groups its forty bullets by Part and tags each with its law.

## E.2 The Ruler: Laws 1–4

Before you ask whether a number is good, ask what it is measured against. The four laws of the Ruler fix the zero point (Law 1), the unit of count (Law 2), the unit of risk (Law 3) and the probability measure (Law 4). Get these wrong and every later law operates on the wrong quantity.

### Law 1. IDO or it didn't happen

> **Strip carry, Treasuries and DTS-scaled credit beta before you call anything alpha, a markout or a hedge.**

$$
\epsilon_{i,t} \;=\; \underbrace{\big(r_{i,t} - r^{\text{TSY}}_{i,t}\big)}_{\text{excess over KRD-matched Treasuries}} \;-\; \underbrace{s_i\,\Delta t}_{\text{spread carry}} \;-\; \underbrace{\sum_{k}\beta_{i,k}\,F_{k,t}}_{\beta_{i,k}\,=\,\text{DTS}_i\, b_k} .
$$

**Why it holds.** A bond's total return $r_{i,t}$ has three sources the desk did not choose to be paid for. Rates come out first, through a portfolio of par Treasuries matched on key-rate durations, which leaves the excess return $r^{\text{ex}}_{i,t}$. Spread carry $s_i\Delta t$ comes out next, because it is earned by holding beta, not by being right. Systematic spread moves come out last. Since $r^{\text{ex}}_{i,t} - s_i\Delta t \approx -D^{\text{spr}}_i\Delta s_{i,t} = -\text{DTS}_i\,(\Delta s_{i,t}/s_i)$, a factor model on relative spread changes, $\Delta s_i/s_i = \sum_k b_k f_k + e_i$, gives loadings proportional to DTS (Law 3). The order is accounting first, attribution second (§8.1). What remains, $\epsilon_{i,t}$, is the only part of the return that a signal, a counterparty score or a hedge can claim.

**Earned in** §8.1 (the two subtractions), §8.8 (what is left is IDO, and how to prove it), §3.3.3 (IDO markouts are the honest hand history). **Bites in** §1.10, §10.6.3 (credit TSMOM's alpha against passive beta had a *t*-statistic of 0.49 in AQR's test: trend is beta that changed its mind), §11.7.2 (a market-value-neutral low-risk tilt is beta wearing a factor's name tag), §15.6, §17.10, §18.7, §19.8, §20.5.3, §22.8.1, §24.1, §28.3 (the overlay manages beta so the cash books keep their IDO).

**The violation.** ROBO, told to "find alpha," sorts bonds by spread and buys the widest decile. It finds a great deal of beta and reports it as alpha in the column heading. ROBO is not wrong about the column heading; it is wrong about the column.

### Law 2. Bonds are not bets; issuers are

> **Effective breadth counts issuers, not CUSIPs. Forty-seven bonds of one issuer are one bet with forty-seven CUSIPs.**

$$
\operatorname{Var}\!\Big(\frac1N\sum_{i=1}^{N}\epsilon_i\Big) = \frac{\sigma^2\,[1+(m-1)\rho]}{N}
\quad\Longrightarrow\quad
BR_{\text{eff}} = \frac{N}{1+(m-1)\rho}, \qquad IR = IC\,\sqrt{BR_{\text{eff}}}\;TC .
$$

The right-hand pair is equation (4.1) of §4.3.

**Why it holds.** Take $N$ bonds from $M$ issuers, $m = N/M$ bonds each, with residual variance $\sigma^2$, residual correlation $\rho$ within an issuer and zero across issuers. The variance of the equally weighted residual is $N^{-2}[N\sigma^2 + N(m-1)\rho\sigma^2]$, which is the left side. Matching it to $\sigma^2/BR_{\text{eff}}$ gives the breadth. As $\rho \to 1$, $BR_{\text{eff}} \to N/m = M$, so the bet is the issuer. Chapter 28 adds a residual correlation $\rho_a$ across issuers, $N_{\text{eff}} = N/\big(1 + (m-1)\rho_w + (N-m)\rho_a\big)$ (28.5). As $N$ grows with $m=1$ this tends to $1/\rho_a$, so a 1% residual correlation caps any credit book at about 100 bets, however many issuers it holds.

*Two numbers to remember (illustrative).* Forty-seven CUSIPs of one issuer at $\rho = 0.9$ give $47/(1 + 46 \times 0.9) = 47/42.4 \approx 1.1$ bets. Kaz's panel of 212,000 bond-months comes to about 24,000 "hats," the uniqueness-weighted count of independent issuer observations (§7.6, §7.13). A model trained on it has the statistical power of the second number and the confidence of the first.

**Earned in** §4.3 (4.1), §7.6 (sample weights and the forty-seven-hat problem), §28.2 (28.4–28.5). **Bites in** §7.7 (cross-validation folds grouped by ultimate parent), §9.7 (combining factors), §11.6 (CCC is a crowd, not a person: diversify the bucket with breadth), §28.8 (an analyst's value is her $\rho$, not her IC), §28.9.

**The violation.** Asked to "diversify the book," ROBO maximizes line count and buys every CUSIP in the Halvorsen capital structure. The risk report shows four hundred lines and one opinion.

### Law 3. DTS is the unit of credit beta

> **Spread volatility scales with spread. Size, hedge and vol-target in DTS; beta is $\text{DTS}_i/\text{DTS}_m$ and carry is the price of DTS.**

$$
\sigma(\Delta s_i) = \sigma_{\text{rel}}\, s_i
\;\;\Longrightarrow\;\;
\sigma\big(r^{\text{ex}}_i\big) \approx D^{\text{spr}}_i\,\sigma(\Delta s_i) = \text{DTS}_i\,\sigma_{\text{rel}},
\qquad
\beta_i = \frac{\text{DTS}_i}{\text{DTS}_m},
\qquad
\frac{\text{carry}_i}{\text{DTS}_i} = \frac{s_i}{D^{\text{spr}}_i s_i} = \frac{1}{D^{\text{spr}}_i}.
$$

**Why it holds.** The empirical fact is that the relative spread change $\Delta s/s$, not the absolute change $\Delta s$, is the stable random variable across ratings, sectors and time. If the market's relative spread change is a common factor $f$, then $r^{\text{ex}}_i \approx -\text{DTS}_i f$ and $r^{\text{ex}}_m \approx -\text{DTS}_m f$, so the regression beta is the DTS ratio. Three consequences follow, and each one has a chapter. Vol targeting is a constant-DTS budget, so it sells after widening before any signal fires (§10.3). Carry per unit of DTS is $1/D^{\text{spr}}$, so a DTS-neutral carry factor is a short-duration factor and belongs with low-risk (§9.5). A dollar-neutral spread sort is a long-beta portfolio (§9.2; the "Sharpe 1.9, beta 0.6" cold open of Chapter 9). The law has a boundary. Below a price of about 70 a bond stops trading on its spread and starts trading on its recovery (§1.4, §8.3), and Law 3 hands the bond to Laws 6 and 7.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.35:* "we demonstrate that the volatility of spread changes (both systematic and idiosyncratic) is linearly proportional to spread level."
>
> **Annotation.** This sentence is the whole of Law 3, and the parenthesis is the part desks forget: the *idiosyncratic* volatility scales with spread too, so the residual risk in Law 1 and the breadth arithmetic in Law 2 should be DTS-scaled as well (§8.4, §19.4). The sample runs from 1989 to 2005. The 2026 desk departs from it in two places. The proportionality bends in the distressed tail, where the price is pinned by recovery rather than by spread, and in rate-driven regimes such as 2022, where the spread–rates correlation in §8.2 changed sign and empirical duration took over part of the hedge.

**Earned in** §8.4 (the canonical home), §9.2 (to become a back-reference to §8.4 in Edition 2), and Chapter 4-B for spread duration itself. **Bites in** §1.4 (risk scales with spread), §7.4 (barriers set in DTS space), §9.5, §10.3, §12.5 (covariance with DTS structure), §19.4 (the hedge in a portfolio trade), §28.7 (the leverage band).

**The violation.** A risk system that budgets in spread duration treats a 500 bp bond and a 100 bp bond of equal duration as equally risky. Ben Dor's own example says they are not: a 200 bp, two-year portfolio carries the same risk as a 100 bp, four-year one (§8.4).

### Law 4. Say which measure you are in

> **Prices live in $\mathbb{Q}$, forecasts live in $\mathbb{P}$, and the gap is the premium you are paid or paying. Tag every expectation and every PD field with its measure.**

$$
s \approx \lambda^{\mathbb{Q}}L^{\mathbb{Q}},
\qquad
\underbrace{s - \lambda^{\mathbb{P}}L^{\mathbb{P}}}_{\text{premium you are paid}} \;\approx\; \big(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}\big)L ,
\qquad
\text{PD}^{\mathbb{Q}} = N\!\Big(N^{-1}\big(\text{PD}^{\mathbb{P}}\big) + \rho\,\text{SR}_M\sqrt T\Big).
$$

**Why it holds.** The credit triangle (§6.8) turns a spread into a risk-neutral hazard times a risk-neutral loss. A recovery analysis, a PRS or an agency default study gives a physical one. Their difference is the credit risk premium (4.5). In Merton the measure change only moves the drift, from $\mu$ to $r$, which shifts distance to default by $\rho\,\text{SR}_M\sqrt T$ (§6.3.2). The premium therefore grows with $\sqrt T$ and is proportionally largest for safe names. *(Illustrative:)* a one-year shift of 0.16 multiplies a 13.8% PD by about 1.3 and a 0.13% PD by about 1.7. The premium is carry, not alpha (Law 1). Mixing the measures produces three recurring errors. The first is calibrating a $\mathbb{P}$ score to $\mathbb{Q}$ prices: PRS is $\mathbb{P}$ and the price is $\mathbb{Q}$, never the other way round (§13.8). The second is comparing a CDS hazard with an agency default rate before removing $\lambda_D$ and replacing the 40% convention (Law 7; §14.10). The third is putting a CDS-implied PD into the loss term of the forward-return identity, which forecasts a zero risk premium by construction (§12.2).

**Earned in** §6.3 (the measure change), §6.8 (the credit triangle), and Chapter 6-B, which becomes the single home for $\mathbb{P}\to\mathbb{Q}$ in intensity space. **Bites in** §1.5 (feed only $\mathbb{Q}$ quantities into the credit triangle), §3.1 (where Edition 2 fixes a $\mathbb{Q}$/$\mathbb{P}$ inconsistency), §4.4 (every value signal is a $\mathbb{Q}$-minus-$\mathbb{P}$ gap, 4.5), §12.2, §13.8, §14.1, §15.4 (the SMR is a $\mathbb{Q}$ break gauge), §18.6, §28.4 (Kelly uses $\lambda^{\mathbb{P}}$).

**The violation.** Applying the $\mathbb{P}\to\mathbb{Q}$ shift to a PD that was already backed out of spreads charges the premium twice, and every bond looks rich (§6.3, annotation). Ines calls the gap the rake. Charging it twice is paying the rake to yourself and calling it a loss.

*Used in:* every Debrief bullet tagged `[L1]`–`[L4]`; Chapter 4-B (spread duration and DTS), Chapter 6-B (the measure rule), Appendix A §A.3 (the "measure of every expectation" rule added in Edition 2), and the Halvorsen audit in §E.6.

## E.3 The Table: Laws 5–8

A price has to survive four things before it deserves the name: the counterparty who asked for it (Law 5), the jump that could end it (Law 6), the way default actually arrives (Law 7), and the document that decides who gets what when it does (Law 8). These are the laws of the poker table, and Ines would add that the table includes the lawyers.

### Law 5. A bid is a posterior, not a markup, and winning is information

> **Condition the price on who is selling and on the fact that you won. A backtest on fills alone cannot see the winner's curse.**

$$
b \;=\; \mathbb{E}^{\mathbb{P}}\big[V \mid \text{client sells}\big] \;=\; m - \pi\,\sigma_V,
\qquad
B^{*} = S_t - \pi J - \tfrac12\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q) - c,
\qquad
n_{\text{eff}} = \frac{n}{1+(n-1)\phi} \le \frac{1}{\phi}.
$$

**Why it holds.** Let the bond's value over the holding horizon be $m \pm \sigma_V$ with equal odds. A fraction $\pi$ of sellers know which, and they sell only in the low state; the rest sell at random. Then $\mathbb{P}(\text{low} \mid \text{sell}) = \tfrac12(1+\pi)$ and the conditional mean is $m - \pi\sigma_V$, which is (3.1). The shade $\pi\sigma_V$ is what the uninformed seller pays for the presence of the informed one. It is a posterior because $\pi$ depends on who is on the line: the Bayes step turns counterparty state into a logistic regression, estimated from markouts by feature bucket (§1.10). Chapter 1's bid equation adds the inventory term and the cost $c$ to the same posterior. Winning conditions a second time. Against $n$ dealers the winner was the most optimistic, so the bid shades by a further $w(n)\,\sigma_V$ (§3.2.3). And $n$ is not the number of dealers in the RFQ: eleven dealers anchored on the same composite at $\phi = 0.45$ count as $11/(1 + 10 \times 0.45) = 2.0$ *(illustrative)* (§2.3.2).

**Earned in** §3.2 (Glosten–Milgrom for RFQ), §1.3 (the bid equation), §18.3 (Kyle derived). **Bites in** §1.9 (toxic flow), §2.3.2 (anchored dealers), §3.3 (markouts are the hand history), §18.7 (raw hit ratios subsidize the wrong people), §18.9 (a BWIC is a first-price auction with a leak), §19.8 (the basket as a mystery box), and Chapter 18-B, which estimates $\pi$ by client tier and $n_{\text{eff}}$ from the desk's own logs.

**The violation.** A uniform markup is a posterior that forgot to ask who was calling. Ines's version: "The hands you lose look better than the hands you win." If you only study the hands you won, Law 14 says you are studying a censored sample.

### Law 6. Charge the jump once

> **Diffusive fear is pennies in bonds; the jump-to-default is the whole premium. Price it in one place, and do not add it again in the spread, the skew and the size.**

$$
\operatorname{Var}[R_h] = (1-q)\operatorname{Var}[X] + q\operatorname{Var}[Y] + \underbrace{q(1-q)\,J^2}_{\text{between the two worlds}},
\qquad
\underbrace{-\big(\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}}\big)J\tau}_{\text{the only jump term in the quote's drift}},
\qquad
\underbrace{\lambda^{\mathbb{P}}J^2\tau}_{\text{the jump term in its variance}} .
$$

**Why it holds.** A high-yield return is two worlds and a coin, $R_h = (1-D)X + DY$ with $\mathbb{P}(D=1) = q$ and jump size $J = \mathbb{E}[X] - \mathbb{E}[Y]$ (§5.1). The between-world term $q(1-q)J^2$ is most of the variance, and trailing price volatility measures only the world in which nothing happens. In the dealer's HJB with a jump (§18.6), a $\mathbb{Q}$-fair composite mid already contains $\lambda^{\mathbb{Q}}J$. The drift therefore adds only the $\mathbb{P}$-minus-$\mathbb{Q}$ difference, which is the desk's credit view, and the variance carries the physical jump. The diffusive Avellaneda–Stoikov spread meanwhile tends to $2/k$, which is greed, not fear (§18.4). *(Illustrative:)* over a five-day hold with $\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}} = 3.2\%$ a year and $J = 48$ points, the credit-view term is $0.032 \times 48 \times 5/252 \approx 0.03$ points. The posterior shade on the same ticket is more than ten times larger (§E.6).

There are three standard ways to charge the jump twice. (i) A CDS-implied $\lambda$ in the drift, on top of a $\mathbb{Q}$-fair composite, charges the market's fear a second time (§18.10). (ii) Applying an $e^{-\lambda T}$ haircut to a warrant or call priced off a market spot double-counts, because jump-to-default enters through the discount rate $r + \lambda$ (§16.4.2; an Edition 2 correction). (iii) Sizing down for jump-to-default after the skew has already priced it charges a third time (§23.4, §28.4).

**Earned in** §5.1 (the mixture), §5.3 (Kou: jumps give a non-zero short spread $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$), §18.6 (jump-to-default inside the HJB), and Chapter 6-B (Merton with jump-to-default, from which the Carr–Wu corridor of §23.3 follows). **Bites in** §10.9 (add $\lambda^{\text{J}}\mathbb{E}[J^2]$ to trend's variance), §11.1 (HY is a short put: skew $-(1-2p)/\sqrt{p(1-p)}$, about $-6.9$ at a 2% PD), §16.4, §23.4 (skew as jump-to-default), §24.3.1 (hedge to jump-to-default, $N^{\text{JTD}} = (P-R)/(1-R)$), §28.4 (Kelly, $f^\ast = 1/L - \lambda^{\mathbb{P}}/c$, 28.11).

**The violation.** Chapter 16's version is the one to tape up: "never charge for the funeral twice." Kaz's version is a model that quotes the CCC bond with a jump in the mid, a jump in the skew and a jump in the risk limit, and then wonders why the desk never wins a ticket.

### Law 7. Default is a menu, and recovery is a U

> **There are two default rates and two recovery humps. 40% is a quoting convention, and a distressed exchange is parole, not immunity.**

$$
\lambda = \lambda_H + \lambda_D,
\qquad
f_R(r) = w_{\text{in}}\,f_{\text{in}}(r) + (1-w_{\text{in}})\,f_{\text{out}}(r),
\qquad
\operatorname{Var}[R] = \underbrace{w_{\text{in}}\sigma^2_{\text{in}} + (1-w_{\text{in}})\sigma^2_{\text{out}}}_{\text{within}} + \underbrace{w_{\text{in}}(1-w_{\text{in}})\,(\mu_{\text{in}}-\mu_{\text{out}})^2}_{\text{membership alone}} .
$$

**Why it holds.** Default now arrives by two doors, hard default ($\lambda_H$) and distressed exchange ($\lambda_D$), and the headline rate adds them. In June 2025 the headline and ex-distressed-exchange rates were 5.8% and 2.1%, almost a factor of three apart on the same issuers (§14.1). Recovery in a non-pro-rata world is a mixture over coalition membership, and $w_{\text{in}}$ is the probability that *you* get the call, not the class's participation share (§5.6). Serta supplies the numbers: $w_{\text{in}} \approx 0.526$, $\mu_{\text{in}} \approx 0.74$ and $\mu_{\text{out}} \approx 0.25$ give a between-group standard deviation of about 24.5 points of par from membership alone (§14.4, illustrative reading). The exchange is not the end of the story. About a quarter of soft events end in hard default, more than 70% of those within two years (§14.3), and only 22% of coercive-LME firms avoided both re-default and bankruptcy within two years (§13.10). In CDS, finally, the swap does not pay recovery. It pays par minus the auction price of the cheapest deliverable (§24.5–24.6). In a failure to pay without acceleration, that can be half of par from a solvent company.

**Earned in** §5.5 (zero-one-inflated Beta recovery), §5.6 (default as a negotiation), §14.1–14.4 (two rates, competing risks, the re-default clock, membership). **Bites in** §6.8 and §6.13 ($s \approx \lambda(1-R)$, and $R$ is a quoting convention), §12.2 (recovery by seat: about 33% for direct loans, 52% for syndicated loans and 39% for HY bonds), §13.3 (the uptier as a recovery transfer), §16.5, §24.2, and Appendix D (the auction mechanics as reference tables).

**The violation.** Plugging 40% into every recovery field. Mags: "Price is what you pay. Recovery is what you get, eventually, after the lawyers." Law 7 adds: *which* recovery you get depends on whether the lawyers invited you.

### Law 8. Every clause is a payoff function, and one word can be the whole loss

> **Read the document as a program before you model it as a distribution. Write every clause as (outcome, trigger, price at trigger).**

$$
\text{clause} \;\mapsto\; \big(\text{outcome},\ \mathbf{1}\{A_t\},\ P_{\text{trigger}}\big),
\qquad
\Delta_j(V) = W^{\text{post}}_j(V) - W^{\text{pre}}_j(V),
\qquad
\sum_{j\,\in\,\text{creditors}} \Delta_j(V) = 0 \ \text{ when equity is out of the money}.
$$

**Why it holds.** An LMT is the difference of two waterfalls, evaluated state by state (§13.3). In the low states value is fixed, so the transaction is zero-sum among creditors: someone's gain is the excluded holder's loss, and "the liquidity story" lives only in the high states. Each standard position then has a payoff shape. An excluded lender in an uptier is short a soft digital put; the victim of a drop-down is short a forward capped at $C^{\text{unsub}}/F$ (§13.10). The 101 change-of-control put pays $\mathbf{1}\{\text{CoC} \wedge \text{downgrade}\}\,(101 - P)^{+}$, and the IG double trigger needs both inspectors (§15.2). Portability is a short digital on a number the sponsor chooses (§15.3). The words are the strikes. Serta's and Mitel's agreements differed by "open market," both cases were decided on 31 December 2024 with opposite outcomes, and the two words were worth \$261.13mm before interest at the July 2026 remand (§3.9, §14.6). The document is parsed as a typed program: definitions form a graph, baskets map the company's state to \$mm, and leakage is a max-flow whose binding baskets are the min cut (§25.2–25.4).

**Earned in** §13.2–13.3 (legal prose to state space; the uptier as a transfer), §15.1–15.3, §21.4 (the OC test is an option book written by the CLO equity), §25.2–25.4, and Chapter 12-B (which document governs which right, the amendment thresholds and sacred rights). **Bites in** §6.5 (a maintenance covenant is a Black–Cox barrier, cov-lite deleted it, and an uptier moves it for someone else), §13.6 (drop-down leakage), §16.3 (a backstop is a short put), §16.5 (a claim is long a ratio and short a call at par), §24.8 (successors: at 25.0% nothing happens, at 25.1% your swap splits), §26.4 (the citation contract), §27.3 (the security master is the credit agreement of the system).

**The violation.** Kaz once asked whether "sacred rights" required a priest. The more expensive version is the desk that fits a recovery distribution to a credit agreement it has not parsed. Theo's question, "But what does the credit agreement say?", is Law 8 asked out loud, and Law 16 is what happens when a judge answers it.

*Used in:* every Debrief bullet tagged `[L5]`–`[L8]`; Chapter 12-B (the document map that Law 8 presupposes), Chapter 18-B (the RFQ engine), Appendix D (auction and deliverables), and §E.6.

## E.4 The Tape: Laws 9–12

The data lie in four characteristic ways. The marks are smoothed (Law 9), the costs are left out (Law 10), the labels are missing (Law 11), and the number of attempts is hidden (Law 12). A backtest that survives all four has earned a small allocation. Most do not survive two.

### Law 9. A mark is a moving average of the truth

> **Stale marks shrink betas, fake lead–lag and flatter Sharpe ratios. Sum the lags and desmooth, gently, before you optimize.**

$$
r^{o}_t = \sum_{k=0}^{K}\theta_k\,r_{t-k},\quad \theta_k \ge 0,\quad \sum_{k}\theta_k = 1
\quad\Longrightarrow\quad
\sigma_o = \sigma\sqrt{\textstyle\sum_k\theta_k^2},
\quad
\beta^{o}_0 = \theta_0\,\beta,
\quad
\sum_{k}\beta^{o}_k = \beta,
\quad
\text{SR}_o = \frac{\text{SR}}{\sqrt{\sum_k\theta_k^2}} .
$$

**Why it holds.** Model the observed return as a moving average of serially uncorrelated true returns, following Getmansky, Lo and Makarov. Its variance is $\sigma^2\sum_k\theta_k^2$, which is less than $\sigma^2$ whenever more than one $\theta_k$ is positive. A regression on the contemporaneous factor captures only $\theta_0$ of the beta. The lagged coefficients hold the rest, which is why the Dimson sum restores it. The mean is unchanged, so the naive Sharpe ratio is inflated by the same factor that deflated the volatility. For AR(1) smoothing at $\phi$, $\theta_k = (1-\phi)\phi^k$ and $\sum_k\theta_k^2 = (1-\phi)/(1+\phi)$. At $\phi = 0.8$ that is $1/9$, so volatility is understated threefold (§12.11). Inversion has a price, though: unsmoothing a kernel with $\theta = 0.7$ amplifies measurement noise more than sixteen times, so pool across co-holders and report intervals (§17.10). Staleness also manufactures lead–lag. A bond that prints with probability $p$ shows a fake equity lead of about $p(1-p)\beta^{\text{ce}}$ (§10.5).

**Earned in** §8.5 (Dimson, Scholes–Williams), §17.2 (the mark as a filter), §12.5 (desmoothing in the covariance), and Chapter 17-B (the BDC mark as a moving average, and the mark gap as a signal). **Bites in** §7.1 (a mark is not a price), §10.5, §19.5 (staleness is variance, not a haircut), §20.2 (NAV is an opinion), §21.7 (desmooth loan marks before you believe a momentum backtest), §28.6 (the stop you don't know you have is the mark), Appendix B §B.8 (composites are model outputs).

**The violation.** A private-credit sleeve with a Sharpe ratio of 2 and a beta of 0.2 to anything public. Law 9 says it has a beta near 1 and a Sharpe ratio near the public one, spread over five quarters of lags. Law 11 says the brochure did not label which.

### Law 10. Costs decide, and capacity is a square

> **Turnover beyond $\alpha/2\bar c$ is charity. At the manager's favorite size the client keeps a third, and liquidity tiers bind before expected returns do.**

$$
T_{\max} = \frac{\alpha_{\text{gross}}}{2\bar c},
\qquad
\mathrm{TO}^\star = \frac{k^2}{4c^2},\quad \alpha^{\text{net}\,\star} = \frac{k^2}{4c},
\qquad
A^{*} = \frac{\mathcal{L}\,g^{2}}{18\,T^{3}\eta^{2}},\quad \alpha(A^{*}) = \frac{g}{3},\quad \alpha\big(\tfrac94A^{*}\big) = 0 .
$$

**Why it holds.** A round trip costs $2\bar c$ per unit of one-way turnover, so net alpha is positive only below $T_{\max}$ (4.6). If gross alpha is concave in turnover, $k\sqrt{\mathrm{TO}}$, the optimal turnover scales as $1/c^2$ and the optimal net alpha as $1/c$, so cheaper plumbing makes the same signal a better strategy: cutting cost from 12 to 7.5 bp buys 2.56 times the turnover (§2.9). With square-root impact, dollar alpha is $gA - \text{const}\cdot A^{3/2}$, which peaks where impact has eaten two-thirds of the spread-net edge. That is (4.2). A manager paid on assets grows on to $\tfrac94A^*$, where net alpha is zero (§4.8).

*Square or cube?* Chapter 11 says that halving turnover quadruples capacity; Chapter 4 says capacity scales as $T^{-3}$. Both are Law 10. The square is the square-root law inverted: capacity is proportional to $\big(\text{margin}/\text{impact coefficient}\big)^2$. The power of turnover depends on where turnover enters the participation rate. In §11.9 impact is charged per unit traded at a participation fixed by the trading horizon, which gives $C^\ast \propto \mathrm{TO}^{-2}$. In §4.8 participation itself scales with turnover, $2TA/\mathcal{L}$, which adds one more power, $A^* \propto T^{-3}$. Exercise E.2 asks for the general exponent.

**Earned in** §2.9 (the data-exhaust theorem), §4.7 (break-even turnover), §4.8 (capacity), §11.9, §28.3 (every signal pays its rake: $h^\ast = \ln 2 \cdot c^{\text{RT}}/\alpha_0$). **Bites in** §9.4 (momentum's break-even $c^\ast = \mathbb{E}[r^{\text{gross}}]/\text{TO}$), §9.8, §10.8, §12.7 (liquidity tiers as the binding constraint), §19.3, §24.7 (exits make the Sharpe: costs took three-quarters of the fallen-angel basis's gross Sharpe), §28.5 (the 5× is the base case: IG round-trip cost went from 0.59% to 3.40% in 2007–2008), and Chapter 10-B (what listed credit futures do to the trend sleeve's cost curve).

**The violation.** The capacity slide. Ask which size it is quoting: $A^*$, $\tfrac94A^*$, or the size at which the slide was made.

### Law 11. Label every number

> **Gross or net, simulated or live, $\mathbb{P}$ or $\mathbb{Q}$, numerator and denominator, knowledge time, and sourced or illustrative. A number without its labels is a rumor with decimals.**

$$
x \;\equiv\; \big(\,v,\ u,\ \mathbb{M},\ g,\ \ell,\ \tfrac{\text{num}}{\text{den}},\ t^{\text{known}},\ \text{src}\,\big),
\qquad
x \oplus y \ \text{is defined only if}\ \big(u, \mathbb{M}, g, \tfrac{\text{num}}{\text{den}}\big)_x = \big(u, \mathbb{M}, g, \tfrac{\text{num}}{\text{den}}\big)_y,
$$

where $v$ is the value, $u$ the unit, $\mathbb{M} \in \{\mathbb{P}, \mathbb{Q}, \text{none}\}$ the measure, $g \in \{\text{gross}, \text{net}\}$, $\ell \in \{\text{simulated}, \text{live}\}$, $t^{\text{known}}$ the time the desk could have known it, and src a citation or the word *illustrative*.

**Why it holds.** Many of the corrections in this book's own Edition 1 fact-check were wrong labels on right numbers: "filings" where the count was of transactions, a date label on the one-minute reporting rule, a CCC spread quoted against the wrong as-of date. The headline and ex-distressed-exchange default rates differ by a factor of 2.76 from the definition alone (§14.1). A portfolio-trading share of "19.8%" is a share of customer volume, and quoting it against total volume changes the trend (§2.6). A Sharpe ratio means one thing gross, simulated and pre-2010, and another net, live and post-2020 (§4.5). Systems need the same discipline. Every price carries `price_kind` and `known_at` or it does not get a badge (§27.3), and every trade keeps three clocks, `exec_ts`, `report_ts` and `knowledge_ts`, joined only on the last (Appendix B). This book obeys Law 11 on every page: *(illustrative)* and *(approx.; source: …)* are Law 11 tags.

**Earned in** §4.5 (the data stack and the replication crisis), §27.2–27.3 (provenance and the bitemporal security master), Appendix B §B.0. **Bites in** §2.6, §7.9 (timestamps are covenants), §14.1 (name the definition in the column), §25.3 (a basket without units didn't happen), §26.4 (a citation that cannot be checked is a hallucination with a footnote), Appendix C §C.3 (contested numbers, most of which are label disputes).

**The violation.** "The market is underpricing default." Which market, which default, which measure, which recovery, as of when? Most such notes are units errors (§14.10), and Law 11 finds them before Law 4 has to.

### Law 12. Count your trials

> **Deflate every Sharpe ratio by the number of things you tried, including the ones the machine tried for you.**

$$
\text{SR}^{\ast}_K \;=\; \mathbb{E}\Big[\max_{k \le K}\widehat{\text{SR}}_k\Big] \;\approx\; \sqrt{V}\,\Big[(1-\gamma_E)\,\Phi^{-1}\!\big(1 - \tfrac1K\big) + \gamma_E\,\Phi^{-1}\!\big(1 - \tfrac{1}{Ke}\big)\Big],
$$

where $K$ is the number of trials (§7.8 writes $N$; here $N$ stays reserved for breadth), $V$ is the variance of the Sharpe estimates across trials, $\gamma_E \approx 0.5772$ is the Euler–Mascheroni constant (subscripted to keep $\gamma$ for risk aversion), and $\Phi$ is the standard normal CDF.

**Why it holds.** The best of $K$ noisy estimates of a zero Sharpe ratio is positive, and extreme-value theory says how positive (Bailey and López de Prado's expected maximum, §7.8). The deflated Sharpe ratio compares the winner with $\text{SR}^\ast_K$, not with zero. *(Illustrative:)* $K = 100$ honest tries on ten years of data give $\sqrt V \approx \sqrt{1/10} \approx 0.32$ for annual Sharpe ratios near zero. The bracket is $0.4228 \times 2.326 + 0.5772 \times 2.680 \approx 2.53$, so pure noise hands you a Sharpe ratio of about 0.8. The agent's trials are your trials: deflate by the logged count, discarded ideas included, and purge by the generator's training cutoff (§26.7). The two laws reinforce each other, since every surviving signal must also survive Law 10. That is why the desk budgets for a live net IR near 0.5, not 2 (§9.12), and asks a new factor to clear roughly $t > 3$ (§7.13).

**Earned in** §7.8 (multiple testing and the deflated Sharpe ratio), §7.9 (the two biases that built the bond-factor zoo), §26.7 (agentic alpha research). **Bites in** §4.5, §7.12 (the lab reports DSR, PBO and MinTRL), §9.9 (the replication debate), and Chapter 9-B (the replication harness and false-discovery control on the 2026 signal zoo).

**The violation.** Kaz tried about 3,000 configurations and reported the winner (§7.8). ROBO tried 228 rules in §E.0 and, to its credit, reported the count.

*Used in:* every Debrief bullet tagged `[L9]`–`[L12]`; Chapter 7-B (the statistics these laws assume), Chapter 9-B (the replication audit), Chapter 17-B (marks), Appendix B (clocks and composites).

## E.5 The Clock: Laws 13–16

Credit outcomes arrive late, by a door you did not label, through sellers who had no choice, and on a date a judge picks. The four laws of the Clock are about *when* and *who decides*, which is where an RSSG banker already has the edge and a model trained on prices does not.

### Law 13. The label is the model

> **What you call an event decides what the model can learn. Label the trade you would make, use cumulative incidence rather than one minus Kaplan–Meier, and never quote a hit rate without its exclusion rate.**

$$
F_k(t) = \int_0^t h_k(u)\,S(u^-)\,du \;\;\le\;\; 1 - \exp\!\Big(-\int_0^t h_k(u)\,du\Big) \;\approx\; 1 - \widehat{\text{KM}}_k(t),
\qquad
\text{avoidance pays} \iff (\pi_X - \pi_K)\,L > s_X - s_K .
$$

**Why it holds.** Treating the competing exits (a distressed exchange, an acquisition, a refinancing at par) as censoring estimates the probability of cause $k$ in an imaginary world where the other causes cannot happen. Because the all-cause survival $S$ is no larger than the cause-$k$ survival, the naive estimate overstates $F_k$, and the bias grows with horizon (§14.2). The same logic governs labels. A triple barrier set on raw returns learns the coupon, so set the barriers in DTS space, on IDO returns, with a 13-week vertical barrier (§7.4). A PD model trained on hard defaults, in a year when distressed exchanges were 65% of defaults, is calibrated to a world that no longer exists (§11.10). And a default screen is a two-number object: with $\pi_X$ and $\pi_K$ the default probabilities of the excluded and kept bonds (Chapter 11's notation, not Law 5's informed share), exclusion pays only when the loss avoided beats the spread given up. The same 77% recall can be worth +44 bp or −9 bp depending on how much of the table you folded (§11.5).

**Earned in** §7.4 (the triple barrier in DTS space), §11.4–11.5 (hazard labels and power curves), §14.2 (competing risks), and Chapter 7-B (survival analysis in the right order: censoring, $S/F/h$, Kaplan–Meier, Cox). **Bites in** §7.5 (meta-labeling: the credit agreement picks the side, the model picks the size), §14.3 (the re-default clock), §15.5 (regulatory clocks, where $\sum_k F_k = 1 - S$ is the unit test).

**The violation.** ROBO, told to "predict defaults," labels every bond that fell below 50 as a default. The model learns to predict the 2022 rates sell-off with great confidence.

### Law 14. Censoring is the signal

> **TRACE caps, surviving bonds, filled RFQs and non-accruals are truncated samples. Model the truncation before the data, and read the truncation flag as data.**

$$
\mathcal{L}(\vartheta) \;=\; \prod_{i:\,Q_i < \bar q} f_\vartheta(Q_i)\;\prod_{i:\,Q_i \ge \bar q}\big[1 - F_\vartheta(\bar q)\big],
\qquad
\mathbb{E}\big[Q \mid Q \ge \bar q\big] = \frac{\alpha}{\alpha - 1}\,\bar q \quad (\text{Pareto tail},\ \alpha > 1).
$$

**Why it holds.** Public TRACE disseminates sizes above \$5mm (IG) or \$1mm (HY) as `5MM+` or `1MM+`, so every block contributes a survival term rather than a density. Fitting the uncapped prints alone throws away the blocks, and the blocks are the informed trades. The imputed caps imply Pareto tail indices of about $5/3$ for IG and $4/3$ for HY, and both have infinite variance (§2.2, §22.2), so never average at the cap. They do have finite means. *(Illustrative:)* a `5MM+` IG print averages $\tfrac{5/3}{2/3} \times \$5\text{mm} = \$12.5$mm and a `1MM+` HY print averages $4 \times \$1\text{mm} = \$4$mm. The cap flag is therefore itself a block flag (§18.8). The same structure appears wherever a rule selects the sample. Filled RFQs are the hands you won (Law 5). Surviving bonds manufactured part of the factor zoo (§7.9). Non-accruals carried at cost hide the fair-value mark (§17.3). And on a single bond the sample maximum sits at the price cap, so the "tail index" is the jump mass (§5.7).

**Earned in** §2.2 (TRACE is censored, not missing), §18.8 (decoding TRACE), §22.2 (the transparency ledger). **Bites in** §3.2, §5.7, §7.9, §14.2, §17.3 (the non-accrual pair hides a mark), Appendix B §B.1 (the cap follows the bond's point-in-time rating, so a downgrade changes what the tape can show).

**The violation.** Averaging trade sizes at the cap and concluding that blocks are about \$5mm. Mags: "Back in my day the tape was censored too. It was called not calling you back."

### Law 15. Forced selling is a supply schedule, not a mood

> **Fallen angels, CLO tests, ETF redemptions and post-reorg holders sell on rules you can read in advance. Price the seller, schedule the supply, and expect the discount to peak after the event.**

$$
dQ_t = -\theta\,Q_t\,dt,
\qquad
p_t = v_t - \kappa\,\frac{Q_t}{M_t},
\qquad
t_{1/2} = \frac{\ln 2}{\theta},
\qquad
s^{*} = \frac{\ln(\theta/\alpha)}{\theta - \alpha}.
$$

**Why it holds.** Overhang $Q_t$ held by constrained holders decays at execution rate $\theta$. Arbitrage capital $M_t$ arrives slowly. The log price sits below fundamental value by $\kappa$ times overhang per unit of capital, so the expected drift is predictable and positive while both are moving (§16.2.2). Fit to the published fallen-angel reversal aggregates, $\hat\theta \approx 3.4$ a year, a half-life of about 2.4 months *(illustrative fit; §16.2.3)*. If the constrained holders receive their shares or bonds with a lag at rate $\alpha$, overhang peaks at $s^{*}$, strictly after the event. Every forced seller in the book has a rule that can be read beforehand. The CLO's CCC excess above 7.5% is haircut in the OC test, and the cure is deterministic: sell the richest CCC (§21.4). The ETF's authorized participants act at the edges of the band (20.4). The post-reorg holder cannot hold equity at all (§16.1). The consequence for Law 5 is direct: a forced sale is information-free about the bond and information-rich about the seller, so $\pi$ is low and the shade is small (§1.10).

**Earned in** §16.2 (forced selling as a supply process), §21.4 (the tests as an option book), §1.8 (the ecosystem as a forced-seller flow graph). **Bites in** §11.6 (buy from forced sellers whose problem is a rating, not a balance sheet), §20.3 and §20.5 (March 2020: IG's flow term collapsed because it was the most sellable risky asset), §21.7 (condition losers on forced-seller pressure), §24.6 (bonds bounce after a large auction sell imbalance).

**The violation.** Calling forced flow "sentiment." Sentiment cannot be scheduled. A rating-driven index exit has a date, a size and a list of sellers, and the desk that wrote them down is the desk that is still bidding at month-end.

### Law 16. The court is a random variable with timestamps

> **Rulings are regime switches on known dates, applied to identifiable words. The plan value is a negotiated number. Model both that way.**

$$
\operatorname{logit}\theta_w(t) \;=\; \alpha_w + \sum_{r} J_{r,w}\,\mathbf{1}\{t \ge t_r\},
\qquad
\text{EV}^{\text{plan}} \;\ne\; \mathbb{E}^{\mathbb{P}}\big[\text{EV}\big].
$$

**Why it holds.** Let $\theta_w(t)$ be the probability that a priming transaction under wording class $w$ survives challenge, given the law as of $t$. A ruling $r$ on date $t_r$ moves the log-odds for every agreement with the same words by $J_{r,w}$. That is zero if the ruling does not touch the language, negative for Serta on `open_market_purchase`, and positive for Mitel on `bare_purchase` (§14.6.1). Because rulings are rare, the jumps are elicited priors with documented reasons, not estimates. The dates are the data. Serta and Mitel were decided on 31 December 2024 with opposite outcomes, and the Serta remand of 7 July 2026 priced the difference at \$261.13mm plus 9% New York prejudgment interest from 22 June 2020 (§14.6). The plan value is the second random variable. It is the number the classes negotiate under the threat of cramdown, not the expected enterprise value, so anchor post-reorg instruments to the price insiders actually pay in the same plan (the rights price, the direct-investment price), never to the disclosure statement's midpoint (§16.1, §16.3).

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.105:* "it is important to understand that the valuation and/or the structure and allocation of the capital structure are essentially negotiated." … "Remember that the plan valuation can be very different than the actual future value."
>
> **Annotation.** Moyer is describing negotiation inside Chapter 11, where senior creditors argue for a low valuation to "hoard" recovery and juniors threaten to contest it. The 2026 desk keeps his conclusion and changes the venue. Most of the negotiation has moved out of court into liability-management exercises (Law 7), so the timestamps that matter are increasingly rulings on contract words in LME litigation, not valuation fights at confirmation. Moyer's second sentence is also the cleanest statement of Law 4 in the restructuring shelf: the plan value is an agreed number used to allocate claims, not a forecast. Tag it accordingly, and never feed it into a $\mathbb{P}$ recovery model as an observation.

**Earned in** §14.6–14.7 (the courts as a regime variable; the Markov-switching engine), §13.9 (autopsies: the court is a random variable), §16.1 (the plan value is negotiated), and Chapters 12-B (Chapter 11 as a timed state machine) and 13-B (the litigation map as a Markov model and the maintained courts table). **Bites in** §3.7 (Serta from a market maker's blotter), §13.8 (PRS), §25.6 (the docket is an append-only event log), §27.3 (Serta's 22 June 2020 is a bitemporal test case, not an anecdote), §22.8 (the regulatory analogue: every effective date is a structural break), and Appendix C (dated courts rows).

**The violation.** A constant "legal haircut." The Ad Hoc Group, through counsel, notes that it has been on both sides of every ruling in §14.6, and that it would prefer you did not timestamp them.

*Used in:* every Debrief bullet tagged `[L13]`–`[L16]`; Chapter 7-B (survival), Chapter 12-B (the state machine), Chapter 13-B (the courts table), Chapter 17-B (redemption queues as a supply schedule), Appendix C.

## E.6 Worked Example: One Ticket, Sixteen Laws

*Friday, 2:58 p.m.* At 7:02 a.m. the second agency cut Halvorsen to BB+, and Halvorsen's bonds will leave the IG indices at month-end. An index-tracking IG fund sends an RFQ to five dealers to sell \$15mm of the Halvorsen 6% senior notes due 2031, the same bonds as Chapter 24's sticky note. The composite mid is 88.00 and the Z-spread 480 bp. Five-year CDS is at 370 bp, and the 3% 2045s, the likely cheapest-to-deliver, last printed at 52. The desk already holds \$10mm of the 2031s against \$10mm of CDS from the Chapter 24 basis trade. Theo has ninety seconds. He runs the card. *(Halvorsen is fictional; every number below is illustrative.)*

| Law | Status | The number on this ticket | What it changes |
| :-- | :-- | :-- | :-- |
| 1 IDO | Binding later | Markouts at 1, 5 and 20 days, net of CDX HY and KRD-matched Treasuries | The hand history is scored on $\epsilon$, not on price |
| 2 Issuers | Binding | New bonds join the existing Halvorsen hat; the 2031s and 2045s at $\rho \approx 0.9$ are one exposure | The issuer limit, not the line count, caps the size |
| 3 DTS | Binding | $\text{DTS} = 3.9 \times 4.80 = 18.7$ against an HY index at about 9.9: $\beta \approx 1.9$ | \$13.2mm of market value carries about \$25mm of index-equivalent beta |
| 4 Measure | Binding | $\lambda^{\mathbb{Q}} = 0.0370/0.60 \approx 6.2\%$; desk $\lambda^{\mathbb{P}} = 3.0\%$ | About 190 bp a year is risk premium: carry, not alpha |
| 5 Posterior | Binding | Rule-driven seller, $\pi = 0.10$; $\sigma_V = 4$ points; shade $\pi\sigma_V = 0.40$ | The bid is a posterior about this seller, not a house markup |
| 6 Jump once | Binding | Credit view $0.032 \times 48 \times 5/252 \approx 0.03$ points; jump variance adds about 1.2 points of s.d. | The composite already holds $\lambda^{\mathbb{Q}}$; no extra skew |
| 7 Menu, U | Binding | $w_{\text{in}} = 0.30$, humps at 65 and 20: $\mathbb{E}[R] = 0.335$, not 0.40 | JTD hedge ratio $0.545/0.665 \approx 0.82$ |
| 8 Clause | Read | Downgrade is not a change of control; the swap's deliverables include the 2045s | Hedge ratio differs by state (below) |
| 9 Mark | Binding | The 2045s' 52 is nine business days old | Issuer beta from marks is $\theta_0\beta$: use the 2031s' trades |
| 10 Costs | Binding | Expected forced-selling reversal about 1.7% (1.5 points) in a month, against a round trip of about 1.0 point | Hold about a month; hedge with the cheap-to-roll index |
| 11 Labels | Binding | 88.00 is `price_kind=composite`, `known_at=14:55`; 480 is Z, not OAS; 3.0% is $\mathbb{P}$, 12 months, model | Written on the ticket, not in Theo's head |
| 12 Trials | Background | $\pi$'s client-tier model was chosen from 40 specifications | Trust the shade to one decimal, not two |
| 13 Label | Background | "Toxic" in the $\pi$ model is a 5-day IDO markout below $-1\sigma$ | A raw-price label would call every fallen angel toxic this week |
| 14 Censoring | Binding | An 11:40 print showed `1MM+` at 87.25; at $\alpha = 4/3$ the mean block is about \$4mm | Someone sold a block today; yesterday's IG cap would have shown its size |
| 15 Supply | Binding | Index exit at month-end; $\theta \approx 3.4$ a year, half-life about 2.4 months | Do not buy all the supply today; the discount peaks later |
| 16 Court | Dormant | PRS 0.18, below the 0.35 alert line | Set the alert; Laws 8 and 16 wake when PRS crosses it |

**The bid.** Chapter 1's bid equation with the audit's terms is $B^* = 88.00 - 0.40 - 0.25 - 0.10 = 87.25$, where 0.25 is the inventory term (the existing Halvorsen position plus Law 6's jump variance) and 0.10 is the handling cost. The bid matches the 11:40 block exactly. "Either the market agrees with you," says Ines, "or the 11:40 seller was the one who knew. The tape can't tell you which. Your markouts can, in five days."

**The hedge, in two states.** Law 7 gives $N^{\text{JTD}} = (0.88 - 0.335)/(1 - 0.335) \approx 0.82$, or about \$12.3mm of protection for \$15mm of bonds. The 40% convention would have said 0.80. The difference is small. The state the convention cannot see is what Law 8 finds in the Definitions: a failure to pay on one bond without acceleration. In that state the auction is set by the 2045s near 52, so the swap pays 48 points, while the unaccelerated 2031s might fall only to about 70, a loss of 18. The ratio that hedges that state is $18/48 \approx 0.38$. The \$12.3mm hedge is roughly twice too large there, and that is the Chapter 24 lesson in one line. Theo hedges the beta with CDX HY (Law 3) and sizes the single-name protection to the bankruptcy state, with a note to revisit the decision if PRS crosses 0.35.

**What the audit shows.** On this ticket the posterior shade (0.40) is more than ten times the desk's credit view over the hold (0.03). Two-thirds of the laws bind, and the binding ones are about the seller, the units and the schedule, not about whether Halvorsen defaults. That is typical. Laws 6, 7, 8 and 16 decide what the desk loses in the tail. Laws 1–5 and 9–15 decide whether the desk earns anything in the middle.

*Used in:* `00_01_tape_to_your_monitor.md` (the issuer bible's Halvorsen entry), Chapter 18-B (the RFQ engine runs this audit automatically), Chapter 24 (the basis trade this ticket inherits), and Exercise E.4.

## E.7 Probation: Laws Waiting for a Third Debrief

A few candidates came close. They are listed so that Edition 3 can promote, merge or retire them on evidence.

- **"Silence is data."** It has its three debriefs: Chapter 15 updates the deal-break probability through quiet milestones, Chapter 25 alerts on docket silence, and Chapter 27 rules that silence is not safety. It also has an equation, Bayes on no news, $\pi_{t+\Delta} = \pi_t S_1(\Delta)\big/\big[\pi_t S_1(\Delta) + (1-\pi_t)S_0(\Delta)\big]$, where $S_j(\Delta)$ is the probability of no event over $\Delta$ under hypothesis $j$. It stays on probation because the three uses disagree about what is silent. In Chapter 15 the world is quiet, and that is information. In Chapters 25 and 27 the pipe is quiet, and that is an alarm. Edition 3 should either split it in two or merge the pipe half into Law 14, since a dead feed is just censoring with a pager.
- **"Every price has a clock"** (Chapters 7 and 27, Appendix B) has been absorbed into Law 11 as $t^{\text{known}}$. Its best line survives as a quotation: "Timestamps are covenants."
- **"Hedge less than naive"** (§8.6, after Paleologo) has one debrief and a strong derivation. It needs two more chapters to notice it.
- **"Regimes size the tilt; valuation directs it"** (§12.11, with echoes in §14.9 and §22.9) has two and a half debriefs. The half is a regulatory structural break, which may be a different animal.
- **The 13-week model** appears in six debriefs and will never be a law. It is not a sentence but a character, and it refuses to stay one thing for long enough to be promoted: a hazard curve in Chapter 6, a runway covariate in Chapter 13, a jump term in Chapter 16 and a dashboard in Chapter 28.

*Used in:* Edition 3 planning (`state/exploratory_space.md`), and the law linter's list of probationary patterns in §E.8.
