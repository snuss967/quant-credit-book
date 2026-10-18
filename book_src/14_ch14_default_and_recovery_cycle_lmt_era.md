# Chapter 14: The Default & Recovery Cycle in the LMT Era (TREND)

*Thursday, 2:40 p.m. The loan market is quiet in the way a card room is quiet right before somebody shoves.*

The RFQ arrives at 2:40: a client wants an offer on \$12mm of the Quillfeather Packaging first-lien term loan due 2029. (Quillfeather is fictional. Its history is a composite of real ones.) Fourteen months ago Quillfeather's sponsor ran a non-pro-rata uptier. A 52% majority of the first-lien lenders exchanged into a new super-priority tranche and put in \$90mm of new money. The other 48% kept their old loans, which now sit behind more than a billion dollars of debt that did not exist the week before. The agencies called it a distressed exchange, counted it as a default, and a few weeks later re-rated the company out of default. The client wants the old, excluded first lien. It was marked at 41 last night.

"So it already defaulted," says Kaz Lind. "Is it immune now? Like chickenpox?"

"It's not immune," says Mags Dunleavy. "It's on parole."

Theo Marsh has the 13-week cash flow model open, the one he still carries on a USB stick for emotional support. "The new money buys them runway to about the third quarter of next year. After that, the interest bill comes back."

Ines Okafor turns her chair a quarter turn. "What's the pot, what are the odds, and who at this table was in the majority group?"

"The pot is about \$4.9mm at 41. The odds..." Theo stops. "The odds are the problem. In 2015 I'd have looked up a recovery for a defaulted first lien and called it forty cents. But this loan has already defaulted once and it isn't in bankruptcy. Its next default could be a filing or another exchange. And its recovery depends less on the word 'first' in its name than on which side of the table its holders were sitting on in June."

"And the buyer?" Ines asks.

"Either they think the parole ends well, or they want to be inside the room for the next deal."

From offstage, the Ad Hoc Group speaks in unison, through counsel: *"We are not sellers. We neither confirm nor deny that we are buyers."*

**The question this chapter answers: what is the joint law of (time to the next default, recovery) for a credit that has already been restructured once, and how is it different from the law we all learned in 2015?**

By the end of this chapter you will be able to: read a default rate and say which of the two default rates it is; split a default intensity into competing soft and hard hazards and estimate their cumulative incidence without the classic Kaplan–Meier bias; calibrate a mixture-cure re-default clock to Moody's 2026 soft-default study; write recovery as a mixture over coalition membership and show that one binary variable can produce most of the cross-sectional dispersion the textbooks attribute to seniority and the cycle; treat cooperation agreements and court rulings as regime variables with dates; run a Markov-switching filter on the default mix; keep $\mathbb{P}$ and $\mathbb{Q}$ apart when the CDS contract and the rating agency disagree about what a default is; and hand ROBO a spec it cannot misread.

## 14.1 Two Default Rates, Two Recovery Rates

In the RSSG seat, "default" had a clear meaning. It was the day the company filed, or the day it missed a coupon and the forbearance agreement ran out. Everything before that was positioning. Everything after was a plan of reorganization, a valuation fight, and eighteen months of fee applications. Default was one absorbing state, and the recovery was whatever the plan said your class got.

The systematic desk inherits a different definition, and the gap between the two is now the most important footnote in credit.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.336:* "Distressed exchanges, on the other hand, are considered defaults whenever the debtholders are offered substitute instruments with lower coupons, longer maturities, or any other diminished financial terms."
>
> **Annotation.** Schmid is paraphrasing S&P's definition, and it was a sensible rule when distressed exchanges were rare, voluntary bond swaps that a creditor committee negotiated with the company. The rule is unchanged. What it now catches is not. An uptier, a drop-down financing, an amend-and-extend at a discount, and a PIK toggle forced through a majority vote can all be "substitute instruments with diminished terms," so all of them can be defaults, even though no court is involved, often no payment is missed, and the company is usually re-rated out of default within weeks. On a 2026 desk this sentence is the reason one company can be "in default" for Moody's, performing for its CDS, and current for its CLO manager's interest-coverage test, all on the same Tuesday. The modern desk departs from the textbook by refusing to collapse those into one flag. It carries two event types, two hazards and two recovery laws, and decides only at the end which one a given contract pays on.

Kaz, who has been reading the S&P rating scale, raises a hand. "What is a 'selective default'? Does the issuer get to pick which quarter?"

"Close," says Mags. "It gets to pick which creditors." That is the correct reading. S&P's SD, like Moody's "/LD" suffix, marks an issuer that has defaulted on a particular issue or class while it keeps paying the rest. It is the rating system's way of saying the company chose its victims.

Here is the fork the rest of the chapter is built on.

| Who is counting | Hard default (bankruptcy, missed payment) | Distressed exchange / LME | What the number is used for |
| :--- | :--- | :--- | :--- |
| Rating agencies (Moody's, S&P, Fitch) | Default | Default (S&P SD, Moody's /LD, Fitch RD) | Default studies, CLO tests, PD model training labels |
| Standard North American corporate CDS (traded without restructuring as a credit event) | Credit event (bankruptcy, failure to pay) | Generally *not* a credit event | $\mathbb{Q}$-hazards from CDS spreads (Chapter 24) |
| Bankruptcy and restructuring studies | Filing | Not counted until a filing | Legal research, "Chapter 22" counts |
| Index default trackers (e.g., LCD-style "with and without LMEs") | Default | Shown both ways | Cycle commentary |

Moody's now publishes the gap directly. In June 2025 the trailing twelve-month speculative-grade default rate for bonds and loans combined was 5.8% including distressed exchanges. Removing the 51 distressed restructurings brought it to 2.1%, "almost one-third" of the headline (Moody's Asset Management Research, *Corporate Credit Risk Looking for a Catalyst to Break Out*, 7 August 2025). Same issuers, same twelve months, a factor of almost three, and the difference is a definition.

The punchline for a model builder is uncomfortable. A probability-of-default model trained on pre-2020 labels ("filed or missed a payment") and scored against today's agency default rate will look as if it under-predicts by roughly that factor of three. It isn't miscalibrated. It is answering a different question. Mixing Moody's DE-inclusive counts, S&P's SD, Fitch's RD and a vendor's "excluding LMEs" series in one training set produces label noise that no amount of gradient boosting will find, because it isn't noise in $X$. It is noise in the definition of $y$.

> **Trend Watch.** *The soft-default takeover, 2010–2026.*
> - **Baseline.** S&P counted distressed exchanges at about 32% of rated US corporate defaults over 2010–2023, then at roughly 50% for three consecutive years to mid-2024 (S&P, *Distressed Exchanges Reached Their Highest Level Since 2009*, 15 August 2024, as cited by FTI Consulting, 9 October 2026; we could not open the S&P original).
> - **2024.** Distressed exchanges were about 63% of Moody's-rated defaults, "the highest annual share on record, with data going back to the 1980s" (Moody's AMR, 6 March 2025). LMT counts hit a high-water mark of 38 (Wachtell Lipton, *Liability Management 2026*, 3 February 2026).
> - **H1 2025.** 64% of defaults, "about the same pace as all of 2024," concentrated in loan-only, private-equity-backed capital structures (Moody's AMR, 7 August 2025).
> - **2025.** About 65% of all defaults were distressed restructurings (Moody's, 28 April 2026). LME counts fell to 24, yet LMEs were still about two-thirds of default activity by issuer count and exceeded payment defaults and bankruptcies on a rolling twelve-month basis every month of the year (Wachtell, 3 February 2026). In Moody's direct-lending proxy, the default rate was 1.6% excluding distressed exchanges and 4.7% including them.
> - **2026.** The Federal Reserve's May 2026 *Financial Stability Report* notes that defaults including distressed exchanges "remained relatively high" even as volume-weighted loan default rates sat below their median. 9fin counted 25 completed LMEs in H1 2026, against 24 in H1 2025, with coercive uptiers having "all but vanished" in favor of equity handovers and consensual amend-and-extends (9fin, 28 August 2026).
> - **What it means for the desk.** The *level* of the headline default rate is now a weak cycle signal, while the *mix* is a strong one. The count of LMTs fell after 2024; the share of defaults that are soft did not. The technique migrated rather than retreating. Any feature called `default_rate` in your warehouse needs a sibling called `default_rate_ex_de`, and the spread between them is itself a regime variable (§14.7).

How strange is a world in which most defaults happen out of court? Very, by the standards of the shelf.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.87:* "Given the relative simplicity of the out-of-court restructuring, one might well wonder why it is successfully employed less than 10% of the time."
>
> **Annotation.** Moyer was writing in 2004, and his answer was the holdout problem: an exchange offer needed very high participation (he cites thresholds of 85–90% elsewhere in the book), and any holder who refused kept a full claim against a company that the others had just de-levered. Twenty years later, out-of-court restructuring is the *majority* outcome. The holdout problem was not solved by better persuasion. It was solved by contract technology that turned holdouts into victims: if a bare majority can amend the credit agreement, subordinate the minority, or move the collateral to an unrestricted subsidiary, then holding out stops being a free option and becomes a short put. That inversion is the whole LMT era in one sentence, and it is why the 2004 base rates in every distressed textbook are the wrong prior for 2026.

Mags, who remembers 2004 as "recent," takes the long view. "We used to call it a coercive exchange, and it needed ninety percent to work. Now it needs fifty point one percent and a dictionary." She pauses. "The Fifth Circuit, to its credit, eventually bought a dictionary too." (We get to that ruling in §14.6.)

The recovery side has forked the same way. Measured *at the exchange*, recoveries on distressed exchanges look excellent: Moody's put first-lien DE recoveries at 71% at end-2024, up from 55% in 2023 (as reported by Bloomberg Law, *Distress Exchange Leads to Re-Default Half the Time*, 23 April 2025). Measured *at the eventual bankruptcy*, first liens of companies that had done an LME recovered far less. PitchBook, summarizing a Fitch study of 2024 emergences, reported weighted-average first-lien recoveries of 23% for issuers with a prior LME against 53% for those without. We could not open the Fitch original, so treat the pair as indicative rather than gospel. The two numbers are not contradictory. The first is measured at a moment chosen by the borrower, for holders who were in the deal. The second is measured at the next event, which is where the excluded holders' losses and the participants' second haircut actually show up. A recovery database that records only the first number has a survivorship bias with a lawyer.

So "the default rate" is now two numbers, and "the recovery rate" is now at least two distributions. The rest of the chapter builds the machinery to carry both.

### Deep-Dive Resource Graph (§14.1)

- **Practitioner Writing.** Moody's Asset Management Research, *Corporate Credit Risk Looking for a Catalyst to Break Out* (7 August 2025): https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf. Moody's AMR, *"Growth Recession" Hounds Parts of Corporate Credit Market* (6 March 2025): https://www.moodys.com/web/en/us/insights/resources/growth-recession-hounds-parts-of-corporate-credit-market.pdf. Wachtell Lipton, *Liability Management 2026: For Better or Worse* (3 February 2026): https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf.
- **Academic Papers.** Franks & Torous (1994), *A Comparison of Financial Recontracting in Distressed Exchanges and Chapter 11 Reorganizations*, Journal of Financial Economics 35. Altman & Karlin (2009), *The Re-emergence of Distressed Exchanges in Corporate Restructurings*, Journal of Credit Risk.
- **Data & Code.** Federal Reserve, *Financial Stability Report* (May 2026), Figure 2.9 (default rates including distressed exchanges): https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf.

## 14.2 Splitting the Default Intensity: Competing Risks

Every credit model in this book so far has consumed one default intensity, $\lambda_t$. The LMT era asks us to split it. The tool is competing-risks survival analysis, which epidemiologists use when a patient can die of more than one thing, and which credit people should use because a borrower can now default in more than one way.

### 14.2.1 Cause-specific hazards and cumulative incidence

Work under the physical measure $\mathbb{P}$ throughout this section, with time $t$ in years. Let $\tau$ be the time of the *first* credit event and $K \in \{H, D\}$ its type: $H$ for a hard default (bankruptcy or payment default) and $D$ for a distressed exchange or LME. In the simulation of §14.7 we add a third exit, $C$, for "cured or refinanced away," which is not a default but does remove the issuer from the risk set. The cause-specific hazard of type $k$ is

$$
\lambda_k(t) = \lim_{h \downarrow 0} \frac{\mathbb{P}(t \le \tau < t+h,\ K = k \mid \tau \ge t)}{h},
\qquad
\lambda(t) = \sum_k \lambda_k(t).
$$

Each $\lambda_k(t)$ is the instantaneous rate of type-$k$ events among issuers that have had no event yet. The all-cause survival function is

$$
S(t) = \mathbb{P}(\tau > t) = \exp\!\left(-\int_0^t \lambda(u)\,du\right).
$$

The object a desk actually wants is the probability that the first event happens by $t$ *and* is of type $k$. This is the cumulative incidence function (CIF), also called the sub-distribution function:

$$
F_k(t) = \mathbb{P}(\tau \le t,\ K = k) = \int_0^t S(u^-)\,\lambda_k(u)\,du.
$$

Read the integrand from left to right: you must survive to just before $u$, and then a type-$k$ event must occur in $[u, u+du)$. Summing over causes gives the identity that every implementation should assert:

$$
\sum_k F_k(t) + S(t) = 1 .
$$

To see it, note $\sum_k \lambda_k = \lambda$ and $\frac{d}{du}S(u) = -\lambda(u)S(u)$, so $\sum_k F_k(t) = \int_0^t \lambda(u)S(u)\,du = 1 - S(t)$.

With constant hazards the integral is elementary:

$$
F_k(t) = \frac{\lambda_k}{\lambda}\left(1 - e^{-\lambda t}\right),
\qquad
\text{DE share} = \lim_{t\to\infty}\frac{F_D(t)}{F_H(t) + F_D(t)} = \frac{\lambda_D}{\lambda_H + \lambda_D}.
$$

With constant hazards the share is the same at every horizon, not only in the limit. A 65% DE share therefore says $\lambda_D/\lambda_H = 0.65/0.35 \approx 1.86$: soft defaults arrive almost twice as fast as hard ones.

Now put Moody's June 2025 numbers through it. Twelve-month default rates are fractions of an issuer cohort, not intensities, so convert first: $\lambda \approx -\ln(1 - 0.058) = 0.0597$ per year. The ex-DE rate is 2.1% of 5.8%, so the DE share is $3.7/5.8 \approx 0.64$. Splitting the intensity in the same proportion gives $\lambda_D \approx 0.038$ and $\lambda_H \approx 0.022$ per year *(approx.; a two-cause conversion of agency rates that ignores within-year timing and withdrawn ratings)*. These are the two numbers we will carry for the rest of the chapter.

### 14.2.2 Estimating CIFs without fooling yourself

Given an event table with times $t_1 < t_2 < \dots$, let $n_i$ be the number at risk just before $t_i$ and $d_{k,i}$ the number of type-$k$ events at $t_i$. The Nelson–Aalen estimator of the cumulative cause-specific hazard is

$$
\hat\Lambda_k(t) = \sum_{t_i \le t} \frac{d_{k,i}}{n_i},
$$

and the Aalen–Johansen estimator of the CIF is

$$
\hat F_k(t) = \sum_{t_i \le t} \hat S(t_i^-)\,\frac{d_{k,i}}{n_i},
\qquad
\hat S(t_i) = \hat S(t_i^-)\left(1 - \frac{\sum_k d_{k,i}}{n_i}\right).
$$

The identity $\sum_k \hat F_k + \hat S = 1$ holds exactly at every jump time, for the same reason as in continuous time: each step moves mass $\hat S(t_i^-)\sum_k d_{k,i}/n_i$ out of survival and into the CIFs. If your implementation fails that assert, it has a bug, not a rounding problem.

Four places where intelligent people get this wrong:

1. **The Kaplan–Meier trap.** The tempting shortcut is to estimate the DE probability as $1 - \widehat{\mathrm{KM}}_D(t)$, treating hard defaults as censored. That estimates $1 - \exp(-\int_0^t \lambda_D)$, the probability of a DE *in a world where hard defaults cannot happen*. Since hard defaults do happen and remove issuers before they can exchange, $1-\widehat{\mathrm{KM}}_D(t) > F_D(t)$ for every $t>0$, and the bias grows with horizon. It is the statistical equivalent of a recovery analysis that assumes the uptier never happened. Our code asserts the inequality so that nobody "simplifies" the estimator later.
2. **Regressing on the wrong hazard.** A Cox model fit to $\lambda_D$ tells you how covariates move the *rate* of DEs among survivors. It does not tell you how they move the *probability* of eventually having a DE, because a covariate that raises $\lambda_H$ also lowers $F_D$ by removing issuers early. If the question is "does a sponsor-owned, loan-only capital structure raise the chance that this company's first default is an exchange?", the right tool is the Fine–Gray model on the sub-distribution hazard (Fine & Gray, 1999). Candidate covariates: `sponsor_backed`, `loan_only_structure`, `docs_vintage` (pre- or post-Serta-blocker), `coop_in_place`, and the Priming Risk Score from Chapter 13.
3. **Rates are not hazards.** Agency default rates are issuer-count fractions over trailing twelve months, with withdrawn ratings handled by agency-specific rules. Convert them with $-\ln(1-\text{rate})$ before you put them next to a CDS-implied intensity, and keep the two causes separate when you do (§14.7.3).
4. **Count-weighted versus dollar-weighted.** Moody's notes that in June 2025 the default *count* fell while the *dollar volume* more than doubled. A DE share computed by count and one computed by dollars can differ by tens of points in a single month. State which one you are using, in the column name.

Kaz has been listening with growing alarm. "So the soft default is a default with a bedside manner."

"It's a default that sends flowers," says Mags. "The hard one sends the bill."

The code for these estimators lives in the chapter's reference engine (§14.7, functions `nelson_aalen_cause` and `aalen_johansen`), together with the sanity checks that keep them honest. Before we write it, we need the piece that makes the LMT era genuinely new: what happens *after* the first event.

## 14.3 The Re-Default Clock: Survival After a Soft Default

Mags's word in the cold open was "parole," and it is the right model. A paroled prisoner is out, but on a different clock from someone who was never convicted. The violations cluster early, and the people who make it through the first couple of years mostly stay out.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.682:* "Default, for example, is a quite reasonable description of an absorbing state."
>
> **Annotation.** In a rating-migration Markov chain, default is the state you never leave, and for a Chapter 11 liquidation or a long reorganization that is still a fine approximation. A distressed exchange breaks it. The issuer is re-rated out of SD within weeks, its loans keep trading, and it rejoins the performing universe with a new capital structure and a new hazard. The modern desk keeps Bolder's chain but adds a *transient* post-exchange state whose exit rates depend on time since entry. That makes the process semi-Markov rather than Markov. It is not a technicality: a model that treats the exchange as absorbing books the loss once and then stops watching the name, which is exactly when the second loss arrives.

### 14.3.1 The state space

Write the issuer's life as a semi-Markov process on five states:

```text
             λ_H                       h_H(u)
  Performing ─────────► Hard default ◄──────── On parole (post-DE, clock u)
  (never LME'd) ──λ_D──────────────────────────►    │   │
       │                                            │   └─ h_D(u) ─► second DE (max_de = 2)
       └─ λ_C ─► Cured / refinanced                 └─ h_C(u) ─► Cured / refinanced
```

From Performing, the competing hazards of §14.2 apply. On entering Parole at the exchange date, a new clock $u$ starts at zero, and the exits are a hard-default hazard $h_H(u)$, a repeat-exchange hazard $h_D(u)$, and a cure (refinanced at par, acquired, or upgraded out of distress). A production engine caps the number of exchanges at two, to keep the state space finite, and documents the cap. The reference engine in §14.7 is leaner still: it simulates only the hard-default exit from parole, and folds repeat exchanges into the choice of $p$ (fact 2 below).

### 14.3.2 A mixture-cure clock, calibrated to Moody's

The facts to match come from Moody's soft-default study of 1,173 borrowers in its Default & Recovery Database, 1979–2026 (David Hamilton, *Lend, Extend, and Then?*, Moody's, 18 May 2026):

1. About one in four soft credit events ended in a hard default.
2. More than one in three ended in a hard default *or* another distressed event.
3. More than 70% of the eventual hard defaults happened within two years.
4. After year five, the cumulative hard-default rate rises by fewer than half a percentage point per year, and roughly two-thirds of borrowers had no hard default or repeat event within a decade.

Facts 1 and 4 together say that a large fraction of borrowers are, in effect, *never* going to hard-default. An exponential or plain Weibull clock cannot represent that, because its eventual default probability is always one. The natural model is a mixture-cure (Boag–Farewell) survival function for $U$, the time since the exchange:

$$
\mathbb{P}(U > u) = (1-p) + p\,S_0(u),
\qquad
S_0(u) = \exp\!\left[-(u/\eta)^k\right],
$$

where $p \in (0,1)$ is the "susceptible" fraction that will eventually hard-default, and $S_0$ is a Weibull survival function with shape $k>0$ and scale $\eta>0$ (years) that applies only to the susceptible. Writing $f_0(u) = \frac{k}{\eta}\left(\frac{u}{\eta}\right)^{k-1} S_0(u)$ for the Weibull density, the population hazard is

$$
h_H(u) = \frac{p\,f_0(u)}{(1-p) + p\,S_0(u)} .
$$

As $u \to \infty$, $S_0 \to 0$ and $h_H(u) \to 0$: the survivors are increasingly the cured, which is fact 4 in hazard form.

**Calibration.** Fact 1 sets $p = 0.25$ for hard default (use $p \approx 0.35$ to $0.40$ if your event is "hard default or another DE," which is fact 2). Fact 3 says the fraction of eventual defaulters who default by $u=2$ is $0.70$:

$$
\frac{F(2)}{p} = 1 - S_0(2) = 0.70
\;\Longrightarrow\;
\left(\frac{2}{\eta}\right)^k = -\ln 0.30 = 1.204
\;\Longrightarrow\;
\eta = \frac{2}{1.204^{1/k}} .
$$

So fact 3 pins $\eta$ once $k$ is chosen. Fact 4 then pins $k$, which is the part people get wrong. The increase in cumulative incidence over year six is $p\,[S_0(5) - S_0(6)]$:

| Shape $k$ | Scale $\eta$ (years) | Hazard among the susceptible | Year-six increment $p\,[S_0(5)-S_0(6)]$ | Consistent with fact 4? |
| :--- | :--- | :--- | :--- | :--- |
| 0.7 | 1.53 | decreasing | 0.68 pp | No |
| 1.0 | 1.66 | constant, 0.60/yr | 0.56 pp | Borderline |
| 1.2 | 1.71 | increasing | 0.39 pp | Yes |

The intuitive guess is a decreasing hazard ($k<1$): the weakest credits fail first. The Moody's facts reject it. Given that a quarter fail eventually and 70% of those go within two years, a decreasing-hazard Weibull leaves too much mass in the long tail. The data want $k$ at or slightly above one, and that has an economic reading every RSSG banker will recognize. Among the susceptible, the hazard starts *low* and *rises*, because the exchange bought runway. Defaults come when the new money runs out, not the morning after the closing.

That is where the 13-week model comes back from the dead. In a hazard regression the covariates enter through the cure fraction and the scale:

$$
\operatorname{logit} p_i = \mathbf{x}_i^\top \boldsymbol\beta_p,
\qquad
\ln \eta_i = \mathbf{x}_i^\top \boldsymbol\beta_\eta,
$$

with $\mathbf{x}_i$ containing `liquidity_runway_weeks` (literally the output of Theo's USB stick), `new_money_fraction`, `maturity_extension_years`, `lme_type` (uptier, drop-down, amend-extend-and-exchange), `sponsor_backed`, `coop_in_place`, and `docs_vintage`. The runway variable should raise $\eta$ (later failures) and the new-money variable should lower $p$ (fewer failures). Maturity extension on its own should do little to either. An amend-and-extend that adds no new money moves the cliff three years to the right and leaves the car in the same gear.

Three ways to get this wrong:

- **Right-censoring.** Exchanges done in 2024 and 2025 have one or two years of follow-up. A naive estimate of $p$ that counts "no hard default yet" as "cured" is biased low, badly, for exactly the cohort you care about.
- **Identifiability.** With short follow-up, a small $p$ with a long $\eta$ and a large $p$ with a short $\eta$ fit the early data equally well. Fix $k$, or put a prior on it from the long-run study, and let the recent cohort move $p$ and $\eta$ only.
- **Left truncation.** If your sample is "issuers still in the database when it began," early failures are missing. Enter each issuer at its exchange date, not at the sample start.

> **Ways This Blows Up.** *What ROBO built from the vague version.* Asked to "model time to re-default," ROBO fit an exponential to a sample with fourteen months of follow-up. It reported a hazard of about 0.11 per year and an expected time to hard default of more than nine years, with a straight face. Both halves are wrong, in opposite directions. The exponential has no cure fraction, so it implies that about two-thirds of the cohort hard-defaults within a decade, against Moody's quarter. And it smears the defaults that do happen, which are front-loaded, across a decade. The fix is not a better optimizer. It is a model with a parameter for "never," plus a spec that says so (§14.7).

> **Trend Watch.** *The re-default ledger, 2020–2026.*
> - **Long-run baseline.** Of 1,173 soft-event borrowers since 1979, about one in four hard-defaulted and more than 70% of those did so within two years (Moody's, 18 May 2026).
> - **The 2023 cohort ran hot.** About 46% of 2023 distressed exchanges had already re-defaulted by April 2025, most in under a year, against a historical average of about 3.5 years (Moody's, as reported by Bloomberg Law, 23 April 2025). That figure counts repeat exchanges as re-defaults.
> - **Coercive LMEs run hotter.** In 89 coercive non-pro-rata LMEs, fewer than half avoided bankruptcy or re-default within one year and only 22% within two. Of the firms with at least two years of history, 56% had filed, and LME debtors spent two to three times longer in bankruptcy than prepackaged cases (Roe & Rotaru, Harvard Law School Bankruptcy Roundtable, 24 February 2026).
> - **The CLO view.** After an LME, 33% of issuers filed for bankruptcy, 56% re-defaulted or were rated CCC+ or below, and 10% repaid or reached B- or better (S&P BSL CLO research, as cited by Wellington, 1 April 2026; secondary).
> - **The names.** Serta: uptier closed 22 June 2020, Chapter 11 on 23 January 2023, about 31 months. Mitel: uptier October 2022, Chapter 11 on 10 March 2025, about 29 months. Wesco/Incora: notes transaction March 2022, Chapter 11 on 1 June 2023, about 15 months. Robertshaw: 2023 LME, Chapter 11 on 15 February 2024. Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 on 1 July 2025, about 11 months. Filing dates are from the S.D. Tex. and D.N.J. dockets.
> - **What it means for the desk.** The headline numbers (25%, 46%, 22% survival) look contradictory and are not. They differ in the event definition (hard only, or hard plus repeat exchange) and in the cohort (all soft events since 1979, a stressed vintage, or coercive deals only). Each is a valid estimate of a different $p$. The desk's job is to condition on deal type and vintage, not to pick the scariest headline. The 38 LMTs of 2024 are inside the two-year window now.

### 14.3.3 Expected loss when the path has a soft default in it

Put the pieces together over a horizon $T$. Let $L_H = 1 - R_H$ be the loss given a hard default with no prior exchange. Let $L_D$ be the immediate economic haircut at the exchange, defined as one minus the value of what you hold right after it, as a fraction of par. Let $L_{H\mid D}$ be the loss on a hard default *after* an exchange, applied to the value that remains. Let $G(v) = p\,[1 - S_0(v)]$ be the probability of a post-exchange hard default within $v$ years. Then

$$
\mathrm{EL}(T) = F_H(T)\,L_H \;+\; \int_0^T S(u)\,\lambda_D\Big[L_D + (1 - L_D)\,L_{H\mid D}\,G(T-u)\Big]\,du .
$$

The first term is the old world. The second integrates over the exchange date $u$: survive to $u$, exchange at rate $\lambda_D$, take the haircut, and then risk a second loss on what is left with the re-default clock running for the remaining $T-u$ years. Replacing $G(T-u)$ by a constant $q$ gives the back-of-envelope version, $\mathrm{EL}(T) \approx F_H(T)L_H + F_D(T)\,[L_D + (1-L_D)\,q\,L_{H\mid D}]$.

Run the envelope version with $\lambda_H = 0.022$, $\lambda_D = 0.038$, $T = 3$, so $F_H(3) = 0.060$ and $F_D(3) = 0.104$. Take $L_H = 0.47$ and $L_{H\mid D} = 0.77$ (the 53% and 23% Fitch recoveries above) and $q = 0.25$. All of it is *illustrative*.

| Holder | $L_D$ | Three-year EL |
| :--- | :--- | :--- |
| Majority side (exchanged at 74, the Serta first-lien ratio) | 0.26 | 7.0% |
| Excluded side (marked at 25, the Serta remand value) | 0.75 | 11.2% |
| Blended at a 52.6% chance of being inside | 0.49 | 9.0% |
| Naive single-state model: 16.5% default probability × 47% LGD | n/a | 7.7% |

The naive model is wrong on average, understating the blended loss by more than a point, and wrong in the cross-section, where the two sides of the same class are four points apart over three years. The exact integral gives slightly lower numbers, because an exchange in year 2.9 has little time to re-default before $T$. Our engine computes both. The four-point gap comes almost entirely from one variable, and the next section is about that variable.

## 14.4 Recovery Is a Mixture over Coalition Membership

The recovery models on the shelf index $R$ by seniority, industry, and the cycle. They also assume something the LMT era has broken.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.357:* "Its precise distribution is not given, but it is assumed to be independent of default and any other recovery events."
>
> **Annotation.** Bolder is describing the standard industrial assumption that recovery is an independent draw. In a non-pro-rata transaction, recovery is not a draw at all. It is the outcome of a negotiation in which the participants' recovery is funded, in part, by the non-participants' loss. The two are negatively dependent by construction, within the same class, on the same day. Independence also fails across time: the exchange that sets your recovery also resets your re-default clock (§14.3). A 2026 desk keeps the Beta machinery from Chapter 5 but replaces the single draw with a mixture whose weights are a model output.

### 14.4.1 Two humps, not one bell

Let $\pi = \mathbb{P}(\text{holder is in the majority group})$. Conditional on a default event in which classmates are treated differently,

$$
R \sim \pi\,\mathrm{Beta}(a_{\text{in}}, b_{\text{in}}) + (1-\pi)\,\mathrm{Beta}(a_{\text{out}}, b_{\text{out}}),
$$

with group means $\mu_g = a_g/(a_g+b_g)$ and variances $\sigma_g^2 = \mu_g(1-\mu_g)/(a_g+b_g+1)$. Let $M$ be the membership indicator. The law of total variance, $\mathrm{Var}[R] = \mathbb{E}[\mathrm{Var}(R\mid M)] + \mathrm{Var}(\mathbb{E}[R\mid M])$, gives

$$
\mathbb{E}[R] = \pi\mu_{\text{in}} + (1-\pi)\mu_{\text{out}},
\qquad
\mathrm{Var}[R] = \underbrace{\pi\sigma_{\text{in}}^2 + (1-\pi)\sigma_{\text{out}}^2}_{\text{within groups}} + \underbrace{\pi(1-\pi)(\mu_{\text{in}} - \mu_{\text{out}})^2}_{\text{between groups}} .
$$

The between-group term is the variance of a Bernoulli($\pi$) scaled by the squared gap in means. It is largest at $\pi = 1/2$, which is where a bare-majority uptier sits by design.

Now put Serta in. On the facts recited in the July 2026 remand opinion, participating lenders held about \$992mm of a \$1.887bn first-lien class, so $\pi \approx 0.526$. They exchanged at 74 cents, so $\mu_{\text{in}} \approx 0.74$, and the court valued the excluded loans at \$0.25, so $\mu_{\text{out}} \approx 0.25$. (Reading the exchange ratio and the court's valuation as "recoveries" is our *illustrative* interpretation.) Then $\mathbb{E}[R] \approx 0.51$, and the between-group variance is

$$
0.526 \times 0.474 \times (0.74 - 0.25)^2 \approx 0.0599,
\qquad
\sqrt{0.0599} \approx 0.245 .
$$

A standard deviation of about 24.5 points of par, *from membership alone*, before any within-group noise.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.103:* "The table supports our opinion that recovery rates decrease during recessions and increase during expansions."
>
> **Annotation.** The table is Moody's 1970 to Q2 2002 recovery data via Schuermann: mean recovery 27.85% in recessions (standard deviation 25.67%), 43.10% in expansions (27.11%), and 40.07% overall (27.50%). That is the classic regime shift in recovery, and it is real: the macro state moves the mean by about fifteen points. Compare our Serta arithmetic. One binary variable moves the mean by 49 points, and its between-group variance of 0.0599 is about four-fifths of the *entire* variance of the 1970–2002 recovery distribution ($0.275^2 \approx 0.0756$). One deal is an illustration, not an estimate. The structural point survives: the LMT era added a second regime axis, orthogonal to the cycle, and on it the regimes are further apart.

Ines puts it in her terms. "A 40% average recovery with a 25-point standard deviation isn't a distribution. It's two distributions that were introduced at a conference."

What does the trend in $\mu_{\text{out}}$ look like? The early uptiers were winner-take-all: Octus measured 100% of value moved away from non-ad-hoc creditors in Wesco, Mitel and Robertshaw, while the six most recent of its eleven non-pro-rata uptiers averaged about 18% (Octus, 16 July 2024). In ConvergeOne, minority lenders' recoveries were about 30% lower than the majority's within the same class (Harvard Law School Bankruptcy Roundtable, 25 November 2025). The market moved from "the minority gets nothing" toward "inclusive but unequal." In mixture terms, $\mu_{\text{out}}$ rose and the gap shrank, but it did not close. "Recovery compression" is the wrong name for what happened. The averages compressed while the distribution split into two humps.

### 14.4.2 The new first stage

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.305:* "However, in our own research, we have found that they account for only about 40 percent of the power we are able to attain in predicting levels of recoveries."
>
> **Annotation.** "They" are lookup tables of historical recoveries by seniority and industry. Bohn and Stein's point was that a model with firm and market covariates does far better than the table. On a 2026 desk the gap is wider, because the most predictive covariate is not in any table: which side of the room you were on. The same authors recommend a two-stage LGD model, a probit for whether any loss occurs given default followed by a regression for its size (p.316). The LMT era adds a stage *before* those two.

The engine becomes a three-stage model:

1. **Stage 0, membership.** $\pi_i = \operatorname{logit}^{-1}(\mathbf{z}_i^\top\boldsymbol\gamma)$, a logistic model for the probability that holder $i$'s position ends up inside the deal. Its features are the RSSG instincts made explicit: position size relative to the class, holder type (CLO, multi-strategy fund, distressed specialist, bank), co-op membership and type (§14.5), whether the holder has been in a prior group with the same sponsor's advisers, and the CLO share of the class.
2. **Stage 1, any loss.** A probit for $\mathbb{P}(L > 0 \mid \text{default}, M)$, as in Bohn–Stein, now conditional on membership.
3. **Stage 2, severity.** A Beta regression for $L \mid L > 0, M$, with the zero- and one-inflation masses of Chapter 5 given membership-specific weights.

Stage 0 is not a portfolio-level number. It is a property of the *holder*, so the same loan has a different expected recovery in different hands. That sounds like heresy until you remember that it is what the Serta remand court computed in dollars.

### Deep-Dive Resource Graph (§14.3–14.4)

- **Practitioner Writing.** Moody's (David Hamilton), *Lend, Extend, and Then?* (18 May 2026): https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html. Octus, *Reorg's Analysis of 11 Non-Pro Rata Uptiers* (16 July 2024): https://octus.com/resources/articles/reorgs-analysis-of-11-non-pro-rata-uptiers/. Roe & Rotaru, *Liability Management's Limited Runway*, HLS Bankruptcy Roundtable (24 February 2026): https://bankruptcyroundtable.law.harvard.edu/2026/02/24/liability-managements-limited-runway-corporate-restructuring-today/.
- **Academic Papers.** Boag (1949) and Farewell (1982) on cure models. Altman, Brady, Resti & Sironi (2005), *The Link between Default and Recovery Rates*, Journal of Business 78(6). Jankowitsch, Nagler & Subrahmanyam (2014), *The Determinants of Recovery Rates in the US Corporate Bond Market*, Journal of Financial Economics. Schuermann (2004), *What Do We Know About Loss Given Default?*
- **Data & Code.** Moody's Default & Recovery Database (vendor; the source of the 1,173-borrower study). CourtListener REST API for filing dates and dockets: https://www.courtlistener.com/help/api/.

## 14.5 Cooperation Agreements: The Lender Cartel as a Repeated Game

If $\pi$ is the variable that matters, lenders will try to control it. The instrument they found is the cooperation agreement: a contract among holders of a class to negotiate with the company only as a group, often with restrictions on selling to anyone who will not sign.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.86:* "However, as in poker, which is analogous because the “multiple-hand” format of the game is similar to the series of transactions in the distressed marketplace, to be effective one must have a credible “bluff.”"
>
> **Annotation.** Moyer's context is the holdout problem (p.85): non-participants can do better than participants, "but if too many hold out, all will be worse off." His solution in 2004 was reputation among "the regulars" of a repeated game. The co-op replaces reputation with a contract. Instead of each lender building a credible bluff over many hands, the class signs a document that makes the bluff binding today. What Moyer could not anticipate is the borrower's counter: if the table agrees not to be bluffed, the sponsor goes looking for a different table, through drop-downs and deals with outside lenders that need no vote from the class at all.

> **Poker Table.** Ines draws it on the whiteboard. "A non-pro-rata uptier is a game where the sponsor needs a majority to call. Without a co-op, every lender is thinking, 'If I fold and the others call, I'm the one who gets primed.' So everybody races to call first. A co-op is the table agreeing not to be bluffed. The sponsor's response is to find a new table." The hand history: in the Serta deal of June 2020, the excluded lenders' loans were marked at about 25 cents at the closing, on the remand court's findings. That is the markout on not being in the room.

### 14.5.1 The threshold game with a co-op

Let a non-pro-rata amendment need participation of at least a fraction $m$ of the class (for a "Required Lenders" vote, $m$ is just over one half). Let a co-op cover a fraction $c \in [0,1]$ of the class, split among $n$ members of roughly equal size $c/n$.

- If $1 - c \ge m$, the sponsor can build a majority entirely outside the co-op, and the co-op is decorative.
- If $1 - c < m$, the co-op holds a blocking position. A deal needs co-op members to defect with a combined share of at least $m - (1-c) = m + c - 1$, which takes

$$
d^\ast(c) = \left\lceil \frac{n\,(m + c - 1)}{c} \right\rceil
$$

defectors. If each member defects independently with probability $\varphi$, the probability that the co-op breaks is a binomial tail:

$$
\Pi(c) = \mathbb{P}\big(\mathrm{Bin}(n, \varphi) \ge d^\ast(c)\big).
$$

With $m = 0.501$, $n = 10$, $c = 0.70$ and $\varphi = 0.10$ (all *illustrative*), $d^\ast = \lceil 2.87 \rceil = 3$ and $\Pi \approx 7.0\%$. Raise coverage to $c = 0.90$ with $n = 15$, and $d^\ast = 7$ and $\Pi \approx 0.03\%$. Coverage above the blocking line turns a coin flip into a tail event. At Optimum's reported co-op coverage of about 99% (below), nearly half the co-op would have to defect.

The hazard of a non-pro-rata LME then factors into a contract term, a coalition term, and an escape hatch:

$$
\lambda_{\text{NPR}}(t) = \lambda_0(t)\,\theta_w(t)\,\big[\mathbf{1}\{1-c \ge m\} + \mathbf{1}\{1-c < m\}\,\Pi(c)\big] \;+\; \lambda_{\text{away}}(t),
$$

where $\lambda_0$ is baseline distress intensity, $\theta_w(t)$ is the probability that a priming deal under document wording $w$ survives legal challenge (§14.6), and $\lambda_{\text{away}}$ is the hazard of transactions that need no class vote: drop-downs into unrestricted subsidiaries within basket capacity and financings from new lenders "away" from the group.

Two refinements carry most of the realism.

**Defection is not a coin flip. It is a price.** The independent-$\varphi$ model is the co-op's best case. A sponsor who offers the cheapest $d^\ast$ members a backstop fee or a better exchange ratio makes defection correlated and deliberate. The "carve-out" co-op, which pre-authorizes some disparate treatment such as backstop fees and advantaged exchange ratios, is the market's mechanism-design answer. It prices the side payment in advance so that it does not break the coalition (Seaton, HLS Bankruptcy Roundtable, 14 April 2026).

**Transfer restrictions change the arrival process of defectors.** Without them, every secondary trade can bring in a buyer who has not signed, and $c$ decays with turnover. With them, a buyer must join, and $c$ is roughly constant. On the desk this matters for liquidity. A co-op'd loan trades only to buyers willing to sign, so the bid side gets thinner exactly when the CLO sellers arrive.

> **Trend Watch.** *Co-ops, from four a year to forty-five.*
> - **Counts.** About 45 co-op agreements were signed in the US in 2024, against an average of about four a year over 2018–2023, a figure 9fin notes was cited in Optimum's antitrust complaint (9fin, *A Crash Course on Co-ops*).
> - **Variants.** Offensive, defensive, and carve-out co-ops, with carve-out the fastest-growing. In event studies, equity reacts negatively to co-op announcements and firm value rises modestly (Seaton, HLS Bankruptcy Roundtable, 14 April 2026).
> - **Borrower countermeasures.** "Anti-cartel" provisions appeared in Warner Bros. Discovery's 2025 bonds, and borrower NDAs aimed at group formation "met significant market resistance" (Seaton, 2026).
> - **The bellwether.** CSC Holdings, Optimum's subsidiary, has about \$21.8bn of debt, and a June 2024 co-op claims about 99% of it. On 1 June 2026 Optimum moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco" and raised \$300mm of preferred (Optimum 8-K, 1 June 2026). Its Q2 2026 10-Q carries a going-concern warning, with \$4.12bn maturing in April 2027 and \$2.225bn in July 2027.
> - **The antitrust front.** Optimum (f/k/a Altice USA) and CSC Holdings sued the co-op lenders in the S.D.N.Y. under the Sherman Act, alleging price-fixing and a group boycott. The complaint alleges the co-op lenders hold 88% of a "Leveraged-Finance Market" it defines itself (Cleary Gottlieb, *Cooperation, Not a Cartel*, 18 December 2025). Defenses include rule-of-reason analysis, market definition, and *Sharon Steel v. Chase Manhattan* (2d Cir. 1982). Similar challenges (Optimum, Selecta) were "in their early days" in early 2026 (Wachtell, 3 February 2026).
> - **Europe.** Baker McKenzie's January 2026 leveraged finance report describes "a growing backlash against cooperation agreements" in 2025, as non-pro-rata deals at Victoria PLC, Ardagh, Selecta and Hunkemöller used intercreditor clauses and slim majority thresholds.
> - **What it means for the desk.** Co-op coverage $c$ is now a first-class feature in the non-pro-rata hazard and in stage 0 of the recovery model. High coverage moves risk from the uptier channel to the drop-down and deal-away channel, so it shifts $\lambda_{\text{away}}$ up even as it pushes $\Pi(c)$ down. And the legal status of the co-op itself is a regime variable with a pending date.

The Ad Hoc Group, represented by counsel, speaks in unison: *"We have signed a cooperation agreement. We decline to transact with the Company on a non-pro-rata basis. We note that there are forty-four other groups saying the same thing this year."* (Cooperation agreements signed in this book so far: one in Chapter 3, plus forty-five in 2024 alone. The counter has overflowed its integer type.)

Optimum then sued them for being a cartel. The table agreed not to be bluffed, and the sponsor sued the table. The model lesson is that a commitment device strong enough to change $\Pi(c)$ by four orders of magnitude is strong enough to draw antitrust scrutiny. The probability that a court treats co-ops as unlawful belongs in the model as a scenario with a date, not as a parameter estimated from history, because the history has no such ruling in it yet.

## 14.6 The Courts as a Regime Variable

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.288:* "LGD realizations can depend on many hard-to-quantify factors, from the quality of a defaulting firm’s assets and franchise to the vagaries of the resolution of legal proceedings and bankruptcy rulings."
>
> **Annotation.** Bohn and Stein list legal vagaries as one reason LGD modeling lagged PD modeling. Between 2024 and 2026 they became the main driver of the excluded holder's recovery, and they became *datable*. A ruling arrives on a known day, applies to identifiable contract language, and shifts the odds for every agreement with the same words. That is not a vagary. It is a regime switch with a timestamp.

> **Docket Diary.** *The rulings that moved $\theta_w$.*
> - **June 2020.** A New York state court declines to enjoin the Serta uptier, which closes on 22 June.
> - **20 June 2024.** *Robertshaw* (Bankr. S.D. Tex.): the borrower breached the credit agreement, but the remedy for the excluded lender is money damages, not restored Required Lender status (Paul Weiss, 24 June 2024).
> - **31 December 2024, New Orleans.** The Fifth Circuit (*In re Serta Simmons Bedding*, No. 23-20181, consolidated with 23-20363, 23-20450 and 23-20451) holds that "open market purchase" means a purchase on "the secondary market for syndicated loans." A privately negotiated exchange with a subset of lenders falls outside it. The court also strikes the plan's indemnity for participating lenders. It observes that the 2020 Uptier "was the first major uptier... But it was far from the last."
> - **31 December 2024, the same day in Manhattan.** The Appellate Division, First Department (*Ocean Trails CLO VII v. MLN TopCo*, 2024 NY Slip Op 06660) permits the Mitel uptier. That agreement's exception said "purchases" with no "open market" qualifier, and subordination was only an indirect effect on the excluded lenders, so sacred rights were not triggered.
> - **17 January 2025.** *Wesco/Incora* bankruptcy court: the 2022 transactions complied with one indenture but violated the 2026 notes indenture because the steps "had the effect" of stripping liens without two-thirds consent. The deal is unwound.
> - **September 2025.** *ConvergeOne* (S.D. Tex. district court) reverses plan confirmation: an exclusive backstop for majority lenders violated equal treatment under §1123(a)(4). Appeal to the Fifth Circuit.
> - **8 December 2025.** *Wesco* district court reverses the bankruptcy court and tests each step on its own wording. Appeal pending.
> - **7 July 2026.** *Serta* remand (Bankr. S.D. Tex.): participating lenders liable for \$261.13mm plus 9% New York prejudgment interest from 22 June 2020 (Mayer Brown, July 2026; §14.8).
> - **Del Monte Foods.** Chapter 11 on 1 July 2025 (Bankr. D.N.J. 25-16984); an adversary proceeding among lender groups on 23 January 2026; a district-court action by the Ad Hoc Group of Minority Secured Lenders on 6 March 2026; an appeal on 28 May 2026.
>
> The Ad Hoc Group notes, through counsel, that it has been on both sides of every one of these.

Two rulings on the same New Year's Eve, with opposite outcomes, both correct on their own words. This is the cleanest natural experiment the LMT era offers. The economics of the two deals were similar. The contracts differed by two words. A model that predicts priming outcomes from deal economics alone would have scored these two cases identically and been wrong about one of them.

### 14.6.1 Encoding a ruling as a jump

Let $\theta_w(t)$ be the probability that a priming transaction under wording class $w$ survives challenge, given the law as of $t$. Wording classes are the tokens from Chapter 13's document parser: `open_market_purchase`, `bare_purchase`, `directly_and_adversely`, `subordination_unanimous`, and so on. Model the log-odds as piecewise constant with jumps at ruling dates $t_r$:

$$
\operatorname{logit}\theta_w(t) = \alpha_w + \sum_{r} J_{r,w}\,\mathbf{1}\{t \ge t_r\},
$$

where $J_{r,w}$ is the jump that ruling $r$ induces for wording $w$. It is zero if the ruling doesn't touch that language, negative for Serta on `open_market_purchase`, positive for Mitel on `bare_purchase`, and jurisdiction-dependent where courts split, as with the step-by-step Wesco district-court reading against the integrated reading in New York's *STG Logistics* (whose exact date we have not verified). Because rulings are rare, $J_{r,w}$ is not estimated from data. It is elicited, as a prior, from people who read the opinion, and then updated on the market's own reaction: the price gap between likely-inside and likely-outside paper in the days after the ruling.

The Fifth Circuit gave the elicitation a head start by stating its own prior: such exceptions "will often not justify an uptier." Translate "often" into a log-odds jump of your choosing and write it down with a date. The discipline matters more than the number. A model that updates on rulings by a documented rule can be audited; a model that "absorbs" them through a re-fit on twenty observations cannot.

The jumps propagate in three places. They enter the Priming Risk Score of Chapter 13 directly, since PRS inputs shift discretely at ruling dates. They enter the non-pro-rata hazard $\lambda_{\text{NPR}}$ of §14.5 through $\theta_w$. And they enter recovery through $\mu_{\text{out}}$. After the Serta remand, an excluded position in a breach case owns a damages claim with a computable value, so the excluded hump moves right. The participants' expected cost of exclusion rises too, which feeds back into a lower $\theta$ for the next deal. Mags summarizes the remand as a credit analyst would. "The best-performing tranche in the Serta capital structure was New York prejudgment interest."

## 14.7 Regime Shifts in the Joint Law of $(\tau, R)$: A Markov-Switching Engine

We now have two regime axes. The macro cycle moves the mean recovery, as in Schmid's table. The LMT regime moves the default mix $\lambda_D/\lambda$, the coalition weight $\pi$, and the excluded mean $\mu_{\text{out}}$. The second axis changed state somewhere around 2020 to 2022. A desk needs to know which state it is in *now*, and it would like a rule that tells it, rather than a debate.

### 14.7.1 The Hamilton filter on the default mix

Let $s_t \in \{0, 1\}$ be a hidden regime ("pre-LME" and "LME"), following a Markov chain with row-stochastic transition matrix $P$, where $P_{ij} = \mathbb{P}(s_{t+1} = j \mid s_t = i)$. Each year (or month) we observe $n_t$ defaults, of which $k_t$ are distressed exchanges, and we model

$$
k_t \mid s_t, n_t \sim \mathrm{Binomial}(n_t, \rho_{s_t}),
\qquad 0 < \rho_0 < \rho_1 < 1,
$$

where $\rho_s$ is the DE share in regime $s$. Using counts rather than shares matters: a 70% share from 10 defaults and a 70% share from 150 should not carry the same weight, and the binomial likelihood weights them correctly. Let $\eta_t$ be the vector of emission likelihoods, $\eta_{t,j} = f(k_t \mid s_t = j)$, and $\hat\xi_{t\mid t-1}$ the predicted regime probabilities. The filter alternates an update and a prediction:

$$
\hat\xi_{t\mid t} = \frac{\hat\xi_{t\mid t-1} \odot \eta_t}{\mathbf{1}^\top(\hat\xi_{t\mid t-1} \odot \eta_t)},
\qquad
\hat\xi_{t+1\mid t} = P^\top \hat\xi_{t\mid t},
$$

where $\odot$ is the element-wise product. The log-likelihood is $\sum_t \log \mathbf{1}^\top(\hat\xi_{t\mid t-1} \odot \eta_t)$, which we maximize over $(\rho_0, \rho_1, P_{00}, P_{11})$. Start the recursion at the stationary distribution, $\mathbb{P}(s_0 = 0) = (1 - P_{11})/(2 - P_{00} - P_{11})$.

Four implementation details decide whether this works:

1. **Log space.** Multiply by $e^{\log \eta_t - \max_j \log\eta_{t,j}}$ and add the max back to the log-likelihood, or the binomial likelihoods underflow in big default years.
2. **Label switching.** Parameterize $\rho_1 = \operatorname{logit}^{-1}(a + e^{b})$ with $\rho_0 = \operatorname{logit}^{-1}(a)$, so the "LME regime" is always the high-share state.
3. **Short samples.** Roughly 45 annual observations cannot pin down four parameters plus a regime path with any confidence. Use monthly counts, pool across rating agencies only after harmonizing definitions, and put priors on $P$.
4. **Time-varying transitions.** The ruling calendar of §14.6 is information about $P$. Let $P$ depend on $t$ through $\operatorname{logit} P_{11}(t) = c_1 + \sum_r \kappa_r \mathbf{1}\{t \ge t_r\}$, so that a ruling against priming raises the probability of leaving the LME regime. Our filter accepts a $(T, 2, 2)$ array for exactly this reason.

The same machinery extends to recovery. Run a second switch on mean LGD with Schmid's $\mu_0 \approx 0.43$ and $\mu_1 \approx 0.28$ as the macro regimes. Treat the LMT regime as orthogonal: it moves $\pi$ and $\mu_{\text{out}}$, not the macro mean.

### 14.7.2 $\mathbb{P}$ versus $\mathbb{Q}$: the definitional wedge

Everything so far lives under $\mathbb{P}$. CDS spreads live under $\mathbb{Q}$, and they also live under a different *definition* of default.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.354:* "A representative average recovery rate of 40% is assumed, such that a loss of 60% is assumed to be incurred with the specified probability."
>
> **Annotation.** The 40% convention is the market's default prior on recovery, and it is baked into CDS quoting. It was always an average over a wide distribution. In the LMT era it is an average over two humps, neither of which sits at 40. Using it for a first lien that has already been through an LME, whose eventual recovery may look more like the 23% in the Fitch study, misstates the implied hazard. The modern desk keeps 40% for quoting, because the contracts do, and never uses it as a $\mathbb{P}$-recovery for names that have been through an LME.

The credit-triangle approximation is $s \approx \lambda^{\mathbb{Q}}(1 - R^{\mathbb{Q}})$. For a fixed spread, the implied intensity under the convention is $s/0.60$, and under a 23% recovery it is $s/0.77$. The ratio is $0.60/0.77 \approx 0.78$, so the convention overstates the implied hazard by about 28% relative to the realistic recovery. On a 600bp name that is the difference between a 10% and a 7.8% annual intensity.

The larger wedge is definitional. Standard North American corporate CDS trades without restructuring as a credit event, so most distressed exchanges do not trigger the contract unless they come with a bankruptcy or a failure to pay (Chapter 24 has the mechanics). CDS therefore prices something close to $\lambda_H^{\mathbb{Q}}$, while the agencies report $\lambda_H^{\mathbb{P}} + \lambda_D^{\mathbb{P}}$. A research note that divides the CDS-implied hazard by the agency default rate and declares that "the market is underpricing default" has usually just divided a hard hazard by a hard-plus-soft hazard. That is the single most common error in this corner of the literature, and it is a units error, not a market inefficiency.

### Specification for AI Implementation

**What ROBO built from the vague version.** Told to "exclude distressed exchanges from the default rate," ROBO deleted the DE rows, reported a 2.1% default rate, and flagged the credit cycle as "benign." The deleted issuers were the ones about to re-default. Told to "model re-default," it fit an exponential to fourteen months of follow-up (§14.3). Neither result is a bug. Both are the spec doing what it said.

**The Spec You Hand the Robot.** Build `lme_cycle_engine.py`, a seeded numpy/scipy/pandas reference implementation that (1) simulates an issuer cohort through Performing → {hard default, distressed exchange, cured} under a two-state regime path, then runs a mixture-cure re-default clock after each exchange; (2) estimates cause-specific cumulative hazards and Aalen–Johansen cumulative incidence, and demonstrates the Kaplan–Meier bias; (3) fits the mixture-cure Weibull by maximum likelihood with right-censoring; (4) computes expected loss by coalition side, exactly by quadrature and by Monte Carlo; (5) fits a two-state binomial Markov-switching model to DE counts with a log-space Hamilton filter; and (6) runs the sanity checks below, printing PASS/FAIL and asserting.

**Event table schema** (pandas DataFrame, one row per event; sorted by `t_event` with a stable sort):

| Column | dtype | Meaning |
| :--- | :--- | :--- |
| `issuer_id` | int64 | Issuer key. Appears once as a first-event row, and a second time if the first event was a DE. |
| `t_event` | float64 | Years from cohort start. Censored rows carry the censoring time. |
| `event` | int8 | First-event rows: 0 censored, 1 hard default, 2 distressed exchange, 3 cured. Post-DE rows: 1 hard default after DE, 0 censored. |
| `time_since_de` | float64 | NaN on first-event rows. Time on the parole clock on post-DE rows. |
| `regime` | int8 | Regime in force in the year of the event (0 pre-LME, 1 LME). |
| `in_majority` | int8 | 1 inside, 0 excluded, −1 not applicable (no DE). |
| `recovery` | float64 | Fraction of par. For a DE, the value held right after the exchange. NaN unless an event with a recovery occurred. |

Production versions add covariate columns (`liquidity_runway_weeks`, `new_money_frac`, `coop_coverage`, `docs_vintage`, `prs`) from Chapters 13 and 25. The reference engine leaves them out so that every column is exercised by a test.

**Numerical guards and edge cases.** `np.random.default_rng(seed)` everywhere, with no global state. Beta parameters must be at least 1e-6. Work in log-survival and use `logaddexp` for the cure mixture. Clip Weibull log-parameters during optimization so that `exp` cannot overflow. Floor the filter normalizer and clip transition probabilities to $[10^{-6}, 1-10^{-6}]$. Exchanges at $t=0$ are impossible by construction, since exponential waits are strictly positive. A horizon beyond `T_max` raises. Tied event times are processed jointly per distinct time, across all causes. Never index by issuer order; always sort by time.

```python
# lme_cycle_engine.py -- Chapter 14 reference implementation (block 1 of 5: parameters and simulation)
import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy import integrate, optimize, special, stats

ETA_K12 = 2.0 / (-math.log(0.30)) ** (1.0 / 1.2)   # fact 3 of Sec. 14.3.2 with k = 1.2 -> ~1.713 years


@dataclass
class LMEParams:
    """All rates per year under P; recoveries as fractions of par. Index 0 = pre-LME regime, 1 = LME regime."""
    lam_H: np.ndarray = field(default_factory=lambda: np.array([0.030, 0.022]))  # hard-default hazard
    lam_D: np.ndarray = field(default_factory=lambda: np.array([0.008, 0.038]))  # distressed-exchange hazard
    lam_C: float = 0.05                                    # cure / refinanced-away hazard
    P: np.ndarray = field(default_factory=lambda: np.array([[0.90, 0.10],
                                                             [0.15, 0.85]]))  # annual regime transitions
    p_redefault: float = 0.25        # susceptible fraction after a DE (Moody's 2026: about 1 in 4)
    k: float = 1.2                   # Weibull shape among the susceptible (Sec. 14.3.2 table)
    eta: float = ETA_K12             # Weibull scale in years, so that F(2)/p = 0.70
    pi: float = 0.526                # P(in majority group): Serta first-lien class
    ab_in: tuple = (14.8, 5.2)       # value right after the DE, inside the group (mean 0.74)
    ab_out: tuple = (2.0, 6.0)       # value right after the DE, excluded (mean 0.25)
    ab_hard_noLME: tuple = (2.65, 2.35)    # recovery on a hard default with no prior LME (mean 0.53)
    ab_hard_postLME: tuple = (1.15, 3.85)  # recovery on a hard default after an LME (mean 0.23)
    T_max: float = 10.0
    censor_rate: float = 0.0         # independent random censoring of the first event, per year

    def __post_init__(self):
        self.lam_H = np.asarray(self.lam_H, dtype=float)
        self.lam_D = np.asarray(self.lam_D, dtype=float)
        self.P = np.asarray(self.P, dtype=float)
        assert self.lam_H.shape == (2,) and self.lam_D.shape == (2,)
        assert self.P.shape == (2, 2) and np.allclose(self.P.sum(axis=1), 1.0)
        assert 0.0 < self.p_redefault < 1.0 and self.k > 0.0 and self.eta > 0.0
        for ab in (self.ab_in, self.ab_out, self.ab_hard_noLME, self.ab_hard_postLME):
            assert min(ab) >= 1e-6, "Beta parameters must be positive"


def beta_mean(ab):
    a, b = ab
    return a / (a + b)


def beta_var(ab):
    a, b = ab
    return a * b / ((a + b) ** 2 * (a + b + 1.0))


def simulate_regime_path(n_years, P, s0, rng):
    s = np.empty(n_years, dtype=np.int8)
    s[0] = s0
    for j in range(1, n_years):
        s[j] = rng.choice(2, p=P[s[j - 1]])
    return s


def simulate_cohort(n, prm, seed, s0=1, regime_path=None):
    """Cohort of n issuers: Performing -> {1 hard, 2 DE, 3 cured}, then the post-DE cure-Weibull clock.

    The regime path is systematic (one path per cohort): every issuer sees the same regime each year.
    """
    rng = np.random.default_rng(seed)
    n_years = int(math.ceil(prm.T_max))
    if regime_path is None:
        s = simulate_regime_path(n_years, prm.P, s0, rng)
    else:
        s = np.asarray(regime_path, dtype=np.int8)
        assert s.shape == (n_years,)

    t1 = np.full(n, prm.T_max)                  # first-event time; T_max means administratively censored
    e1 = np.zeros(n, dtype=np.int8)
    g1 = np.full(n, s[-1], dtype=np.int8)
    alive = np.ones(n, dtype=bool)
    for j in range(n_years):                    # hazards are constant within each regime-year
        idx = np.flatnonzero(alive)
        if idx.size == 0:
            break
        lh, ld, lc = prm.lam_H[s[j]], prm.lam_D[s[j]], prm.lam_C
        lam = lh + ld + lc
        if lam <= 0.0:
            continue
        width = min(1.0, prm.T_max - j)
        wait = rng.exponential(1.0 / lam, size=idx.size)
        hit = wait < width
        who = idx[hit]
        t1[who] = j + wait[hit]
        u = rng.random(who.size) * lam          # which cause fired, proportional to its hazard
        e1[who] = np.where(u < lh, 1, np.where(u < lh + ld, 2, 3)).astype(np.int8)
        g1[who] = s[j]
        alive[who] = False

    if prm.censor_rate > 0.0:
        c = rng.exponential(1.0 / prm.censor_rate, size=n)
        cens = c < t1
        t1[cens] = c[cens]
        e1[cens] = 0

    rec1 = np.full(n, np.nan)
    in_maj = np.full(n, -1, dtype=np.int8)
    is_h = e1 == 1
    rec1[is_h] = rng.beta(*prm.ab_hard_noLME, size=int(is_h.sum()))
    de = np.flatnonzero(e1 == 2)
    member = rng.random(de.size) < prm.pi
    in_maj[de] = member.astype(np.int8)
    r_in = rng.beta(*prm.ab_in, size=de.size)
    r_out = rng.beta(*prm.ab_out, size=de.size)
    rec1[de] = np.where(member, r_in, r_out)

    susc = rng.random(de.size) < prm.p_redefault           # cured draws never hard-default
    u_draw = np.full(de.size, np.inf)
    u_draw[susc] = prm.eta * rng.weibull(prm.k, size=int(susc.sum()))
    follow = prm.T_max - t1[de]
    hit2 = u_draw <= follow
    u_obs = np.where(hit2, u_draw, follow)
    rec2 = np.full(de.size, np.nan)
    rec2[hit2] = rng.beta(*prm.ab_hard_postLME, size=int(hit2.sum()))
    t2 = t1[de] + u_obs
    g2 = s[np.minimum(t2.astype(int), n_years - 1)]

    first = pd.DataFrame({"issuer_id": np.arange(n, dtype=np.int64), "t_event": t1, "event": e1,
                          "time_since_de": np.nan, "regime": g1, "in_majority": in_maj, "recovery": rec1})
    post = pd.DataFrame({"issuer_id": de.astype(np.int64), "t_event": t2, "event": hit2.astype(np.int8),
                         "time_since_de": u_obs, "regime": g2, "in_majority": in_maj[de], "recovery": rec2})
    df = pd.concat([first, post], ignore_index=True)
    return df.sort_values("t_event", kind="stable").reset_index(drop=True)
```

```python
# block 2 of 5: competing-risks estimators (first events only)
def _first_events(df):
    f = df[df["time_since_de"].isna()]
    return f["t_event"].to_numpy(dtype=float), f["event"].to_numpy(dtype=int)


def _risk_table(t, e, causes):
    order = np.argsort(t, kind="stable")
    t, e = t[order], e[order]
    times = np.unique(t[e > 0])                                   # distinct event times
    n_risk = (t.size - np.searchsorted(t, times, side="left")).astype(float)
    d = {}
    for k in causes:                                              # ties handled per distinct time
        tk = t[e == k]
        d[k] = (np.searchsorted(tk, times, side="right") - np.searchsorted(tk, times, side="left")).astype(float)
    return times, n_risk, d


def nelson_aalen_cause(df, cause, causes=(1, 2, 3)):
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    return times, np.cumsum(d[cause] / n_risk)


def aalen_johansen(df, causes=(1, 2, 3)):
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    d_all = sum(d[k] for k in causes)
    s_after = np.cumprod(1.0 - d_all / n_risk)
    s_before = np.concatenate(([1.0], s_after[:-1]))
    out = {"time": times, "S": s_after}
    for k, name in zip(causes, ("F_H", "F_D", "F_C")):
        out[name] = np.cumsum(s_before * d[k] / n_risk)
    return pd.DataFrame(out)


def km_naive_cif(df, cause, causes=(1, 2, 3)):
    """The WRONG estimator, kept for the test: 1 - KM with competing causes treated as censoring."""
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    return times, 1.0 - np.cumprod(1.0 - d[cause] / n_risk)


def step_at(times, values, t):
    i = np.searchsorted(times, t, side="right") - 1
    return float(np.where(i >= 0, values[np.maximum(i, 0)], 0.0))
```

```python
# block 3 of 5: re-default clock, expected loss, coalition mixture, co-op game
def _cure_nll(theta, u, delta):
    a = theta[0]
    b, c = np.clip(theta[1], -5.0, 5.0), np.clip(theta[2], -7.0, 7.0)   # log k, log eta (overflow guard)
    k, eta = math.exp(b), math.exp(c)
    log_p, log_1mp = -np.logaddexp(0.0, -a), -np.logaddexp(0.0, a)
    with np.errstate(over="ignore"):
        z = (u / eta) ** k
    log_f0 = b - c + (k - 1.0) * (np.log(u) - c) - z
    log_surv = np.logaddexp(log_1mp, log_p - z)                  # log[(1-p) + p S0(u)]
    ll = np.where(delta == 1, log_p + log_f0, log_surv)
    return -float(ll.sum())


def fit_cure_weibull(u, delta, seed=0, n_starts=4):
    u = np.maximum(np.asarray(u, dtype=float), 1e-8)
    delta = np.asarray(delta, dtype=int)
    rng = np.random.default_rng(seed)
    best = None
    for i in range(n_starts):
        x0 = np.array([special.logit(0.3), 0.0, 0.5]) + (rng.normal(0.0, 0.3, 3) if i else 0.0)
        res = optimize.minimize(_cure_nll, x0, args=(u, delta), method="Nelder-Mead",
                                options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000})
        if best is None or res.fun < best.fun:
            best = res
    a, b, c = best.x
    return float(special.expit(a)), math.exp(np.clip(b, -5, 5)), math.exp(np.clip(c, -7, 7)), -float(best.fun)


def expected_loss(prm, T, side="blend", regime=1):
    """Exact EL(T) of Sec. 14.3.3 in a single regime, by quadrature over the exchange date."""
    if T > prm.T_max:
        raise ValueError("horizon beyond T_max")
    lh, ld, lc = prm.lam_H[regime], prm.lam_D[regime], prm.lam_C
    lam = lh + ld + lc
    L_H = 1.0 - beta_mean(prm.ab_hard_noLME)
    L_post = 1.0 - beta_mean(prm.ab_hard_postLME)
    mu = {"in": beta_mean(prm.ab_in), "out": beta_mean(prm.ab_out)}
    mu["blend"] = prm.pi * mu["in"] + (1.0 - prm.pi) * mu["out"]
    L_D = 1.0 - mu[side]
    F_H = lh / lam * (1.0 - math.exp(-lam * T))

    def G(v):
        return prm.p_redefault * (1.0 - math.exp(-(max(v, 0.0) / prm.eta) ** prm.k))

    def integrand(x):
        return math.exp(-lam * x) * ld * (L_D + (1.0 - L_D) * L_post * G(T - x))

    de_part, _ = integrate.quad(integrand, 0.0, T)
    return F_H * L_H + de_part


def expected_loss_mc(df, T, side="blend"):
    first = df[df["time_since_de"].isna()]
    post = df[df["time_since_de"].notna()].set_index("issuer_id")
    n = len(first)
    h = first[(first["event"] == 1) & (first["t_event"] <= T)]
    loss = float((1.0 - h["recovery"]).sum()) / n
    de = first[(first["event"] == 2) & (first["t_event"] <= T)]
    de_side = de if side == "blend" else de[de["in_majority"] == (1 if side == "in" else 0)]
    if len(de_side) == 0:
        return loss
    p2 = post.loc[de_side["issuer_id"].to_numpy()]
    redef = (p2["event"].to_numpy() == 1) & (p2["t_event"].to_numpy() <= T)
    r_d = de_side["recovery"].to_numpy()
    r_post = np.nan_to_num(p2["recovery"].to_numpy(), nan=1.0)
    per_de = (1.0 - r_d) + r_d * (1.0 - r_post) * redef
    return loss + len(de) / n * float(per_de.mean())


def coalition_mixture_moments(pi, ab_in, ab_out):
    m_in, m_out = beta_mean(ab_in), beta_mean(ab_out)
    mean = pi * m_in + (1.0 - pi) * m_out
    within = pi * beta_var(ab_in) + (1.0 - pi) * beta_var(ab_out)
    between = pi * (1.0 - pi) * (m_in - m_out) ** 2
    return mean, within + between, between


def coop_break_prob(c, m=0.501, n=10, phi=0.10):
    """Sec. 14.5.1: P(at least d* of n equal co-op members defect), independent defection prob phi."""
    if 1.0 - c >= m:
        return 1.0                                             # co-op below the blocking line
    d_star = math.ceil(n * (m + c - 1.0) / c - 1e-12)
    return float(stats.binom.sf(d_star - 1, n, phi))
```

```python
# block 4 of 5: two-state binomial Markov-switching model on DE counts
def hamilton_filter(logf, P, xi0=None):
    """logf: (T, 2) log emission likelihoods; P: (2, 2) or (T, 2, 2) row-stochastic."""
    logf = np.asarray(logf, dtype=float)
    T_, K = logf.shape
    Pt = np.broadcast_to(P, (T_, K, K)) if np.ndim(P) == 2 else np.asarray(P)
    if xi0 is None:
        denom = 2.0 - Pt[0][0, 0] - Pt[0][1, 1]
        pi0 = (1.0 - Pt[0][1, 1]) / denom if denom > 1e-12 else 0.5
        xi0 = np.array([pi0, 1.0 - pi0])
    xi_pred = np.asarray(xi0, dtype=float)
    filt = np.empty((T_, K))
    ll = 0.0
    for t in range(T_):
        mx = logf[t].max()
        w = xi_pred * np.exp(logf[t] - mx)
        c = max(float(w.sum()), 1e-300)
        ll += math.log(c) + mx
        filt[t] = w / c
        xi_pred = Pt[t].T @ filt[t]
    return filt, ll


def binom_logf(k, n, shares):
    shares = np.clip(np.asarray(shares, dtype=float), 1e-9, 1.0 - 1e-9)
    return stats.binom.logpmf(np.asarray(k)[:, None], np.asarray(n)[:, None], shares[None, :])


def _ms2_unpack(theta):
    a, b, c0, c1 = theta
    s0 = special.expit(a)
    s1 = special.expit(a + math.exp(min(b, 5.0)))             # ordered: no label switching
    p00 = float(np.clip(special.expit(c0), 1e-6, 1 - 1e-6))
    p11 = float(np.clip(special.expit(c1), 1e-6, 1 - 1e-6))
    return np.array([s0, s1]), np.array([[p00, 1.0 - p00], [1.0 - p11, p11]])


def fit_ms2(k, n, seed=0, n_starts=6):
    rng = np.random.default_rng(seed)

    def nll(theta):
        shares, P = _ms2_unpack(theta)
        return -hamilton_filter(binom_logf(k, n, shares), P)[1]

    best = None
    for _ in range(n_starts):
        x0 = np.array([rng.normal(-1.0, 0.7), rng.normal(0.0, 0.5), rng.normal(2.0, 0.5), rng.normal(2.0, 0.5)])
        res = optimize.minimize(nll, x0, method="Nelder-Mead",
                                options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 4000})
        if best is None or res.fun < best.fun:
            best = res
    shares, P = _ms2_unpack(best.x)
    filt, ll = hamilton_filter(binom_logf(k, n, shares), P)
    return {"shares": shares, "P": P, "filtered": filt, "loglik": ll}


def simulate_de_share_series(n_years, shares, P, mean_defaults, seed, s0=0):
    rng = np.random.default_rng(seed)
    s = simulate_regime_path(n_years, np.asarray(P, dtype=float), s0, rng)
    n = rng.poisson(mean_defaults, size=n_years)
    k = rng.binomial(n, np.asarray(shares)[s])
    return s, k, n
```

```python
# block 5 of 5: sanity checks (each prints PASS/FAIL and asserts)
def check(name, ok):
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
    assert ok, name


prm = LMEParams()
check("F(2)/p = 0.70 at the calibrated eta", abs((1 - math.exp(-(2 / prm.eta) ** prm.k)) - 0.70) < 1e-12)

one = LMEParams(P=np.eye(2))                                     # single-regime world for closed forms
path1 = np.ones(10, dtype=np.int8)
df1 = simulate_cohort(50_000, one, seed=14, regime_path=path1)
aj = aalen_johansen(df1)
resid = float((aj["S"] + aj["F_H"] + aj["F_D"] + aj["F_C"] - 1.0).abs().max())
check("S + F_H + F_D + F_C = 1 at every jump (1e-10)", resid < 1e-10)
lam1 = one.lam_H[1] + one.lam_D[1] + one.lam_C
for t in (1.0, 3.0, 5.0):
    for col, lk in (("F_H", one.lam_H[1]), ("F_D", one.lam_D[1])):
        truth = lk / lam1 * (1 - math.exp(-lam1 * t))
        est = step_at(aj["time"].to_numpy(), aj[col].to_numpy(), t)
        se = math.sqrt(truth * (1 - truth) / 50_000)
        check(f"Aalen-Johansen {col}({t:.0f}) within 4 SE of closed form", abs(est - truth) < 4 * se)

tk, naive = km_naive_cif(df1, cause=2)
check("Kaplan-Meier trap: 1 - KM_D(5) > F_D(5)",
      step_at(tk, naive, 5.0) > step_at(aj["time"].to_numpy(), aj["F_D"].to_numpy(), 5.0))

f1 = df1[df1["time_since_de"].isna()]
n_h, n_d = int((f1["event"] == 1).sum()), int((f1["event"] == 2).sum())
share_true = one.lam_D[1] / (one.lam_H[1] + one.lam_D[1])
share_se = math.sqrt(share_true * (1 - share_true) / (n_h + n_d))
check("DE share of first defaults -> lam_D/(lam_H+lam_D)", abs(n_d / (n_h + n_d) - share_true) < 4 * share_se)

rng = np.random.default_rng(7)
member = rng.random(400_000) < prm.pi
r = np.where(member, rng.beta(*prm.ab_in, 400_000), rng.beta(*prm.ab_out, 400_000))
mean_f, var_f, between_f = coalition_mixture_moments(prm.pi, prm.ab_in, prm.ab_out)
pm = member.mean()
between_s = pm * (1 - pm) * (r[member].mean() - r[~member].mean()) ** 2
check("mixture mean matches simulation", abs(r.mean() - mean_f) < 0.01)
check("mixture variance matches simulation", abs(r.var() - var_f) < 0.002)
check("between-group variance matches simulation", abs(between_s - between_f) < 0.002)
check("Serta between-group sd ~ 0.245",
      abs(math.sqrt(coalition_mixture_moments(0.526, (74, 26), (25, 75))[2]) - 0.245) < 0.001)

rng = np.random.default_rng(2026)
N = 20_000
susc = rng.random(N) < prm.p_redefault
u_true = np.where(susc, prm.eta * rng.weibull(prm.k, N), np.inf)
cens = rng.uniform(0.5, 10.0, N)
u_obs, d_obs = np.minimum(u_true, cens), (u_true <= cens).astype(int)
p_hat, k_hat, eta_hat, _ = fit_cure_weibull(u_obs, d_obs)
print(f"cure-Weibull fit: p={p_hat:.3f}, k={k_hat:.3f}, eta={eta_hat:.3f}")
check("cure fit: p within 0.03", abs(p_hat - prm.p_redefault) < 0.03)
check("cure fit: k within 0.15", abs(k_hat - prm.k) < 0.15)
check("cure fit: eta within 15%", abs(eta_hat / prm.eta - 1) < 0.15)
check("cure fit: F(2)/p ~ 0.70", abs((1 - math.exp(-(2 / eta_hat) ** k_hat)) - 0.70) < 0.03)
short = np.minimum(u_true, 14 / 12)                                # ROBO's 14 months of follow-up
lam_exp = (u_true <= 14 / 12).sum() / short.sum()
print(f"ROBO's exponential: hazard {lam_exp:.3f}/yr, mean {1 / lam_exp:.1f} yrs, "
      f"10y default prob {1 - math.exp(-10 * lam_exp):.0%} vs truth {prm.p_redefault:.0%}")
check("exponential on short follow-up overstates the 10y default prob", 1 - math.exp(-10 * lam_exp) > 0.5)

df_el = simulate_cohort(60_000, one, seed=99, regime_path=path1)
for side in ("in", "out", "blend"):
    ex, mc = expected_loss(one, 3.0, side), expected_loss_mc(df_el, 3.0, side)
    print(f"EL(3y) {side:>5}: exact {ex:.4f}  MC {mc:.4f}")
    check(f"EL exact vs MC ({side})", abs(ex - mc) < 0.005)
check("excluded holder's EL exceeds included holder's",
      expected_loss(one, 3.0, "out") > expected_loss(one, 3.0, "in"))

s_true, k_de, n_def = simulate_de_share_series(80, [0.30, 0.63], [[0.92, 0.08], [0.10, 0.90]], 90, seed=5)
fit = fit_ms2(k_de, n_def, seed=1)
filt = fit["filtered"]
check("filtered probabilities in [0, 1]", bool(((filt >= 0) & (filt <= 1)).all()))
check("filtered rows sum to 1", bool(np.allclose(filt.sum(axis=1), 1.0)))
agree = float(((filt[:, 1] > 0.5).astype(int) == s_true).mean())
print(f"MS2 shares {np.round(fit['shares'], 3)}, regime agreement {agree:.0%}")
check("filtered regime agrees with truth > 85% of years", agree > 0.85)

check("P vs Q: implied-hazard ratio 0.60/0.77 ~ 0.779", abs((0.06 / 0.77) / (0.06 / 0.60) - 0.779) < 0.001)
check("co-op c=0.70, n=10: break prob ~7.0%", abs(coop_break_prob(0.70) - 0.0702) < 0.0005)
check("co-op c=0.90, n=15: break prob < 0.1%", coop_break_prob(0.90, n=15) < 1e-3)
check("co-op below the blocking line is decorative", coop_break_prob(0.40) == 1.0)
check("Serta: 734 x 47.43% ~ 348 (USD mm)", abs(734 * 0.4743 - 348) < 1.0)
check("Serta: 484.88 - 895 x 0.25 = 261.13 (USD mm)", abs(484.88 - 895 * 0.25 - 261.13) < 1e-9)
```

The tests double as documentation. If a later contributor "simplifies" `aalen_johansen` into one minus Kaplan–Meier, the trap test fails. If someone replaces the cure model with an exponential, the fourteen-month test prints ROBO's answer next to the truth.

### Deep-Dive Resource Graph (§14.7)

- **Academic Papers.** Hamilton (1989), *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*, Econometrica. Fine & Gray (1999), *A Proportional Hazards Model for the Subdistribution of a Competing Risk*, JASA 94(446). Aalen & Johansen (1978), *An Empirical Transition Matrix for Non-homogeneous Markov Chains Based on Censored Observations*, Scandinavian Journal of Statistics.
- **Data & Code.** Moody's and S&P annual default studies (vendor) for DE counts by year; Federal Reserve FSR Figure 2.9 for a public DE-inclusive series.
