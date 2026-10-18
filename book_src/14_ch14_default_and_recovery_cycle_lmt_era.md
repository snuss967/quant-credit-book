# Chapter 14: The Default & Recovery Cycle in the LMT Era (TREND)

*Thursday, 2:40 p.m. The loan market is quiet in the way a card room is quiet right before somebody shoves.*

The RFQ arrives at 2:40: a client wants an offer on \$12mm of the Quillfeather Packaging first-lien term loan due 2029. (Quillfeather is fictional. Its history is a composite of real ones.) Fourteen months ago Quillfeather's sponsor ran a non-pro-rata uptier. A 52% majority of the first-lien lenders exchanged into a new super-priority tranche and put in \$90mm of new money. The other 48% kept their old loans, which now sit behind more than a billion dollars of debt that did not exist the week before. The agencies called it a distressed exchange, counted it as a default, and a few weeks later re-rated the company out of default. The client wants the old, excluded first lien. It was marked at 41 last night.

It is a one-way request. The client has asked for an offer and not for a bid, which on a loan desk is the difference between "what is this worth?" and "I want it." The name on the ticket belongs to a special-situations fund that the coverage sheet lists as a buyer of stressed paper. As far as anyone can tell from the press reports and the cleansing materials published after the uptier, it was not in the June group.

Ines Okafor does not look up from her screen. "Hand history."

Theo Marsh pulls the markouts. The desk has traded the excluded Quillfeather loan nine times since the uptier, all in small size, almost all of it CLOs selling to the desk in the last week of a month, and the desk made money a week later on every one of those trades *(illustrative)*. "Nobody has ever asked us for an offer on this," he says. "Only bids."

"So this is the first hand where somebody is raising into us," says Ines.

"So it already defaulted," says Kaz Lind. "Is it immune now? Like chickenpox?"

"It's not immune," says Mags Dunleavy. "It's on parole."

"I don't understand why it trades at all." Kaz has the look of someone whose model just produced a negative variance. "In every model I have ever built, default is absorbing. The process stops. You collect $R$ and go home. This thing defaulted fourteen months ago and it was marked last night."

"That's a bankruptcy you're describing," says Mags. "This was a default the way a speeding ticket is a criminal record. The agencies wrote it down. The company kept paying interest. The loan is still outstanding, and the people who own it still have to decide every morning whether to keep owning it. Back in my day, default meant the phone stopped ringing. Now it means the phone starts." She does not reach for a terminal. She has been asked for this comparison often enough that she gives it from memory. "Serta. Twenty-second of June, 2020. A bare majority of the first lien, 52.6% of the class on the numbers the remand court eventually used, put in new money and swapped their loans into a super-priority tranche at 74. Everybody else in the same class stayed behind in loans the court later valued at about 25. Same loan, same Monday, forty-nine points apart, and the only difference was who had picked up the phone." She taps the 41 on Theo's screen. "That 41 is the 25 and the 74 averaged by someone who doesn't know which one they own."

Kaz takes the line literally, which is the most useful thing Kaz does. "If the only two outcomes are 25 and 74, a price of 41 puts weight $(41-25)/(74-25) = 16/49 \approx 0.33$ on the good one. So the market thinks a holder of this loan has about a one-in-three chance of being in the room next time."

"Or of a court putting them there," says Mags. "Ask the Serta excluded lenders how long that takes. And your arithmetic ignores time, which is the expensive part."

Theo has the 13-week cash flow model open, the one he still carries on a USB stick for emotional support. He rolled it forward last night out of habit, the way some people check the weather, and he reads the bottom line off the screen. "The new money buys them runway to about the third quarter of next year. After that, the interest bill comes back." He scrolls. "Liquidity crosses the revolver's minimum-availability test somewhere in that quarter, unless they sell something or get another deal done."

"Another deal," says Kaz, "meaning another default."

"Meaning another default by the agencies' definition, possibly," says Theo. "Or a filing. Those are different events with different recoveries, and the 41 doesn't tell you which one it's pricing."

Ines turns her chair a quarter turn. "What's the pot, what are the odds, and who at this table was in the majority group?"

"The pot is about \$4.9mm at 41. The odds..." Theo stops. "The odds are the problem. In 2015 I'd have looked up a recovery for a defaulted first lien and called it forty cents. But this loan has already defaulted once and it isn't in bankruptcy. Its next default could be a filing or another exchange. And its recovery depends less on the word 'first' in its name than on which side of the table its holders were sitting on in June."

"And the buyer?" Ines asks.

"Either they think the parole ends well, or they want to be inside the room for the next deal." Theo looks at the ticket again, and the thing he had been circling lands. "And they weren't inside the room last time. A fund that wasn't in the June group, asking only for an offer, in a loan that has only ever traded one way. They're not buying a recovery. They're buying a seat."

"Then the flow is the information," says Ines. "If they're assembling a block for the next negotiation, every piece they buy is a piece the sponsor will have to call, and 41 is too cheap to be short to them. If they just like the runway, 41 is fine and we're a normal dealer having a normal Thursday. Which hump our \$12mm ends up in depends on who is buying it, and that isn't on the term sheet."

From offstage, the Ad Hoc Group speaks in unison, through counsel: *"We are not sellers. We neither confirm nor deny that we are buyers."*

Ines lets that go by. "Here's what I want before you answer. I want to know which of the two default rates that 41 is pricing, the one that counts this exchange or the one that pretends it didn't happen. I want the soft tap and the hard tap on that hazard split apart, and their cumulative incidence estimated without the Kaplan–Meier lie. I want a re-default clock calibrated to Moody's 2026 soft-default study, not to your gut. I want recovery written as two humps and a coin, and I want to see for myself that the coin, one binary variable for which side of the room you sat on, explains more of the spread in recoveries than seniority and the cycle that the textbooks credit. I want the co-op and the courts on a calendar, as variables with dates. I want a filter on the default mix that tells me which world we're in. I want the bookmaker's odds and the true odds kept in separate drawers when the CDS contract and the agency disagree about what a default even is. And then I want ROBO to be able to build all of it without asking you a single question, because it won't ask. It'll just build the wrong thing."

**The question this chapter answers: what is the joint law of (time to the next default, recovery) for a credit that has already been restructured once, and how is it different from the law we all learned in 2015?**

By the end of this chapter you will be able to do everything on Ines's list, and to answer the question she asks next. It is 2:41. Do you offer \$12mm at 41, and what would make you offer 38 or 44?

## 14.1 Two Default Rates, Two Recovery Rates

In the RSSG seat, "default" had a clear meaning. It was the day the company filed, or the day it missed a coupon and the forbearance agreement ran out. Everything before that was positioning. Everything after was a plan of reorganization, a valuation fight, and eighteen months of fee applications. Default was one absorbing state, and the recovery was whatever the plan said your class got.

The systematic desk inherits a different definition, and the gap between the two is now the most important footnote in credit.

Before the definition fight starts, one piece of vocabulary, because this chapter uses two phrases for "how often companies default" and they do not mean the same thing. The number in a rating agency's headline is a *rate*: of the issuers alive a year ago, the share that defaulted. The number a model wants is an *intensity*, or *hazard*, written $\lambda_t$: how fast the survivors are defaulting at this moment. Theo met the second one in Chapter 5, when his 13-week model was turned into a hazard. Here it meets the first one, and the two are about to be asked to do the same job.

> **Math, Gently.** *A default rate is an odometer; a hazard is a speedometer.* An odometer tells you how many miles the car covered this year. A speedometer tells you how fast it is going right now. A twelve-month default rate is an odometer reading: of the companies alive last June, 5.8% had defaulted by this June. A hazard rate $\lambda$ is the speedometer: the rate, per year, at which the companies still alive are defaulting at this instant. If the speed held constant all year, the share surviving the year is $e^{-\lambda}$, so a 5.8% rate means $e^{-\lambda} = 0.942$, a speed of $\lambda = -\ln(0.942) \approx 0.0597$ per year. The two numbers are close when they are small and drift apart as they grow, because a company that defaulted in March cannot default again in October; the survivors are a shrinking base. At that same constant speed, three years of survival is $e^{-3 \times 0.0597} = e^{-0.179} \approx 0.84$, so about 16% of the cohort is gone, not the $3 \times 5.8\% = 17.4\%$ you get by adding up odometer readings. A constant speed gives the **exponential distribution** for the waiting time to default: constant speed, no memory, meaning the chance of getting through the next year is the same whether the company is one year past its LBO or ten. That makes it different from a **normal** distribution, which is a symmetric bell that happily puts weight on negative numbers (a default time of minus two years is not a thing), and from a **Poisson** distribution, which counts *how many* defaults arrive in a window rather than *how long* you wait for the first; the Poisson and the exponential are the same process seen from opposite ends (§5.3.2, §6.1.4). Most of this chapter is about what happens when the speed is not constant and there are two engines instead of one. The full version, with two hazards and their cumulative incidence, is in §14.2.1. *(Random walks and Itô's $\tfrac12\sigma^2$ do no work in this chapter; their first-use boxes are in §3.1.3, §5.2.3 and §6.1.1. Risk-neutral pricing returns in §14.7.2, and its first box is in §6.2.2.)*

With the vocabulary in hand, here is the sentence that makes one company's speedometer show two different speeds at once.

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

Moody's now publishes the gap directly. In June 2025 the trailing twelve-month speculative-grade default rate for bonds and loans combined was 5.8% including distressed exchanges. Removing the 51 distressed restructurings brought it to 2.1%, "almost one-third" of the headline (Moody's Asset Management Research, *Corporate Credit Risk Looking for a Catalyst to Break Out*, 7 August 2025). Same issuers, same twelve months, a factor of almost three, and the difference is a definition. Figure 14.1 sets that gap beside the soft share of defaults behind it.

![Figure 14.1: Counting distressed exchanges multiplies the headline default rate by almost three (left), because soft defaults have grown from about a third to about two-thirds of all defaults (right). Source: Moody's Asset Management Research (6 March 2025, 7 August 2025), Moody's (28 April and 18 May 2026) and S&P (15 August 2024, as cited by FTI Consulting, 9 October 2026), as quoted in §14.1; shares are rounded as published, S&P's are for US defaults, and the agencies' definitions differ.](assets/figures/ch14_two_default_rates.png)

The punchline for a model builder is uncomfortable. A probability-of-default model trained on pre-2020 labels ("filed or missed a payment") and scored against today's agency default rate will look as if it under-predicts by roughly that factor of three. It isn't miscalibrated. It is answering a different question. Mixing Moody's DE-inclusive counts, S&P's SD, Fitch's RD and a vendor's "excluding LMEs" series in one training set produces label noise that no amount of gradient boosting will find, because it isn't noise in $X$. It is noise in the definition of $y$.

Here are the same years seen from a chair that has to live with both numbers. Picture a CLO manager *(a fictional composite)* running a dozen vehicles of broadly syndicated loans from an office where the most important document is the monthly trustee report. Her job is not to beat an index. It is to keep seven numbers inside their lines, above all a CCC share under its limit, "typically set to 7.5%," and overcollateralization and interest-coverage cushions above theirs; the median CLO, by one ECB-system study, runs "within 4% of the most stringent covenant threshold" (Kundu, ESRB Working Paper 141, March 2023).

In 2024 the LMT count reached a record 38 (Wachtell Lipton, 3 February 2026), and for her that year was a parade of phone calls she was not on. A sponsor's advisers would call a few large holders, a deal would close, a press release would arrive. If her vehicles were in the group, she came out with a first-out loan she could hold. If they were not, she came out with a loan rated SD for a few days and then CCC, and once her CCC bucket overflowed, the excess was marked at the lowest price in the bucket, straight out of her OC numerator. Either way the agencies' count ticked up, because an exchange is a default whichever side of it you sat on. That was the year distressed exchanges reached about three in five Moody's-rated defaults.

In 2025 the count fell to 24. A consultant's deck called it the year LMEs peaked. Her trustee reports said otherwise. The deals kept coming, a few fewer and a little more consensual, and the soft share of defaults did not budge: about two-thirds by issuer count, and ahead of payment defaults and bankruptcies on a rolling twelve-month basis in every month of the year (Wachtell, 3 February 2026). Fewer coercive uptiers, more discounted amend-and-extends and equity handovers, each still a default to the agencies and still a CCC in her bucket. The technique had changed clothes, not careers.

By May 2026 the Federal Reserve was saying it in its *Financial Stability Report*: defaults including distressed exchanges "remained relatively high," even while volume-weighted loan default rates sat below their median. That is a polite way of saying the odometer and the speedometer had come apart, and that the number on her monthly report depended on which one the trustee read.

What she learned, and what a model builder has to learn from her, is that the *level* of the default rate became a weak signal and the *mix* became a strong one. The box below is the ledger behind that story.

> **Trend Watch.** *The soft-default takeover, 2010–2026.*
> - **Baseline.** S&P counted distressed exchanges at roughly one-third of US defaults over 2010–2023 and about half in the years to mid-2024 (S&P, *Distressed Exchanges Reached Their Highest Level Since 2009*, 15 August 2024, as cited by FTI Consulting, 9 October 2026; we could not open the S&P original).
> - **2024.** Distressed exchanges were roughly three in five Moody's-rated defaults, a record share (Moody's AMR, 6 March 2025). LMT counts hit a high-water mark of 38 (Wachtell Lipton, *Liability Management 2026*, 3 February 2026).
> - **H1 2025.** About 60% of defaults in the first half of 2025, similar to 2024, concentrated in loan-only, private-equity-backed capital structures (Moody's AMR, 7 August 2025).
> - **2025.** About 65% of all defaults were distressed restructurings (Moody's, 28 April 2026). LME counts fell to 24, yet LMEs were still about two-thirds of default activity by issuer count and exceeded payment defaults and bankruptcies on a rolling twelve-month basis every month of the year (Wachtell, 3 February 2026). In Moody's direct-lending proxy, the default rate was 1.6% excluding distressed exchanges and 4.7% including them.
> - **2026.** The Federal Reserve's May 2026 *Financial Stability Report* notes that defaults including distressed exchanges "remained relatively high" even as volume-weighted loan default rates sat below their median. 9fin counted 25 completed LMEs in H1 2026, against 24 in H1 2025, with coercive uptiers having "all but vanished" in favor of equity handovers and consensual amend-and-extends (9fin, 28 August 2026).
> - **What it means for the desk.** The *level* of the headline default rate is now a weak cycle signal, while the *mix* is a strong one. The count of LMTs fell after 2024; the share of defaults that are soft did not. The technique migrated rather than retreating. Any feature called `default_rate` in your warehouse needs a sibling called `default_rate_ex_de`, and the spread between them is itself a regime variable (§14.7).

How strange is a world in which most defaults happen out of court? Very, by the standards of the shelf.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.87:* "Given the relative simplicity of the out-of-court restructuring, one might well wonder why it is successfully employed less than 10% of the time."
>
> **Annotation.** Moyer was writing in 2004, and his answer was the holdout problem: an exchange offer needed very high participation (he cites thresholds of 85–90% elsewhere in the book), and any holder who refused kept a full claim against a company that the others had just de-levered. Twenty years later, out-of-court restructuring is the *majority* outcome. The holdout problem was not solved by better persuasion. It was solved by contract technology that turned holdouts into victims: if a bare majority can amend the credit agreement, subordinate the minority, or move the collateral to an unrestricted subsidiary, then holding out stops being a free option and becomes a short put. That inversion is the whole LMT era in one sentence, and it is why the 2004 base rates in every distressed textbook are the wrong prior for 2026.

Mags, who remembers 2004 as "recent," takes the long view. "We used to call it a coercive exchange, and it needed ninety percent to work. Now it needs fifty point one percent and a dictionary." She pauses. "The Fifth Circuit, to its credit, eventually bought a dictionary too." (We get to that ruling in §14.6.)

**Quant-shop life (fictional composite): forty-one issuers that cannot agree.** A systematic asset manager, the Tuesday of the week a new vendor default file arrives. Nobody announces the file. It lands in a storage bucket at 6:12 a.m., the ingestion job picks it up at 6:15, and by 9:30 there is a ticket in the queue, DATA-2291, titled "default_flag mismatch, 2023 cohort," assigned to Hana, the junior quant who owns the risk-data pipeline (Chapter 5). Hana has learned that tickets with the word "mismatch" in the title never close on the day they open.

The PD model's training set carries three default columns, because three sources sell default histories and the firm licenses all of them. `default_flag_mdy` is Moody's, with distressed exchanges counted. `default_flag_sp` is S&P's, where an SD counts. `default_flag_vnd` is a vendor's "ex-LME" series, which counts a default only on a filing or a missed payment. On most rows the three agree, because most companies either pay or do not. On the 2023 rows they disagree about 41 issuers *(an invented count for this composite; the real number depends on the vendor and the universe)*. Hana sorts the 41 by date, and the pattern is not subtle. Nearly every one is an uptier, a drop-down or a discounted amend-and-extend. Moody's and S&P say default; the vendor says performing. The model, trained on a column called `y`, has been told both on alternate refreshes, depending on which source a configuration file written in 2021 happened to point at.

The meeting about it lasts fifty minutes, and forty of them are about names. One researcher wants a single `default_flag` with a documented precedence rule. Another wants the three source columns kept forever and a fourth, `default_type`, taking the values `HARD`, `DE` and `NONE`. Someone proposes `default_flag_v2`, and the room goes quiet the way rooms do when everyone remembers `vol_60d_v2`. Theo, invited because he "knows the restructuring side," asks the question he always asks: "What does the credit agreement call it?" Nobody knows, and it turns out to be the right question, because the credit agreement does not call it anything. The exchange was done *under* the agreement, by amendment, and on the company's own documents nothing ever went wrong. The agencies called it a default. The lenders left outside called it something that does not go in a schema.

Then the point-in-time problem arrives, the one Chapter 5 called "what we knew when." One of the 41 was rated SD by S&P for nine days and then B-. The current file shows B-. A back-test run on the current file never sees the SD, and treats a company the market spent nine days pricing as a defaulter as a clean B- credit all along. The fix is dull and correct: store both ratings, each with the time it took effect and the time the firm received it, and make the training job ask for the state *as known* on each date. Hana writes it into the ticket as a schema change, a `rating_event` table keyed on issuer, agency, rating, effective time and received time, and it takes the rest of the week.

By Friday the training set has a `default_type` column, three source flags, and a precedence rule written down where the risk committee can read it. Not one line of the model's own logic has changed, and its validation accuracy has moved by a few points anyway *(illustrative)*, because for two years it had been graded against an answer key that changed with the configuration. That is the "noise in the definition of $y$" from earlier in this section, seen from the desk where somebody has to fix it.

The recovery side has forked the same way. Measured *at the exchange*, recoveries on distressed exchanges look excellent: Moody's put first-lien DE recoveries at 71% at end-2024, up from 55% in 2023 (as reported by Bloomberg Law, *Distress Exchange Leads to Re-Default Half the Time*, 23 April 2025). Measured *at the eventual bankruptcy*, first liens of companies that had done an LME recovered far less. PitchBook, summarizing a Fitch study of 2024 emergences, reported weighted-average first-lien recoveries of 23% for issuers with a prior LME against 53% for those without. We could not open the Fitch original, so treat the pair as indicative rather than gospel. The two numbers are not contradictory. The first is measured at a moment chosen by the borrower, for holders who were in the deal. The second is measured at the next event, which is where the excluded holders' losses and the participants' second haircut actually show up. A recovery database that records only the first number has a survivorship bias with a lawyer.

So "the default rate" is now two numbers, and "the recovery rate" is now at least two distributions. The rest of the chapter builds the machinery to carry both.

### Deep-Dive Resource Graph (§14.1)

- **Practitioner Writing.** Moody's Asset Management Research, *Corporate Credit Risk Looking for a Catalyst to Break Out* (7 August 2025): https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf. Moody's AMR, *"Growth Recession" Hounds Parts of Corporate Credit Market* (6 March 2025): https://www.moodys.com/web/en/us/insights/resources/growth-recession-hounds-parts-of-corporate-credit-market.pdf. Wachtell Lipton, *Liability Management 2026: For Better or Worse* (3 February 2026): https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf.
- **Academic Papers.** Franks & Torous (1994), *A Comparison of Financial Recontracting in Distressed Exchanges and Chapter 11 Reorganizations*, Journal of Financial Economics 35. Altman & Karlin (2009), *The Re-emergence of Distressed Exchanges in Corporate Restructurings*, Journal of Credit Risk.
- **Data & Code.** Federal Reserve, *Financial Stability Report* (May 2026), Figure 2.9 (default rates including distressed exchanges): https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf.

## 14.2 Splitting the Default Intensity: Competing Risks

Every credit model in this book so far has consumed one default intensity, $\lambda_t$. The LMT era asks us to split it. The tool is competing-risks survival analysis, which epidemiologists use when a patient can die of more than one thing, and which credit people should use because a borrower can now default in more than one way.

> **Math, Gently.** *Competing risks: one bucket, two taps.* Fill a bucket with water, one litre for each issuer in a cohort that has not yet had a credit event. Two taps at the bottom drain it. The hard tap lets issuers out through a filing or a missed payment; the soft tap lets them out through an exchange. Each tap runs at its own speed, $\lambda_H$ and $\lambda_D$, and the bucket empties at the combined speed $\lambda = \lambda_H + \lambda_D$. The question a desk asks is not only "how fast is the bucket emptying?" but "of the water that has left, how much went out each tap?" If the taps run at constant speed, the answer is $\lambda_k/\lambda$, and it does not depend on how long you watch: after a month or after ten years, the soft tap has taken the same share. Taps running at about 0.022 and 0.038 per year (the split derived in §14.2.1) take about 36% and 64% of the water, which is the 64% soft share read backwards. The running total that has gone out of tap $k$ by time $t$ is the *cumulative incidence* $F_k(t)$, and the water still in the bucket is the survival $S(t)$; what has left plus what remains is always the whole bucket. The classic mistake, which §14.2.2 calls the Kaplan–Meier trap, is to estimate one tap's flow by pretending the other tap is shut. You treat every issuer that left through the soft tap as if it had quietly walked out of the study, and you end up computing how much water the hard tap *would* have drained from a bucket that nobody else was draining. That bucket does not exist, and the number it produces is too big. The full version is in §14.2.1.

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

In words: everything that has left the bucket, through either tap, plus everything still in it, is the whole bucket. The proof is short and comes after the example.

With constant hazards the integral is elementary:

$$
F_k(t) = \frac{\lambda_k}{\lambda}\left(1 - e^{-\lambda t}\right),
\qquad
\text{DE share} = \lim_{t\to\infty}\frac{F_D(t)}{F_H(t) + F_D(t)} = \frac{\lambda_D}{\lambda_H + \lambda_D}.
$$

With constant hazards the share is the same at every horizon, not only in the limit. A 65% DE share therefore says $\lambda_D/\lambda_H = 0.65/0.35 \approx 1.86$: soft defaults arrive almost twice as fast as hard ones.

Now put Moody's June 2025 numbers through it. Twelve-month default rates are fractions of an issuer cohort, not intensities, so convert first: $\lambda \approx -\ln(1 - 0.058) = 0.0597$ per year. The ex-DE rate is 2.1% of 5.8%, so the DE share is $3.7/5.8 \approx 0.64$. Splitting the intensity in the same proportion gives $\lambda_D \approx 0.038$ and $\lambda_H \approx 0.022$ per year *(approx.; a two-cause conversion of agency rates that ignores within-year timing and withdrawn ratings)*. These are the two numbers we will carry for the rest of the chapter.

#### The Full Derivation

The identity $\sum_k F_k(t) + S(t) = 1$ follows in one line. Note $\sum_k \lambda_k = \lambda$ and $\frac{d}{du}S(u) = -\lambda(u)S(u)$, so $\sum_k F_k(t) = \int_0^t \lambda(u)S(u)\,du = 1 - S(t)$. The constant-hazard formula is the same integral with $\lambda_k$ and $\lambda$ pulled outside: $F_k(t) = \lambda_k \int_0^t e^{-\lambda u}\,du = \frac{\lambda_k}{\lambda}\left(1 - e^{-\lambda t}\right)$.

### 14.2.2 Estimating CIFs without fooling yourself

> **Math, Gently.** *A survival curve is an attendance register.* Take ten issuers and call the roll once a year. Survival is the share still answering "present." In year one, one of them files: one hard default among ten at risk. In year two, one of the nine survivors does an exchange: one soft default among nine at risk. The **Nelson–Aalen** estimator keeps a running tally of how dangerous each roll call was, adding 1/10 to the hard tally at year one and 1/9 to the soft tally at year two; each event is divided by the number of names in the room when it happened. The **Aalen–Johansen** estimator turns those tallies into probabilities by weighting each step by the share still present just before it: $\hat F_H(1) = 1 \times 1/10 = 0.10$, $\hat F_D(2) = 0.9 \times 1/9 = 0.10$, and $\hat S(2) = 0.9 \times (1 - 1/9) = 0.80$. The three sum to one, as they must. Now add one complication: a third issuer's rating is withdrawn after year one, because it was taken private and stopped paying an agency. It did not default. It left the register. That is **censoring**: we know it survived to year one and nothing after. The right treatment is neither to count it as a survivor forever nor as a default, but to drop it from the at-risk count from then on, so later fractions divide by fewer names. With that withdrawal the year-two exchange counts as 1/8, $\hat F_D(2) = 0.9 \times 1/8 \approx 0.11$ and $\hat S(2) = 0.9 \times 7/8 \approx 0.79$, and the three still sum to one. The general formulas follow.

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

The identity $\sum_k \hat F_k + \hat S = 1$ holds exactly at every jump time, for the same reason as in continuous time: each step moves mass $\hat S(t_i^-)\sum_k d_{k,i}/n_i$ out of survival and into the CIFs. If your implementation fails that assert, it has a bug, not a rounding problem. Figure 14.2 draws the identity at the rates of §14.2.1.

![Figure 14.2: The three outcomes always sum to one (left), and treating hard defaults as censoring overstates the chance of a distressed exchange by a gap that widens with the horizon (right, dashed line). Illustrative: closed-form constant hazards of 2.2% (hard) and 3.8% (soft) per year from §14.2.1, with no cures.](assets/figures/ch14_competing_risks_cif.png)

There are four places where intelligent people get this wrong, and the desk found all four the usual way, in an argument.

Kaz goes first, because Kaz has a shortcut. "We don't need a new estimator. Fit a Kaplan–Meier curve to the exchanges, treat the hard defaults as censored, and one minus the curve is the probability of an exchange. Two lines in any survival library."

"No," says Mags, before Kaz has finished, with the certainty of someone who does not yet know why. Then she works out why. "A company that files in year one can't do an exchange in year three. You're counting exchanges the bankruptcy already made impossible."

She is right, and the mistake has a name: **the Kaplan–Meier trap**. Kaz's shortcut estimates the DE probability as $1 - \widehat{\mathrm{KM}}_D(t)$, treating hard defaults as censored. That estimates $1 - \exp(-\int_0^t \lambda_D)$, the probability of a DE *in a world where hard defaults cannot happen*. Since hard defaults do happen, and remove issuers before they can exchange, $1-\widehat{\mathrm{KM}}_D(t) > F_D(t)$ for every $t>0$, and the bias grows with the horizon, as the right panel of Figure 14.2 shows. It is the statistical equivalent of a recovery analysis that assumes the uptier never happened. Our code asserts the inequality so that nobody "simplifies" the estimator later.

Kaz regroups. "Fine. Then a Cox regression on the exchange hazard, to see which covariates matter." That is the second trap, and a subtler one: **regressing on the wrong hazard**. A Cox model fit to $\lambda_D$ tells you how covariates move the *rate* of DEs among survivors. It does not tell you how they move the *probability* of eventually having a DE, because a covariate that raises $\lambda_H$ also lowers $F_D$ by removing issuers early. Theo, who has sat through enough sponsor pitches to know what the real question is, puts it in words: does a sponsor-owned, loan-only capital structure raise the chance that this company's first default is an exchange? That question belongs to the Fine–Gray model on the sub-distribution hazard (Fine & Gray, 1999). The candidate covariates write themselves from Part IV: `sponsor_backed`, `loan_only_structure`, `docs_vintage` (pre- or post-Serta-blocker), `coop_in_place`, and the Priming Risk Score from Chapter 13.

Then Theo asks the question nobody else thought to ask. "What happens to $n_i$ when an agency withdraws a rating?" The answer is the third trap: **rates are not hazards**. Agency default rates are issuer-count fractions over trailing twelve months, with withdrawn ratings handled by agency-specific rules, and every such rule changes the at-risk count without any event happening, which is censoring by another name (the attendance register above). Convert agency rates with $-\ln(1-\text{rate})$ before you put them next to a CDS-implied intensity, and keep the two causes separate when you do (§14.7.2).

Ines, who has been reading markouts through all of this, lands the last one without looking up. "And when you've finished, tell me whether you counted companies or dollars." That is the fourth trap, **count-weighted versus dollar-weighted**. Moody's notes that in June 2025 the default *count* fell while the *dollar volume* more than doubled. A DE share computed by count and one computed by dollars can differ by tens of points in a single month. State which one you are using, in the column name, so that Hana's successor never has to open a ticket about it.

Kaz has been listening with growing alarm. "So the soft default is a default with a bedside manner."

"It's a default that sends flowers," says Mags. "The hard one sends the bill."

**When competing risks are the right tool, and when they break.** The two estimators answer two different questions, and the first judgment is knowing which question you have. If you hold the loan and care about *what* happens to it, the cause-specific cumulative incidence functions are the object: they tell you how much of the cohort will have exchanged, filed, or neither by the horizon you care about, and they feed straight into the expected-loss integral of §14.3.3. If the question is *which features* make the first event an exchange rather than a filing, the sort of question a sponsor-screening model or a Priming Risk Score backtest asks, use the Fine–Gray sub-distribution model, because it puts the covariates on the probability you care about rather than on a rate among survivors. Both break in the same quiet way. They assume that a "D" in the event column means the same thing in every row, and the moment a data team harmonizes Moody's distressed exchanges, S&P's SDs and a vendor's ex-LME flags into one label without a timestamped definition table, that assumption is false and nothing in the likelihood will say so. The fitted CIFs will be smooth, the confidence bands narrow, and the soft share wrong by whatever the label mix happens to be that quarter. A seasoned practitioner reads the label dictionary before the likelihood: which agency, which definition, as of which date, and what happened to the withdrawn ratings. Only then does the estimator get a vote. Hana's forty-one issuers are what this looks like from the inside.

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

> **Math, Gently.** *Lightbulbs, unplugged bulbs, and bulbs that never burn out.* Picture a lab testing a box of lightbulbs by switching them on and writing down when each one fails. Three things make the study harder than it sounds. First, some bulbs are unplugged before they fail, because the budget ran out or the lab moved; we know they lasted *at least* that long and nothing more. That is **censoring**, the withdrawn-rating problem of §14.2.2 again, and the exchanges of 2024 and 2025 are the bulbs most recently plugged in. Second, bulbs can fail more often as they age, the way a filament thins ($k>1$ in a **Weibull** distribution), or less often as they age, because the defective ones go first ($k<1$), or at the same rate whatever their age, which is the exponential of §14.1 ($k=1$). The Weibull is the exponential with one extra dial, the shape $k$, which says whether time makes things worse or better; a second dial, the scale $\eta$, says roughly how long a typical failure takes. Third, and this is the part that matters here: suppose three-quarters of the box are LEDs that will not fail on any clock the study can run. Then no amount of waiting will see most of the box fail, and any model whose curve must eventually reach 100% is wrong in the long run however well it fits the first year. The fix is a **cure fraction**: say a share $p$ of the bulbs are the failing kind and $1-p$ are not, and give only the failing kind a Weibull clock. Worked: with $p = 0.25$, $k = 1.2$ and $\eta = 1.71$ years, a failing-kind bulb has a $1 - e^{-(2/1.71)^{1.2}} \approx 0.70$ chance of going within two years, so a bulb picked at random from the box fails within two years with probability $0.25 \times 0.70 = 0.175$, and fails ever with probability 0.25. Swap "bulb" for "issuer after an exchange" and "fail" for "hard default," and those are the Moody's facts below. The calibration algebra is in The Full Derivation later in this subsection.

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

**Calibration.** Each Moody's fact turns one dial. Fact 1 sets $p = 0.25$ for hard default (use $p \approx 0.35$ to $0.40$ if your event is "hard default or another DE," which is fact 2). Fact 3 says the fraction of eventual defaulters who default by $u=2$ is $0.70$, which leaves one equation linking $\eta$ and $k$, $\eta = 2/1.204^{1/k}$ (derived below). So fact 3 pins $\eta$ once $k$ is chosen. Fact 4 then pins $k$, which is the part people get wrong. The increase in cumulative incidence over year six is $p\,[S_0(5) - S_0(6)]$:

| Shape $k$ | Scale $\eta$ (years) | Hazard among the susceptible | Year-six increment $p\,[S_0(5)-S_0(6)]$ | Consistent with fact 4? |
| :--- | :--- | :--- | :--- | :--- |
| 0.7 | 1.53 | decreasing | 0.68 pp | No |
| 1.0 | 1.66 | constant, 0.60/yr | 0.56 pp | Borderline |
| 1.2 | 1.71 | increasing | 0.39 pp | Yes |

The intuitive guess is a decreasing hazard ($k<1$): the weakest credits fail first. The Moody's facts reject it. Given that a quarter fail eventually and 70% of those go within two years, a decreasing-hazard Weibull leaves too much mass in the long tail. The data want $k$ at or slightly above one, and that has an economic reading every RSSG banker will recognize. Among the susceptible, the hazard starts *low* and *rises*, because the exchange bought runway. Defaults come when the new money runs out, not the morning after the closing. Figure 14.3 plots the three clocks beside ROBO's exponential.

![Figure 14.3: Left: all three Weibull shapes pass through the same two-year anchor and flatten at the 25% cure ceiling, while ROBO's exponential keeps climbing, reaching two-thirds by year ten, because its hazard never decays. Right: the cure model's population hazard falls toward zero as cured issuers come to dominate the survivors, while the exponential's stays at 0.11 a year. Illustrative: the mixture-cure Weibull of §14.3.2 with p = 0.25 and the scale solved from the Moody's 70%-within-two-years fact (Hamilton, 18 May 2026).](assets/figures/ch14_redefault_clock.png)

#### The Full Derivation

The population hazard follows from the mixture survival function by the definition $h(u) = -\frac{d}{du}\ln \mathbb{P}(U>u)$. The derivative of $(1-p) + p\,S_0(u)$ is $-p\,f_0(u)$, so $h_H(u) = p\,f_0(u)/[(1-p) + p\,S_0(u)]$, which is the formula above.

For the scale, fact 3 says that of the eventual hard defaulters, 70% default by $u = 2$. The eventual defaulters are the susceptible fraction, so the condition is on $S_0$ alone:

$$
\frac{F(2)}{p} = 1 - S_0(2) = 0.70
\;\Longrightarrow\;
\left(\frac{2}{\eta}\right)^k = -\ln 0.30 = 1.204
\;\Longrightarrow\;
\eta = \frac{2}{1.204^{1/k}} .
$$

At $k = 0.7$, $1.0$ and $1.2$ this gives $\eta = 1.53$, $1.66$ and $1.71$, the scale column of the table. For the year-six column at $k = 1.2$: $S_0(5) = \exp[-(5/1.71)^{1.2}] \approx 0.027$ and $S_0(6) = \exp[-(6/1.71)^{1.2}] \approx 0.011$, so $p\,[S_0(5) - S_0(6)] \approx 0.25 \times 0.016$, about 0.4 percentage points (the table's 0.39, which carries more decimals), under fact 4's half-point ceiling. The same arithmetic at $k = 0.7$ gives 0.68 points, which is why the decreasing hazard is rejected.

That is where the 13-week model comes back from the dead. In a hazard regression the covariates enter through the cure fraction and the scale:

$$
\operatorname{logit} p_i = \mathbf{x}_i^\top \boldsymbol\beta_p,
\qquad
\ln \eta_i = \mathbf{x}_i^\top \boldsymbol\beta_\eta,
$$

with $\mathbf{x}_i$ containing `liquidity_runway_weeks` (literally the output of Theo's USB stick), `new_money_fraction`, `maturity_extension_years`, `lme_type` (uptier, drop-down, amend-extend-and-exchange), `sponsor_backed`, `coop_in_place`, and `docs_vintage`. The runway variable should raise $\eta$ (later failures) and the new-money variable should lower $p$ (fewer failures). Maturity extension on its own should do little to either. An amend-and-extend that adds no new money moves the cliff three years to the right and leaves the car in the same gear.

> **Math, Gently.** *The logit link, or odds as a betting line.* A probability has to live between 0 and 1, but a regression score $\mathbf{x}^\top\boldsymbol\beta$ can land anywhere on the real line, so the model needs a translator. Bookmakers already have one: odds. A probability of 0.25 is odds of 1 to 3, one chance for and three against; a probability of 0.5 is evens. Odds run from zero to infinity, and their logarithm, the **log-odds** or **logit**, $\operatorname{logit} p = \ln[p/(1-p)]$, runs from minus infinity to plus infinity, which is exactly the range a linear score covers. The way back is the inverse logit, $p = 1/(1+e^{-z})$. A score of zero is evens, $\operatorname{logit}^{-1}(0) = 0.5$. Add one unit and you are at $1/(1+e^{-1}) \approx 0.73$; subtract one and you are at 0.27. Each unit of score multiplies the odds by $e \approx 2.7$ wherever you start, so a coefficient reads as "this feature multiplies the odds of being in the susceptible group by $e^{\beta}$." The scale $\eta$ gets a log link instead, for the same reason one level down: $\eta$ must be positive, and $\ln \eta$ can be anything. Log-odds first appeared on this desk in §3.2.2, turning an RFQ into the chance of trading against someone informed; they come back in §14.4.2 and §14.6.1.

Theo reads the covariate list twice before he sees it. `liquidity_runway_weeks`. He plugs in the USB stick, opens the model he built at RSSG and has rolled forward every week since out of something between habit and grief, and scrolls to the last row. Every 13-week cash flow model ends in the same place: the week in which cash crosses the minimum-liquidity line. "That's my bottom line," he says. "Literally. The last row. That's the covariate that moves $\eta$." He had spent three weeks assuming that the thing on the stick was the part of his old life he would have to leave at the door. It turns out to be a feature.

Kaz, who has never read a credit agreement, asks the question that proves it. "What does a PIK toggle do to runway? 'Toggle' sounds like a light switch. Does the company turn the interest off?"

"More or less," says Theo. "For a while it can pay interest in more debt instead of cash. Cash interest goes down, so runway goes up. The principal grows. You've bought time and paid for it out of recovery."

"So it raises $\eta$ and raises $L$," says Kaz. "Both at once. That's not a covariate, that's a trade."

"And it may lower $p$, if the extra time lets the business recover, or do nothing to $p$ at all if it just moves the cliff," says Mags. "Back in my day we called that extend and pretend, and we did it by fax."

Theo wants a check against something real, and Mitel is the obvious one. In October 2022 Mitel's participating lenders put in about \$156mm of new first-out money (§14.8.2). He does not have Mitel's weekly cash burn, and he does not invent it; the reading this chapter uses is that the new money bought about two and a half years of runway. Mitel filed its prepackaged Chapter 11 on 10 March 2025, 29 months after the uptier. The clock and the cliff landed within a few months of each other. "So the runway was the clock," says Ines, "and the clock was right."

"Then the hazard regression," says Kaz slowly, "is your thirteen-week model with a link function."

"Please don't tell my old MD," says Theo.

Three ways to get this wrong:

- **Right-censoring.** Exchanges done in 2024 and 2025 have one or two years of follow-up. A naive estimate of $p$ that counts "no hard default yet" as "cured" is biased low, badly, for exactly the cohort you care about.
- **Identifiability.** With short follow-up, a small $p$ with a long $\eta$ and a large $p$ with a short $\eta$ fit the early data equally well. Fix $k$, or put a prior on it from the long-run study, and let the recent cohort move $p$ and $\eta$ only.
- **Left truncation.** If your sample is "issuers still in the database when it began," early failures are missing. Enter each issuer at its exchange date, not at the sample start.

> **Ways This Blows Up.** *What ROBO built from the vague version.* Asked to "model time to re-default," ROBO fit an exponential to a sample with fourteen months of follow-up. It reported a hazard of about 0.11 per year and an expected time to hard default of more than nine years, with a straight face. Both halves are wrong, in opposite directions. The exponential has no cure fraction, so it implies that about two-thirds of the cohort hard-defaults within a decade, against Moody's quarter. And it smears the defaults that do happen, which are front-loaded, across a decade. The fix is not a better optimizer. It is a model with a parameter for "never," plus a spec that says so (§14.7).

Before the ledger, a warning about reading it. The box below carries five numbers that look as if they cannot all be true: about 25% of soft-event borrowers eventually hard-default; 46% of one cohort had re-defaulted within two years; only 22% of coercive deals got through two years clean; roughly a third filed; 56% filed or went to CCC. A desk that reads them as five noisy estimates of one quantity will average them, get something near 40%, and be wrong about every name it owns. They are five estimates of five different $p$'s. The 25% is hard defaults only, over every soft event in Moody's database since 1979. The 46% counts a repeat exchange as a re-default and is a single, stressed vintage. The 22% is a survival rate, not a default rate, for coercive non-pro-rata deals only, the riskiest slice. The third and the 56% come from a CLO-focused sample in which "re-defaulted or rated CCC+ or below" is one bucket. Change the cohort or the event definition and you change $p$, and the mixture-cure model is built to let you do exactly that: one $p$ per deal type and vintage, one $\eta$ tied to runway, and a shape $k$ shared across all of them from the long-run study. If you want to hear the authors of the most-quoted study state their own caveats aloud, the *Cloud 9fin* episode "LME Doomscrolling: Data-driven reality check" (7 April 2026; https://share.transistor.fm/s/1f62123b) has Mark Roe and Vasile Rotaru walking 9fin's Laurie Tomassian through what their sample does and does not cover.

> **Trend Watch.** *The re-default ledger, 2020–2026.*
> - **Long-run baseline.** Of 1,173 soft-event borrowers since 1979, about one in four hard-defaulted and more than 70% of those did so within two years (Moody's, 18 May 2026).
> - **The 2023 cohort ran hot.** About 46% of 2023 distressed exchanges had already re-defaulted by April 2025, most in under a year, against a historical average of about 3.5 years (Moody's, as reported by Bloomberg Law, 23 April 2025). That figure reportedly counts repeat exchanges as re-defaults.
> - **Coercive LMEs run hotter.** In 89 coercive non-pro-rata LMEs, fewer than half avoided bankruptcy or re-default within one year and only 22% within two. Of the firms with at least two years of history, 56% had filed, and LME debtors spent two to three times longer in bankruptcy than prepackaged cases (Roe & Rotaru, Harvard Law School Bankruptcy Roundtable, 24 February 2026).
> - **The CLO view.** S&P CLO research, as relayed by Wellington (1 April 2026; secondary), finds that roughly a third of issuers filed after an LME, about 56% re-defaulted or were rated CCC+ or below, and about 10% repaid or reached B- or better.
> - **The names.** Serta: uptier closed 22 June 2020, Chapter 11 on 23 January 2023, about 31 months. Mitel: uptier October 2022, Chapter 11 in March 2025, about 29 months. Wesco/Incora: one-day notes transaction 28 March 2022, Chapter 11 on 1 June 2023, about 14 months (the rulings that followed, 10 July 2024 oral, 17 January 2025 written, 8 December 2025 reversal, are in the §14.6 Docket Diary and Chapter 13). Robertshaw: 2023 LME, Chapter 11 on 15 February 2024. Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 in July 2025, about 11 months (docket date not verified). Filing dates are as reported from the S.D. Tex. and D.N.J. dockets in the case dossiers and secondary sources; we did not open every docket ourselves.
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

The naive model is wrong on average, understating the blended loss by more than a point, and wrong in the cross-section, where the two sides of the same class are four points apart over three years. The exact integral gives slightly lower numbers, because an exchange in year 2.9 has little time to re-default before $T$. Our engine computes the exact version and checks it against Monte Carlo. The four-point gap comes almost entirely from one variable, and the next section is about that variable.

## 14.4 Recovery Is a Mixture over Coalition Membership

The recovery models on the shelf index $R$ by seniority, industry, and the cycle. They also assume something the LMT era has broken.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.357:* "Its precise distribution is not given, but it is assumed to be independent of default and any other recovery events."
>
> **Annotation.** Bolder is describing the standard industrial assumption that recovery is an independent draw. In a non-pro-rata transaction, recovery is not a draw at all. It is the outcome of a negotiation in which the participants' recovery is funded, in part, by the non-participants' loss. The two are negatively dependent by construction, within the same class, on the same day. Independence also fails across time: the exchange that sets your recovery also resets your re-default clock (§14.3). A 2026 desk keeps the Beta machinery from Chapter 5 but replaces the single draw with a mixture whose weights are a model output.

### 14.4.1 Two humps, not one bell

> **Math, Gently.** *Two humps, or why a room's spread can be mostly the gap between groups.* Measure the heights of everyone at a school open evening, half parents and half children. The room's average is somewhere around 1.4 metres, a height almost nobody in the room has. The room's spread is large, but not because adults vary much among themselves or children among themselves; most of it is the gap between the two groups. That is a **mixture**: first a coin decides which group you are in, then a group-specific distribution decides your height. The **law of total variance** makes the split exact: total variance is the average variance *within* the groups plus the variance *between* the group averages. With a coin that lands "adult" with probability $\pi$ and group averages a gap $\Delta$ apart, the between part is $\pi(1-\pi)\Delta^2$. Recovery after a non-pro-rata deal is the same room, and the next question is which distribution each group should get. Not a **normal**: its bell has tails running past 0 and past 100 cents, so it puts weight on recoveries below nothing and above par. Not a **lognormal**: it cannot go negative but has no ceiling, so it still puts weight above par. A **Beta** distribution lives on $[0,1]$ exactly, as a recovery measured as a fraction of par does, and with its two parameters it can be a hump near 0.74, a hump near 0.25, or a U with mass piled at both ends (its first-use box is in §5.5.2). Worked: with $\pi = 0.526$ and group means of 74 and 25 cents, a gap of 49 points, the between-group standard deviation is $\sqrt{0.526 \times 0.474} \times 49 \approx 24.5$ points of par, from membership alone. The formulae follow, the derivation comes after the example, and Figure 14.4 draws the room.

Let $\pi = \mathbb{P}(\text{holder is in the majority group})$. Conditional on a default event in which classmates are treated differently,

$$
R \sim \pi\,\mathrm{Beta}(a_{\text{in}}, b_{\text{in}}) + (1-\pi)\,\mathrm{Beta}(a_{\text{out}}, b_{\text{out}}),
$$

with group means $\mu_g = a_g/(a_g+b_g)$ and variances $\sigma_g^2 = \mu_g(1-\mu_g)/(a_g+b_g+1)$. The mean recovery is the coin-weighted average of the two group means, $\pi\mu_{\text{in}} + (1-\pi)\mu_{\text{out}}$, and the variance splits, exactly as in the school hall, into a within-group part and a between-group part, $\pi(1-\pi)(\mu_{\text{in}} - \mu_{\text{out}})^2$. The between-group term is the variance of a Bernoulli($\pi$) scaled by the squared gap in means. It is largest at $\pi = 1/2$, which is where a bare-majority uptier sits by design.

Now put Serta in. On the facts recited in the July 2026 remand opinion, participating lenders held about \$992mm of a \$1.887bn first-lien class, so $\pi \approx 0.526$. They exchanged at 74 cents, so $\mu_{\text{in}} \approx 0.74$, and the court valued the excluded loans at \$0.25, so $\mu_{\text{out}} \approx 0.25$. (Reading the exchange ratio and the court's valuation as "recoveries" is our *illustrative* interpretation.) Then $\mathbb{E}[R] \approx 0.51$, and the between-group variance is

$$
0.526 \times 0.474 \times (0.74 - 0.25)^2 \approx 0.0599,
\qquad
\sqrt{0.0599} \approx 0.245 .
$$

A standard deviation of about 24.5 points of par, *from membership alone*, before any within-group noise. Figure 14.4 draws the two humps behind that number.

![Figure 14.4: The Serta class splits into two recovery humps 49 points apart, and a single Beta with the same mean and standard deviation (24.9 points: the 24.5 from membership alone plus a little within-group noise) peaks at a recovery that almost nobody receives. Illustrative: π = 0.526, Beta(74, 26) for participants and Beta(25, 75) for excluded lenders, with the 52.6%, 74 and 25 taken from the Serta remand facts (Mayer Brown, July 2026) and the Beta concentrations assumed.](assets/figures/ch14_two_humps.png)

#### The Full Derivation

Let $M$ be the membership indicator, so $M = 1$ with probability $\pi$ and $R \mid M$ is the Beta for the holder's group. The law of total variance, $\mathrm{Var}[R] = \mathbb{E}[\mathrm{Var}(R\mid M)] + \mathrm{Var}(\mathbb{E}[R\mid M])$, gives

$$
\mathbb{E}[R] = \pi\mu_{\text{in}} + (1-\pi)\mu_{\text{out}},
\qquad
\mathrm{Var}[R] = \underbrace{\pi\sigma_{\text{in}}^2 + (1-\pi)\sigma_{\text{out}}^2}_{\text{within groups}} + \underbrace{\pi(1-\pi)(\mu_{\text{in}} - \mu_{\text{out}})^2}_{\text{between groups}} .
$$

The first term is the average of the two conditional variances. The second is the variance of the conditional mean $\mathbb{E}[R \mid M]$, a two-point random variable equal to $\mu_{\text{in}}$ with probability $\pi$ and $\mu_{\text{out}}$ otherwise; its variance is $\pi(1-\pi)$ times the squared distance between the two points.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.103:* "The table supports our opinion that recovery rates decrease during recessions and increase during expansions."
>
> **Annotation.** The table is Moody's 1970 to Q2 2002 recovery data via Schuermann: mean recovery 27.85% in recessions (standard deviation 25.67%), 43.10% in expansions (27.11%), and 40.07% overall (27.50%). That is the classic regime shift in recovery, and it is real: the macro state moves the mean by about fifteen points. Compare our Serta arithmetic. One binary variable moves the mean by 49 points, and its between-group variance of 0.0599 is about four-fifths of the *entire* variance of the 1970–2002 recovery distribution ($0.275^2 \approx 0.0756$). One deal is an illustration, not an estimate. The structural point survives: the LMT era added a second regime axis, orthogonal to the cycle, and on it the regimes are further apart.

Ines puts it in her terms. "A 40% average recovery with a 25-point standard deviation isn't a distribution. It's two distributions that were introduced at a conference."

What does the trend in $\mu_{\text{out}}$ look like? The early uptiers were winner-take-all: Octus measured 100% of value moved away from non-ad-hoc creditors in Wesco, Mitel and Robertshaw, while the six most recent of its eleven non-pro-rata uptiers averaged about 18% (Octus, 16 July 2024). In ConvergeOne, minority lenders' recoveries were about 30% lower than the majority's within the same class (Harvard Law School Bankruptcy Roundtable, 25 November 2025). The market moved from "the minority gets nothing" toward "inclusive but unequal." In mixture terms, $\mu_{\text{out}}$ rose and the gap shrank, but it did not close. "Recovery compression" is the wrong name for what happened. The averages compressed while the distribution split into two humps.

### 14.4.2 The new first stage

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.305:* "However, in our own research, we have found that they account for only about 40 percent of the power we are able to attain in predicting levels of recoveries."
>
> **Annotation.** "They" are lookup tables of historical recoveries by seniority and industry. Bohn and Stein's point was that a model with firm and market covariates does far better than the table. On a 2026 desk the gap is wider, because the most predictive covariate is not in any table: which side of the room you were on. The same authors recommend a two-stage LGD model, a probit for whether any loss occurs given default followed by a regression for its size (p.316). The LMT era adds a stage *before* those two.

The engine becomes a three-stage model, and the easiest way to see why is to watch Mags explain the first stage to someone who has never had to read the document it comes from.

"You can't observe who's in the room until the deal closes," says Kaz. "So how do I estimate $\pi$ for a holder before then?"

Mags pulls up a Rule 2019 statement from an old Chapter 11. "Same way I always did. This is the one time an ad hoc group has to tell the world who it is. Bankruptcy Rule 2019 makes a group that acts for more than one creditor file a verified statement: every member, and what each of them holds in each class, as of a date. Out of court you get press leaks and cleansing materials. In court you get the register." She scrolls. "Start with size. This one holds four percent of the first lien by itself; that's a phone that rings. Then type. That name ending in 'CLO 2019-1 Ltd.' is a CLO, and CLOs are bad at writing new-money checks. This one's a multi-strategy fund. This one's a distressed specialist that has been in three groups with the same financial adviser in five years. Then look at who's missing. If the class is sixty percent CLO and the group has none of them, you already know which hump the CLOs are in."

"And the co-op," says Theo. "Whether there is one, and what kind."

"That's §14.5," says Mags. "But yes."

Kaz writes it down the way Kaz writes everything down, as a model. **Stage 0, membership**: $\pi_i = \operatorname{logit}^{-1}(\mathbf{z}_i^\top\boldsymbol\gamma)$, a logistic model (the logit box in §14.3.2) for the probability that holder $i$'s position ends up inside the deal. Its features are the RSSG instincts Mags just read off the register, made explicit: position size relative to the class, holder type (CLO, multi-strategy fund, distressed specialist, bank), co-op membership and type (§14.5), whether the holder has been in a prior group with the same sponsor's advisers, and the CLO share of the class.

"Then the old question," says Mags. "Do you lose anything at all? Insiders in a good deal take out the first-out at or near par. Outsiders almost always lose something." That is **Stage 1, any loss**: a probit for $\mathbb{P}(L > 0 \mid \text{default}, M)$, as in Bohn–Stein, now conditional on membership.

"And then how much," says Kaz, "with a pile at zero for the insiders who are made whole and a pile at one for the outsiders who get nothing." That is **Stage 2, severity**: a Beta regression for $L \mid L > 0, M$, with the zero- and one-inflation masses of Chapter 5 given membership-specific weights.

"Now you're reading," says Mags.

Stage 0 is not a portfolio-level number. It is a property of the *holder*, so the same loan has a different expected recovery in different hands. That sounds like heresy until you remember that it is what the Serta remand court computed in dollars.

> **View From Another Seat.** *The direct lender: you do not get to choose your hump, because you are the class.* Everything in this section assumes a holder who is one of many in a syndicated class, choosing, or failing to choose, a side. A direct lender holding most or all of a loan has no side to choose. When the borrower runs out of runway there is no majority to join; the direct lender *is* the required lender, its "recovery" is a mark it sets itself, and the restructuring is an amendment it writes itself. Pluralsight shows what that looks like in public filings. Ares Capital (ARCC) held a \$106.2mm first-lien loan to Pluralsight, marked at 89.0 at 31 December 2023 and 48.0 at 30 June 2024, and on 30 September 2024 converted it into about \$54.7mm (at cost) of new first-lien paper and equity, with a \$60mm realized loss (ARCC 10-Q filings). Another BDC lender in the same loan carried it at 96.8 at the end of 2023, according to its own filing: two lenders, one loan, one date, almost eight points apart. Nothing in that sequence was a vote among strangers, and no Rule 2019 statement would have told anyone anything the lenders did not already know. This seat's question is not $\pi$. It is whether to put in new money and own the company, which is a private-equity decision dressed as a credit one. ARCC's president has said publicly that "we will walk away from transactions based on documentation terms" (Jim Miller, ARCC Q4 2025 earnings call, 4 February 2026), which is the direct lender's version of choosing its hump: write the document so that nobody else can get into the room. For the systematic desk, the private mark is the dataset. A mark that falls forty points in two quarters and then converts into equity is a distressed exchange in everything but an agency's name, and a PD model's labels should treat it as one.

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

**Lumen, 31 October 2023 to 22 March 2024: the co-op as the deal.** The desk keeps a folder called "Replays." Each one is a real credit event cut off at a date, with nothing in it that was not public by that date: the filings, the vendor price sheets, the press, and whatever the desk itself traded. Ines runs one on a Friday afternoon every few weeks, and the rule is that nobody may mention anything that happened after the cut-off. Today's folder is Lumen Technologies, and the cut-off is 10 November 2023. Mags and Ines were on the desk then. Theo was still at RSSG, watching the deal from the other side of the street, and Kaz was finishing a postdoc on rough paths. So for two of them this is history and for two of them it is a hand they have never seen.

"We were outside the room on this one," says Ines, "which makes it the best kind of hand history. You get to see exactly what not being in the room cost, to the point."

The folder opens on Tuesday, 31 October 2023. Lumen, the telecom company that owns, among other things, Level 3's fiber network, had a wall: roughly \$10bn of Lumen and Level 3 debt due in 2027. That morning it filed an 8-K announcing a transaction support agreement with a group of creditors holding "over \$7 billion" of its debt. The headline terms were \$1.2bn of new Level 3 first-lien money, in 11% first-lien notes due 2029, with backstop economics that CreditSights summarized as a \$200mm fee plus 5% of the new money, about \$60mm. Level 3's existing 3.4% 2027 and 3.875% 2029 first-lien notes could be exchanged at a 66.7% consent threshold. Up to \$2bn, about 51%, of Level 3's unsecured notes would move into a new second lien. Lumen's term loans would go 85% into super-priority paper.

Kaz reads the 8-K twice, looking for a list. "Who's in the group?"

"Nobody you can name from the 8-K," says Mags. "The filings don't say. Read the advisers."

That is Theo's part of the replay, and he is good at it, because it is the part of a deal he used to live in. Lumen's financial adviser is Guggenheim and its counsel is Wachtell. The creditors have their own financial adviser, and Houlihan Lokey's own deal page later describes itself as the exclusive financial adviser to an ad hoc group of crossholders holding about \$11bn of Lumen debt. Theo puts the word on the whiteboard and underlines it: *crossholders*.

"That's the whole deal," he says. "Lumen has silos. There's debt at the parent, debt at Level 3, debt at Qwest, and each silo has its own collateral and its own guarantees. A holder who owns paper in only one silo wants value moved *into* that silo. A crossholder owns paper in several, so it can agree to move value from one silo to another, because it's on both ends of the transfer. The company needs somebody who can say yes in more than one room at once. The crossholders are the only people who can."

"So who needed whom?" asks Ines, which is the question she always asks of a restructuring, and the one Theo was trained to answer in a pitch book.

"Lumen needed the 2027 wall moved, and it needed new money to do it, and it needed enough consents in each silo to amend the documents: two-thirds for the Level 3 secured, a bare majority for the unsecured. The crossholders needed to be the ones who supplied the money and the consents, because whoever does that gets the new first lien, the fees, and the exchange ratios. Everyone else gets primed." He points at the screen. "And look at the fee stack. Company financial adviser, company counsel, creditor financial adviser, creditor counsel, backstop fees. This was priced and papered for months before the 8-K. By the time we read it, the hand was over. We're reading the hand history of a hand we weren't dealt."

The next document in the folder is the CreditSights price sheet for the week of 9 November 2023, and it is the reason the replay exists. It lists the bonds that were *not* tendered into the agreement, the non-TSA paper, and the ladder is a lesson in what seniority labels are worth once a coalition has formed. At Lumen, the 4% secured notes due 2027 are at 57 and the 5.125% 2026s at 52; the long unsecured bonds from 2028 to 2042 are in the high 20s; the term loan B is at 75. At Level 3, the 3.4% first-lien 2027s are at 83 and the 3.875% first-lien 2029s at 73; the unsecured 2027s at 59, the 2028s at 47, the 2029s at about 40. And across the ladder, by CreditSights' estimate, the same bond held by a TSA signer was worth about ten points more than the identical bond held by someone who had not signed. About 49% of Level 3's unsecured notes, \$1.94bn to \$1.97bn of face, were on the wrong side of that line, primed by the new second lien that the other 51% would receive. *(Prices are vendor-indicative, not trades.)*

Kaz loves this table the way some people love a train timetable. "Ten points between two copies of the same bond. Same coupon, same maturity, same issuer, same indenture. The only difference is a signature." Kaz does the arithmetic aloud, because Kaz always does. "On \$20mm face, ten points is \$2mm. So a signature is worth \$2mm. That's the price of a signature."

"No," says Mags. "If signatures were for sale at \$2mm, you'd buy a non-TSA bond at 47, sign, and sell it on as a TSA bond at 57, and you'd keep doing it until the gap closed. It doesn't close. Read the terms again. The signer's bonds can only be transferred to another signer. A non-TSA bond can be sold to anyone, and a TSA bond can be sold only to someone who is already inside or agrees to join. And nobody is offering you a seat." She taps the line that says the note deals are privately negotiated. "The ten points isn't the price of a signature. It's the price of a closed door. The transfer restriction is what keeps it closed."

Theo sees it before Kaz does. "That's §14.4. Two humps in one issuer, ten points apart, and the deal hasn't even closed. The coin that decides which hump you're in was tossed in the summer, in a room with the crossholders' advisers in it, and the transfer restriction stops anyone from tossing it again in the secondary market." Stage 0 of the recovery model, he realizes, is not a forecast here. For a holder outside the group on 10 November, membership is already a known zero, and the only uncertainty left is what the outside hump turns out to be worth.

"Then why does anyone sell the non-TSA bond at all?" asks Kaz. "If it's going to be primed, it should be worth less than 47. If the co-op could break, it should be worth more."

"Now you're asking the right question," says Ines. She draws the table. Two piles of chips, one large and one small. "The deal needs two-thirds of the Level 3 secured to call, and fifty point one percent of the unsecured. That's how many players at the table have to push their chips in. The crossholders already have more than seven billion dollars' worth of chips in the middle and they've signed an agreement not to pick them up. You're sitting outside the group with twenty million. You can't stop the hand. The only things you can do are fold, which means sell at 47 to someone who thinks the odds are better than you do, or stay in and hope something happens on the turn, or try to buy a seat at a table that isn't selling them."

"What's the pot?" Theo asks, before she can.

"Twenty million face at 47 is \$9.4mm. That's what you'd get for folding now." She writes the question on the board in block capitals, which she does only in replays:

*It is 10 November 2023. You own \$20mm of Level 3 2028s at 47. You have not signed, and once you sign, transfers to non-parties will be void. Sign, sell, or hold, and why?*

The room argues for twenty minutes, which is the point of a replay. Kaz wants to sell. "The co-op has more than \$7bn of a structure where the deal needs two-thirds and one-half. Unless a large fraction of them defect, the deal closes and we're primed. Sell at 47 and stop thinking about it."

Mags wants to hold. "Primed isn't zero. Lumen is a real company with real fiber, and the reason they're doing this out of court is that the business has assets somebody will buy. Primed paper in a company that sells assets gets paid. Primed paper in a company that files gets an adversary proceeding and four years."

Theo wants to know whether "sign" is even on the menu. "The term-loan pieces might be open to everyone. The note deals are negotiated with the group. If the company doesn't need our consent to cross the threshold, it has no reason to let us in. We can't sign a document nobody has sent us." He looks at the board. "The real choice is sell or hold. 'Sign' is a fantasy for a holder our size who wasn't in the room in the summer."

"That's the answer to Kaz's question about why anyone sells," says Ines. "Some holders can't sign and can't wait. A high-yield fund meeting redemptions, or a CLO holding the term loan with a test date at month-end, isn't asking what the paper is worth in two years. It's asking what it's worth by the 30th."

Then she closes the folder on 10 November and opens the next one, which is the part where the replay gives the answers.

On 22 January 2024 Lumen signed an amended and restated transaction support agreement, announced a few days later, that covered "over \$12.5 billion" of debt and commitments, more than 70% of Lumen and Level 3 debt maturing through 2027. The new money grew to \$1.325bn, alongside a new revolver of about \$1bn. The terms said in public what the November prices had already implied. The term-loan pieces were open to all lenders. The note deals were privately negotiated and, in the 8-K's own words, "not offered to all holders." The closing thresholds were 66.7% for the Level 3 secured notes, 50.1% for the unsecured, and 95% for Lumen's Term A and A-1 loans. Each subscriber's share of the new money was capped at \$250mm, which spread the economics across the group and kept any one member from becoming the group. Transfers of a signer's debt to non-parties were void. The outside date was 29 February 2024.

"There's the door," says Mags. "In writing."

The deal closed on 22 March 2024. Lumen reported more than \$15bn of debt and commitments in the transactions, with participation of 94.4% in the Lumen Term A and A-1 loans, 98.5% in the Lumen Term B and 99.5% in the Level 3 Term B. The 2025 and 2026 maturities fell from about \$2.1bn to \$600mm. The 2027 maturities, the wall that had started it, fell from about \$9.5bn to \$800mm. The new money came in as \$1.325bn of secured notes due November 2029.

Kaz looks at the participation numbers for a while. "Ninety-four to ninety-nine and a half percent. With thresholds of fifty and sixty-seven. They didn't just clear the threshold, they buried it."

"That's what a co-op is for," says Ines. "A co-op that clears the threshold by a hair is a coalition. A co-op that clears it by thirty points is the deal."

Then comes the part of the replay that the desk finds hard to sit through, because it is where the people who did nothing were paid. On 17 September 2024 Lumen launched follow-on exchange offers aimed at the non-participants: \$500mm of new 10% Lumen secured notes and \$350mm of 10% Level 3 second-lien notes due 2032. It offered \$975 per \$1,000 for the Lumen 4% secured 2027s, of which 80.8% tendered, \$700 for the 4.5% 2029s, of which 20.9% tendered, and \$860 for the Level 3 4.25% 2028s. Paper that had been 47 in November 2023 was being offered 86 ten months later, in new secured paper. On 2 February 2026 Lumen closed the \$5.75bn sale of its consumer fiber business to AT&T and used about \$4.8bn to retire super-priority debt, leaving total debt under \$13bn, interest about \$300mm a year lower, and net leverage under four times. On 20 May 2026 a cash tender capped at \$750mm took in the Level 3 4.25% 2028s at about 99.4% of par, early premium included. We found no lawsuit by the excluded holders; CreditSights called their indenture claims "difficult," and in the end nobody needed to file one.

Kaz is quiet for a moment, which for Kaz is a long time. "So the holder who did the 'wrong' thing, sat outside, didn't sign, didn't sell, got 86 in new paper in ten months, or about 99 in cash in two and a half years. The holder who sold at 47 to stop thinking about it got 47."

"With hindsight," says Ines. "On 10 November 2023 you didn't know there'd be an AT&T sale. You didn't know the company would want to clean up its stubs. Nobody in the replay folder did. If Lumen had filed instead, the holdout would have been the excluded class in a Chapter 11 with a new super-priority layer in front of it, and you'd be reading about it in §14.8 next to Serta."

"So the answer is 'hold'?" asks Kaz.

"The answer is that 'hold' was a bet on two things," says Theo, "and only one of them was about the co-op. The co-op was going to win. Anyone who could read the advisers' list and the thresholds could see that. The bet was on what came after: whether the company would have assets to sell and a reason to buy back the stubs, or whether it would file. That second bet is the re-default clock from §14.3. Lumen got runway, used it, sold something, and the cure fraction swallowed it. It was one of the three-quarters."

Mags, who has been waiting, gives the lesson the way she always gives lessons, as a correction. "Moyer said the holdout problem was why out-of-court deals failed: holdouts keep their full claim and the deal can't get done. Then contract technology turned the holdout into the victim; that's Serta. And then, at Lumen, the holdout got paid anyway, because the company was healthy enough to come back for the stubs. It's the same problem three times, and the answer depends on the re-default clock, not on the co-op."

"Which means," says Ines, "that on 10 November the question wasn't 'sign, sell, or hold.' It was two questions. Will the co-op hold? And if it does, what is the company's runway after it closes? The second one is §14.3. The first one is a binomial tail, and Kaz is going to compute it."

Kaz is already writing.

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

> **Math, Gently.** *The binomial tail, or how often a jury folds.* Picture a jury of ten that will convict unless at least three jurors change their minds, and suppose each juror, independently, has a 10% chance of folding. How often do three or more fold? The **binomial distribution** counts the successes in a fixed number of independent yes-or-no trials that share one probability; here, ten trials at 0.10. No folds has probability $0.9^{10} \approx 0.349$; exactly one, $10 \times 0.1 \times 0.9^9 \approx 0.387$; exactly two, $45 \times 0.1^2 \times 0.9^8 \approx 0.194$. Those add to about 0.930, so three or more fold about 7.0% of the time. That last number is a **tail**, the probability of landing at or beyond a threshold rather than at any one value. Two features make tails powerful in coalition design. Raising the threshold by one juror cuts the tail by a large factor, because each extra fold has to happen on top of the others (four or more folds: about 1.3%). And the whole calculation rests on the word "independently," which is precisely the assumption a sponsor with a fee to offer is paid to break. The co-op version is the next paragraph: ten members, three defections needed, 7.0%.

With $m = 0.501$, $n = 10$, $c = 0.70$ and $\varphi = 0.10$ (all *illustrative*), $d^\ast = \lceil 2.87 \rceil = 3$ and $\Pi \approx 7.0\%$. Raise coverage to $c = 0.90$ with $n = 15$, and $d^\ast = 7$ and $\Pi \approx 0.03\%$. Coverage above the blocking line turns a coin flip into a tail event. At Optimum's reported co-op coverage of about 99% (below), nearly half the co-op would have to defect.

Now go back to the replay and answer the question on Ines's whiteboard. From the holdout's chair on 10 November 2023 the question is not whether a co-op can block a sponsor; at Lumen the group *was* the sponsor's counterparty. The holdout wants to know whether enough signers will walk to sink the deal, and that is the same binomial tail with the roles swapped: the deal fails only if signers holding more than $c - m$ of the class defect. In the term loans, where the deal eventually closed with 94.4% to 99.5% participation, the cushion over a bare majority was enormous, and the tail is negligible on any reasonable $\varphi$. The Level 3 unsecured were the interesting class, because they were built the Serta way: about 51% of the notes were slated to move into the new second lien against a 50.1% threshold. With ten equal signers, a single defector would have taken the group below the line, and at $\varphi = 0.10$ the chance that at least one of ten walks is $1 - 0.9^{10} \approx 65\%$. The deal closed anyway, which tells you $\varphi$ was nothing like 0.10. The two refinements below say why. The fees, the exchange ratios and the \$250mm cap per subscriber were the price of making defection unattractive, and the transfer restriction meant a signer who wanted out could not sell to a non-signer. A holder outside the group should have read the co-op as unbreakable and the menu as "sell or hold," not "wait for a crack." The one real option the holdout owned was the one Theo had called a fantasy: if a signer had walked, the company would have needed a replacement within days, and a non-signer with \$20mm of the right bonds would suddenly have been offered a seat. After that, the only live question was the re-default clock.

#### The Full Derivation

The coverage $c$ is now concrete, so here is how it enters the hazard.

The hazard of a non-pro-rata LME factors into a contract term, a coalition term, and an escape hatch:

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
> - **The bellwether.** CSC Holdings, Optimum's subsidiary, has about \$21.8bn of debt, and a June 2024 co-op claims about 99% of it. In an 8-K filed on 1 June 2026, Optimum disclosed that it had moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco", which sold \$300mm of preferred on 29 May 2026. Optimum's Q2 2026 10-Q discloses about \$4.12bn of principal maturing in April 2027 and \$2.225bn in July 2027 against cash of about \$1.30bn, and states substantial doubt about its ability to continue as a going concern (Optimum 10-Q, period ended 30 June 2026).
> - **The antitrust front.** Optimum (f/k/a Altice USA) and CSC Holdings sued the co-op lenders in the S.D.N.Y. under the Sherman Act, alleging price-fixing and a group boycott. The complaint alleges the co-op lenders hold 88% of a "Leveraged-Finance Market" it defines itself (Cleary Gottlieb, *Cooperation, Not a Cartel*, 18 December 2025). Defenses include rule-of-reason analysis, market definition, and *Sharon Steel v. Chase Manhattan* (2d Cir. 1982). Similar challenges (Optimum, Selecta) were "in their early days" in early 2026 (Wachtell, 3 February 2026).
> - **Europe.** Baker McKenzie's January 2026 leveraged finance report describes "a growing backlash against cooperation agreements" in 2025, as non-pro-rata deals at Victoria PLC, Ardagh, Selecta and Hunkemöller used intercreditor clauses and slim majority thresholds.
> - **What it means for the desk.** Co-op coverage $c$ is now a first-class feature in the non-pro-rata hazard and in stage 0 of the recovery model. High coverage moves risk from the uptier channel to the drop-down and deal-away channel, so it shifts $\lambda_{\text{away}}$ up even as it pushes $\Pi(c)$ down. And the legal status of the co-op itself is a regime variable with a pending date.

The Ad Hoc Group, represented by counsel, speaks in unison: *"We have signed a cooperation agreement. We decline to transact with the Company on a non-pro-rata basis. We note that there are forty-four other groups saying the same thing this year."* (Cooperation agreements signed in this book so far: one in Chapter 3, plus forty-five in 2024 alone. The counter has overflowed its integer type.)

**The courts calendar, or Optimum one docket entry at a time.** Every Monday at 8:15 a.m., before the European runs are digested and long before anything interesting happens, Theo updates the courts calendar. It is the least glamorous job on the desk and the one he was given in his first week, on the theory that a former restructuring banker would at least know what a docket is. The calendar is a table with one row per legal event that could move a recovery: the date, the forum, the judge, the contract words or doctrine at issue, the direction for the excluded holders, and a column headed `status` that is almost always `pending`. It feeds the courts table in §14.6 and, through it, the regime filter in §14.7. Most Mondays nothing changes. Theo opens the docket for each live case, reads the new entries, finds that they are scheduling orders and notices of appearance, and writes `no change` thirty times. Ines says this is the most important thirty minutes of his week. Theo suspects she says it to everyone who has the job.

Optimum is the row that never sits still, and laid end to end its entries read like a thriller written by a court clerk.

It starts in June 2024, when lenders to CSC Holdings, the main borrowing group of the cable company then called Altice USA and since renamed Optimum Communications, signed a cooperation agreement that claimed about 99% of CSC's roughly \$21.8bn of debt. On the threshold arithmetic of §14.5.1 that is the end of the uptier channel. With coverage of 99% and a bare-majority amendment threshold, nearly half the co-op would have to defect before a sponsor could build a majority, and the co-op itself, as the company later described it, barred its members from dealing with the company unless a two-thirds supermajority of them agreed. Kaz runs the numbers on a napkin and gets a breaking probability so small that the floating-point type complains. "The table agreed not to be bluffed," says Ines. "So watch what the sponsor does instead."

What the company did instead was the two things the model says a fully covered borrower will do: go around the table, and sue it.

On 25 November 2025 Optimum and CSC Holdings sued their co-op lenders in the Southern District of New York (*Optimum Communications, Inc. v. Apollo Capital Management, L.P.*, No. 1:25-cv-09785). The named defendants include Apollo, Ares and BlackRock, along with other large credit managers. The theory is antitrust: price-fixing and a group boycott under section 1 of the Sherman Act, on the argument that lenders who agree to deal with a borrower only as a bloc are a cartel in the market for leveraged finance. The complaint alleges the co-op lenders hold 88% of a "Leveraged-Finance Market" that the complaint defines for itself (Cleary Gottlieb, 18 December 2025). CreditSights reported "significant bond price declines" the next day, without publishing cents. Theo adds a row. Direction for the co-op lenders: negative if the suit survives. Direction for the bonds: the market had already told him.

"Group boycott," says Kaz, reading over his shoulder. "Is that when the lenders all refuse to go to the company's Christmas party?"

"Close enough to be dangerous," says Mags. "It's when competitors agree not to deal with someone. The question is whether lenders to one borrower are competitors at all, or one class with one interest. *Sharon Steel* says the competition happens when the debt is issued. The company says blocking access to new credit is something else." She shrugs. "Back in my day we'd have called it a steering committee and gone to lunch."

On 6 February 2026 the defendants moved to dismiss; an amended complaint followed in February. On 19 February Judge Jeannette Vargas declined to stay discovery while the motion was pending, which means that the lenders' internal emails about the co-op began to be a thing that could be read, whatever happened to the motion. Trade groups for lenders and asset managers, the LSTA among them, filed amicus briefs in support of dismissal in late March. Theo's calendar acquires a second Optimum row, and then a third, and Hana's pipeline acquires a field called `discovery_open` that nobody had needed before.

Then, at the end of May, the other move. In an 8-K filed on 1 June 2026, Optimum disclosed that it had moved Optimum East and its 50.01% stake in Lightpath, its fiber business, into an unrestricted subsidiary, "Unsub Topco," which sold \$300mm of preferred on 29 May. An unrestricted subsidiary sits outside the restricted group whose assets back CSC's debt, which is the whole point of putting assets there. It is $\lambda_{\text{away}}$ in a press release: a transaction that needs no vote from the class because it happens somewhere the class cannot reach.

"Unsub Topco," says Theo, to nobody in particular, as he types the row. "The subsidiary the lenders can't follow."

On 30 June 2026 the quarterly report said the rest out loud. Optimum's 10-Q for the second quarter disclosed principal of about \$4.12bn maturing in April 2027 and \$2.225bn in July 2027, against cash and equivalents of about \$1.30bn, and concluded that without committed financing there was substantial doubt about the company's ability to continue as a going concern (Optimum 10-Q, period ended 30 June 2026). On 4 August 2026 the court confined discovery to a court-defined "phase one" (ECF 132). As of mid-October 2026, Theo's row for the motion to dismiss still says `pending`.

He reads the row aloud at the Monday meeting, and for once nobody says "no change." The row is the whole chapter in one name. The re-default clock is running toward April 2027, with no cure in sight. The coalition variable is at its maximum, 99% coverage, and has pushed the action out of the uptier channel and into the drop-down channel, exactly as the Trend Watch box above predicts. The court variable is live in two directions at once: a pending ruling on whether the co-op is lawful, and a discovery process that may decide what the co-op lenders are willing to say to each other in writing from now on. And the recovery for any holder depends less on the word "first" in the loan's name than on which side of the table it sits on when the April 2027 wall arrives.

"Which side are we?" asks Kaz.

"Neither," says Ines. "We're the dealer. Which is its own seat." She means the next two boxes, and the one at the end of §14.9.

Optimum sued them for being a cartel. The table agreed not to be bluffed, and the borrower sued the table. The model lesson is that a commitment device strong enough to change $\Pi(c)$ by four orders of magnitude is strong enough to draw antitrust scrutiny. The probability that a court treats co-ops as unlawful belongs in the model as a scenario with a date, not as a parameter estimated from history, because the history has no such ruling in it yet.

> **View From Another Seat.** *The CLO manager: a co-op'd loan is a position you may not be able to sell in time.* To the CLO manager of §14.1, a co-op is less a strategy than a liquidity term. Joining one may be the only way to avoid being primed, but a loan whose transfers are restricted to signers can be sold only to someone willing to sign, and in a stressed name that list is short and made mostly of funds that are already inside. If the loan is downgraded to CCC in the meantime, the manager may reach a CCC-bucket or overcollateralization test date holding a position it cannot move before the trustee report, and the excess CCC is marked at the lowest price in the bucket whatever the manager thinks the loan is worth. The public worry from this side of the market is less about any one co-op than about the maturity wall that makes co-ops necessary. Loomis Sayles' Full Discretion team, a large loan investor, wrote in its fourth-quarter 2025 letter that "we do believe the risk of liability management exercises will remain elevated as not all these maturities are refinanceable," in the same letter in which it saw "low risk of downturn in 2026" (Loomis Sayles, Q4 2025 letter, January 2026). That pairing, a benign cycle and elevated LME risk, is the two-axis world of §14.4 in a practitioner's words: the macro regime and the coalition regime are different dials. For this seat the question is not $\Pi(c)$. It is whether $c$ comes with a transfer restriction that will bind before the next test date.

> **View From Another Seat.** *The opportunistic or special-situations fund: the co-op is the product.* For a fund whose edge is documents, counsel and a willingness to be restricted for months, a co-op is not a defensive necessity. It is the thing being sold. Buy enough of a class to matter, organize the rest of the class around you, and the sponsor must negotiate with your group or go around it, and going around it is expensive and, after Optimum, litigated. The public example is Veritas in 2024. Elliott and allied holders of more than half of Veritas's \$2.5bn of loans and \$1.8bn of bonds objected to Carlyle's proposal, which they said paid under 60 cents in cash, and "have already formed their own 'co-operation agreement'" (Hedgeweek, 25 June 2024, citing the *Financial Times*). From this seat a thirty-cent bond is an option on a negotiation, and the fund wants to own the blocking position in the vote rather than forecast it. For a systematic desk, a known blocker accumulating in a name is a state variable: the hazard of a non-pro-rata deal falls, the variance of recovery rises, and the RFQ flow from that kind of fund, like the one-way request in the cold open, is information about which hump the paper is heading for.

## 14.6 The Courts as a Regime Variable

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.288:* "LGD realizations can depend on many hard-to-quantify factors, from the quality of a defaulting firm’s assets and franchise to the vagaries of the resolution of legal proceedings and bankruptcy rulings."
>
> **Annotation.** Bohn and Stein list legal vagaries as one reason LGD modeling lagged PD modeling. Between 2024 and 2026 they became the main driver of the excluded holder's recovery, and they became *datable*. A ruling arrives on a known day, applies to identifiable contract language, and shifts the odds for every agreement with the same words. That is not a vagary. It is a regime switch with a timestamp.

> **Docket Diary.** *The rulings that moved $\theta_w$.*
> - **June 2020.** A New York state court declines to enjoin the Serta uptier, which closes on 22 June.
> - **20 June 2024.** *Robertshaw* (Bankr. S.D. Tex.), inside the Chapter 11 the company filed on 15 February 2024, about two months after its December 2023 control-flip financing and nine months after the original deal: the borrower breached the credit agreement, but the remedy for the excluded lender is money damages, not restored Required Lender status (Paul Weiss, 24 June 2024).
> - **31 December 2024, New Orleans.** The Fifth Circuit (*In re Serta Simmons Bedding*, No. 23-20181, consolidated with 23-20363, 23-20450 and 23-20451) holds that "open market purchase" means a purchase on "the secondary market for syndicated loans." A privately negotiated exchange with a subset of lenders falls outside it. The court also strikes the plan's indemnity for participating lenders. It observes that the 2020 Uptier "was the first major uptier... But it was far from the last."
> - **31 December 2024, the same day in Manhattan.** The Appellate Division, First Department (*Ocean Trails CLO VII v. MLN TopCo*, 2024 NY Slip Op 06660) permits the Mitel uptier. That agreement's exception said "purchases" with no "open market" qualifier, and subordination was only an indirect effect on the excluded lenders, so sacred rights were not triggered.
> - **10 July 2024 (oral ruling) and 17 January 2025 (written report and recommendation).** *Wesco/Incora* bankruptcy court (Judge Isgur): the 2022 transactions complied with one indenture but violated the 2026 notes indenture because the steps "had the effect" of stripping liens without two-thirds consent. The 2026 notes' liens are restored and the deal is unwound as to them.
> - **September 2025.** *ConvergeOne* (S.D. Tex. district court) reverses plan confirmation: an exclusive backstop for majority lenders violated equal treatment under §1123(a)(4). Appeal to the Fifth Circuit.
> - **8 December 2025.** *Wesco* district court (Chief Judge Crane) reverses the bankruptcy court and tests each step on its own wording. Appeal pending.
> - **7 July 2026.** *Serta* remand (Bankr. S.D. Tex.): participating lenders liable for \$261.13mm plus 9% New York prejudgment interest from 22 June 2020 (Mayer Brown, July 2026; §14.8).
> - **Del Monte Foods.** Chapter 11 on 1 July 2025 (Bankr. D.N.J. 25-16984); an adversary proceeding among lender groups on 23 January 2026; a district-court action by the Ad Hoc Group of Minority Secured Lenders on 6 March 2026; an appeal on 28 May 2026.
>
> The Ad Hoc Group notes, through counsel, that it has been on both sides of every one of these.

Two rulings on the same New Year's Eve, with opposite outcomes, both correct on their own words. This is the cleanest natural experiment the LMT era offers. The economics of the two deals were similar. The contracts differed by two words. A model that predicts priming outcomes from deal economics alone would have scored these two cases identically and been wrong about one of them. Figure 14.5 puts the rulings on one calendar with the exchanges they judged and the filings that followed.

![Figure 14.5: Two of four exchanged names filed inside Moody's two-year window and two after it, and the rulings that repriced these deals arrived only in 2024 to 2026. Source: filing dates and rulings as given in §14.3 (Trend Watch), §14.6 (Docket Diary) and §14.8, from the S.D. Tex. and D.N.J. dockets and law-firm memos; dates are month-level where the chapter gives only a month, and the Del Monte exchange date (August 2024) is as reported and not verified against the docket.](assets/figures/ch14_lme_timeline.png)

**Robertshaw, or the register is a battlefield.** The Docket Diary gives Robertshaw one line, and Mags thinks that is an insult to the line. She tells it standing up, the way she tells the stories she considers educational, and she starts with a question for Kaz. "Who is the Required Lender?"

"The lender who is required to lend?" says Kaz.

"The lender whose signature is required," says Mags. "Which is why everyone wants to be it."

The story starts in 2018, when the private-equity firm One Rock bought Robertshaw, a controls manufacturer, with \$510mm of first-lien loans, \$110mm of second-lien loans, about \$260mm of equity and an asset-based revolver. By 2023 the company needed money, and on 9 May 2023 it signed a New York-law Super-Priority Credit Agreement with an ad hoc group of lenders, Bain Capital Credit, Canyon and Eaton Vance, together with Invesco. The deal put in \$95mm of first-out new money and exchanged the old first and second liens into second-out and third-out loans. Under the new agreement, "Required Lender" meant a holder of more than 50% of the first-out plus second-out loans, and the agreement said how to tell: you read the agent's register.

"That's the token," says Theo. "Not a phrase about open markets. A number on a register."

"And a register can be bought," says Mags. In July 2023 Invesco quietly bought enough loans to cross 50% of the first-out plus second-out combined, through a majority of the first-out though not of the second-out, and became the Required Lender on its own. Nobody else in the group seems to have known. In the autumn the company missed interest, and a series of amendments followed in October and November: they extended the grace period, provided \$17mm of bridge money, set a deadline for a Chapter 11 filing and installed an independent director chosen by Invesco. Invesco directed the agent not to post them. The ad hoc group learned about them around 15 November.

Kaz looks genuinely shocked, which is rare. "The amendments existed, and the other lenders couldn't see them?"

"Welcome to the loan market," says Mags. "It's not a stock exchange. It's a spreadsheet at an agent bank and a data room you may or may not be invited into."

The counter came on 11 December 2023. The ad hoc group and One Rock lent \$228.3mm to RS Funding, a vehicle that the parent voted and Robertshaw economically owned. The cash repaid the \$30mm revolver and prepaid \$117.6mm of first-out loans, plus a \$30.7mm make-whole. Because Invesco's majority sat in the first-out, shrinking the first-out shrank Invesco's share of the combined class. Invesco received more than \$90mm of the prepayment and fell below 50%. The ad hoc group became the Required Lender and signed a fifth amendment for \$228mm of new debt. Invesco sued in New York in late December. On 15 February 2024, about two months after the control flip, Robertshaw filed for Chapter 11 in the Southern District of Texas before Judge Lopez.

"So the whole fight," says Theo, "was over who got to be the one signature, and it took place entirely on the register, and the company filed anyway within nine months of the deal that started it."

On 20 June 2024 Judge Lopez ruled. The ad hoc group were the Required Lenders, the fifth amendment was valid, the lenders had not breached and there was no tortious interference. Robertshaw itself, the court found, had breached by not sending 100% of the net proceeds to RS Funding as the agreement required. The remedy was a money claim, not restored Required Lender status (662 B.R. 300; Paul Weiss, 24 June 2024). Invesco claimed about \$40mm; the debtors said such a claim would recover about 3%. In June 2024 the business was sold by credit bid, about \$286mm made up of roughly \$217mm of super-priority claims plus interest and about \$65mm of DIP financing, to the ad hoc group and One Rock, with no rival bid. A liquidating plan was confirmed over Invesco's objection on 16 August 2024, with an \$11mm pool for unsecured creditors and a \$10mm deficiency pool.

Ines writes the hand history on the board. "Invesco won the register in July and lost it in December. It won a breach finding in June and was paid about three cents on it. The group that lost the register in July won it back with a prepayment and then owned the company by August. Same loans, same agent, same agreement."

"Required Lender is read from a register," says Mags, "and the register is a battlefield. Back in my day we fought over the plan. Now we fight over the spreadsheet that decides who gets to propose one."

**When the jump model works, and when it breaks.** Robertshaw is the right case for judging the jump model of §14.6.1, because on that model it barely registers. The ruling did not interpret a phrase that appears in hundreds of other agreements. It turned on conduct: who bought which loans and when, which amendments were posted, which vehicle the money went through, and whether the net proceeds went where the agreement said. The jump model for $\theta_w$ works when a ruling turns on a token you can parse, such as "open market purchase," a bare "purchases," or "the effect of" releasing collateral, because one ruling on a token reprices every document that carries it, on a known date. It breaks when the ruling turns on facts that no document parser can see, such as an unposted amendment or a quiet purchase on the register. Those cases do not generalize across documents, and the text gives no warning of them; the only early signal is the trading, and in a loan market the trading is the agent's register. Even where the token model works, it will mislead you if you skip the remedy. Robertshaw found a breach and gave the injured lender a money claim against a debtor that was about to be sold by credit bid, which made the claim worth whatever the unsecured pool was worth. Serta's remand found a breach too, but its damages ran against the participating lenders, who were solvent, and with interest at 9%. The same word, "breach," carried values of about three cents and about forty-five points. A seasoned practitioner therefore reads the remedy before the merits: rescission or damages, damages against whom, and whether the claim survives a sale or a plan. Only then is it worth asking which way the judge will rule.

### 14.6.1 Encoding a ruling as a jump

Think of each wording class as a horse with a betting line: $\theta_w$, the chance that a priming deal written under that wording survives a challenge. On most days the line does not move. On a ruling day it jumps, for every document that carries those words at once, and it jumps on the log-odds scale. The logit box in §14.3.2 explains why that scale: a probability has to stay between 0 and 1, but its log-odds can move freely, and a jump of $+1$ takes an even-money line to about 0.73 wherever the line happens to start. Here the "covariates" are ruling dates, and each one adds its jump from that day forward.

#### The Full Derivation

Let $\theta_w(t)$ be the probability that a priming transaction under wording class $w$ survives challenge, given the law as of $t$. Wording classes are the tokens from Chapter 13's document parser: `open_market_purchase`, `bare_purchase`, `directly_and_adversely`, `subordination_unanimous`, and so on. Model the log-odds as piecewise constant with jumps at ruling dates $t_r$:

$$
\operatorname{logit}\theta_w(t) = \alpha_w + \sum_{r} J_{r,w}\,\mathbf{1}\{t \ge t_r\},
$$

where $J_{r,w}$ is the jump that ruling $r$ induces for wording $w$. It is zero if the ruling doesn't touch that language, negative for Serta on `open_market_purchase`, positive for Mitel on `bare_purchase`, and jurisdiction-dependent where courts split, as with the step-by-step Wesco district-court reading against the integrated reading in New York's *STG Logistics* (whose exact date we have not verified). Because rulings are rare, $J_{r,w}$ is not estimated from data. It is elicited, as a prior, from people who read the opinion, and then updated on the market's own reaction: the price gap between likely-inside and likely-outside paper in the days after the ruling.

#### Measuring the reaction, and the Lions Gate caution

"The days after the ruling" hides a trap, and the Lions Gate separation is the case that shows it. Holders of Lions Gate's 5.5% notes due 2029, the paper a May 2024 exchange had left with less of the company behind it, objected when the studio business sought approval of its separation arrangement in British Columbia. The notes were at 77.0 on 17 April 2025, before the arrangement was announced, and at 72.8 on 22 April, after it. On 5 May, the day the Supreme Court of British Columbia approved the arrangement over the objection (*Lionsgate Studios Corp. (Re)*, 2025 BCSC 1293), they were bid at 78.05, above where they had started (BVAL prices recited in the judgment, paragraphs 24 and 28). A desk that measured the jump on the opinion date would conclude that a ruling against the objecting holders was good news for them. It was not good news. It was old news. The announcement carried the damage, and by the hearing the market had priced both the arrangement and the likelihood that the court would approve it. So measure the reaction from $t-1$ to $t+5$ trading days around the *announcement* that made the ruling likely, not only around the opinion, and record which window you used, because the two can have opposite signs.

#### Calibrating the jumps


The Fifth Circuit gave the elicitation a head start by stating its own prior: such exceptions "will often not justify an uptier." Translate "often" into a log-odds jump of your choosing and write it down with a date. The discipline matters more than the number. A model that updates on rulings by a documented rule can be audited; a model that "absorbs" them through a re-fit on twenty observations cannot.

The jumps propagate in three places. They enter the Priming Risk Score of Chapter 13 directly, since PRS inputs shift discretely at ruling dates. They enter the non-pro-rata hazard $\lambda_{\text{NPR}}$ of §14.5 through $\theta_w$. And they enter recovery through $\mu_{\text{out}}$. After the Serta remand, an excluded position in a breach case owns a damages claim with a computable value, so the excluded hump moves right. The participants' expected cost of exclusion rises too, which feeds back into a lower $\theta$ for the next deal. Mags summarizes the remand as a credit analyst would. "The best-performing tranche in the Serta capital structure was New York prejudgment interest."

## 14.7 Regime Shifts in the Joint Law of $(\tau, R)$: A Markov-Switching Engine

We now have two regime axes. The macro cycle moves the mean recovery, as in Schmid's table. The LMT regime moves the default mix $\lambda_D/\lambda$, the coalition weight $\pi$, and the excluded mean $\mu_{\text{out}}$. The second axis changed state somewhere around 2020 to 2022. A desk needs to know which state it is in *now*, and it would like a rule that tells it, rather than a debate.

### 14.7.1 The Hamilton filter on the default mix

Some version of the argument that motivates this section happens on the desk most Mondays. Mags says the world changed at Serta and has not changed back. Kaz points at the Trend Watch in §14.1: the LMT count fell from 38 in 2024 to 24 in 2025, so surely something is turning. Mags points at the same box, at the line about the soft share of defaults not budging, and says that a count falling while the share stays put is what a regime looks like when it settles in, not when it ends. Theo spent years in rooms where the answer to "has the cycle turned?" was a slide with an arrow on it, and he notices that the two of them are reading the same evidence and reaching for the same word, *regime*, which neither of them can see. Nobody has ever observed a regime. People observe defaults, and some of those defaults are exchanges.

Ines ends it the way she ends most arguments. "I can't size off a word. Give me a number, tell me how sure you are, and tell me what would change your mind."

That request, a belief about something hidden, updated by evidence that arrives in lumps, is exactly what a hidden Markov filter does. It is less exotic than its name.

> **Math, Gently.** *A hidden Markov filter, or guessing the weather from umbrellas.* You work in a basement with no windows, and you want to know whether it is raining outside. You cannot see the sky, but you can see the door. On a rainy day about 65% of the people who walk in carry an umbrella; on a dry day about 30% still do, out of habit or a pessimistic forecast. This morning you start with no view, 50/50, and ten people come in, seven of them carrying umbrellas. How likely is seven-of-ten under each kind of day? The binomial formula, $\binom{10}{7}\rho^7(1-\rho)^3$, gives about 0.252 if it is raining ($\rho = 0.65$) and about 0.009 if it is dry ($\rho = 0.30$). Bayes' rule multiplies your belief by that evidence and rescales so the two answers add to one: $0.252/(0.252 + 0.009) \approx 0.966$. In the odds form from §1.3.3, the evidence is a likelihood ratio of about 28, and even odds times 28 is 28 to 1. That is the **update** step. The **prediction** step is what makes the model *Markov*: weather is sticky, so before the door opens tomorrow you blur tonight's belief through the stickiness. If a rainy day is followed by rain 90% of the time and a dry day by dry 95% of the time, tomorrow's starting belief in rain is $0.966 \times 0.90 + 0.034 \times 0.05 \approx 0.871$, a little less sure than tonight, because the weather might change overnight. It is *hidden* because you never see the sky; the only memory the weather has is today's state, which is all "Markov" means. Now translate. Rain is the LME regime, the door is the stream of defaults, and an umbrella is a distressed exchange. One more number explains why the filter counts umbrellas instead of quoting a percentage: seven umbrellas out of ten doors gives odds of 28 to 1, but 105 out of 150, the same 70%, gives odds of about $e^{50}$, because a hundred and fifty people walking in is far more evidence than ten. §12.4 met the same filter reading spreads with bell-curve evidence; here the evidence is counts. The full version is the pair of equations that follows.

Let $s_t \in \{0, 1\}$ be a hidden regime ("pre-LME" and "LME"), following a Markov chain with row-stochastic transition matrix $P$, where $P_{ij} = \mathbb{P}(s_{t+1} = j \mid s_t = i)$. Each year (or month) we observe $n_t$ defaults, of which $k_t$ are distressed exchanges, and we model

$$
k_t \mid s_t, n_t \sim \mathrm{Binomial}(n_t, \rho_{s_t}),
\qquad 0 < \rho_0 < \rho_1 < 1,
$$

where $\rho_s$ is the DE share in regime $s$. Using counts rather than shares matters, for the reason the umbrellas gave: a 70% share from 10 defaults and a 70% share from 150 are very different amounts of evidence, and the binomial likelihood weights them correctly. Let $\eta_t$ be the vector of emission likelihoods, $\eta_{t,j} = f(k_t \mid s_t = j)$, and $\hat\xi_{t\mid t-1}$ the predicted regime probabilities. (The subscript $t$ keeps this evidence vector apart from the Weibull scale $\eta$ of §14.3.2; the two never meet in one equation.) The filter alternates an update and a prediction:

$$
\hat\xi_{t\mid t} = \frac{\hat\xi_{t\mid t-1} \odot \eta_t}{\mathbf{1}^\top(\hat\xi_{t\mid t-1} \odot \eta_t)},
\qquad
\hat\xi_{t+1\mid t} = P^\top \hat\xi_{t\mid t},
$$

where $\odot$ is the element-wise product. The log-likelihood is $\sum_t \log \mathbf{1}^\top(\hat\xi_{t\mid t-1} \odot \eta_t)$, which we maximize over $(\rho_0, \rho_1, P_{00}, P_{11})$. Start the recursion at the stationary distribution, $\mathbb{P}(s_0 = 0) = (1 - P_{11})/(2 - P_{00} - P_{11})$.

The equations are the easy part. Four implementation details decide whether the thing works, and Kaz dictates them to ROBO on a Thursday afternoon in one long paragraph, because Kaz talks in paragraphs and ROBO does not mind. The first is log space. In a big default year the binomial likelihoods get small enough to underflow, so the filter multiplies by $e^{\log \eta_t - \max_j \log\eta_{t,j}}$ instead of by $\eta_t$, and adds the max back to the log-likelihood; nothing about the answer changes except that it stops being zero. The second is label switching. Left alone, an optimizer is as happy calling the high-exchange state "0" as "1," and on alternate runs it will, so Kaz parameterizes $\rho_0 = \operatorname{logit}^{-1}(a)$ and $\rho_1 = \operatorname{logit}^{-1}(a + e^{b})$, and the "LME regime" is the high-share state by construction, because $e^{b}$ is always positive. (The logit is the betting-line translator from §14.3.2.) The third is the one Kaz says twice. Roughly 45 annual observations cannot pin down four parameters plus a regime path with any confidence, so the filter runs on monthly counts, pools across rating agencies only after their definitions have been harmonized through a timestamped label dictionary (the dull table from §14.1 and §14.2 that records which source called what a default, and when), and puts priors on $P$. The fourth is that $P$ is not a constant. The ruling calendar of §14.6 is information about how likely the regime is to end, so $P$ is allowed to depend on time through $\operatorname{logit} P_{11}(t) = c_1 + \sum_r \kappa_r \mathbf{1}\{t \ge t_r\}$, and a ruling against priming raises the probability of leaving the LME regime. That is why the filter accepts a $(T, 2, 2)$ array of transition matrices, one per period, rather than a single $2 \times 2$ matrix. ROBO reads the paragraph back as four numbered requirements, which is what Kaz meant and not what Kaz said.

The same machinery extends to recovery: a second switch on mean LGD, with Schmid's $\mu_0 \approx 0.43$ and $\mu_1 \approx 0.28$ as the macro regimes, and the LMT regime treated as orthogonal to it. The macro cycle moves the mean; the LMT regime moves $\pi$ and $\mu_{\text{out}}$, not the macro mean.

**Quant-shop life (fictional composite): "Why is this number different from yesterday?"** The spec Theo wrote on a Friday said, in full, "Add the LME regime to the morning dashboard." What ROBO built from the vague version was a column called `regime` holding zeros and ones: the more likely state in each month, which is the most literal reading of "the regime." It flipped from 0 to 1 in 2021, flipped back for one month in the summer of 2023 when a thin month brought four bankruptcies and not a single exchange, and flipped again the month after. Read as a label, it said the world had changed three times in two years. Read as a probability, which was sitting one column over and which nobody had asked for, it said the filter had dropped from 0.86 to 0.25 and recovered *(illustrative)*, which is a thin month doing what thin months do. Theo rewrote the spec: `p_lme_filtered`, the filtered probability of the LME state to two decimals, with the as-of date of the default counts it used and the vintage of the parameters it ran with. ROBO built exactly that. It went on the dashboard on a Monday at 0.94.

The desk's risk committee meets monthly, on a Wednesday, in a room with a projector that takes four minutes to find the laptop. The chair is a former rates trader who reads every number on a slide as if it were a limit. On Wednesday morning the dashboard says 0.88, and the chair asks the question every risk committee asks about every number: "Nothing defaulted yesterday. Why is this different from yesterday?"

The honest answer has the shape of a P&L explain, and Theo has learned, faster than he expected to, to bring the explain before the question. Three things can move a filtered probability overnight, and only one of them is news. The first is new data. The month's default count closed with nine defaults, four of them exchanges, a slightly old-world month, and on its own that takes the number from 0.94 to 0.91. The second is a restatement. The vendor reclassified one March exchange as a missed payment, because the company skipped a coupon a week after the deal closed, which is the forty-one-issuers problem of §14.1 now running through a filter. Every filtered number depends on all the months before it, so changing March changes every month since March, and today's by two points. The third is a refit. The nightly job re-estimated $(\rho_0, \rho_1, P_{00}, P_{11})$ by maximum likelihood on the longer sample, and with a sample this short a single month nudged $\hat P_{11}$ down, which made the LME regime look slightly less sticky and cost one more point. 0.94, 0.91, 0.89, 0.88 *(all illustrative)*.

"So which of those do I believe?" asks the chair.

Ines answers before Theo can. "The first one is a hand. Somebody played a card and we saw it. The second is the dealer fixing a misdeal. The third is us deciding to read the cards differently. The first one moves my size. The other two move my paperwork."

"Back in my day," says Mags, "the regime was whatever the man with the biggest position said it was at the morning meeting, and you found out he'd changed his mind when he sold. This is better." She considers the slide. "It's wrong in writing."

The fixes are the boring kind that matter. Refits move to the first business day of the month, and each one goes into the model change log with the old and new parameters side by side, so the number cannot drift merely because a job ran. The dashboard's published history is archived as published, each day's filtered probability frozen beside the data and parameter vintages that produced it. That is the "what we knew when" table of §14.1 applied to the model's own output, and the reason for it is the same: a back-test that rebuilds the history with today's parameters would credit the desk with a confidence it never had. And there is now a second, clearly labelled column, the *smoothed* probability, which uses the whole sample, including the months after the date in question, to say what the regime most likely was back then. The smoothed number for March 2023 changes every time a new month arrives. The published filtered number for March 2023 never changes. The committee wants both, for different reasons: the filtered one to audit what the desk did, the smoothed one to argue about history. Kaz asks whether it would be simpler to show only the smoothed one, since it is more accurate.

"It's more accurate about the past," says Ines, "because it got to read the future. Show me what you knew."

The ticket is titled "regime explain." It is the first of Theo's tickets to close inside a week.

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

The schema above describes a table we do not have. The real one would hold a few dozen liability-management deals a year, most with a year or two of follow-up, spread across sponsors, document vintages and rating agencies that disagree about what a default is. Theo wants to know whether his Aalen–Johansen code returns the right cumulative incidence, and on that table nobody can say what the right answer is. Kaz, who has never met a problem that could not be improved by writing a simulator, proposes the obvious fix: build a world where the answer is known and see whether the estimators find it. Theo built his 13-week model the same way, assuming the receipts and watching whether the revolver survived, so it is the first idea all week that feels like home.

Listing 14.1 is that world. `LMEParams` holds every number the chapter has argued for, with regimes indexed 0 for pre-LME and 1 for LME. Hard-default hazards are 0.030 and 0.022 a year, exchange hazards 0.008 and 0.038, there is a 5% cure hazard, and a 2-by-2 matrix moves the regime from year to year. After an exchange, 25% of issuers are susceptible to a hard default on a Weibull clock with shape 1.2 and a scale of about 1.71 years, computed from fact 3 of §14.3.2 so that 70% of eventual defaulters are gone within two years. Four Betas set recoveries as fractions of par: 0.74 inside the group, 0.25 excluded, 0.53 on a hard default with no prior LME, and 0.23 after one. The constructor asserts shapes, row sums and positive Beta parameters, so a bad world fails on creation rather than three tests later.

`simulate_cohort` then walks the issuers forward year by year along a single regime path. In each year every survivor draws an exponential wait at that regime's total hazard. A wait shorter than the year is an event, and its cause is picked in proportion to the three hazards. Redrawing at each year boundary is legitimate because the exponential forgets. Whoever is left at `T_max` is administratively censored, and `censor_rate` can add independent early censoring. Recoveries follow: a Beta draw for each hard default, a membership coin with probability `pi` for each exchange, then a susceptibility coin and a Weibull draw for the post-exchange clock, cut off at the follow-up the cohort actually has. The output is the schema above, first-event rows plus one post-exchange row per exchanger, stably sorted by time.

Use it wherever you need a known answer: tests, power studies, or asking how many exchanges you must watch before `p_redefault` is pinned down. Do not read it as a forecast. Hazards are constant inside a regime-year, and the re-default clock ignores the regime entirely. The edge case that bites is that the regime path is one draw per cohort, so issuers are not independent. Closed-form checks hold only when you pass `P` as the identity or fix `regime_path`, and with a live path the sampling noise is wider than any binomial standard error suggests.

*The full listing is [Listing 14.1 in Appendix F](#code-14-1).*

Kaz has read the Kaplan–Meier warning in §14.2.2 and is unrepentant. "Hard defaults and cures are just censoring, and I have a one-line function for censoring." It is a fine instinct and a wrong answer, and the trap is that the output looks right: a number between zero and one, rising with the horizon. Mags supplies the distinction in her own terms. "Censoring is when you lose sight of the loan. A hard default is when the loan can no longer do anything else." An estimator that mixes the two computes the probability of an exchange in a world with no bankruptcies, and no desk trades there. The correct bookkeeping is a risk table kept across all causes at once and rebuilt every time the vendor file refreshes, which is exactly the chore that belongs in code someone has tested, not in a spreadsheet someone has inherited.

Listing 14.2 does that bookkeeping. `_first_events` keeps only the rows with no `time_since_de`, so each issuer enters once and leaves at its first exit, whatever that is. `_risk_table` sorts the times with a stable sort, takes the distinct times at which something happened, counts the issuers still at risk at each one (an issuer censored at exactly that instant still counts), and counts events of each cause with sorted searches, so tied times are handled together instead of in whatever order the file happens to hold them.

`nelson_aalen_cause` cumulates events over the at-risk count for one cause. `aalen_johansen` does the main job. It updates all-cause survival as a running product of one minus total events over at-risk, then adds up, for each cause, the survival just before each time multiplied by that cause's events over at-risk. The result is a frame with `S`, `F_H`, `F_D` and `F_C`, which sum to one at every row. `km_naive_cif` is the trap, built on the same risk table as one minus the product of one minus the single-cause rate. Its docstring calls it wrong, and it stays in the module so that the test can prove the inequality. `step_at` reads any of these step curves at an arbitrary horizon and returns zero before the first event.

Use these for the descriptive question, what share of a cohort has had a first event of type k by horizon t, and feed them first-event data only. They say nothing about covariates, where §14.2.2 sends you to Fine–Gray, and nothing about what happens after an exchange, which is the next listing's job. The edge case is the `causes` argument. It must list every exit code, cures included. Pass `(1, 2)` because a cure is not a default and the cures stay in the table as exits that never count, which is the Kaplan–Meier trap again with cures as the censoring cause. Worse, `S + F_H + F_D` still equals one, because the identity is algebraic, so the sum-to-one check cannot see it. In our test cohort the ten-year `F_D` inflates from about 0.23 to about 0.28.

*The full listing is [Listing 14.2 in Appendix F](#code-14-2).*

Theo's envelope table in §14.3.3 gave three-year expected losses of 7.0%, 11.2% and 9.0% for the majority side, the excluded side and a holder who does not yet know which one he is. Kaz stares at it for a while. "You gave a name that exchanged in month thirty-five the same chance of re-defaulting inside the window as one that exchanged on day one." Theo concedes, because it is true, and because the correction is an integral over the exchange date with a re-default clock inside it, whose parameters must themselves be fitted to censored data. That is a fit, an integral and two small formulas (the recovery mixture of §14.4 and the co-op break probability of §14.5), each easy once and each wrong the second time someone changes an input. A desk puts them in one place and then tests the integral against brute force.

Listing 14.3 starts with the clock. `_cure_nll` is the negative log-likelihood of the mixture-cure Weibull, given times since exchange `u` and a flag `delta` that is 1 for an observed hard default. It works on unconstrained numbers (the logit of `p`, the log shape, the log scale), clips the logs so that an exponential cannot overflow, and uses `logaddexp` so that the censored term, the log of $(1-p) + p\,S_0(u)$, stays stable. `fit_cure_weibull` minimizes it with Nelder–Mead from four starts, the first at `p` of 0.3 and shape of 1, and keeps the best. It returns `p`, shape, scale and the log-likelihood.

`expected_loss` is the integral of §14.3.3 for one regime, done by `scipy` quadrature over the exchange date. Survival uses the full hazard, cure included, so on the engine's defaults the three-year numbers (about 5.9%, 10.2% and 7.9% for inside, excluded and blended) sit below the envelope table. Late exchanges have little time to re-default, and the 5% cure hazard thins the survivors, which the envelope left out. `side` picks whose recovery is used, and a horizon beyond `T_max` raises. `expected_loss_mc` computes the same quantity from a simulated table: hard-default losses by T, plus for each exchange the haircut and, when a post-exchange default row falls inside T, the second loss on what was left. Because it uses realized recoveries, it tests the integral instead of repeating it. `coalition_mixture_moments` applies the law of total variance and returns the mean, the variance and the between-group piece. `coop_break_prob` is the binomial tail of §14.5.1, and returns 1.0 below the blocking line, where the co-op is decorative.

Use the fit on any post-exchange cohort with right-censoring, and the loss functions for the inside/outside spread. Do not carry the exact loss across a regime change, since it assumes one regime's constant hazards. The edge case that bites is follow-up. The optimizer always returns an answer. In one trial run with 300 exchanges watched for fourteen months, it reported `p` near 0.13 and a shape above 2, against truths of 0.25 and 1.2. Fix the shape or give it a prior (§14.3.2) before trusting a short sample.

*The full listing is [Listing 14.3 in Appendix F](#code-14-3).*

Nobody rings a bell when a regime changes. Mags will tell you the LME era began with Serta in June 2020, a modeler with a different sample will say 2022, and a sponsor's counsel will say it never began and the documents do not use the word. What the desk has is a count each period of defaults and of how many were exchanges, and what it needs is a number, refreshed as each new count lands, for the probability that it is standing in the high-exchange regime today. That is the Hamilton filter of §14.7.1. It is a short recursion and the kind that fails silently, because an unlikely count under one regime can push a likelihood so low that everything multiplied by it rounds to zero. The desk writes it once, in log space, tests it, and never again lets anyone type it from memory.

Listing 14.4 is that filter and the machinery around it. `hamilton_filter` takes a `(T, 2)` array of log emission likelihoods and a transition matrix, either 2-by-2 or `(T, 2, 2)` for the time-varying case. Unless you supply a start, it begins at the stationary distribution implied by the first matrix, falling back to even odds when both regimes are nearly absorbing. At each date it subtracts the row maximum before exponentiating, multiplies by the predicted regime probabilities, normalizes with a floor of 1e-300, adds the log normalizer and the maximum back into the running log-likelihood, and predicts the next date through the transpose of `P`. It returns the filtered probabilities and the log-likelihood. "Filtered" is the point. Each row uses only data through that date, so it is what the desk could have known then, not a smoothed history that peeked.

`binom_logf` turns counts into the emission array, with shares clipped away from 0 and 1, so a 70% share from 150 defaults outweighs one from 10. A period with zero defaults gives zeros in both columns, which is no information, only a step through `P`. `_ms2_unpack` maps four unconstrained numbers to the model: the low share is the logistic of `a`, the high share is the logistic of `a + exp(b)` so the second regime is always the high-exchange one and the labels cannot swap, and two persistence probabilities are clipped away from 0 and 1. `fit_ms2` minimizes the negative log-likelihood by Nelder–Mead from six random starts. `simulate_de_share_series` makes test data from a Markov path, Poisson default counts and binomial exchange counts.

Use it on monthly or pooled counts with harmonized definitions, since 45 annual points cannot carry four parameters and a path. Note that `fit_ms2` estimates a constant `P`. The filter accepts the ruling calendar as a `(T, 2, 2)` array, but nothing in the module fits the ruling coefficients of §14.7.1, so that link you build yourself. The edge case that bites is timing. Row `t` of a time-varying `P` governs the step from date `t` to `t+1`, so a ruling dated to `t_r` first moves the prediction for `t_r + 1`. If it should bear on the ruling period's own count, put the change at `t_r − 1`.

*The full listing is [Listing 14.4 in Appendix F](#code-14-4).*

Every model review ends in the same two questions. How do you know it is right, and why did the answer move overnight? Theo's 13-week model had a check cell at the bottom of the cash waterfall that turned red when the balance did not foot, and he credits it with saving him from more embarrassing calls than any senior colleague. The engine needs the same instrument, with more cells and a stricter idea of what counts as footing. The cheapest honest test is a world whose answer you wrote down in advance.

Listing 14.5 is that instrument. `check` is the whole framework: it prints PASS or FAIL and asserts, so a failing run stops at the offending line instead of scrolling past. The checks climb through the engine in order. First, the Weibull scale must put 70% of susceptible defaults inside two years, to 1e-12. Then a single-regime world (`P` the identity, a fixed regime path, 50,000 issuers) lets closed forms apply. The Aalen–Johansen pieces must sum to one at every jump within 1e-10, and `F_H` and `F_D` at one, three and five years must land within four standard errors of $\tfrac{\lambda_k}{\lambda}(1-e^{-\lambda t})$. One minus Kaplan–Meier must exceed the right answer at five years, and the exchange share of first defaults must match $\lambda_D/(\lambda_H+\lambda_D)$.

Next the mixture moments are compared with 400,000 draws, and the Serta between-group standard deviation of 0.245 is recomputed from Beta(74, 26) and Beta(25, 75). The cure fit runs on 20,000 simulated issuers with censoring spread between half a year and ten, and must recover `p` to 0.03, shape to 0.15 and scale to 15%. The same clock truncated at fourteen months feeds ROBO's exponential, whose ten-year default probability is printed beside the truth (65% against 25% in our run) and asserted to exceed 50%. Exact and Monte Carlo expected loss must agree within half a point for each side, and the excluded holder must lose more than the included one. The Markov-switching fit must return valid probabilities that sum to one and call the regime correctly in more than 85% of 80 simulated years. Last come arithmetic tripwires: the P-versus-Q ratio, three co-op cases, and two Serta dollar identities, such as \$484.88mm less \$895mm of face at 25 cents equaling \$261.13mm.

Run it after every edit and before any refactor merges. It proves that the code implements the stated math. It says nothing about whether the math describes the market, since no real data touch it. The edge case that bites is that every closed-form comparison runs with regime switching turned off. The cohort simulator's regime transitions are never checked against a closed form, and the Markov-switching test uses a separate generator, so a green run is silent about how the two interact.

*The full listing is [Listing 14.5 in Appendix F](#code-14-5).*

The tests double as documentation. If a later contributor "simplifies" `aalen_johansen` into one minus Kaplan–Meier, the trap test fails. If someone replaces the cure model with an exponential, the fourteen-month test prints ROBO's answer next to the truth.

### Deep-Dive Resource Graph (§14.7)

- **Academic Papers.** Hamilton (1989), *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*, Econometrica. Fine & Gray (1999), *A Proportional Hazards Model for the Subdistribution of a Competing Risk*, JASA 94(446). Aalen & Johansen (1978), *An Empirical Transition Matrix for Non-homogeneous Markov Chains Based on Censored Observations*, Scandinavian Journal of Statistics.
- **Data & Code.** Moody's and S&P annual default studies (vendor) for DE counts by year; Federal Reserve FSR Figure 2.9 for a public DE-inclusive series.

## 14.8 Case Studies: Three Clocks

### 14.8.1 Case Study: Serta Simmons Bedding, 2020–2026 (the whole regime in one name)

- **2016.** A \$1.95bn first-lien term loan and a \$450mm second lien (Duane Morris, February 2025).
- **22 June 2020.** The uptier closes. It brings \$200mm of new-money first-out super-priority debt, and participating lenders exchange about \$1.2bn of first- and second-lien loans into about \$875mm of second-out super-priority debt, first liens at 74 and second liens at 39 (Proskauer, 2 January 2025; Jones Day, March 2025). On the remand court's findings, the participants held about 52.6% of the first-lien class, and the excluded loans were worth about \$0.25 at the closing.
- **23 January 2023.** Chapter 11 in the Southern District of Texas, about 31 months after the uptier. On 28 March 2023 the bankruptcy court grants partial summary judgment that the exchange was an "open market purchase." The plan is confirmed on 14 June 2023.
- **31 December 2024.** The Fifth Circuit reverses and strikes the plan's indemnity (§14.6).
- **November 2025 to July 2026.** Serta itself wins summary judgment on discharge grounds, which leaves the participating lenders as the defendants. Trial is held in March 2026. On 7 July 2026 the court awards \$261.13mm (but-for value of about \$484.88mm against actual value of \$223.75mm, which is \$895mm face at \$0.25), plus 9% New York prejudgment interest from 22 June 2020, allocated severally by each defendant's holdings (Mayer Brown, July 2026).

Run the interest. From 22 June 2020 to 7 July 2026 is about 6.04 years, so 9% simple interest adds roughly 54% to the award, about \$142mm, for a total near \$403mm *(approx.; before allocation, collection risk, or appeal)*. On \$895mm of face, that is about 45 points of par, *on top of* whatever the excluded loans recovered in the plan. Our "illustrative" $\mu_{\text{out}} = 0.25$ was the value at closing. Six years later, the excluded hump had a litigation tail worth more than the loan. Mags's line about New York interest was not entirely a joke.

The remand also produced the most useful hand history in the book. Defendants' mitigation expert testified that up to \$186mm face of the first-lien loans traded between June 2020 and the end of 2021, and constructed hypothetical sales of \$62mm to \$94mm. The court recited Bloomberg chats with a dealer's loan market maker. "That's my markout," says Ines. "Entered into evidence."

**How a systematic desk flags it.** Four signals were observable before 22 June 2020: the document token ("open market purchase" with no definition, a Priming Risk Score input in Chapter 13), a fragmented CLO-heavy holder base with no co-op ($c \approx 0$ in §14.5), Rule 2019 and press evidence that a group was forming, and RFQ flow in the loan that was one-sided by holder type. After the closing, the trade was the inside/outside spread and, after 31 December 2024, the excluded claim as a contingent asset with a dated appellate path.

### 14.8.2 Case Study: Mitel Networks, 2022–2025 (win the case, lose the credit)

In October 2022 participating lenders provided about \$156mm of new-money first-out debt, exchanged first-lien loans into second-out at a 5% discount, and exchanged second-lien loans into third-out at an 18% discount (Paul Weiss, 10 January 2025). The excluded lenders were left behind about \$857mm of priming debt. On 31 December 2024 the First Department held the deal permitted. On 10 March 2025 Mitel filed a prepackaged Chapter 11 in the Southern District of Texas, about 29 months after the uptier, and the plan was confirmed in April 2025.

The lesson is about which parameter a ruling moves. Mitel's legal victory set $\theta_w$ for the bare-"purchase" wording close to one. It did nothing to the re-default clock, because the clock runs on runway, and \$156mm of new money bought about two and a half years of it. In the mixture-cure model, Mitel was one of the susceptible 25%, and it failed inside the high-hazard window that the $k > 1$ calibration predicts. Legality and survival are close to independent.

### 14.8.3 Case Study: Del Monte Foods, 2024–2026 (the fast clock)

Here we keep to the dockets. A 2024 financing, reported as a non-pro-rata deal in August 2024, was followed by Chapter 11 on 1 July 2025 (Bankr. D.N.J. 25-16984), about eleven months later and well inside Moody's two-year window. Litigation between lender groups followed: an adversary proceeding naming members of the Ad Hoc Term Lender Group and of the Ad Hoc Group of Minority Secured Lenders (23 January 2026), a district-court action by the minority group (6 March 2026), and a bankruptcy appeal (28 May 2026). The deal terms, recoveries and holdings are in the first-day declaration and the complaints, and a desk should read them before putting numbers on this one. The shape is already instructive: a short $\eta$, then a second fight about $\pi$ inside the bankruptcy itself.

## 14.9 Trading the Regime

Five signals come out of this chapter. Each is a feature with a timestamp, not an opinion.

1. **Post-LME re-default versus market-implied.** Six to 24 months after an exchange, a name sits in the peak of the hazard hump, but agency ratings often stay flat after LMEs (Roe & Rotaru, 2026). Compare the cure-model hazard to the hazard implied by the loan price, computed with the *post*-LME recovery rather than 40%. The gap is a systematic underweight in defensive high-yield books (Chapter 11).
2. **Coalition membership.** Stage 0 of §14.4 scored from Rule 2019 statements, co-op announcements, CLO trustee holdings, and the adviser-hire headlines that Chapter 25's NLP pipeline extracts. Long likely-inside, short likely-outside in the same class, where the document score is high and the holder base fragmented.
3. **Docs vintage.** Pre- versus post-blocker documents. Buccola and Nini (2024) find that most new loans blocked uptiers by mid-2022 while the legacy stock stayed loose, and that stock decays only as it matures or is amended. It is a factor, not a one-off.
4. **The dual default-rate spread.** Headline minus ex-DE default rate as a regime input to high-yield beta and to the Hamilton filter of §14.7.
5. **Ruling dates as event windows.** Pending appellate decisions (Wesco and ConvergeOne in the Fifth Circuit, the first co-op antitrust ruling) are known catalysts with direction-dependent jumps in $\theta_w$ and $\mu_{\text{out}}$. Pre-compute the repricing under each outcome.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** A strong claim, and the right kind of signal to own. The question this chapter teaches you to ask is: *which* default? A bond-index default definition, a structural model built on asset value and volatility, and a sample mostly from before the LMT era were all built to catch hard defaults. A soft default is a negotiation over runway and coalition, and asset value is only one input to it. A 2026 default-avoidance signal should be scored separately on $F_H$ and $F_D$, and its hit rate on distressed exchanges reported on its own line.

"IDO or it didn't happen," says Ines, closing the hand. "Knowing that distressed exchanges are 65% of defaults is beta. Everyone has the Moody's report. Knowing which 52.6% of the class you're in is alpha."

## 14.10 Desk Debrief

- **"The default rate" is two numbers.** Headline and ex-DE rates differed by a factor of almost three in June 2025 (5.8% vs. 2.1%). Carry $\lambda_H$ and $\lambda_D$ separately, and name the definition in the column.
- **Use cumulative incidence, not 1 − Kaplan–Meier.** Censoring the competing cause overstates the probability of the cause you care about, and the bias grows with horizon.
- **A distressed exchange is parole, not immunity.** About a quarter of soft events end in hard default, more than 70% of those within two years. The hazard among the susceptible *rises* at first, because the deal bought runway. Calibrate $k \gtrsim 1$, not $k < 1$.
- **Recovery is two humps.** Membership alone can generate a 24-point standard deviation. Stage 0 of the LGD model is $\mathbb{P}(\text{in majority})$, and it belongs to the holder, not the loan.
- **Co-ops move risk; they don't remove it.** Coverage above the blocking line crushes the uptier hazard and raises the drop-down and deal-away hazard. The co-op's own legality is a dated scenario.
- **Rulings are regime switches with timestamps.** Encode them as documented log-odds jumps by wording class. Serta and Mitel, decided the same day, are the proof that tokens beat economics.
- **Never compare a CDS hazard with an agency default rate** without removing $\lambda_D$ and replacing the 40% convention. Most "the market is underpricing default" notes are units errors.

**The Spec You Hand the Robot.** "Build `lme_cycle_engine.py` per §14.7. Inputs: an event table with the schema given, or `LMEParams` for simulation. Hazards are per year under $\mathbb{P}$, recoveries are fractions of par, and the DE recovery is the value held immediately after the exchange. Estimate cause-specific Nelson–Aalen and Aalen–Johansen CIFs on first events only, and assert $S + \sum_k F_k = 1$ to 1e-10. Fit the post-DE clock as a mixture-cure Weibull with right-censoring. Never fit an exponential or set the hazard to zero after the last observed event. Report EL by coalition side (`in`, `out`, `blend`) by quadrature, and check it against Monte Carlo within 0.005. Fit the two-state binomial Markov-switching model on DE *counts*, with ordered shares and a log-space filter, and accept time-varying $P$ as a $(T,2,2)$ array. Never delete DE rows to 'exclude' them: report the ex-DE rate as a second output. Seed every generator. Raise on a horizon beyond `T_max`. Print PASS/FAIL for every check in block 5."

## Exercises

1. **Two rates, two hazards.** Moody's reports 5.8% including and 2.1% excluding distressed exchanges. Convert both to intensities, compute $\lambda_D/\lambda_H$, and compute the three-year $F_D$ and $F_H$. Then explain, in one paragraph a PM would read, why a CDX-implied hazard should be compared with only one of them.
2. **Kaz's parole question.** Using the mixture-cure model with $p = 0.25$, find $\eta$ for $k = 0.8, 1.0, 1.2, 1.5$ from the 70%-within-two-years condition. For each, compute the population hazard $h_H(u)$ at $u = 0.5, 2, 6$ years and the year-six increment in cumulative incidence. Which shapes satisfy all four Moody's facts? What does your answer say about when to short a post-LME loan?
3. **Which hump are you in?** You own \$10mm of a first-lien loan in a class where a co-op covers 70% and you are not in it. Under the §14.5.1 game ($m = 0.501$, $n = 10$, $\varphi = 0.10$), compute the probability of a non-pro-rata deal. Then let the sponsor buy defectors so that $\varphi = 0.35$. Using the coalition mixture with $\mu_{\text{in}} = 0.74$ and $\mu_{\text{out}} = 0.25$, what is the most you would pay to join the co-op, in points?
4. **The best-performing tranche.** An excluded Serta lender bought \$5mm face of the excluded first lien at 20 in January 2021. Using the July 2026 award, 9% simple prejudgment interest from 22 June 2020, a 60% probability that the award is collected in full by July 2027 and zero otherwise, and ignoring plan recoveries, compute the expected multiple and IRR. Then state every assumption a litigation-finance desk would attack.
5. **Fix ROBO.** Rewrite the instruction "exclude distressed exchanges from the default rate" as a spec of no more than 120 words that ROBO cannot misread. Include units, the output columns, what happens to the excluded issuers' future events, and one assert.
6. **Regime detection.** Simulate 40 years of DE counts with $\rho_0 = 0.30$, $\rho_1 = 0.63$, and mean defaults 90 per year, with a switch in year 30. Fit `fit_ms2` and report the first year in which the filtered LME-regime probability exceeds 0.9. Repeat with mean defaults of 12 per year (a private-credit-sized sample). How many years of "it's just noise" does the small sample buy you?

### Deep-Dive Resource Graph

**Podcasts**
- *Cloud 9fin*, 9fin's podcast on leveraged finance and restructuring (episode titles via 9fin's insights listing).
- *Bloomberg Odd Lots*: search the archive for episodes on liability management and creditor-on-creditor violence (titles not verified here).
- *Petition*, restructuring writing and podcast: https://www.petition11.com/archive.

**Practitioner Writing**
- Moody's (David Hamilton), *Lend, Extend, and Then?* (18 May 2026): https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html.
- Moody's, *America's Corporate Credit Is at a Tipping Point* (28 April 2026): https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html.
- 9fin, *A Crash Course on Co-ops*: https://www.9fin.com/insights/cooperation-agreement-crash-course. 9fin, *H1 2026 LME Update* (28 August 2026): https://www.9fin.com/insights/h1-2026-lme-update.
- Seaton, *The Value and Legality of Lender Cooperation Agreements*, HLS Bankruptcy Roundtable (14 April 2026): https://bankruptcyroundtable.law.harvard.edu/2026/04/14/the-value-and-legality-of-lender-cooperation-agreements/.
- Mayer Brown, *Serta Simmons Bedding: The Fifth Circuit's Uptier Decision and the Landmark Damages Ruling on Remand* (July 2026): https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand.
- Paul Weiss, *Appellate Review of Uptier Transactions* (10 January 2025): https://paulweiss.com/media/3985746/appellate_review_of_uptier_transactions_serta_and_mitel_decisions_reversed_on_appeal.pdf.
- Cleary Gottlieb, *Cooperation, Not a Cartel* (18 December 2025), on the Optimum antitrust complaint (title only).
- Baker McKenzie, *In the Know: Leveraged Finance Annual Report 2026* (January 2026): https://www.bakermckenzie.com/en/insight/publications/2026/01/-/media/files/insight/publications/2026/01/lev-fin-annual-report-2026.pdf.
- Matt Levine, *Money Stuff* (Bloomberg Opinion), passim on uptiers and "open market purchase."

**Academic Papers**
- Buccola & Nini (2024), *The Loan Market Response to Dropdown and Uptier Transactions*, 53 J. Legal Stud. 489.
- Parikh (2023), *Creditors Strike Back: The Return of the Cooperation Agreement*, 73 Duke L.J. Online 1.
- Ellias & Stark (2020), *Bankruptcy Hardball*, 108 Cal. L. Rev.: https://www.californialawreview.org/print/bankruptcy-hardball.
- Roe & Rotaru (2026), *Liability Management's Limited Runway*, HLS Bankruptcy Roundtable summary (link in §14.4 graph).
- Franks & Torous (1994), JFE 35; Altman, Brady, Resti & Sironi (2005), Journal of Business 78(6); Fine & Gray (1999), JASA 94(446); Hamilton (1989), Econometrica.

**Data & Code**
- Fifth Circuit opinion, *In re Serta Simmons Bedding*, No. 23-20181: https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf.
- CourtListener REST API (dockets, filing dates, opinions): https://www.courtlistener.com/help/api/.
- SEC EDGAR (LME 8-Ks, Item 1.01 and 2.03 filings, unrestricted-subsidiary designations): https://www.sec.gov/edgar.
- Federal Reserve, *Financial Stability Report* (May 2026): https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf.
- Vendor datasets, named without links: Moody's Default & Recovery Database, S&P CreditPro, Fitch leveraged finance recovery studies, PitchBook LCD default tracker (with and without LMEs), and the Octus, Debtwire and 9fin LME trackers.

<!-- STATUS: COMPLETE -->
