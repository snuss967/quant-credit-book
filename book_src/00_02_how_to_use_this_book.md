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

## 0.5 The Gates: "Before You Leave This Part, You Can…"

*Wednesday 30 September 2026, 12:20 p.m., the desk's lunch table, Theo's second week. Fictional.*

Theo mentioned that each Part of the reading list ended in a gate, and Kaz brightened, because this was a word they knew.

"Like the gate on a semi-liquid credit fund? Five per cent of the shares a quarter, pro rata, and everyone who asked for more joins the queue?"

"The other kind," Theo said.

"In the other kind, how many get through each quarter?"

"Everyone who can do the ten things."

Kaz thought about it while eating a sandwich in the methodical way Kaz ate everything. "Then it isn't a gate. A gate rations a shared resource. Yours has no capacity constraint; nobody else's request changes your fill." They put the sandwich down. "It's a test with a door."

That is a better definition than the one Theo had been given, and it is the right one. Chapter 17 §17.6 has the other kind of gate, where a 5% quarterly cap turns a run on a fund into a twenty-quarter queue and the order of the requests matters a great deal. The gates in this book ration nothing. They answer one question for one reader, the question on Theo's index card: am I ready for the next Part, or do I only feel ready?

Each Part opener will close, in this edition, with a list of ten things the reader can do on leaving the Part. Every item names the section that builds it and the exercise that tests it, and Appendix Z, as it fills in, will hold the worked solution. The gate is a markout, not a quiz. A quiz asks whether you recognise the right answer among four. A gate asks for the number, written down before you look, and the number is either within the check or it is not. There is no partial credit for having read the section recently.

Here is the Part II gate in full, as the model for the other seven. It is the gate the transition coach drafted first, and it is the one where the most readers will discover that they had a feeling and not a skill.

| # | Before you leave Part II, you can… | Built in | The check |
| :-- | :-- | :-- | :-- |
| 1 | Compute by hand the skew of a one-year bond with a 4% default probability, and say why the shortcut $-1/\sqrt{\text{PD}}$ is close | §5.1.3 | About −4.7; the shortcut gives −5 |
| 2 | Derive the $\tfrac12\sigma^2$ in Itô's lemma on paper from $(dW)^2 = dt$, and say in one sentence what it does to a median path | §6.1.2 | The median grows at $\mu - \tfrac12\sigma^2$ |
| 3 | Explain to Kaz why $N(-\text{DD})$ is not a default probability anyone should quote | §6.4.3 | At a DD of 4 the normal says about 3 in 100,000; most firms sit at 4 or above and default anyway, so the desk maps DD through an empirical table |
| 4 | Bootstrap a hazard curve from five CDS quotes, and flag the bucket where the hazard goes negative | §6.8 | A negative bucket means survival rises with time: a stale quote or an arbitrage, never a probability |
| 5 | Turn a spread and a recovery into a hazard rate in your head | §6.8 | 300 bp at 40% recovery is about 5% a year |
| 6 | Say which measure a number is in before you say the number | §6-B.6 | A CDS-implied PD is $\mathbb{Q}$, a cohort default rate is $\mathbb{P}$, and their ratio is a premium, not an error |
| 7 | Replicate a one-period option with the stock and a bond, and read the risk-neutral probability off as a ratio of prices | §6-B.2.2 | The probability comes from prices, not from anyone's forecast |
| 8 | Cluster a panel regression by issuer and watch a t-statistic of six fall to about two and a half | §7-B.0, §7-B.1 | Eleven bonds of one issuer are one observation wearing eleven CUSIPs |
| 9 | Fit a Kaplan–Meier curve to a cohort with censored bonds, and say what dropping the censored ones does | §7-B.4 | It throws away survivors, so the default rate comes out too high |
| 10 | Split a panel for validation so that no issuer sits in both the training and the test set | §7.7 | The grouping key is the ultimate parent, not the CUSIP |

> **Math, Gently.** *Skew, and why a 4% bond has so much of it.* Skew measures lopsidedness: how much a distribution leans to one side, in units of its own spread. A symmetric bell has skew zero. The survive-or-jump bond of section 0.3 is about as lopsided as an everyday instrument gets, and the arithmetic fits on a napkin. Treat the bond's outcome as a coin that comes up "default" with probability $p$. The skew of such a coin is $(1 - 2p)/\sqrt{p(1-p)}$, and because default is the *bad* side for a bondholder, the bond's return carries the minus sign. At $p = 0.04$, $\sqrt{0.04 \times 0.96} \approx 0.196$ and $1 - 2p = 0.92$, so the skew is $-0.92/0.196 \approx -4.7$. When $p$ is small, both $1 - 2p$ and $1 - p$ are close to one, which leaves $-1/\sqrt{p} = -5$: the shortcut in the gate. Notice which way it moves. The *safer* the bond, the *more* skewed it is, because the rarer the default, the further it sits from everything else in units of a standard deviation. That is why a normal distribution, which has no skew at all, calls a day that a mixture finds ordinary a fourteen-sigma event. The full version is §5.1.3.

Theo failed item 4 the first time, in the second week of August, and the way he failed it is typical. His bootstrap produced a hazard of −0.4% a year in the bucket between three and five years, and he did not flag it, because the survival curve still looked like a survival curve and the number was small. Kaz, who saw the hand history a month later, explained the problem in one sentence: a negative hazard means the probability of surviving to five years is *higher* than the probability of surviving to three, which is not a probability statement about the company but a statement that somebody's quotes do not agree with each other. Either a quote was stale or there was an arbitrage, and the desk's answer to both is the same, which is to find out before using the curve. The gate item exists because the failure is silent. Nothing crashes. The number is merely impossible.

The other seven gates are summarised here in a line each; their full lists close the Part openers.

| Part | The gate, in one line |
| :-- | :-- |
| I. Arrival | Price a two-point bond in both measures; quote the bid after two sales from a seller who may be informed (§3.2); compute a markout with the sign right (§3.3); compute DV01 and DTS for one bond and size its hedge (§4B.5); fill in your own rows of the Edge Ledger (§3.5) |
| III. Isolating IDO | Decompose a bond's return into rates, spread beta and residual with the right signs (§8.1); hedge in DTS rather than notional (§8.4); make an explain foot (§8C.4); size a pair to a stop (§8D.5); filter, not smooth, a two-state regime (§12.4) |
| IV. Restructuring | Find the fulcrum (§12B.6); write an uptier as a transfer of recovery (§13.3); score one credit agreement for priming risk (§13.8); split a default intensity into competing risks (§14.2) |
| V. Markets | Derive the reservation price and spread of a market maker (§18.4); put jump-to-default inside it (§18.6); price a portfolio trade's four terms (§19.2); derive an ETF's arbitrage band (§20.3) |
| VI. Cross-asset | Turn equity volatility into a spread (§23.2); price the two legs of a CDS (§24.2); name the four things people mean by "basis" (§24.3) |
| VII. Machines | Turn a definitions article into a graph and find the add-back fixed point (§25.2, §25.3); write a spec with invariants that ROBO cannot satisfy vacuously (§26.9); explain why a kill switch is a stopping rule (§27.7) |
| VIII. The PM | Compute effective breadth when issuers cluster (§28.2); size with Kelly through a trapdoor and say why the answer is a fraction of it (§28.4); state the standard error of a year of P&L (§28.8) |

A reader on one of the seat paths of section 0.4 meets only the gates on their path. A market maker who never opens Part IV never faces its gate, and should not feel bad about the fact; the gate is for the Part you are leaving, not for the book.

## 0.6 The Ninety Days Before Day One

*Thursday 8 October 2026, 6:45 p.m., Theo's third week. Fictional.*

Mags found the calendar because it fell out of Theo's notebook. It was a single printed page, ninety boxes in rows of seven, every box filled in pencil with section numbers and a time, most of them crossed through, a few circled in red. Week eleven had a coffee ring on it.

She held it at arm's length, the way she held anything with a formula on it.

"Back in my day," she said, "the study plan was a Bloomberg terminal and someone shouting. You learned what a make-whole was when a salesman screamed it at you across the floor at four o'clock, and you learned what a springing lien was when one sprang." She turned the page over, as though there might be more on the back. "My first restructuring, I read the indenture on the plane. The second one, I read it before the plane. That was the whole curriculum."

"Did it work?"

"For the ones who survived it." She handed the calendar back. "This has a calendar. It has the red circles where you got it wrong." She paused, the way she paused before saying anything kind. "It's better than shouting. Don't tell anyone I said so."

The plan that page records was built from the transition coach's 30/60/90 proposal, adjusted for the arithmetic of one person's evenings, and it is offered here as a worked example rather than a prescription. Ines's offer arrived at the end of the interview week of Chapter 4-D, the calendar started on Sunday 28 June, and the first day was Tuesday 22 September, which is eighty-six days away; the plan was called ninety because every plan is, and the missing four came out of sleep, which is how every plan the desk has ever written was funded.

The first thing the calendar settles is how many hours there are. Theo budgeted twelve to fifteen a week, two evenings and most of a weekend day, around a notice period at PJT that was supposed to be quiet and was not. Over a little more than twelve weeks that is somewhere between 150 and 185 hours. The book, read in full at the pace assumed in section 0.4, would take something like twice that. So the plan does not read the book. It reads the parts of the book that the first ninety days on a desk will draw on, at the tier those days will demand, and leaves the rest for the year. This turns out to be the most realistic feature of the whole exercise. A desk never has time to read everything either; it triages, and the triage is a skill.

| Days | Chapters, and the tier they get | Projects and checkpoints | Hours |
| :-- | :-- | :-- | --: |
| 1–30 | 1-B in full; Chapters 1, 2 and 4 at Tier 1 (cold opens, case studies, the Trend Watches); Chapter 3 with §3.1–3.3 at Tier 2; 3-B; 4-B at Tier 2 with `bondmath.py` built; Chapter 5 with §5.1–5.3 at Tier 2. Appendix A's phrasebook (§A.10) open on the second screen throughout | Edge Ledger rows drafted (§3.5); the Part I gate on day 30 | 55–60 |
| 31–60 | Chapter 6 with §6.1, §6.2, §6.4 and §6.8 at Tier 2 and §6.11 built; 6-B; Chapter 7 at Tier 1 except §7.7; 7-B at Tier 2; Chapter 8 through §8.4 | Portfolio project 1 (the TRACE panel and the Roll spread by trade size) and project 6 (the DD-to-PD map with issuer-grouped validation), from §4D.11; the Part II gate on day 60 | 55–60 |
| 61–86 | 12-B; Chapters 13 and 14 at Tier 1 with §13.3, §13.8 and §14.2 at Tier 2; Chapter 18 through §18.6 | Project 2 (the Priming Risk Score on public credit agreements) and project 4 (the RFQ quoting game with a hand history); Chapter 4-D's sixty tagged problems; a mock interview, or for a reader with an offer, a mock morning | 45–55 |

<!-- FIGURE: ch00_ninety_days.png (a calendar strip, days 1 to 90 with days 87 to 90 hatched as "funded by sleep"; chapters above the line, coloured by tier; projects and the three gate checkpoints below; the mock interview or mock morning at day 86; an arrow off the right edge labelled "§3B.8: the ninety days after") -->

A few choices in that table carry most of its weight. Appendix A's phrasebook sits beside the first month because the ex-banker's hardest problem in the first weeks is not an equation; it is that he already has a word for everything and every word is subtly wrong. "Downside case" becomes a left tail at a stated horizon, "cushion" becomes a distance to a barrier, "the market is pricing in" becomes a $\mathbb{Q}$ quantity that is not a forecast, and the dictionary is where those translations live (§A.10). Projects 1 and 6 come in the second month because they force the reader to touch real data (TRACE prints, filings, equity prices) and to make the two mistakes everyone makes with it, the look-ahead join and the issuer that appears in both folds, before anyone is paying for them. Projects 2 and 4 come last because they are the two a desk head asks about first: one reads documents as features, the other plays the market-maker's game against an informed counterparty and scores it by markouts.

The last box is a choice between two endings. A reader still looking for a seat ends the ninety days with a mock interview built from Chapter 4-D: a market on something with a document answer, a Kelly question with a trapdoor, and a pitch delivered as a distribution. A reader who already has the seat, as Theo did, ends with a mock morning instead. He took a week of public prices for a handful of bonds, built the explain he expected the desk to show him, wrote down in advance the line he thought would refuse to tie, and checked it against what actually happened. The prediction was wrong in an instructive way (he had forgotten accrued interest on a bond that went ex-coupon midweek), which is exactly what the first thirty days on the seat would ask of him.

The ritual that held the plan together took one hour on Sunday evenings. Theo listed the week's exercises, and for each one he wrote down his number, the check, the gap, the minutes it took, its tier, and a confidence he had recorded *before* checking: 50, 70 or 90 per cent. Ines called it the hand history, and the name is exact. A poker player reviews hands to find the leaks that a single session hides; a trader reviews markouts for the same reason; a reader reviews the week's exercises to find which kind of mistake is recurring, which is almost never the kind they expected.

> **Math, Gently.** *How many exercises before you know you are good.* Suppose that after the first month the hand history shows 25 exercises, 18 of them right within the check. The hit rate is $18/25 = 0.72$. How sure can you be that it is really 0.72 and not, say, 0.60? A hit rate built from $n$ independent tries wobbles by about one *standard error*, $\sqrt{p(1-p)/n}$. Here that is $\sqrt{0.72 \times 0.28 / 25} \approx 0.09$. A rough 95% band is two standard errors either side, about 0.54 to 0.90, which is wide enough to include "fine" and "not yet." After a hundred exercises at the same rate the standard error halves to about 0.045, and the band narrows to 0.63 to 0.81. The lesson is not that 25 exercises are useless; it is that a month of exercises can tell you that you are not hopeless, and it takes a quarter to tell you that you are good. Section 4D.10 does the same arithmetic on a year of trading calls (forty calls at 55% have a standard error of about 7.9 points, which makes a 55% year indistinguishable from a coin), and §28.8 makes the same argument from the PM's chair. The general machinery of standard errors, including what happens when the tries are *not* independent, is §7-B.1 and §7-B.8.

The confidence column turned out to be the most useful thing in the hand history, more useful than the hit rate. By the end of July, Theo's 90% answers were right about 75% of the time, and his 50% answers were right about 70% of the time. He was overconfident about the derivations he had read recently and underconfident about the arithmetic he had done for years at PJT, which is the standard profile of an ex-banker in month one, and the calibration table said so before any person had to.

> **View From Another Seat.** *Three rooms reading the same ninety-day plan.* Show Theo's calendar to the head of a **dealer's market-making desk** and the first question is whether, by day ninety, he can predict the morning explain: which line will be large, which will refuse to tie, which hedge leg will need a roll quote. The plan's mock morning is the part she would read twice. Show it to the PM of a **multi-manager pod** and the question is about the ledger: is every view written as a sentence with a date in it, with the hedge, the ratio and the exit stated before the trade, so that a risk manager can audit the book without asking what anybody meant? The hand history is the part he would read twice. Show it to a **distressed fund** and the question is about documents: has the candidate read a credit agreement this summer, all of it, including the definitions article and the exhibits, and can he say which paragraph moves the price? Project 2 is the part that room would read twice, and it would wonder, politely, why it comes so late. None of the three is wrong. They are describing different jobs, and the plan's own seat path (section 0.4) is what decides which of the three is reading.

The ninety days end where Chapter 3-B begins. Its §3B.8 takes over on the first day of the seat, with a plan that is shorter than Theo expected, because the desk does not want a plan from a new hire; it wants evidence that he can be given a clock. In days 1 to 30 he reads the feed diff, the security master, the explain and the risk pack every morning, until he can predict the unexplained line before he sees it; by days 61 to 90 he ships one feature through the first rung of the deployment ladder (replay, then paper, §27.8). The artifact that bridges the two plans is the RSSG Edge Ledger of §3.5: the inventory of what the banker brings, with a decay rate on each skill. Theo drafted his rows in the first month at the kitchen table, revised them after the Part II gate, and brought them to the desk on day one. It was the first document anybody on the desk asked him for, and the only one from the summer that he had written entirely himself.

## 0.7 Run the Book

*Tuesday 11 August 2026, 11:15 p.m., day forty-five of the plan. Fictional.*

Theo had five CDS quotes for a single-B issuer, copied from a public source for a project, and a theory that the book's bootstrap in Appendix F would turn them into a hazard curve faster than his own version, which had taken a weekend. He pasted the quotes over the listing's example quotes, ran it, and watched it stop.

`AssertionError: I: bootstrap reprices every quote`

Above it, a warning: a negative hazard on the bucket ending at five years, *check quotes/recovery*.

It was late, and he had a banker's reflex about documents that fail at 11 p.m., which is that someone else drafted them badly. He wrote to Kaz, who had given him an email address at the end of the interview "in case the Sharpe ratio keeps you up at night." *I think the book's code is broken. Chapter 6 bootstrap. Assert fails on real quotes.*

The reply came four minutes later, which said something about Kaz's evenings. It was one line.

*That's the exercise.*

It was the same bucket his own bootstrap had let through without comment the week before (section 0.5). His version had produced a small negative number and carried on. The book's version had refused to carry on, by design, because a negative hazard is not a small number but an impossible one, and the listing's author had decided long before Theo arrived that the code would stop rather than hand an impossible number to whatever came next. A failing assert is not a bug report. It is the grade, delivered by someone who thought about the mistake before you made it.

The mechanics, so that nothing about running the code is a mystery.

**What you need.** Python 3.9 or newer (the floor the README sets, from the pinned packages and the annotations the listings use) and the seven packages in `requirements.txt`: NumPy, SciPy, pandas, scikit-learn, statsmodels, networkx and PyMuPDF. The listings themselves lean almost entirely on NumPy, SciPy, pandas and the standard library; PyMuPDF serves the tooling that indexes the source PDFs, not the reader.

**Where the code lives.** Since the second edition, the chapters carry no code at all. Every listing has moved to Appendix F, grouped by chapter (§F.6 holds Chapter 6's listings, §F.7-B holds 7-B's), each with an anchor of the form `#code-6-6`, and each chapter explains in prose, at the point where a listing used to sit, what it computes, why it is built that way, and when it breaks. Within one chapter's section the listings accumulate like the cells of a notebook: a later one may use any name an earlier one defined, so a listing pasted on its own will fail with a `NameError` until the ones above it are pasted too. Nothing carries over from one chapter's section to the next.

**How to run it.** The checker, `tools/check_book.py`, takes any Markdown file, joins its ```` ```python ```` blocks in order into one script, skips any block whose first line is `# sketch`, and runs the script in a fresh temporary directory, with a ten-minute timeout by default. Pointed at a chapter it now finds nothing to run, because the chapters hold no code. Theo's habit, which is as good as any, was to save one chapter's section of Appendix F as its own Markdown file and point the checker at that, with `--file` and `--run-code`. Pointed at the whole appendix, the checker runs every chapter's listings in one interpreter, one after another, which tests the appendix rather than any one chapter.

**The missing directory.** The reusable engines (`bondmath.py`, `creditstats.py`, `risk_model.py` and the rest) are meant to live in `book_src/lib/`, where a later chapter's code can import them. At the time of writing that directory does not exist, and the change that would put it on the checker's path has not landed. Until it does, the README's workaround applies: set `PYTHONPATH` to the absolute path of `book_src/lib` before running the checker, which passes your environment through, or paste the defining listing above the ones that need it. This is the copy-and-paste import that section 0.2 apologised for.

**What "(illustrative)" means.** The tag appears more than four hundred times in the book's source. A number so marked is a worked example on the book's fictional issuers (Halvorsen, Kestrel and their neighbours), or a replay of a real episode with invented sizes, prices or P&L. It is never a quotation of a market. Numbers that come from a source say so, with the source. The distinction matters most in exactly the place readers are most tempted to ignore it: a worked example whose numbers look plausible enough to be real is the one most likely to be repeated in an interview as though it were.

#### Quant-Shop Life: Ticket Number Four

*A bank's credit-trading desk, the first two weeks of a new analyst. A fictional composite; the bank, the people and the tickets are invented, and the process is a typical one rather than any firm's.*

On day one there is a badge, a laptop, a desk with someone else's sticky notes still on the monitor, and a list of mandatory training modules that the analyst completes by Thursday: the code of conduct, information barriers, anti-money-laundering, the personal-trading policy, and the policy on the personal-trading policy. Her brokerage accounts go on a disclosure form. Any trade in them now needs pre-clearance, which she will discover in March when she tries to sell a mutual fund.

On day two she files a request for market-data entitlements. Each vendor feed is a licence with a cost centre, so each needs the desk head's approval and the market-data team's, in that order, and the desk head is travelling. The evaluated-price feed arrives on day six. The bond reference data, without which the evaluated prices are a column of numbers attached to identifiers nobody can read, arrives on day nine.

The laptop cannot reach the public package index. Packages come from an internal mirror, two minor versions behind, and anything not already on the mirror needs a ticket. She files the first ticket on day three, for a statistics package. On day four she discovers that a listing she wants to run also needs a graph library, and files a second ticket. The third, on day five, is for a package that turns out to be on the mirror under a different name. The fourth is the one she still tells people about: a request to approve a version of a package that the mirror already had, filed because the error message said a version "or later" and she had not read the "or later."

Her first query against real data runs on day nine. Her desk head's only comment at the Friday review is that day nine is good for this floor. The analyst who joined the same week from a systematic fund, and who had run the book's listings on his own laptop over the summer in a clean environment, filed one ticket on day two listing every package he would need. He had his first query on day six, and he spent days six to nine finding out that the evaluated prices for one sector were three days stale, which became the first thing anybody on the desk thanked him for. The transition coach's review has a phrase for the gap between them: time to first compute. Nothing in it is about talent.

#### The hand history as a listing

The Sunday ritual of section 0.6 is a small computation, and by the third week Theo wanted it done the same way every week, which is the usual reason anything on a desk becomes code. His first request to ROBO was the vague version, *track my progress*, and what ROBO built from it was a progress bar that advanced by one per cent for every page of the book he marked as read. It reached 31% in the first week. It had no way to go down, which made it the most encouraging and least informative object Theo owned.

What he needed instead was the markout of section 0.1, computed over a week of exercises. The listing in Appendix F takes the week's rows, one per exercise, each with its tier (`read`, `derive` or `build`), the confidence written down before checking (as a fraction between zero and one), whether the answer fell within the check (true, false, or `None` when no check exists yet), and the minutes it took. It returns four things: the hit rate with its standard error, overall and by tier; a calibration table, the realised hit rate at each stated confidence; the minutes spent at each tier, to set against the prior hours of section 0.4; and a count of unchecked rows. It is written in plain Python with nothing but the standard library, because a review that needs an entitlement ticket before it runs is a review that will not run on a Sunday.

Two design choices carry the weight. An exercise without a check is counted as unchecked, never as right, because the commonest way to inflate a hit rate is to grade the exercises you cannot grade in your own favour; until Appendix Z covers an exercise, it sits in the unchecked count, visibly. And a confidence above one is refused with an error that asks whether it is a percentage, because "70" for "70%" is the unit mistake every reader makes in the first week, and silently treating it as a probability of seventy would ruin the calibration table without crashing anything.

The tool is for the reader who has twenty or more checked exercises; below that, the standard errors are wide enough that the table mostly reports the noise (section 0.6). It also understates its own uncertainty in a way worth knowing. The standard error assumes the exercises are independent, and they are not: five exercises from one chapter share a reader's understanding of that chapter, the same way eleven bonds of one issuer share a waterfall, so the honest error bar is wider, by the clustering argument of §7-B.1. The edge case that bites is the week with no checked rows in a tier, which the listing reports by leaving that tier out of the table rather than printing a hit rate of zero over zero.

<!-- EXPLAINED -->
```python
import math
from collections import defaultdict

TIERS = ("read", "derive", "build")


def _validate(row):
    """Return the row's tier in lower case; refuse rows whose units are wrong."""
    tier = str(row["tier"]).lower()
    if tier not in TIERS:
        raise ValueError(f"tier {row['tier']!r} is not one of {TIERS}")
    conf = row["confidence"]
    if not 0.0 < conf <= 1.0:
        raise ValueError(f"confidence {conf} outside (0, 1]: is it a percentage?")
    if row["minutes"] < 0:
        raise ValueError("minutes must be non-negative")
    if row["correct"] not in (True, False, None):
        raise ValueError("correct must be True, False or None (no check yet)")
    return tier


def hit_rate(rows):
    """Hit rate and binomial standard error over checked rows; None if nothing is checked."""
    checked = [r for r in rows if r["correct"] is not None]
    n = len(checked)
    if n == 0:
        return None
    p = sum(1 for r in checked if r["correct"]) / n
    return {"n": n, "p": p, "se": math.sqrt(p * (1.0 - p) / n)}


def hand_history(rows):
    """Weekly review: hit rate by tier, calibration by stated confidence, minutes by tier."""
    by_tier, by_conf = defaultdict(list), defaultdict(list)
    minutes = defaultdict(float)
    unchecked = 0
    for r in rows:
        tier = _validate(r)
        minutes[tier] += r["minutes"]
        if r["correct"] is None:
            unchecked += 1
            continue
        by_tier[tier].append(r)
        by_conf[round(r["confidence"], 2)].append(r)
    return {
        "overall": hit_rate(rows),
        "by_tier": {t: hit_rate(by_tier[t]) for t in TIERS if by_tier[t]},
        "calibration": {c: hit_rate(rs)["p"] for c, rs in sorted(by_conf.items())},
        "minutes": dict(minutes),
        "unchecked": unchecked,
    }


def _rows(conf, tier, n_right, n_wrong, minutes):
    right = {"tier": tier, "confidence": conf, "correct": True, "minutes": minutes}
    wrong = {"tier": tier, "confidence": conf, "correct": False, "minutes": minutes}
    return [right] * n_right + [wrong] * n_wrong


# Theo's July (illustrative): overconfident on fresh derivations, underconfident on old arithmetic.
july = (_rows(0.9, "derive", 9, 3, 40.0)
        + _rows(0.5, "read", 7, 3, 15.0)
        + _rows(0.7, "build", 2, 1, 120.0)
        + [{"tier": "build", "confidence": 0.7, "correct": None, "minutes": 90.0}] * 2)
rep = hand_history(july)
assert rep["overall"]["n"] == 25 and abs(rep["overall"]["p"] - 0.72) < 1e-12
assert abs(rep["overall"]["se"] - 0.0898) < 1e-3          # sqrt(0.72 * 0.28 / 25)
assert rep["unchecked"] == 2                              # no check yet is not "right"
assert abs(rep["calibration"][0.9] - 0.75) < 1e-12        # said 90%, was right 75%
assert abs(rep["calibration"][0.5] - 0.70) < 1e-12        # said 50%, was right 70%
assert abs(rep["minutes"]["build"] - 540.0) < 1e-9
assert set(rep["by_tier"]) == {"read", "derive", "build"}

# A quarter of exercises at the same rate halves the standard error.
quarter = _rows(0.7, "derive", 72, 28, 30.0)
assert abs(hit_rate(quarter)["se"] - rep["overall"]["se"] / 2) < 1e-12

# The edge case: a confidence written as a percentage is refused, not silently used.
try:
    hand_history([{"tier": "read", "confidence": 70, "correct": True, "minutes": 5.0}])
    raise AssertionError("a percentage slipped through as a probability")
except ValueError:
    pass
print("hand_history: all checks pass")
```

