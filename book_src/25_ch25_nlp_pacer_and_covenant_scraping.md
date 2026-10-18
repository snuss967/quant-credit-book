# Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets


## 25.0 Cold Open: Thirty Percent of What?

*A Friday replay on the fictional desk. The dialogue is invented; the dates, docket numbers, holdings and Determinations Committee votes come from the court record and the sources cited in §25.5.2 and §24.8.3. No bond price is quoted, because none is sourced here.*

On the last Friday of October, at the hour when the market-making screens go quiet and Ines runs her replays, she put one PDF on the big monitor and did not say what year it was. Fifty-five pages. A caption from the Southern District of New York: *U.S. Bank N.A. v. Windstream Services, LLC*, No. 1:17-cv-07857, Document 245, filed Friday, 15 February 2019. Somebody had paid PACER for it once, and the RECAP extension had copied it into the free archive (CourtListener docket 6169562), which is how a document from a Friday in 2019 reaches a Friday in 2026 for nothing.

"Normally I stop the tape before the ending," Ines said. "Today you get the ending first. It's the cheapest page in the case."

Theo went straight for the conclusions, because that is what six years of restructuring work teaches a person to do with fifty-five pages and a room: find the part a judge signed. Judge Jesse Furman's Findings of Fact and Conclusions of Law, as the parties' public statements summarized them, came down to three holdings. In substance, the Windstream subsidiaries that had owned the network had sold it and leased it back, and having the parent sign the master lease did not change what had happened. The notes Windstream had issued in November 2017 were not "Additional Notes" under the indenture. And the acceleration of the 6 3/8% senior notes due 2023 stood. Aurelius, the fund on the other side, described the judgment as \$310.5 million plus interest from 23 July 2018.

"So the hedge fund wins," Kaz said. "When did it start winning?"

Mags answered, because she was the one who remembered the 8-K. "April 2015. Windstream spun its copper and fiber into a REIT, the thing that became Uniti, on the twenty-fourth, and leased the network back. Everybody I knew read it as a tax trade. Clever, boring, done." She took the marker. "Then two and a half years of nothing. Then, on 21 September 2017, a notice of default on the six-and-three-eighths."

She wrote the rest as a ledger, one dated line at a time. About \$465mm of the original notes were outstanding, and Aurelius owned roughly 64% of them. On 4 October the credit-derivatives Determinations Committee voted 15 to 0 that no Failure to Pay had occurred. On 12 October the trustee went to court, and that complaint was the docket now on the screen. On 6 November Windstream issued \$553.7mm of new notes and called them Additional Notes of the same series.

"Nobody adds bonds to a series in the middle of a fight about that series," Theo said, "unless they want more votes in it."

"Hold that thought until Furman," Mags said, and kept writing. On 7 December Aurelius accelerated. On 21 December the Committee voted 15 to 0 again, no Failure to Pay, while Windstream disputed the notice in court. Then fourteen months of litigation, and then the PDF.

Kaz had already read ahead to the last line of the case history. "In June 2021 the later appeals were dismissed as 'equitably moot.' Does that mean the judges got bored?"

"It means the company had already been through bankruptcy and come out, money had moved, and unwinding it would hurt people who were never in the room," Mags said. "The court can't unscramble the egg, so it declines to try."

Kaz wrote *equitably moot = too late to unscramble, not bored* on the whiteboard, under *blocker = clause, not person*.

Theo had the 2013 indenture open on his second screen by then, which surprised nobody. "But what does the indenture say?" He scrolled, stopped, scrolled back. "Here's the thing. The covenant itself is short. 'Limitation on Sale and Leaseback Transactions.' All the work is done by the defined term, 'Sale and Leaseback Transaction,' and the defined term turns on *who* transferred the property and *who* is leasing it back. If the who is the parent, because the parent signed the lease, it isn't one. If the who is the subsidiaries that owned the network and still use it, it is. Four years, one defined term, and a pronoun."

"Ten days after the ruling," Mags said, and wrote the last line: 25 February 2019, Chapter 11. "Aurelius won the argument and got a claim against a company in bankruptcy. That's the trouble with winning a covenant fight against a borrower who can't pay. You get to be right in front of a different judge." What the credit-default swaps did in those fourteen months, including the protection that expired inside the gap, is Chapter 24's story (§24.8.3).

Ines wiped everything below the 12 October line. "Now forget the ending. It is Thursday, 12 October 2017. The complaint has just been filed. Everything above this line is public, and nothing below it has happened." She handed out index cards. "Write three things. What the defined term is worth, in dollars. Which way it cuts. And what you do with the 6 3/8% notes."

Kaz wrote a number. Mags wrote a question. Theo wrote the definition out by hand, which took most of the card. Ines collected them unread and put them in her jacket pocket. "We grade these when the desk's parser has read the same indenture (§25.5.2). One more thing. Somebody at that table had read the definition long before the notice went out. By the time it reached a docket, the only people who hadn't looked at their own cards were the ones holding the notes."

*Halyard Holdings is the desk's fictional practice borrower, a sponsor-backed widget maker (Chapter 26); everything in the next scene is invented.*

On Monday at 7:41 a.m. an 8-K landed on EDGAR: Halyard, filing Amendment No. 3 to its credit agreement as Exhibit 10.1. The term loan was quoted at 84 *(illustrative)*, which is the price at which people start reading. Kaz had an answer in ninety seconds. "The general restricted payments basket is thirty percent. I searched for 'Restricted Payments' and took the first number after it."

"Thirty percent of what?" said Theo.

"Of Consolidated EBITDA. It's capitalized, so it's defined somewhere. I like that about lawyers. It's a typed language."

The definition of "Consolidated EBITDA" started on page 19 and ended on page 30. It called "Consolidated Net Income," "Pro Forma Basis," "Specified Transaction" and "Run-Rate Cost Savings," and the Run-Rate Cost Savings were capped at 25% of Consolidated EBITDA "calculated after giving effect to such adjustments." "It's recursive," said Kaz, delighted. "It's a definition that grades its own homework," said Mags. "Back in my day the EBITDA definition fit on an index card, and we still didn't believe it. Now it has a table of contents."

Ines didn't look up. "Friday's lesson, again. The ad hoc group hired counsel in February, and their lawyers read Section 1.01 for a living. You're the last player at the table to look at your own cards."

Theo opened a ticket for ROBO: *Extract all baskets.* ROBO returned 412 baskets, one for every occurrence of the phrase "the greater of." Two of them were in the definition of "Excluded Taxes." Theo stared at the list, then at the USB stick holding his old 13-week cash flow model, then back at the list. The question was not whether a machine could read Halyard's agreement. It was this: **how do you turn a 300-page credit agreement and a 4,000-entry bankruptcy docket into numbers a model can trust, with every number pointing back to the sentence it came from, before the people who wrote the sentences trade on them?**

The chapter answers in one movement, and it helps to see the whole arc once before walking it. A credit agreement is a program: definitions are variables and covenants are assertions (§25.2). A basket is a function that returns dollars (§25.3). Leakage is a flow through baskets (§25.4). An amendment is a change in the capacity vector rather than in the tokens (§25.5). The docket is an append-only log whose marks and sequences carry the trade (§25.6–25.7). And every number has to point back to its span, because classifier error is an exchange rate on alpha (§25.9). Three real events carry the weight, one for each layer of text in §25.1.1: J.Crew for the contract, Windstream for the amendment and the court, and Serta for the docket.

By the end of this chapter you will be able to: parse an agreement's defined terms into a dependency graph and evaluate it in the right order; compute basket capacity in dollars, including grower, builder, ratio and add-back fixed points; treat value leakage (the J.Crew trapdoor) as a max-flow problem; version documents and explain why bag-of-words diffs miss the most expensive edits; build EDGAR and CourtListener ingest that respects the rate limits; turn Rule 2019 statements into a holdings time series and claims transfers into a flow; and quantify how much information coefficient a sloppy clause classifier costs you.

## 25.1 The Document Is the Constraint Set

At PJT, Theo read one credit agreement at a time, very well, with a highlighter and a deadline. The desk needs something different: every agreement in the universe read every morning, with the numbers kept current as amendments, exhibits and docket entries arrive. Same skill, different production function.

The economic object is the same in both seats. A covenant package is the boundary of the borrower's feasible set. Everything Chapter 13 priced (uptiers, drop-downs, double-dips) is a move inside that set, and the Priming Risk Score is a hazard on moves that approach the boundary. If you do not know where the boundary is, you are pricing a game without knowing the rules, which in poker is called "being the fish."

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.166:* "The basic tools of credit risk management are restrictive contract provisions, generally called covenants. Covenants are detailed contractual provisions contained in lending documents or bond indentures. Covenants are intensely negotiated and often the most difficult aspect of the lending document upon which to agree."
>
> **Annotation.** Moyer writes from the lender's chair: covenants are the protections the lender bargained for. The academic ancestor is Smith & Warner (1979), *On Financial Contracting: An Analysis of Bond Covenants*, which treats covenants as controls on the agency costs between shareholders and bondholders. A 2026 systematic desk keeps the economics and flips the sign. In a sponsor-drafted, cov-lite agreement, the "restrictive provisions" are mostly *permissions*: baskets the borrower can spend. The intense negotiation Moyer describes now happens before the deal launches, between sponsor counsel and arrangers. Its output is a set of capacities measured in dollars. The desk's job is to compute those capacities, track them through time, and notice when somebody is about to spend them.

### 25.1.1 Three layers of text

The credit text a desk can actually get comes in three layers. Each has its own latency, cost and API-friendliness.

| Layer | Documents | Where | Latency | Cost | API-friendliness |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Contract | Credit agreements, indentures, amendments, intercreditors | SEC EDGAR, exhibits EX-4 (instruments) and EX-10 (material contracts) | Seconds after dissemination | Free | High: JSON APIs, full-text search |
| Docket | Petitions, first-day declarations, Rule 2019 statements, motions, orders | PACER; RECAP mirror; CourtListener API | Minutes to days (RECAP depends on who bought it) | \$0.10 per page, capped at \$3 per document; free if mirrored | Medium: throttled REST, webhooks |
| Claims | Claims registers, transfer notices, ballots | Claims agents' case portals | Days | Free to view | Low: bot-blocked or JavaScript-rendered |

(PACER pricing from pacer.uscourts.gov, "PACER pricing: how fees work," fetched 2026-10-17. Portal behavior is from the Fable dossier's fetches on the same date; §25.8 has details.)

The contract layer is censored, and Theo learned how on a weeknight at PJT, a little after eleven, when the credit agreement a borrower had filed as an exhibit reached his screen without Schedule 1.01(b). The schedule held the excluded-subsidiary list, and the pricing grid had gone out with another omitted annex, so the document he was supposed to model told him neither who sat inside the collateral nor what the loan cost. Nothing was wrong with the filing. Regulation S-K Item 601(a)(5) lets a registrant omit schedules. Item 601(b)(10)(iv) lets it "redact specific provisions or terms" that are not material and that it treats as confidential. Item 601(b)(4)(iii)(A) lets it leave out any long-term debt instrument "if the total amount of securities authorized thereunder" does not exceed "10 percent of the total assets of the registrant and its subsidiaries on a consolidated basis," provided it agrees to furnish a copy on request. Private, sponsor-owned and 144A-for-life issuers file nothing at all. Theo called company counsel, had the schedule by midnight, and went back to his model. A desk reading 2,000 agreements cannot make 2,000 phone calls, and what it cannot see is not missing at random: small facilities never appear, the absent schedules are precisely the ones with the grid and the excluded subsidiaries, and a backtest on EDGAR agreements is a backtest on the public-filer subsample, which is how the desk labels every one of them.

The desk's first attempt to skip the reading altogether failed in a quieter way. ROBO, routed through a language model, came back that week with a restricted-payments capacity of \$140mm for Halyard *(illustrative)* and no span to say which sentence the number came from. Nobody could tell whether it was right, which on a trading desk is the same as its being wrong.

> **Desk Myth vs. Desk Reality.** *Myth:* "We'll point a large language model at the agreement and it will tell us the restricted payments capacity." *Reality:* A language model is very good at *finding the span* that defines a basket and very bad at being the place where arithmetic happens without a test. The desk splits the job. The model proposes spans with citations. A deterministic parser turns spans into typed nodes. A calculator with unit tests turns nodes into dollars. Every dollar carries a pointer back to the clause it came from. Chapter 26 calls this the citation contract. This chapter is what goes on the other side of it.

The documents were always there. What took systematic credit a while was noticing that they were data.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.32:* "The relatively few alternative data approaches that we have seen applied to quant credit strategies thus far include: analysing company linkages (suppliers and customers) from the Revere dataset...; bond short interest information; text-mining credit analysts' reports."
>
> **Annotation.** In 2022 one of the largest systematic managers listed text as an aside, and the text in question was *analysts' reports*, which are opinions about documents rather than the documents themselves. The gap since then is not mainly a story about better models. The documents were always free on EDGAR and RECAP. What changed is that LLM-assisted span extraction made covenant parsing cheap enough to run across a whole universe, while the 2017–2024 liability-management era made covenant capacity worth parsing at all. Text has moved from a footnote to a pipeline. The pipeline's competitive edge, though, is the boring part: dedupe, versioning, rate limits and units.

## 25.2 The Definition Graph: Legalese as a Typed Program

Moyer wrote the parser's job description twenty years before anyone tried to automate it, and he wrote it for a tired human.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.167:* "...take what is far too often, at least in the view of most nonlawyers, an unnecessarily turgid and impenetrable mass of legalese-laced verbiage and explain why it exists and what it is attempting to accomplish."
>
> **Annotation.** This is the parser's job description, written in 2005 for a human reader. The modern version has two halves. "Why it exists" is still a human question, and it is why the desk hired Theo. "What it is attempting to accomplish" can now be partly mechanized. A credit agreement is a program written in a typed language: defined terms are variables, definitions are function bodies, and covenants are assertions evaluated against those variables. The turgidity is real, but it has structure, and structure is what parsers eat.

Kaz read the first forty definitions of the Halyard agreement and announced a finding. "An 'Unrestricted Subsidiary' is a subsidiary with no parental controls."

"That's...correct," said Theo.

"And the borrower can designate one whenever it likes, subject to a basket?"

"Also correct."

"So it's a teenager with the car keys."

"And the intellectual property," said Mags, "is the car."

### 25.2.1 Two structures, not one

An agreement carries two structures, and the parsers that conflate them break. The first is the **section tree** $\mathcal{T}$: Article → Section → clause (a) → sub-clause (i) → item (A). It is the abstract syntax tree in the compiler sense, and a cross-reference such as "Section 6.08(b)(iv)" is a path in it. When the model ROBO called invented a clause "(xiv)" in Chapter 26, it was naming a path that does not exist, and a tree lookup would have caught it before anyone priced it. The second is the **definition graph** $G = (V, \mathcal{E}^{\text{dep}})$. Its vertices $V$ are the defined terms plus the operative provisions, and there is an edge $u \to v$ when the text of $u$ *uses* $v$. "Consolidated Total Net Leverage Ratio" points to "Consolidated Total Debt" and to "Consolidated EBITDA," which points to "Consolidated Net Income," "Pro Forma Basis," and on down. Theo had always walked the second structure with a highlighter; he had simply never drawn it.

(The edge set is written $\mathcal{E}^{\text{dep}}$ because $E_t$ is equity value in this book's notation. For the same reason, from §25.3 on, covenant EBITDA is $\mathcal{E}$, calligraphic.)

To evaluate a covenant, ROBO has to evaluate every term it reaches, each one after its own dependencies. That ordering has a name, a topological order of $G$, and it is older than any credit agreement.

> **Math, Gently.** *Graphs, adjacency matrices and why loops never die.* Picture a spreadsheet. Cell B7 says `=B5/B6`, B5 adds up a column, B6 pulls a number from another tab. Excel cannot compute B7 until it has computed B5 and B6, so it quietly works out an order in which every cell comes after the cells it reads. That order is a *topological order*, and the web of "this cell reads that cell" is a *graph*: dots for cells (or defined terms), arrows for "uses." When you write `=B7` into B5, Excel throws its circular-reference warning, because now there is a loop and no order exists. A graph can be stored as a table, the *adjacency matrix* $A$, with a 1 in row $u$, column $v$ when $u$ uses $v$. Multiply the table by itself and the entries count two-step paths; cube it and they count three-step paths. Take three terms, the Leverage Ratio (L), Consolidated EBITDA (E) and Consolidated Net Income (N), with L using E and E using N:
>
> $$
> A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \qquad A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad A^3 = 0.
> $$
>
> $A^2$ has exactly one nonzero entry, the walk L → E → N, and $A^3$ is all zeros, because in a graph without loops every path eventually runs out of road. A matrix that some power turns into zero is called *nilpotent*. Now add one arrow, N → L, and the road never ends: you can go round the loop as often as you like, so every power has a nonzero entry. Loops, and only loops, keep the powers alive. The lemma that turns this into a unit test is next.

### 25.2.2 Reachability, nilpotence and blast radius

Let $A \in \{0,1\}^{n\times n}$ be the adjacency matrix of $G$, with $A_{uv} = 1$ if $u$ uses $v$. Then $(A^k)_{uv}$ counts the walks of length $k$ from $u$ to $v$. The reachability matrix is

$$
R_{uv} = \mathbb{1}\Big\{\sum_{k=1}^{n} (A^k)_{uv} > 0\Big\}.
$$

**Lemma 25.1.** $G$ is acyclic if and only if $A$ is nilpotent, with $A^n = 0$.

The proof is at the end of this subsection. The lemma becomes a unit test: compute $A^n$ (or, more cheaply, run a depth-first search) and if it is not zero, the agreement has a circular definition that has to be handled on purpose rather than by accident.

The **blast radius** of an amendment that rewrites term $v$ is the set of everything that depends on it:

$$
\mathcal{B}(v) = \{u \in V : R_{uv} = 1\}, \qquad \beta(v) = |\mathcal{B}(v)|.
$$

Amend "Consolidated EBITDA" and you have touched every leverage ratio, every grower basket, the pricing grid, the excess-cash-flow sweep, and usually the definition of "Available Amount." Amend "Excluded Taxes" and you have touched very little. Section 25.5 weights $\mathcal{B}(v)$ by dollars of capacity, and that weighted blast radius is the most useful single number to compute on an amendment.

#### The Full Derivation: nilpotence and reachability

*Proof of Lemma 25.1.* Suppose $G$ is acyclic. A walk of length $n$ visits $n+1$ vertices, so by pigeonhole it visits some vertex twice. The segment between the two visits is a cycle, which is a contradiction. So there are no walks of length $n$, and $A^n = 0$. Conversely, if $G$ contains a cycle of length $\ell$, then for every $m \ge 1$ there is a closed walk of length $m\ell$, so $A^{k} \ne 0$ for infinitely many $k$ and $A$ is not nilpotent. $\square$

### 25.2.3 Cycles are real; condense them

Real agreements have cycles. Halyard's Run-Rate Cost Savings cap refers to Consolidated EBITDA "after giving effect to" the cost savings, and Pro Forma Basis refers to Consolidated EBITDA, which is calculated on a Pro Forma Basis. The standard fix is to compute the **strongly connected components** (Tarjan's algorithm, $O(|V| + |\mathcal{E}^{\text{dep}}|)$), collapse each component into a single super-node, and evaluate the resulting condensation, which is a directed acyclic graph by construction. Inside each component you solve a fixed point. (A strongly connected component is a largest set of terms in which every term can reach every other by following arrows: a loop, plus everything tangled into it. A contraction is a rule that pulls any two guesses closer together each time you apply it, so applying it over and over homes in on one answer; the box for it is in the next section, where the add-back cap needs it.) Section 25.3 shows the fixed point for the add-back cap is a contraction, so the iteration converges, and it also shows the cap ends up larger than it looks. Figure 25.1 draws the synthetic Section 1.01 of Listing 25.1 with both of its loops.

![Figure 25.1: In the synthetic Section 1.01 of Listing 25.1, two groups of terms define each other (dashed loops: the add-back cap through Consolidated EBITDA, and the J.Crew blocker), and amending Consolidated EBITDA reaches only three other terms (shaded, β = 3) while Excluded Taxes reaches none. Illustrative: edges produced by the Listing 25.1 term matcher on the book's synthetic agreement text; an arrow runs from a term to each term its definition uses.](assets/figures/ch25_definition_graph.png)

### 25.2.4 Finding the vertices and edges

Vertices come from definition sentences: `"Term" means ...`, `"Term" has the meaning assigned to such term in Section 7.02`, and inline definitions buried in operative text (`(any such transaction, a "Specified Transaction")`). Edges come from matching the term dictionary against each definition body. That sounds like the easy half, and it is the half that bites.

*A fictional composite, set at a systematic asset manager before Theo's time; the count is illustrative.* Nothing crashed on the night the matcher reversed the documents. The nightly parser diff finished at 4:10 a.m. and reported that 212 agreements had lost their J.Crew blocker since the previous evening *(illustrative)*. No amendments had been filed. Paloma, the data engineer on the early shift, noticed because 212 is not a number the loan market produces between midnight and four. She opened one agreement, found the sentence that barred transfers of Material Intellectual Property to "any Unrestricted Subsidiary," and saw the edge the parser had drawn from it: to "Restricted Subsidiary." A pull request the afternoon before had made the matcher case-insensitive, to catch a few lower-case cross-references, and "restricted subsidiary" sits inside "Unrestricted Subsidiary" like a smaller doll. Every blocker now read as a limit on the wrong entities. The 6:30 signal run would have ranked 212 protected loans as high-leakage shorts. Paloma held it, which meant the portfolio manager arrived to an empty screen and a two-line note, and the team spent the day rebuilding three weeks of history to find out how far back the change reached. The sentence that desk says now, before any matcher change ships, is six words long: "Longest match first, case on, consume the span." The box below is the full list of ways this goes wrong.

> **Ways This Blows Up.** *Substring matching.* Ignoring case, the term "Restricted Subsidiary" is a substring of "Unrestricted Subsidiary." A parser that matches case-insensitively, without word boundaries or longest-match-first, will draw an edge from every unrestricted-subsidiary provision to "Restricted Subsidiary," reversing the most important distinction in the document. The same trap catches "Lender" inside "Affiliated Lender" and "Debt" inside "Consolidated Total Debt." The fix: match case-sensitively, sort the dictionary by length descending, match with word boundaries, and consume each matched span before trying shorter terms. Other ways this goes wrong: plurals ("Restricted Payments" for "Restricted Payment"); terms defined by reference to *another* document (the Intercreditor Agreement, the Existing Indenture); a term defined in Section 1.01 and quietly redefined "for purposes of this Article X"; and exhibits filed as scanned images with no text layer. Every one of these fails silently.

> **Trend Watch. The vocabulary of liability management on EDGAR, 2018–2026.** EDGAR full-text search covers "all EDGAR filings submitted electronically since 2001," including exhibits (SEC EFTS FAQ). Queries run against the full-text search API on 2026-10-17 (counts are *filings including exhibits*, not distinct agreements):
>
> | Phrase | 2018 | 2021 | 2025 |
> | :--- | ---: | ---: | ---: |
> | "Material Intellectual Property", all forms | 2,281 | 4,571 | 3,411 |
> | "Material Intellectual Property", 8-K | 847 | 1,225 | 1,157 |
> | "first lien credit agreement", 8-K | 223 | 343 | 146 |
>
> The phrase "unrestricted subsidiary" appears in 1,931 8-K filings from 2024-01-01 through 2026-10-17 (an exact count). *What changed:* J.Crew-blocker vocabulary in 8-K exhibits rose about 37% from 2018 to 2025, while 8-K filings mentioning a first-lien credit agreement fell to about 65% of their 2018 level. The 2021 all-forms spike probably reflects the SPAC wave (S-4 and S-1 registrations), not loans. As a *crude* density, the ratio of blocker mentions to first-lien agreement mentions in 8-Ks went from $847/223 \approx 3.8$ to $1{,}157/146 \approx 7.9$. *What it means:* the public filer base for leveraged loans is shrinking as deals move to private credit (Chapter 17), while the agreements that remain are full of LMT defenses. Two cautions belong in the same box. The numerator and denominator are different document sets. And the API caps `hits.total` at 10,000, so a broad normalizer like "credit agreement" silently returns "≥10,000." The ratio is a picture, not a statistic.

## 25.3 Basket Arithmetic: From Clauses to Dollars

The first sticky note Theo put up on the desk, over the second monitor, says: *a basket is not a sentence; it is a function from the state of the company to a number of dollars.* This section is that note written out, with units, and tested.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.220:* "Often, negative pledge provisions have fairly significant 'carve-outs' that will be stated in either absolute (e.g., \$100 million) or relative (e.g., 10% of net tangible assets) amounts. In the absence of other lending provisions that may be constraints, these carve-outs essentially define how much cash the firm can raise on a secured basis."
>
> **Annotation.** This is the 2005 ancestor of the modern "greater of \$X and Y% of Consolidated EBITDA" grower basket. Moyer's last sentence is the thesis of this section: the carve-outs *are* the secured-debt capacity, which makes them the priming risk. Two things have changed since. First, the relative component is now usually keyed to EBITDA, a number the borrower defines, rather than to net tangible assets, a number accountants define. Second, "greater of" turns the basket into a ratchet that grows with EBITDA, and some recent agreements add "high-water mark" language so the basket does not shrink when EBITDA falls. The parser has to read the basket's base, its fixed floor and its memory.

### 25.3.1 Node types

Every basket becomes a typed node with explicit parameters. The template phrases below are synthetic, written for this book, not copied from any agreement.

| Node type | Template phrase (synthetic) | Capacity $K$ | Parameters |
| :--- | :--- | :--- | :--- |
| Fixed | "not to exceed \$50,000,000 at any time outstanding" | $X$ | $X$ |
| Grower | "the greater of \$75,000,000 and 35% of Consolidated EBITDA" | $\max(X, p\,\mathcal{E})$ | $X$, $p$, base term |
| Ratio | "so long as, on a Pro Forma Basis, the First Lien Net Leverage Ratio does not exceed 4.50:1.00" | $\max(0, m\,\mathcal{E} - F^{\text{sc}})$ | $m$, scope, netting rule |
| Builder | "the Available Amount at such time" | path-dependent; see (25.2) | starter, CNI share, equity credit |
| Maintenance test | "shall not permit the Total Net Leverage Ratio as of the last day of any Test Period to exceed..." | none; a breach is a default | $m$, test dates, cure rights |

Mags read the grower row aloud from Halyard's agreement, slowly, the way she reads anything she has decided not to trust. "'The greater of \$75,000,000 and 35% of Consolidated EBITDA.'"

"So it's seventy-five million," Kaz said, "unless thirty-five percent of EBITDA is bigger. Which it is whenever EBITDA is above two hundred and fourteen million and change." A pause while Kaz followed the capitalized word back into Section 1.01, eleven pages of it, add-backs included. "Oh. The basket grows with a number the sponsor writes."

"Now you're reading it like a lender," Mags said. "The seventy-five is the lender's. The thirty-five percent is the sponsor's. 'Greater of' means the sponsor always gets whichever is better that quarter."

"A max function," Kaz said, "where the counterparty controls one of the arguments." Kaz wrote it on the board, $\max(X, p\,\mathcal{E})$, and drew an arrow from $\mathcal{E}$ to the word *sponsor*. Theo pointed at the table's last column, the one headed "base term." The base is not a number. It is a pointer back into the definition graph, which is why the graph had to come first.

Each node also carries a usage $U_j$, and availability is $K_j - U_j$. Reclassification language ("may divide, classify and reclassify") lets the borrower move usage between baskets after the fact. In practice that means usage is a decision variable for the borrower, not a fact for you.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.168:* "...the leverage covenant, which is usually structured to limit debt to a specified multiple of EBITDA... In complex multitiered capital structures, the leverage test may only address the layer in question. Thus a senior loan may specify that senior debt will not be more than, for example, 2.5x EBITDA, but may be silent on how much total debt is allowed."
>
> **Annotation.** In schema terms, *scope is a field, not a footnote*. A ratio node without its scope (total, senior, secured, first-lien) is a number without units. Moyer's example is a senior test silent on total debt. The 2026 equivalent is a first-lien net leverage incurrence test that is silent on junior secured debt. It permits a second-lien or unsecured layer, sometimes at a different ratio, and that layer is how a "4.50x" agreement ends up with 7x of total debt. Kaz's first parser stored `ratio = 4.5` and nothing else. ROBO, given that schema, reported that Halyard could not borrow another dollar of junior debt. Halyard borrowed another \$250mm of junior debt the following quarter *(illustrative)*.

### 25.3.2 The ratio basket, and the four words that stop a perpetual-motion machine

Halyard's first-lien test is the dialect that hides the most money in the fewest words, so it is worth slowing down on.

> **Math, Gently.** *Solving a test for the amount it allows.* Picture a bathtub with a line painted on the side. The test says that after you pour in your bucket, the water must still be below the line. The line is $m$ times EBITDA; the water already in the tub is the existing debt, less any cash the definition lets you subtract. The biggest bucket you can pour is the gap between the line and the water. With $m = 4.50$x, $\mathcal{E} = 200$, existing debt of 900 and no cash, the line sits at $4.5 \times 200 = 900$ and the tub is already full, so the biggest bucket is $900 - 900 = 0$. Now change one rule: the cash you borrow can be subtracted from the debt while it sits in the bank. Pour in 100 and you also drain 100, so the level is $(900 + 100 - 100)/200 = 4.5$, which passes. Pour in a thousand and the level is still $(900 - 0)/200 = 4.5$. The bucket no longer changes the water, so the test cannot stop it. Solving an inequality for capacity means moving everything except the new amount to one side; when the new amount cancels out entirely, there is no limit at all. The algebra follows.

Let $F^{\text{sc}}$ be existing debt within the test's scope, $C$ the unrestricted cash the definition lets you net, $m$ the permitted ratio, and $\Delta$ the new debt. The pro forma incurrence test is

$$
\frac{F^{\text{sc}} + \Delta - C'}{\mathcal{E}} \le m,
$$

where $C'$ is the cash netted *after* the incurrence.

*Case 1: proceeds are not netted* ($C' = C$). Solving for the largest $\Delta$,

$$
\Delta^{*} = \max\big(0,\; m\,\mathcal{E} - F^{\text{sc}} + C\big).
$$

*Case 2: proceeds are netted and held as cash* ($C' = C + \Delta$). The left-hand side becomes $(F^{\text{sc}} - C)/\mathcal{E}$, which does not depend on $\Delta$. If the test passes at all, it passes for every $\Delta$, so $\Delta^{*} = \infty$.

This is why agreements say the ratio is computed "without netting the cash proceeds of the Indebtedness being incurred," and why many also cap netted cash at a fixed amount, $C' = \min(C, X^{\text{net}})$. A parser that misses those words reports infinite capacity, and in this case the parser is reading the document correctly; it is the document that has been drafted badly. Without the clause, the ratio test is a perpetual-motion machine: borrow a dollar, hold the dollar, net the dollar, repeat.

> **View From Another Seat.** *A direct lender.* The lender that negotiated the netting clause does not parse it; it refuses it. A direct lender writes and holds its own loans, so its leverage over the document comes before the money moves rather than after. Ares Capital's management put that seat's position on the company's fourth-quarter 2025 earnings call on 4 February 2026. Asked whether deal terms were loosening, they answered that if anything there was "a heightened focus on documentation terms" after the liability-management headlines in the broadly syndicated market, and they presented documentation as a core part of the investment committee's work *(ARCC Q4 2025 call; no individual speaker or further wording is quoted here)*. For that seat, a missing "without netting the cash proceeds" is a clause to fix before the loan closes. The systematic desk has no such door. The loan is already in its universe, quoted every day and held by people it trades with, and it cannot walk away from a clause it never negotiated. It can only price the clause, which is why the parser has to find the four words, or notice their absence, before the sponsor's lawyers remind everyone.

### 25.3.3 The add-back fixed point

Back to the cold open, and to the phrase Kaz called recursive. Let $\mathcal{E}_0$ be EBITDA before run-rate add-backs, $A$ the add-back claimed, and $c$ the cap. Measured *before* giving effect to the add-backs, the cap says $A \le c\,\mathcal{E}_0$. Measured *after* giving effect to them, it says $A \le c\,(\mathcal{E}_0 + A)$: the add-back counts toward the base it is capped by. Rearranging the second, and using $0 < c < 1$,

$$
A(1 - c) \le c\,\mathcal{E}_0 \quad\Longrightarrow\quad A \le \frac{c}{1-c}\,\mathcal{E}_0. \tag{25.1}
$$

The gap between the two readings is $\frac{c}{1-c} - c = \frac{c^2}{1-c}$ of $\mathcal{E}_0$. At $c = 25\%$ the "after" reading allows add-backs of $33.3\%$ of pre-add-back EBITDA instead of $25\%$: 8.3 extra points of EBITDA from four words. Per word, that beats "open market purchase," which needed three words and a Fifth Circuit appeal (Chapter 13).

The algebra solved the loop in one line because the loop was simple. Most loops in Section 1.01 are not, and ROBO needs a method that works when nobody has done the algebra for it.

> **Math, Gently.** *Fixed points and contractions.* A definition that refers to itself cannot just be computed; it has to be guessed and checked. Picture a guess that corrects itself by a quarter of its own error every round. Halyard's cap is 25% of EBITDA *including* the add-back. Start from what the sponsor claims, \$80mm, on pre-add-back EBITDA of \$200mm. Round one: 25% of $200 + 80$ is 70, so 80 is too much; try 70. Round two: 25% of 270 is 67.5. Round three: 25% of 267.5 is 66.9. Round four: 66.7, and the number stops moving. A number that reproduces itself when you feed it back in is a *fixed point*; here $A = 0.25\,(200 + A)$, so $A = 66.7$. The distance to the answer goes 13.3, 3.3, 0.8, 0.2, a quarter of the previous gap each time, because each extra dollar of guess raises the cap by only 25 cents. A rule that shrinks gaps like that is a *contraction*, and a contraction lands on its fixed point from any starting guess. If each extra dollar raised the cap by a dollar or more, the guesses would never settle. Keep \$66.7mm in mind; the Halyard table in the next subsection is built on it.

Equation (25.1) is the general recipe in disguise. Write the cycle as a map and iterate:

$$
A_{k+1} = T(A_k) = \min\big(A^{\text{claimed}},\; c\,(\mathcal{E}_0 + A_k)\big).
$$

The code in §25.10 evaluates every strongly connected component this way, and a component whose map does not shrink the gaps goes to a human instead of to a number. For Theo, that is a feature, not a bug. Why the iteration is guaranteed to land is the short argument below.

#### The Full Derivation: the cycle as a contraction

For any two guesses $a$ and $a'$, the map $a \mapsto c\,(\mathcal{E}_0 + a)$ moves by exactly $c\,|a - a'|$, and taking a minimum with the constant $A^{\text{claimed}}$ never increases a distance. So $|T(a) - T(a')| \le c\,|a - a'|$: $T$ is Lipschitz with constant $c < 1$, and by the Banach fixed-point theorem the iteration converges from any start to the unique fixed point, with error shrinking like $c^k$. If a component's map is *not* a contraction (estimated Lipschitz constant $\ge 1$), the definitions are ill-posed and the parser hands the component to a human.

### 25.3.4 Capacity is levered to add-backs

Now put the \$66.7mm to work. **Halyard, worked** *(illustrative)*. Take $\mathcal{E}_0 = \$200$mm, claimed add-backs of \$80mm, the 25% "after giving effect" cap, a first-lien net leverage incurrence test at $m = 4.50$x with existing first-lien net debt $F^{\text{sc}} = \$900$mm (proceeds not netted), and a general debt basket at the greater of \$75mm and 35% of Consolidated EBITDA. From (25.1), $A = \min(80, 66.7) = \$66.7$mm, so $\mathcal{E} = \$266.7$mm.

| | No add-backs | With add-backs |
| :--- | ---: | ---: |
| Covenant EBITDA $\mathcal{E}$ (\$mm) | 200.0 | 266.7 |
| Ratio capacity $\max(0, 4.5\,\mathcal{E} - 900)$ | 0.0 | 300.0 |
| General basket $\max(75, 0.35\,\mathcal{E})$ | 75.0 | 93.3 |
| **Total incremental capacity** | **75.0** | **393.3** |

> **Math, Gently.** *Hockey sticks, kinks and slopes that switch on.* Draw Halyard's capacity against covenant EBITDA and you get a hockey stick with two bends. Below \$200mm the ratio test has no headroom, so it contributes nothing and the line sits flat at the general basket's \$75mm floor: an extra dollar of EBITDA buys nothing. At \$200mm the blade starts. Each extra dollar of EBITDA lifts $4.5\,\mathcal{E}$ by \$4.50 while the debt already in place stays put, so capacity climbs \$4.50 a dollar. At about \$214.3mm comes the second bend, where 35% of EBITDA overtakes the \$75mm floor and the general basket starts growing too, by 35 cents a dollar. Between 250 and 251, say, the ratio piece goes from 225 to 229.5 and the basket from 87.5 to 87.85, so capacity rises by \$4.85. A function made by taking the larger of straight lines can only bend upward, never down, and mathematicians call that *convex*. Its slope at any point is the sum of the slopes of the pieces that are switched on there, and the switch is written as an *indicator*, $\mathbb{1}\{\cdot\}$, which is 1 when the condition inside holds and 0 when it does not. The general formula follows.

In general, total incremental debt capacity, from the ratio basket plus grower general-debt baskets $j$, is

$$
K(\mathcal{E}) = \max\big(0,\, m\,\mathcal{E} - F^{\text{sc}}\big) + \sum_j \max\big(X_j,\; p_j\,\mathcal{E}\big).
$$

Each term is a maximum of affine functions, so $K$ is convex and piecewise linear in $\mathcal{E}$: capacity accelerates as EBITDA grows. Where it is differentiable,

$$
\frac{\partial K}{\partial \mathcal{E}} = m\,\mathbb{1}\{m\,\mathcal{E} > F^{\text{sc}}\} + \sum_j p_j\,\mathbb{1}\{p_j\,\mathcal{E} > X_j\},
$$

and $\partial \mathcal{E}/\partial A = 1$ below the add-back cap and $0$ above it.

At the margin, each dollar of add-back buys $4.50 + 0.35 = 4.85$ dollars of debt capacity, and every one of those dollars can sit ahead of you. Figure 25.2 shows both halves of the arithmetic.

![Figure 25.2: Measuring the 25% cap "after giving effect" lets add-backs reach 33.3% of pre-add-back EBITDA instead of 25% (left), and at Halyard the resulting \$66.7mm of add-backs lift incremental debt capacity from \$75mm to \$393.3mm (right). Illustrative: the Halyard terms of §25.3.4, with pre-add-back EBITDA of \$200mm, a 4.50x first-lien test on \$900mm of net debt with proceeds not netted, and a general basket at the greater of \$75mm and 35% of EBITDA.](assets/figures/ch25_addback_capacity.png)

"This is why I don't trust anything called 'adjusted,'" said Mags. "Every adjusted dollar is worth almost five dollars of somebody else's priming debt."

Kaz already had a paper open. "This is the large-sample version of your suspicion," Kaz said, and read it to her in the flat voice Kaz uses for results that are going to annoy someone. Badawi, Dyreng, de Fontenay & Hills (draft 2021), *Contractual Complexity in Debt Agreements: The Case of EBITDA*, extracted EBITDA definitions from 4,532 credit agreements (1996–2018). They hand-coded seven specific adjustments on a random subsample of 581, built a permissiveness score running from one (GAAP net income plus interest, taxes and D&A) to eight, and extended it out of sample with a Naive Bayes classifier. Mean permissiveness is 3.61 (s.d. 1.74), and it rises over the sample.

"Rises," Mags said. "Of course it rises."

"It gets better," said Kaz, meaning worse. More permissive definitions come with tighter covenant thresholds but *fewer* violations, and with more negative market reactions when a violation does happen. Sponsor-backed borrowers are more permissive. Mags took the printout and read the abstract twice, which on her scale is applause. Theo wrote the two lessons the desk keeps from it in his notebook: EBITDA is the root of the definition graph, so it is the node whose blast radius is largest; and its complexity is itself a time series the desk can measure.

### 25.3.5 The builder basket, or the 13-week model gets a job

The builder ("Available Amount," "Cumulative Credit") is path-dependent. A common synthetic form: a starter amount $S = \max(X_s, p_s\,\mathcal{E})$, plus 50% of cumulative Consolidated Net Income from a reference date "taken as one accounting period" (or, if that cumulative figure is a deficit, minus 100% of it), plus retained equity proceeds $Q_t$, minus usage $U_t$. With cumulative CNI $N_t = \sum_{q \le t} \text{CNI}_q$, $N^{+} = \max(N, 0)$ and $N^{-} = \max(-N, 0)$:

$$
B_t = S + \tfrac{1}{2}\,N_t^{+} - N_t^{-} + Q_t - U_t, \qquad \text{available}_t = \max(0, B_t). \tag{25.2}
$$

The kink at $N_t = 0$ is asymmetric: slope $\tfrac12$ above, slope $1$ below, so losses count double. Some agreements use a retained-excess-cash-flow builder instead, and some high-yield indentures use an EBITDA-less-a-multiple-of-fixed-charges alternative. Those are different node subtypes with different inputs, and a schema that squeezes all three into one formula gets all three slightly wrong, which is the most expensive way to be wrong.

Here the running gag earns its keep. Theo's 13-week cash flow model, reborn as a state-space feature, forecasts next quarter's $\text{CNI}_q$, which forecasts $B_{t+1}$. That tells the desk how much builder capacity the sponsor will have on the next dividend date, before the sponsor's own treasury team has finished its spreadsheet.

The first quarter the feature ran, it was wrong by \$55mm *(illustrative)*, and the 13-week model was innocent. ROBO had been handed "net income" from the fundamentals feed, which arrives as a trailing four quarters, and it computed Halyard's builder as a \$50mm starter plus half of a healthy LTM \$30mm: \$65mm available. Theo looked at the number on Monday morning and frowned, because he remembered the reference date. "The first full fiscal quarter after closing," he said. "They had two years of restructuring charges before this one." Cumulative CNI from that date was minus \$40mm, the deficit branch of (25.2) applied, and losses count double, so the builder was \$50mm minus \$40mm: \$10mm. The window had quietly forgiven two bad years that the agreement never forgives. Kaz changed the input from `cni_ltm` to the full quarterly tape since the reference date and added a test that fails if the tape starts late. The desk's sentence for it now: the builder has a memory, so feed it the whole tape.

### 25.3.6 Maintenance versus incurrence: two node types, two default semantics

Moyer describes the maintenance covenant as a performance milestone (for example, "'EBITDA for the third fiscal quarter will exceed \$X'") and notes that "where performance covenants are included, failure to comply with the requirement is a default" (Moyer_Distressed_Debt_Analysis p.174). In the graph, a maintenance node is evaluated on every test date, and a breach emits an `EventOfDefault` (subject to equity-cure rights, which are a basket of their own). An incurrence node is evaluated only when the borrower acts, and failing it emits `NotPermitted`. Incurrence tests never "violate"; they merely "permit." That difference has hollowed out the classic covenant-breach signal.

> **Trend Watch. Covenants leave the building: maintenance to incurrence, 1997–2024.** Griffin, Nini & Smith, *Losing Control? The 20-Year Decline in Loan Covenant Violations* (summarized on the Harvard Law School Forum on Corporate Governance, Nov 4, 2022), find that the annual share of U.S. public firms reporting a financial covenant violation fell by "nearly 70%" over twenty years (from over 12% in 1997 to under 5% in 2016, per the abstract as quoted in secondary sources). Late-1990s loans typically had "three or four covenants," while loans today rely on "one or two covenants" benchmarked against EBITDA. About half of the decline is a false-positive rate that "falls nearly 90%." On the leveraged-loan side, S&P Global reported in October 2021 that cov-lite deals exceeded 90% of leveraged-loan issuance, a record at the time. Per PitchBook|LCD, as reported in Paul Weiss's *Covenant-Lite Loans: Overview* (Practical Law, 2025), cov-lite loans were about 88.91% of outstanding U.S. leveraged loans (at par) at year-end 2022, 89.23% (about \$1,248.87 billion) at year-end 2023, and 91.09% (about \$1,292.74 billion) at year-end 2024, and about 93% of institutional issuance in both 2023 and 2024. (The full-year 2025 figure was not verified for this edition.) *What it means for the desk:* a parser that reads only the financial covenant section reads almost nothing. The risk now lives in incurrence baskets, which never trip a default and only tell you what the borrower is *allowed* to do next. Covenant-breach signals from the 1990s literature have to be rebuilt as capacity signals.

## 25.4 Value Leakage as a Flow Problem

Baskets do not act alone. Value leaves the collateral pool by *routes*: from the loan parties to non-guarantor restricted subsidiaries, from there to unrestricted subsidiaries, and from there to new creditors. A list of baskets can't tell you how much value can leak, because the binding constraint depends on how the baskets connect. A graph can.

### 25.4.1 The entity graph and max-flow min-cut

> **Math, Gently.** *Flows, cuts, and the narrowest place in the plumbing.* Picture water before money. Two pipes run from a reservoir into a tank, one 40 wide and one 60 wide, and a single pipe runs out of the tank to a field. A *flow* is any way of running water that respects each pipe's width and never lets the tank fill or drain: what goes in comes out. How much can reach the field each hour? Weld the outflow pipe shut, width 0, and the answer is 0, however wide the inflows are. Open it to 30 and the answer is 30, because the outflow pipe is the bottleneck. Open it to 1,000 and the answer is 100, because now the two inflows are the bottleneck and together they carry $40 + 60$. A *cut* is any set of pipes that, sawn through, would stop all water reaching the field, and its capacity is the total width you sawed. Sawing the outflow costs 0, 30 or 1,000 in the three cases; sawing both inflows costs 100 every time. The biggest flow always equals the cheapest cut: 0, then 30, then 100. Look at the third case again. Making the outflow enormous did not add a drop beyond 100. It moved the bottleneck upstream, onto two pipes nobody had been watching. Swap water for dollars of collateral and pipe width for basket capacity, and that sentence is the next case study. The formal version is next.

Now the dollars. Build a directed graph $H$ whose nodes are entity classes: the source $s$ (the loan parties, holding the collateral), intermediate classes such as $N$ (restricted subsidiaries that are not guarantors), and the sink $t$ (unrestricted subsidiaries, outside the covenant perimeter). Each arc $a$ has a capacity $c_a \ge 0$ in dollars: the basket that permits investments or asset transfers along that route. A **flow** $f$ assigns $0 \le f_a \le c_a$ to each arc, with inflow equal to outflow at every intermediate node. Its value $|f|$ is the net flow into $t$. The **leakage capacity** is

$$
\Phi = \max_{f}\; |f|.
$$

(We use $\Phi$ because $\Lambda$ is reserved for order arrival and $\lambda$ for default intensity.)

An $s$–$t$ **cut** $(\mathcal{S}, \mathcal{S}^c)$ splits the nodes so that $s \in \mathcal{S}$ and $t \notin \mathcal{S}$. Its capacity $c(\mathcal{S})$ is the sum of capacities on arcs leaving $\mathcal{S}$. The **max-flow min-cut theorem** (Ford & Fulkerson, 1956) says that the largest flow equals the smallest cut, exactly as it did for the water:

$$
\Phi = \min_{\mathcal{S}}\; c(\mathcal{S}).
$$

The theorem is what makes this practical, because the min cut names *which* baskets bind. Raising the capacity of an arc that is not in the min cut changes nothing. Raising the capacity of an arc in the min cut, including to infinity, moves the cut, and $\Phi$ jumps to the next-smallest cut. That is exactly what a trapdoor does, and it is the third case in the box with lawyers instead of plumbers.

#### The Full Derivation: any flow is at most any cut

Half of the theorem is bookkeeping. Sum the conservation condition over the nodes in $\mathcal{S}$. Every intermediate node contributes zero, and the source contributes its net outflow, which is the flow's value. Arcs with both ends inside $\mathcal{S}$ appear once as an outflow and once as an inflow and cancel, so what survives is the traffic across the boundary:

$$
|f| = \sum_{a \,\in\, \text{out}(\mathcal{S})} f_a \;-\; \sum_{a \,\in\, \text{in}(\mathcal{S})} f_a \;\le\; \sum_{a \,\in\, \text{out}(\mathcal{S})} c_a = c(\mathcal{S}),
$$

because $f_a \le c_a$ on arcs leaving $\mathcal{S}$ and $f_a \ge 0$ on arcs entering it. That is weak duality: any flow is at most any cut. The other half, that some flow attains the smallest cut, is Ford and Fulkerson's argument. Push flow along any path from $s$ to $t$ that still has room (counting the option of undoing flow already sent the other way), and repeat until no such path remains. At that moment the nodes still reachable from $s$ form a cut whose outgoing arcs are all full and whose incoming arcs are all empty, so the inequality above holds with equality and the flow equals that cut. The Edmonds–Karp routine behind Figure 25.3 is this argument run as an algorithm, choosing the shortest open path each time so that it is guaranteed to finish.

### 25.4.2 Case Study: J.Crew, 2016–2017, the Trapdoor as a Cut

#### Long Scene: J.Crew, Two Small Baskets and a Third Provision (October 2016 – September 2017)

*A Friday replay on the fictional desk. The cards, the parser runs and the dialogue are invented. The dates, baskets, values and exchange terms come from J.Crew's own filings (its Form 10-K for the fiscal year ended 28 January 2017, its 1 February 2017 press release, and its Form 10-Q for the quarter ended 29 April 2017) and from the law-firm accounts named in the scene. No loan price is quoted, because none is sourced here.*

**Beat one: an empty garage (12 October 2016).** The Friday after Windstream, Ines put one paragraph from J.Crew's annual report on the big monitor and covered everything below its first sentence with a strip of printer paper and a binder clip. The visible sentence said that on 12 October 2016 the company had designated certain newly formed Delaware entities as unrestricted subsidiaries under its senior credit facilities and its PIK Notes indenture.

"The annual report was filed after all of this happened," Ines said, "so I'm feeding it to you a date at a time, and you get only what's above the paper. What does an unrestricted subsidiary with nothing in it tell you?"

"It's outside the covenants, not out on good behavior," Kaz said, before anyone could start. "I've been told twice." Kaz had the term loan agreement loaded already, and the list-of-baskets parser from §25.3 had run over its investments covenant during the walk back from the coffee machine. It returned what it had been built to return: a basket for investments in restricted subsidiaries that are not loan parties, \$150mm; a general investment basket, \$100mm; and a scatter of small carve-outs for joint ventures and employee loans. "Two hundred and fifty million of investment capacity, most of it labeled for non-guarantors. Small baskets for foreign subsidiaries. Every borrower with a business abroad has them."

Theo was less relaxed. Six years in restructuring had taught him one thing about empty entities, which is that nobody builds a garage without a car in mind. "Why form new ones in October? An unrestricted subsidiary is a place to put things the lenders can't reach. The question is what fits through the door."

"Through which door," said Mags. "There are always more doors than the table of contents admits."

Kaz added a node to the entity graph labeled `Unrestricted (new)` and drew no arcs into it, because the parser had found no basket that pointed there. The graph's leakage capacity came out at zero. Kaz circled the zero on the whiteboard, pleased with how quiet it looked.

**Beat two: the brand leaves the building (5 December 2016; the company's press release, 1 February 2017).** Ines slid the paper down two lines. On 5 December 2016 a subsidiary had transferred a 72.04% undivided interest in certain of the company's domestic intellectual property to one of the new unrestricted subsidiaries. The company's press release came two months later. On 1 February 2017, the day it sued its own term-loan agent, J.Crew said in that release (furnished on an 8-K) that the step "fully complied" with its term loan agreement (Chapter 13's Docket Diary in §13.6 has the whole sentence). The intellectual property was, in plain English, the name on the label.

She stopped the paper there and handed out index cards. "It is 1 February 2017. The press release and the agreement are in front of you, and nothing else is. Write three things. Phi for this loan, in dollars. Which arcs bind. And whether you short the term loan now or wait."

*Your card, too: the leakage capacity in dollars, the arcs in the minimum cut, and now or wait. Write it before you read the others.*

Kaz's card was done in a minute: $\Phi = 0$. The parser had found no basket running from the non-guarantor bucket into an unrestricted subsidiary, so the cut sat on an arc of width zero, and a transfer through a zero-width arc is a transfer the agreement does not permit. "Either they used a basket my parser missed or they breached," Kaz said. "If they breached, the lenders win in court. I'd buy the loan if it drops on the headline."

Mags's card had four words on it: *Read the third provision.* "A company doesn't write 'fully complied' in the same paragraph as the transfer unless its lawyers have already walked the route, step by step, with a map. They had a route. Find it before you trade it."

Theo's card took the longest. He had the investments covenant open, and on the second pass he found what the parser had stepped over because it was not a basket with a number in it: a provision that let restricted subsidiaries which were not loan parties invest, in unrestricted subsidiaries, the proceeds of investments made into them under the non-guarantor basket. No dollar figure. No cap. A pipe from the bucket to the garage, as wide as whatever arrived in the bucket. "Then the two baskets upstream are the cut," he wrote. "Phi is \$250mm, which is about what a brand is worth. Short now."

Ines read the three cards and asked her question. "Who at this table had already read it?"

Nobody answered, so she did. "The borrower's lawyers. And the lenders had owned the same page for as long as they had owned the loan; the word 'secret,' which they would use later, suggests that few of them had noticed it. When the transfer was disclosed, they were the last players at the table to look at their own cards."

**Beat three: the car gets a lien (June 2017).** Ines moved the paper again. J.Crew's Form 10-Q for the quarter ended 29 April 2017, filed on 12 June, described the follow-on as a subsequent event. Affiliates would offer to acquire the outstanding PIK Notes, the holding-company notes that sat structurally behind the term loans, for up to \$190 million of new preference shares, up to 15% of the parent's common stock, and up to \$250 million of new notes secured by the transferred IP, alongside a \$150 million term-loan repurchase and a \$30 million add-on borrowing.

Kaz drew one more arc, out of the garage toward a box labeled `new secured notes`, and stood back. "So the sink isn't a sink. It has a creditor behind it, and the creditor used to be behind the term loan."

"Look at the repurchase," Theo said. "A hundred and fifty million of term loan bought back in the same package. Some of the lenders get paid to leave the room."

"And the rest get to read about it," Mags said. "Price is what you pay." How the exchange actually closed, in July 2017, is in Chapter 13's Docket Diary; Ines's paper stopped at the offer.

**Beat four: the word "secret" (7 September 2017).** The last line under the paper. An ad hoc minority group of senior term lenders had filed an amended complaint in New York state court over what it called the "secret trapdoor" (Locke Lord, October 2017).

Mags put her finger on the adjective. "The provision was in the agreement those lenders lent under, and in every copy they were sent. 'Secret' is what you call a page that was there all along, in a voice that carries better in front of a judge."

**The grading.** Ines took the paper off the screen and graded the cards against what happened, with Kaz redrawing the graph as she went. The route was the one Theo had found. As Torys (May 2019) describes it, the company used two investment baskets to move the interest, valued at \$250 million, into a non-guarantor restricted subsidiary (J.Crew Cayman), and then a third provision to move it on to the unrestricted subsidiary. King & Spalding's account identifies the first two as a \$150 million basket for investments in non-guarantor restricted subsidiaries and a \$100 million general investment basket. The third provision permitted non-loan-party restricted subsidiaries to invest in unrestricted subsidiaries the proceeds of investments made under the non-guarantor basket, and the lenders called it the "trapdoor." Kaz's drawing is the stylized model, and it holds both readings of the cut.

*In the formula.* Use a stylized three-node graph: $s \to N$ with two parallel arcs, $c_1 = 150$ (non-guarantor basket) and $c_2 = 100$ (general basket), and $N \to t$, the trapdoor. Ignore any direct $s \to t$ basket, so the model matches the disclosed route.

- *Before you read the trapdoor*, an analyst might treat $N \to t$ as capacity $0$ (nothing in the non-guarantor bucket was supposed to reach an unrestricted subsidiary). The min cut is $\{N \to t\}$, and $\Phi = 0$.
- *After you read it*, $c_{N\to t} = \infty$ (bounded only by what arrives at $N$). The min cut moves upstream to $\{s \to N\}$, and $\Phi = c_1 + c_2 = \$250$mm.

The trapdoor did not create new capacity. It moved the min cut upstream to two baskets that everyone had priced as "small baskets for foreign subsidiaries" rather than as leakage. A list-of-baskets parser sees \$150mm and \$100mm of investment capacity in non-guarantors and moves on. A flow parser sees \$250mm of capacity to unrestricted subsidiaries, and the IP was worth \$250mm. Figure 25.3 draws the two readings side by side.

![Figure 25.3: Reading the trapdoor as capacity zero puts the minimum cut on the trapdoor and gives Φ = 0 (top); reading it as unbounded moves the cut upstream onto the \$150mm and \$100mm baskets and gives Φ = \$250mm (bottom), the value of the IP that moved. Source: the \$150mm and \$100mm baskets as identified by King & Spalding and the \$250mm value of the IP interest as described by Torys (May 2019), both as quoted in §25.4.2; the three-node graph is the stylized model of §25.4.2, solved with the Edmonds-Karp routine of Listing 25.3.](assets/figures/ch25_jcrew_mincut.png)

Kaz's card was the first bullet, and Kaz graded it before Ines could. "My parser stores a basket when it sees a dollar sign. The trapdoor had no dollar sign, so it went in as a pipe of width zero. The most expensive clause in the agreement, and it was the only one that didn't state a price." A list-of-baskets parser makes that mistake by construction, which is why the grade was the useful kind of zero. The empty garage of beat one was the other half of the miss: a newly designated, previously empty entity class is exactly what a versioned diff of the debt disclosures (§25.5) is built to notice, and the parser had circled it as quiet.

Mags's card was right and could not be traded. "Read the third provision" is the correct instruction and not a position, and Mags accepted the grade with the expression of someone who has been right and flat before.

Theo's card had the right $\Phi$ and, Ines said, the crowded trade. By 1 February the transfer was public and every lender in the loan was reading the same agreement at once, so a single-name short was a bet on being faster than a room that had just woken up. The card that scored full marks was the one nobody at the table wrote, because it was about every other loan. Ivashina & Vallee, *Weak Credit Covenants* (NBER WP 27316, 2020; *Management Science*, 2025), hand-build contractual-weakness measures from 1,240 credit agreements and show that those measures explain the market-wide price reaction to the 2017 J.Crew restructuring. Document features got priced across the cross-section only *after* the market learned the trick. A desk with $\Phi$ already computed for every loan knew which names were next on the day the trick became famous, and a min-cut calculator that read pipes without dollar signs would have put J.Crew's IP route in the top tail of $\Phi/\text{EV}$ *before* December 2016, because the provision was already in the agreement. So the full-marks card said: rank the universe on leakage capacity, short the high-$\Phi$ loans against the low-$\Phi$ ones within a rating bucket, and size for the repricing, not the default.

"Short a loan how, exactly?" Mags said. "Nobody lends you a term loan." She was right, and the pair has to be built from things that can be sold. A loan fund or a CLO expresses the short as an underweight; a pod expresses it through the same issuer's bonds or single-name protection where they exist, and leaves the name alone where they don't. The within-bucket pairing removes the rating and sector beta, so what remains is the document; what leaks is every way the parser can misread the document, and §25.9 puts a price on that. (We do not reproduce J.Crew loan prices here; pull vendor marks for the 2016–2017 window before backtesting this, and remember §25.9's stale-quote warning.)

Then Mags told them where the plumbing breaks, which she does after every replay whether or not anyone asks. J.Crew's two upstream baskets were fixed dollar amounts. "Yours won't be. Plenty of the investment baskets written since are 'the greater of' a number and a percentage of EBITDA, and some are ratio-based, unlimited while a leverage test passes. Every pipe's width is a function of EBITDA now, so your $\Phi$ moves every quarter. Run it every night a compliance certificate or a 10-Q lands, not once a year when somebody remembers." The hockey stick of §25.3.4 is the reason: the widths inherit its kinks. Her second warning was about the patch.

*Blockers are commodity-specific cuts.* The "J.Crew blocker" drafted after 2017 typically bars transfers of material intellectual property to unrestricted subsidiaries. In flow terms, it sets the capacity to zero for one commodity (Material IP) on the arcs into $t$, and leaves cash and other assets untouched. So the right model is multi-commodity, and a blocker reduces $\Phi^{\text{IP}}$, not $\Phi$. The Chapter 13 feature `unsub_capacity_pct_ev` is $\Phi^{\text{non-IP}}/\text{EV}$ plus whatever $\Phi^{\text{IP}}$ survives the blocker's definitions. That last term is usually where the next fight is.

"The market patches the last trick, not the next one," Mags said. Buccola & Nini's hand-coding of more than 600 loan agreements found that only about 40% of pre-2020 loans restricted uptiers at all (the numbers are in the Trend Watch of §13.3.1): the lenders had bolted the IP door after J.Crew and left the seniority door open until Serta walked through it in 2020. So the desk reports $\Phi^{\text{IP}}$ beside $\Phi$, and keeps a column for the route nobody has named yet.

The sequel is short in this chapter because it is told elsewhere. J.Crew filed for Chapter 11 on 4 May 2020 in the Eastern District of Virginia (No. 20-32181), as Chapter 13's Docket Diary records, and the trick it made famous turned up on a bond stack in March 2023, when Carvana designated ADESA US Auction, LLC unrestricted under its unsecured indentures before its exchange offer and released its guarantees (Chapter 5's cold open).

"So the borrower's lawyers," said Kaz slowly, "solved a max-flow problem."

"By hand," said Mags. "In 2016. With a \$250 million objective function."

> **View From Another Seat.** *A CLO manager, then an opportunistic credit fund.* A CLO manager holding a loan like J.Crew's in 2017 would not have asked for $\Phi$. Its questions come from its own vehicle's indenture: does this loan stay out of the CCC bucket, and what does its mark do to the overcollateralization tests? Kundu (ESRB Working Paper 141, March 2023) states the constraint plainly: "A CLO faces a limit on loans rated CCC/Caa1 or below, typically set to 7.5%. The loans in excess of this percentage are marked at the lowest market value of the loans in the CCC/Caa1 bucket." A loan that slides toward CCC after a drop-down threatens the numerator of the OC ratio, and Kundu finds that the haircut-at-the-lowest-price rule leads managers to sell their *higher*-priced CCC loans first, a "contractual arbitrage" in which the forced seller often sells the wrong loan. For that seat a document score is a downgrade forecast, and the trade is to be out before the next test date, not to short a cross-section. The opportunistic credit fund stands on the other side of that sale. It reads the same document after the price has fallen and asks whether the market is over-extrapolating: is the leakage the headline implies still available, or has the route already been used, blocked or put in front of a judge? If its own reading says the fear is larger than $\Phi$, it buys what the CLO had to sell, and it is paid for patience rather than speed. One agreement, three questions. The systematic desk asks how much can leak; the CLO asks whether the mark breaks a test; the opportunistic fund asks whether the price already assumes more leakage than the document allows.

## 25.5 Versions and Diffs: Amendments Are Events

J.Crew moved value without changing a word of its agreement. The other way to move it is to change the words, and the oldest version of that trick is older than the leveraged loan market.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.86:* "The most common coercive tactic is to 'strip' the covenant protections of nontendering bonds. To implement this, the exchange offer will include a provision that tendering bonds will be deemed to have voted to authorize an amendment to the indenture of the original bonds, which effectively deletes all protective covenants."
>
> **Annotation.** The exit consent shows that a document is not a constant. The same indenture can protect you on Monday and be an empty shell on Friday, and the transition is itself the event to trade. So the parser has to *version* documents: every amendment, supplemental indenture, waiver and joinder is a new version with a filing timestamp, and the desk stores the parsed node vector for each version. The modern uptier (Chapter 13) is the exit consent's loan-market grandchild. A Required Lender amendment rewrites the pro rata sharing or the waterfall, and the diff between versions *is* the transaction.

### 25.5.1 Text diffs are blind where it matters

Cohen, Malloy & Nguyen, *Lazy Prices* (NBER WP 25084, 2018; *Journal of Finance*, 2020), showed that a portfolio short the firms that change their 10-K and 10-Q language and long the firms that don't earned "up to 188 basis points in monthly alpha" ("over 22% per year"). There was no announcement effect, and the changes also predicted firm-level bankruptcies. Kaz read the paper on a Sunday and arrived on Monday with the obvious port already running: the same similarity measure, pointed at every amendment and indenture supplement in the universe. It ran beautifully and found nothing, and the reason it found nothing is worth working out slowly.

> **Math, Gently.** *Counting words, and the angle between two documents.* Picture two shopping lists compared by a clerk who only counts items. List one says *the* three times, *shall* twice and *4.50* once. List two is identical except that *4.50* has become *5.25*. Write each list as a column of counts over the four words the two lists use between them: $(3, 2, 1, 0)$ and $(3, 2, 0, 1)$. That column is a *count vector*, an arrow in a four-dimensional space, and two documents count as similar when their arrows point the same way. The measure is the cosine of the angle between the arrows. Multiply matching entries and add them up (the *dot product*: $9 + 4 + 0 + 0 = 13$), then divide by the two arrows' lengths, each $\sqrt{9 + 4 + 1} = \sqrt{14}$, so their product is 14. The cosine is $13/14 = 0.93$, and the clerk reports the lists as 93% alike. On a six-word list one swap is loud. Now let the list be a credit agreement of 150,000 tokens, in which "the" alone turns up thousands of times. The arrow becomes enormous while the swapped entry is still a single 1, and the cosine moves by about four parts in ten million. The clerk cannot tell 4.50 from 5.25, because to the clerk they are just two different words that each appear once. A classical inequality, Cauchy–Schwarz, guarantees that a long document's arrow is long, and that guarantee is the whole proof below.

Here is the general result. Let $x \in \mathbb{N}^d$ be the token-count vector of an agreement with $n = \sum_i x_i$ tokens over a vocabulary of size $d$. An amendment that changes the leverage ratio from "4.50" to "5.25," where "4.50" appeared once and "5.25" never, moves cosine similarity by

$$
1 - \cos(x, x') = \frac{1}{\|x\|^2} \le \frac{d}{n^2}.
$$

For a 300-page agreement with $n \approx 150{,}000$ tokens and $d \approx 10{,}000$, the bound gives $1 - \cos \le 4.4 \times 10^{-7}$. At Halyard's $\mathcal{E} = \$266.7$mm, the same edit adds $0.75 \times 266.7 = \$200$mm of ratio capacity. The most expensive token in the document moves cosine similarity by less than one part in two million. Figure 25.4 sets the two measuring sticks against each other.

![Figure 25.4: Swapping one token for another moves a 150,000-token agreement's cosine similarity by about 4 × 10⁻⁷, and it would take roughly 155 amended occurrences of the ratio to move it by 1% (left), while the same edit from 4.50x to 5.25x adds \$200mm of ratio-basket capacity (right). Illustrative: the §25.5.1 count-vector model with 150,000 tokens over a 10,000-word vocabulary (‖x‖² ≈ 2.4 × 10⁶), and Halyard's covenant EBITDA of \$266.7mm against \$900mm of first-lien net debt.](assets/figures/ch25_token_vs_capacity.png)

*Lazy Prices* works on 10-Ks because the informative edits there are rewrites of whole risk-factor and litigation paragraphs. Covenant edits are numeric and surgical. The diff that matters is on the parsed capacity vector $K(v)$, not on tokens. For versions $v_{k-1}$ and $v_k$ we define the **dollar-weighted blast radius**

$$
\Delta K_k = \sum_{u \in V} \big| K_u(v_k) - K_u(v_{k-1}) \big|, \qquad \text{signal}_k = \frac{\Delta K_k}{\text{EV}},
$$

and keep the signed per-node changes alongside it, because a capacity *reduction* (a lender win in an amend-and-extend) and a capacity *increase* (a sponsor win) trade in opposite directions.

#### The Full Derivation: one swapped token

The amendment swaps one token for another, $x' = x - e_i + e_j$, where $e_i$ is the unit vector for "4.50" and $e_j$ the one for "5.25." In the common case "4.50" appeared once ($x_i = 1$) and "5.25" never ($x_j = 0$). Then

$$
x \cdot x' = \|x\|^2 - 1, \qquad \|x'\|^2 = \|x\|^2 - 2 + 0 + 2 = \|x\|^2,
$$

because the dot product loses the single matching count on "4.50," and the new vector's squared length loses $1^2$ on that coordinate and gains $1^2$ on the "5.25" coordinate (the middle terms are $-2x_i + 2x_j + 2 = 0$ written out). So the two arrows have the same length and

$$
1 - \cos(x, x') = 1 - \frac{\|x\|^2 - 1}{\|x\|^2} = \frac{1}{\|x\|^2} \le \frac{d}{n^2},
$$

where the inequality is Cauchy–Schwarz, $\|x\|^2 \ge n^2/d$: applied to $x$ and the all-ones vector, it says $n^2 = (\sum_i x_i)^2 \le d \sum_i x_i^2$. The longer the document, the longer its arrow, and the less any one token can turn it.

### 25.5.2 Case Study: Windstream, Aurelius, and One Defined Term (2015–2019)

*Facts* are in the cold open (§25.0), and the swaps side, from the 15 to 0 votes to the auction, is in §24.8.3. Two docket details belong here because a parser needs them: the case is S.D.N.Y. No. 1:17-cv-07857 (CourtListener docket 6169562, Doc. 245 for the findings), and the appeals Kaz misread were *In re Windstream Holdings*, 7:20-cv-04276 and 7:20-cv-05529, dismissed as equitably moot on 2021-06-23. Windstream argued publicly that Aurelius was net short through CDS, and the "net-short activism" debate that followed belongs to Part VI.

*The grading is fictional, like the parser runs and the dialogue; the holdings are Judge Furman's as summarized in §25.0, and the swaps facts are Chapter 24's.*

On the Tuesday after the replay ROBO finished parsing the 2013 indenture, and Ines took the three index cards out of her jacket pocket, still unread, and laid them face up next to the parser's output.

Kaz's card said \$0. The parser had walked the definition graph exactly as §25.2 builds it. The covenant node "Limitation on Sale and Leaseback Transactions" depends on the defined term "Sale and Leaseback Transaction," which depends on who transfers the property and who leases it back. To fill in the "who," the parser had gone where a parser goes, to the master lease's signature block, and found the parent, which sits above the issuer and outside the covenant's reach. The node evaluated to `NotApplicable`. "A node that doesn't apply is worth nothing," Kaz said, "so the term cuts for the company and you hold the notes." Kaz's parser had also accepted the \$553.7mm of November 2017 notes as Additional Notes of the series, because the issuer's own paperwork called them that.

Theo's card was the definition copied out by hand, with two phrases circled, *transfers* and *leases back*. Under it he had answered the "who" the way a restructuring banker answers it, by asking which entity owned the network before the spin and which entity still ran traffic over it every morning. Both answers were the operating subsidiaries. `Restricted`. "Which way it cuts: for the noteholders, legally. What I do with the 6 3/8s:" and there the card ran out, which Ines graded as honest.

Mags's card was a single question: *Who pays the judgment?*

Ines read the holdings back to them. The subsidiaries had sold and leased back, and the parent's signature did not change the substance; the November notes were not Additional Notes; the acceleration stood. The court had taken the economic reading of both defined terms, the one about the lease and the one about the series.

"My parser read the signature block," Kaz said. "The judge read the network." Kaz's card had the worst kind of error, an answer that was formally correct and economically wrong, produced with complete confidence. The Additional Notes miss was the same error in a second costume. A label in a supplemental indenture is the issuer's claim about a defined term, not proof that the term is satisfied, and in a fight about votes in a series, which notes belong to the series is the whole fight. Theo's card had full marks on the term and nothing on the trade.

Mags's question was the trade, and nobody got full marks on it. The judgment Aurelius described as \$310.5 million plus interest arrived ten days before the Chapter 11 petition, so the noteholders who won the covenant fight won a claim against a company in bankruptcy. The defined term said who would win the argument. It did not say whether the borrower could survive losing it, and that is a credit question, which Chapters 5 and 6 own. A card that says "the covenant binds, so the notes accelerate, so the company files, so the trade is about recoveries and the swaps calendar, not about being right" is the full-marks card in hindsight. Ines admitted that nobody writes that card on 12 October.

The lesson for the spec is the one the cards split on: *entity resolution in the definition graph has to be economic as well as formal*. Every node that turns on a party ("the Borrower or any Restricted Subsidiary") needs both a formal binding and an economic binding, and a flag when they disagree. On Windstream the disagreement flag would have been the alert.

It would also have been an early one. The 2015 spin and master lease were public, and a transaction-to-node matcher run on the 8-K announcing the transaction would have hit "Sale and Leaseback Transaction." That node's blast radius included acceleration of the whole series, so it belonged in the legal-risk queue with a dollar exposure attached, not in a footnote. One defined term was worth \$310.5 million plus interest by the winner's count, which makes Windstream about as clean an example as exists of why the definition graph, not the keyword index, is the unit of analysis.

The other thing the case teaches arrives through the docket rather than the document, and it is where the rest of this chapter goes. From September 2017 the clock was public. The notice of default went out on 21 September; the cure period was tolled to 7 December; the trustee asked the court for a declaratory judgment; and the Determinations Committee twice refused, 15 to 0, to find a Failure to Pay. A docket-driven state machine (§25.7.2) would have carried every one of those states, with dates. And the dates mattered for money, because standard swaps mature quarterly: five quarterly maturities, 20 December 2017 through 20 December 2018, fell between the acceleration and the ruling, protection bought for those dates expired inside the gap and never paid, and the Committee refused to backdate. Contracts still alive on 25 February 2019 paid. Chapter 24 (§24.8.3) tells the swaps side, and it is the calendar that any bond-against-protection package on Windstream had to survive. Here the lesson is about plumbing: the people who read the docket every morning knew which contracts were dying.

## 25.6 The Docket as an Event Stream

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.285:* "A bankruptcy is a legal process before a bankruptcy court, with virtually all information associated with the process in the form of filings listed on the case docket of the relevant court."
>
> **Annotation.** For a quant this is the best sentence in the distressed literature: the whole state of a bankruptcy is a single append-only log. Moyer also counted how big the log gets. WorldCom's docket ran to "9,686 filings totaling over 100,000 pages" between July 2002 and June 2003, and PACER documents came with "per-page charges" (p.387, nn.28, 30). At today's \$0.10 per page, a 100,000-page docket costs at most \$10,000, and less once the \$3-per-document cap clips the long filings. So the binding constraint is parsing, not purchasing. A desk can afford to be a RECAP contributor rather than a free rider.

Two pages later Moyer says why somebody has to read the log every morning, and it is the sentence Windstream's fourteen months illustrate.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.287:* "The bankruptcy docket must be monitored constantly because material events can occur which may not independently be announced... actions by various creditor constituencies that can give important insight on their strategies will also be filed, but otherwise not generally announced."
>
> **Annotation.** "Not generally announced" is an alt-data definition written before the term existed. The docket is a marked point process: entries arrive at times $t_1 < t_2 < \dots$, each with a mark (entry type, filer, attached documents, page count). The trading content is in the marks, and in the *sequences* of marks, which is why §25.7 builds a state machine rather than a keyword alert.

### 25.6.1 The plumbing, with the numbers that bind

*The week is fictional. The endpoints, limits and fees are as the SEC, Free Law Project and the federal judiciary publish them, as fetched on 2026-10-17 unless another date is given.*

The week before the Windstream replay, Ines gave Theo the docket feed as what she called a small project, which on this desk means a project whose smallness is the joke. Every number in it arrived the same way, as the thing that broke that day.

On Monday it was a leading zero. The SEC's EDGAR APIs need no key: `https://data.sec.gov/submissions/CIK##########.json` returns a filer's whole filing history and `.../api/xbrl/companyfacts/CIK##########.json` its XBRL facts. ROBO's first call came back empty because it had passed the Central Index Key as an integer, and the endpoint wants it zero-padded to ten digits. This is a classic ROBO bug, in the sense that ROBO has made it in every shop that has ever had a ROBO. Once the zeros were in, the feed was startlingly fresh: submissions update in real time, with a typical delay under a second, and the bulk zips are republished nightly at around 3:00 a.m. ET. Theo had tried the first call from a notebook in his browser, which failed for an unrelated reason (there is no CORS on these endpoints), so the fetcher moved to a server that day and has lived there since.

On Tuesday it was manners. Told to fetch every 8-K exhibit for the universe, ROBO did, as fast as the network allowed, under a User-Agent string that said `ROBO`, and by lunch the SEC was answering with refusals. The Webmaster FAQ is polite and exact about it: "our current maximum access rate is 10 requests per second," and a client declares a User-Agent containing a real contact mailbox. Theo's own address went into the header, which is how he learned that the SEC's fair-access rules make the person who writes the spec personally reachable.

On Wednesday it was a number that was too round. EDGAR full-text search (`efts.sec.gov/LATEST/search-index`) covers filings since 2001, exhibits included, and it understands quoted phrases, `OR` and `NOT`, `NEAR(n)` and trailing wildcards. It returns 100 hits a page. Theo's query for "open market purchase" reported exactly 10,000 hits, and Kaz, who distrusts any count that ends in four zeros, found the reason in a minute: the service caps `hits.total` at 10,000, so the number was a ceiling, not a count.

On Thursday it was CourtListener, Free Law Project's front end to the RECAP archive. Its REST API v4 documentation says, "By default, authenticated users may make up to 5 requests per minute, 50 requests per hour, and 125 requests per day." Free Law Project's post of 7 May 2026 says full API access now comes with membership, so the tier a desk actually lives under depends on whether someone has paid for it, and the token bucket of §25.6.2 has to be configured from what the account sees that day. The search types took the afternoon. A search with `type=r` returns dockets, each with at most three nested documents, which is how Theo's first Rule 2019 sweep found the cases and missed most of the statements; `type=rd` returns documents, and it is the only way to enumerate every Rule 2019 filing in a case. Counts are approximate above 2,000, and results are cached for ten minutes, which explains why the same query asked twice in five minutes gave the same answer after a new statement had posted. Theo started the historical backfill after dinner, and it died at 9 p.m. Pacific, because Thursdays from 21:00 to 23:59 PT are CourtListener's weekly maintenance window. The quarterly bulk CSVs would have spared him, except that they include dockets but not docket *entries*, so an entry-level backfill means API calls or a commercial arrangement.

On Friday it was money. RECAP Fetch (`/api/rest/v4/recap-fetch/`) will buy a document from PACER on the desk's behalf, at up to 30 requests per minute, using the desk's own PACER credentials, and the documentation is candid that "You'll still have to pay your PACER bill when it comes." PACER charges \$0.10 a page, no more than \$3 a document, waives fees of \$30 or less a quarter, and gives court opinions away free. Theo also learned that PACER passwords expire every 180 days, which he wrote down as a curiosity and which turned out to be an operations-calendar item rather than a footnote (the vignette in §25.6.2 has the week it mattered, at another shop). Free Law Project's Pray and Pay lets a user register interest in a document nobody has bought yet and be told when someone does, which Mags called "the most civilized thing that has ever happened to a bankruptcy court." "Back in my day," she said, "you paid a runner to stand at the clerk's window, and the runner had better taste in restaurants than in documents."

> **Trend Watch. The public side's whole information set, 2024–2026.** Everything in this feed is public: EDGAR, RECAP, and the PACER pages somebody has bought. That is a choice about which side of the information wall the desk sits on, and since 2024 the wall has had a regulator watching it. The SEC settled with Sound Point Capital Management on 26 August 2024 (\$1.8mm civil penalty), finding that the firm participated in lender groups and creditors' committees, sometimes received material non-public information about companies whose loans were in CLOs it traded, and lacked adequate written policies for that risk; on 30 September 2024 it settled with Marathon Asset Management (\$1.5mm) over policies not "reasonably designed to address" MNPI risk from ad hoc committee participation (§3.6.3 has both orders). Private-side holders come back to the public tape through two doors the feed can see. A loan holder that elects to be a public-only lender declines the agent's private materials so that it can keep trading, and lives with knowing less. A restricted creditor is freed by a cleansing 8-K, typically furnished under Item 7.01 with the term sheets and often the company's projections attached; Wolfspeed's 8-K of 23 June 2025 put the materials its creditors had seen under NDA up as exhibit 99.2 (§3.6.3). *What it means for the desk:* the cleansing 8-K is the richest public document a restructuring produces and the least surprising one to the people who negotiated it. The parser files it as its own document class, stamps the moment the restricted holders rejoin the flow, and reads its contents as news to everyone except the people who wrote them.

### 25.6.2 Rate limits as a token bucket

A published limit like "ten requests per second" sounds like a single number. In code it is two, and the gap between them is where feeds get blocked.

> **Math, Gently.** *Buckets, taps, and why "ten a second" can mean twenty.* Picture a bucket under a dripping tap. The tap adds $\rho$ cups of water every second, the bucket holds at most $b$ cups and overflows beyond that, and every request has to scoop out one cup before it may leave. When the bucket is empty, requests wait for the drip. The two numbers do different jobs: $\rho$ is the long-run pace, and $b$ is how much you can spend at once after a quiet spell. Take $b = 10$ and $\rho = 10$, which sounds like "ten a second." A bucket that has sat full overnight can spend all ten cups in the first instant, and the tap drips ten more during the next second, so twenty requests go out inside one second. Now take $b = 2$ and $\rho = 8$. The most that can ever go out in a second is the two cups already in the bucket plus the eight that drip in, so ten, never eleven. The rule hiding in the picture is *burst plus rate*: the most a bucket admits in a window is what it holds at the start plus what the tap adds during the window. The general statement is the lemma next.

Model a rate limiter as a bucket holding $z_t \in [0, b]$ tokens, refilled at rate $\rho$ tokens per second and capped at $b$. Each request consumes one token and is allowed only if $z_t \ge 1$.

**Lemma 25.2.** Over any interval $[t, t+h]$, a token bucket admits at most $b + \rho h$ requests.

*Proof.* At time $t$ the bucket holds at most $b$ tokens. During the interval at most $\rho h$ tokens are added. Every admitted request removes one token and the level never goes negative. So the number of admitted requests is at most $b + \rho h$. $\square$

*Quant-shop life (fictional composite): the data team at a systematic asset manager, the same shop as Paloma's substring night in §25.2.4, a year on. The people, times and counts are invented.*

The page went off at 03:07 on a Wednesday. Rhea, the data engineer on call that week, read it in the dark with one eye: `edgar_ingest: HTTP 403 rate 38% (threshold 5%)`. The nightly exhibit backfill had been slow, and the afternoon before somebody had sped it up the obvious way, by running four workers instead of one. Each worker had its own token bucket, configured exactly as the team's wiki said, $b = 2$ and $\rho = 8$. Each worker, inspected alone, was a model citizen. Together they were sending up to forty requests in a second to a service whose fair-access limit belongs to the client, not to the process, and the SEC had done what its FAQ says it will do. Rhea killed three workers, watched the 403s drain away, and went back to bed at 03:31. At nine she filed the ticket that moved the bucket into a shared store behind a lock. The fix was about forty lines. The code review took two days, because someone asked whether the lock should be per host, and the meeting to answer that question was longer than the fix.

The second incident was quieter, which was the problem. For six days in the spring the Rule 2019 feed reported nothing. The dashboard was green, the error log was empty, and at the Monday meeting the portfolio manager remarked that the restructuring world seemed to be having a calm week. It was not. The desk's PACER password had expired on day 181, PACER passwords lasting 180 days, and the RECAP Fetch job, which had been written to treat any failed purchase as "nothing new to buy," had been quietly finding nothing new to buy since. A junior analyst pulling one docket by hand for an unrelated memo found two verified statements the feed had never seen. The post-mortem template had a field labeled *Impact*, into which the first draft wrote "none known." Paloma, who runs the team now, changed it to "unknown," which is a different word, and added two action items. The first was a ticket titled *Alert on silence*: a feed that usually speaks pages someone when it has been quiet for longer than it has ever been quiet before. The second was a recurring calendar entry on day 170 of every cycle, *Rotate PACER password (ten days early)*, which became, by attendance, the most popular recurring meeting at the firm.

Both nights leave a sentence in any spec for a rate-limited feed. Burst plus rate means that guaranteeing at most $L$ requests in any window of length $h_0$ takes $b + \rho h_0 \le L$, which is why the box's $b = 2$, $\rho = 8$ is EDGAR's safe setting with $L = 10$ and $h_0 = 1$, and "rate 10, burst 10" is not; and because $W$ processes with private buckets admit up to $W(b + \rho h)$ in aggregate, the bucket has to be global, behind a lock or in a shared store.

For CourtListener's default tier the binding limit is the daily one. Polling $M$ dockets every $T$ days costs $M/T$ requests per day, so daily polling caps out at 125 dockets *before* any searches. The right architecture is therefore search-first (one call returns 20 hits with entry descriptions), alerts and webhooks for push, and a paid tier for backfills.

> **Ways This Blows Up.** (1) *Phrase counts are polluted.* "Open market purchase" in EDGAR full-text search is dominated by fund prospectuses and Form 4s in 2018, and by SPAC sponsor agreements in 2025's 8-Ks. The most expensive three words in finance are also some of the most boring. (2) *Exhibits are refiled*, so one agreement is counted many times. Dedupe by accession number plus a hash of the exhibit text. (3) *The 10,000 cap* truncates silently (`relation: "gte"`). (4) *Untested operators.* `NEAR()` queries with quoted phrases returned zero hits for 2018, 2021 and 2025 alike, which cannot be true. Validate every search operator against a known-positive filing before you trust a zero. (5) *Keyword precision.* In the live Rule 2019 search, one of the top five hits was an appellate motion to dismiss, so put a classifier on the entry text and the PDF's first page. (6) *Sealed placeholders and expired PACER passwords* look like silence. Alert on silence.

> **Trend Watch. Docket access, 2005–2026: from per-page phone-book to throttled API.** In 2005 Moyer described PACER fees as "reasonable" with "few practical alternatives" (Moyer_Distressed_Debt_Analysis p.286). Free Law Project's RECAP archive has run "since 2009." Its browser extension adds users' PACER purchases to a free mirror that now holds "tens of millions of PACER documents" (free.law/recap; no as-of date given). On 2026-10-17, a single anonymous CourtListener v4 search for `"rule 2019" "verified statement"` returned a count in the high hundreds to low thousands (1,868 on that day), with the newest hits dated September 2026. The feed is current to within weeks, and bankruptcy courts (`txsb`, `njb`, `miwb`, `okwb`) are in it. The shock came on August 7, 2025, when the Administrative Office of the U.S. Courts cited "escalated cyberattacks of a sophisticated and persistent nature on its case management system" (as reported by CNN). Secondary reporting says more than 20 courts then issued standing orders that sealed documents may be filed in CM/ECF but not viewed electronically. *What it means:* the public docket is now cheap, fast and machine-readable, and it can change shape overnight. A feed that silently drops sealed exhibits looks the same as a feed in which nothing happened.

## 25.7 The Rule 2019 Time Series and the Holder Graph

Federal Rule of Bankruptcy Procedure 2019, as amended in 2011, requires any group or committee of multiple creditors "acting in concert" to file a verified statement. Indenture trustees and agents are excused "solely for that reason." The statement must disclose, for each member, name, address and "the nature and amount of each disclosable economic interest," which is defined broadly enough to cover derivatives. Members who claim to represent others must also give the quarter and year each interest was acquired, unless it was acquired more than a year before the petition. A verified *supplemental* statement is due when a disclosed fact materially changes and the group takes a position. The sanctions have teeth: the court can refuse to hear the group or invalidate its votes.

The rule got this shape through a fight. In *In re Northwest Airlines* (Bankr. S.D.N.Y. 2007), Judge Gropper held on February 26, 2007 that the plain terms of the old rule required an ad hoc equity committee to disclose holdings. On March 9 he refused to seal the trading details, because "Rule 2019 was a disclosure rule that would be thwarted" if the other holders could not see them (Cleary Gottlieb alert memo, Mar 13, 2007). The old rule demanded "the amounts paid therefore." The 2011 amendment dropped price disclosure in exchange for broader coverage (CDS, total return swaps, shorts) and the acquisition quarter. So the Rule 2019 series carries **quantities and dates, never prices**. Prices have to be imputed.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.329:* "Usually the largest creditor schedule will list as the creditors only the indenture trustee for any bond issues, even though the indenture trustee probably will not actually own any bonds."
>
> **Annotation.** This is the entity-resolution warning in one sentence: the name on the claim is not the holder. A naive holder graph built from schedules has one giant node, the indenture trustee, which owns nothing and, as Moyer notes elsewhere, will "only do what they are clearly obliged to do" (p.76). Ad hoc groups exist because trustees are passive. Rule 2019 is how the desk sees through the trustee to the beneficial holders who will actually vote. The modern desk fuses three sources: Rule 2019 for the active holders, CLO trustee reports for the loan side, and 13F and N-PORT filings for the fund side. Each source has a different lag.

### 25.7.1 From statements to a panel

The first time Theo showed Ines a Rule 2019 statement, she skipped the names and went straight to the columns of numbers. "Their cost basis is their hand," she said. "Rule 2019 makes them show you half of it." The half it shows is quantities and dates. Turning those into a share, a concentration and a vote takes very little mathematics, and the other half of the hand, the price they paid, comes at the end of this subsection.

> **Math, Gently.** *Fuzzy slices, lumpy pies, and the one-third line.* Picture a pie chart of a \$1bn loan class in which every slice is labeled "approximately." A group's *share* is its slice: four members disclosing \$82mm, \$61mm, \$39mm and \$28mm hold \$210mm, or 21% of the class. Each figure was rounded to the nearest million, so each could be off by half a million and the total by up to \$2mm, and the honest statement is "between 20.8% and 21.2%." That is an *interval*, and it is the right object to carry. *Concentration* asks a different question: how lumpy is the whole pie? Square each holder's share and add the squares. Three holders at 50%, 30% and 20% give $0.25 + 0.09 + 0.04 = 0.38$; ten holders at 10% each give $0.10$. The sum is the Herfindahl–Hirschman index, HHI, and it has a friendly reading: it is the chance that two dollars drawn at random from the class belong to the same holder. Then the vote. A plan needs two-thirds of the dollars *that vote*, so a block holding more than a third of the voted dollars can stop it. If 60% of the class votes, the 21% group holds $21/60 = 35\%$ of the vote and blocks. If turnout rises to 70%, the same group holds $21/70 = 30\%$ and does not. Nothing about the group changed; the room got fuller. The formulas follow.

For group $g$, statement $k$ filed at $t_k$, and class $c$ with face $F_c$, let $h_{i,c,k}$ be member $i$'s disclosed face. Then the group's class share, net flow and holder concentration are

$$
\theta_{g,c}(t_k) = \frac{1}{F_c}\sum_{i \in g} h_{i,c,k}, \qquad \Delta h_{i,c,k} = h_{i,c,k} - h_{i,c,k-1}, \qquad H_c(t_k) = \sum_i \Big(\frac{h_{i,c,k}}{F_c}\Big)^2.
$$

$H_c$ is the `holder_hhi` input in §13.2.1. Statements say "approximately," so assume each of $n$ members rounds to the nearest $\delta$; then $|\hat\theta - \theta| \le n\delta/(2F_c)$. Carry that as an interval, not a point.

**Blocking arithmetic.** Under 11 U.S.C. §1126(c), a class accepts a plan if holders of at least two-thirds in amount and more than half in number *of the claims that vote* accept. If a fraction $\varphi$ of the class's face votes and the group, holding $\theta \le \varphi$, votes as a block, its share of the voted amount is $\theta/\varphi$. It can defeat acceptance on amount alone when

$$
\frac{\theta}{\varphi} > \frac13 \quad\Longleftrightarrow\quad \theta > \frac{\varphi}{3}.
$$

So low turnout lowers the blocking bar. With 60% turnout *(illustrative)* the bar is 20% of the class: a group above it blocks on amount, while a group at exactly 20% holds exactly a third of the vote, and a third is not more than a third. That knife-edge is why the rounding interval above is carried into the blocking flag rather than thrown away. Out of court, the analogous threshold is the agreement's "Required Lenders" (typically more than 50%), which is the $\theta_{\text{required}}$ of Chapter 13.

**Imputed cost basis.** This is the other half of Ines's hand. With disclosed acquisition quarters $q$ and a quarterly average price $\bar P_q$ from TRACE or loan marks, the imputed basis is $\hat c_i = \sum_q h_{i,q}\bar P_q / \sum_q h_{i,q}$. A group with a basis of 40 will take a plan at 55 that a basis-90 group will fight to the end, so two groups with the same share can be playing entirely different hands.

**Endogenous sampling.** Supplements are filed when holdings change *and* the group takes a position. So the timing of a filing is informative in its own right: a statement appears because something is about to happen.

### 25.7.2 The docket as a state machine

Classify entries into marks and map them to states: Quiet → Organized (first 2019 statement) → Contested (exclusivity, standing or lien-challenge motions) → Standstill (stipulated stays, mediation) → Plan → Confirmed. Figure 25.5 draws the chain with the Hughes case below it.

![Figure 25.5: The docket state machine runs from Quiet to Confirmed, and the Hughes Satellite Systems case of the Docket Diary below walked Organized to Contested in 31 days and Contested to Standstill in 10, each step marked by a docketed entry. Source: Hughes Satellite Systems Corp., Bankr. S.D. Tex. No. 26-90739, Docs. 154 (2026-08-10), 320 (2026-09-10) and 369 (2026-09-20), as cited in §25.7.2.](assets/figures/ch25_docket_state_machine.png)

> **Docket Diary. Hughes Satellite Systems Corporation, Bankr. S.D. Tex. No. 26-90739 (2026).** Doc. 154 (2026-08-10): "Verified Statement of Noteholders Pursuant to Bankruptcy Rule 2019... Exhibit A." Doc. 320 (2026-09-10, 40 pp.): "The Noteholder Group's Emergency Motion to Terminate the Debtors' Exclusive Periods Pursuant to 11 U.S.C. § 1121(d)(1)," hearing set for 9/28/2026, exhibits filed under seal. Doc. 369 (2026-09-20, 36 pp.): "Stipulated Order Staying Litigation and Investigations in the Chapter 11 Cases." That is Organized → Contested in 31 days and Contested → Standstill in 10. *The Ad Hoc Group, through counsel, in unison:* "We reserve all rights. Including the right to have reserved them earlier." Ines read the sequence aloud: "A bet, a raise, and both players agreeing to check it down." (Facts beyond the docket entry text are not stated here.)

Thirty-one days from organizing to attacking exclusivity. Kaz wanted to know whether that was fast, which is a question about a rate, and rates on a docket have a simple model.

> **Math, Gently.** *Events on a clock: Poisson counts, exponential waits, and rate as count over time at risk.* (Chapter 6 met this clock as a default hazard in §6.1.4; here it times lawyers.) A docket is a clock with labeled ticks: at each tick an entry arrives carrying a label (a 2019 statement, an exclusivity motion, a stipulated stay). That is a *marked point process*, and the simplest model of its ticks asks only how often they come. Suppose that while a group is Organized, an attack on exclusivity is equally likely on any day it has not yet happened, at a rate of $q$ per day. Two distributions then describe the same process from two sides. The *Poisson* distribution counts: how many attacks in a 30-day window? On average $30q$. The *exponential* distribution waits: how long until the first? On average $1/q$ days, and the chance of waiting longer than $t$ days is $e^{-qt}$. The exponential's defining quirk is that it has no memory, so a group that has sat Organized for fifty quiet days is no more "due" than one that organized yesterday. If you accept that, estimating $q$ is division. Across four cases, three groups moved from Organized to Contested and one is still Organized today, and together they spent 120 days in the Organized state. Three moves in 120 days at risk gives $\hat q = 1/40$ per day, a mean wait of 40 days. The still-quiet case adds its days to the denominator and nothing to the numerator, which is how the estimate stays honest about stories that have not finished. Hughes took 31 days, and under the model $1 - e^{-31/40} \approx 54\%$ of groups would have attacked by then: ordinary, not fast. Where the wait does have a memory (a statutory exclusivity deadline approaching, a hearing already on the calendar) the exponential is the wrong picture and the rate has to depend on time. The general estimator is next.

Treat the path as a continuous-time Markov chain with transition intensities $q_{ab}$. (These are $q_{ab}$ with two subscripts, distinct from inventory $q$.) With $N_{ab}$ observed $a \to b$ transitions and total time $T_a$ spent in state $a$ across a panel of cases, the maximum-likelihood estimate of each intensity is the box's division,

$$
\hat q_{ab} = \frac{N_{ab}}{T_a}.
$$

This is the right estimator for "how long after a group organizes does it attack exclusivity," and it stays honest about cases still in progress, because their time in state counts in $T_a$ even if no transition has happened yet.

#### The Full Derivation: the intensity MLE with censored spells

In a continuous-time Markov chain the time spent in state $a$ before leaving is exponential with total rate $\sum_{b \ne a} q_{ab}$, and the exit goes to $b$ with probability proportional to $q_{ab}$. A completed spell of length $\tau$ that ends in $b$ therefore contributes the density $q_{ab}\,e^{-\tau\sum_{b'} q_{ab'}}$ to the likelihood; a spell still running when the data stop (a *censored* spell) contributes only the survival term $e^{-\tau\sum_{b'} q_{ab'}}$, because all we know is that nothing happened yet. Multiplying across spells and cases and taking logs, the exponents add up to $-q_{ab}T_a$ for every pair, with $T_a$ the total time at risk in $a$, completed and censored alike, and each observed $a \to b$ move adds a $\log q_{ab}$. So

$$
\log \mathcal{L} = \sum_{a}\sum_{b \ne a}\big(N_{ab}\log q_{ab} - q_{ab}\,T_a\big),
$$

and setting $\partial \log \mathcal{L}/\partial q_{ab} = N_{ab}/q_{ab} - T_a = 0$ gives $\hat q_{ab} = N_{ab}/T_a$. The second derivative, $-N_{ab}/q_{ab}^2$, is negative, so this is a maximum. Dropping the censored spells instead would shrink $T_a$ and bias every rate upward, which on a docket means believing that fights start sooner than they do.

### 25.7.3 Case Study: Serta Simmons, Read From the Docket (2023)

Chapter 13 (§13.3.1) priced the 2020 uptier, Chapter 14 (§14.8.1) follows the whole case from 2020 to the 2026 remand, and Chapter 3 (§3.7) watched the uptier from a dealer's blotter. This section reads only the bankruptcy docket, the way the feed of §25.6 reads it, one entry at a time.

#### Long Scene: Serta, Day One, Two Statements (January – June 2023)

*A Friday replay on the fictional desk. The cards, Kaz's classifier and its 2 a.m. page, and all dialogue are invented. No one on the desk held, traded or was restricted in Serta's securities in 2023; Mags's 2020 history is Chapter 14's and is not retold here. The petition, docket entries, adversary proceeding, orders, lender names, deal terms and recoveries come from the court record, the Fifth Circuit's opinion and the law-firm accounts cited. No loan price is quoted.*

**Beat one: thirty-one months (23 January 2023).** Two Fridays after Windstream, Ines started the replay with a date and a subtraction. Serta Simmons Bedding had filed for Chapter 11 in the Southern District of Texas on 23 January 2023, No. 23-90020. The uptier had closed on 22 June 2020. "Thirty-one months," she said. "Long enough for everybody involved to have hired a second set of lawyers."

"A hundred and thirty-five weeks," said Theo, who had done the division in his head. "Ten of my 13-week models end to end, with a few weeks left over for the lawyers." The USB stick in his pocket did not comment.

She put the 2020 terms up once, as the Fifth Circuit's opinion later listed them, so that nobody had to argue from memory. The participating lenders, named as appellees, were Barings, Boston Management and Research, Credit Suisse Asset Management, Eaton Vance and Invesco Senior Secured Management. They had provided \$200 million of new money in exchange for \$200 million of first-out super-priority debt, and exchanged \$1.2 billion of their first- and second-lien loans for approximately \$875 million of second-out super-priority debt. (The \$734mm that the 2026 remand court used is the first-lien participants' share of that second-out; §5.6.2 reconciles the two.) Everyone else in the first lien had been left behind it.

Mags looked at the list of names for a while and said nothing about 2020, which for Mags is a speech. "You've heard my version," she said finally. "Read it the way the machine reads it. The machine doesn't have a version."

**Beat two: two statements before lunch (24 January 2023).** The day after the petition, Ines advanced the docket by one day and stopped. Three things had appeared. Doc. 69 was the original verified statement of the Ad Hoc Priority Lender Group, the side that had done the 2020 deal. Doc. 75 was the original verified statement of the Ad Hoc Group of First Lien Lenders, the excluded side. And in a separate adversary proceeding, No. 4:23-ap-09001, the fight over the 2020 transaction had been opened in the bankruptcy court on the same day. On RECAP, when this chapter's query ran, the two statements showed as "not available," because nobody had bought them.

"Doc. 75 is on the screen," Ines said, and handed out cards. "Write three things. Which class you want to own. What these two statements tell you about turnout and blocking. And what you'd pay for the PDFs." She held up a hand before anyone started writing. "And one house rule, because the last person who broke it was a backtest. Whatever you buy, you buy at a price somebody would have shown you *after* these entries posted. Not Monday's close, not the last print before the petition. A strategy that reads Doc. 75 and fills at yesterday's mark is trading out of tomorrow's newspaper."

*Your card, too: the class, what two day-one statements say about turnout and the one-third line, and your price for the PDFs. Write it before the others.*

Kaz's card was all arithmetic and no PDFs. "Own the excluded first lien. It's the cheap side, and the excluded lenders organized on day one, so they'll vote as a block. Two organized groups means high turnout. I don't need the documents; the docket text tells me who filed." Kaz's price for the PDFs: zero.

Theo's card went the other way on the class. "Own what the plan pays first. The excluded side's best weapon is the lawsuit in that adversary proceeding, and lawsuits outlive cases. Two statements on day one means the fight is certain before the first-day hearing ends, so the price of the excluded paper is a price for litigation, and I don't know how to price a court." On turnout he wrote that two organized groups would push the share of the class that votes toward the top of its range, and so push the blocking bar of §25.7.1 up with it: whoever wanted to block would need more than a third of a full room. His price for the PDFs: "Three dollars each, whatever they cost."

Mags's card said: *Buy every PDF. Then read 69 and 75 side by side and see whose name is missing from both.* "The names in a statement are who'll vote," she said. "The names that aren't there are who's going to sell to them."

Ines collected the cards and asked her question anyway. "Who at this table knows more than you?"

"Everyone who signed Doc. 69 or Doc. 75," said Theo. "They know what they hold, roughly what they paid, and what they've agreed with each other. We know they exist."

"Then those statements are them showing you half their hand," Ines said, "and somebody here was about to decline to look at it for three dollars." Kaz changed nothing on the card, so that it could be graded honestly.

**Beat three: the 2 a.m. page, and the flow (February – June 2023).** Kaz ran the rest of the docket overnight, through the desk's live alerting with the clock compressed, to see what the classifier would have done. At 2:04 a.m. Theo's phone lit up on his nightstand: *New Rule 2019 statement, Serta Simmons Bedding, Doc. 273.* He read it with one eye. Five utility creditors, one counsel, filed 9 February 2023: a perfectly valid Rule 2019 statement with no bearing on what anyone's term loan would recover. The classifier had been right that it was a Rule 2019 statement and wrong that Theo cared. At 2:11 it paged him again for Doc. 289, the Ad Hoc Equity Group's original statement of 10 February, and at 2:26 for Doc. 311, the utilities' statement of 13 February adding one more member. Theo wrote three lines on a sticky note before he went back to sleep; the sticky note is Exercise 6.

The pages that mattered were quieter. On 1 March the Ad Hoc Priority Lender Group filed an amended verified statement, Doc. 389, and on 21 June a second amended one, Doc. 1116. With Doc. 69, that made three dated snapshots of the same group, 24 January, 1 March and 21 June, and three snapshots of a group are its holdings time series. The diff between them is the flow, and that is the panel of §25.7.1 filling itself in. Whether the group grew or shrank between snapshots, and by how much, is inside the PDFs, which was the whole case for buying them. The timing was informative before anyone opened one. Doc. 1116 posted on 21 June, eight days before the company emerged, and a group that files a second amended statement a week before emergence is a group that is about to do something with its holdings, which is the endogenous sampling of §25.7.1 caught in the act. Between the second and third snapshots the adversary proceeding produced the entry Mags liked best: a stipulated order of 22 May 2023 concerning "North Star's status as a disqualified institution." "That's a fact about who's allowed to hold this loan at all," she said, "and no press release ever told anybody." A holder graph needs the disqualified-lender list as much as it needs the holders, because the list says who can never become one. The bankruptcy court's March ruling for the participating lenders and the June plan, with its indemnity for them, are in Chapter 14's account; the docket feed saw both as entries on the day they posted.

**Beat four: emergence, and the long tail (29 June 2023 – 31 December 2024).** Serta emerged from Chapter 11 on 29 June 2023. Ines put the recoveries next to the cards. By Skadden's tally of recoveries by coalition status, the participants recovered 100% and about 75%, and the non-participating lenders 0.6% to 2.4%.

Then she advanced the clock once more, past the end of the case. On 31 December 2024 the Fifth Circuit held that "the 2020 Uptier was not a permissible open market purchase within the meaning of the 2016 Agreement," twenty-three months after Doc. 75 had told anyone reading the docket that there would be a fight. The most expensive three words in finance had finally been priced, by a court, long after the case that made them famous was over.

**The grading.** Kaz's card lost on the class, through the whole of 2023, and lost on the PDFs. The docket text could say who filed but not what they held, and the statements were the only public source of the holdings: a share, an interval and a blocking flag all start from the numbers inside the PDF. "I assumed the free part was the important part," Kaz said. "It was the free part."

Theo's card won on the class through emergence, and Ines graded the reasoning rather than the outcome. "You didn't pick the winner. You declined to price a court, and the docket told you a court was coming. That's a fine reason to stay out of the excluded paper. It's not a reason to know how the appeal ends." His turnout line got full marks: when both sides of an uptier organize on day one, the room fills, and a fuller room raises the bar for blocking, which is the arithmetic of §25.7.1 running on real entries.

Mags's card was the only one that answered the third question correctly and the only one that bought nothing. The PDFs cost \$3 or less each through RECAP Fetch, the whole series less than lunch, and they were the panel. Her second sentence, about the names missing from both statements, was the best idea on the table and the hardest to automate, and it is where §25.8's claims-transfer feed picks up.

The reader's card is graded on the same three lines, and on one more thing: whether it would have survived the house rule. A card that buys the excluded first lien at the last mark before Doc. 75 has already broken it.

Ines closed with the hand history, as she always does. Every group that filed on 24 January knew its own cards before the desk could read the docket; the desk was always going to be one of the last players to see them. At three dollars a statement it did not have to be the very last.

"The docket told you there would be a fight on the first day," Mags said, putting her card in the recycling. "It didn't tell you who'd win, and it certainly didn't tell you when being right would pay."

Here is the whole sequence the CourtListener `type=rd` query returns for the case's Rule 2019 filings:

| Entry date | Doc. | Filer | What |
| :--- | :--- | :--- | :--- |
| 2023-01-24 | 69 | Ad Hoc Priority Lender Group | Original verified statement |
| 2023-01-24 | 75 | Ad Hoc Group of First Lien Lenders | Original verified statement (the excluded-lender side) |
| 2023-02-09 | 273 | Five utility creditors, one counsel | Rule 2019 statement |
| 2023-02-10 | 289 | Ad Hoc Equity Group | Original verified statement |
| 2023-02-13 | 311 | Utilities plus one more | Statement adding a member |
| 2023-03-01 | 389 | Ad Hoc Priority Lender Group | Amended verified statement |
| 2023-06-21 | 1116 | Ad Hoc Priority Lender Group | Second amended verified statement |

The table is what the classifier has to rank by class: the utilities' and the equity group's statements are valid Rule 2019 filings, and only three of the seven rows move a term-loan recovery.

Huang, Lewellen & Wang, *Creditor Coalitions in Bankruptcy* (SSRN 4854111; HLS Bankruptcy Roundtable, Feb 11, 2025) is what turns this feed from a who's-who into a return predictor. Working from Chapter 11 filings, "especially Rule 2019 disclosures," they find coalitions are more likely in large classes with dispersed ownership and illiquid debt, and that "coalition announcements are associated with increased bond prices," with significant positive returns across creditor classes. (Sample sizes and magnitudes are not reproduced here pending the paper's own tables.)

## 25.8 Claims Registers and the Transfer Feed

Rule 3001(e) creates the third layer. When a claim is transferred after a proof of claim is filed, "the transferee must file evidence of the transfer," *except* for claims based on publicly traded notes, bonds or debentures. The clerk mails notice, and the transferor has 21 days to object. So every trade claim, vendor claim, lease-rejection claim and bank-loan claim that changes hands after the bar date leaves a docket entry naming the transferor, the transferee and the face amount, but never the price. The bond side is dark. The resulting features are the share of class face transferred, the concentration of transferees (the same few funds buying everything), and the time from bar date to transfer. Each of these says something about who will be at the plan negotiation.

What the feed is *for* depends on the class it watches, and Mags explained it the Monday after the Serta replay, picking up her own unanswered sentence about the names missing from both statements. "The notice gives you face and no price, so everybody skips it. Read the transferee line instead. When the same three or four claims funds keep turning up as transferee in the general unsecured class, buying trade claims, vendor claims, lease-rejection claims, they aren't collecting. They're climbing. They want a seat on the creditors' committee, a blocking position in the class vote, or both, and you are watching a coalition form in public, one notice at a time, before anybody files a Rule 2019 statement about it." That is a practitioner's pattern, the restructuring-advisory read of how identity maps to a playbook, not a frequency this chapter has measured. "Back in my day," Mags added, "you found out who'd bought the trade claims when they walked into the committee meeting with better chairs than yours. Now the docket prints their names. This is better." The general unsecured (GUC) class matters twice. The U.S. trustee appoints the committee of unsecured creditors; the creditors do not elect it (11 U.S.C. §1102(a)(1)), and it "shall ordinarily consist of the persons, willing to serve, that hold the seven largest claims" (§1102(b)(1)), unless a prepetition committee that was "fairly chosen and is representative" stands in. And the same class votes on the plan. A transferee accumulating GUC face is therefore climbing the ladder that picks the committee and the ladder that decides acceptance at once, so the feed shows coalition formation in the class that sits at the table. Mags's rule for it was the desk's shortest spec of the week: put the transferees into the same concentration index and the same blocking flag as the Rule 2019 panel, so that a coalition shows up in one place whichever door it came in by.

The arithmetic is §25.7's, applied to transfers instead of statements. For entity $j$ in class $c$ with filed face $F_c$, net the notices in and out:

$$
\theta^{\text{xfer}}_{j,c}(t) = \frac{1}{F_c}\Big(\sum_{\text{in}} \text{face} - \sum_{\text{out}} \text{face}\Big), \qquad H^{\text{xfer}}_c(t) = \sum_{j:\ \theta^{\text{xfer}}_{j,c} > 0} \big(\theta^{\text{xfer}}_{j,c}\big)^2 .
$$

Both are floors. $H^{\text{xfer}}_c$ is a lower bound on the `holder_hhi` of §25.7.1 once affiliated funds are merged into one entity (the entity-resolution warning in the Moyer annotation above), because it ignores whatever each buyer held before the petition. And $\theta^{\text{xfer}}_{j,c}$ is a lower bound on $j$'s share of the class, because publicly traded notes escape Rule 3001(e) and, in a GUC class that includes unsecured notes, the feed never sees the bond side. A buyer whose $\theta^{\text{xfer}}_{j,c}$ climbs toward $\varphi/3$, with $\varphi$ the fraction of class face expected to vote, is approaching the blocking bar of §25.7.1 on amount (the separate headcount test in §1126(c) is a different question). One caution travels with it: $F_c$ is *filed* face, and claims objections and estimation will move the denominator, so carry the share as an interval, as §25.7.1 does for rounding. Whether a rising transferee concentration predicts anything about the plan is a hypothesis for the desk to test on its own docket panel, not a result cited here.

Moyer's starting point still holds: the petition's list of the 20 largest unsecured creditors "can often give insight on the possible composition of the unsecured creditor committee" (Moyer_Distressed_Debt_Analysis p.286). The plumbing is the hard part. On 2026-10-17, Kroll's restructuring portal returned HTTP 403 to an automated fetch, Epiq served a JavaScript-only shell, Stretto's case site was live, and Verita returned 503. Claims registers are the least API-friendly layer in the stack, so the desk's budget line for them is a headless browser, one adapter per claims agent, and an afternoon reading each portal's terms before anything is automated.

## 25.9 From Text to Signal: Error, Decay and Discipline

### 25.9.1 Classifier error is an IC tax

Every scene in this chapter has turned on a reader's mistake: the matcher that reversed 212 blockers overnight, the parser that read a pipe with no dollar sign as a pipe of width zero, the classifier that woke Theo for the utilities. Mistakes like these never appear as a line in the morning P&L explain. They appear as a signal that works less well than it should, and that loss can be measured in the currency the desk is paid in.

> **Math, Gently.** *Sensitivity, specificity, and one number for how much better than a coin.* Picture 1,000 credit agreements on a table, 50 with a trapdoor-style route and 950 without. The classifier is good. It catches 90% of the real trapdoors, its *sensitivity*, so it flags 45 of the 50. It correctly clears 95% of the clean agreements, its *specificity*, so it wrongly flags 5% of 950, about 47 or 48. Count the flags: roughly 92 or 93, of which 45 are real, so about half the flags are wrong before anyone has traded, and nothing is wrong with the classifier. Trapdoors are rare, and a small error rate on a big clean pile makes as many false alarms as there are true ones. That is the base-rate effect, which Chapter 3's box in §3.4.3 met as a disease test and Chapter 1's odds-form Bayes box in §1.3.3 does in your head. The new idea here is a single score for the classifier itself: *Youden's J*, sensitivity plus specificity minus one, here $0.90 + 0.95 - 1 = 0.85$. A coin flip that flags agreements at random, whatever they say, scores 0, because it flags the trapdoors and the clean ones at the same rate; a perfect reader scores 1. What the half-wrong flags do to the signal's correlation with future returns is the formula next.

Now the general version. Let $x \in \{0,1\}$ be a true document feature (for example, "has a trapdoor-type route") with base rate $\pi$, and let $\hat x$ be the classifier's output, with sensitivity $a = \mathbb{P}(\hat x = 1 \mid x = 1)$ and specificity $b = \mathbb{P}(\hat x = 0 \mid x = 0)$. Assume errors are independent of the forward return $r$ given $x$. Then the classifier's information coefficient is the true one, scaled by $J = a + b - 1$ and by a ratio of standard deviations:

$$
\text{IC}(\hat x) = J\,\frac{\sqrt{\pi(1-\pi)}}{\sqrt{\hat\pi(1-\hat\pi)}}\;\text{IC}(x), \qquad \hat\pi = (1-b) + J\pi. \tag{25.3}
$$

$J$ is Youden's index, and it is the exchange rate between classifier quality and alpha. Take $\pi = 5\%$, $a = 0.90$, $b = 0.95$. Then $J = 0.85$, $\hat\pi = 9.25\%$, and the IC falls to $0.639$ of its true value. By the fundamental law ($\text{IR} \approx \text{IC}\sqrt{\text{BR}}$) the desk needs $1/0.639^2 \approx 2.45$ times the breadth to break even. Those are the box's numbers, and the box's half-wrong flags are the same fact seen from the flag's side: $\mathbb{P}(x = 1 \mid \hat x = 1) = a\pi/\hat\pi \approx 0.49$.

This is the quantitative argument for the citation contract. Dahl et al. (2024), *Large Legal Fictions*, found hallucination rates of "roughly 58% to 88%" on verifiable questions about federal cases. Magesh et al. (2024) found that leading retrieval-augmented legal research tools still hallucinated "between 17% and 33% of the time." Either rate, plugged into (25.3), takes most of the signal away. So ROBO never emits a covenant value without a span, and the test harness scores span correctness, not fluency. For pre-training and evaluation there are public corpora: CUAD (510 contracts, 41 clause types, 13,000+ expert labels), LEDGAR ("over 60'000 contracts," "almost 100'000 provisions," from SEC filings) and LegalBench (162 tasks). None of them labels basket arithmetic, so the desk's gold set is hand-built from its own universe.

> **View From Another Seat.** *A non-bank electronic market maker.* For a shop that answers thousands of RFQs a day from a running hedge book, the IC tax belongs to somebody else, because the document reaches it in a different currency. It prices a block against its hedges, bidding when the CDX, ETF or rates hedge is cheap and the flow looks uninformed. What it cannot do is read a 300-page agreement in the seconds an RFQ allows, so around LMT rumors it widens or skips the name altogether (the characterization in this book's dealer-perspectives dossier, not a statement by any firm). Document risk arrives on its screen as width, not as a feature: the quote gets wider in exactly the names where §25.4's $\Phi$ is large, whether or not the shop ever computes $\Phi$. That helps the systematic desk twice. A name the fast market makers have stopped quoting is a name where the desk's own document score is about to be tested, and the width they charge is part of what it costs to trade the signal. The parser's answer arrives in hours. The dealer's arrives in milliseconds, priced as a spread.

On a multi-manager platform the same tax is paid one pair at a time, and the Pair Book records it.

> **The Pair.** *Pair Book entry PB-08, Dov Adler's pod, stressed with this chapter's parser. Vantress, Dov's pod and Wen Zhao are fictional composites; the positions, prices, fee and the screen's error rates are illustrative. Lumen, Level 3, their notes and the TSA dates are real and come from §13.5. A replay, cut off like Chapter 13's at Friday, 10 November 2023.* **Thesis and legs.** As opened in §13.5: the deal will protect the creditors whose collateral sits at Level 3 and leave the parent's unsecured holders behind them. Long \$15mm face of Level 3's 3.875% first-lien 2029s at 73; short \$10mm face of Lumen's parent-level unsecured notes, borrowed from an asset manager at 150 bp on market value. **What the hedge removes.** The family's spread beta, the telecom factor and most of the rates, by market-value DTS inside the issuer family (§13.5 has the ratio). **What idio remains.** Which entity the collateral reaches, which is a question of defined terms. On the definition graph of §25.2, terms like "Collateral," "Guarantor" and "Excluded Subsidiary" sit upstream of every lien grant, and their blast radius is the set of covenants a deal would have to touch to move value from one entity's creditors to the other's. The pair is long the entity those terms protect. **What leaks.** The reader, twice. The pod found the pair with a document screen that flags "collateral stays at the subsidiary," true for about one name in five; at a sensitivity of 0.85 and a specificity of 0.90, (25.3) leaves the screen about 0.69 of its true IC, so it needs roughly twice the breadth for the same information ratio. And the short is the expensive leg by construction: the bonds one document screen calls weak are the bonds every screen calls weak, so Wen's 150 bp is the fee before the crowd arrives, and the recall comes in the week of the vote. **What it costs.** §13.5's carry, about \$150k over four months, plus about \$250k of half-spreads in and out. The IC tax adds no line to the explain; it shows up later as a smaller capture ratio.

#### The Full Derivation: the IC exchange rate

Because the classifier's errors depend only on the true feature, its expected output given the truth and the return is a straight line in $x$: it flags a true trapdoor with probability $a$ and a clean agreement with probability $1 - b$, so $\mathbb{E}[\hat x \mid x, r] = (1-b) + (a + b - 1)\,x$. Covariance with $r$ passes through the conditional expectation (the law of total covariance, since $\hat x$'s own noise is independent of $r$), and the constant drops out:

$$
\text{Cov}(\hat x, r) = \text{Cov}\big(\mathbb{E}[\hat x \mid x, r],\, r\big) = J\,\text{Cov}(x, r), \qquad J = a + b - 1.
$$

An IC is a correlation, so divide by the standard deviations: $\text{IC}(\hat x) = J\,(\sigma_x/\sigma_{\hat x})\,\text{IC}(x)$. Both features are zero-one variables, with $\sigma_x = \sqrt{\pi(1-\pi)}$ and $\sigma_{\hat x} = \sqrt{\hat\pi(1-\hat\pi)}$, where the classifier's flag rate is $\hat\pi = a\pi + (1-b)(1-\pi) = (1-b) + J\pi$. Substituting gives (25.3). The ratio of standard deviations is the base-rate effect in the formula: when the feature is rare, false flags inflate $\hat\pi$ and with it $\sigma_{\hat x}$, so the same $J$ costs more IC.

### 25.9.2 Discipline and decay

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.156:* "There are so many choices that generating all possible features from alternative data would be a recipe for confusion and data mining."
>
> **Annotation.** A 300-page agreement has millions of n-grams, and some of them will backtest beautifully by accident. The defense is to pre-register: the document features are the typed nodes in the Chapter 13 table ($\Phi$, ratio headroom, builder availability, blocker flags) plus the docket states of §25.7.2, fixed *before* looking at returns. New features go through a written hypothesis first. This is the one place on the desk where bureaucracy is alpha.

Pre-registration guards the features. The prices the features are tested against need a guard of their own, and the clearest statement of it comes from a book about bonds and stocks rather than dockets.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.621:* "Indeed, bonds may react more slowly than stocks to news affecting a corporation... In this case, the relationship between equity momentum and subsequent returns of corporate bonds can be an illusion: Investors, trying to implement the strategy, would in reality be offered 'updated' prices of corporate bonds."
>
> **Annotation.** This is Ines's house rule from the Serta replay (§25.7.3) in its original habitat, equity signals meeting stale bond prices. Docket and amendment signals share the same trap. If a backtest goes long the loans whose priority-lender group just filed a 2019 statement and marks the entry at the last TRACE print or the prior day's loan mark, it is buying at a price no dealer would show after the docket entry posted. Measure signal decay as $\text{IC}(h)$ across horizons $h$, and enter at a quote that is executable *after* the event timestamp, with the delay set by the feed's actual latency (seconds for EDGAR, minutes to days for RECAP). Then apply the desk motto: IDO or it didn't happen. Strip the carry, rates and factor beta before you call anything alpha (Chapter 8).

## 25.10 The Covenant-and-Docket Engine

Every block of the engine answers a moment from this chapter, and it is easier to read the code as a list of those moments than as a list of functions. Paloma's 4:10 a.m. diff, with 212 blockers gone and no amendment filed, is why the first block consumes every span it matches. Theo's Monday frown at a \$65mm builder that was really \$10mm, and the 412 baskets ROBO found for "the greater of," are why the second turns sentences into typed functions and feeds them the whole quarterly tape. Kaz's J.Crew card, $\Phi = 0$ because a pipe had no dollar sign on it, is why the third reads baskets as a flow and names the cut. Kaz's Sunday port of *Lazy Prices*, which ran beautifully and found nothing, is why the fourth block is a test and not a tool. Rhea's 03:07 page and the six silent days after a password expired are why the fifth and sixth blocks share one bucket per host and refuse to mistake silence for peace. Ines's half of a hand is the seventh, Hughes's thirty-one days the eighth. And the 2:04 a.m. page for the Serta utilities, the classifier being wrong in the cheap direction, is the reason for the ninth, which prices the expensive direction and will not ship a number whose sentence it cannot find. The specification comes first, because ROBO builds exactly what the specification says.

### Specification for AI Implementation

*What ROBO built from the vague version.* "Extract all baskets" produced 412 matches for "the greater of," including two in "Excluded Taxes," with no units, no scope and no citations. ROBO did exactly what it was asked. The precise version follows.

**The Spec You Hand the Robot (engine).** Build a pipeline that (1) parses defined terms into a dependency graph with case-sensitive, word-bounded, longest-match-first, span-consuming term matching; (2) computes strongly connected components, evaluates the condensation in Tarjan emission order, and solves each cycle as a contraction fixed point, refusing any cycle whose Lipschitz constant is $\ge 1$; (3) turns basket spans into typed nodes (fixed, grower, ratio, builder) with explicit units (\$mm), scope and netting flags; (4) computes leakage capacity $\Phi$ by max-flow and reports the min-cut arcs; (5) diffs versions on the capacity vector, not tokens; (6) ingests EDGAR and CourtListener through one global token bucket with $b + \rho h_0 \le L$; (7) builds a Rule 2019 holdings panel with share intervals, flows, imputed basis and blocking flags; and (8) attaches a source span to every emitted number and asserts that the span exists in the document.

**Schemas.**

| Table | Key | Fields (units) |
| :--- | :--- | :--- |
| `documents` | `doc_id`, `version` | `accession`, `exhibit` (EX-4.x/EX-10.x), `filed_at` (UTC), `sha256`, `source_url` |
| `terms` | `doc_id`, `version`, `term` | `body`, `char_start`, `char_end`, `scc_id`, `eval_rank` |
| `edges` | `doc_id`, `version`, `u`, `v` | `is_self_ref` |
| `nodes` | `doc_id`, `version`, `node_id` | `node_type`, `params` (JSON; \$mm, ratios as x), `scope`, `nets_proceeds`, `span`, `section_path` |
| `capacity` | `doc_id`, `version`, `asof` | `ebitda_mm`, `K_mm` per node, `phi_mm`, `phi_ip_mm`, `cut_arcs` |
| `docket_entries` | `court_id`, `docket_number`, `entry_no` | `filed_at`, `description`, `doc_class`, `pages`, `recap_available` |
| `r2019_lots` | `case`, `stmt`, `holder`, `class` | `face_mm`, `acq_quarter`, `filed_at`, `rounding_mm` |

**Edge cases to handle.** Plural and possessive terms. Terms defined by reference to another document. Redefinitions "for purposes of this Article." Scanned exhibits with no text layer. Bracketed redactions and omitted schedules (Item 601). Negative or zero EBITDA, where ratio capacity is zero and the code must not divide. Netting language and netted-cash caps. Builder deficits. Infinite-capacity arcs. Approximate amounts in Rule 2019 statements. Censored docket spells. Sealed entries. The 10,000-hit cap on full-text search.

The blocks below run in order in one interpreter. All text and holders are synthetic.

Go back to the morning Theo spent on page 19. Kaz's first parser found a number and stopped. Theo's method was slower and better: open Section 1.01, read "Consolidated EBITDA," note every defined term inside it, and then do the same for each of those terms until the list stops growing. A human can do that for one agreement in an afternoon with a highlighter and a mild grudge. The desk has to do it for every agreement in the universe, and again whenever an amendment lands at 7:41 a.m. So the first block of the engine is Theo's afternoon compressed into milliseconds, with one extra duty his highlighter never had: it must announce, loudly, when the definitions loop back on themselves, because the EBITDA definition does.

Listing 25.1 builds the definition graph from a short synthetic Section 1.01 written for this book. The input is raw text. The outputs are a dictionary of definitions, a directed edge list, the strongly connected components, and a blast radius for any term. `parse_definitions` finds each line of the form `"Term" means ...` and stores the body together with its character offset, which is the citation anchor that every later number will point back to. `find_references` then scans each body for the other terms. The matcher is case-sensitive, word-bounded and tolerant of plurals. It takes the longest terms first and marks the characters it has consumed, so that "Unrestricted Subsidiary" cannot leave a "Restricted Subsidiary" hiding inside it. The listing asserts that the naive case-insensitive test would draw the wrong edge. `tarjan_scc` then collapses each loop into one component and emits components with dependencies first, which is the evaluation order for Section 25.3; the asserts check that ordering edge by edge. Two adjacency matrices confirm Lemma 25.1: the matrix over terms is not nilpotent, because loops exist, and the matrix over components is, because the condensation is a DAG. Finally `blast_radius` walks the edges backwards, so amending Consolidated EBITDA reaches the First Lien Net Leverage Ratio and amending Excluded Taxes reaches nothing.

The printout shows two loops, not one. Beyond the add-back loop through Consolidated EBITDA and Run-Rate Cost Savings, there is the J.Crew blocker: a Restricted Subsidiary is a Subsidiary that is not an Unrestricted Subsidiary, an Unrestricted Subsidiary may not own Material Intellectual Property, and that term is defined by reference to the Restricted Subsidiaries. A term that mentions itself is dropped from the edges and reported separately.

The block belongs in front of any basket arithmetic, on any agreement whose Section 1.01 follows the usual shape, and it knows the dictionary and nothing else. Its weak spot is the one-line body. The pattern reads from the opening quotation mark to the end of the physical line, so a definition that wraps onto a second line contributes only its first line, and one that begins "has the meaning assigned to such term in Section 7.02" contributes nothing. Every edge hiding in the lost text vanishes without an error, which makes it the substring night's quieter cousin: nothing crashes, and the graph is simply smaller than the agreement. The desk's habit is to count the parsed terms against the quoted terms in Section 1.01 before believing a graph.

*The full listing is [Listing 25.1 in Appendix F](#code-25-1).*

The graph tells ROBO which terms to evaluate and in what order. It does not say how many dollars the borrower can raise, and "thirty percent of what?" only gets answered once a sentence has become a function with units. Agreements state their baskets in several dialects, and each dialect has a trap that costs real money: a floor-or-percentage ratchet, a leverage test that forgot to say "without netting," an add-back cap measured on the wrong base, a cumulative builder computed over a trailing window. Theo's sticky note says a basket is a function. This is the block where the function is written down and tested, in millions, against the Halyard numbers of Section 25.3.4.

Listing 25.2 turns two synthetic covenant lines and the add-back definition from the previous listing into the capacity table of Section 25.3.4. Three small regular expressions turn sentences into typed objects. A `Grower` holds a fixed floor and a percentage of EBITDA and returns the larger. A `RatioBasket` holds the permitted multiple, the debt in scope, the cash it may net, and a flag for whether the cash proceeds of the new debt count; it returns zero when EBITDA is zero or negative, and it returns infinity when proceeds are netted and the test passes at all. `parse_baskets` converts dollars to millions and percentages to fractions, and sets the netting flag to true unless the clause contains the words "without netting." The scope debt of \$900mm is not in the text at all; the caller supplies it from the capital structure.

`addback_fixed_point` evaluates the cap on Run-Rate Cost Savings. If the definition says "after giving effect," it iterates the map of Section 25.3.3 until it stops moving, and it refuses any cap outside zero to one, because then the map is not a contraction and a human should read the definition. Otherwise it takes the simple minimum. The listing reads the cap and the "after giving effect" phrase from the Run-Rate Cost Savings body parsed in Listing 25.1, so the blocks are chained. On \$200mm of base EBITDA with \$80mm claimed, the add-back is \$66.7mm after giving effect and \$50mm before. Total incremental capacity moves from \$75.0mm to \$393.3mm, and a finite-difference check recovers the 4.85 slope. `builder_available` implements Equation (25.2) over the whole quarterly history, so losses count double and the result is floored at zero.

What comes out is a capacity vector the desk can diff and price, and what goes missing goes missing silently: a clause the expressions never match produces no node and no error. The sharper problem is infinity. A ratio test that nets the proceeds of the new debt really does allow unlimited borrowing, and a parser that reports so is reading a badly drafted document correctly. But the netting flag is set by the literal words "without netting," so a clause that reaches the same protection in other words comes back infinite, and a single `inf` poisons every sum it enters. On this desk an infinity is a ticket for a human to read the clause, never a number.

*The full listing is [Listing 25.2 in Appendix F](#code-25-2).*

"So the borrower's lawyers solved a max-flow problem," said Kaz, and the sentence is the whole design brief for the next block. A list of baskets cannot say how much value can leave the collateral pool, because the binding constraint depends on how the baskets connect. A \$150 million basket and a \$100 million basket look like small change for foreign subsidiaries until a third provision connects the room they open onto to the exit. The desk wants two outputs: a dollar figure for leakage capacity, $\Phi$, and, more usefully, the name of the basket that binds, because that is the sentence worth a lawyer's afternoon.

Listing 25.3 implements the Edmonds-Karp form of max-flow on a graph whose arcs are baskets. Each arc is a tuple of from-entity, to-entity, basket name and dollar capacity in millions. The function first builds a residual graph, adding a zero-capacity reverse arc for every forward arc so that flow sent down a poor route can be taken back later. Then it loops. A breadth-first search finds the shortest path with spare capacity from source to sink. The smallest residual on that path is pushed through, the residuals update, and the pushed amount joins the running total. When no path remains, the total is $\Phi$. One more search from the source, across arcs that still have slack, marks the reachable side, and the original arcs that cross from the reachable side to the unreachable side are the minimum cut, returned by basket name. If an uncapped route runs all the way from source to sink, the function returns infinity and an empty cut, because there is no basket to name.

The sample is the J.Crew route of Section 25.4.2: two parallel arcs from the loan parties to a non-guarantor restricted subsidiary, at 150 and 100, and a trapdoor arc onward to the unrestricted subsidiary. With the trapdoor at zero, the answer is zero and the cut is the trapdoor. With the trapdoor at infinity the answer is \$250mm and the cut is the two upstream baskets, whose capacities sum to the flow, as the theorem promises. The trapdoor created no capacity. It moved the cut onto baskets everyone had filed under "small."

It answers any question about a permissions network of the form how much can pass, and through which door, so long as the arcs are capacities in one currency. Its limit is in the last lines, and it is the one Mags raised after the J.Crew replay. The listing models a blocker by rerunning the same single-commodity graph, once with the trapdoor shut and once open, and relabelling the answers as "IP blocked" and "cash open." It does not solve a real multi-commodity flow. A blocker closes the Material Intellectual Property route and leaves cash routes alone, but the two commodities draw on the same \$250mm of basket capacity, so their capacities cannot be added. The pair is an upper bound for each, never a sum.

*The full listing is [Listing 25.3 in Appendix F](#code-25-3).*

*Lazy Prices* made money from the observation that firms which rewrite their filings underperform firms which don't, and the tempting port is to run the same similarity score on every credit-agreement amendment and sort by change. Anyone who has watched a sponsor amend a leverage multiple knows why that fails, and a desk that has never watched one learns it from a backtest, which is the expensive way. The amendment that moves \$200 million of capacity changes one number in a document of 150,000 words. Before ROBO builds a diff, it should be shown the size of the problem.

Listing 25.4 is that demonstration, and it is a test rather than a tool. It draws a synthetic agreement as a count vector over a 10,000-word vocabulary with 150,000 tokens, plants the token "4.50" exactly once and "5.25" not at all, and then swaps one for the other, which is the amendment. It computes the cosine similarity of the two versions and asserts two things: that one minus the cosine equals one over the squared length of the count vector, and that this sits below the Cauchy-Schwarz bound of vocabulary size over token count squared. The printed gap is about 4 x 10^-7, a number no sane similarity threshold will flag.

Then it measures the same edit the way the desk should. It builds a ratio basket with the amended multiple using the `RatioBasket` class and the add-back-adjusted EBITDA from Listing 25.2, and takes the difference in capacity: exactly \$200mm. One edit, two measuring sticks. The first reads zero for practical purposes, and the second reads a fifth of a billion dollars. That is the argument for diffing the capacity vector of Section 25.5.1 and not the tokens.

The identity is exact only because of the setup: the old number appears once and the new one never. In a real agreement a ratio literal recurs in the incurrence test, the pricing grid and a definition, and an amendment may touch one occurrence or all of them. The toy is the cleanest case for the argument (Exercise 4 asks how many occurrences it would take to matter), and the measurement is the capacity change, not the cosine. The block also draws its counts from the generator seeded in Listing 25.1, so run out of order it sees different random numbers, though the conclusion does not change.

*The full listing is [Listing 25.4 in Appendix F](#code-25-4).*

A desk that reads every filing every morning makes a great many requests before breakfast, to a regulator that has published its patience in one sentence: ten requests per second. The penalty for exceeding it is not a fine. It is a block, and a blocked desk reads nothing, which on a docket-driven strategy is indistinguishable from a quiet week. Rhea's four private buckets broke the limit one way at 03:07, and a burst allowance set equal to the rate breaks it another. Lemma 25.2 explains both, and the next block lets you watch them happen.

Listing 25.5 implements the token bucket of Section 25.6.2 and tests the lemma against it. `TokenBucket` holds a rate, a burst size and a current level. Each call to `try_acquire(now)` first tops up the level by the elapsed time multiplied by the rate, capped at the burst, then spends one token if at least one is there and reports yes or no. The clock is passed in, not read, which keeps the class deterministic and testable.

The test throws 6,000 request attempts uniformly across 60 seconds, a demand of 100 per second, at two buckets. The naive bucket has rate 10 and burst 10, which is what a developer would write after reading "ten requests per second." The safe bucket has rate 8 and burst 2, chosen so that the burst plus one second of refill stays within the limit of 10. `max_in_window` slides a one-second window across the admitted timestamps and finds the busiest one. The naive bucket reaches 19 requests inside a single second, comfortably under the lemma's ceiling of 20 and nearly double what EDGAR allows. The safe bucket peaks at 9. The listing asserts all three facts. It closes with the User-Agent header the SEC asks for, carrying a placeholder mailbox that must be replaced by a real one, and a function that builds the submissions URL by zero-padding the CIK to ten digits, which is the classic ROBO bug.

The bucket goes in front of every external host, one per host, set from that host's own published limit. The word that matters is "global." The class is a single object in a single process, and Rhea's page in §25.6.2 is what several private copies do to a budget; the docstring itself says to move the state behind a lock or into a shared store before production. A per-second bucket also says nothing about a daily cap, which is the problem the next listing walks into.

*The full listing is [Listing 25.5 in Appendix F](#code-25-5).*

A limiter in a test harness is not an ingest. The live version has to wait its turn, survive the 403s and 503s that public data sources hand out whenever their hosting is in a mood, and decide when to stop retrying and tell a person, because a feed that silently stops looks exactly like a quiet docket. (The list of ways this blows up in Section 25.6 ends with three words: alert on silence.) The smallest honest version of that loop is short enough to read in one sitting, and it is run against the two sources the engine needs.

Listing 25.6 is a sketch. It is not executed with the other blocks, because it needs network access, a real contact mailbox and a CourtListener token. `polite_get` creates a bucket at the safe EDGAR setting and wraps `requests.get` in three behaviors. It waits, polling every ten milliseconds, until the bucket releases a token. It sends the request with a thirty-second timeout. And if the status is 403, 429 or 503 it sleeps for two to the power of the attempt number, so one, two, four, eight and sixteen seconds, then tries again; any other bad status raises, and success returns the parsed JSON. After five failures it raises a `RuntimeError` naming the URL, which is where a real deployment would page a person.

Two calls follow. The first asks EDGAR full-text search for the phrase "unrestricted subsidiary" in 8-Ks filed from 2024-01-01 to 2026-10-17, which is the query behind the Trend Watch box in Section 25.2. The second asks CourtListener for Rule 2019 "verified statement" documents in the Serta Simmons docket, 23-90020, in the Southern District of Texas. The `type` of `rd` returns documents rather than dockets, which is the only way to list every Rule 2019 filing in a case.

As it stands it is a template for per-host adapters rather than an adapter, because one bucket serves two hosts. Eight requests per second with a burst of two is shaped for EDGAR. CourtListener's default tier allows 5 requests per minute and 125 per day, and this bucket would happily release a day's allowance in about sixteen seconds, so each host gets its own bucket from its own published limits. Retrying a 403 deserves suspicion too: against a portal that has decided you are a bot, five polite retries just make a longer log.

*The full listing is [Listing 25.6 in Appendix F](#code-25-6).*

Section 25.7 made a promise. The Rule 2019 statements an ad hoc group files disclose quantities and dates but never prices, and from them a desk can build a holdings time series, a blocking test and an imputed cost basis. Ines's line was that a cost basis is a hand and Rule 2019 makes the group show you half of it. The catch is one a poker player knows: the information arrives in installments, rounded, from people who file when they have a reason to. Below are two statements from one synthetic group and the arithmetic a desk runs on them before anyone calls the group's counsel.

Listing 25.7 starts from eight synthetic lots across two verified statements, filed 2026-01-15 and 2026-03-02, against a class with \$1,000mm of face. Each lot has a holder, a face amount and an acquisition quarter. A pivot sums face by holder and statement, which gives the panel of Section 25.7.1. From the panel the code takes three things. The first is the group's share of the class, $\theta$, which moves from 24% to 33%. The second is each holder's flow, the difference between statements: Holder_A adds \$30mm and a new member, Holder_D, arrives with \$60mm. The third is a rounding interval. Statements say "approximately," so each member's figure is good to half a million dollars, and with four members that is 0.2 points of the class.

`blocks` is the amount test of 11 U.S.C. 1126(c): a group defeats acceptance when its share exceeds a third of the face that votes. At 60% turnout, 33% blocks. At full turnout it falls short of 33.3% by a third of a point, which is the sort of margin lawyers bill for. The numerosity prong, more than half in number, is not coded. The imputed basis maps each lot's acquisition quarter to a synthetic quarterly average price and takes the face-weighted average per holder from the latest statement: 82 for Holder_A and 58 for Holder_D. Last comes a Herfindahl index of the disclosed holdings, labelled a lower bound, because a holder who never filed is invisible and every added holder can only raise the sum of squares.

Each new statement becomes a panel row within minutes of filing, and the panel describes the filers, not the whole class. The weak joint is the price map. Rule 2019 excuses the acquisition quarter for interests acquired more than a year before the petition, so some lots will arrive without one. Here a missing quarter becomes a missing price, which pandas skips in the numerator of the weighted average but not in the denominator, so the basis sinks toward zero with no warning: leave a single \$30mm lot unpriced and Holder_A's basis of 82 reads as 70.4. The production version refuses a lot it cannot price.

*The full listing is [Listing 25.7 in Appendix F](#code-25-7).*

Hughes took 31 days to go from Organized to Contested and ten more to reach Standstill. One case is an anecdote. A panel of cases is a rate, and a rate is what lets a desk ask how long after a group organizes it usually attacks exclusivity, and how nervous to be when day 60 passes with nothing on the docket. The estimator is a division. The interesting part is the denominator.

Listing 25.8 runs the maximum-likelihood estimator of Section 25.7.2 on a three-case toy panel. Each row is a spell: a case, the state it was in, the days it spent there, and the state it moved to, with a blank meaning it is still there. Case 1 mimics the Hughes sequence. Case 2 contests after 45 days and has sat in contest for 60 more. Case 3 has been Organized for 90 days and nothing has happened. The code sums days by state to get the exposure $T_a$, counts transitions by pair of states for $N_{ab}$, and divides. Organized to Contested comes out at 2 over 166 per day, because all 166 days count, including case 3's silent 90. Contested to Standstill comes out at 1 over 70. Drop the unfinished spells, the tempting move, and the first rate becomes 2 over 76, more than double, because only the cases that moved survive to be counted.

What it buys is an expected clock on a docket stage and a flag for a case that has outlived its peers. Three cases buy very little, and the model's assumption travels with every output: the intensity is constant within a state, so waits are exponential, and a hearing date set by a judge's calendar is not memoryless (the box in §25.7.2 says when that picture breaks). Censoring is the trap. Cases in progress carry the most recent information and the least complete one, and an estimator that discards them overstates how fast dockets move.

*The full listing is [Listing 25.8 in Appendix F](#code-25-8).*

Everything before this point assumed the clause classifier was right. It will not be. The question for the desk is not whether the classifier errs but what the errors cost in alpha, and Section 25.9.1 puts the price in one formula built on Youden's index. A formula is a claim, though, and a simulation is evidence. The engine also needs one last assertion before it ships a number: that the sentence the number points to exists. That assertion is the citation contract, and it is what keeps the model's mistakes from becoming the desk's.

Listing 25.9 has two jobs. The first simulates the IC tax of Equation (25.3). It draws 400,000 synthetic documents with a true feature at a 5% base rate, builds a forward return equal to the feature plus unit-variance noise, and generates a classifier flag with 90% sensitivity and 95% specificity, each flag drawn independently of the return once the truth is known. It computes the predicted retention from $J = 0.85$ and the flagged rate of 9.25%, and compares it with the ratio of correlations in the simulation: 0.639 predicted, about 0.647 simulated, inside the 0.03 tolerance the assert allows. At that retention you need roughly 2.45 times the breadth to break even. It also confirms the flag precision of 0.486, which is the number that surprises people who hear "95% specific": about half the flags are false.

The second job is the citation contract in miniature. For every parsed basket it asserts that the stored span is a substring of the covenant text, and it asserts that the phrase "calculated after giving effect to such adjustments" is in the Run-Rate Cost Savings body that the fixed point relied on. A number whose sentence cannot be found fails the build.

The simulation translates a validation-set confusion matrix into the extra breadth the desk has to find, and the assertions belong at every stage that emits a number. Both have a blind spot. The simulation builds in, by construction, that errors are independent of the return once the truth is known. If the classifier misses more often on unusual documents, and unusual documents are where the returns are, the errors correlate with the outcome and Equation (25.3) flatters the desk. And the span check proves the sentence exists, not that the number was computed from it, which is Windstream's lesson again: Kaz's parser could have cited its signature block perfectly.

*The full listing is [Listing 25.9 in Appendix F](#code-25-9).*


## 25.11 Desk Debrief

**Finder.** One row per tool: where its equation lives, the picture that explains it, the moment that shows when it breaks, and the code that computes it. The three real events line up with the three layers of text from §25.1.1, as promised at the start: J.Crew for the contract, Windstream for the amendment and the court, Serta for the docket.

| Concept | Equation | Intuition | Judgment (scene) | Code |
| :--- | :--- | :--- | :--- | :--- |
| Definition graph and blast radius | Lemma 25.1; reachability (§25.2.2) | Spreadsheet cells and the circular-reference warning (§25.2.1) | Paloma's 4:10 a.m. diff, 212 blockers gone: case-sensitive, longest match first, word-bounded, consume each span before shorter terms (§25.2.4) | [Listing 25.1](#code-25-1) |
| Grower and ratio baskets | $\max(X, p\,\mathcal{E})$; $\Delta^{*} = \max(0, m\,\mathcal{E} - F^{\text{sc}} + C)$, unbounded when proceeds are netted (§25.3.1–25.3.2) | Bathtub with a painted line (§25.3.2) | Mags reads "the greater of" aloud and Kaz finds the sponsor's argument (§25.3.1); the lender who refuses the clause against the desk that has to price it (§25.3.2) | [Listing 25.2](#code-25-2) |
| Add-back fixed point | (25.1) (§25.3.3) | A guess that corrects itself by a quarter: 80, 70, 67.5, 66.9, 66.7 (§25.3.3) | "A definition that grades its own homework"; a cycle with Lipschitz constant of 1 or more goes to a human (§25.3.3) | [Listing 25.2](#code-25-2) |
| Capacity convexity and the builder | $K(\mathcal{E})$, $\partial K/\partial\mathcal{E}$ (§25.3.4); (25.2) (§25.3.5) | Hockey stick with two bends (§25.3.4) | Each adjusted dollar buys 4.85 of capacity ahead of you (§25.3.4); the \$65mm LTM builder that was \$10mm: feed it the whole tape (§25.3.5) | [Listing 25.2](#code-25-2) |
| Leakage as max-flow | $\Phi = \min_{\mathcal{S}} c(\mathcal{S})$ (§25.4.1) | Pipes into a tank; the bottleneck moves upstream (§25.4.1) | J.Crew's three cards and the cross-sectional trade; blockers per commodity; recompute when EBITDA moves (§25.4.2) | [Listing 25.3](#code-25-3) |
| Capacity diffs, not token diffs | $1 - \cos(x, x') = 1/\lVert x\rVert^2 \le d/n^2$; $\Delta K_k$ (§25.5.1) | Shopping lists compared by a clerk (§25.5.1) | Kaz's port of *Lazy Prices* (§25.5.1); Windstream's formal against economic binding, and the flag when they disagree (§25.5.2) | [Listing 25.4](#code-25-4) |
| Token bucket | Lemma 25.2; $b + \rho h_0 \le L$ (§25.6.2) | Bucket under a dripping tap (§25.6.2) | The week the feed was built (§25.6.1); Rhea's 03:07 page and the six silent days: alert on silence (§25.6.2) | [Listings 25.5–25.6](#code-25-5) |
| Rule 2019 panel and blocking | $\theta_{g,c}$, $H_c$, $\theta > \varphi/3$, $\hat c_i$ (§25.7.1) | Pie labeled "approximately" (§25.7.1) | Serta's two day-one statements and three cards (§25.7.3); Mags on the transferee line (§25.8) | [Listing 25.7](#code-25-7) |
| Docket intensities | $\hat q_{ab} = N_{ab}/T_a$ (§25.7.2) | Events on a clock; count over time at risk (§25.7.2) | Hughes's 31 days were ordinary, not fast; censored spells stay in the denominator (§25.7.2) | [Listing 25.8](#code-25-8) |
| Classifier error as an IC tax | (25.3) (§25.9.1) | A thousand agreements, half the flags wrong (§25.9.1) | The 2:04 a.m. utilities page (§25.7.3); the dealer who prices documents as width and PB-08's screen at 0.69 of its IC (§25.9.1); Ines's house rule on entry prices (§25.7.3) | [Listing 25.9](#code-25-9) |

- **A basket is a function, not a sentence.** It maps the state of the company to \$mm and carries a scope, a netting flag and a source span. Without units, it didn't happen.
- **Parse definitions into a graph.** Evaluate it in Tarjan order and solve cycles as contractions. The EBITDA node has the largest blast radius in the document, so read it first and diff it every time.
- **"After giving effect to" turns a 25% cap into 33.3%.** Each add-back dollar buys $m + \sum p_j$ dollars of debt capacity, 4.85 at Halyard. Mags is right to distrust "adjusted."
- **Leakage is max-flow; the binding baskets are the min cut.** J.Crew's trapdoor created no capacity of its own. It moved the cut upstream onto \$250mm of "small" baskets.
- **Diff the capacity vector, not the tokens.** One ratio edit moves cosine similarity by less than $10^{-6}$ and capacity by \$200mm.
- **The docket is an append-only event log.** Use one global token bucket with $b + \rho h_0 \le L$. CourtListener's 125 requests a day means search and webhooks, not polling. Alert on silence.
- **Rule 2019 gives you quantities and dates, never prices.** Impute basis from the acquisition quarter, carry rounding as an interval, and remember that with turnout $\varphi$ a group blocks at $\theta > \varphi/3$.
- **Classifier error is an IC tax.** The tax rate is Youden's $J$ times a variance ratio, and at a 5% base rate half your flags are wrong. Span-cite everything.

**The Spec You Hand the Robot.**

```text
TASK: Covenant capacity + docket monitor for universe U (loans/bonds with EDGAR exhibits or open bankruptcy cases).
INPUTS: EDGAR exhibits EX-4.*, EX-10.* (versioned by accession, sha256); CourtListener v4 search/webhooks; RECAP Fetch
        (our PACER account); Rule 2019 statements; claims-transfer notices. All money in $mm, ratios in x, dates UTC.
STEP 1  Definitions -> graph. Case-sensitive, word-bounded, longest-match-first, span-consuming matcher; plurals.
        Tarjan SCCs; evaluate condensation in emission order; solve each cycle by fixed-point iteration; if the
        estimated Lipschitz constant >= 1, STOP and route to a human. Never guess a missing definition.
STEP 2  Baskets -> typed nodes {fixed, grower, ratio, builder, maintenance} with scope, netting flag, usage.
        Ratio with proceeds netting -> return inf and raise a red flag. Builder uses cumulative CNI (50% / -100%).
STEP 3  Entity graph -> max-flow Phi by commodity (IP, cash, other); report min-cut arcs and Phi/EV.
STEP 4  On each new version: dollar-weighted blast radius sum_u |K_u(v_k) - K_u(v_k-1)| / EV, signed per node.
STEP 5  Docket: classify entries (entry text + first page); state machine Quiet->Organized->Contested->Standstill->
        Plan->Confirmed; MLE q_ab = N_ab / T_a with censored spells. Rule 2019 -> panel of (holder, class, face,
        acq_quarter) with share intervals, flows, imputed basis, HHI lower bound, blocking flag theta > turnout/3.
RATE LIMITS: one shared bucket; EDGAR b + rho <= 10 per second with real-mailbox User-Agent; CourtListener <= 5/min,
        50/h, 125/day; backoff on 403/429/503; PACER password expiry alert at day 170.
OUTPUT CONTRACT: every number carries (doc_id, version, char_start, char_end); assert span text exists in source.
TESTS: the asserts in Blocks 1-8 of Section 25.10 must pass before any signal is published.
DO NOT: count phrases without dedupe; trust a zero from an untested search operator; enter backtests at prices
        stamped before the event; mine n-grams outside the pre-registered feature list.
```

### Exercises

1. **The four most expensive words, again.** Halyard's lawyers propose a 30% run-rate cap "calculated after giving effect to such adjustments." Compute the effective cap as a fraction of $\mathcal{E}_0$ and the gap versus the "before" reading. Show that the gap is $c^2/(1-c)$, and find the $c$ at which the "after" reading exactly doubles the "before" reading. (Answers: 42.9% vs. 30%; $c = 1/2$.)
2. **Break Kaz's regex.** Write five unit tests that defeat a naive term matcher: "Affiliated Lender," the possessive "Restricted Subsidiaries'," a term defined inline in parentheses, a redefinition "for purposes of this Article VII," and a PDF line-break hyphenation ("Unre-" / "stricted Subsidiary"). Which of these does Block 1 fail as written? Patch it without breaking the existing asserts.
3. **Move the cut.** Add a direct Loan Parties → Unrestricted investment basket of \$40mm to the J.Crew graph and cap the trapdoor at \$60mm. Compute $\Phi$ and name the min-cut arcs. Then add a J.Crew blocker and recompute $\Phi^{\text{IP}}$. (Answer to the first part: $\Phi = 100$, with cut {trapdoor, direct basket}.)
4. **How loud must a covenant shout?** Show that if "4.50" appears $k$ times and every instance is amended, $1 - \cos(x, x') = k^2/\|x\|^2$. With $\|x\|^2 \approx 2.4 \times 10^6$, how many times would the ratio have to appear for cosine similarity to move by 1%? (About 155. No agreement states its leverage ratio 155 times, although a few seem to be trying.)
5. **Is the group a blocker?** Block 6's group holds 33% of the class, with a ±0.2% rounding interval. Find the turnouts $\varphi$ for which "blocks" is robust, the turnouts for which "does not block" is robust, and the ambiguous band in between. Ines wants to know the most you would pay in PACER fees to resolve it. (Hint: \$3 per statement, so less than the coffee.)
6. **Spec ROBO into sleeping through the utilities.** ROBO is told to "page Theo on any new Rule 2019 statement." Write a three-line spec that stops it from paging him at 2 a.m. over the Serta utility creditors' statements but still pages for a second amended statement from the priority-lender group. State which fields of the entry it should key on.

### Deep-Dive Resource Graph

**Podcasts**
- **AI Can Tell Us Something About Credit Market Weakness** (*Odd Lots*, Bloomberg, December 4, 2025). Guest Dan Wertman of Noetica, whose product scans deal documents and measures linguistic and term trends over time: the commercial twin of the Section 25.10 engine, and the best audio on language drift as a credit-cycle feature. https://omny.fm/shows/odd-lots/ai-can-tell-us-something-about-credit-market-weakness
- **Divisive Debt Maneuvers; Bank Stress Returns** (*The Credit Edge*, Bloomberg Intelligence, April 27, 2023). Drop-down transactions that move assets out of lenders' reach, and the creditor lawsuits they provoke: the behaviour the entity-graph nodes of Section 25.4 are built to detect. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/divisive-debt-maneuvers-bank-stress-returns
- **Covenants: A Primer on J Crew Blockers and How Issuers Can Circumvent Them (Oct. 6, 2020)** (*Octus Radio*, October 6, 2020). The inception and mechanics of J.Crew blockers, the assets they most commonly catch and the "creative ways to circumvent" them; read it as a spec for the blocker-detection nodes of Section 25.4.1 and the J.Crew case in Section 25.4.2. https://share.transistor.fm/s/007e753e
- **The best and worst of high yield bond covenants** (*Cloud 9fin*, host Jennifer Munnings with Chris Osborne of 9fin, March 14, 2024). European restricted-payment builder baskets "are under threat", yet investors are better protected against "being J.Screwed" than before: named clause families to build parsers for in Section 25.3.5 and Section 25.4.2. https://share.transistor.fm/s/ca974c89

**Blog Posts**
- **RECAP Search Alerts for PACER Are Now Live!** (Free Law Project, June 18, 2025) and **How I Use RECAP Search Alerts for PACER Data** (Michael Lissner, June 23, 2025). Saved-search alerts that fire whenever new matching content reaches the RECAP Archive, plus the director's own usage notes: the turnkey version of the docket event stream in Section 25.6, and cheaper than building a poller to start. https://free.law/2025/06/18/recap-search-alerts-for-pacer/ ; https://free.law/2025/06/24/how-i-use-recap-alerts/
- **Full CourtListener Data Access via API Now Included with Membership** (Free Law Project, Jenifer Whiston, May 7, 2026). From May 7, 2026 any CourtListener member can use the full REST API v4, including the PACER/RECAP APIs that previously needed special permission; it changes the access assumptions of Section 25.6.1, so check the rate limits before coding the token bucket of Section 25.6.2. https://free.law/2026/05/07/api-included-in-memberships/
- **AI Tools and Assistants such as Claude Can Now Connect to CourtListener's Full Functionality** (Free Law Project, May 12, 2026). CourtListener as an MCP connector for Claude and other assistants (case law, PACER data, citation analysis, alerts), pitched as grounding against hallucinated case law: the agent-facing interface to the docket engine, and a cross-reference to Chapter 26. https://free.law/2026/05/12/courtlistener-is-now-available-inside-claude/

**Practitioner Writing**
- Torys LLP (May 2019), "The J.Crew 'trap door' and its implications for the future of leveraged finance": https://www.torys.com/our-latest-thinking/publications/2019/05/the-j-crew-trap-door-and-its-implications-for-the-future-of-leveraged-finance
- King & Spalding, "How did they do it: J. Crew": https://www.kslaw.com/attachments/000/008/521/original/How_did_they_do_it_J._Crew.pdf
- Locke Lord (October 2017), "J.Crew Group, Inc.": https://www.lockelord.com/newsandevents/publications/2017/10/jcrew-group-inc
- Cleary Gottlieb (March 13, 2007), *Bankruptcy Court Requires Ad Hoc Equity Committee Members to Submit Detailed Information on Holdings Under Bankruptcy Rule 2019(a)*.
- Paul Weiss / Practical Law (2025), *Covenant-Lite Loans: Overview* (PitchBook|LCD figures).
- Griffin, Nini & Smith, Harvard Law School Forum on Corporate Governance post (November 4, 2022).
- Huang, Lewellen & Wang, Harvard Law School Bankruptcy Roundtable post (February 11, 2025).
- Matt Levine, *Money Stuff* (Bloomberg Opinion), on J.Crew, Serta and "open market purchase." No specific column is cited here.

**Academic Papers**
- Smith & Warner (1979), *On Financial Contracting: An Analysis of Bond Covenants*, Journal of Financial Economics.
- Ford & Fulkerson (1956), *Maximal Flow Through a Network*, Canadian Journal of Mathematics.
- Ivashina & Vallee, *Weak Credit Covenants*, NBER WP 27316 (2020); *Management Science* (2025): https://www.nber.org/papers/w27316
- Cohen, Malloy & Nguyen, *Lazy Prices*, NBER WP 25084; *Journal of Finance* (2020): https://www.nber.org/papers/w25084
- Badawi, Dyreng, de Fontenay & Hills (draft 2021), *Contractual Complexity in Debt Agreements: The Case of EBITDA*.
- Griffin, Nini & Smith, *Losing Control? The 20-Year Decline in Loan Covenant Violations*.
- Huang, Lewellen & Wang, *Creditor Coalitions in Bankruptcy*, SSRN 4854111.
- Hendrycks, Burns, Chen & Ball (2021), *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review*: https://arxiv.org/abs/2103.06268
- Tuggener, von Däniken, Peetz & Cieliebak (2020), *LEDGAR: A Large-Scale Multi-label Corpus for Text Classification of Legal Provisions in Contracts*, LREC 2020.
- Guha et al. (2023), *LegalBench*: https://arxiv.org/abs/2308.11462
- Dahl, Magesh, Suzgun & Ho (2024), *Large Legal Fictions*: https://arxiv.org/abs/2401.01301
- Magesh, Surani, Dahl, Suzgun, Manning & Ho (2024), *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*: https://arxiv.org/abs/2405.20362

**Data & Code**
- SEC EDGAR: https://www.sec.gov/edgar. Full-text search UI: https://www.sec.gov/edgar/search/. API endpoint: `https://efts.sec.gov/LATEST/search-index`. Submissions API: `https://data.sec.gov/submissions/CIK##########.json` (CIK zero-padded to ten digits).
- CourtListener REST API (v4 documentation on wiki.free.law): https://www.courtlistener.com/help/api/
- RECAP Archive (Free Law Project): https://free.law/recap
- PACER: https://pacer.uscourts.gov/
- *U.S. Bank N.A. v. Windstream Services, LLC*, Findings of Fact and Conclusions of Law (Doc. 245, Feb 15, 2019): https://www.courtlistener.com/docket/6169562/245/us-bank-national-association-v-windstream-services-llc/
- CUAD code and fine-tuned checkpoints: https://github.com/TheAtticusProject/cuad
- Stretto case portal: https://cases.stretto.com/
- Federal Rules of Bankruptcy Procedure 2019 and 3001(e), and Regulation S-K Item 601 (Cornell LII text).

<!-- STATUS: COMPLETE -->
