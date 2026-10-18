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

From Performing, the competing hazards of §14.2 apply. On entering Parole at the exchange date, a new clock $u$ starts at zero, and the exits are a hard-default hazard $h_H(u)$, a repeat-exchange hazard $h_D(u)$, and a cure (refinanced at par, acquired, or upgraded out of distress). We cap the number of exchanges at two in code, to keep the state space finite, and document the cap as a known simplification.

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

> **Ways This Blows Up.** *What ROBO built from the vague version.* Asked to "model time to re-default," ROBO fit an exponential to a sample with fourteen months of follow-up. It reported a hazard of about 0.12 per year and an expected time to hard default of roughly eight and a half years, with a straight face. Both halves are wrong, in opposite directions. The exponential has no cure fraction, so it implies that about two-thirds of the cohort hard-defaults within a decade, against Moody's quarter. And it smears the defaults that do happen, which are front-loaded, across a decade. The fix is not a better optimizer. It is a model with a parameter for "never," plus a spec that says so (§14.7).

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
> - **31 December 2024, morning in Louisiana.** The Fifth Circuit (*In re Serta Simmons Bedding*, No. 23-20181, consolidated with 23-20363, 23-20450 and 23-20451) holds that "open market purchase" means a purchase on "the secondary market for syndicated loans." A privately negotiated exchange with a subset of lenders falls outside it. The court also strikes the plan's indemnity for participating lenders. It observes that the 2020 Uptier "was the first major uptier... But it was far from the last."
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
