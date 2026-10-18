# Preface: Read the Credit Agreement, Then Take the Derivative

At 2:58 p.m. on a Friday, three weeks into his new job, Theo Marsh gets a request for quote. A client wants a bid on \$15 million of a single-B bond issued by a company whose lender call is on Monday. Theo knows this company. In a previous life he read its credit agreement twice, in a conference room, over cold Thai food, and he can still tell you the Available Amount basket's starting dollar amount and which section of Article VII lets the sponsor move the crown-jewel subsidiary out of the collateral package. He also knows that the person on the other end of this RFQ might know all of that too. Or might be a mutual fund rebalancing into month-end. He has three seconds to decide. His old job gave him three weeks.

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

## Four seats through the book

Eight parts, twenty-eight numbered chapters, the lettered chapters that sit beside them (4-B, 6-B, 7-B, 12-B and others), Appendices A through F, and growing. You do not have to read it in order, and where you are going matters more than which tribe you came from, so the paths below are seats. The tribe only decides which primers you skim. The four primers build, once, the tools that later chapters borrow: 4-B (bond price, spread and DV01), 6-B (options, jump-to-default and the two probability measures), 7-B (regression, survival analysis, shrinkage, PCA and the bootstrap) and 12-B (documents, liens and Chapter 11 as a state machine).

The banker enters through Chapter 3, which is written for you; its RSSG Edge Ledger inventories what you bring to the new desk. Take the primers before the chapters that borrow them, in the order 4-B, 5, 6, 6-B, 7-B, 12-B, because Chapters 13–15 use survival analysis, Beta regression and option payoffs that those chapters build. The quant starts with Chapter 3 to see what the other tribe knows, may skim 4-B, 6-B and 7-B, and reads 12-B whatever else gets skipped: it is the one primer written in a language the quant does not yet speak.

**Seat 1: the market maker.** Read Part I straight through, 4-B included, then Chapter 8 with its companions 8-B (the risk model you run every morning) and 8-C (the morning explain). Part V (Chapters 18–22) is your home turf. Notice where credit departs from what Avellaneda–Stoikov assumed: jump-to-default, RFQs instead of order books, bonds that have not traded in nine days.

**Seat 2: the systematic high-yield or investment-grade PM.** Part II is your toolbox, with 6-B and 7-B behind Chapters 6 and 7. It will mostly be review for a quant, but Chapter 5's treatment of recovery distributions and Chapter 7's issuer-grouped cross-validation contain the traps that have been quietly eating your Sharpe ratio. Then Part III (Chapters 8–12), and Part VIII, which is yours. Read 12-B before Part IV, and Part IV last, slowly.

**Seat 3: the event and distressed quant.** The route is Part I, then 4-B, 5, 6, 6-B, 7-B and 12-B, then Part IV (Chapters 13–17), which is the banker's home turf with the numbers attached: liability management transactions as game theory, the default cycle as a regime shift, change-of-control puts as options, post-reorg equity as forced-seller flow, and private credit as the thing eating your old job. Chapter 12-C, which prices plan value, sits right behind 12-B. The quant should then read Chapter 13 and Chapter 25 back to back: the first is what an uptier does to your return distribution, the second is how to parse the document that permitted it. If you came from banking, you will be tempted to skip Chapter 6 because someone once told you that Merton models do not work in distressed credit. That person was half right, and the half they were wrong about is where the money is.

**Seat 4: risk and strat.** 4-B, 6-B and 7-B are yours to live in. Then 8-B and 8-C, Chapter 22 (regulation and the forces reshaping liquidity), Part VI (Chapters 23–24: cross-asset convexity, the volatility surface, the bond–CDS basis) and Chapter 27 (systems). Appendix D is the plumbing reference.

Whatever the seat, come back for the Parts you skipped, including Parts III, V, VI, VII, and VIII where they were not on your route, and keep Appendix A open the whole time.

**The AI-agent specifier reads with a lens rather than a seat.** Read this preface, then Appendix A, then go through every `### Specification for AI Implementation` block in the book in order, starting with Chapters 5–8 (distributions, structural models, labeling, decomposition), then Chapter 13 (the Priming Risk Score), Chapters 18–19 (quoting and basket pricing), and Chapters 25–27 (document parsing, agent workflows, and system architecture). Chapter 26 is the operating manual for directing coding agents and should be read before you direct one. Then go back and read the prose: a spec you do not understand is a spec you cannot debug.

There is also an unofficial path for the reader who is here for the trends: Chapters 2, 4, 10, 14, 17, 21, 22, and 26, each marked TREND in the table of contents, followed by Appendix C, the Trend Tracker.

## The cast

Twenty-eight chapters written by a committee tend to read like twenty-eight chapters written by a committee. So we use a small recurring cast. They are fictional. Every line of dialogue in the book belongs to them. Real firms and real people appear only with verifiable facts attached.

**Theo Marsh** (he/him) is you, or the version of you who is three weeks into a systematic credit desk after years at PJT RSSG. He carries his old 13-week cash flow model on a USB stick "for emotional support." He asks, "But what does the credit agreement say?" He is usually right, which is annoying for everyone else and the reason he was hired.

**Ines Okafor** (she/her) runs credit market making and used to play poker professionally, which she regards as the same job with worse coffee. She frames every problem as a hand: what's the pot, what are the odds, and who at this table knows more than you? She calls markouts "the hand history" and reviews them the way other people review their text messages at 1 a.m.

**Dr. Kasimir "Kaz" Lind** (they/them) holds a PhD in stochastic analysis and builds the desk's models. Kaz is brilliant and has never read a credit agreement. They once asked whether "sacred rights" required a priest. Kaz's opening move in any derivation is "let's just assume Gaussian," and Kaz's second move is regret. You will learn a great deal from watching Kaz be wrong in precise ways.

**Marguerite "Mags" Dunleavy** (she/her) has run distressed money since the 1990s and remembers pricing bonds by phone and by grudge. Her creed: "Price is what you pay. Recovery is what you get, eventually, after the lawyers." She is deeply suspicious of anything called "adjusted," she greets every new technology with a story about how it used to be worse, and she is grudgingly, eventually, impressed.

**ROBO** (it/its) is the AI coding agent Theo specifies work to. ROBO implements exactly what it was asked, which is the problem. Told to "minimize drawdown," it holds cash forever. It never complains and never guesses, and it is therefore the most honest reviewer of a specification you will ever meet. Every "Spec You Hand the Robot" box in this book is an attempt to say something to ROBO that cannot be misread.

**The Ad Hoc Group** is a Greek chorus of lenders, always "represented by counsel." It speaks in unison, mostly in Rule 2019 statements. It forms, it splits, it signs cooperation agreements, and the book keeps a running count of those, because someone should.

A few other things recur on purpose. Theo's 13-week model refuses to die: it comes back as a survival curve in Part II, as a state-space feature in Chapters 3 and 25, as the liquidity-runway variable inside the Priming Risk Score in Chapter 13, and finally as the PM dashboard in Chapter 28. "Open market purchase" is the most expensive three words in finance and will keep showing up until the courts stop making it so. And the desk motto is "IDO or it didn't happen": until you have stripped carry, rates, and factor beta out of a return, you have not found alpha, you have found a benchmark with a hat on.

## How a chapter is built

Every chapter (and most sections) carries six elements in a recognizable order:

1. **Intuitive desk framing.** How a market maker or an RSSG partner sees the problem in plain, ruthless trading terms, usually with the cast in the room.
2. **Rigorous mathematical derivation.** Full equations, step by step, every Greek letter defined, boundary conditions stated, using the single notation table in Appendix A. The joke, if there is one, comes after the load-bearing step, never inside it.
3. **A specification for AI implementation.** A block headed `### Specification for AI Implementation` with data schemas, tensor shapes, edge cases, numerical-stability guards, and a reference implementation in Python (written to run on numpy, scipy, and pandas as given) or a sketch in C++ or Rust where latency matters. It often opens with what ROBO built from the vague version of the request, followed by the precise version.
4. **Source extraction.** Short exact quotations from the fourteen books and papers on our shelf, each cited to a page and followed by a longer annotation on why it matters on a 2026 desk and where the modern desk departs from it.
5. **A deep-dive case study.** Serta, J.Crew, Incora, Carvana, SVB, Hertz, Windstream, March 2020, May 2005: tranches, price paths, dollar values (sourced or marked approximate), and what a systematic desk would have flagged and traded.
6. **A Deep-Dive Resource Graph.** Podcasts, practitioner writing, academic papers, and data and code repositories, grouped, so you can keep going after we stop.

Between those elements you will find a small set of boxes, each with a fixed label: **Desk Myth vs. Desk Reality**, **Poker Table** (game-theory intuition, usually Ines), **Docket Diary** (court process with dates, often with commentary from the Ad Hoc Group), **Ways This Blows Up** (numerical instability, model failure, operational risk), and **Trend Watch**.

Trend Watch boxes deserve a paragraph of their own, because "trend" means two things in this book and we care about both. The first meaning is the structural trends reshaping credit markets: electronification, portfolio trading, ETF-led liquidity, the LMT era, private credit, the regulatory agenda. Every chapter includes at least one Trend Watch box with dated, sourced figures showing how its topic changed over 2018–2026, and Appendix C stitches them into a single timeline. The second meaning is trend as a strategy: time-series momentum in credit indices and excess returns, cross-asset lead–lag, trend combined with carry, and how it behaved in 2008, 2020, and 2022. That gets Chapter 10 to itself and recurs through Parts III and VIII. If a chapter does not tell you what changed and when, we consider it unfinished.

Each chapter opens with a cold-open desk scene and closes with a Desk Debrief (takeaways sharp enough to tape to a monitor), a compact Spec You Hand the Robot, and a few exercises, some of them funny, all of them real.

## A note on how this book is made, and why you should check the build stamp

Honesty requires a disclosure. This book is not written by a person at a desk. It is grown by an autonomous loop of AI agents: a showrunner that keeps the voice and the notation consistent, writer agents assigned to chapters, and advisor agents running on Anthropic's Fable model that research each target (the shelf, the web, the dockets, the papers, the trend data) and hand the writer a brief before a word is written. The loop reads its own state, picks the next most valuable thing to write, writes it, rebuilds the book, updates its notes to itself, and goes again. It never stops on its own. Somebody has to tell it to.

The book therefore ships in **editions**. Edition 1 is the first complete draft of every chapter in the table of contents. Each later edition deepens chapters, adds what the latest research says is missing, and refreshes the Trend Tracker. Because the loop rebuilds the whole text every few hours, the title page carries a build stamp in the subtitle, a date and time in UTC. Please look at it. A trend figure dated 2025 in a build from 2027 is a figure nobody has refreshed yet, and a court ruling described as "pending" may no longer be. Where the agents were unsure they have said so in the text, usually with the word *approximate*, occasionally with a parenthetical that reads like someone leaving a note for their future self, because that is what it is.

Two consequences follow. The book will sometimes repeat itself across chapters, because different agents wrote from the same brief; think of it as spaced repetition until we trim it. And its priorities are, in order, research, net-new writing, growing the table of contents, polish, and only then checking that every code example runs, so a bug can survive an edition. The book gets deeper every cycle rather than prettier, which we think is the right trade for a market that changes this fast. If you find an error, you are almost certainly right; the next edition reads the repository's state notes and continuation prompt.

## The integrity pledge

Because an autonomous loop can generate plausible-looking nonsense at scale, we hold it to rules a human author might get away with bending:

- **Sourced or labeled.** Every historical price, spread, recovery, volume, and dollar amount is either cited to a source or explicitly marked *illustrative* or *approximate*. If a number has neither, it is a bug; treat it as illustrative and tell us.
- **No invented identifiers.** No fabricated CUSIPs, ISINs, SSRN numbers, DOIs, podcast episode numbers, or URLs. Tranches are identified descriptively ("Serta Simmons 2016 First Lien Term Loan due 2023"). A link appears only if it was verified when that passage was written or is a stable canonical root; otherwise you get title, author, and year, and a search engine.
- **No fake quotes.** Real people and firms appear with verifiable facts only. All dialogue belongs to the fictional cast.
- **Code written to run.** Every Python reference implementation is written to execute as given on numpy, scipy, and pandas, with seeded randomness and built-in sanity checks (Monte Carlo against closed form, a waterfall that conserves value, a hazard curve that stays non-negative). Execution checks are a low-priority cleanup pass; the specification around the code is written so that you, or ROBO, can find what survived.
- **Every joke rides on a correct idea.** If a line is funny but wrong, the line goes. If a derivation is correct but dull, we try harder.

Theo is still staring at the RFQ. The clock in the corner of the screen says 2.1 seconds. Turn the page.

<!-- STATUS: COMPLETE -->
