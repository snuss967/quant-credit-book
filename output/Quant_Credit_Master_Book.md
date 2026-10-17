---
title: 'Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk'
subtitle: 'Mathematical Foundations, Microstructure, LMT Game Theory, and Alpha Isolation (Edition 1, Build: 2026-10-17 23:23 UTC)'
toc: true
toc-depth: 3
---


# Preface: Read the Credit Agreement, Then Take the Derivative

At 2:58 p.m. on a Friday, three weeks into his new job, Theo Marsh gets a request for quote. A client wants a bid on \$15 million of a single-B bond issued by a company whose lender call is on Monday. Theo knows this company. In a previous life he read its credit agreement twice, in a conference room, over cold Thai food, and he can still tell you the Available Amount builder basket's starting dollar amount and which section of Article VII the sponsor would use to move the crown-jewel subsidiary out of the collateral package. He also knows that the person on the other end of this RFQ might know all of that too. Or might be a mutual fund rebalancing into month-end. He has three seconds to decide. His old job gave him three weeks.

"What's the pot," says Ines Okafor from the next seat, not looking up, "what are the odds, and who at this table knows more than you?"

Theo's first instinct is to ask what the credit agreement says. That instinct is correct. At this clock speed it is also useless, unless somebody has already turned the credit agreement into a number. This book is about how to be that somebody.

## Why this book exists

There are two tribes in credit, and they have been talking past each other for about twenty years.

The first tribe sits in restructuring and special situations groups, at PJT Partners' RSSG and the handful of places like it. Its unit of work is the bespoke legal bottleneck. It spends ninety hours building a 13-week cash flow model, reads 350-page credit agreements for sport, knows where the trapdoors are (Restricted Payments baskets, J.Crew-style drop-downs, Serta-style uptiers, EBITDA add-back caps), and understands Chapter 11 as a repeated game with exclusivity periods, DIP roll-ups, ad hoc groups, and 363 sales. Its edge is information that does not live in a time series. Its weakness is that it treats every credit as an artisanal snowflake and has never been forced to write its judgment down as a probability.

The second tribe sits on systematic market-making desks and in multi-strategy quant pods. Its unit of work is conditional expected value per unit of inventory variance per day. It prices adverse selection in three seconds, hedges in CDX and Treasury futures, measures its own mistakes with markouts, and runs factor models across two thousand issuers. Its edge is turning information into a repeatable, sized, hedged, measured bet. Its weakness is that it treats CUSIPs as exchangeable time series, and so it finds out about uptiers from the price.

The thesis of this book is that these are the same job performed at different clock speeds. Both tribes estimate a distribution of outcomes conditional on what they know, and then price it. The banker does it in weeks with a spreadsheet and a lawyer; the market maker does it in seconds with a model and a hedge. The bridge between them is codification: turning legal prose into state-space variables, process knowledge into transition matrices, and judgment into priors that a model can update. A desk that has done this can price the Friday RFQ correctly. A desk that has not is the counterparty the informed seller was looking for.

Two trends make this the right moment to build the bridge, and trends are a preoccupation of this book. The first is electronification. Between TRACE in 2002 and today's all-to-all platforms, portfolio trades, and ETF baskets, corporate credit went from a market where prices were discovered by phone and by grudge (Mags Dunleavy's phrase, and she was there) to one that produces data exhaust at a rate that makes systematic strategies possible. Chapter 2 dates and sources that story. The second trend is that AI coding agents have made the specifier the scarce resource. The person who can write a correct specification for a priming-risk model, with units, boundary conditions, and edge cases, now matters more than the person who can type it. The ex-RSSG banker who learns to specify is suddenly holding something a pure mathematician cannot buy: a decade of knowing which clause matters.

## Who this is for

In rough order of how hard we are thinking about you:

1. **The RSSG banker going systematic.** You know credit agreements cold and have never priced adverse selection in three seconds. The math is taught from first principles up through stochastic calculus and machine learning, and every model is tied back to a clause, a docket entry, or a trade you already understand.
2. **The quant moving into credit.** You know the math and have been quietly losing money on structural breaks. This book explains where the breaks come from, in enough legal detail that you can model them, and in no more.
3. **The AI-agent specifier.** You direct coding agents and need to know *why* an objective function is written the way it is, *where* the numerics blow up (ill-conditioned covariance matrices of stale bonds, barrier-crossing bias in Monte Carlo, hazard bootstraps that go negative), and *how* to write a specification tight enough that a model builds the right engine the first time.
4. **The desk head or PM** building a team out of ex-bankers and PhDs who, at present, cannot understand each other at lunch. Part VIII is yours.

It is not for anyone who wants sell-side fluff, a qualitative narrative without a probability attached, or a gut feeling that has not been written down. We despise those things, warmly.

## Three ways through the book

The book has eight parts and twenty-eight chapters in its first edition, plus three appendices, and it will grow. You do not have to read it in order. Three reading paths, one per tribe:

**Path 1: the RSSG banker.** Read Part I straight through; Chapter 3 is written for you specifically, and the RSSG Edge Ledger in it is the inventory of what you are bringing to the new desk. Then jump to Part IV (Chapters 13–17), which is your home turf with the numbers attached: liability management transactions as game theory, the default cycle as a regime shift, change-of-control puts as options, post-reorg equity as forced-seller flow, and private credit as the thing eating your old job. Only then go back to Part II (Chapters 5–7). You will be tempted to skip Chapter 6 because someone once told you that Merton models do not work in distressed credit. That person was half right, and the half they were wrong about is where the money is. Finish with Parts III, V, VI, VII, and VIII in order. Keep Appendix A open the whole time.

**Path 2: the quant.** Start with Chapter 3 to see what the other tribe knows, then read Chapter 13 and Chapter 25 back to back: the first is what an uptier does to your return distribution, the second is how to parse the document that permitted it. Then take Part V and Part VI, which are your home turf, and notice where credit microstructure departs from what Avellaneda–Stoikov assumed (jump-to-default, RFQs instead of limit order books, bonds that have not traded in nine days). Part II will mostly be review, but Chapter 5's treatment of recovery distributions and Chapter 7's issuer-grouped cross-validation contain the traps that have been quietly eating your Sharpe ratio. Read Part IV last, slowly. Then Part VIII.

**Path 3: the AI-agent specifier.** Read this preface, then Appendix A, then go through every `### Specification for AI Implementation` block in the book in order, starting with Chapters 5–8 (distributions, structural models, labeling, decomposition), then Chapter 13 (the Priming Risk Score), Chapters 18–19 (quoting and basket pricing), and Chapters 25–27 (document parsing, agent workflows, and system architecture). Chapter 26 is the operating manual for directing coding agents and should be read before you direct one. Then go back and read the prose: a spec you do not understand is a spec you cannot debug.

There is also a fourth, unofficial path for the reader who is here for the trends: Chapters 2, 4, 10, 14, 17, 21, 22, and 26, each marked TREND in the table of contents, followed by Appendix C, the Trend Tracker.

## The cast

Twenty-eight chapters written by a committee tend to read like twenty-eight chapters written by a committee. So we use a small recurring cast. They are fictional. Every line of dialogue in the book belongs to them. Real firms, real cases, and real people appear only with verifiable facts attached and never with invented quotes.

**Theo Marsh** (he/him) is you, or the version of you who is three weeks into a systematic credit desk after years at PJT RSSG. He carries his old 13-week cash flow model on a USB stick "for emotional support." He asks, "But what does the credit agreement say?" He is usually right, which is annoying for everyone else and the reason he was hired.

**Ines Okafor** (she/her) runs credit market making and used to play poker professionally, which she regards as the same job with worse coffee. She frames every problem as a hand: what's the pot, what are the odds, and who at this table knows more than you? She calls markouts "the hand history" and reviews them the way other people review their text messages at 1 a.m.

**Dr. Kasimir "Kaz" Lind** (they/them) holds a PhD in stochastic analysis and builds the desk's models. Kaz is brilliant and has never read a credit agreement. They once asked whether "sacred rights" required a priest. Kaz's opening move in any derivation is "let's just assume Gaussian," and Kaz's second move is regret. You will learn a great deal from watching Kaz be wrong in precise ways.

**Marguerite "Mags" Dunleavy** (she/her) has run distressed money since the 1990s and remembers pricing bonds by phone and by grudge. Her creed: "Price is what you pay. Recovery is what you get, eventually, after the lawyers." She is deeply suspicious of anything called "adjusted," she greets every new technology with a story about how it used to be worse, and she is grudgingly, eventually, impressed.

**ROBO** (it/its) is the AI coding agent Theo specifies work to. ROBO implements exactly what it was asked, which is the problem. Told to "minimize drawdown," it holds cash forever. It never complains and never guesses, and it is therefore the most honest reviewer of a specification you will ever meet. Every "Spec You Hand the Robot" box in this book is an attempt to say something to ROBO that cannot be misread.

**The Ad Hoc Group** is a Greek chorus of lenders, always "represented by counsel." It speaks in unison, mostly in Rule 2019 statements. It forms, it splits, it signs cooperation agreements, and the book keeps a running count of those, because someone should.

A few other things recur on purpose. Theo's 13-week model refuses to die: it comes back as a survival curve in Part II, as a state-space feature in Chapters 3 and 25, as the liquidity-runway variable inside the Priming Risk Score in Chapter 13, and finally as the PM dashboard in Chapter 28. "Open market purchase" is the most expensive three words in finance and will keep showing up until the courts stop making it so. And the desk motto is "IDO or it didn't happen": until you have stripped carry, rates, and factor beta out of a return, you have not found alpha, you have found a benchmark with a hat on.

## How a chapter is built

Every chapter (and most sections) carries six elements, in a recognizable order, so that you always know where you are:

1. **Intuitive desk framing.** How a market maker or an RSSG partner sees the problem in plain, ruthless trading terms, usually with the cast in the room.
2. **Rigorous mathematical derivation.** Full equations, step by step, every Greek letter defined, boundary conditions stated, using the single notation table in Appendix A. The joke, if there is one, comes after the load-bearing step, never inside it.
3. **A specification for AI implementation.** A block headed `### Specification for AI Implementation` with data schemas, tensor shapes, edge cases, numerical-stability guards, and a reference implementation in Python (written to run on numpy, scipy, and pandas as given) or a sketch in C++ or Rust where latency matters. It often opens with what ROBO built from the vague version of the request, followed by the precise version.
4. **Source extraction.** Short exact quotations from the fourteen books and papers on our shelf, each cited to a page and followed by a longer annotation in our own words about why it matters on a 2026 desk and where the modern desk departs from it.
5. **A deep-dive case study.** Serta, J.Crew, Incora, Carvana, SVB, Hertz, Windstream, March 2020, May 2005: tranches, price paths, dollar values (sourced or marked approximate), and what a systematic desk would have flagged and traded.
6. **A Deep-Dive Resource Graph.** Podcasts, practitioner writing, academic papers, and data and code repositories, grouped, so you can keep going after we stop.

Between those elements you will find a small set of boxes, each with a fixed label: **Desk Myth vs. Desk Reality**, **Poker Table** (game-theory intuition, usually Ines), **Docket Diary** (court process with dates, often with commentary from the Ad Hoc Group), **Ways This Blows Up** (numerical instability, model failure, operational risk), and **Trend Watch**.

Trend Watch boxes deserve a paragraph of their own, because "trend" means two things in this book and we care about both. The first meaning is the structural trends reshaping credit markets: electronification, portfolio trading, ETF-led liquidity, the LMT era, private credit, the regulatory agenda. Every chapter includes at least one Trend Watch box with dated, sourced figures showing how its topic changed over 2018–2026, and Appendix C stitches them into a single timeline. The second meaning is trend as a strategy: time-series momentum in credit indices and excess returns, cross-asset lead–lag, trend combined with carry, and how it behaved in 2008, 2020, and 2022. That gets a whole chapter (Chapter 10) and a recurring role in Parts III and VIII. If a chapter does not tell you what changed and when, we consider it unfinished.

Each chapter opens with a cold-open desk scene and closes with a Desk Debrief (takeaways sharp enough to tape to a monitor), a compact Spec You Hand the Robot, and a few exercises, some of them funny, all of them real.

## A note on how this book is made, and why you should check the build stamp

Honesty requires a disclosure. This book is not written by a person at a desk. It is grown by an autonomous loop of AI agents: a showrunner that keeps the voice and the notation consistent, writer agents assigned to chapters, and advisor agents running on Anthropic's Fable model that research each target (the shelf, the web, the dockets, the papers, the trend data) and hand the writer a brief before a word is written. The loop reads its own state, picks the next most valuable thing to write, writes it, rebuilds the book, updates its notes to itself, and goes again. It never stops on its own. Somebody has to tell it to.

The book therefore ships in **editions**. Edition 1 is the first complete draft of every chapter in the table of contents. Each later edition is a research pass that deepens chapters, adds the chapters and sections the latest research says are missing, and refreshes the Trend Tracker. Because the loop rebuilds the whole text every few hours, the title page carries a build stamp in the subtitle, a date and time in UTC. Please look at it. A trend figure dated 2025 in a build from 2027 is a figure nobody has refreshed yet, and a court ruling described as "pending" may no longer be. Where the agents were unsure they have said so in the text, usually with the word *approximate*, occasionally with a parenthetical that reads like someone leaving a note for their future self, because that is what it is.

Two consequences follow. The book will sometimes repeat itself across chapters, because different agents wrote from the same brief; think of it as spaced repetition until we trim it. And its priorities are, in order, research, net-new writing, growing the table of contents, polish, and only then checking that every code example runs, so a bug can survive an edition. The book gets deeper every cycle rather than prettier, which we think is the right trade for a market that changes this fast. If you find an error, you are almost certainly right; the next edition reads the repository's state notes and continuation prompt.

## The integrity pledge

Because an autonomous loop can generate plausible-looking nonsense at scale, we hold it to rules a human author might get away with bending:

- **Sourced or labeled.** Every historical price, spread, recovery, volume, and dollar amount is either cited to a source or explicitly marked *illustrative* or *approximate*. If a number has neither, it is a bug; treat it as illustrative and tell us.
- **No invented identifiers.** No fabricated CUSIPs, ISINs, SSRN numbers, DOIs, podcast episode numbers, or URLs. Tranches are identified descriptively ("Serta Simmons 2016 First Lien Term Loan due 2023"). A link appears only if it was verified when that passage was written or is a stable canonical root; otherwise you get title, author, and year, and a search engine.
- **No fake quotes.** Real people and firms appear with verifiable facts only. All dialogue belongs to the fictional cast.
- **Code written to run.** Every Python reference implementation is written to execute as given on numpy, scipy, and pandas, with seeded randomness and built-in sanity checks (Monte Carlo against closed form, a waterfall that conserves value, a hazard curve that stays non-negative). Execution checks are a low-priority cleanup pass; the specification around the code is written so that you, or ROBO, can find what survived.
- **Every joke rides on a correct idea.** If a line is funny but wrong, the line goes. If a derivation is correct but dull, we try harder.

Theo is still staring at the RFQ. The clock in the corner of the screen says 2.1 seconds. Turn the page.


---


# Part I: The Cognitive Bridge & The State of Quant Credit

*Chapters 1–4*

Every immigrant story starts at customs. Theo Marsh arrives at the systematic credit desk with one carry-on: a USB stick holding his 13-week cash flow model. "Anything to declare?" "A liquidity forecast." "Is it for personal use?" "Emotional support." He is waved through, and the first thing he notices is that everyone here speaks a language that sounds like his own but has a different grammar. They say "spread" and mean a random variable. They say "flow" and mean a probability of being picked off. They say "the credit agreement" rarely, and when they do, they say it the way you would mention a relative who lives abroad.

Part I is the arrival kit: a phrasebook, a short history of how the country got electricity, a set of language lessons, and a census.

**Chapter 1, The Anthology of the Desk & the Modern Quant Credit Landscape,** is the phrasebook and the map. It compiles the load-bearing ideas from the fourteen books and papers on our shelf (DTS and spread-volatility scaling, distance-to-default, credit factors, intensity models, the distressed process, portfolio construction) with short quotations and long annotations, and then draws the ecosystem as a flow graph of who is a forced seller to whom: CLOs with CCC buckets, insurers with ratings constraints, ETFs with redemptions, mutual funds with outflows, and the market makers, factor pods, and capital-structure arbitrageurs who harvest each flow. Alpha in credit is mostly standing where someone else has to sell.

**Chapter 2, The Revolutions in Credit Trading (TREND),** is the history of the electrification. From TRACE in 2002 through all-to-all trading, RFQ automation, portfolio trading, and ETF-driven liquidity to the non-bank liquidity providers who now quote next to the banks, it dates and sources the market-structure story for 2018–2026, following Man Group's 2023 framework, and explains why a market that produces data exhaust is a market where systematic strategies can finally live.

**Chapter 3, Cognitive Rewiring, From PJT RSSG to Systematic Desk Head,** is the language course, and it is the chapter the title of this book promises. It takes the questions a restructuring banker asks (will this company survive the quarter? who controls the vote? where is the fulcrum?) and rewrites each one as a distribution. It adapts Glosten–Milgrom to the RFQ, teaches markouts as the empirical test of whether you were picked off, builds the RSSG Edge Ledger (every skill you brought with you, mapped to a codable feature, a data source, and a decay horizon), and shows what order flow looks like in the weeks before a liability management transaction, when some counterparties know and most do not.

**Chapter 4, Inside the Systematic Credit Industry (TREND + FRAMEWORKS),** is the census. It lays the five industry frameworks on our shelf (Man Group's 2022 and 2023 papers, Blackstone's systematic platform, BlackRock's defensive high yield, Nuveen's multi-asset framework) side by side with AQR, Robeco, and the rest, along the axes of alpha families, data stack, portfolio construction, execution, capacity, and risk. The comparative map it produces is the exploratory space for everything that follows, and the AUM and launch-date trends it sources show that systematic credit has stopped being a white paper and become an industry.

The trend that defines this part is electronification, and the reason it matters is epistemological rather than technological. A phone market produces anecdotes; an electronic market produces a dataset. Once the dataset exists, the restructuring banker's knowledge stops being an anecdote too. It becomes a feature, with a timestamp, that can be tested against the hand history. That is the whole bridge, and Part I is where we pour the footings.

A warning that applies to the whole book and especially here: the two tribes fail in mirror-image ways. The quant treats bonds as exchangeable time series and is surprised by the uptier. The banker treats every credit as unique and cannot size, hedge, or measure. Theo's job, and yours, is to be surprised by neither. Ines puts it more simply. "You already know who at the table knows more than you. You just never wrote it down."


---


# Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape

## 1.1 The Epistemological Clash: PJT RSSG vs. The Automated Market Maker

Walk onto the restructuring floor at PJT Partners (RSSG) in Midtown Manhattan, and the unit of account is the **bespoke legal bottleneck**. An analyst spends 90 hours modeling a 13-week cash flow forecast, reading a 350-page Senior Secured Credit Agreement from 2019, calculating exact dollar capacity inside the *Available Amount* builder basket under Section 7.06, and determining whether an ad-hoc group holding $50.1\%$ of the Term Loan B can strip collateral coverage via an amendment and drop intellectual property into an unrestricted subsidiary. Time moves in weeks; alpha is extracted by structuring a private non-pro-rata transaction where your client captures a $20\text{-point}$ priming premium over left-behind minority lenders.

Now walk onto the quantitative credit and cross-asset market-making floor at Susquehanna International Group (SIG) in Bala Cynwyd, or a systematic credit pod at Citadel or DE Shaw. The unit of account is **conditional expected value per unit of inventory variance per day**. Nobody is reading a single indenture cover-to-cover during market hours. Instead, an automated pricing engine ingests real-time FINRA TRACE prints, CME Treasury futures ticks, OPRA single-stock option implied volatility surfaces, and HYG/LQD ETF creation-redemption baskets. When a client sends an all-to-all Request for Quote (RFQ) on MarketAxess asking for a bid on $\$15\text{ million}$ notional of a stressed $B3/B-$ high-yield bond, the desk has **less than 3 seconds** to solve an adverse selection problem:

$$\text{Quote Bid } B^* = \mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \text{Order Flow } \mathcal{O}_t] - \frac{1}{2}\gamma \sigma^2_{\text{IDO}} (2q + \Delta q) - \Lambda_{\text{tox}}(\mathcal{O}_t)$$

Where:
- $\mathbb{E}[V_{t+\Delta t} \mid \mathcal{F}_t, \mathcal{O}_t]$ is the posterior fair value conditioned on public filtration $\mathcal{F}_t$ and the event that a counterparty is actively trying to sell size $\Delta q$.
- $\gamma$ is the desk's risk-aversion parameter, $\sigma^2_{\text{IDO}}$ is the unhedged idiosyncratic variance of the bond after stripping Treasury duration and CDX beta, and $q$ is current desk inventory.
- $\Lambda_{\text{tox}}(\mathcal{O}_t)$ is the **Adverse Selection Penalty**: the probability that the seller has just left a lender call or analyzed a covenant trapdoor and knows an LMT or earnings miss is imminent.

### Why the Hybrid PJT RSSG + Quant Architect Owns the Future
Pure quantitative researchers trained in equity stat-arb fail in distressed and high-yield credit because they treat cusips as exchangeable time series. When a company executes a Serta-style uptier or a J.Crew trapdoor drop-down, historical price correlations break down instantaneously—a structural discontinuity occurs that a standard Kalman filter or GARCH model cannot anticipate.

Conversely, traditional fundamental restructuring analysts fail on a systematic desk because they treat every credit as an artisanal snowflake, refusing to codify their intuition into continuous probability distributions. **The ultimate alpha in modern credit belongs to the architect who can translate PJT RSSG legal and structural mechanics into state-space features that feed an automated pricing and risk engine.**

---

## 1.2 Evaluating the Market Set in Quantitative Credit

To extract maximum alpha and isolate pure Idiosyncratic Return (**IDO**), a Desk Head or Portfolio Manager must first map the structural players in the ecosystem and understand their mechanical constraints:

| Strategy / Desk Archetype | Representative Firms | Holding Horizon | Primary Edge | Structural Vulnerability (How You Arb Them) |
| :--- | :--- | :--- | :--- | :--- |
| **Automated OTC Market Makers & PT Desks** | SIG, Jane Street, Citadel Securities, Flow Traders | Milliseconds to 10 Days | ETF Creation/Redemption loops, Portfolio Trading (PT) pricing speed, cross-asset latency | Exposed to **toxic fundamental flow** on bespoke LMTs, covenant priming, and bankruptcy docket surprises |
| **Systematic Factor Credit Pods** | AQR, Man Numeric, BlackRock Systematic, Two Sigma | 1 to 6 Months | Cross-sectional factor harvesting (Value, Equity-to-Credit Momentum, Carry, Quality) across 2,000+ issuers | Slow to react to discrete structural breaks (M&A CoC waivers, drop-down rumors); mechanical rebalancing creates predictable flow |
| **Capital Structure & Volatility Arbitrage** | DE Shaw, Saba Capital, Elliott (Trading), Millennium pods | 5 Days to 6 Months | Merton-model dislocations, Equity Put Skew vs. High-Yield Spreads, CDS-to-Bond Basis, Orphan CDS | Vulnerable to squeeze dynamics in repo/borrow markets and basis blowouts during liquidity crunches |
| **CLO Vehicles (Par-Constrained Institutional Buyers)** | Blackstone, Carlyle, Palmer Square, Ares | Buy-and-Hold (Reinvestment Period) | Structural leverage via AAA-to-Equity tranche arbitrage | **Forced mechanical sellers** when CCC buckets exceed $7.5\%$ or upon default; cannot easily fund new-money post-reorg equity rights offerings |

> **[AGENT EXPANSION DIRECTIVE FOR NEXT ITERATION]:** Pull cited excerpts from `/state/pdf_pages/Ben_Dor_Quantitative_Credit_Portfolio_Management/` on DTS (Duration Times Spread) and empirical duration, `/state/pdf_pages/Bohn_Stein_Active_Credit_Portfolio_Management/` on structural default models, and `/state/pdf_pages/Moyer_Distressed_Debt_Analysis/` on the distressed investing process. Expand Section 1.3 into a 6,000-word compilation of foundational texts with full mathematical commentary.


---


# Part II: Mathematical & Probabilistic Foundations for AI Specifiers

*Chapters 5–7*

Here is the thing nobody tells you about becoming an architect: you stop pouring concrete. ROBO pours the concrete now. ROBO pours it fast, cleanly, and exactly where you pointed, including the time Theo pointed at the wrong wall. Theo told ROBO to "make the model less volatile." ROBO set $\sigma_V$ to zero. The model-implied spread on every bond in the book went to zero, the desk was briefly the safest financial institution on earth, and Kaz spent the afternoon explaining to a very patient machine that volatility was not a bug.

Part II is the building code. It teaches you which walls are load-bearing in credit mathematics, so that when you direct a coding agent you can tell it what to knock out and what to leave alone. You will not be asked to pour the concrete yourself. You will be asked to know, before the robot starts, where the roof will fall if it gets the sign of $d_2$ wrong.

**Chapter 5, Probability Distributions in Distressed & High-Yield Credit,** is about the shape of outcomes, which is the first thing a specifier must write down and the first thing most specs get wrong. A bond's return is a mixture: with probability $S(t)$ it survives and the spread wiggles, and with probability $1 - S(t)$ it jumps to recovery. The upside is capped by the call price; the downside has a floor at recovery and a very long corridor in between. The chapter builds that mixture with closed-form moments, separates the Lévy and jump-diffusion machinery that earns its place on a desk from the machinery that is decoration, models recovery as a Beta distribution conditioned on collateral and seniority (because "40 percent" is a CDS convention, not a fact), and fits tails with extreme-value tools. It also keeps price, spread, and return distributions apart, and physical and risk-neutral recovery apart, which sounds pedantic until you have paid for mixing them.

**Chapter 6, Stochastic Calculus, Intensity Models & Structural Frameworks,** is where Theo's 13-week model is reborn as a survival curve. It starts with Itô's lemma as the tax code of stochastic calculus, the $\tfrac{1}{2}\sigma^2$ correction that the IRS of randomness collects whether you like it or not, and builds up through Merton (equity is a call on the firm; debt is a riskless bond short a put), KMV distance-to-default, Black–Cox first passage with covenant barriers, Jarrow–Turnbull and Duffie–Singleton reduced-form models, CIR intensities in closed form, and bootstrapping a hazard curve from CDS quotes. The credit triangle $s \approx \lambda(1-R)$ shows up here and never leaves. So do the traps: equity vol used as asset vol, $\mathbb{P}$ and $\mathbb{Q}$ in the same equation, and the Monte Carlo barrier bias that makes a naive first-passage simulation underprice default.

**Chapter 7, Machine Learning on Small-Sample, Non-Stationary Credit Data,** is the honest chapter about why corporate credit is the worst dataset in finance: stale TRACE marks, survivorship through calls and exchanges, forty-seven bonds from one issuer that are one data point wearing forty-seven hats, regimes that change under you, and fundamentals that arrive with a lag. It adapts the small-sample toolkit (fractional differentiation, triple-barrier labels in DTS-scaled spread space, meta-labeling, purged and issuer-grouped cross-validation, the deflated Sharpe ratio) to credit, and surveys the 2019–2026 research frontier on machine learning for bond returns, including the replication fights.

The trend that defines this part runs in two directions at once. In research, the question of whether machine learning finds anything in bond returns beyond what a handful of characteristics explain is live and contested, and Chapter 7 keeps score. On the desk, the arrival of capable coding agents has moved the bottleneck from implementation to specification, which is why every section in this part ends with a block written for a machine. Kaz, who has spent a career writing the implementation, finds this disorienting. "Let's just assume Gaussian," they say, and Theo, who has now read Chapter 5, says: "Which part? The spread, the recovery, or the day the sponsor moves the IP?"


---


# Part III: Isolating Idiosyncratic Alpha (IDO), Factors & Trend

*Chapters 8–12*

Picture a mixing desk. A bond's return comes in on a dozen tracks at once: a rates track, a carry track, a credit-beta track, a few factor tracks (value, momentum, quality, low-risk, size), a liquidity track, and somewhere underneath, if you are lucky and the issuer is interesting, a track that is only this bond. Everyone who has ever pitched a credit has pointed at the mix and said "listen to that." Part III teaches you to press mute on every track but one and find out what is actually there.

The first time Theo did it, the solo channel was silent. The bond he loved, the one whose capital structure he could draw from memory, had returned 9 percent over the year, and every basis point of it was duration and carry. The desk motto was taped to his monitor by the following morning: *IDO or it didn't happen.*

**Chapter 8, Stripping Beta to Isolate Pure IDO,** is the mute button. It decomposes a bond's return with the signs right ($-D\,\Delta y$, not $+$), separates OAS carry from yield carry, and explains the most useful empirical fact in high yield: measured duration is much shorter than analytical duration, and for CCC bonds it turns negative, because spreads and rates move against each other. It covers DTS, the betas you compute when prices are stale (Dimson and Scholes–Williams lag sums), and the hedge matrix across CDX, Treasury futures, HYG and JNK, and equity puts, which is a constrained least-squares problem so ill-conditioned that ridge regularization is a safety feature rather than a style choice. The 2022 rates sell-off is the case study, because it was the year everyone's duration hedge was wrong in the same direction.

**Chapter 9, Factor Investing in Corporate Credit,** is the factor tracks: value, momentum, quality, carry, low-risk, size and liquidity, and the "informed investor" factor from Man Group's 2022 framework. The chapter is about construction more than discovery, because in credit the construction is the alpha: neutralization within rating, sector, and maturity buckets, DTS-neutral versus market-value-neutral portfolios, long-only constraints, liquidity cost scores that eat the paper return, crowding, and the 2019–2026 debate over whether published credit factors replicate.

**Chapter 10, Trend-Following & Time-Series Momentum in Credit (TREND),** is the track that is itself a trend, and the one readers who came for trends should turn to first. It applies the time-series-momentum framework to CDX, iTraxx, and credit excess returns, studies the equity-to-credit lead–lag that makes cross-asset trend work, combines trend with carry, scales by volatility, and looks hard at the crisis years, 2008, 2020, and 2022, where trend's drawdown behavior is the entire reason anyone allocates to it. It also asks what trend does in a market where returns jump, which is a polite way of describing the LMT era.

**Chapter 11, Defensive Systematic High Yield,** follows BlackRock's framework: default avoidance, downside mitigation, the CCC problem (where most of the index's defaults and most of its negative convexity live), quality and low-risk tilts, the arithmetic of upside and downside capture, and the capacity question that decides whether any of this scales.

**Chapter 12, Multi-Asset Credit Allocation,** zooms out to Nuveen's framework for rotating across high yield, loans, emerging-market debt, preferreds, securitized credit, and private credit: regimes, valuation per unit of default loss and per unit of volatility, risk budgets, and liquidity tiers, so that the allocation can be unwound in the order the market will let you.

The trend that defines this part is that systematic credit has grown a track record. Factor and trend strategies in credit used to be backtests in white papers; they now have live performance through two full drawdowns, and the sourced figures in these chapters let you judge them. Mags remains unconvinced. "Back in my day we had one factor. It was called 'I know the CFO.'" Then she asks to see the momentum chart again.


---


# Part IV: Quantifying Special Situations & PJT RSSG Mechanics

*Chapters 13–17*

Imagine a building whose floors can be reordered by a vote of 50.1 percent of the residents while the rest are asleep. Imagine the furniture can be carried out through a door that was in the blueprint all along, in a clause nobody read because it was called "Permitted Investments." Imagine the same sofa can be pledged to two different lenders at once, and that this is, after a fashion, legal. Welcome to the capital structure of a sponsor-owned leveraged company in the 2020s. Theo grew up in this building. Kaz, on hearing the phrase "fulcrum security," asked whether it was a physics thing. "It's where the value breaks," said Mags, "and where the lawyers start."

Part IV is Theo's home turf, which is exactly why it is the most dangerous part of the book for him. He knows these mechanics the way a native speaker knows grammar: fluently, and without being able to state the rules. The job here is to state them, as probabilities, transition matrices, payoff tables, and features a model can read.

**Chapter 13, Codifying Liability Management Transactions (LMTs),** builds the Priming Risk Score, $\text{PRS} \in [0,1]$, from document features and Bayesian priors: basket capacity, blocker language, sponsor history, maturity walls, and the liquidity-runway variable that is Theo's 13-week model in a new coat. It treats non-pro-rata uptiers (Serta, Boardriders, Mitel, Incora) and drop-downs (J.Crew, PetSmart and Chewy, Envision) as an n-player threshold game in which the sponsor auctions a priming premium between lender groups, and builds a multi-obligor waterfall engine for double-dips and pari-plus structures that, unlike several real ones, conserves value. "Open market purchase" enters the book here as the most expensive three words in finance, and the cooperation-agreement counter starts at zero.

**Chapter 14, The Default & Recovery Cycle in the LMT Era (TREND),** is where the mechanics become statistics. Distressed exchanges now account for a large and sourced share of defaults, re-default rates after exchanges are high, recoveries have compressed, cooperation agreements have proliferated, and the 2024–2026 court rulings have redrawn what a majority may do to a minority. The chapter models each of these as a regime shift in the default and recovery distributions of Chapter 5, so that a desk's PD and LGD inputs stop assuming it is 2006.

**Chapter 15, Event-Driven M&A, Regulatory Spreads & Change-of-Control,** prices the 101 change-of-control put as an option that pays only if the deal closes *and* the trigger is met, treats portability as a short option written by bondholders, handles special mandatory redemptions on escrowed acquisition debt, and models antitrust timelines as survival analysis, with Kaplan–Meier and Cox proportional hazards doing the work that "the lawyers think second half" used to do.

**Chapter 16, Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims,** follows the value out the far side of the process: the forced CLO selling and orphan-equity dynamics that make post-reorg stocks systematically mispriced, rights offerings as options plus a backstop premium, the difference between a 503(b)(9) claim and a general unsecured one, and Hertz in 2020 as the case where the equity was not, in fact, worthless.

**Chapter 17, Private Credit & the Public–Private Convergence (TREND),** closes the part with the trend that is eating the old job: the growth of private credit, BDC marks against public comparables, private-to-public refinancings, systematic approaches to a market with no TRACE, and what a public-markets quant desk can actually arbitrage.

The trend that defines this part is the replacement of the bankruptcy by the exchange. The modal default is no longer a petition in Delaware or Houston; it is a transaction, negotiated among a subset of lenders, that leaves the rest holding a different instrument than they bought. For the quant, this means the return distribution has a new mass point and the historical recovery data has a new bias. For the banker, it means the thing you did for a living is now a feature. The Ad Hoc Group, represented by counsel, declines to comment, but reserves all rights.


---


# Part V: Market Microstructure, Portfolio Trading, ETFs & Loans

*Chapters 18–22*

Equities are a supermarket. Every item has a price tag, there is one checkout, and the queue is visible to everyone. Corporate credit is a bazaar. There are no price tags; every price is a negotiation; the merchant studies your face while you study the rug; and if you ask three stalls for a quote on the same rug, all three now know something about you. Electronification is the slow installation of barcode scanners, one stall at a time. The ETF is a supermarket built next to the bazaar that sells sealed boxes of bazaar goods at a posted price, and the people who open the boxes for a living are called authorized participants. The loan market is the stall at the back where you agree a price today and the rug arrives in three weeks, maybe.

Ines runs this part of the book, because it is a poker room with worse lighting. "In the bazaar the merchant reads your face," she says. "On the RFQ, the merchant reads your hand history. Be the merchant."

**Chapter 18, OTC Credit Microstructure & the Market Maker's Equations,** is the core derivation of the book's market-making half. It walks through Harris's taxonomy of traders, the Roll, Glosten–Milgrom, and Kyle models of the spread, and then the Avellaneda–Stoikov and Guéant–Lehalle–Fernandez-Tapia machinery in full (the HJB equation, the exponential-utility ansatz, the reservation price $r^{\text{res}}$, the optimal spread) before adapting it to the thing credit actually is: RFQs rather than limit order books, win probabilities that depend on the distance to a composite price, inventory that cannot be unwound at will, and a jump-to-default term that adds $q\lambda J$ to the reservation price. It decodes TRACE, measures RFQ hit rates, and treats BWIC leakage as the information problem it is.

**Chapter 19, Portfolio Trading & Basket Pricing Engines,** prices a 150-line portfolio trade in ninety seconds: the sum of fair values, less liquidation costs, less a risk charge on the residual covariance over the unwind horizon, which requires a covariance matrix for bonds that have not traded this month, a factor model and shrinkage to make it invertible, an eviction rule for the lines you refuse, a stress model for liquidity that becomes correlated exactly when you need it not to, and a healthy fear of the mystery box, the basket assembled by someone who knows which lines are the problem.

**Chapter 20, Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN),** explains how the sealed boxes get made and unmade: authorized participants, custom baskets, bid-side NAV, the arbitrage bands set by creation and redemption costs, ETF price as the market's real-time estimate when the bonds themselves are not trading, and March 2020, when the boxes traded at discounts that looked like a malfunction and were in fact the only honest price on the screen.

**Chapter 21, Leveraged Loans, CLOs & Loan-Market Microstructure (TREND),** is the back stall: settlement that takes weeks, CLO constraints (CCC buckets, overcollateralization and interest-coverage tests) that turn vehicles into forced sellers on a schedule, repricing waves, the halting arrival of loan e-trading, and the loan and CLO ETFs that now sit on top of a market never designed for daily liquidity.

**Chapter 22, Market-Structure Regulation & the Forces Reshaping Liquidity (TREND),** takes each rule that changed the plumbing (TRACE reporting-time changes, T+1 settlement, the Treasury clearing mandate, Basel III endgame and dealer capital, CDS reporting and clearing) and works through what it did to the economics of a desk.

The trend that defines this part is that the basket became the unit of liquidity. Single bonds still trade one at a time, by negotiation, but an increasing share of risk moves in portfolios and ETF creation units, priced by engines in seconds, and the data exhaust from those trades is the raw material for everything in Part III. Mags, asked about this, says that back in her day you could get a two-way market on a single bond by calling someone who owed you a favor, and that it was worse, and that she misses it.


---


# Part VI: Capital Structure Arbitrage & Volatility Surfaces

*Chapters 23–24*

One patient, four doctors. The equity market, the equity options market, the CDS market, and the bond market each examine the same firm and each issue a diagnosis: a stock price, an implied volatility surface, a CDS spread, a bond price. Merton's insight was that all four are looking at the same thing, the firm's asset value $V_t$ and its volatility $\sigma_V$, and that their diagnoses must therefore be consistent. Capital structure arbitrage is the bet that when the doctors disagree, they will eventually agree, and that you know which one is right. Its risk is that you are wrong about which doctor, or that the patient contracts a disease none of the doctors had a word for. In May 2005 the patient was General Motors, the credit market said "downgrade," the equity market said "takeover bid," and a large number of funds that were long the bonds and short the stock discovered that the doctors can disagree for a very long time.

Kaz is at home in this part, because it is almost entirely math, and uneasy in it, because the math keeps bumping into documents. "A springing lien," they ask, "is a lien that... springs?" Mags nods. "Usually at you."

**Chapter 23, Cross-Asset Convexity & the Volatility Surface,** links the surfaces. It derives $\sigma_E E = \sigma_V V\, N(d_1)$ and uses it to turn equity volatility into a credit spread, covers the CreditGrades model that commercialized the idea, and follows Carr and Wu in reading deep out-of-the-money puts as credit instruments and the skew as a market price for jump-to-default. It expresses the Greeks in spread terms so a bond trader can use them, treats convertible and capital-structure arbitrage as trades on the same surface, and takes two autopsies: May 2005, when the cross-asset hedge failed in both legs at once, and Silicon Valley Bank in March 2023, when the equity, options, and credit markets priced the same balance sheet at three different speeds.

**Chapter 24, Bond-to-CDS Basis & Deliverable Obligation Mechanics,** is the CDS doctor's chart, read closely. It prices the premium and protection legs, defines the risky annuity, handles standard coupons and upfronts, and then works through the several things people mean by "basis" (against Z-spread, against asset swap, against par-equivalent CDS spread), the funding and repo terms that explain most of a negative basis, the cheapest-to-deliver option, and the two-stage auction. The last third is where the chart gets interesting: orphaned CDS when the debt moves and the reference entity does not, the manufactured credit events at Hovnanian and the Windstream fight, the 2019 ISDA narrowly-tailored-credit-event supplement that followed, and what liability management transactions have done to the definition of a credit event.

The trend that defines this part is a migration. Single-name CDS liquidity has thinned and concentrated, index CDS and equity options have become the practical instruments for expressing a view on credit volatility, and the legal boundary of what counts as a credit event has been tested by people who read the definitions more carefully than the drafters did. The quant consequence is that the "arbitrage" in capital structure arbitrage is increasingly a bet on the relative speed of four markets rather than on a true mispricing, and the desk that measures those speeds, with the lead–lag tools from Chapter 10 and the hedge matrices from Chapter 8, is the desk that gets paid. Ines's summary is shorter. "Four players, one deck, and one of them has read the rules. Figure out which."


---


# Part VII: Alternative Data, NLP, AI & Systems

*Chapters 25–27*

A credit agreement is a program. It has variables ("Consolidated EBITDA"), functions ("Permitted Investments"), conditionals ("so long as no Event of Default shall have occurred and be continuing"), recursion (Consolidated EBITDA is defined in terms of Consolidated Net Income, which excludes items defined by reference to Consolidated EBITDA), and a type system that two law firms will argue about for eighteen months. What it does not have is a compiler. For forty years the runtime was a lawyer. Part VII builds the compiler, then builds the machine it runs on.

Theo's first specification for ROBO in this part read: "compute the capacity of the general Restricted Payments basket." ROBO returned "\$50 million." The basket was "the greater of \$50 million and 100 percent of Consolidated EBITDA," and Consolidated EBITDA that quarter was negative, so ROBO was, infuriatingly, correct. Theo rewrote the spec. It now has units, a definition graph, a fiscal-quarter lookup, and a test case named after the quarter in question.

**Chapter 25, NLP for Credit Agreements, Indentures & PACER Dockets,** parses the program. It treats defined terms as nodes in a graph and finds the cycles, segments the document, extracts definitions, normalizes "greater of" baskets into capacity functions of EBITDA, uses language models for extraction with schema validation and mandatory citations back to the page, and feeds the result into the capacity calculator and the Priming Risk Score features of Chapter 13. It then turns to the court docket: EDGAR for the documents, CourtListener and RECAP for the filings, Rule 2019 statements as a time series of who holds what and when the Ad Hoc Group formed, split, or re-formed, claims registers as a map of the unsecured pool, and DIP roll-ups as the first move of the endgame. It uses synthetic agreement text throughout, and it studies how fast each of these signals decays once the market has read the same filing.

**Chapter 26, AI Agents & LLMs on the Credit Desk (TREND),** is the operating manual for the specifier, which is to say for the reader. It covers the pricing and research tools that language models have made possible, agentic workflows for research and surveillance, evaluation and hallucination controls (a citation that cannot be checked is a hallucination with a footnote), document question-answering with provenance, and the discipline of writing a spec a machine cannot misread: units, boundary conditions, edge cases, deterministic replay, and tests that fail loudly. It tracks adoption on desks from 2023 through 2026, with dates.

**Chapter 27, System Construction, Low-Latency Infrastructure & ASICs/FPGAs,** is the machine. It is honest about latency economics: a bond RFQ gives you seconds, but the hedge and the quote-pull happen in microseconds, and a desk that is slow to pull its quotes when Treasuries gap is a desk that has donated money to someone faster. It covers the ingestion pipeline, the security master (an LMT exchange creates new identifiers, and a security master that does not know this will price the wrong bond), pricing and risk engines, the OMS and EMS, FIX, FPGA trigger tables that evaluate $\Delta P = -D\,\Delta y$ per bond against a threshold without asking a CPU, kernel bypass, latency budgets as a queueing problem, and the kill switch, with Knight Capital in 2012 as the reason the kill switch is not optional.

The trend that defines this part is the arrival of language models on the desk and the quiet reassignment of work that followed: reading moved to machines, specifying moved to humans, and the humans who could specify best turned out to be the ones who had read the most documents by hand. Mags observes that back in her day you read the indenture yourself and were wrong in private. Theo observes that ROBO is wrong in public, instantly, and with a stack trace, and that he has come to prefer it.


---


# Part VIII: The Portfolio Manager's Playbook

*Chapter 28 and the Appendices*

The pit boss does not play hands. The pit boss decides which tables are open, what the limits are, how many chips each dealer is holding, when a dealer is tilting, and when to close the floor. Ines, who has been both the player and the pit boss, says the promotion feels like being asked to stop breathing and supervise breathing instead. Part VIII is for the reader who is about to be promoted into that chair, or who already sits in it and wants to know why the ex-RSSG analyst and the stochastic-analysis PhD cannot agree on what "risk" means at lunch.

Theo's 13-week cash flow model makes its final appearance here. It began as a spreadsheet on a USB stick, became a survival curve in Part II, a state-space feature in Chapters 3 and 25, and the liquidity-runway variable inside the Priming Risk Score in Part IV. In Chapter 28 it is the PM dashboard: the desk's own 13-week forecast of capital, liquidity, and drawdown room, with the same question it always asked (do we make it to the other side of the quarter?) now pointed at the portfolio rather than the issuer. Mags, shown the dashboard, says it is the first adjusted number she has ever trusted, and then asks who adjusted it.

**Chapter 28, What a Desk Head / Senior PM Must Know to Extract Maximum Alpha,** is a single long chapter built on Paleologo's portfolio-management framework and the sharper edges of credit. It allocates risk across signal horizons, from the three-second RFQ to the three-month factor tilt to the three-year restructuring, and shows why the Fundamental Law's $\text{IR} = \text{IC}\sqrt{\text{BR}}$ overstates breadth when forty-seven bonds share one issuer. It derives Kelly sizing for a bet with jump-to-default and a recovery floor, then applies the fractional-Kelly haircut that estimation error demands, because full Kelly on a default bet is the gambler's ruin problem wearing a suit. It covers drawdown control when bid-ask spreads widen fivefold, liquidity-adjusted VaR and days-to-liquidate, mark-to-bid discipline, the drawdown rules commonly reported at multi-strategy pods (labeled as such), and the construction of a team in which ex-RSSG analysts and PhDs produce one model instead of two arguments.

After Chapter 28 come the appendices, which are not optional reading so much as optional location. **Appendix A, Notation, Units & Conventions,** is the single notation table the whole book uses, with units, typical magnitudes, day counts, spread and recovery conventions, and a glossary of the desk and restructuring vocabulary. **Appendix B, the Data & API Atlas,** maps the data sources and interfaces (TRACE, EDGAR, CourtListener, CME, OPRA, vendor composites, open datasets) that the specifications assume. **Appendix C, the Trend Tracker,** is the dated, sourced timeline of every Trend Watch box in the book, refreshed each edition, and the first place to look if you want to know what changed since the build stamp on the title page.

The trend that defines this part is the pod. The multi-strategy platform, with its tight drawdown limits, its centralized risk, and its appetite for uncorrelated idiosyncratic return, has become the dominant employer of systematic credit talent, and its constraints shape what a PM can hold, for how long, and at what size. Under those constraints the motto is no longer a slogan. IDO or it didn't happen is the allocation rule: capital goes to the horizons and the people who produce return that survives the mute button of Part III.

Ines closes the floor. "You've seen the hand history. You know the pot. Go run the table."


---


# Appendix A: Notation, Units & Conventions

This appendix is the reader-facing edition of the book's internal style sheet. Every chapter uses the symbols below with the meanings, units, and conventions below. When a chapter has to deviate, it says so in a sentence at the point of deviation. The appendix is kept in sync with the house style bible every edition; if a symbol appears in a chapter and not here, one of the two is wrong, and it is probably the chapter.

Mags's advice applies to notation as much as to bonds: price is what you pay, and units are what you get, eventually, after the debugging.

## A.1 Three questions to ask of every symbol

Most errors in quantitative credit are not errors of mathematics. They are errors of units and conventions, and they survive because a number with the wrong units looks exactly like a number with the right ones. Before you use any quantity in this book, in a formula or in a specification handed to ROBO, ask:

1. **Which measure?** Physical ($\mathbb{P}$) or risk-neutral ($\mathbb{Q}$)? A default intensity backed out of CDS is a $\mathbb{Q}$ quantity and is systematically larger than the $\mathbb{P}$ intensity you would estimate from default history. Mixing them is the most common single bug in credit models, and it is invisible until a stress test.
2. **Which units?** Decimal, percent, basis points, points of par, years, dollars? A spread of 350 basis points is $0.035$ in a formula and "350bp" in prose, never "3.5" and never "0.35%" unless you want ROBO to build a desk that quotes bonds at a spread of 35,000bp.
3. **Which convention?** Clean or dirty price? Recovery of face, market value, or Treasury? Excess return over Treasuries or over swaps? Annualized or not? Each has a correct answer in context, and the context must be written down.

ROBO asks all three questions every time. It just does not tell you that it asked, and it picks an answer. Tell it the answer first.

## A.2 The master notation table

Typical magnitudes are illustrative and regime-dependent; they are here so you can sanity-check an output, not so you can cite them.

| Symbol | Meaning | Units | Typical magnitude (illustrative) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| $\mathbb{P}$, $\mathbb{Q}$ | Physical and risk-neutral probability measures | none | | Every expectation names its measure: $\mathbb{E}^{\mathbb{Q}}[\cdot]$. |
| $\mathcal{F}_t$ | Filtration: information available at time $t$ | none | | The conditioning set for every price. |
| $\mathbb{E}[\cdot]$ | Expectation | as its argument | | Never written "EV"; that is enterprise value. |
| $t$, $T$ | Time, maturity | years | $T - t$ of $0.25$ to $10$ | Day count stated when it matters (§A.4). |
| $V_t$ | Firm asset value (structural models) | \$ or \$mm | | Unobservable; inferred from $E_t$ and $\sigma_E$. |
| $F$ | Face value of debt (structural models) | \$ or \$mm | | Never $D$, which is duration. Unsubscripted $F$ only. |
| $E_t$ | Equity market value | \$ or \$mm | | |
| $\sigma_V$, $\sigma_E$ | Asset and equity volatility | annualized, decimal | $\sigma_E$ of $0.25$ to $0.60$ for HY issuers; $\sigma_V$ lower by leverage | Equity vol is not asset vol; see Chapters 6 and 23. |
| $r$, $r_t$ | Risk-free rate, short rate | annualized decimal, continuously compounded | $0.03$ to $0.055$ (2023–2026, approx.) | Stated if discretely compounded. |
| $\tau$ | Default time | years | | Never time to maturity; that is $T - t$. |
| $\lambda_t$ | Default intensity (hazard rate) | per year | IG $0.001$ to $0.01$; single-B $0.03$ to $0.08$; CCC $0.10$ to $0.30$ and up, under $\mathbb{Q}$ | Reserved for default. Order arrival uses $\Lambda$. |
| $S(t)$ | Survival probability, $\mathbb{Q}(\tau > t)$ | probability | $e^{-\lambda t}$ under constant intensity | $S^{\mathbb{P}}(t)$ for physical. Parentheses, not a subscript. |
| $R$, $L = 1 - R$ | Recovery rate, loss given default | fraction of par unless stated | $R = 0.40$ is the senior-unsecured CDS convention | Convention (RFV, RMV, RT) named explicitly (§A.6). |
| $s$ | Credit spread | decimal in formulas, bp in prose | IG $70$ to $150$bp; BB $200$ to $350$bp; B $300$ to $500$bp; CCC $700$ to $1{,}200$bp and up (approx.) | Measure named: OAS, $Z$, G, ASW, or PECS (§A.5). |
| $\text{OAS}$, $Z$ | Option-adjusted spread, Z-spread | bp | | $\text{OAS} \le Z$ for callables. |
| $D^{\text{mod}}$, $D^{\text{spr}}$, $D^{\text{emp}}$ | Modified, spread, and empirical duration | years (per unit of decimal yield) | IG $6$ to $8$; HY $3$ to $5$; $D^{\text{emp}} \ll D^{\text{mod}}$ in HY, near zero or negative for CCC | Chapter 8. |
| $\text{DTS}_i = D^{\text{spr}}_i \cdot s_i$ | Duration times spread | years times bp | IG $7 \times 100 = 700$; HY $4 \times 400 = 1{,}600$ | Spread volatility scales with DTS (Ben Dor). |
| $y$, $y^{\text{TSY}}$ | Yield, Treasury yield | annualized decimal | | Semi-annual bond-equivalent for US corporates unless stated. |
| $P$ | Bond price | per 100 of par, clean unless stated | $0$ to $110$; distressed below $70$ | Defaulted bonds trade flat (§A.5). |
| $S_t$ | Generic mid price or underlying | price units | | Market-making chapters. Subscript, not parentheses. |
| $q$ | Inventory | \$ notional (or units) | plus or minus \$5mm to \$50mm per line | Signed: long positive. |
| $\gamma$ | Risk aversion | inverse price | calibrated to inventory limits | Not the option Greek, which is $\Gamma$. |
| $\Lambda(\delta) = A e^{-k\delta}$ | Order-arrival intensity at quote distance $\delta$ | arrivals per day | $A$ of $0.5$ to $20$ per day per bond | $k$ in inverse distance units; written $k_\Lambda$ if a factor index $k$ is nearby. |
| $\delta$ | Quote distance from mid | price units or bp | | Not the option delta, which is $\Delta$. |
| $r^{\text{res}}$ | Reservation price | price units | | Not $r$, the interest rate. |
| $W_t$, $N_t$ | Brownian motion, Poisson process | | | $N(\cdot)$ with parentheses is the standard normal CDF. |
| $J$ | Jump size on default (price points lost) | points of par | $P - 100R$ | Appears in the $q\lambda J$ term. |
| $F_{k,t}$, $\beta_{i,k}$, $\epsilon_{i,t}$ | Factor return, loading, idiosyncratic return | decimal | | Subscripted $F$ is a factor; unsubscripted $F$ is face. |
| IDO | Idiosyncratic return | decimal or bp | | The residual after rates, carry, and factors. |
| $\text{PRS} \in [0,1]$ | Priming Risk Score | probability | | Chapter 13. |
| $\text{EV}$ | Enterprise value | \$mm | | Restructuring valuation; never expected value. |
| IC, IR, BR | Information coefficient, information ratio, breadth | none | IC $0.02$ to $0.10$; live IR $0.3$ to $1.0$ | Chapter 28; breadth corrected for issuer clustering. |
| $\Sigma$, $\mathbf{w}$ | Covariance matrix, portfolio weights | decimal squared, decimal | | Shrinkage is mandatory for stale bonds (Chapter 19). |
| $h$ | Markout horizon | minutes to days | 5 minutes, 1 hour, 1 day, 5 days | §A.7. |
| $\rho$ | Correlation | none | spread–rate $\rho < 0$ in HY | Chapter 8. |
| $\mathcal{N}(\mu,\sigma^2)$, $N(\cdot)$, $\phi(\cdot)$ | Normal distribution, its CDF, its density | | | Kaz's opening move. |
| $d_1$, $d_2$ | Black–Scholes–Merton arguments | none | | Signs verified in Chapter 6. |

## A.3 Collisions and how the book resolves them

Any symbol set this large collides with itself. The rule is: distinguish by decoration, and say so in the text. The standing resolutions:

- $F$ (face value) versus $F_{k,t}$ (factor return): the factor always carries subscripts.
- $k$ (factor index) versus $k$ (arrival-intensity decay): when both appear in one section, the decay parameter becomes $k_\Lambda$.
- $r$ (rate) versus $r^{\text{res}}$ (reservation price) versus returns: returns are written $\text{TR}$, $\text{XR}$, or $x_{i,t}$ (§A.7); if a chapter borrows $r_{i,t}$ for a return, it moves the rate to $r_f$ for that section and says so.
- $\lambda$ is default intensity, always. Arrivals are $\Lambda$. Kyle's lambda, when it appears in Chapter 18, is $\lambda^{\text{Kyle}}$.
- $D$ is duration, always. Debt face is $F$; debt market value, when needed, is $B_t$.
- $S(t)$ (survival, parentheses) versus $S_t$ (mid price, subscript). When a market-making section needs both, survival is written in full as $S^{\mathbb{Q}}(t)$.
- $\sigma$ with no subscript is the mid-price volatility in price units per square-root year in market-making sections and an annualized decimal in structural sections; each section says which in its first equation.
- $\gamma$ (risk aversion) versus the option gamma, which is $\Gamma$; $\delta$ (quote distance) versus the option delta, which is $\Delta$.
- EV is enterprise value; $\mathbb{E}[\cdot]$ is expectation. "The EV of the trade" is a phrase the book does not use.
- $\tau$ is the default time, never time to maturity (that is $T - t$) and never a transaction-cost parameter.

## A.4 Time, dates, and day counts

$t$ is measured in years everywhere. Converting calendar time into years requires a day-count basis, and the basis depends on the instrument. When a formula mixes instruments, convert each to a year fraction on its own basis and say so. A specification that says "time in years" without a basis is a specification ROBO will fill in with calendar days over 365, which is right for none of the instruments below.

| Instrument | Day count | Coupon or payment | Settlement | Notes |
| :--- | :--- | :--- | :--- | :--- |
| US corporate bonds (fixed) | 30/360 | semi-annual | T+1 (since May 28, 2024; T+2 before) | Quoted clean, settled dirty. |
| US Treasuries | ACT/ACT | semi-annual | T+1 | Benchmark for G-spread and excess returns. |
| CDS (SNAC) | ACT/360 | quarterly on 20 March, June, September, December | T+1, with upfront | Fixed coupon of 100bp (IG) or 500bp (HY); accrued rebated at trade; indices roll in March and September. |
| Leveraged loans | ACT/360 | per interest period (often 1 or 3 months) at term SOFR plus margin, often with a floor | T+7 par, T+20 distressed (LSTA convention; delayed compensation thereafter) | Chapter 21. |
| Money market, repo | ACT/360 | at maturity | T+0 or T+1 | The funding leg of the basis. |
| Equity options | calendar days over 365 for expiry; 252 trading days for volatility | | T+1 | Chapter 23. |

Calendar conventions the restructuring chapters rely on: Chapter 11 deadlines run in calendar days from the petition date, with the debtor's exclusive period to file a plan at 120 days and to solicit acceptances at 180 days, each extendable by the court to a cap of 18 and 20 months respectively. Credit-agreement test dates are fiscal-quarter ends, and the quarter that matters for basket capacity is the most recently ended one for which financial statements have been delivered, which is rarely the one you were thinking of.

## A.5 Prices, yields, and spreads

**Price.** Per 100 of par. One point is one percent of par, or \$10,000 per \$1 million of face. The integer part of a price is its "handle." Bonds are quoted clean (excluding accrued interest) and settle dirty (clean plus accrued). Bonds in default trade flat: no accrued interest is added, and the price embeds whatever claim to accrued the holder has. Loans quote on price per 100 plus a margin over the reference rate.

**Yield.** US corporates quote a semi-annual bond-equivalent yield; formulas in this book use continuous compounding unless they say otherwise. The conversion is $r^{\text{cc}} = 2 \ln\!\left(1 + \tfrac{y}{2}\right)$. Callable bonds quote yield-to-worst, the lowest yield across all call and maturity dates on the assumption that the issuer exercises against you, which it will.

**Basis points.** 1bp $= 0.01\% = 0.0001$. Spreads are written in basis points in prose and tables and in decimal in formulas, and code carries the unit in the variable name (`spread_bp`, `spread_dec`). "Spreads widened 25bp," never "0.25%."

**Dollar sensitivities.** DV01 is the dollar change in a position's value for a one-basis-point move in yield; CS01 is the same for spread. For a bullet bond,

$$\text{DV01} \approx D^{\text{mod}} \times \frac{P}{100} \times \text{Face} \times 0.0001 .$$

A \$10 million position at a price of 95 with $D^{\text{mod}} = 6$ has a DV01 of about $6 \times 0.95 \times 10{,}000{,}000 \times 0.0001 = 5{,}700$ dollars per basis point *(illustrative)*.

**Spread measures.** "The spread" is at least five different numbers, and the basis between a bond and its CDS depends on which one you chose.

| Measure | Definition | Use | Trap |
| :--- | :--- | :--- | :--- |
| G-spread | Yield minus the interpolated Treasury yield at the same maturity | Quick IG comparisons | Ignores curve shape and coupon. |
| I-spread | Yield minus the interpolated swap rate | Swap-funded investors | The swap curve (SOFR) choice matters. |
| Z-spread ($Z$) | Constant spread added to every zero rate on a discount curve so that discounted cash flows equal the dirty price | Bullet bonds; the standard input to a basis | Name the curve (Treasury or swap). Ignores embedded options. |
| OAS | Z-spread after removing option value with an interest-rate model | Callable and putable bonds; HY index analytics | Model-dependent; $\text{OAS} \le Z$ for callables, the gap being option cost in bp. |
| ASW (par-par) | Margin over floating such that a package of the bond bought at par plus a coupon-for-floating swap is worth zero | Funded investors; basis against CDS | Diverges from $Z$ when price is far from par; a market-value variant exists. |
| PECS | The flat CDS spread whose implied survival curve, with the CDS recovery assumption, reprices the bond | The right bond spread for a CDS basis | Depends on the assumed recovery. |
| Discount margin | For floaters and loans, the spread over the reference rate that equates PV to price, assuming forwards equal the current rate | Loans and FRNs | State whether the floor is priced. |
| CDS quoted spread | A quoting convention converted to an upfront payment by the ISDA Standard Model under a flat hazard rate and a fixed recovery | Quoting | Not the par spread of a term-structure model; the upfront is the traded number. |

The book's **basis** is $\text{basis} = s^{\text{CDS}} - s^{\text{bond}}$, with the bond measure named ($Z$ or PECS). Negative basis means the bond is cheap relative to protection: buy the bond, buy protection, and discover what funding costs in a crisis (Chapter 24).

**Price versus spread quoting.** Bonds trade on spread while a spread is informative and on price once it is not. The common rule of thumb is that a spread above roughly 1,000bp, or a price in the low 80s or below, means the bond is "trading on price" *(convention; approximate)*, because the yield-to-maturity arithmetic assumes the coupons will be paid, and at that point nobody believes it.

**Spread duration versus modified duration.** $D^{\text{spr}}$ is the sensitivity of price to spread; $D^{\text{mod}}$ to yield. For fixed-rate bullets they are nearly equal. For floaters, $D^{\text{mod}}$ is roughly the time to the next reset while $D^{\text{spr}}$ is roughly the remaining life, which is why loans have almost no rate risk and plenty of credit risk.

**DTS.** $\text{DTS} = D^{\text{spr}} \times s$ with $s$ in basis points, in units of years times bp. Its justification is empirical: relative spread changes have similar volatility across bonds, so absolute excess-return volatility is proportional to DTS. A bond with DTS 1,600 is about twice as risky as one with DTS 800, regardless of which has the longer duration (Chapter 8).

## A.6 Recovery conventions

Recovery is a rate, a convention, and an argument, in that order.

**Symbol.** $R$ is the recovery rate and $L = 1 - R$ the loss given default, both as fractions of the relevant base. The base is the convention:

- **Recovery of face value (RFV).** On default the holder receives $R$ times face (plus, in some setups, accrued). This is how CDS settle (the auction yields a price per 100 of par) and how the book prices bonds unless it says otherwise. It makes a bond's default payoff independent of its coupon and maturity, which is realistic for claims in bankruptcy.
- **Recovery of market value (RMV).** On default the holder receives $R$ times the bond's market value an instant before default (Duffie–Singleton). It produces the elegant risky discount rate $r + \lambda L$, which lets you price defaultable cash flows on a spread-adjusted curve as if they were riskless. "Forty percent of whatever it was worth a second ago" is not what happens in a courtroom, but the mathematics is clean enough that it is worth knowing when the approximation is harmless (Chapter 6).
- **Recovery of Treasury (RT).** On default the holder receives $R$ times the value of an otherwise identical riskless bond (Jarrow–Turnbull). Useful in rating-transition models; rare on a desk.

**Market conventions.** The ISDA Standard Model converts quoted CDS spreads to upfront payments using assumed recoveries of 40 percent for senior unsecured and 20 percent for subordinated North American corporate reference entities. These are quoting conventions, not forecasts, and a desk that treats 40 percent as an expected recovery for a CCC retailer with a drop-down in progress has confused a unit with a fact.

**Realized recoveries.** Two different measurements share the name: the trading price of the defaulted instrument about 30 days after default, and the ultimate recovery at emergence, discounted back to the default date. They can differ substantially and in either direction. Any cited recovery statistic in this book names which one it is. Recoveries fall with seniority and collateral (first-lien loans at the top, subordinated bonds at the bottom); the sourced numbers and their dispersion are in Chapter 5, where recovery is modeled as a Beta distribution with mass points at zero and one.

**Physical versus risk-neutral.** A recovery backed out of market prices is a $\mathbb{Q}$ quantity. The credit triangle $s \approx \lambda(1 - R)$ shows why this matters: one observed spread is consistent with infinitely many $(\lambda, R)$ pairs, and the market's split between them is not identified from the spread alone. Recovery locks exist to trade the split directly.

**Recovery in the LMT era.** Recovery is now a property of the instrument and the transaction, not the issuer. A priming transaction changes $R$ for left-behind lenders without any default occurring, which is why the default and recovery distributions of Chapter 5 are re-estimated under the regime shifts of Chapter 14.

## A.7 Return conventions

- **Total return** ($\text{TR}$): price change plus coupon income plus reinvestment over the period, per unit of starting dirty price, in decimal.
- **Excess return** ($\text{XR}$): total return minus the return of a duration-matched Treasury portfolio over the same period. Matching is ideally by key-rate duration, not by a single number. This is the book's default meaning of "excess return" in Part III. Excess return over swaps is used for asset-swap-based analysis and is named as such.
- **Spread return approximation:** $\text{XR} \approx -D^{\text{spr}}\,\Delta s + \tfrac{1}{2} C^{\text{spr}} (\Delta s)^2 + \text{carry}$, with $s$ in decimal and $C^{\text{spr}}$ the spread convexity. **OAS carry** is $\text{OAS} \times \Delta t$; **yield carry** includes the Treasury component; **roll-down** is reported separately.
- **Simple versus log returns:** simple returns aggregate across positions; log returns aggregate across time. Each chapter says which it is using.
- **Annualization:** means by 252 (daily) or 12 (monthly); volatilities by $\sqrt{252}$ or $\sqrt{12}$. Bonds with stale prices understate short-horizon volatility and correlation, which is why Chapter 8 uses lag-sum betas and Chapter 19 shrinks covariances.
- **Markout:** $\text{markout}_h = \text{side} \times \left(m_{t+h} - P_{\text{trade}}\right)$, with $\text{side} = +1$ when the desk bought and $-1$ when it sold, $m$ the composite mid, and $h$ the horizon (5 minutes, 1 hour, 1 day, 5 days). Reported in bp of price or bp of spread, stated which. A persistently negative average markout on a counterparty's flow is the definition of toxic flow. Ines calls the markout log the hand history and reads it before she reads anything else.
- **Sharpe ratio and information ratio:** annualized; Sharpe in excess of funding, IR relative to the named benchmark; always reported with the sample length, and in Chapter 7 with the deflated version that accounts for the number of strategies tried.
- **IDO:** the residual $\epsilon_{i,t}$ after removing rates, carry, and factor exposures (Chapter 8). Reported in bp per period. The desk's unit of alpha.
- **DTS-scaled returns:** $\text{XR} / \text{DTS}$, making bonds of different risk comparable.
- **In code:** returns and spreads are decimals inside arrays; conversion to bp and percent happens at the input and output boundaries; variable names carry units.

## A.8 Sizes, signs, and desk arithmetic

- **Units of size.** \$mm is millions and \$bn is billions. Face (notional) and market value are different numbers: \$10mm face at a price of 60 is \$6mm of market value and \$10mm of claim.
- **Risk is reported four ways:** DV01 (rates), CS01 (spread), DTS-weighted market value (proportional spread risk), and jump-to-default, $\text{JTD} = \text{MV} - R \times \text{Face}$ for a long position, the loss if the issuer defaults now.
- **Sign conventions.** Long credit means long the bond or short protection; the protection buyer pays the premium and is short credit. Spreads up means prices down means long credit loses. In a return decomposition the rate term is $-D\,\Delta y$; a plus sign there is the most common bug in a first implementation.
- **Rounding.** Bond prices in decimals (historically eighths); spreads to the basis point; CDS upfronts to a hundredth of a point.
- **TRACE dissemination.** Prints above the dissemination caps display with a capped size; the caps and reporting times have changed over the period this book covers and are detailed in Chapters 18 and 22.

## A.9 Glossary of desk and restructuring terms

One line each, alphabetical, with a joke where the term can bear one.

- **363 sale.** A sale of a debtor's assets under Section 363 of the Bankruptcy Code, outside the ordinary course and "free and clear" of liens, usually with a stalking-horse bidder and an auction. Faster than a plan, which is why buyers like it and some creditors do not.
- **503(b)(9) claim.** An administrative-expense priority claim for the value of goods (not services) a debtor received in the 20 days before filing. The one time in bankruptcy when being a late supplier is good news.
- **Absolute priority rule.** Under Section 1129(b), a dissenting class must be paid in full before any junior class receives anything. Honored in principle, negotiated in practice, and the reason the fulcrum matters.
- **Ad hoc group.** An informal group of creditors holding the same instrument who hire common counsel to negotiate collectively. Disclosed in Rule 2019 statements. Speaks in unison, mostly in footnotes.
- **Adequate protection.** Compensation a secured creditor receives in bankruptcy for the diminution in value of its collateral while the automatic stay is in effect. "Adequate" is doing a lot of work in that sentence.
- **All-to-all trading.** An electronic protocol in which any participant, not only dealers, can respond to a request for quote. The moment the bazaar got a second set of stalls.
- **Asset swap (ASW).** A package of a fixed-rate bond and an interest-rate swap converting its coupon to floating; the asset swap spread is the margin over the floating rate that makes the package worth par.
- **Authorized participant (AP).** A dealer permitted to create and redeem ETF shares in kind with the fund, exchanging baskets of bonds for creation units. The people who open the sealed boxes.
- **Available Amount basket.** A builder basket for restricted payments and investments whose capacity grows with retained earnings (or a fraction of net income or EBITDA) since closing. Capacity you did not know the sponsor had.
- **Backstop.** A commitment, usually by an ad hoc group, to purchase any portion of a rights offering not taken up by other holders, in exchange for a fee and often a discount. The committed capital is real; so is the fee.
- **Basis (CDS–bond).** The difference between the CDS spread and the bond's spread on a comparable measure (Z, ASW, or PECS). Negative basis: bond cheap to CDS. The trade that works until funding disappears.
- **Blocker.** A covenant provision drafted after a famous transaction to prevent the next one: a J.Crew blocker (restricts transfers of material IP to unrestricted subsidiaries), a Serta blocker (requires pro rata treatment in any uptier), a Chewy blocker (restricts guarantor release via partial equity sales). Named like hurricanes, for the damage.
- **BWIC / OWIC.** Bids (or offers) wanted in competition: a list of bonds or loans put out for auction, typically by a fund or CLO. Every dealer who sees the list learns something, which is the leakage problem.
- **CCC bucket.** The maximum share (commonly 7.5 percent) of a CLO's portfolio that may be rated CCC or below before excess holdings are carried at market value for overcollateralization tests. The reason CLOs sell at the worst time.
- **CDX / iTraxx.** The standardized credit default swap indices for North America (CDX IG, 125 names; CDX HY, 100 names) and Europe (iTraxx Main and Crossover), rolling to a new series each March and September. The most liquid thing in credit; the hedge everyone uses and nobody loves.
- **Change-of-control (CoC) put.** The bondholder's right to put bonds to the issuer at 101 upon a change of control, often coupled with a ratings-decline trigger. An option that pays only if the deal closes and the trigger is met.
- **Cheapest-to-deliver (CTD).** In CDS settlement, the protection buyer's right to deliver (or the auction's tendency to price) the lowest-priced qualifying obligation. A free option embedded in a product sold as insurance.
- **Clean / dirty price.** Clean excludes accrued interest; dirty includes it. Bonds are quoted clean and settled dirty. Defaulted bonds trade flat.
- **CLO.** Collateralized loan obligation: a vehicle that buys leveraged loans and issues tranches from AAA to equity, managed subject to coverage and quality tests during a reinvestment period. The largest buyer of loans and a mechanical seller under stress.
- **Composite price.** A vendor's estimate of a bond's current mid built from TRACE prints, dealer quotes, and models. Several named products exist; the book calls them composites. Not a price; a prior.
- **Cooperation agreement.** An agreement among lenders to act together and not to participate in a non-pro-rata transaction without the group. Increments the counter.
- **Covenant-lite.** A loan without financial maintenance covenants, relying on incurrence tests only. "Lite" refers to the lender's protection, not the document's weight.
- **Cram-down.** Confirmation of a plan over the objection of an impaired class under Section 1129(b), subject to the absolute priority rule and the fair-and-equitable test. Nobody gets crammed up.
- **Creation unit.** The block size (often tens of thousands of shares) in which an ETF's shares are created or redeemed by authorized participants.
- **Credit event.** The ISDA-defined triggers for CDS: bankruptcy, failure to pay, and (where applicable) restructuring, plus others for sovereigns. Determined by a Determinations Committee, and the subject of more creative lawyering than the drafters anticipated.
- **Cross-default / cross-acceleration.** A default under one debt instrument triggers a default under another (cross-default), or does so only once the first debt is actually accelerated (cross-acceleration). The difference is a quarter of negotiation.
- **Custom basket.** A creation or redemption basket that differs from a pro rata slice of the fund, permitted under the 2019 ETF rule. How bond ETFs stay liquid when their bonds are not.
- **D2C / D2D.** Dealer-to-client and dealer-to-dealer trading. TRACE flags which is which; the information content differs.
- **Debtor-in-possession (DIP) financing.** New money lent to a debtor in bankruptcy with super-priority status, often with liens priming prepetition lenders. The first-mover advantage in Chapter 11.
- **DIP roll-up.** A DIP structured so that prepetition loans held by the DIP lenders are converted into (rolled into) the super-priority DIP. The lenders who provide new money get their old money promoted.
- **Discount margin.** For a floating-rate instrument, the spread over the reference rate that equates the present value of cash flows to the price, assuming forward rates equal the current rate.
- **Distressed exchange.** An out-of-court transaction in which creditors accept new securities or cash worth less than the original claim, to avoid a bankruptcy. Counted as a default by the rating agencies; counted as a feature by the sponsor.
- **Double-dip.** A structure that gives new lenders two claims against the same credit group: one direct (or via a guarantee) and one via an intercompany loan from the borrowing entity. Two tickets, one seat.
- **Drop-down.** The transfer of assets (classically intellectual property) to an unrestricted subsidiary outside the collateral package, which then raises new debt against them. J.Crew, 2016. The door was in the blueprint.
- **DTS (Duration Times Spread).** Spread duration multiplied by spread, in years times bp. The best single measure of a bond's credit risk, because spread volatility scales with spread level.
- **DV01 / CS01.** The dollar change in a position for a one-basis-point move in yield (DV01) or credit spread (CS01).
- **EBITDA add-backs.** Adjustments to EBITDA permitted by the credit agreement, including projected cost savings and synergies, often capped at a percentage of EBITDA, and often not. Mags's least favorite word is "adjusted."
- **Exclusivity period.** The window (initially 120 days from the petition date to file a plan and 180 days to solicit acceptances, extendable up to 18 and 20 months) during which only the debtor may propose a plan. The clock the whole case runs on.
- **Fallen angel / rising star.** A bond downgraded from investment grade to high yield (fallen angel) or upgraded the other way (rising star). Forced-seller flow in both directions.
- **First-day motions.** The motions a debtor files at the start of a case to keep operating: cash management, wages, critical vendors, DIP approval. The first signal of who is in charge.
- **Fulcrum security.** The class in the capital structure at which value runs out, which therefore receives most of the reorganized equity. Not a physics thing, Kaz.
- **General unsecured claim (GUC).** A claim with no collateral and no statutory priority; the residual class, usually paid in cents, stock, or litigation-trust interests.
- **Hit rate.** The share of RFQs a dealer wins. A high hit rate is good news until the markouts arrive.
- **IDO.** Idiosyncratic return: what remains of a bond's return after removing rates, carry, and factor exposure. The desk's unit of alpha. IDO or it didn't happen.
- **iNAV.** The intraday indicative value of an ETF, published periodically during the trading day from the fund's basket. A number that is correct about a basket nobody can trade.
- **Impaired class.** A class of claims whose legal rights are altered by the plan; only impaired classes vote. Being unimpaired sounds nice and means you have no say.
- **Incurrence vs. maintenance covenant.** A maintenance covenant must be satisfied at every test date; an incurrence covenant is tested only when the borrower takes an action (incurs debt, pays a dividend). Covenant-lite means the maintenance covenants went away.
- **Investment grade / high yield.** Rated Baa3/BBB- or better by the agencies, or not. The boundary with the most forced sellers on either side.
- **J.Crew trapdoor.** The combination of investment baskets that allowed J.Crew in 2016 to move intellectual property into an unrestricted subsidiary and borrow against it. Now a common noun.
- **Jump-to-default (JTD).** The loss a position suffers if the issuer defaults immediately: market value minus recovery times face. The risk that no diffusion model sees coming.
- **Key-rate duration.** The sensitivity of price to a move in one maturity point of the yield curve, holding the others fixed. The thing a "duration-matched" hedge usually is not.
- **Liability management transaction (LMT).** An out-of-court transaction (uptier, drop-down, double-dip, exchange) that changes the priority or collateral of existing debt, typically with the consent of a majority but not all lenders. The genus, not the species.
- **Liquidity cost score (LCS).** A bond-level estimate of round-trip transaction cost as a fraction of price, built from quotes and trades (Barclays methodology; Ben Dor). The number that turns paper alpha into real alpha, or does not.
- **Markout.** The change in a composite mid after a trade, signed by the dealer's side, at a fixed horizon. The hand history: it tells you whether the counterparty knew something.
- **Most-favored-nation (MFN).** A provision requiring that if the borrower issues new pari passu debt at a wider spread, existing lenders' spread is raised to match, often subject to a cushion and a sunset. A spread floor with an expiry date.
- **NAV.** Net asset value of a fund per share, struck once a day from the fund's marks; for bond ETFs, usually a bid-side valuation.
- **Negative pledge.** A covenant barring the borrower from granting liens to others without equally securing the covenanted creditor. Plain-vanilla bonds have them; the exceptions are where the structuring happens.
- **OAS (option-adjusted spread).** The constant spread over the discount curve that reprices the bond after accounting for embedded options under an interest-rate model.
- **OC / IC tests.** Overcollateralization and interest-coverage tests in a CLO; failing one diverts cash flows from junior tranches to pay down senior notes. The automatic deleveraging that makes CLOs sell loans into weakness.
- **Open market purchase.** The exception in many credit agreements allowing a borrower to buy back loans from individual lenders without a pro rata offer. The three words on which the Serta uptier rested; the Fifth Circuit disagreed on the last day of 2024. The most expensive three words in finance.
- **Orphaned CDS.** A credit default swap whose reference entity no longer has deliverable debt, usually after a refinancing at a different entity, leaving protection that pays nothing on a default that cannot technically occur.
- **Pari passu.** Of equal rank. The thing minority lenders believed they were until the amendment passed.
- **Pari-plus.** A liability management structure in which new debt ranks pari passu with existing debt at the original borrower and also holds an additional claim elsewhere in the group. A double-dip with better branding.
- **PECS (par-equivalent CDS spread).** A bond's spread restated as the flat CDS spread that would reprice it under the CDS survival curve and recovery assumption, so that bond and CDS can be compared directly.
- **PIK (payment-in-kind).** Interest paid by issuing more of the same instrument rather than cash. The borrower's way of saying "later."
- **Plan of reorganization.** The document that specifies how claims are classified, treated, and paid in a Chapter 11 case; confirmed by the court after creditor voting.
- **Portability.** A provision allowing a change of control without triggering the CoC put if a leverage or ratings test is met. A short option bondholders wrote without being asked.
- **Portfolio trade (PT).** A single transaction in which a basket of bonds (often 50 to several hundred lines) is bought or sold at one price with one counterparty, typically a dealer who hedges with ETF creation or redemption. The basket is now the unit of liquidity.
- **Pre-pack / pre-negotiated.** A bankruptcy in which the plan is negotiated (and in a pre-pack, voted) before filing, so that the case lasts weeks instead of years.
- **Priming.** Placing new debt ahead of existing debt in priority or collateral, whether by a DIP, an uptier, or a drop-down. The Priming Risk Score estimates its probability.
- **Priming Risk Score (PRS).** This book's model-based probability, in $[0,1]$, that an issuer executes a priming transaction within a horizon, built from document features, sponsor behavior, and liquidity runway. Defined in Chapter 13.
- **Pro rata sharing.** The requirement that payments and collateral proceeds be shared among lenders in proportion to holdings. A sacred right in most agreements; the thing the uptier is designed to route around.
- **Recovery lock.** A derivative fixing the recovery rate on a reference entity, isolating recovery risk from default-timing risk. Exists because the credit triangle has two unknowns.
- **Reinvestment period.** The years (commonly four to five) during which a CLO manager may reinvest principal proceeds in new loans; after it ends, the vehicle amortizes. The age at which CLOs stop buying.
- **Request for quote (RFQ).** An electronic request to one or more dealers for a price on a specified size, with a response window. The unit of interaction on the modern credit desk; the adverse-selection problem in three seconds.
- **Restricted payments (RP) basket.** Capacity under the credit agreement for dividends, distributions, and certain investments, built from fixed amounts, builder amounts, and ratio-based tests. Where the money leaves.
- **Restricted / unrestricted subsidiary.** Subsidiaries inside the covenant and collateral package (restricted) or designated outside it (unrestricted). Assets that move from one to the other have left the building.
- **Rights offering.** An offering of new equity in a reorganized company to existing claimholders, often at a discount to plan value and usually backstopped. The entry fee for the post-reorg equity.
- **Risky PV01 (RPV01).** The present value of one basis point of CDS premium paid until default or maturity: the survival-weighted annuity. The number that converts a spread into an upfront.
- **Rule 2019 statement.** A disclosure under Federal Rule of Bankruptcy Procedure 2019 by a group or committee representing multiple creditors, listing members and their holdings. The Ad Hoc Group's only unscripted speech.
- **Sacred rights.** Amendments that require the consent of each affected lender rather than a majority: pro rata sharing, payment terms, release of all or substantially all collateral. No priest is involved.
- **SNAC (Standard North American Corporate) contract.** The post-2009 CDS contract with fixed coupons (100 or 500 basis points), standardized dates, and an upfront payment, enabling fungibility and central clearing.
- **Special mandatory redemption (SMR).** A provision requiring the issuer to redeem acquisition-financing bonds, usually at 101, if the acquisition fails to close by a deadline. An option on the deal breaking.
- **Springing lien / springing maturity.** A lien that attaches, or a maturity that accelerates, upon a trigger such as a ratings change or the failure to refinance another tranche by a date. Yes, Kaz, it springs. At you.
- **Succession event.** ISDA rules determining which entity a CDS references after a merger, spin-off, or debt transfer. Where orphaned CDS are born.
- **Toxic flow.** Order flow whose counterparties, on average, know more than the market maker, so that filling it loses money after the fact. Measured by markouts; priced by the adverse-selection penalty.
- **TRACE.** FINRA's Trade Reporting and Compliance Engine, which has disseminated corporate bond transaction prices since 2002. The origin of the dataset, and thus of this book.
- **Uptier.** A transaction in which a majority of lenders amend the agreement to allow new super-priority debt, exchange their holdings into it, and leave non-participating lenders subordinated. Serta, 2020. The floors were reordered overnight.
- **Waterfall.** The ordered allocation of value among claims by priority and collateral, under a plan, a CLO indenture, or an intercreditor agreement. A correct waterfall conserves value; test yours.
- **Yield-to-worst.** The lowest yield across all call and maturity dates for a callable bond, assuming the issuer exercises against you. The yield you should assume.
- **Z-spread.** The constant spread added to every point on a zero-coupon discount curve so that discounted cash flows equal the bond's dirty price.
- **Zero floor.** A minimum level (often zero, sometimes higher) for the reference rate in a floating-rate loan, so the coupon cannot fall below margin plus floor. An interest-rate option the borrower sold without pricing it.


---


# Appendix B: The Data & API Atlas

It is 11:40 p.m. Theo Marsh has fourteen browser tabs open and a spreadsheet called `data_sources_FINAL_v3.xlsx`.

"TRACE has every corporate bond trade," he says. "EDGAR has every credit agreement. FRED has the high-yield spread back to the nineties. So I can rebuild the credit market from public data and go home."

Ines Okafor doesn't look up. "Which of those rows did you check this week? A trade over \$5 million shows up on the tape as `5MM+`. The credit agreement is filed with its schedules left out and the pricing grid redacted. And since April, the FRED series you love keeps only three years of history. Every dataset is a hand history with some cards face down. Your job is to know which ones."

Mags Dunleavy, coat on: "Back in my day the data source was a guy named Lenny. Lenny had survivorship bias too. He only remembered the trades that worked."

ROBO, asked to "get all the bond data," has queued 4.1 million requests to `data.sec.gov` with no User-Agent header. It is about to find out what a 403 is.

This appendix is the reference to keep open next to every other chapter. By the end of it you will be able to: (i) say, for each major credit data source, what it is, who pays for it, and which fields carry signal; (ii) list how each one misleads you: stale prices, survivorship, look-ahead, caps, licensing; (iii) quantify how stale prices distort variance and beta, and correct for it; and (iv) give ROBO a strict, testable schema for a tidy bond panel. Every URL below was checked on 2026-10-17. Where we could not check a source, it has no link.

## B.0 How to Read an Atlas Entry (and Four Ways Data Lies)

Each entry gives **what it is**, **access & cost**, **key fields**, **gotchas**, and **used in**. Four failure modes come up in almost every entry, so we state them formally once. ROBO cannot enforce a vibe.

**Sin 1: Stale prices.** Let $r_t$ be the true log return, i.i.d. with variance $\sigma^2$. Suppose the observed price only partially adjusts each day: $p^{o}_t = (1-\theta)\,p_t + \theta\,p^{o}_{t-1}$, where $\theta\in[0,1)$ measures staleness. Then

$$r^{o}_t = (1-\theta)\sum_{k=0}^{\infty} \theta^{k} r_{t-k}, \qquad \operatorname{Var}(r^{o}_t) = (1-\theta)^2 \sigma^2 \sum_{k=0}^{\infty}\theta^{2k} = \frac{1-\theta}{1+\theta}\,\sigma^2 .$$

The lag-$h$ autocovariance is $\gamma_h = \theta^{h}\operatorname{Var}(r^o_t)$, so $\rho_1=\theta$. The long-run variance is untouched:

$$\sum_{h=-\infty}^{\infty}\gamma_h = \frac{1-\theta}{1+\theta}\sigma^2\Big(1 + \tfrac{2\theta}{1-\theta}\Big) = \sigma^2 .$$

Staleness does not remove risk. It spreads today's risk over the following days. With $\theta=0.6$, a bond shows 25% of its true daily variance (half the volatility) and 60% first-order autocorrelation. Betas take the same hit. If $r_t=\beta f_t+\epsilon_t$ and the factor is observed fresh, then $\operatorname{Cov}(r^o_t,f_{t-k})=(1-\theta)\theta^k\beta\sigma_f^2$. A contemporaneous regression recovers only $(1-\theta)\beta$. The Dimson (1979) sum of lagged betas recovers $\beta$, because $\sum_k(1-\theta)\theta^k=1$. This is part of why high-yield bonds look rate-insensitive in daily data (Chapter 8). A stale price is a calm price, and calm is the most expensive thing to be wrong about.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.208:* "we attempt to directly identify and exclude observations that possibly reflect stale prices. Specifically, all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month."
>
> **Annotation.** The Barclays team used two fixes. Sampling biweekly instead of daily lowers the effective $\theta$, and a run-length filter removes bonds whose quotes don't move. The run-length rule still works as a first screen on *evaluated* prices, because those repeat when nothing new arrives. A price carried forward from TRACE trades doesn't look like "unchanged quotes," though. It is a single trade price copied onto later rows, so our schema carries an explicit `days_stale` counter instead (§B.16). The derivation shows what the filter buys you: dropping the bonds with high $\theta$ pushes measured variance and beta back toward the truth. The price is a tilt toward liquid names, which is a factor exposure of its own (Chapter 9).

**Sin 2: Look-ahead.** A feature $X_{i,t}$ is admissible only if $X_{i,t}\in\mathcal{F}_t$. In code, that means you join on `knowledge_ts` (when you could have known it), never `effective_ts` (the date the value refers to). Some examples. A TRACE print executed at 4:58 p.m. and reported at 5:12 p.m. is known at 5:12. A downgrade effective Tuesday and published Thursday is known Thursday. An XBRL fact is known when the filing is accepted. Restated values must not overwrite originals in a backtest.

**Sin 3: Survivorship.** The universe at date $t$ is every bond that existed and was eligible at $t$, including bonds that later defaulted, were called, tendered, or matured. Today's index constituents, today's ETF holdings, and any "active securities" table are survivor-biased. In credit, the bonds that drop out are the defaulted ones, and they *are* the left tail.

**Sin 4: Licensing.** Ratings, CUSIPs, index levels, and composites come with contracts that limit storage, redistribution, and derived products. If you can't legally keep the data behind a backtest, you can't audit the backtest. That is a model risk.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.20:* "It is necessary to combine information from a number of different data sources in order to build up a picture of the price landscape in the credit markets. These include data from market runs, electronic platforms, TRACE data and dealer information."
>
> **Annotation.** No single source gives you the price. This appendix sorts the sources into three kinds: *public and lagged* (TRACE), *proprietary and fresh* (platform RFQs, dealer runs), and *model outputs* (composites, evaluated prices). If a model treats all three as interchangeable "prices," the noise in one leaks into labels built from another.

## B.1 FINRA TRACE: The Tape

**What it is.** FINRA's reporting and dissemination system for OTC fixed-income trades. It launched July 1, 2002, with a 75-minute reporting deadline. The deadline fell to 45 minutes (October 1, 2003), then 30 (October 1, 2004), then 15 (July 1, 2005). Every public corporate trade has been disseminated as soon as it is received since January 9, 2006. Later additions: agency debentures and primary-market trades (March 1, 2010); ABS/MBS reporting (May 16, 2011); dissemination of 144A trades (June 30, 2014) and ABS (June 1, 2015); Treasuries reportable for regulatory purposes (July 10, 2017). *(Source: FINRA, TRACE Fact Book 2025, <https://www.finra.org/sites/default/files/2026-02/TRACE_FactBook_2025.pdf>.)*

**Access & cost.** TRACE comes in four layers, from freshest to most complete:

1. **Real-time feeds.** The Bond Trade Dissemination Service (BTDS) is the real-time corporate feed. Agency, securitized-product, and 144A trades have their own feeds. You license it from FINRA or, more often, through a market-data vendor, and it is priced like professional market data. We could not retrieve the current BTDS spec or fee schedule this session, so check both before you build a feed handler.
2. **Free views.** FINRA's site shows disseminated trades for individual bonds. The API Developer Center (<https://developer.finra.org/>) has a Query API and a dataset catalog. This is the public tape: sizes are capped and dealers are not identified.
3. **Enhanced Historical Data (EHD).** EHD includes "information previously not disseminated to the public, such as buy/sell indicators and counterparty (dealer or customer) information," and quantity "as reported and not subject to dissemination caps." FINRA "makes historical data available 6 months (18 months for Securitized Products) after the transaction date and publishes the information quarterly" (FINRA EHD product sheet, <https://www.finra.org/sites/default/files/TRACE_Enhanced_Historical_Data.pdf>). Coverage: corporate and 144A from July 1, 2002, agency from April 2010, structured products from May 2011. You need a Historical Data Agreement and pay fees. CUSIP and non-CUSIP versions are offered, the latter "for customers without a CUSIP license" (<https://www.finra.org/filing-reporting/trace/historic-academic-data>). Materials from 2016–2017 quote an 18-month corporate lag. The current page says 6.
4. **Academic Corporate Bond TRACE Data.** Available only to higher-education institutions, "on a 36-month delayed basis," with "masked identifying information regarding the dealer reporting each transaction." It includes 144A and non-disseminated trades. At launch the fee was \$500 per year plus a \$500 one-time set-up fee (FINRA Regulatory Notice 16-43, <https://www.finra.org/sites/default/files/notice_doc_file_ref/Regulatory-Notice-16-43.pdf>). Masked dealer IDs make dealer-network and inventory research possible, but nothing like them exists in production. Keep it on the research side of the wall.

Most researchers get TRACE Standard, Enhanced, and 144A tables through **WRDS**.

**Key fields.** CUSIP and FINRA symbol; execution date and time; *report* date and time; price; yield; quantity (capped publicly, true in EHD); buy/sell side; reporting- and contra-party type (dealer or customer); principal or agency capacity; commission flag; trade status and message sequence numbers; as-of and special-condition flags; ATS identifier; and the portfolio-trade modifier (from May 15, 2023).

**Dissemination caps.** On the public tape, investment-grade and unrated trades above \$5 million print as `5MM+`, and high-yield trades above \$1 million print as `1MM+`. True sizes appear only in historical products.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162:* "TRACE ... disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** "Censored" is the statistically correct word. A capped print is right-censored, so volume sums and VWAPs built from the public tape are skewed toward small trades, and small trades tend to print on the wrong side of the spread. A 2026 desk does three things about it. It flags every capped print. It imputes true size from a tail fitted to EHD, for example a Pareto tail conditional on exceeding the cap. And it never trains on public-tape volumes while scoring on EHD volumes. One more trap: the cap depends on the rating *at trade time*. A fallen angel's cap drops from \$5mm to \$1mm on the day the downgrade becomes known, and §B.16 tests for exactly this.

**Reporting timing: the one-minute saga.** The 15-minute outer limit has applied to corporates since 2005. On September 20, 2024, the SEC approved SR-FINRA-2024-004, which cut the limit to one minute for fully electronic trades. Manual trades got a phase-in (15 minutes, then 10, then 5), and firms with fewer than 4,000 reported trades a year were exempt. "FINRA has not implemented the changes approved in File No. SR-FINRA-2024-004." Members pointed to allocations, portfolio trades, and voice or chat workflows. On September 16, 2025, the SEC approved SR-FINRA-2025-008, which *keeps* the 15-minute limit. The same filing lets dual broker-dealer/investment-adviser firms report the allocations of an aggregate order as a single report that includes the number of accounts (Release No. 34-103986, <https://public-inspection.federalregister.gov/2025-18147.pdf>). The record shows 82.9% of eligible trades executed between 8:00 a.m. and 6:15 p.m. were already reported within one minute in 2022. The rule mainly targeted the slow 17%, which is mostly blocks and voice trades, and those are the trades that carry information. Rule 6730 also sets 60 minutes for Treasuries, post-issuance CMOs, and specified pools; same day for CDOs and CMBS executed by 5:00 p.m.; and T+1 for List/Fixed Offering Price and Takedown trades (<https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730>).

**What is *not* disseminated.** Under Rule 6750 (<https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750>): affiliate trades; certain M&A transfers; List/Fixed Offering Price and Takedown trades; CMBS, CDOs, and CMOs that don't qualify for periodic dissemination; foreign sovereigns; and Treasuries other than on-the-run nominal coupons. Those on-the-run coupons have been disseminated end-of-day since March 25, 2024, with size caps, no participant IDs, and free next-day access for non-professional use (Regulatory Notice 24-06). CLO tranches fall under the CDO exclusion. They are *reported* to TRACE but not disseminated by transaction, so no public CLO tape exists.

**Gotchas.**
- *The tape is messages, not trades.* Cancellations, corrections, and reversals must be matched to the original by message sequence number. The rules differ before and after FINRA's February 2012 re-platform (Dick-Nielsen 2009, 2014).
- *Double counting.* An inter-dealer trade is reported by both sides, and agency trades can print twice.
- *Fat fingers.* Decimal shifts (1012.5 for 101.25) and one-print spikes that bounce back need explicit screens.
- *Two clocks.* Execution time and report time differ. A late report on a block is information in itself.
- *Settlement.* US corporates settle T+1 since May 28, 2024. Accrue interest to settlement date.

**Used in.** Chapters 2, 3, 7, 8, 9, 18, 19, 20, 22.

> **Trend Watch. The tape that almost got faster (2018–2026).** FINRA added transparency at the edges. Covered depository institutions began reporting Treasury, agency, and MBS trades on September 1, 2022. The portfolio-trade modifier and 60-minute Treasury reporting arrived May 15, 2023, and USD foreign sovereigns became reportable on November 6, 2023 (TRACE Fact Book 2025). End-of-day transaction data for on-the-run Treasuries began March 25, 2024. The historical corporate lag shrank from 18 months to 6. The core corporate tape, though, went in a circle. One-minute reporting was approved September 20, 2024, never implemented, and replaced on September 16, 2025, by a 15-minute limit plus aggregate allocation reporting. The SEC approved the MSRB's matching rollback the same day (SR-MSRB-2025-01, Release No. 34-103987). Cap increases have been proposed since the SEC Fixed Income Market Structure Advisory Committee's 2018 block-trade pilot recommendation (higher caps, up to \$10mm for IG, with delayed dissemination), but they have not changed the public tape. **Desk implication:** the 15-minute window and the caps are the information asymmetry your market-making model prices (Chapter 18). Treat both as fixed until a rule changes them. Keep the PT flag as a feature, because PT prints are priced as part of a basket, not bond by bond (Chapter 19).

## B.2 SEC EDGAR: The Legal Prose Warehouse

**What it is.** The SEC's filing system, holding 10-K and 10-Q financials (with XBRL), 8-K event disclosures, and the debt contracts filed as exhibits.

**Access & cost.** Free. The `data.sec.gov` APIs "do not require any authentication or API keys to access" (<https://www.sec.gov/edgar/sec-api-documentation>). `CIK##########` below is the zero-padded 10-digit CIK.
- Submissions: `https://data.sec.gov/submissions/CIK##########.json` ("typical processing delay of less than a second").
- Company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`. Company concept: `.../api/xbrl/companyconcept/CIK##########/us-gaap/<Tag>.json`.
- Frames: `https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json`. Periods are written `CY2019` (annual), `CY2019Q1` (quarterly), and `CY2019Q1I` (instantaneous).
- Bulk files `companyfacts.zip` and `submissions.zip` are rebuilt nightly (around 3:00 a.m. ET). Use them for any large pull.

XBRL endpoints usually lag under a minute. There is no CORS support, so run your code server-side. Fair-access rules (<https://www.sec.gov/os/accessing-edgar-data>): "Current max request rate: 10 requests/second," and every request must carry a declared User-Agent of the form `Sample Company Name AdminContact@<sample company domain>.com`.

**Full-text search** (<https://www.sec.gov/edgar/search/efts-faq.html>) covers all electronic filings "since 2001," including "all attachments (such as exhibits)." It supports exact phrases, `OR`, `NOT`, `NEAR(n)` (default 10 words), and trailing wildcards. The JSON endpoint behind it on `efts.sec.gov` is undocumented, so assume it can change. This is the tool for a J.Crew-blocker screen: every exhibit since 2018 with *unrestricted subsidiary* within five words of *intellectual property* (Chapter 13).

**Credit-document exhibits** (Regulation S-K Item 601, <https://www.law.cornell.edu/cfr/text/17/229.601>): **EX-4** (indentures, supplemental indentures); **EX-10** ("every contract not made in the ordinary course of business that is material," which includes credit agreements, amendments, intercreditors, and joinders, usually attached to an 8-K under Item 1.01 or 2.03, or to a 10-Q); **EX-21** (subsidiaries, your starting point for the restricted/unrestricted map).

**Gotchas.**
- *The 10% hole.* Long-term debt that "does not exceed 10 percent of the total assets of the registrant and its subsidiaries on a consolidated basis" need not be filed (Item 601(b)(4)(iii)(A)).
- *Redactions.* Schedules may be omitted if they are listed (Item 601(a)(5)). Terms that are "both not material and is the type that the registrant treats as private or confidential" may be redacted (Item 601(b)(10)(iv)). Pricing grids often show up as `[***]`, so give your parser a redaction token.
- *Private issuers.* Issuers whose debt is 144A-for-life file nothing. Their documents sit in lender data rooms, on the private side.
- *XBRL look-ahead.* Frames returns, for each entity, the fact "that is last filed," so restatements overwrite originals. Rebuild point-in-time values from `companyfacts` using each fact's accession number and `filed` date, or better, the acceptance timestamp from submissions. Debt details often sit in custom extension tags that frames won't return.

**Used in.** Chapters 11, 13, 15, 25, 26.

## B.3 CourtListener, RECAP, PACER, and the Claims Agents

**What it is.** PACER is the judiciary's pay-per-page docket system. Free Law Project's CourtListener hosts the **RECAP Archive**, which mirrors PACER documents that users of the RECAP browser extension have already paid for. Claims agents run free case websites with dockets and claims registers.

**Access & cost.**
- **PACER** (<https://pacer.uscourts.gov/pacer-pricing-how-fees-work>): \$0.10 per page, capped at \$3 per document. The cap does not cover search results or reports that aren't case-specific. Audio is \$2.40 a file and opinions are free. Fees are waived in any quarter where you spend \$30 or less. Every docket refresh is billed again, so pull mega-case dockets incrementally with date filters.
- **CourtListener REST API v4** (docs now on the Free Law Project wiki, <https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview>). Base URL `https://www.courtlistener.com/api/rest/v4/`. Authenticate with the header `Authorization: Token <token>`; the docs warn that "a common mistake is to forget the word 'Token'." Current defaults: "authenticated users may make up to 5 requests per minute, 50 requests per hour, and 125 requests per day," on a rolling window, with higher limits available through membership or commercial agreements. Use webhooks for docket alerts rather than polling.
- **RECAP Fetch** (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/recap>): `POST /api/rest/v4/recap-fetch/` with `request_type` 1 (docket), 2 (PDF), or 3 (attachment page). It "uses your PACER credentials to purchase and download PACER content," runs asynchronously, and allows 30 requests a minute. The upload endpoint is "not available to the public."
- **Python.** `juriscraper` (<https://github.com/freelawproject/juriscraper>, BSD-2, Python 3.11+) parses court sites and "a variety of pages and reports within the PACER system."
- **Claims agents.** Stretto (<https://cases.stretto.com/>), Epiq (<https://dm.epiq11.com/>), and Verita Global (<https://www.veritaglobal.com/>), whose CaseView links point to the legacy KCC domain. Kroll Restructuring Administration (formerly Prime Clerk) and Omni Agent Solutions are the other majors; we could not open their sites this session. Agent sites are free, usually update faster than RECAP, and post claims registers in structured form.

**Key fields.** Dockets: court, case number, `pacer_case_id`, filing date, judge, parties, attorneys. Entries: number, date, description, and documents with `pacer_doc_id`. Claims: claim number, creditor, debtor entity, amount, priority (secured, 503(b)(9), priority, GUC), date filed. Rule 2019 statements become a time series of who is in the ad hoc group (Chapter 25).

> **Docket Diary.** A document is in RECAP only if someone with the extension bought it. Coverage is therefore biased toward cases that people with money care about. Mega-case first-day declarations are almost always there. The small-cap Chapter 11 your model actually needs often isn't. *The Ad Hoc Group, represented by counsel, notes that its Rule 2019 statement was amended four times and RECAP holds two of the versions.*

**Gotchas.** Docket text is free-form, so the same motion can carry a dozen different descriptions. Claim amounts are as *asserted*, not as allowed, and duplicate claims filed against several debtor entities inflate the totals. For look-ahead purposes, the right timestamp is when the entry appeared on the docket, not the date printed inside the PDF.

**Used in.** Chapters 13, 14, 16, 25.

## B.4 MSRB EMMA

**What it is.** EMMA (<https://emma.msrb.org/>) is the MSRB's free site for municipal trade data, official statements, continuing disclosures, statistics, and yield curves. Real-time and historical feeds are sold as MSRB subscriptions. Rule G-14 requires reporting to RTRS "as soon as practicable but no later than 15 minutes after the Time of Trade" (<https://www.msrb.org/Rules-and-Interpretations/MSRB-Rules/General/Rule-G-14>). One-minute amendments were approved September 20, 2024, and rescinded September 16, 2025.

**Gotchas.** Munis mask large trade sizes under their own conventions, so check RTRS dissemination rules before reusing TRACE cleaning code. Most issues almost never trade, which makes staleness worse than in HY corporates. A late continuing-disclosure filing is itself a credit signal.

**Used in.** Chapters 12, 22.

## B.5 CME Treasury Futures, MDP 3.0, and BrokerTec

**What it is.** CME lists the Treasury futures used for rate hedging (2-, 5-, and 10-year, Ultra 10-year, Bond, and Ultra Bond). It also owns **BrokerTec**, the inter-dealer central limit order book for cash Treasuries and repo, acquired with NEX Group in 2018. The real-time protocol is **MDP 3.0**: UDP multicast, Simple Binary Encoding (SBE), incremental and snapshot-recovery channels, and market-by-price and market-by-order books. History is sold through CME DataMine. CME's site returned HTTP 503 to automated requests this session, so we give no deep links.

**Access & cost.** Exchange licensing is per device or per enterprise, and an algorithm consuming the feed triggers non-display fees. DataMine is priced per dataset. Many shops buy normalized data rather than decode raw SBE.

**Key fields.** Contract and expiry, book levels and sizes, trades with the aggressor side, sequence numbers, exchange timestamps, settlement prices, and open interest. Add the deliverable basket and conversion factors, which you need for cheapest-to-deliver (CTD) and futures DV01 (Chapters 8, 24).

**Gotchas.** When you see a sequence gap, recover from the snapshot channel; never interpolate across it. Futures DV01 jumps when the CTD changes. Rolls move liquidity between contracts, and back-adjusted series give correct returns but wrong levels. BrokerTec shows only the inter-dealer market. Client flow, which is where the information is, trades on dealer-to-client RFQ platforms.

**Used in.** Chapters 8, 22, 24, 27.

## B.6 OPRA, Cboe, and Options Data

**What it is.** **OPRA** (<https://www.opraplan.com/>) is the securities information processor for US listed options. It disseminates consolidated "last sale and quotation information," volume, open interest, and end-of-day summaries from BOX, Cboe, MEMX, MIAX, Nasdaq, and NYSE options venues. Its 2026 notices add IEX Options and MX2 Options, extend trading hours effective September 21, 2026, and upgrade hardware. **Cboe DataShop** (<https://datashop.cboe.com/>) sells Option EOD Summary (with a 3:45 p.m. ET snapshot), interval Option Quotes, and Option Trades, with optional implied volatility and Greeks and an academic discount. OptionMetrics IvyDB, usually through WRDS, is the academic standard for volatility surfaces.

**Access & cost.** OPRA charges vendor and subscriber fees under its fee schedule. For credit work, a daily or 3:45 p.m. surface snapshot per issuer is enough for Merton/CreditGrades inputs, put-vs-CDS comparisons, and skew-implied jump-to-default (Chapter 23).

**Gotchas.** The options "close" is a quote snapshot, and it isn't synchronized with the equity close, which produces false put-call parity violations. Early exercise and dividends bias naive Black–Scholes implied vols in the deep out-of-the-money puts that carry the default signal. Corporate actions change contract terms.

**Used in.** Chapters 8, 23, 27.

## B.7 Index Data: ICE BofA, Bloomberg, iBoxx/CDX/iTraxx, and FRED

**What it is.**
- **ICE BofA** (<https://www.ice.com/fixed-income-data-services/index-solutions>): "over 6,000" fixed-income indices, including US High Yield (H0A0) and US Corporate (C0A0). ICE says its index history on Snowflake Marketplace spans "50 years."
- **Bloomberg** (the former Lehman/Barclays family): Aggregate, Corporate, High Yield, and the Very Liquid versions. JNK tracks the Bloomberg High Yield Very Liquid Index.
- **iBoxx, CDX, iTraxx** belong to S&P Global since its 2022 merger with IHS Markit. HYG tracks the iBoxx USD Liquid High Yield Index. CDX and iTraxx roll to a new series every six months.
- **FRED** republishes ICE BofA OAS: **BAMLH0A0HYM2** (HY, <https://fred.stlouisfed.org/series/BAMLH0A0HYM2>) and **BAMLC0A0CM** (IG, <https://fred.stlouisfed.org/series/BAMLC0A0CM>). On 2026-10-15 they were 3.23% and 0.84%, i.e., 323 bp and 84 bp (FRED, accessed 2026-10-17). The FRED API (<https://fred.stlouisfed.org/docs/api/fred/>) includes `fred/series/vintagedates` for real-time vintages.

**Access & cost.** Constituent-level data (weights, prices, OAS, duration, ratings by bond) is licensed and expensive. Index-level series are cheaper.

**Gotchas.**
- *Month-end rebalancing.* A bond downgraded mid-month stays in the IG index until the month-end rebalance, and fallen-angel selling clusters on those dates (Chapter 9).
- *Index prices are evaluated, bid-side prices* (§B.8). Index OAS is smoothed, so §B.0 applies.
- *Excess-return definitions differ.* Some families use duration-matched Treasuries, others swaps. Don't mix them in one regression.
- *CDX rolls.* An on-the-run series jumps in level on the roll date, so splice explicitly.
- *FRED is shrinking.* The series notes now say "Starting in April 2026, this series will only include 3 years of observations. For more data, go to the source." They also say "Copyright, 2023, ICE Data Indices. Reproduction of this data in any form is prohibited," and the data is "provided for your internal use only."

**Used in.** Chapters 2, 8, 9, 10, 11, 12, 20.

> **Trend Watch. Free data giveth, and free data taketh away (2018–2026).** In 2018 one line of `pandas-datareader` pulled decades of daily HY OAS from FRED. Since April 2026, FRED keeps three years and sends you "to the source," while ICE sells 50 years of history on Snowflake. CourtListener's default authenticated allowance is now 125 requests a day. Academic open data went the other way. The Open Source Bond Asset Pricing project released TRACE-based panels and factor libraries, with its Stage 1 daily panel in public beta on 2025-12-11, and FINRA's EHD corporate lag fell to 6 months. **Desk implication:** cache everything free in a versioned, point-in-time local store, because free data disappears. License what production depends on. Reconcile the open panels against vendor data so you notice when either one drifts.

## B.8 Composite and Evaluated Pricing: Model Outputs Dressed as Prices

**What it is.**
- **MarketAxess CP+** (<https://www.marketaxess.com/price/cp-plus>) covers IG, HY, EM, loans, munis, sovereigns, and rates. It is built from "proprietary MarketAxess trading activity, TRACE, TraX, and other market signals," including inquiries that never traded. MarketAxess says it prices "80% more bonds than public sources alone," and delivers via FIX API, OMS feeds, and an Excel add-in.
- **Tradeweb Ai-Price** is a machine-learning price for bonds that haven't traded recently, with confidence measures. **Bloomberg BVAL** is an evaluated price with a BVAL Score that grades how much market evidence supports it. **ICE evaluated pricing**, including continuous evaluated pricing, is the incumbent for fund NAVs. Others include S&P Global and LSEG evaluated pricing and BondCliQ quotes. We could not open the Tradeweb, Bloomberg, or ICE pricing pages this session, so read their methodology documents before you depend on them.

**Access & cost.** Enterprise licenses, with limits on redistribution and on how long you may store the data.

**Key fields.** Bid, mid, and ask; timestamp; confidence or score; methodology tier (based on trades vs. based on comparable bonds).

**Gotchas.**
- *Circularity.* Composites are built partly from TRACE. If you train on composite labels with TRACE features, part of what you predict is your own input. Validate on *subsequent* trades (markouts).
- *Staleness.* A bond with no new information follows its comparables, so its $\theta$ sits well above zero. Use the score field to set observation weights.
- *Bid-side NAVs.* Credit ETF NAVs are struck from bid-side evaluated prices. In March 2020, part of the "discount" of HYG and LQD to NAV was the NAV being stale (Chapter 20).
- *Licensing.* Composite contracts often forbid long histories or index-building. Read them before you build a 20-year backtest.

**Used in.** Chapters 7, 18, 19, 20.

> **Trend Watch. Pricing became a product (2018–2026).** Trading venues turned their order-flow data into pricing products (CP+, Ai-Price), and evaluated-pricing vendors sped up their updates. A portfolio trade, flagged in TRACE since May 15, 2023, is priced against composite mids, and the dealer's markup is measured against them (Chapter 19). **Desk implication:** your pricing engine competes with the composites. Log both prices on every RFQ, and show the edge as better markouts on the same trades.

## B.9 Ratings-Agency Default Studies

**What it is.** S&P Global Ratings publishes an annual global corporate default and rating-transition study. Moody's publishes an annual study of corporate default and recovery rates since 1920. Fitch publishes default studies and loan and HY default indices. SEC Rule 17g-7(b) requires rating agencies to publish their rating-action histories in XBRL, with a lag, which gives you free (if awkward) point-in-time ratings.

**Access & cost.** Summaries are often free after registration. Full data and production rating feeds are licensed. The trace-data-pipeline public download leaves out some columns "because agency ratings are licensed."

**Gotchas.** Results depend on how a study handles withdrawn ratings. Distressed exchanges count as defaults (S&P "SD"; Moody's distressed exchanges). In the LMT era that changes the recovery distribution and leads to re-defaults (Chapter 14). Default rates are physical-measure, through-the-cycle numbers. Using them as $\mathbb{Q}$ hazards without a risk premium understates spreads, which is the credit spread puzzle (Chapter 6). Join ratings on publication time, not effective date.

**Used in.** Chapters 5, 6, 11, 14.

## B.10 Academic Bond Panels: OBAP, WRDS Bond Returns, Mergent FISD

**Open Source Bond Asset Pricing** (<https://openbondassetpricing.com/>), run by Alexander Dickerson and coauthors, publishes "108 Bond Factors," 341 factors from *Factor Investing with Delays*, a bond-level ML panel with 341 predictors (2002-07 to 2022-12), duration-matched Treasury returns, and replication packages. Its **trace-data-pipeline** (<https://github.com/Alexander-M-Dickerson/trace-data-pipeline>, MIT license) works in stages. Stage 0 turns Enhanced, Standard, and 144A TRACE into daily panels using Dick-Nielsen (2009, 2014) and van Binsbergen–Nozawa–Schwert (2025) filters, a decimal-shift corrector (10×, 0.1×, 100×, 0.01×), a bounce-back filter, agency de-duplication, and an ultra-distressed flag. Stage 1 adds QuantLib analytics, ratings, and FISD terms. Stage 2 builds 108 monthly signals. Stages 0–1 need WRDS. §B.16 is a teaching-scale version of Stages 0–1.

**WRDS Bond Returns** (<https://wrds-www.wharton.upenn.edu/pages/grid-items/wrds-bond-returns/>) is a monthly panel of prices, returns, coupons, and yields built from TRACE Standard and Enhanced, starting July 2002, with a bond-to-equity link table built through CRSP. Its month-end price rule, meaning which late-month trade counts as the month-end price, moves measured reversal and factor premia. That sensitivity is the subject of Dickerson et al., *The Corporate Bond Factor Replication Crisis*.

**Mergent FISD** (via WRDS) is the academic security master. It holds offering terms, coupon type, maturity, seniority, 144A and convertible flags, call, put, and sink schedules, covenant indicators, and histories of amount outstanding and ratings. **Gotchas:** coverage of small and private issues is patchy. Amount-outstanding updates lag tenders and exchanges, and in an LMT the change in amount outstanding *is* the event. CUSIPs are licensed.

**Used in.** Chapters 7, 9, 10, 11.

## B.11 Leveraged Loans and CLOs

**What it is.** There is no public loan tape. In *Kirschner v. JPMorgan Chase* (2d Cir. 2023), the court held that the syndicated term-loan notes at issue were not securities. The sources you have: the **LSTA** (<https://www.lsta.org/>), which publishes market analysis such as its *BSL Market Monthly* (built on the Morningstar LSTA Leveraged Loan Index), settlement standards, and documentation; PitchBook LCD for new issues and defaults; and dealer-quote mark services such as LSEG's. CLO data comes from Intex (waterfalls), monthly trustee reports (collateral, OC/IC tests, CCC buckets), rating-agency surveillance, and Creditflux's CLO-i. TRACE collects CLO tranche trades but does not disseminate them (§B.1).

**Gotchas.** Loan "prices" are averages of dealer quotes, not trades. Settlement takes days to weeks. Repricings and amend-and-extends change a loan's terms without changing its identifier. Trustee reports arrive monthly and late, so the forced-seller signal from a CCC bucket (Chapter 21) is about a month stale.

**Used in.** Chapters 12, 16, 17, 21.

## B.12 ETF Holdings Files

**What it is.** Under SEC Rule 6c-11 (2019), most US ETFs post full holdings every day. iShares pages include "Download latest fund holdings CSV data." HYG (<https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf>) launched April 4, 2007. SPDR pages offer a daily `.xlsx`. JNK (<https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk>) launched November 28, 2007. The files are free to download, and each sponsor's terms govern redistribution.

**Key fields.** As-of date, name, identifiers (ISIN, sometimes CUSIP), par, market value, weight, price, and sector, plus coupon, maturity, duration, and yield for bond funds. Layouts differ by sponsor, so write one parser per sponsor and test each against a stored sample file.

**Gotchas.** The holdings file is not the creation basket, because custom baskets are allowed (Chapter 20). Each file overwrites the last one. If you don't archive daily, you have no history and every backtest is survivor-biased. Cash, futures, and CDS overlays need special handling. File prices are the sponsor's evaluated prices, not trades.

**Used in.** Chapters 2, 19, 20.

## B.13 CDS Public Data (Brief)

Swap data repositories disseminate index CDS under CFTC rules. Single-name CDS have been disseminated under the SEC's Regulation SBSR since early 2022 *(approximate; check the SBSR compliance schedule)*. Sizes are capped and reference-entity mapping is painful. Use these tapes for activity signals and basis studies (Chapter 24), and buy levels from a vendor.

## B.14 Open-Source Tooling

| Tool | What it does | Verified notes (2026-10-17) |
| :--- | :--- | :--- |
| `edgartools` (<https://github.com/dgunning/edgartools>) | EDGAR filings, XBRL statements, full-text search | MIT; Python 3.11+; call `set_identity("name@example.com")` first; stays within 10 req/s |
| OpenBB Open Data Platform (<https://github.com/OpenBB-finance/OpenBB>) | One data layer for public and licensed providers (Python, REST, MCP) | `pip install openbb`; Apache-2.0; Python 3.10–3.14; `openbb-api` serves on port 6900 |
| `pandas-datareader` (<https://pandas-datareader.readthedocs.io/en/latest/>) | Remote readers, including FRED | 0.11.2 dev build in the docs (July 2026); FRED now returns 3 years for ICE series |
| `juriscraper` | Court and PACER parsing | BSD-2; Python 3.11+ |
| trace-data-pipeline / PyBondLab | TRACE cleaning, analytics, factors | MIT; Stages 0–1 need WRDS |
| `wrds`, `QuantLib`, `fredapi` | WRDS SQL; bond math; FRED client | Not re-verified this session |

> **Ways This Blows Up.** When a provider changes its terms (FRED's window, CourtListener's limits, EDGAR's User-Agent rule), the wrappers break *quietly*. A call that returns three years of OAS where it used to return thirty raises no exception. It just deletes 2008 from your regime model. Assert row counts and date ranges on every pull, and fail the job if history shrinks.

## B.15 Case Study: A Fallen Angel Through Every Lens

Here is what a fallen angel looks like as data, using the synthetic bond `SYN-IG-B` from the code below (all numbers *illustrative*). The rating agency's downgrade from BBB- to BB+ takes effect on June 10 and is published on June 12. On EDGAR, an 8-K Item 2.03 filing earlier in the year attached an amendment as EX-10.1 with its pricing grid redacted. On the TRACE tape, large prints switch from `5MM+` to `1MM+` on June 12, not June 10. A model that joins on effective date "knows" about the cap change two days early. Index data keeps the bond in the IG index until the June month-end rebalance, which is when forced selling clusters. The ETF holdings file shows the IG fund's position disappearing at the rebalance, and the HY fund's holdings file shows the bond showing up the next day. Composites mark it down gradually, because they move with the comparables at a $\theta$ well above zero. Daily returns built from composites understate the move's volatility, and a Dimson-summed beta to HYG recovers it.

The desk's job is to line these five clocks up by `knowledge_ts`. That alignment is a feature in its own right. The gap between the downgrade's knowledge time and the index rebalance is the forced-selling window that Chapters 9 and 20 trade.

## B.16 Specification for AI Implementation: The Tidy Bond Panel

**The Spec You Hand the Robot.** *What ROBO built from the vague version ("make me a daily bond price table"):* it took the last trade of each day and forward-filled across holidays and weekends. It dropped the defaulted bond because its yield failed to solve. It joined ratings on effective date. Every one of those choices ships a bias into production. Here is the precise version.

| Table | Key | Required columns (units) | Rules |
| :--- | :--- | :--- | :--- |
| `secmaster` | `bond_id` | coupon (decimal), maturity, offering_amt (\$ par), security_level, rule_144a, freq, day_count | One row per bond; IDs are synthetic in tests, CUSIPs in production (licensed) |
| `ratings` | (`bond_id`, `knowledge_ts`) | effective_ts, knowledge_ts, rating, rating_num (1 = AAA … 22 = D) | As-of join on `knowledge_ts` only |
| `msgs` | `msg_seq` | trc_st ∈ {T, X, C}, orig_msg_seq, exec_ts, report_ts, price (% of par), qty_true (\$ par), side ∈ {B, S, D} | Simplified status codes; map FINRA's real codes per vintage (pre/post 2012) |
| `trades` | `msg_seq` | + rating at trade, cap, qty_dissem, qty_capped, flags | No cancelled or corrected originals; screens for decimal shifts and bounce-backs |
| `daily` | (`bond_id`, `date`) | px_clean, px_vwap_dissem, n_trades, par_volume, days_stale, is_stale, status, accrued, ytm, dur_mod, spread (decimal), dts (yr·bp) | Full business-day grid until maturity; defaulted bonds kept, flagged `trades_flat` |
| `monthly` | (`bond_id`, `month_end`) | px_eom, accrued, cpn_paid, ret_total | Month-end price only if `days_stale` ≤ 5; else NaN, never filled |

Edge cases the code must handle: settlement on T+1 business day; 30/360 accrual to settlement; flat trading (zero accrued, no yield) after default; caps keyed to point-in-time rating; Brent bracket of $[-5\%, 500\%]$ for distressed yields. Sanity checks: price–yield round trip to $10^{-8}$; analytic vs. finite-difference duration to $10^{-6}$; a par bond priced on a coupon date equals 100; and a Monte Carlo check of the §B.0 result $\operatorname{Var}(r^o)/\sigma^2=(1-\theta)/(1+\theta)$, $\rho_1=\theta$. The spread is a curve-interpolated G-spread against an *illustrative* Nelson–Siegel curve, not OAS. Requires pandas ≥ 2.2.

```python
# Tidy bond panel from a synthetic TRACE-like tape. Bond ids are synthetic labels, NOT CUSIPs.
import numpy as np
import pandas as pd
from scipy.optimize import brentq

RNG = np.random.default_rng(20261017)
IG_CAP, HY_CAP = 5_000_000, 1_000_000          # dissemination caps (par $)
RATING_SCALE = {"AAA": 1, "AA+": 2, "AA": 3, "AA-": 4, "A+": 5, "A": 6, "A-": 7,
                "BBB+": 8, "BBB": 9, "BBB-": 10, "BB+": 11, "BB": 12, "BB-": 13,
                "B+": 14, "B": 15, "B-": 16, "CCC+": 17, "CCC": 18, "CCC-": 19,
                "CC": 20, "C": 21, "D": 22}
IG_MAX_NUM = RATING_SCALE["BBB-"]

# ---------------------------------------------------------------- 1. security master
secmaster = pd.DataFrame({
    "bond_id":        ["SYN-IG-A", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D"],
    "issuer_id":      ["ISS1", "ISS2", "ISS3", "ISS4"],
    "coupon":         [0.0450, 0.0525, 0.07875, 0.0950],
    "maturity":       pd.to_datetime(["2033-06-15", "2031-03-01", "2030-09-15", "2029-12-01"]),
    "offering_date":  pd.to_datetime(["2023-06-15", "2021-03-01", "2022-09-15", "2021-12-01"]),
    "offering_amt":   [1_500_000_000, 750_000_000, 600_000_000, 400_000_000],
    "security_level": ["SEN", "SEN", "SEN", "SUB"],
    "rule_144a":      [False, False, True, False],
    "freq":           [2, 2, 2, 2],
    "day_count":      ["30/360"] * 4,
})

# ------------------------------------------------- 2. point-in-time ratings history
# join on knowledge_ts (publication), never effective_ts
ratings = pd.DataFrame({
    "bond_id":      ["SYN-IG-A", "SYN-IG-B", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D", "SYN-HY-D"],
    "effective_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-10", "2022-09-01",
                                    "2021-11-20", "2026-08-14"]),
    "knowledge_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-12", "2022-09-01",
                                    "2021-11-20", "2026-08-17"]),
    "rating":       ["A-", "BBB-", "BB+", "B", "CCC", "D"],
})
ratings["rating_num"] = ratings["rating"].map(RATING_SCALE).astype("int64")
DEFAULT_DATE = {"SYN-HY-D": pd.Timestamp("2026-08-14")}

# ------------------------------------------------------------- 3. bond math (30/360)
def d30360(d1, d2):
    """US 30/360 (bond basis) day count between two Timestamps."""
    D1 = min(d1.day, 30)
    D2 = d2.day
    if D2 == 31 and D1 >= 30:
        D2 = 30
    return 360 * (d2.year - d1.year) + 30 * (d2.month - d1.month) + (D2 - D1)

def coupon_dates(maturity, freq=2, start=None):
    months = 12 // freq
    out, d, k = [], maturity, 0
    while start is None or d > start - pd.DateOffset(months=months):
        out.append(d)
        k += 1
        d = maturity - pd.DateOffset(months=months * k)
        if start is None and k > 400:
            break
    return sorted(out)

def schedule(settle, maturity, freq=2):
    """(previous coupon date, list of future coupon dates) relative to settle."""
    dates = coupon_dates(maturity, freq, start=settle)
    future = [d for d in dates if d > settle]
    past = [d for d in dates if d <= settle]
    prev = past[-1] if past else future[0] - pd.DateOffset(months=12 // freq)
    return prev, future

def accrued(settle, maturity, coupon, freq=2):
    prev, _ = schedule(settle, maturity, freq)
    return 100.0 * coupon / freq * d30360(prev, settle) / (360.0 / freq)

def dirty_from_yield(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)          # fraction of period to next coupon
    k = np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    return float(np.sum(cf / (1.0 + y / freq) ** (w + k)))

def clean_from_yield(y, settle, maturity, coupon, freq=2):
    return dirty_from_yield(y, settle, maturity, coupon, freq) - accrued(settle, maturity, coupon, freq)

def yield_from_clean(p_clean, settle, maturity, coupon, freq=2):
    f = lambda y: clean_from_yield(y, settle, maturity, coupon, freq) - p_clean
    return brentq(f, -0.05, 5.0, xtol=1e-12)              # bracket: -5% to 500%

def mod_duration(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)
    n = w + np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    pv = cf / (1.0 + y / freq) ** n
    macaulay_years = np.sum((n / freq) * pv) / np.sum(pv)
    return float(macaulay_years / (1.0 + y / freq))

def tsy_curve(T, b0=0.042, b1=-0.005, b2=0.010, tau=2.0):
    """Synthetic Nelson-Siegel par curve (illustrative), bond-equivalent decimal."""
    T = np.maximum(np.asarray(T, dtype=float), 1e-6)
    x = T / tau
    return b0 + b1 * (1 - np.exp(-x)) / x + b2 * ((1 - np.exp(-x)) / x - np.exp(-x))

# ----------------------------------------------- 4. simulate "true" paths and a tape
bdays = pd.bdate_range("2026-03-02", "2026-09-30")
y0 = {"SYN-IG-A": 0.0480, "SYN-IG-B": 0.0590, "SYN-HY-C": 0.0760, "SYN-HY-D": 0.1350}
vol = {"SYN-IG-A": 0.0006, "SYN-IG-B": 0.0010, "SYN-HY-C": 0.0020, "SYN-HY-D": 0.0060}
lam = {"SYN-IG-A": 6.0, "SYN-IG-B": 4.0, "SYN-HY-C": 2.0, "SYN-HY-D": 1.5}
half_spread = {"SYN-IG-A": 0.10, "SYN-IG-B": 0.20, "SYN-HY-C": 0.40, "SYN-HY-D": 1.00}

rows, seq = [], 0
for _, b in secmaster.iterrows():
    y = y0[b.bond_id]
    for d in bdays:
        y += vol[b.bond_id] * RNG.standard_normal()
        if b.bond_id == "SYN-IG-B" and d >= pd.Timestamp("2026-06-10"):
            y += 0.0004                                   # fallen-angel drift
        settle = d + pd.offsets.BDay(1)                   # US corporates settle T+1
        defaulted = b.bond_id in DEFAULT_DATE and d >= DEFAULT_DATE[b.bond_id]
        if defaulted:
            true_px = 31.0 + 2.0 * RNG.standard_normal()  # trades flat near recovery
        else:
            true_px = clean_from_yield(max(y, 0.0), settle, b.maturity, b.coupon)
        for _ in range(RNG.poisson(lam[b.bond_id] * (2.0 if defaulted else 1.0))):
            side = RNG.choice(["B", "S", "D"], p=[0.4, 0.4, 0.2])   # cust buy/sell, dealer
            sgn = {"B": 1.0, "S": -1.0, "D": 0.0}[side]
            px = round(true_px + sgn * half_spread[b.bond_id] + 0.05 * RNG.standard_normal(), 3)
            median_qty = 1_000_000 if b.bond_id.startswith("SYN-IG") else 500_000
            qty = float(np.clip(np.round(RNG.lognormal(np.log(median_qty), 1.0), -3), 1_000, 25_000_000))
            exec_ts = d + pd.Timedelta(hours=9, minutes=30) + pd.Timedelta(seconds=int(RNG.integers(0, 6.5 * 3600)))
            seq += 1
            rows.append(dict(msg_seq=seq, orig_msg_seq=np.nan, trc_st="T", bond_id=b.bond_id,
                             exec_ts=exec_ts, report_ts=exec_ts + pd.Timedelta(seconds=int(RNG.integers(1, 900))),
                             price=px, qty_true=qty, side=side))
msgs = pd.DataFrame(rows)

# inject tape pathologies: cancels, corrections, a decimal shift, a bounce-back print
t_idx = msgs.index[msgs.trc_st == "T"]
cancel_targets = RNG.choice(t_idx, size=6, replace=False)
fix_targets = RNG.choice(np.setdiff1d(t_idx, cancel_targets), size=6, replace=False)
extra = []
for i in cancel_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="X")
    extra.append(r)
for i in fix_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="C", price=round(r["price"] + 0.25, 3))
    extra.append(r)
msgs = pd.concat([msgs, pd.DataFrame(extra)], ignore_index=True)
ig_a = msgs.index[(msgs.bond_id == "SYN-IG-A") & (msgs.trc_st == "T")]
msgs.loc[ig_a[100], "price"] *= 10.0                      # decimal-shift typo
msgs.loc[ig_a[200], "price"] += 7.0                       # bounce-back spike
msgs["orig_msg_seq"] = msgs["orig_msg_seq"].astype("Int64")

# ------------------------------- 5. point-in-time rating join (no look-ahead allowed)
def pit_rating(df, ts_col):
    left = df.sort_values(ts_col)
    right = ratings.sort_values("knowledge_ts")[["bond_id", "knowledge_ts", "rating", "rating_num"]]
    out = pd.merge_asof(left, right, left_on=ts_col, right_on="knowledge_ts", by="bond_id",
                        direction="backward", allow_exact_matches=True)
    assert (out["knowledge_ts"] <= out[ts_col]).all(), "look-ahead in rating join"
    return out

# --------------------------------------------- 6. clean the tape (Dick-Nielsen-lite)
def clean_tape(m):
    m = m.copy()
    cancelled = set(m.loc[m.trc_st == "X", "orig_msg_seq"].dropna().astype(int))
    corrected = set(m.loc[m.trc_st == "C", "orig_msg_seq"].dropna().astype(int))
    keep = (m.trc_st.isin(["T", "C"])) & ~m.msg_seq.isin(cancelled | corrected)
    t = m.loc[keep].copy()
    t = t.sort_values(["bond_id", "exec_ts"]).reset_index(drop=True)
    # decimal-shift and bounce-back screens against a rolling median of neighbours
    med = t.groupby("bond_id")["price"].transform(lambda s: s.rolling(11, center=True, min_periods=3).median())
    ratio = t["price"] / med
    t["flag_decimal"] = (ratio > 5) | (ratio < 0.2)
    prev_ = t.groupby("bond_id")["price"].shift(1)
    next_ = t.groupby("bond_id")["price"].shift(-1)
    jump_out = (t["price"] - prev_).abs()
    jump_back = (next_ - t["price"]).abs()
    t["flag_bounce"] = (jump_out > 3.0) & (jump_back > 3.0) & ((next_ - prev_).abs() < 1.0) & ~t["flag_decimal"]
    t = t.loc[~(t.flag_decimal | t.flag_bounce)].copy()
    # point-in-time rating -> dissemination cap the public tape would have shown
    t = pit_rating(t, "exec_ts")
    t["cap"] = np.where(t["rating_num"] <= IG_MAX_NUM, IG_CAP, HY_CAP)
    t["qty_dissem"] = np.minimum(t["qty_true"], t["cap"])
    t["qty_capped"] = t["qty_true"] > t["cap"]
    t["date"] = t["exec_ts"].dt.normalize()
    return t

trades = clean_tape(msgs)

# ------------------------------------------------ 7. bond-day panel on a full grid
def vwap(g, qty_col):
    return float(np.sum(g["price"] * g[qty_col]) / np.sum(g[qty_col]))

agg = (trades.groupby(["bond_id", "date"])
       .apply(lambda g: pd.Series({
           "px_vwap_true": vwap(g, "qty_true"),
           "px_vwap_dissem": vwap(g, "qty_dissem"),
           "px_last": g.sort_values("exec_ts")["price"].iloc[-1],
           "n_trades": len(g),
           "par_volume": g["qty_true"].sum(),
           "n_capped": int(g["qty_capped"].sum()),
           "cust_buy_par": g.loc[g.side == "B", "qty_true"].sum(),
           "cust_sell_par": g.loc[g.side == "S", "qty_true"].sum(),
       }), include_groups=False)
       .reset_index())

grid = pd.MultiIndex.from_product([secmaster.bond_id, bdays], names=["bond_id", "date"]).to_frame(index=False)
daily = grid.merge(agg, on=["bond_id", "date"], how="left").merge(secmaster, on="bond_id", how="left")
daily = daily.loc[daily["date"] < daily["maturity"]].copy()      # never drop defaulted bonds
daily = daily.sort_values(["bond_id", "date"]).reset_index(drop=True)
daily["traded"] = daily["n_trades"].fillna(0).astype("int64") > 0
daily["n_trades"] = daily["n_trades"].fillna(0).astype("int64")
daily["par_volume"] = daily["par_volume"].fillna(0.0)
daily["last_trade_date"] = daily["date"].where(daily["traded"])
daily["last_trade_date"] = daily.groupby("bond_id")["last_trade_date"].ffill()
daily["px_clean"] = daily.groupby("bond_id")["px_vwap_true"].ffill()          # carried price
daily["days_stale"] = [np.busday_count(l.date(), d.date()) if pd.notna(l) else np.nan
                       for l, d in zip(daily["last_trade_date"], daily["date"])]
daily["days_stale"] = daily["days_stale"].astype("float64")
daily["is_stale"] = daily["days_stale"] > 0
daily["status"] = np.where([b in DEFAULT_DATE and d >= DEFAULT_DATE[b] for b, d in zip(daily.bond_id, daily.date)],
                           "defaulted", "performing")
daily["trades_flat"] = daily["status"].eq("defaulted")
daily = pit_rating(daily, "date").sort_values(["bond_id", "date"]).reset_index(drop=True)

def analytics(r):
    if pd.isna(r.px_clean):
        return pd.Series({"accrued": np.nan, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    settle = r.date + pd.offsets.BDay(1)
    ai = 0.0 if r.trades_flat else accrued(settle, r.maturity, r.coupon)
    if r.trades_flat:                                   # yields are meaningless once flat
        return pd.Series({"accrued": ai, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    y = yield_from_clean(r.px_clean, settle, r.maturity, r.coupon)
    dmod = mod_duration(y, settle, r.maturity, r.coupon)
    T = (r.maturity - settle).days / 365.25
    ty = float(tsy_curve(T))
    s = y - ty
    return pd.Series({"accrued": ai, "ytm": y, "dur_mod": dmod, "tsy_yld": ty, "spread": s,
                      "dts": dmod * s * 1e4})          # DTS in years x bp
daily = pd.concat([daily, daily.apply(analytics, axis=1)], axis=1)

# ------------------------------------------- 8. monthly returns (stale-aware rule)
def monthly_returns(dp, max_stale_days=5):
    d = dp.copy()
    d["month_end"] = d["date"] + pd.offsets.BMonthEnd(0)
    me = d.loc[d["date"] == d["month_end"]].copy()
    ok = me["days_stale"] <= max_stale_days
    me["px_eom"] = np.where(ok, me["px_clean"], np.nan)
    me = me.sort_values(["bond_id", "month_end"])
    me["px_prev"] = me.groupby("bond_id")["px_eom"].shift(1)
    me["ai_prev"] = me.groupby("bond_id")["accrued"].shift(1)
    # coupon paid in (prev, this]: detected by an accrued-interest reset (approximation)
    me["cpn_paid"] = np.where((me["accrued"] < me["ai_prev"]) & ~me["trades_flat"],
                              100.0 * me["coupon"] / me["freq"], 0.0)
    me["ret_total"] = (me["px_eom"] + me["accrued"] + me["cpn_paid"]) / (me["px_prev"] + me["ai_prev"]) - 1.0
    return me[["bond_id", "month_end", "px_eom", "accrued", "cpn_paid", "ret_total",
               "days_stale", "rating", "status", "spread", "dur_mod", "dts"]].reset_index(drop=True)

monthly = monthly_returns(daily)

# --------------------------------------------------------- 9. schema + sanity checks
DAILY_SCHEMA = {"bond_id": "str", "date": "datetime", "px_clean": "float",
                "px_vwap_dissem": "float", "n_trades": "int", "par_volume": "float",
                "days_stale": "float", "is_stale": "bool", "rating": "str",
                "rating_num": "int", "status": "str", "accrued": "float",
                "ytm": "float", "dur_mod": "float", "spread": "float", "dts": "float"}
KIND_CHECK = {"str": pd.api.types.is_string_dtype, "datetime": pd.api.types.is_datetime64_any_dtype,
              "float": pd.api.types.is_float_dtype, "int": pd.api.types.is_integer_dtype,
              "bool": pd.api.types.is_bool_dtype}
for col, kind in DAILY_SCHEMA.items():
    assert col in daily.columns, f"missing column {col}"
    assert KIND_CHECK[kind](daily[col]), f"{col}: dtype {daily[col].dtype} is not {kind}"
assert not daily.duplicated(["bond_id", "date"]).any(), "panel key not unique"
assert (daily["date"] < daily["maturity"]).all()
assert "SYN-HY-D" in set(monthly.loc[monthly.status == "defaulted", "bond_id"]), "survivorship: defaulted bond dropped"
# no cancelled or corrected originals survive
dead = set(msgs.loc[msgs.trc_st.isin(["X", "C"]), "orig_msg_seq"].dropna().astype(int))
assert not trades["msg_seq"].isin(dead).any()
assert not trades["price"].gt(200).any(), "decimal-shift print survived"
# price-yield round trip and duration vs finite difference
s0, m0, c0 = pd.Timestamp("2026-04-15"), pd.Timestamp("2031-03-01"), 0.0525
y_rt = yield_from_clean(97.25, s0, m0, c0)
assert abs(clean_from_yield(y_rt, s0, m0, c0) - 97.25) < 1e-8
h = 1e-6
fd = -(dirty_from_yield(y_rt + h, s0, m0, c0) - dirty_from_yield(y_rt - h, s0, m0, c0)) / (2 * h) / dirty_from_yield(y_rt, s0, m0, c0)
assert abs(fd - mod_duration(y_rt, s0, m0, c0)) < 1e-6
# par bond on a coupon date prices at par
assert abs(clean_from_yield(0.0525, pd.Timestamp("2026-03-01"), m0, c0) - 100.0) < 1e-9
# fallen angel: the cap switches from $5mm to $1mm once the downgrade is KNOWN
fa = trades.loc[trades.bond_id == "SYN-IG-B"]
assert (fa.loc[fa.exec_ts < "2026-06-12", "cap"] == IG_CAP).all()
assert (fa.loc[fa.exec_ts >= "2026-06-13", "cap"] == HY_CAP).all()
# stale-price theorem check: EWMA smoothing shrinks variance by (1-theta)/(1+theta)
theta, n = 0.6, 400_000
r = RNG.standard_normal(n)
ro = np.empty(n); ro[0] = (1 - theta) * r[0]
for i in range(1, n):
    ro[i] = theta * ro[i - 1] + (1 - theta) * r[i]
var_ratio = ro[1000:].var() / r[1000:].var()
rho1 = np.corrcoef(ro[1001:], ro[1000:-1])[0, 1]
assert abs(var_ratio - (1 - theta) / (1 + theta)) < 0.01 and abs(rho1 - theta) < 0.01

print(f"messages={len(msgs)}, clean trades={len(trades)}, capped prints={int(trades.qty_capped.sum())}")
print(f"daily panel rows={len(daily)}, stale share={daily.is_stale.mean():.1%}")
print(f"var ratio={var_ratio:.4f} (theory {(1-theta)/(1+theta):.4f}), rho1={rho1:.4f}")
print(monthly.to_string(index=False, float_format=lambda v: f"{v:.4f}"))
```

## B.17 Desk Debrief

- **Every price has a clock.** Store `exec_ts`, `report_ts`, and `knowledge_ts` separately, and join only on knowledge.
- **Staleness hides risk; it doesn't remove it.** Observed variance shrinks by $(1-\theta)/(1+\theta)$, and summing lagged betas brings the full beta back.
- **The public TRACE tape is censored** at \$5mm IG and \$1mm HY. The cap follows the bond's point-in-time rating.
- **The 15-minute window survived.** One-minute reporting was approved in 2024 and abandoned in 2025, for both TRACE and the MSRB.
- **EDGAR misses the 10% hole, the redactions, and every 144A-for-life issuer.** Your covenant model has a coverage map whether you draw it or not.
- **Free data shrinks.** FRED's ICE series now keep 3 years and CourtListener allows 125 requests a day by default. Cache, version, and assert row counts.
- **Composites are model outputs.** Validate against later trades, never against themselves.
- **IDO or it didn't happen**, and IDO on stale prices didn't happen either.

**The Spec You Hand the Robot (summary).** "Build `daily` on a full business-day grid per bond until maturity. Never drop defaulted bonds; flag them `trades_flat`. Clean messages by matching X and C records to originals by `orig_msg_seq`. Join ratings by `merge_asof` on `knowledge_ts` and assert there is no look-ahead. Compute caps from point-in-time ratings. Carry prices forward only with an explicit `days_stale`, and leave a month-end return as NaN when `days_stale` > 5. Enforce dtypes by kind, keep keys unique, and pass the price–yield, duration, par, and staleness checks, or fail the build."

**Exercises.**
1. Estimate $\theta$ for each bond in `daily` from $\rho_1$ of returns on days with trades. Compare it with the variance-ratio estimate. Which one is more robust when trading days are irregular?
2. Fit a Pareto tail to `qty_true` above \$1mm for HY prints. Impute sizes for `1MM+` prints and measure the bias you remove from a capped VWAP.
3. Using the EDGAR full-text syntax, write a query for 8-K exhibits that pair "unrestricted subsidiary" with "intellectual property," and list three ways it gives false positives.
4. Kaz insists the frames API is fine for backtests "because restatements are rare." Design a test that measures how often a `companyfacts` value for a debt tag changes between its first and last `filed` date.
5. ROBO keeps refreshing a 6,000-entry docket on PACER every hour. Estimate the quarterly PACER bill and redesign the job around CourtListener webhooks and claims-agent sites.

### Deep-Dive Resource Graph

**Podcasts.** Bloomberg's *Odd Lots* (market-structure, TRACE, and portfolio-trading episodes); *Flirting with Models* (Corey Hoffstein) on systematic data hygiene.

**Practitioner Writing.** Matt Levine, *Money Stuff* (on bond-market transparency and the "price" of untraded bonds); MarketAxess TraX and CP+ research; Free Law Project's CourtListener documentation (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview>).

**Academic Papers.** Dick-Nielsen (2009), *Liquidity Biases in TRACE*; Dick-Nielsen (2014), *How to Clean Enhanced TRACE Data*; Dimson (1979), *Risk Measurement When Shares Are Subject to Infrequent Trading*; Getmansky, Lo & Makarov (2004), *An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns*; Edwards, Harris & Piwowar (2007), *Corporate Bond Market Transaction Costs and Transparency*; Bessembinder, Kahle, Maxwell & Xu (2009), *Measuring Abnormal Bond Performance*; Bai, Bali & Wen (2019), *Common Risk Factors in the Cross-Section of Corporate Bond Returns*; Dickerson, Mueller & Robotti (2023), *Priced Risk in Corporate Bonds*; Dickerson, Robotti & Rossetti, *The Corporate Bond Factor Replication Crisis* (working paper).

**Data & Code.** FINRA TRACE historic and academic data (<https://www.finra.org/filing-reporting/trace/historic-academic-data>); FINRA Rules 6730 and 6750 (<https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730>, <https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750>); SEC EDGAR APIs (<https://www.sec.gov/edgar/sec-api-documentation>) and fair access (<https://www.sec.gov/os/accessing-edgar-data>); RECAP Fetch (<https://wiki.free.law/c/courtlistener/help/api/rest/v4/recap>); PACER fees (<https://pacer.uscourts.gov/pacer-pricing-how-fees-work>); EMMA (<https://emma.msrb.org/>); OPRA (<https://www.opraplan.com/>); Cboe DataShop (<https://datashop.cboe.com/>); FRED HY OAS (<https://fred.stlouisfed.org/series/BAMLH0A0HYM2>); OBAP (<https://openbondassetpricing.com/>) and its pipeline (<https://github.com/Alexander-M-Dickerson/trace-data-pipeline>); WRDS Bond Returns (<https://wrds-www.wharton.upenn.edu/pages/grid-items/wrds-bond-returns/>); edgartools (<https://github.com/dgunning/edgartools>); OpenBB (<https://github.com/OpenBB-finance/OpenBB>).


---

