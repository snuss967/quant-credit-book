# Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 25.x" section):
25.0 Cold open; 25.1 The document is the constraint set; 25.2 The definition graph (+ Trend Watch: LMT vocabulary on EDGAR);
25.3 Basket arithmetic (+ Trend Watch: covenants leave the building); 25.4 Leakage as max-flow (Case Study: J.Crew);
25.5 Versions and diffs (Case Study: Windstream); 25.6 The docket as an event stream (+ Trend Watch: docket access);
25.7 Rule 2019 time series (Docket Diary + Case Study: Serta on the docket); 25.8 Claims registers; 25.9 Text to signal;
25.10 Specification for AI Implementation; 25.11 Desk Debrief, Spec You Hand the Robot, Exercises; Deep-Dive Resource Graph. -->

## 25.0 Cold Open: Thirty Percent of What?

At 7:41 a.m. an 8-K landed on EDGAR: Halyard Holdings, the desk's fictional practice borrower (Chapter 26), filing Amendment No. 3 to its credit agreement as Exhibit 10.1. The term loan was quoted at 84 *(illustrative)*, which is the price at which people start reading.

Kaz had an answer in ninety seconds. "The general restricted payments basket is thirty percent. I searched for 'Restricted Payments' and took the first number after it."

"Thirty percent of what?" said Theo.

"Of Consolidated EBITDA. It's capitalized, so it's defined somewhere. I like that about lawyers. It's a typed language."

Theo scrolled to Section 1.01. The definition of "Consolidated EBITDA" started on page 19 and ended on page 30. It referred to "Consolidated Net Income," "Pro Forma Basis," "Specified Transaction," and "Run-Rate Cost Savings." The Run-Rate Cost Savings were capped at 25% of Consolidated EBITDA "calculated after giving effect to such adjustments."

"It's recursive," said Kaz, delighted. "The definition calls itself."

"It's a definition that grades its own homework," said Mags. "Back in my day the EBITDA definition fit on an index card, and we still didn't believe it. Now it has a table of contents."

Ines didn't look up. "Before you price that basket: who at this table already knows the number? The ad hoc group hired counsel in February. Their lawyers read Section 1.01 for a living. You're the last player at the table to look at your own cards."

Theo opened a ticket for ROBO: *Extract all baskets.* ROBO returned 412 baskets, one for every occurrence of the phrase "the greater of." Two of them were in the definition of "Excluded Taxes."

Theo stared at the list, then at the USB stick holding his old 13-week cash flow model, then back at the list. The question was not whether a machine could read Halyard's agreement. It was this: **how do you turn a 300-page credit agreement and a 4,000-entry bankruptcy docket into numbers a model can trust, with every number pointing back to the sentence it came from, before the people who wrote the sentences trade on them?**

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

The contract layer is censored, and the censoring is not random. Regulation S-K Item 601(b)(4)(iii)(A) lets a registrant omit any long-term debt instrument "if the total amount of securities authorized thereunder" does not exceed "10 percent of the total assets of the registrant and its subsidiaries on a consolidated basis," provided it agrees to furnish a copy on request. Item 601(b)(10)(iv) lets it "redact specific provisions or terms" that are not material and that it treats as confidential, and Item 601(a)(5) lets it omit schedules. Private, sponsor-owned and 144A-for-life issuers file nothing at all. In practice this means three things. Small facilities may never appear. The schedules most likely to be missing are the ones that hold the pricing grid and the excluded-subsidiary list. And any backtest on EDGAR agreements is a backtest on the public-filer subsample, so label it that way.

> **Desk Myth vs. Desk Reality.** *Myth:* "We'll point a large language model at the agreement and it will tell us the restricted payments capacity." *Reality:* A language model is very good at *finding the span* that defines a basket and very bad at being the place where arithmetic happens without a test. The desk splits the job. The model proposes spans with citations. A deterministic parser turns spans into typed nodes. A calculator with unit tests turns nodes into dollars. Every dollar carries a pointer back to the clause it came from. Chapter 26 calls this the citation contract. This chapter is what goes on the other side of it.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.32:* "The relatively few alternative data approaches that we have seen applied to quant credit strategies thus far include: analysing company linkages (suppliers and customers) from the Revere dataset...; bond short interest information; text-mining credit analysts' reports."
>
> **Annotation.** In 2022 one of the largest systematic managers listed text as an aside, and the text in question was *analysts' reports*, which are opinions about documents rather than the documents themselves. The gap since then is not mainly a story about better models. The documents were always free on EDGAR and RECAP. What changed is that LLM-assisted span extraction made covenant parsing cheap enough to run across a whole universe, while the 2017–2024 liability-management era made covenant capacity worth parsing at all. Text has moved from a footnote to a pipeline. The pipeline's competitive edge, though, is the boring part: dedupe, versioning, rate limits and units.

## 25.2 The Definition Graph: Legalese as a Typed Program

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

An agreement carries two structures, and parsers that conflate them break.

1. **The section tree** $\mathcal{T}$: Article → Section → clause (a) → sub-clause (i) → item (A). This is the abstract syntax tree in the compiler sense. A cross-reference like "Section 6.08(b)(iv)" is a path in $\mathcal{T}$. ROBO's hallucinated "(xiv)" in Chapter 26 was a path that doesn't exist, and a tree lookup would have caught it.
2. **The definition graph** $G = (V, \mathcal{E}^{\text{dep}})$: the vertices $V$ are defined terms plus operative provisions, and there is an edge $u \to v$ when the text of $u$ *uses* $v$. "Consolidated Total Net Leverage Ratio" points to "Consolidated Total Debt" and "Consolidated EBITDA," which points to "Consolidated Net Income," "Pro Forma Basis," and so on.

(The edge set is written $\mathcal{E}^{\text{dep}}$ because $E_t$ is equity value in this book's notation. For the same reason, from §25.3 on, covenant EBITDA is $\mathcal{E}$, calligraphic.)

To evaluate a covenant you must evaluate every term it reaches, and you must evaluate each term after its dependencies. Formally, you need a topological order of $G$.

### 25.2.2 Reachability, nilpotence and blast radius

Let $A \in \{0,1\}^{n\times n}$ be the adjacency matrix of $G$, with $A_{uv} = 1$ if $u$ uses $v$. Then $(A^k)_{uv}$ counts the walks of length $k$ from $u$ to $v$. The reachability matrix is

$$
R_{uv} = \mathbb{1}\Big\{\sum_{k=1}^{n} (A^k)_{uv} > 0\Big\}.
$$

**Lemma 25.1.** $G$ is acyclic if and only if $A$ is nilpotent, with $A^n = 0$.

*Proof.* Suppose $G$ is acyclic. A walk of length $n$ visits $n+1$ vertices, so by pigeonhole it visits some vertex twice. The segment between the two visits is a cycle, which is a contradiction. So there are no walks of length $n$, and $A^n = 0$. Conversely, if $G$ contains a cycle of length $\ell$, then for every $m \ge 1$ there is a closed walk of length $m\ell$, so $A^{k} \ne 0$ for infinitely many $k$ and $A$ is not nilpotent. $\square$

The lemma becomes a unit test: compute $A^n$ (or, more cheaply, run a depth-first search) and if it is not zero, the agreement has a circular definition you must handle explicitly.

The **blast radius** of an amendment that rewrites term $v$ is the set of everything that depends on it:

$$
\mathcal{B}(v) = \{u \in V : R_{uv} = 1\}, \qquad \beta(v) = |\mathcal{B}(v)|.
$$

Amend "Consolidated EBITDA" and you have touched every leverage ratio, every grower basket, the pricing grid, the excess-cash-flow sweep, and usually the definition of "Available Amount." Amend "Excluded Taxes" and you have touched very little. Section 25.5 weights $\mathcal{B}(v)$ by dollars of capacity, and that weighted blast radius is the most useful single number to compute on an amendment.

### 25.2.3 Cycles are real; condense them

Real agreements have cycles. Halyard's Run-Rate Cost Savings cap refers to Consolidated EBITDA "after giving effect to" the cost savings, and Pro Forma Basis refers to Consolidated EBITDA, which is calculated on a Pro Forma Basis. The standard fix is to compute the **strongly connected components** (Tarjan's algorithm, $O(|V| + |\mathcal{E}^{\text{dep}}|)$), collapse each component into a single super-node, and evaluate the resulting condensation, which is a directed acyclic graph by construction. Inside each component you solve a fixed point. Section 25.3 shows the fixed point for the add-back cap is a contraction, so the iteration converges, and it also shows the cap ends up larger than it looks.

### 25.2.4 Finding the vertices and edges

Vertices come from definition sentences: `"Term" means ...`, `"Term" has the meaning assigned to such term in Section 7.02`, and inline definitions buried in operative text (`(any such transaction, a "Specified Transaction")`). Edges come from matching the term dictionary against each definition body.

> **Ways This Blows Up.** *Substring matching.* The term "Restricted Subsidiary" is a substring of "Unrestricted Subsidiary." A parser that matches without word boundaries and longest-match-first will draw an edge from every unrestricted-subsidiary provision to "Restricted Subsidiary," reversing the most important distinction in the document. The same trap catches "Lender" inside "Affiliated Lender" and "Debt" inside "Consolidated Total Debt." The fix: sort the dictionary by length descending, match with word boundaries, and consume each matched span before trying shorter terms. Other ways this goes wrong: plurals ("Restricted Payments" for "Restricted Payment"); terms defined by reference to *another* document (the Intercreditor Agreement, the Existing Indenture); a term defined in Section 1.01 and quietly redefined "for purposes of this Article X"; and exhibits filed as scanned images with no text layer. Every one of these fails silently.

> **Trend Watch. The vocabulary of liability management on EDGAR, 2018–2026.** EDGAR full-text search covers "all EDGAR filings submitted electronically since 2001," including exhibits (SEC EFTS FAQ). Queries run against the full-text search API on 2026-10-17 (counts are *filings including exhibits*, not distinct agreements):
>
> | Phrase | 2018 | 2021 | 2025 |
> | :--- | ---: | ---: | ---: |
> | "Material Intellectual Property", all forms | 2,281 | 4,571 | 3,411 |
> | "Material Intellectual Property", 8-K | 847 | 1,225 | 1,157 |
> | "first lien credit agreement", 8-K | 223 | 343 | 146 |
>
> The phrase "unrestricted subsidiary" appears in 1,931 8-K filings from 2024-01-01 through 2026-10-17 (an exact count). *What changed:* J.Crew-blocker vocabulary in 8-K exhibits rose about 37% from 2018 to 2025, while 8-K filings mentioning a first-lien credit agreement fell to about 65% of their 2018 level. The 2021 all-forms spike comes from the SPAC wave (S-4 and S-1 registrations), not from loans. As a *crude* density, the ratio of blocker mentions to first-lien agreement mentions in 8-Ks went from $847/223 \approx 3.8$ to $1{,}157/146 \approx 7.9$. *What it means:* the public filer base for leveraged loans is shrinking as deals move to private credit (Chapter 17), while the agreements that remain are full of LMT defenses. Two cautions belong in the same box. The numerator and denominator are different document sets. And the API caps `hits.total` at 10,000, so a broad normalizer like "credit agreement" silently returns "≥10,000." The ratio is a picture, not a statistic.

## 25.3 Basket Arithmetic: From Clauses to Dollars

Theo's first rule on the desk, written on a sticky note over the second monitor: *a basket is not a sentence; it is a function from the state of the company to a number of dollars.* Write the function down, give it units, and test it.

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
| Builder | "the Available Amount at such time" | path-dependent; see (25.4) | starter, CNI share, equity credit |
| Maintenance test | "shall not permit the Total Net Leverage Ratio as of the last day of any Test Period to exceed..." | none; a breach is a default | $m$, test dates, cure rights |

Each node also carries a usage $U_j$, and availability is $K_j - U_j$. Reclassification language ("may divide, classify and reclassify") lets the borrower move usage between baskets after the fact. In practice that means usage is a decision variable for the borrower, not a fact for you.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.168:* "...the leverage covenant, which is usually structured to limit debt to a specified multiple of EBITDA... In complex multitiered capital structures, the leverage test may only address the layer in question. Thus a senior loan may specify that senior debt will not be more than, for example, 2.5x EBITDA, but may be silent on how much total debt is allowed."
>
> **Annotation.** In schema terms, *scope is a field, not a footnote*. A ratio node without its scope (total, senior, secured, first-lien) is a number without units. Moyer's example is a senior test silent on total debt. The 2026 equivalent is a first-lien net leverage incurrence test that is silent on junior secured debt. It permits a second-lien or unsecured layer, sometimes at a different ratio, and that layer is how a "4.50x" agreement ends up with 7x of total debt. Kaz's first parser stored `ratio = 4.5` and nothing else. ROBO, given that schema, reported that Halyard could not borrow another dollar of junior debt. Halyard borrowed another \$250mm of junior debt the following quarter *(illustrative)*.

### 25.3.2 The ratio basket, and the four words that stop a perpetual-motion machine

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

### 25.3.3 The add-back fixed point

Back to the cold open. Let $\mathcal{E}_0$ be EBITDA before run-rate add-backs, $A$ the add-back claimed, and $c$ the cap. Everything turns on one phrase.

- Cap measured *before* giving effect to the add-backs: $A \le c\,\mathcal{E}_0$.
- Cap measured *after* giving effect to the add-backs: $A \le c\,(\mathcal{E}_0 + A)$.

Rearranging the second, and using $0 < c < 1$,

$$
A(1 - c) \le c\,\mathcal{E}_0 \quad\Longrightarrow\quad A \le \frac{c}{1-c}\,\mathcal{E}_0. \tag{25.1}
$$

The gap between the two readings is $\frac{c}{1-c} - c = \frac{c^2}{1-c}$ of $\mathcal{E}_0$. At $c = 25\%$ the "after" reading allows add-backs of $33.3\%$ of pre-add-back EBITDA instead of $25\%$: 8.3 extra points of EBITDA from four words. Per word, that beats "open market purchase," which needed three words and a Fifth Circuit appeal (Chapter 13).

Equation (25.1) is also the general recipe for evaluating a cycle in the definition graph. Write the cycle as a map and iterate:

$$
A_{k+1} = T(A_k) = \min\big(A^{\text{claimed}},\; c\,(\mathcal{E}_0 + A_k)\big).
$$

$T$ is Lipschitz with constant $c < 1$, so by the Banach fixed-point theorem the iteration converges from any start, with error shrinking like $c^k$. The code in §25.10 evaluates every strongly connected component this way. If a component's map is *not* a contraction (estimated Lipschitz constant $\ge 1$), the definitions are ill-posed and the parser hands the component to a human. For Theo, that is a feature, not a bug.

### 25.3.4 Capacity is levered to add-backs

Total incremental debt capacity, from the ratio basket plus grower general-debt baskets $j$, is

$$
K(\mathcal{E}) = \max\big(0,\, m\,\mathcal{E} - F^{\text{sc}}\big) + \sum_j \max\big(X_j,\; p_j\,\mathcal{E}\big).
$$

Each term is a maximum of affine functions, so $K$ is convex and piecewise linear in $\mathcal{E}$: capacity accelerates as EBITDA grows. Where it is differentiable,

$$
\frac{\partial K}{\partial \mathcal{E}} = m\,\mathbb{1}\{m\,\mathcal{E} > F^{\text{sc}}\} + \sum_j p_j\,\mathbb{1}\{p_j\,\mathcal{E} > X_j\},
$$

and $\partial \mathcal{E}/\partial A = 1$ below the add-back cap and $0$ above it.

**Halyard, worked** *(illustrative)*. Take $\mathcal{E}_0 = \$200$mm, claimed add-backs of \$80mm, the 25% "after giving effect" cap, a first-lien net leverage incurrence test at $m = 4.50$x with existing first-lien net debt $F^{\text{sc}} = \$900$mm (proceeds not netted), and a general debt basket at the greater of \$75mm and 35% of Consolidated EBITDA. From (25.1), $A = \min(80, 66.7) = \$66.7$mm, so $\mathcal{E} = \$266.7$mm.

| | No add-backs | With add-backs |
| :--- | ---: | ---: |
| Covenant EBITDA $\mathcal{E}$ (\$mm) | 200.0 | 266.7 |
| Ratio capacity $\max(0, 4.5\,\mathcal{E} - 900)$ | 0.0 | 300.0 |
| General basket $\max(75, 0.35\,\mathcal{E})$ | 75.0 | 93.3 |
| **Total incremental capacity** | **75.0** | **393.3** |

At the margin, each dollar of add-back buys $4.50 + 0.35 = 4.85$ dollars of debt capacity, and every one of those dollars can sit ahead of you.

"This is why I don't trust anything called 'adjusted,'" said Mags. "Every adjusted dollar is worth almost five dollars of somebody else's priming debt."

Badawi, Dyreng, de Fontenay & Hills (draft 2021), *Contractual Complexity in Debt Agreements: The Case of EBITDA*, is the large-sample version of Mags's suspicion. They extract EBITDA definitions from 4,532 credit agreements (1996–2018), hand-code seven specific adjustments on a random subsample of 581 to build a permissiveness score from one (GAAP net income plus interest, taxes, D&A) to eight, and extend it out of sample with a Naive Bayes classifier. Mean permissiveness is 3.61 (s.d. 1.74), and it rises over the sample. More permissive definitions come with tighter covenant thresholds but *fewer* violations, and with more negative market reactions when a violation does happen. Sponsor-backed borrowers are more permissive. Two lessons carry over to the desk. EBITDA is the root of the definition graph, so it is the node whose blast radius is largest. And its complexity is itself a time series you can measure.

### 25.3.5 The builder basket, or the 13-week model gets a job

The builder ("Available Amount," "Cumulative Credit") is path-dependent. A common synthetic form: a starter amount $S = \max(X_s, p_s\,\mathcal{E})$, plus 50% of cumulative Consolidated Net Income from a reference date "taken as one accounting period" (or, if that cumulative figure is a deficit, minus 100% of it), plus retained equity proceeds $Q_t$, minus usage $U_t$. With cumulative CNI $N_t = \sum_{q \le t} \text{CNI}_q$, $N^{+} = \max(N, 0)$ and $N^{-} = \max(-N, 0)$:

$$
B_t = S + \tfrac{1}{2}\,N_t^{+} - N_t^{-} + Q_t - U_t, \qquad \text{available}_t = \max(0, B_t). \tag{25.2}
$$

The kink at $N_t = 0$ is asymmetric: slope $\tfrac12$ above, slope $1$ below, so losses count double. And because the formula is cumulative, an LTM window gives the wrong answer; you need the whole quarterly history from the reference date. Some agreements use a retained-excess-cash-flow builder instead, and some high-yield indentures use an EBITDA-less-a-multiple-of-fixed-charges alternative. These are different node subtypes with different inputs, so do not force them into one formula.

Here the running gag earns its keep. Theo's 13-week cash flow model, reborn as a state-space feature, forecasts next quarter's $\text{CNI}_q$, which forecasts $B_{t+1}$. That tells you how much builder capacity the sponsor will have on the next dividend date, before the sponsor's own treasury team has finished its spreadsheet.

### 25.3.6 Maintenance versus incurrence: two node types, two default semantics

Moyer describes the maintenance covenant as a performance milestone (for example, "'EBITDA for the third fiscal quarter will exceed \$X'") and notes that "where performance covenants are included, failure to comply with the requirement is a default" (Moyer_Distressed_Debt_Analysis p.174). In the graph, a maintenance node is evaluated on every test date, and a breach emits an `EventOfDefault` (subject to equity-cure rights, which are a basket of their own). An incurrence node is evaluated only when the borrower acts, and failing it emits `NotPermitted`. Incurrence tests never "violate"; they merely "permit." That difference has hollowed out the classic covenant-breach signal.

> **Trend Watch. Covenants leave the building: maintenance to incurrence, 1997–2024.** Griffin, Nini & Smith, *Losing Control? The 20-Year Decline in Loan Covenant Violations* (summarized on the Harvard Law School Forum on Corporate Governance, Nov 4, 2022), find that the annual share of U.S. public firms reporting a financial covenant violation fell by "nearly 70%" over twenty years (from over 12% in 1997 to under 5% in 2016, per the abstract as quoted in secondary sources). Late-1990s loans typically had "three or four covenants," while loans today rely on "one or two covenants" benchmarked against EBITDA. About half of the decline is a false-positive rate that "falls nearly 90%." On the leveraged-loan side, S&P Global reported in October 2021 that cov-lite deals exceeded 90% of leveraged-loan issuance, a record at the time. Per PitchBook|LCD, as reported in Paul Weiss's *Covenant-Lite Loans: Overview* (Practical Law, 2025), cov-lite loans were about 88.91% of outstanding U.S. leveraged loans (at par) at year-end 2022, 89.23% (about \$1,248.87 billion) at year-end 2023, and 91.09% (about \$1,292.74 billion) at year-end 2024, and about 93% of institutional issuance in both 2023 and 2024. (The full-year 2025 figure was not verified for this edition.) *What it means for the desk:* a parser that reads only the financial covenant section reads almost nothing. The risk now lives in incurrence baskets, which never trip a default and only tell you what the borrower is *allowed* to do next. Covenant-breach signals from the 1990s literature have to be rebuilt as capacity signals.

## 25.4 Value Leakage as a Flow Problem

Baskets do not act alone. Value leaves the collateral pool by *routes*: from the loan parties to non-guarantor restricted subsidiaries, from there to unrestricted subsidiaries, and from there to new creditors. A list of baskets can't tell you how much value can leak, because the binding constraint depends on how the baskets connect. A graph can.

### 25.4.1 The entity graph and max-flow min-cut

Build a directed graph $H$ whose nodes are entity classes: the source $s$ (the loan parties, holding the collateral), intermediate classes such as $N$ (restricted subsidiaries that are not guarantors), and the sink $t$ (unrestricted subsidiaries, outside the covenant perimeter). Each arc $a$ has a capacity $c_a \ge 0$ in dollars: the basket that permits investments or asset transfers along that route. A **flow** $f$ assigns $0 \le f_a \le c_a$ to each arc, with inflow equal to outflow at every intermediate node. Its value $|f|$ is the net flow into $t$. The **leakage capacity** is

$$
\Phi = \max_{f}\; |f|.
$$

(We use $\Phi$ because $\Lambda$ is reserved for order arrival and $\lambda$ for default intensity.)

An $s$–$t$ **cut** $(\mathcal{S}, \mathcal{S}^c)$ splits the nodes so that $s \in \mathcal{S}$ and $t \notin \mathcal{S}$. Its capacity $c(\mathcal{S})$ is the sum of capacities on arcs leaving $\mathcal{S}$.

**Weak duality (any flow ≤ any cut).** Summing conservation over the nodes in $\mathcal{S}$,

$$
|f| = \sum_{a \,\in\, \text{out}(\mathcal{S})} f_a \;-\; \sum_{a \,\in\, \text{in}(\mathcal{S})} f_a \;\le\; \sum_{a \,\in\, \text{out}(\mathcal{S})} c_a = c(\mathcal{S}),
$$

because $f_a \le c_a$ on arcs leaving $\mathcal{S}$ and $f_a \ge 0$ on arcs entering it. The **max-flow min-cut theorem** (Ford & Fulkerson, 1956) says the bound is tight:

$$
\Phi = \min_{\mathcal{S}}\; c(\mathcal{S}).
$$

The theorem is what makes this practical, because the min cut tells you *which* baskets bind. Raising the capacity of an arc that is not in the min cut changes nothing. Raising the capacity of an arc in the min cut, including to infinity, moves the cut, and $\Phi$ jumps to the next-smallest cut. That is exactly what a trapdoor does.

### 25.4.2 Case Study: J.Crew, 2016–2017, the Trapdoor as a Cut

*Facts.* J.Crew's annual report on Form 10-K for the fiscal year ended January 28, 2017 discloses that on October 12, 2016 the company designated certain newly formed Delaware entities as unrestricted subsidiaries under its senior credit facilities and its PIK Notes indenture, and that on December 5, 2016 a subsidiary transferred a 72.04% undivided interest in certain domestic intellectual property to one of those unrestricted subsidiaries. As Torys (May 2019) describes the routing, the company used two investment baskets to move the interest, valued at \$250 million, into a non-guarantor restricted subsidiary (J.Crew Cayman), and then a third provision to move it on to the unrestricted subsidiary. King & Spalding's account identifies the first two as a \$150 million basket for investments in non-guarantor restricted subsidiaries and a \$100 million general investment basket. The third provision permitted non-loan-party restricted subsidiaries to invest in unrestricted subsidiaries proceeds of investments made under the non-guarantor basket, and lenders called it the "trapdoor." J.Crew's April 2017 Form 10-Q describes the follow-on exchange: affiliates would offer to acquire the outstanding PIK Notes for up to \$190 million of new preference shares, up to 15% of the parent's common stock, and up to \$250 million of new notes secured by the transferred IP, alongside a \$150 million term-loan repurchase and a \$30 million add-on borrowing. On September 7, 2017 an ad hoc minority group of senior term lenders filed an amended complaint in New York state court over the "secret trapdoor" (Locke Lord, October 2017).

*In the formula.* Use a stylized three-node graph: $s \to N$ with two parallel arcs, $c_1 = 150$ (non-guarantor basket) and $c_2 = 100$ (general basket), and $N \to t$, the trapdoor. Ignore any direct $s \to t$ basket, so the model matches the disclosed route.

- *Before you read the trapdoor*, an analyst might treat $N \to t$ as capacity $0$ (nothing in the non-guarantor bucket was supposed to reach an unrestricted subsidiary). The min cut is $\{N \to t\}$, and $\Phi = 0$.
- *After you read it*, $c_{N\to t} = \infty$ (bounded only by what arrives at $N$). The min cut moves upstream to $\{s \to N\}$, and $\Phi = c_1 + c_2 = \$250$mm.

The trapdoor did not create new capacity. It moved the min cut upstream to two baskets that everyone had priced as "small baskets for foreign subsidiaries" rather than as leakage. A list-of-baskets parser sees \$150mm and \$100mm of investment capacity in non-guarantors and moves on. A flow parser sees \$250mm of capacity to unrestricted subsidiaries, and the IP was worth \$250mm.

*Blockers are commodity-specific cuts.* The "J.Crew blocker" drafted after 2017 typically bars transfers of material intellectual property to unrestricted subsidiaries. In flow terms, it sets the capacity to zero for one commodity (Material IP) on the arcs into $t$, and leaves cash and other assets untouched. So the right model is multi-commodity, and a blocker reduces $\Phi^{\text{IP}}$, not $\Phi$. The Chapter 13 feature `unsub_capacity_pct_ev` is $\Phi^{\text{non-IP}}/\text{EV}$ plus whatever $\Phi^{\text{IP}}$ survives the blocker's definitions. That last term is usually where the next fight is.

*How a systematic desk would have flagged and traded it.* The designation of unrestricted subsidiaries showed up in J.Crew's own periodic filings, so a versioned diff of the debt and liquidity disclosures (§25.5) would have registered a new, previously empty entity class becoming populated. A min-cut calculator would have put $\Phi/\text{EV}$ for J.Crew's IP route in the top tail of the universe *before* December 2016. The bigger trade came afterward. Ivashina & Vallee, *Weak Credit Covenants* (NBER WP 27316, 2020; *Management Science*, 2025), hand-build contractual-weakness measures from 1,240 credit agreements and show that those measures explain the market-wide price reaction to the 2017 J.Crew restructuring. In other words, document features got priced across the cross-section only *after* the market learned the trick. A desk with $\Phi$ already computed for every loan knew which names were next on the day the trick became famous. That is the trade: rank on leakage capacity, short the high-$\Phi$ loans against the low-$\Phi$ ones within a rating bucket, and size for the repricing, not the default. (We do not reproduce J.Crew loan prices here; pull vendor marks for the 2016–2017 window before backtesting this, and remember §25.9's stale-quote warning.)

"So the borrower's lawyers," said Kaz slowly, "solved a max-flow problem."

"By hand," said Mags. "In 2016. With a \$250 million objective function."

## 25.5 Versions and Diffs: Amendments Are Events

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.86:* "The most common coercive tactic is to 'strip' the covenant protections of nontendering bonds. To implement this, the exchange offer will include a provision that tendering bonds will be deemed to have voted to authorize an amendment to the indenture of the original bonds, which effectively deletes all protective covenants."
>
> **Annotation.** The exit consent shows that a document is not a constant. The same indenture can protect you on Monday and be an empty shell on Friday, and the transition is itself the event to trade. So the parser has to *version* documents: every amendment, supplemental indenture, waiver and joinder is a new version with a filing timestamp, and the desk stores the parsed node vector for each version. The modern uptier (Chapter 13) is the exit consent's loan-market grandchild. A Required Lender amendment rewrites the pro rata sharing or the waterfall, and the diff between versions *is* the transaction.

### 25.5.1 Text diffs are blind where it matters

Cohen, Malloy & Nguyen, *Lazy Prices* (NBER WP 25084, 2018; *Journal of Finance*, 2020), showed that a portfolio short the firms that change their 10-K and 10-Q language and long the firms that don't earned "up to 188 basis points in monthly alpha" ("over 22% per year"). There was no announcement effect, and the changes also predicted firm-level bankruptcies. The obvious port is to run the same similarity measure on amendments and indenture supplements. It fails, and the reason is worth deriving.

Let $x \in \mathbb{N}^d$ be the token-count vector of an agreement with $n = \sum_i x_i$ tokens over a vocabulary of size $d$. An amendment changes the leverage ratio from "4.50" to "5.25," so one token is swapped: $x' = x - e_i + e_j$. Take the common case where "4.50" appeared once ($x_i = 1$) and "5.25" never ($x_j = 0$). Then

$$
x \cdot x' = \|x\|^2 - 1, \qquad \|x'\|^2 = \|x\|^2 - 2 + 0 + 2 = \|x\|^2,
$$

so

$$
1 - \cos(x, x') = \frac{1}{\|x\|^2} \le \frac{d}{n^2},
$$

where the inequality is Cauchy–Schwarz, $\|x\|^2 \ge n^2/d$. For a 300-page agreement with $n \approx 150{,}000$ tokens and $d \approx 10{,}000$, the bound gives $1 - \cos \le 4.4 \times 10^{-7}$. At Halyard's $\mathcal{E} = \$266.7$mm, the same edit adds $0.75 \times 266.7 = \$200$mm of ratio capacity. The most expensive token in the document moves cosine similarity by less than one part in two million.

*Lazy Prices* works on 10-Ks because the informative edits there are rewrites of whole risk-factor and litigation paragraphs. Covenant edits are numeric and surgical. The diff that matters is on the parsed capacity vector $K(v)$, not on tokens. For versions $v_{k-1}$ and $v_k$ we define the **dollar-weighted blast radius**

$$
\Delta K_k = \sum_{u \in V} \big| K_u(v_k) - K_u(v_{k-1}) \big|, \qquad \text{signal}_k = \frac{\Delta K_k}{\text{EV}},
$$

and keep the signed per-node changes alongside it, because a capacity *reduction* (a lender win in an amend-and-extend) and a capacity *increase* (a sponsor win) trade in opposite directions.

### 25.5.2 Case Study: Windstream, Aurelius, and One Defined Term (2015–2019)

*Facts.* In 2015 Windstream spun off network assets into the REIT that became Uniti and leased them back. Aurelius, a holder of Windstream's 6 3/8% notes due 2023 issued under a 2013 indenture, argued that the transaction was a "Sale and Leaseback Transaction" the indenture did not permit. *U.S. Bank N.A. v. Windstream Services, LLC*, S.D.N.Y. No. 1:17-cv-07857, was filed on 2017-10-12 and is in RECAP (CourtListener docket 6169562). On 2019-02-15 Judge Furman entered Findings of Fact and Conclusions of Law (Doc. 245, 55 pp.). As summarized in the parties' public statements, the court held that in substance the transferor subsidiaries had sold the assets and leased them back, and that naming the parent as the sole signatory to the master lease did not change this. It also held that notes issued in November 2017 were not "Additional Notes" under the indenture, and it upheld the acceleration of the 6 3/8% notes. Aurelius described the judgment as \$310.5 million plus interest from July 23, 2018. Windstream filed for Chapter 11 on 2019-02-25, ten days later. Later appeals (*In re Windstream Holdings*, 7:20-cv-04276 and 7:20-cv-05529) were dismissed as equitably moot on 2021-06-23. Windstream argued publicly that Aurelius was net short through CDS, and the "net-short activism" debate that followed belongs to Part VI.

*In the formula.* The covenant node "Limitation on Sale and Leaseback Transactions" depends on the defined term "Sale and Leaseback Transaction," which depends on who transfers and who leases back. A parser that resolves "who" from the signature block (the parent signed the lease) evaluates the node to `NotApplicable`. A parser that resolves "who" economically (which entity owned the assets, which entity uses them) evaluates it to `Restricted`. The court took the second view. So the lesson for the spec is that *entity resolution in the definition graph must be economic, not formal*. Every node that turns on a party ("the Borrower or any Restricted Subsidiary") needs both a formal binding and an economic binding, and a flag when they disagree.

*How a systematic desk would have flagged it.* The 2015 spin and master lease were public. A transaction-to-node matcher, run on the 8-K announcing the transaction, would have hit "Sale and Leaseback Transaction." That node's blast radius included acceleration of the whole series, so it belonged in the legal-risk queue with a dollar exposure attached, not in a footnote. From 2017 on, the docket feed (§25.6) supplied the event chain: suit filed, findings, Chapter 11. One defined term was worth \$310.5 million plus interest by the winner's count. That is about as clean an example as there is of why the definition graph, not the keyword index, is the unit of analysis.

## 25.6 The Docket as an Event Stream

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.285:* "A bankruptcy is a legal process before a bankruptcy court, with virtually all information associated with the process in the form of filings listed on the case docket of the relevant court."
>
> **Annotation.** For a quant this is the best sentence in the distressed literature: the whole state of a bankruptcy is a single append-only log. Moyer also counted how big the log gets. WorldCom's docket ran to "9,686 filings totaling over 100,000 pages" between July 2002 and June 2003, and PACER documents came with "per-page charges" (p.387, nn.28, 30). At today's \$0.10 per page, a 100,000-page docket costs at most \$10,000, and less once the \$3-per-document cap clips the long filings. So the binding constraint is parsing, not purchasing. A desk can afford to be a RECAP contributor rather than a free rider.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.287:* "The bankruptcy docket must be monitored constantly because material events can occur which may not independently be announced... actions by various creditor constituencies that can give important insight on their strategies will also be filed, but otherwise not generally announced."
>
> **Annotation.** "Not generally announced" is an alt-data definition written before the term existed. The docket is a marked point process: entries arrive at times $t_1 < t_2 < \dots$, each with a mark (entry type, filer, attached documents, page count). The trading content is in the marks, and in the *sequences* of marks, which is why §25.7 builds a state machine rather than a keyword alert.

### 25.6.1 The plumbing, with the numbers that bind

- **EDGAR APIs** (sec.gov, "EDGAR Application Programming Interfaces"): `https://data.sec.gov/submissions/CIK##########.json` gives filing history and `.../api/xbrl/companyfacts/CIK##########.json` gives XBRL facts. No key is needed. The CIK must be zero-padded to ten digits, which is a classic ROBO bug. Submissions update in real time (typical delay under a second), and bulk zips are republished nightly around 3:00 a.m. ET. There is no CORS, so fetch server-side.
- **EDGAR fair access** (Webmaster FAQ): "our current maximum access rate is 10 requests per second." Declare a User-Agent containing a real contact mailbox.
- **EDGAR full-text search** (`efts.sec.gov/LATEST/search-index`): covers filings since 2001 and exhibits included. It supports quoted phrases, `OR`/`NOT`, `NEAR(n)` and trailing wildcards. It returns 100 hits per page and caps `hits.total` at 10,000.
- **CourtListener REST API v4** (Free Law Project): "By default, authenticated users may make up to 5 requests per minute, 50 requests per hour, and 125 requests per day." Search `type=r` returns dockets with at most three nested documents each. `type=rd` returns documents, which is the only way to enumerate every Rule 2019 filing in a case. Counts are approximate above 2,000. Results are cached for ten minutes. There is a weekly maintenance window on Thursdays, 21:00–23:59 PT. Quarterly bulk CSVs include dockets but not docket *entries*, so an entry-level backfill means API calls or a commercial arrangement.
- **RECAP Fetch** (`/api/rest/v4/recap-fetch/`): buys from PACER with *your* credentials ("You'll still have to pay your PACER bill when it comes"), at up to 30 requests per minute. PACER passwords expire every 180 days, which is an operations-calendar item, not a footnote. **Pray and Pay** lets you register interest in an unpurchased document and be notified when someone buys it.
- **PACER** (pacer.uscourts.gov): \$0.10 per page, no more than \$3 per document, fees waived at \$30 or less per quarter, and court opinions free.

### 25.6.2 Rate limits as a token bucket

Model a rate limiter as a bucket holding $z_t \in [0, b]$ tokens, refilled at rate $\rho$ tokens per second and capped at $b$. Each request consumes one token and is allowed only if $z_t \ge 1$.

**Lemma 25.2.** Over any interval $[t, t+h]$, a token bucket admits at most $b + \rho h$ requests.

*Proof.* At time $t$ the bucket holds at most $b$ tokens. During the interval at most $\rho h$ tokens are added. Every admitted request removes one token and the level never goes negative. So the number of admitted requests is at most $b + \rho h$. $\square$

Two spec consequences follow, and ROBO violated both on its first try.

1. *Burst plus rate.* "Rate 10 per second, burst 10" can admit **20** requests in a one-second window. To guarantee at most $L$ requests in any window of length $h_0$, choose $b + \rho h_0 \le L$. For EDGAR, with $L = 10$ and $h_0 = 1$, a safe choice is $b = 2$, $\rho = 8$.
2. *Workers multiply.* $W$ processes with private buckets admit up to $W(b + \rho h)$ in aggregate. The bucket must be global, behind a lock or in a shared store.

For CourtListener's default tier the binding limit is the daily one. Polling $M$ dockets every $T$ days costs $M/T$ requests per day, so daily polling caps out at 125 dockets *before* any searches. The right architecture is therefore search-first (one call returns 20 hits with entry descriptions), alerts and webhooks for push, and a paid tier for backfills.

> **Trend Watch. Docket access, 2005–2026: from per-page phone-book to throttled API.** In 2005 Moyer described PACER fees as "reasonable" with "few practical alternatives" (Moyer_Distressed_Debt_Analysis p.286). Free Law Project's RECAP archive has run "since 2009." Its browser extension adds users' PACER purchases to a free mirror that now holds "tens of millions of PACER documents" (free.law/recap; no as-of date given). On 2026-10-17, a single anonymous CourtListener v4 search for `"rule 2019" "verified statement"` returned a count of 1,868, with the newest hits dated September 2026. The feed is current to within weeks, and bankruptcy courts (`txsb`, `njb`, `miwb`, `okwb`) are in it. The shock came on August 7, 2025, when the Administrative Office of the U.S. Courts cited "escalated cyberattacks of a sophisticated and persistent nature on its case management system" (as reported by CNN). Secondary reporting says more than 20 courts then issued standing orders that sealed documents may be filed in CM/ECF but not viewed electronically. *What it means:* the public docket is now cheap, fast and machine-readable, and it can change shape overnight. A feed that silently drops sealed exhibits looks the same as a feed in which nothing happened.

> **Ways This Blows Up.** (1) *Phrase counts are polluted.* "Open market purchase" in EDGAR full-text search is dominated by fund prospectuses and Form 4s in 2018, and by SPAC sponsor agreements in 2025's 8-Ks. The most expensive three words in finance are also some of the most boring. (2) *Exhibits are refiled*, so one agreement is counted many times. Dedupe by accession number plus a hash of the exhibit text. (3) *The 10,000 cap* truncates silently (`relation: "gte"`). (4) *Untested operators.* `NEAR()` queries with quoted phrases returned zero hits for 2018, 2021 and 2025 alike, which cannot be true. Validate every search operator against a known-positive filing before you trust a zero. (5) *Keyword precision.* In the live Rule 2019 search, one of the top five hits was an appellate motion to dismiss, so put a classifier on the entry text and the PDF's first page. (6) *Sealed placeholders and expired PACER passwords* look like silence. Alert on silence.

