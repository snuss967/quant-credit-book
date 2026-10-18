# How to Use This Book: The Ramp, the Gates, the Ninety Days Before Day One, and How to Study With the Robot

*Every scene in these pages is fictional. Theo Marsh, Ines Okafor, Kaz Lind, Mags Dunleavy and ROBO are the book's cast; Dov Adler, Wen Zhao and Marcus Oyelaran belong to Vantress Capital Management, a fictional multi-manager platform. Their positions, prices and P&L are illustrative. The studies, chapters and files named in the prose are real, and each is cited where it appears.*

*Builds on:* the preface (the four seats, the cast, Theo's origin). *Used in:* Chapter 3-B §3B.8 (which takes over the ninety days after day one), Chapter 4-D (which assumes the study protocol described here), Chapter 26 §26.9 (the same protocol from the production side), Chapter 8-D (the home of the Pair Book) and every Part opener, each of which will close with the gate this front matter defines.

## Cold Open: The Sunday After the Offer

*Sunday 28 June 2026, eighty-six days before Theo's first day on Ines's desk (Tuesday 22 September 2026). A flashback.*

The kitchen table held three objects, laid out the way Theo laid out closing documents, in the order someone would need to sign them.

On the left was the offer letter, printed, because six years at PJT had taught him that a document does not exist until someone can staple it. In the middle was the reading list Ines had attached to the offer email. It was, give or take a lettered chapter, the table of contents of the book you are holding: twenty-eight numbered chapters, the primers beside them, appendices from A to F, well over a million words, or roughly a dozen novels' worth of a book that has ambitions to read like one. On the right was the USB stick with the 13-week cash flow model, which had gone to five interviews that week and been asked for once (§4D.10). It was having a good week.

A terminal was open on the laptop behind them. Theo had typed the obvious question: *I start on 22 September. Here is the list. What is the plan?*

ROBO answered in under a minute. It could work through the exercises in Chapters 1 to 28 and the lettered chapters, run every listing in Appendix F, and produce a summary of each chapter with its key results and worked solutions. Estimated completion: Tuesday.

It was ROBO's second generous offer of the weekend. On Saturday it had offered to build all twelve of the portfolio projects in Chapter 4-D, and Theo had declined that one too, for reasons that were still forming. Now he did the arithmetic a banker does on any proposal that arrives too quickly and too cheaply. A summary of the solutions is the solutions. If ROBO did the exercises by Tuesday, then on 22 September Theo would own an excellent summary of a book he had not learned, and he would be sitting at a desk that had hired him because, in a glass room one Thursday morning, he had made a market badly and out loud and updated in the open. Nobody consults a summary at 2:58 p.m. on the Friday before a lender call. There is no time, and in any case the summary does not know which way the client is leaning.

He texted Ines instead, which he was not sure was allowed. Her reply came forty minutes later, in three messages, in order of importance, the way she did everything.

*The derivations are yours. Nobody else's hands, including the robot's.*

*The builds, let it write. Then break what it wrote, on purpose, and see whether the tests notice.*

*Nothing goes to the robot until you've had a go at it yourself. Write your number down first. That's the hand history.*

A fourth arrived a minute later. *Pot is ninety days. The odds depend on whether you keep score.*

Theo typed *No thanks, not the exercises* into the terminal. ROBO replied *Understood* and waited for the next instruction. It did not mind. It never complains and never guesses, and it had no way of knowing that it had just been told the most useful thing anyone would tell Theo all summer.

He copied Ines's three messages onto an index card and propped it against the USB stick. Then he wrote the question underneath, the one he would spend the next eighty-six days answering: *How does a person studying alone at a kitchen table know that he is ready for Chapter 14 before he opens it?*

This front matter is the answer the desk gave him. It is short by the standards of this book and long by the standards of front matter, because it does a job no chapter does. The preface says what is in the book and offers four routes through it. These pages say where on the route you are, what you ought to be able to do before moving on, how to check that you can, and how to study alongside the same coding agent the book teaches you to direct. By the end you will have a map in which the arrows are module imports, three tiers of effort and a sense of which one each section is asking for, the four seat paths with hours attached, a model of the gate at the end of each Part, a ninety-day plan for the stretch between the offer and the first day, a working account of how to run the book's code and what a failing assert means, a protocol for studying with ROBO that survives the evidence on what agents do to learning, and the marker that lets you follow the Pair Book, the long-short thread that runs from Chapter 1-B to Chapter 28.

## 0.1 A Course Disguised as a Reference

A reference book is something you consult. A course is something that changes what you can do. This book has been both from the first edition, but it has mostly *looked* like the first, and a book that looks like a reference is read like one: a chapter at a time, when a question comes up, with a satisfying feeling of comprehension at the end of each section and no particular evidence that the feeling is justified.

The second edition's transition coach (one of the reviewers who read the first edition as a reader in Theo's position would) put the problem in one line. The book had roughly 160 exercises, uniformly hard and uniformly without solutions, and a reader who could not tell whether they had got Chapter 13's first exercise right could not tell whether they were ready for Chapter 14. "A desk," the review said, "would call it trading without a markout."

That sentence is the method of this front matter, so it is worth slowing down on the object it names.

> **Math, Gently.** *A markout is a grade that arrives later.* When a market maker buys a bond from a client, nobody knows at that moment whether the price was good. A markout answers the question by waiting. Take the trade price, wait a fixed horizon (five minutes, a day, twenty days), look at where the bond's mid has gone, and record the difference, signed so that a positive number means the trade made money. Say the desk buys \$2mm of a bond at 94.50 and twenty minutes later the mid is 94.25. The markout is $(94.25 - 94.50) \times 2{,}000{,}000 / 100 = -\$5{,}000$: the desk paid a quarter of a point too much, and the market said so without anybody having to have an opinion. One markout is noise. A few hundred of them, sorted by client, size or time of day, are a portrait of who at the table knows more than you. Ines calls the collection "the hand history." The full version, with the sign conventions and the decomposition that strips out the market's own move before blaming anyone, is in §3.3.

The study version of a markout has the same three parts. The trade is the number you write down before you look anything up: the skew of the bond, the hazard rate, the bid after the second sale. The later price is the book's check, which comes in three forms. Many exercises carry a parenthetical *Check:* with the number in it, the pattern Chapters 3 and 5 started and the second edition is spreading to every chapter along with tags (`[Read]`, `[Derive]`, `[Build]`) and time estimates. Every listing in Appendix F carries asserts, lines of code that stop the program with an error if a result is wrong. And Chapter 4-D's sixty tagged problems point at the sections that teach them. The worked solutions are being gathered into Appendix Z, which is being written in stages, primers and Part I first. The markout is the gap between your number and the check, and the hand history is the record of those gaps over weeks.

The method has a cost the reader feels immediately, which is that it is slower than reading. Writing a number down before checking it takes a minute, and being wrong in writing is less pleasant than being vaguely right in one's head. That unpleasantness is the point. A feeling of understanding is a Level 3 asset: marked to model, by the holder, who is also the one paid on the mark. An exercise with a check is a Level 1 price. Somebody, somewhere, will trade with you at it.

There is a second reason the desk insists on the number, and it took Theo a few weeks on the seat to see it. A trading desk is not short of people who understand things. It is short of people whose understanding can be *audited*, by a risk manager, by a PM, by a model review, by the explain at 7 a.m. The habit of writing the number first is the habit of being auditable, and a reader who builds it at a kitchen table in July arrives on the desk in September already speaking the desk's language, even before knowing most of its words.

## 0.2 The Map: The Primers Are Imports

The preface lists four primers and says, in one sentence, that they "build, once, what later chapters borrow." It is worth seeing exactly what is borrowed, because the borrowing is literal. Each primer ends in a module of code, and later chapters' code imports it.

| Primer | What it builds, in words | Its module (Appendix F) | Who imports it |
| :-- | :-- | :-- | :-- |
| **4-B** Bond math for the desk | Price, yield, day counts, duration in its five meanings, convexity, DV01, CS01, DTS, eight spreads, the callable bond | `bondmath.py` (§4B.9, listings in §F.4-B) | Chapter 5 (returns from prices), Chapter 8 and 8-B through 8-D (hedge ratios and risk), Chapter 19 (basket DV01), Chapter 24 (the bond leg of the basis) |
| **6-B** Options and the two measures | Payoffs as hockey sticks, replication, Black–Scholes, the Greeks as risk-report lines, jump-to-default, Girsanov for intensities | `credit_options.py` (§6-B.9, §F.6-B) | Chapter 6 (equity as a call), Chapters 13, 15 and 16 (LMT payoffs, change-of-control puts, rights offerings and warrants), Chapter 23 (the volatility surface), Chapter 12-C |
| **7-B** Statistics for credit panels | Panel regression with clustered errors, logistic models and calibration, survival analysis, shrinkage, PCA, the bootstrap, Monte Carlo | `creditstats.py` (§7-B.10, §F.7-B) | Chapters 8 through 12, 14 and 15, each of which "regresses, classifies, survives, shrinks, resamples or simulates" (§7-B.0) |
| **12-B** The restructuring process | Four documents, liens and subordination, voting thresholds, the out-of-court menu, Chapter 11 as a timed state machine, the fulcrum | `restructuring_state_machine.py` (§12B.10, §F.12-B) | All of Part IV (Chapters 13 to 17) and Chapter 12-C |

<!-- FIGURE: ch00_dependency_map.png (the foundations DAG: the four primers as nodes labelled with their modules; arrows as imports into Parts II to VIII; Part IV drawn behind the 12-B node; a second, thinner edge set in a contrasting colour for the RV path 1-B → 4-B → 5 → 8 → 8-D → 8-B → 8-C → 24 → 28; second-generation edges 8-B → 8-C, 8-B and §8.4 → 8-D, §3B.4 → 3-B's desk_calendar.py) -->

A second generation of modules sits on the first. Chapter 8-B's `risk_model.py` supplies the factor spread returns that Chapter 8-C's morning explain attributes against; Chapter 8-D's `pair_book.py` takes its rulers from §8.4 and its betas and limits from 8-B; Chapter 3-B's `desk_calendar.py` runs on the contract clocks of §3B.4, which are the grace periods and notice periods a restructuring banker already carries in his head, now written down as dated features. The figure the map will become draws these as arrows, because that is what they are.

The practical consequence is that the reading order in the preface is not a matter of taste. It is a dependency graph, and it fails the way dependency graphs fail. A reader who opens Chapter 14 before 7-B meets Kaplan–Meier curves, competing risks and a Markov-switching filter in their working clothes, without the introductions, and the chapter seems to be written in a dialect. Nothing is wrong with the reader or the chapter; an import is missing. The transition coach found exactly this in the first edition's suggested path for bankers, which sent them into Part IV before the survival analysis, Beta regression and option payoffs it uses had been built. The preface now routes every seat through the primers for that reason.

One honest footnote belongs on the map. The arrows are imports in intent. At the time of writing they are imports you perform with copy and paste, because the directory where the modules are meant to live, `book_src/lib/`, has not yet been created, and the change that would put it on the checker's path has not landed. Section 0.7 explains the workaround. Most imports at most desks began this way, as a listing someone pasted above their own and promised to clean up later.

The map has one more edge set, drawn thinner and in a different colour, which belongs to the thread section 0.9 describes. It runs from the pod's Tuesday in Chapter 1-B through bond arithmetic (4-B), the survive-or-jump mixture (5), the decomposition that strips beta (8), the life of a pair (8-D), the limit sheet that sizes it (8-B), the explain that judges it (8-C), the basis on its short leg (24), and the year-end review that pays for it (28). A reader who follows only those edges will have read about a fifth of the book and understood the one trade every multi-manager platform in the world is organised around.

## 0.3 Three Tiers: Reading, Deriving, Building

*Friday 25 September 2026, 5:40 p.m., the end of Theo's first week on the desk. Fictional.*

Ines kept the reading list on paper, and by Friday Theo's copy had acquired a pencilled 1, 2 or 3 beside every section, in her handwriting, which looked like a ticket someone had written in a hurry and meant.

Kaz read it upside down from across the desk. "Tier 3," they said. "Is that like a mezzanine tranche? Subordinated, thin, first to absorb losses?"

"It's the one where you build it," Theo said.

Mags did not look up from her screen. "Tier 3 is where you find out the model was wrong."

Kaz considered this. "So, first to absorb losses."

Nobody corrected them, because nobody could find the error.

The tiers describe what a section asks the reader to *do*, not how hard it is. The same chapter usually holds all three, and the clearest way to see the difference is to watch one idea pass through each.

**Tier 1 is reading.** A Tier 1 section is done when you can retell its idea to someone else with a picture and one number. The survive-or-jump mixture in §5.1 is the model case. Its whole content can be drawn on a napkin, and the napkin is worth more than a page of formulas for most of what a desk does with it.

> **Math, Gently.** *A distribution, and a mixture of two.* A distribution is a list of the things that can happen, with how often each one happens: the outcomes along the bottom of a chart, the frequencies as the height of the bars. Many quantities on a desk have a familiar single-humped shape. A one-year high-yield bond's return does not. With high probability the company survives, and the return lands in a tall, narrow hill near the coupon. With small probability it defaults, and the return lands in a separate lump far to the left, near the recovery. The two pieces are a *mixture*: one distribution for each world, weighted by how likely the world is. A tiny number makes the shape vivid. Take a bond at par with a 7% coupon, a 4% chance of default within the year, and recovery of 40. The surviving world returns about +7%; the default world returns about −60%. The mean is $0.96 \times 7\% + 0.04 \times (-60\%) = 4.32\%$, a number that almost no actual outcome lands near. Most years the bond does better than its mean, and in the year it does not, it does very much worse. The full version, with the variance, the skew and the "fourteen-sigma Tuesday" that a normal distribution cannot explain, is §5.1.

**Tier 2 is deriving.** A Tier 2 section is done when you can produce its result on paper, from the line before, without looking. Some derivations deserve this because the result is used constantly and misremembered constantly; others because the derivation is where the idea actually lives, and a reader who has only seen the conclusion will apply it where it does not hold. Itô's lemma in §6.1 is the cleanest example of the second kind.

> **Math, Gently.** *The volatility tax, at all three tiers.* Read it first: if an asset's price is random and grows at an average rate $\mu$, the typical path (the median) grows more slowly than the average, at about $\mu - \tfrac12\sigma^2$. With $\mu = 5\%$ and $\sigma = 40\%$, the tax is $\tfrac12 \times 0.40^2 = 8\%$ a year, so the average path ends up 5% a year but the median path *shrinks* by about 3% a year. A few very good paths drag the average up; most paths never see them. That is the Tier 1 version, and for many purposes it is enough. Then derive it: write the log price $f(S) = \ln S$ and expand to second order, as ordinary calculus would refuse to do,
>
> $$
> d(\ln S) = \frac{dS}{S} - \frac{1}{2}\frac{(dS)^2}{S^2} = \mu\,dt + \sigma\,dW - \frac{1}{2}\sigma^2\,dt,
> $$
>
> where the last step uses the one fact that makes randomness different, $(dW)^2 = dt$. In ordinary calculus a squared small change is negligible. Here it is not: a random step of size $\sqrt{dt}$, squared, is a step of size $dt$, and it stays in the answer as the $\tfrac12\sigma^2$. Then build it: simulate a hundred thousand price paths for one year with those numbers, and compare the average ending price with the median. The average sits near $e^{0.05} \approx 1.051$ times the start, the median near $e^{-0.03} \approx 0.970$, and the gap is the tax. The Monte Carlo machinery, with standard errors so that you know whether the gap you see is real, is §7-B.8. The full derivation, and why the tax decides whether a structural model's default probability is a $\mathbb{P}$ number or a $\mathbb{Q}$ number, is §6.1.

**Tier 3 is building.** A Tier 3 section is done when the engine runs and its asserts pass, and when you can say what each assert is protecting against. Section 6.11 is the model: one module for structural and intensity models, whose listings live in Appendix F (§F.6), with asserts that refuse a negative hazard, a survival curve that rises, and a default probability outside zero and one. The building is the exercise, and section 0.8 describes how the work divides between the reader and the coding agent at this tier, because it divides differently from the way most readers expect.

A full table, every section of the book with its tier, is planned for the first page of Appendix Z. What fits here is the summary by Part, which is enough to plan a week.

| Part | Mostly Tier 1 | Where Tier 2 concentrates | The Tier 3 builds |
| :-- | :-- | :-- | :-- |
| I. Arrival (1–4-D) | Chapters 1, 1-B, 2, 4, 4-C; the cold opens and case studies throughout | §3.1–3.3 (two-point distributions, Glosten–Milgrom for RFQs, markouts); §4B.2–4B.5 (price–yield, duration, DV01 and DTS) | `bondmath.py` (§4B.9); the RFQ and markout engine (§3.8); 3-B's `desk_calendar.py` |
| II. Foundations (5–7-B) | §5.2's three distributions; §6.10's Carvana and Hertz | §5.1 (mixture moments and skew); §6.1 (Itô); §6.2 (Merton); §6.8 (the hazard bootstrap); §6-B.2 (replication); §6-B.6 (the two measures); §7-B.1 (clustered errors); §7-B.4 (survival) | §6.11's engine; `credit_options.py`; `creditstats.py`; Chapter 7's purged, issuer-grouped validation |
| III. Isolating IDO (8–12-C) | The case studies in §8.7 and §10.7; most of Chapter 11's narrative | §8.1 (the decomposition); §8.4 (DTS); §8B.5 (the jump layer); §8C.4 (the foot); §9.7 (effective breadth); §12.4 (the two-state filter) | The IDO engine (§8.9); `risk_model.py`; `pnl_explain.py`; `pair_book.py`; the factor lab (§9.11) |
| IV. Restructuring (13–17) | For the banker, much of it: this is home turf with numbers attached | §13.3 (the uptier as a recovery transfer); §13.4 (threshold games); §14.2 (competing risks); §14.3 (the re-default clock) | The Priming Risk Score (§13.8); the Markov-switching engine (§14.7); 12-B's state machine |
| V. Markets (18–22) | §18.1, §18.8 and Chapter 22's regulatory ledger | §18.3–18.6 (Glosten–Milgrom, Avellaneda–Stoikov, jump-to-default in the HJB); §19.2 (the master equation); §20.3 (the arbitrage band) | The quoting engine; the basket pricer; the ETF monitor (§20.7) |
| VI. Cross-asset (23–24) | §23.1; §24.1 | §23.2 (CreditGrades); §24.2 (pricing the swap); §24.5 (the delivery option) | The basis monitor (§24.7) |
| VII. Machines (25–27) | Chapter 26's Trend Watch and case studies; §27.1 | §25.3 (basket arithmetic); §27.5 (queues) | The definition graph (§25.2); the agent harness (§26.12); the trigger tables (§27.6) |
| VIII. The PM (28) | §28.8 | §28.2 (effective breadth); §28.4 (Kelly with jump-to-default) | The PM dashboard (§28.9) |

How much to skip is a judgment the table can inform but not make. The pattern that worked for Theo, and for the readers the transition coach had in mind, runs roughly as follows. Tier 1 sections are almost never worth skipping: they are cheap, they carry the vocabulary, and they are where the book tells you which of its tools apply to the situation in front of you and which do not, which is the part no formula supplies. Tier 2 derivations can be read on a first pass and derived later, at the gate (section 0.5), as long as the gate actually happens; a derivation read but never produced is a feeling, not a skill. Tier 3 builds are the exercises themselves, and a reader who skips them has read a cookbook without cooking. The exceptions are real. A reader who is not going to quote bonds can read Chapter 18's builds at Tier 1 and lose little; a reader who will never sit near a restructuring can do the same with 12-B's state machine and lose a little more than they think.

## 0.4 Four Seats, With the Primers Routed In

The preface gives four seats and a route for each. What follows is the same four routes, written as section sequences with the primers placed where their imports are first needed, the second edition's lettered chapters placed on the paths, and a rough number of hours attached.

The hours are a prior, not a promise. They assume Tier 1 reading at something like 3,500 words an hour, Tier 2 at the sections named in the tier table and roughly an hour per derivation, and Tier 3 builds with the coding agent drafting and the reader breaking, at two to four hours each. A reader who keeps the hand history (section 0.6) will know within two weeks whether their own rate is faster or slower, and should replace the prior with the data, which is the only thing the book ever asks anyone to do with a prior.

| Seat | The route | Rough hours |
| :-- | :-- | --: |
| **1. Market maker** | 1-B → Part I with 4-B and 2-B (transaction cost analysis) → 3-B → Chapter 8 → 8-B → 8-C → Part V (18–22) → 7-B as Chapter 18 calls on it | 180–220 |
| **2. Systematic HY or IG PM** | 1-B → Part I → 4-C → 5 → 6 → 6-B → 7 → 7-B → Part III (8, 8-B, 8-C, 8-D, 9–12) → Part VIII → 12-B → Part IV last | 230–280 |
| **3. Event and distressed quant** (the banker's spine) | 1-B → Part I → 4-B → 4-C → 5 → 6 → 6-B → 7-B → 12-B → 12-C → 8-D → Part IV (13–17), with 13 and 25 read back to back | 210–250 |
| **4. Risk and strat** | 1-B → 4-B → 6-B → 7-B → 8 → 8-B → 8-C → 22 → Part VI (23–24) → 27 | 160–200 |

<!-- FIGURE: ch00_seat_paths.png (the four seat paths drawn as transit lines over the table of contents; the lettered Edition 2 chapters as stations; the four primers as interchange stations where lines cross; 4-D drawn as a feeder line into every path's first station for the reader without an offer) -->

Several of the stations need a sentence on why they sit where they do. Chapter 1-B, the week in five quant shops, is on every path's first week, because it is the cheapest way to find out which of the five rooms you are walking into and therefore which path is yours. Chapter 3-B, the first year on the desk, belongs right after Chapter 3 for anyone with a start date, because it tells you what the desk will measure you on, and studying without knowing the measure is the kind of optimisation ROBO would do. Chapter 4-C, one bond seen from seven seats, is on the PM and distressed paths because both seats spend their careers trading against the other six. Chapter 4-D, getting the seat, comes before everything else for the reader without an offer, and can wait for the reader with one. Chapters 8-B and 8-C, the risk model and the morning explain, are on the market-making and risk paths because those seats read them every morning; 8-D, the Pair Book, is on the PM and distressed paths because that is where the long-short trade lives. Chapter 12-C goes immediately after 12-B on the distressed path, because 12-B builds the process and 12-C prices what the process produces, and the two read as one argument.

Three further lenses cut across the seats rather than replacing them.

**The AI-agent specifier.** The preface's lens for anyone who will direct coding agents: read every `### Specification for AI Implementation` block in order, starting with Chapters 5 to 8, then 13, 18 and 19, then 25 to 27, with Chapter 26 as the operating manual. What this front matter adds is that the specifier's path and the study protocol of section 0.8 are the same skill seen from two sides. A reader who has written down what a function should return before asking for it has written a spec; a reader who has broken ROBO's version on purpose has reviewed one.

**The TREND path.** Chapters 2, 4, 10, 14, 17, 21, 22 and 26, each marked TREND in the table of contents, then Appendix C's Trend Tracker. It is the right path for a reader who needs to talk intelligently about the market's structure before they need to compute anything in it, and the wrong path for a reader with a start date on a trading desk, who will be asked to compute first.

**The RV path.** 1-B → 4-B → 5 → 8 → 8-D → 8-B → 8-C → 24 → 28: the long-one-credit, short-another trade from the first time the reader sees it on a pod's Tuesday to the year-end review that decides what the pod is paid. Section 0.9 describes it, because it is less a path than a second book running inside this one.

