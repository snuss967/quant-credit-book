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

> **Ways This Blows Up.** *Substring matching.* Ignoring case, the term "Restricted Subsidiary" is a substring of "Unrestricted Subsidiary." A parser that matches case-insensitively, without word boundaries or longest-match-first, will draw an edge from every unrestricted-subsidiary provision to "Restricted Subsidiary," reversing the most important distinction in the document. The same trap catches "Lender" inside "Affiliated Lender" and "Debt" inside "Consolidated Total Debt." The fix: match case-sensitively, sort the dictionary by length descending, match with word boundaries, and consume each matched span before trying shorter terms. Other ways this goes wrong: plurals ("Restricted Payments" for "Restricted Payment"); terms defined by reference to *another* document (the Intercreditor Agreement, the Existing Indenture); a term defined in Section 1.01 and quietly redefined "for purposes of this Article X"; and exhibits filed as scanned images with no text layer. Every one of these fails silently.

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

## 25.7 The Rule 2019 Time Series and the Holder Graph

Federal Rule of Bankruptcy Procedure 2019, as amended in 2011, requires any group or committee of multiple creditors "acting in concert" to file a verified statement. Indenture trustees and agents are excused "solely for that reason." The statement must disclose, for each member, name, address and "the nature and amount of each disclosable economic interest," which is defined broadly enough to cover derivatives. Members who claim to represent others must also give the quarter and year each interest was acquired, unless it was acquired more than a year before the petition. A verified *supplemental* statement is due when a disclosed fact materially changes and the group takes a position. The sanctions have teeth: the court can refuse to hear the group or invalidate its votes.

The rule got this shape through a fight. In *In re Northwest Airlines* (Bankr. S.D.N.Y. 2007), Judge Gropper held on February 26, 2007 that the plain terms of the old rule required an ad hoc equity committee to disclose holdings. On March 9 he refused to seal the trading details, because "Rule 2019 was a disclosure rule that would be thwarted" if the other holders could not see them (Cleary Gottlieb alert memo, Mar 13, 2007). The old rule demanded "the amounts paid therefore." The 2011 amendment dropped price disclosure in exchange for broader coverage (CDS, total return swaps, shorts) and the acquisition quarter. So the Rule 2019 series carries **quantities and dates, never prices**. Prices have to be imputed.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.329:* "Usually the largest creditor schedule will list as the creditors only the indenture trustee for any bond issues, even though the indenture trustee probably will not actually own any bonds."
>
> **Annotation.** This is the entity-resolution warning in one sentence: the name on the claim is not the holder. A naive holder graph built from schedules has one giant node, the indenture trustee, which owns nothing and, as Moyer notes elsewhere, will "only do what they are clearly obliged to do" (p.76). Ad hoc groups exist because trustees are passive. Rule 2019 is how the desk sees through the trustee to the beneficial holders who will actually vote. The modern desk fuses three sources: Rule 2019 for the active holders, CLO trustee reports for the loan side, and 13F and N-PORT filings for the fund side. Each source has a different lag.

### 25.7.1 From statements to a panel

For group $g$, statement $k$ filed at $t_k$, and class $c$ with face $F_c$, let $h_{i,c,k}$ be member $i$'s disclosed face. Then the group's class share, net flow and holder concentration are

$$
\theta_{g,c}(t_k) = \frac{1}{F_c}\sum_{i \in g} h_{i,c,k}, \qquad \Delta h_{i,c,k} = h_{i,c,k} - h_{i,c,k-1}, \qquad H_c(t_k) = \sum_i \Big(\frac{h_{i,c,k}}{F_c}\Big)^2.
$$

$H_c$ is the `holder_hhi` input in §13.2.1. Statements say "approximately," so assume each of $n$ members rounds to the nearest $\delta$; then $|\hat\theta - \theta| \le n\delta/(2F_c)$. Carry that as an interval, not a point.

**Blocking arithmetic.** Under 11 U.S.C. §1126(c), a class accepts a plan if holders of at least two-thirds in amount and more than half in number *of the claims that vote* accept. If a fraction $\varphi$ of the class's face votes and the group, holding $\theta \le \varphi$, votes as a block, its share of the voted amount is $\theta/\varphi$. It can defeat acceptance on amount alone when

$$
\frac{\theta}{\varphi} > \frac13 \quad\Longleftrightarrow\quad \theta > \frac{\varphi}{3}.
$$

So low turnout lowers the blocking bar. With 60% turnout *(illustrative)*, 20% of the class blocks. Out of court, the analogous threshold is the agreement's "Required Lenders" (typically more than 50%), which is the $\theta_{\text{required}}$ of Chapter 13.

**Imputed cost basis.** With disclosed acquisition quarters $q$ and a quarterly average price $\bar P_q$ from TRACE or loan marks, the imputed basis is $\hat c_i = \sum_q h_{i,q}\bar P_q / \sum_q h_{i,q}$. A group with a basis of 40 will take a plan at 55 that a basis-90 group will fight to the end. "Their cost basis is their hand," said Ines. "Rule 2019 makes them show you half of it."

**Endogenous sampling.** Supplements are filed when holdings change *and* the group takes a position. So the timing of a filing is informative in its own right: a statement appears because something is about to happen.

### 25.7.2 The docket as a state machine

Classify entries into marks and map them to states: Quiet → Organized (first 2019 statement) → Contested (exclusivity, standing or lien-challenge motions) → Standstill (stipulated stays, mediation) → Plan → Confirmed. Treat the path as a continuous-time Markov chain with transition intensities $q_{ab}$. (These are $q_{ab}$ with two subscripts, distinct from inventory $q$.) With $N_{ab}$ observed $a \to b$ transitions and total time $T_a$ spent in state $a$ across a panel of cases, the log-likelihood is

$$
\log \mathcal{L} = \sum_{a}\sum_{b \ne a}\big(N_{ab}\log q_{ab} - q_{ab}\,T_a\big),
$$

and setting $\partial \log \mathcal{L}/\partial q_{ab} = N_{ab}/q_{ab} - T_a = 0$ gives $\hat q_{ab} = N_{ab}/T_a$. This is the right estimator for "how long after a group organizes does it attack exclusivity," and it stays honest about cases still in progress, because their time in state counts in $T_a$ even if no transition has happened yet.

> **Docket Diary. Hughes Satellite Systems Corporation, Bankr. S.D. Tex. No. 26-90739 (2026).** Doc. 154 (2026-08-10): "Verified Statement of Noteholders Pursuant to Bankruptcy Rule 2019... Exhibit A." Doc. 320 (2026-09-10, 40 pp.): "The Noteholder Group's Emergency Motion to Terminate the Debtors' Exclusive Periods Pursuant to 11 U.S.C. § 1121(d)(1)," hearing set for 9/28/2026, exhibits filed under seal. Doc. 369 (2026-09-20, 36 pp.): "Stipulated Order Staying Litigation and Investigations in the Chapter 11 Cases." That is Organized → Contested in 31 days and Contested → Standstill in 10. *The Ad Hoc Group, through counsel, in unison:* "We reserve all rights. Including the right to have reserved them earlier." Ines read the sequence aloud: "A bet, a raise, and both players agreeing to check it down." (Facts beyond the docket entry text are not stated here.)

### 25.7.3 Case Study: Serta Simmons, Read From the Docket (2023)

Chapter 13 (§13.3.1) priced the 2020 uptier. Here is what the bankruptcy docket shows. Serta Simmons Bedding filed in the Southern District of Texas on 2023-01-23 (No. 23-90020). A CourtListener `type=rd` query for Rule 2019 filings returns this sequence:

| Entry date | Doc. | Filer | What |
| :--- | :--- | :--- | :--- |
| 2023-01-24 | 69 | Ad Hoc Priority Lender Group | Original verified statement |
| 2023-01-24 | 75 | Ad Hoc Group of First Lien Lenders | Original verified statement (the excluded-lender side) |
| 2023-02-09 | 273 | Five utility creditors, one counsel | Rule 2019 statement |
| 2023-02-10 | 289 | Ad Hoc Equity Group | Original verified statement |
| 2023-02-13 | 311 | Utilities plus one more | Statement adding a member |
| 2023-03-01 | 389 | Ad Hoc Priority Lender Group | Amended verified statement |
| 2023-06-21 | 1116 | Ad Hoc Priority Lender Group | Second amended verified statement |

Four things a desk takes from this. First, *both sides of the uptier organized on day one*: Docs 69 and 75 were filed together, a day after the petition, so litigation was certain before the first-day hearing ended. Second, the priority-lender group's statements at {Jan 24, Mar 1, Jun 21} *are* its holdings time series, and the diff between them is the flow. Third, the classifier has to rank by class: the utilities' statements are valid Rule 2019 filings with no bearing on term-loan recovery. Fourth, the PDFs showed as "not available" in RECAP because nobody had bought them, and at \$3 or less each through RECAP Fetch, the whole series costs less than lunch. The adversary proceeding (No. 4:23-ap-09001, filed 2023-01-24) carries a 2023-05-22 stipulated order on "North Star's status as a disqualified institution," a disqualified-lender-list fact that a holder graph needs and no press release gave. The Fifth Circuit's December 31, 2024 holding that the 2020 transaction was not an "open market purchase" came twenty-three months after Doc. 75 told you there would be a fight.

Huang, Lewellen & Wang, *Creditor Coalitions in Bankruptcy* (SSRN 4854111; HLS Bankruptcy Roundtable, Feb 11, 2025) is what turns this feed from a who's-who into a return predictor. Working from Chapter 11 filings, "especially Rule 2019 disclosures," they find coalitions are more likely in large classes with dispersed ownership and illiquid debt, and that "coalition announcements are associated with increased bond prices," with significant positive returns across creditor classes. (Sample sizes and magnitudes are not reproduced here pending the paper's own tables.)

## 25.8 Claims Registers and the Transfer Feed

Rule 3001(e) creates the third layer. When a claim is transferred after a proof of claim is filed, "the transferee must file evidence of the transfer," *except* for claims based on publicly traded notes, bonds or debentures. The clerk mails notice, and the transferor has 21 days to object. So every trade claim, vendor claim, lease-rejection claim and bank-loan claim that changes hands after the bar date leaves a docket entry naming the transferor, the transferee and the face amount, but never the price. The bond side is dark. The resulting features are the share of class face transferred, the concentration of transferees (the same few funds buying everything), and the time from bar date to transfer. Each of these says something about who will be at the plan negotiation.

Moyer's starting point still holds: the petition's list of the 20 largest unsecured creditors "can often give insight on the possible composition of the unsecured creditor committee" (Moyer_Distressed_Debt_Analysis p.286). The plumbing is the hard part. On 2026-10-17, Kroll's restructuring portal returned HTTP 403 to an automated fetch, Epiq served a JavaScript-only shell, Stretto's case site was live, and Verita returned 503. Claims registers are the least API-friendly layer in the stack. Budget a headless browser and per-agent adapters, and read each portal's terms before automating.

## 25.9 From Text to Signal: Error, Decay and Discipline

### 25.9.1 Classifier error is an IC tax

Let $x \in \{0,1\}$ be a true document feature (for example, "has a trapdoor-type route") with base rate $\pi$, and let $\hat x$ be the classifier's output, with sensitivity $a = \mathbb{P}(\hat x = 1 \mid x = 1)$ and specificity $b = \mathbb{P}(\hat x = 0 \mid x = 0)$. Assume errors are independent of the forward return $r$ given $x$. Then $\mathbb{E}[\hat x \mid x, r] = (1-b) + (a + b - 1)\,x$, so

$$
\text{Cov}(\hat x, r) = \text{Cov}\big(\mathbb{E}[\hat x \mid x, r],\, r\big) = J\,\text{Cov}(x, r), \qquad J = a + b - 1,
$$

and therefore

$$
\text{IC}(\hat x) = J\,\frac{\sqrt{\pi(1-\pi)}}{\sqrt{\hat\pi(1-\hat\pi)}}\;\text{IC}(x), \qquad \hat\pi = (1-b) + J\pi. \tag{25.3}
$$

$J$ is Youden's index, and it is the exchange rate between classifier quality and alpha. Take $\pi = 5\%$, $a = 0.90$, $b = 0.95$. Then $J = 0.85$, $\hat\pi = 9.25\%$, and the IC falls to $0.639$ of its true value. By the fundamental law ($\text{IR} \approx \text{IC}\sqrt{\text{BR}}$) you need $1/0.639^2 \approx 2.45$ times the breadth to break even. Note also that with a 5% base rate, a "95% specific" classifier is wrong on about half of its flags: $\mathbb{P}(x = 1 \mid \hat x = 1) = a\pi/\hat\pi \approx 0.49$.

This is the quantitative argument for the citation contract. Dahl et al. (2024), *Large Legal Fictions*, found hallucination rates of "roughly 58% to 88%" on verifiable questions about federal cases. Magesh et al. (2024) found that leading retrieval-augmented legal research tools still hallucinated "between 17% and 33% of the time." Either rate, plugged into (25.3), takes most of the signal away. So ROBO never emits a covenant value without a span, and the test harness scores span correctness, not fluency. For pre-training and evaluation there are public corpora: CUAD (510 contracts, 41 clause types, 13,000+ expert labels), LEDGAR ("over 60'000 contracts," "almost 100'000 provisions," from SEC filings) and LegalBench (162 tasks). None of them labels basket arithmetic, so the desk's gold set is hand-built from its own universe.

### 25.9.2 Discipline and decay

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.156:* "There are so many choices that generating all possible features from alternative data would be a recipe for confusion and data mining."
>
> **Annotation.** A 300-page agreement has millions of n-grams, and some of them will backtest beautifully by accident. The defense is to pre-register: the document features are the typed nodes in the Chapter 13 table ($\Phi$, ratio headroom, builder availability, blocker flags) plus the docket states of §25.7.2, fixed *before* looking at returns. New features go through a written hypothesis first. This is the one place on the desk where bureaucracy is alpha.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.621:* "Indeed, bonds may react more slowly than stocks to news affecting a corporation... In this case, the relationship between equity momentum and subsequent returns of corporate bonds can be an illusion: Investors, trying to implement the strategy, would in reality be offered 'updated' prices of corporate bonds."
>
> **Annotation.** Docket and amendment signals share the same trap. If a backtest goes long the loans whose priority-lender group just filed a 2019 statement and marks the entry at the last TRACE print or the prior day's loan mark, it is buying at a price no dealer would show after the docket entry posted. Measure signal decay as $\text{IC}(h)$ across horizons $h$, and enter at a quote that is executable *after* the event timestamp, with the delay set by the feed's actual latency (seconds for EDGAR, minutes to days for RECAP). Then apply the desk motto: IDO or it didn't happen. Strip the carry, rates and factor beta before you call anything alpha (Chapter 8).

## 25.10 The Covenant-and-Docket Engine

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

```python
# Block 1: the definition graph ------------------------------------------------
import math
import re
from collections import defaultdict, deque
from dataclasses import dataclass

import numpy as np
import pandas as pd

rng = np.random.default_rng(2525)

# Synthetic text written for this book; not copied from any real agreement.
AGREEMENT = """
"Consolidated Net Income" means the net income of the Borrower and its Restricted Subsidiaries for such period.
"Run-Rate Cost Savings" means cost savings projected in good faith, not to exceed 25% of Consolidated EBITDA for such period (calculated after giving effect to such adjustments).
"Consolidated EBITDA" means Consolidated Net Income plus interest, taxes, depreciation and amortization, plus Run-Rate Cost Savings, in each case calculated on a Pro Forma Basis.
"Pro Forma Basis" means, with respect to any Specified Transaction, giving effect to such transaction as if it occurred on the first day of the Test Period, including for purposes of Consolidated EBITDA.
"Specified Transaction" means any acquisition, disposition or incurrence of Indebtedness.
"Indebtedness" means all obligations for borrowed money.
"Lien" means any mortgage, pledge or security interest.
"Lenders" means the lenders party hereto.
"Collateral" means all property subject to a Lien in favor of the Lenders.
"Consolidated First Lien Net Debt" means Indebtedness secured by a Lien on the Collateral on a pari passu basis, less unrestricted cash.
"First Lien Net Leverage Ratio" means the ratio of Consolidated First Lien Net Debt to Consolidated EBITDA.
"Subsidiary" means any entity controlled by the Borrower.
"Restricted Subsidiary" means any Subsidiary that is not an Unrestricted Subsidiary.
"Unrestricted Subsidiary" means any Subsidiary designated as such, provided that no Unrestricted Subsidiary may own Material Intellectual Property.
"Material Intellectual Property" means intellectual property material to the business of the Borrower and its Restricted Subsidiaries.
"Excluded Taxes" means taxes imposed on the Lenders.
"""

DEF_RE = re.compile(r'^"(?P<term>[^"]+)"\s+means\s+(?P<body>.+)$', flags=re.M)


def parse_definitions(text):
    """Return {term: (body, char_offset)}; the offset is the citation anchor."""
    return {m.group("term"): (m.group("body"), m.start()) for m in DEF_RE.finditer(text)}


def term_pattern(term):
    """Case-sensitive, word-bounded pattern that also accepts the plural."""
    stem = re.escape(term[:-1]) + "(?:y|ies)" if term.endswith("y") else re.escape(term) + "s?"
    return re.compile(r"(?<![A-Za-z\-])" + stem + r"(?![A-Za-z])")


def find_references(body, terms):
    """Longest-match-first and span-consuming, so 'Lien' inside a longer term is not an edge."""
    taken = np.zeros(len(body), dtype=bool)
    found = set()
    for t in sorted(terms, key=len, reverse=True):
        for m in term_pattern(t).finditer(body):
            s, e = m.span()
            if not taken[s:e].any():
                taken[s:e] = True
                found.add(t)
    return found


def tarjan_scc(nodes, adj):
    """Tarjan's SCCs. Emission order is an evaluation order: dependencies come first."""
    index, low, on_stack, stack, comps = {}, {}, set(), [], []
    counter = [0]

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack.add(v)
        for w in sorted(adj[v]):
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop()
                on_stack.discard(w)
                comp.add(w)
                if w == v:
                    break
            comps.append(frozenset(comp))

    for v in sorted(nodes):
        if v not in index:
            strong(v)
    return comps


def blast_radius(v, adj):
    """Everything that (transitively) uses v: the set B(v) of Section 25.2.2."""
    rev = defaultdict(set)
    for u, vs in adj.items():
        for w in vs:
            rev[w].add(u)
    seen, queue = set(), deque([v])
    while queue:
        for u in rev[queue.popleft()]:
            if u not in seen:
                seen.add(u)
                queue.append(u)
    seen.discard(v)
    return seen


defs = parse_definitions(AGREEMENT)
TERMS = list(defs)
refs = {u: find_references(body, TERMS) for u, (body, _) in defs.items()}
self_refs = sorted(u for u in refs if u in refs[u])
edges = {u: vs - {u} for u, vs in refs.items()}

# The substring trap: a case-insensitive matcher invents the opposite edge.
naive_hits = [t for t in TERMS if t.lower() in "any unrestricted subsidiary"]
assert "Restricted Subsidiary" in naive_hits
assert find_references("any Unrestricted Subsidiary", TERMS) == {"Unrestricted Subsidiary"}
assert find_references("Restricted Subsidiaries of the Borrower", TERMS) == {"Restricted Subsidiary"}

comps = tarjan_scc(TERMS, edges)
comp_of = {v: i for i, c in enumerate(comps) for v in c}
cycles = sorted(sorted(c) for c in comps if len(c) > 1)
for u, vs in edges.items():                       # dependencies are evaluated first
    for v in vs:
        if comp_of[u] != comp_of[v]:
            assert comp_of[v] < comp_of[u]

idx = {t: i for i, t in enumerate(TERMS)}
A = np.zeros((len(TERMS), len(TERMS)), dtype=np.int64)
C = np.zeros((len(comps), len(comps)), dtype=np.int64)
for u, vs in edges.items():
    for v in vs:
        A[idx[u], idx[v]] = 1
        if comp_of[u] != comp_of[v]:
            C[comp_of[u], comp_of[v]] = 1
assert np.linalg.matrix_power(A, len(TERMS)).any()          # cycles: A is not nilpotent
assert not np.linalg.matrix_power(C, len(comps)).any()      # Lemma 25.1: condensation is a DAG

assert ["Consolidated EBITDA", "Pro Forma Basis", "Run-Rate Cost Savings"] in cycles
assert "First Lien Net Leverage Ratio" in blast_radius("Consolidated EBITDA", edges)
assert blast_radius("Excluded Taxes", edges) == set()
print("cycles:", cycles, "| self-references:", self_refs)
```

```python
# Block 2: basket arithmetic (units: $mm) -------------------------------------
COVENANTS = """
Section 6.01(b)(xii). Indebtedness in an aggregate principal amount not to exceed the greater of $75,000,000 and 35% of Consolidated EBITDA.
Section 6.01(b)(xx). Indebtedness so long as, on a Pro Forma Basis, the First Lien Net Leverage Ratio does not exceed 4.50:1.00 (calculated without netting the cash proceeds of such Indebtedness).
"""
GROWER_RE = re.compile(r"greater of \$([\d,]+) and (\d+(?:\.\d+)?)% of Consolidated EBITDA")
RATIO_RE = re.compile(r"does not exceed (\d+\.\d+):1\.00")
CAP_RE = re.compile(r"not to exceed (\d+(?:\.\d+)?)% of Consolidated EBITDA")


@dataclass
class Grower:
    fixed_mm: float
    pct: float
    span: str

    def capacity(self, ebitda_mm):
        return max(self.fixed_mm, self.pct * ebitda_mm)


@dataclass
class RatioBasket:
    max_ratio: float
    scope_debt_mm: float
    nettable_cash_mm: float
    nets_proceeds: bool
    span: str

    def capacity(self, ebitda_mm):
        if ebitda_mm <= 0:
            return 0.0
        if self.nets_proceeds:                # Case 2 of 25.3.2: the perpetual-motion machine
            ok = (self.scope_debt_mm - self.nettable_cash_mm) / ebitda_mm <= self.max_ratio
            return math.inf if ok else 0.0
        return max(0.0, self.max_ratio * ebitda_mm - self.scope_debt_mm + self.nettable_cash_mm)


def parse_baskets(text, scope_debt_mm, nettable_cash_mm=0.0):
    out = []
    for line in text.strip().splitlines():
        g = GROWER_RE.search(line)
        if g:
            out.append(Grower(float(g.group(1).replace(",", "")) / 1e6, float(g.group(2)) / 100, line))
        r = RATIO_RE.search(line)
        if r:
            out.append(RatioBasket(float(r.group(1)), scope_debt_mm, nettable_cash_mm,
                                   nets_proceeds="without netting" not in line, span=line))
    return out


def addback_fixed_point(e0_mm, claimed_mm, cap, after_effect=True, tol=1e-10, max_iter=10_000):
    """Equation (25.1). 'After giving effect' turns the cap into a contraction fixed point."""
    if not after_effect:
        return min(claimed_mm, cap * e0_mm)
    if not 0.0 <= cap < 1.0:
        raise ValueError("cap >= 1: the cycle is not a contraction; send it to a human")
    a = 0.0
    for _ in range(max_iter):
        a_next = min(claimed_mm, cap * (e0_mm + a))
        if abs(a_next - a) < tol:
            return a_next
        a = a_next
    raise RuntimeError("add-back iteration did not converge")


def total_capacity(ebitda_mm, nodes):
    return sum(n.capacity(ebitda_mm) for n in nodes)


def builder_available(starter_mm, cni_quarters_mm, equity_mm=0.0, usage_mm=0.0):
    """Equation (25.2): 50% of cumulative CNI if positive, minus 100% of a deficit."""
    n = float(np.sum(cni_quarters_mm))
    return max(0.0, starter_mm + (0.5 * n if n >= 0 else n) + equity_mm - usage_mm)


rrcs_body = defs["Run-Rate Cost Savings"][0]
CAP = float(CAP_RE.search(rrcs_body).group(1)) / 100
AFTER = "after giving effect" in rrcs_body
E0, CLAIMED = 200.0, 80.0                                  # Halyard, illustrative
A_after = addback_fixed_point(E0, CLAIMED, CAP, after_effect=AFTER)
A_before = addback_fixed_point(E0, CLAIMED, CAP, after_effect=False)
assert CAP == 0.25 and AFTER
assert abs(A_after - CAP / (1 - CAP) * E0) < 1e-6         # 66.67, the closed form
assert abs(A_before - 50.0) < 1e-12

baskets = parse_baskets(COVENANTS, scope_debt_mm=900.0)
grower = next(b for b in baskets if isinstance(b, Grower))
ratio = next(b for b in baskets if isinstance(b, RatioBasket))
assert (grower.fixed_mm, grower.pct) == (75.0, 0.35)
assert ratio.max_ratio == 4.5 and not ratio.nets_proceeds

E_with = E0 + A_after
K_without, K_with = total_capacity(E0, baskets), total_capacity(E_with, baskets)
assert abs(K_without - 75.0) < 1e-9
assert abs(K_with - 393.333) < 1e-3
h = 1e-6
slope = (total_capacity(E_with + h, baskets) - total_capacity(E_with, baskets)) / h
assert abs(slope - 4.85) < 1e-4                            # dK/dE = m + p

leaky = RatioBasket(4.5, 900.0, 0.0, nets_proceeds=True, span="(synthetic: netting allowed)")
assert math.isinf(leaky.capacity(E_with))

assert builder_available(50.0, [30.0, -10.0]) == 60.0
assert builder_available(50.0, [10.0, -30.0]) == 30.0     # losses count double
assert builder_available(50.0, [-80.0]) == 0.0
print(f"capacity without add-backs ${K_without:.1f}mm, with ${K_with:.1f}mm, slope {slope:.2f}")
```

```python
# Block 3: leakage capacity as max-flow (units: $mm) --------------------------
def max_flow_min_cut(arcs, s, t):
    """Edmonds-Karp. arcs: list of (u, v, basket, capacity). Returns (value, cut_arcs)."""
    cap = defaultdict(lambda: defaultdict(float))
    for u, v, _, c in arcs:
        cap[u][v] += c
        cap[v][u] += 0.0
    res = {u: dict(vs) for u, vs in cap.items()}
    value = 0.0
    while True:
        parent, queue = {s: None}, deque([s])
        while queue and t not in parent:
            u = queue.popleft()
            for v, c in res[u].items():
                if c > 1e-12 and v not in parent:
                    parent[v] = u
                    queue.append(v)
        if t not in parent:
            break
        path, v = [], t
        while parent[v] is not None:
            path.append((parent[v], v))
            v = parent[v]
        push = min(res[u][v] for u, v in path)
        if math.isinf(push):
            return math.inf, []                       # an uncapped route all the way out
        for u, v in path:
            res[u][v] -= push
            res[v][u] += push
        value += push
    reach, queue = {s}, deque([s])
    while queue:
        u = queue.popleft()
        for v, c in res[u].items():
            if c > 1e-12 and v not in reach:
                reach.add(v)
                queue.append(v)
    return value, [a for a in arcs if a[0] in reach and a[1] not in reach]


def jcrew_arcs(trapdoor_mm):
    return [("LoanParties", "NonGuarantorRS", "non-guarantor investments", 150.0),
            ("LoanParties", "NonGuarantorRS", "general investments", 100.0),
            ("NonGuarantorRS", "Unrestricted", "trapdoor", trapdoor_mm)]


phi_before, cut_before = max_flow_min_cut(jcrew_arcs(0.0), "LoanParties", "Unrestricted")
phi_after, cut_after = max_flow_min_cut(jcrew_arcs(math.inf), "LoanParties", "Unrestricted")
assert phi_before == 0.0 and [a[2] for a in cut_before] == ["trapdoor"]
assert phi_after == 250.0 and sum(a[3] for a in cut_after) == phi_after   # max-flow = min-cut
# A J.Crew blocker is commodity-specific: it zeroes IP arcs into the sink, not cash arcs.
# (Commodities share basket capacity, so phi_ip + phi_cash <= 250 jointly.)
phi_ip_blocked, _ = max_flow_min_cut(jcrew_arcs(0.0), "LoanParties", "Unrestricted")
phi_cash, _ = max_flow_min_cut(jcrew_arcs(math.inf), "LoanParties", "Unrestricted")
assert phi_ip_blocked == 0.0 and phi_cash == 250.0
```

```python
# Block 4: why token diffs miss covenant edits (Section 25.5.1) ---------------
d, n_tok = 10_000, 150_000
x = np.bincount(rng.integers(0, d - 2, size=n_tok), minlength=d).astype(float)
x[d - 2], x[d - 1] = 1.0, 0.0              # token "4.50" appears once; "5.25" never
x_new = x.copy()
x_new[d - 2] -= 1.0
x_new[d - 1] += 1.0
cos = x @ x_new / (np.linalg.norm(x) * np.linalg.norm(x_new))
assert np.isclose(1 - cos, 1 / (x @ x), rtol=1e-6)
assert 1 - cos <= d / x.sum() ** 2                          # Cauchy-Schwarz bound
amended = RatioBasket(5.25, 900.0, 0.0, False, span="(synthetic amendment)")
delta_K = amended.capacity(E_with) - ratio.capacity(E_with)
assert abs(delta_K - 200.0) < 1e-6
print(f"1 - cos = {1 - cos:.2e}; capacity change = ${delta_K:,.1f}mm")
```

```python
# Block 5: rate limits (Lemma 25.2) and EDGAR hygiene -------------------------
class TokenBucket:
    """One global bucket. In production, share it across workers (lock or Redis)."""

    def __init__(self, rate, burst):
        self.rate, self.burst = float(rate), float(burst)
        self.tokens, self.t = float(burst), 0.0

    def try_acquire(self, now):
        self.tokens = min(self.burst, self.tokens + (now - self.t) * self.rate)
        self.t = now
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False


def max_in_window(times, h):
    times = np.sort(np.asarray(times))
    return int(np.max(np.searchsorted(times, times + h, side="right") - np.arange(len(times))))


attempts = np.sort(rng.uniform(0.0, 60.0, size=6_000))      # 100 requests/s of demand
naive_bucket, safe_bucket = TokenBucket(rate=10, burst=10), TokenBucket(rate=8, burst=2)
naive_ok = [t for t in attempts if naive_bucket.try_acquire(t)]
safe_ok = [t for t in attempts if safe_bucket.try_acquire(t)]
assert max_in_window(naive_ok, 1.0) <= 10 + 10 * 1.0           # the lemma's bound holds...
assert max_in_window(naive_ok, 1.0) > 10                        # ...and breaks 10 requests/s
assert max_in_window(safe_ok, 1.0) <= 10                        # b + rho*h0 <= L

USER_AGENT = "Example Desk Research desk-ops@example.com"     # the SEC asks for a real mailbox


def edgar_submissions_url(cik):
    return f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"


assert edgar_submissions_url("1234") == "https://data.sec.gov/submissions/CIK0000001234.json"
```

```python
# sketch: live ingest (not run here; needs network access, a real mailbox and a CourtListener token)
import time
import requests

bucket = TokenBucket(rate=8, burst=2)


def polite_get(url, headers, params=None, retries=5):
    for attempt in range(retries):
        while not bucket.try_acquire(time.monotonic()):
            time.sleep(0.01)
        r = requests.get(url, headers=headers, params=params, timeout=30)
        if r.status_code in (403, 429, 503):
            time.sleep(2 ** attempt)          # exponential backoff, then alert a human
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"gave up on {url}")


fts = polite_get("https://efts.sec.gov/LATEST/search-index", {"User-Agent": USER_AGENT},
                 {"q": '"unrestricted subsidiary"', "forms": "8-K", "dateRange": "custom",
                  "startdt": "2024-01-01", "enddt": "2026-10-17"})
dockets = polite_get("https://www.courtlistener.com/api/rest/v4/search/",
                     {"Authorization": "Token <YOUR_TOKEN>"},
                     {"type": "rd", "q": '"rule 2019" "verified statement"',
                      "docket_number": "23-90020", "court": "txsb"})
```

```python
# Block 6: Rule 2019 statements -> holdings panel (synthetic holders; $mm face) --
lots = pd.DataFrame(
    [  # statement, filed, holder, face_mm, acquisition quarter
        (1, "2026-01-15", "Holder_A", 120.0, "2025Q3"),
        (1, "2026-01-15", "Holder_B", 80.0, "2025Q4"),
        (1, "2026-01-15", "Holder_C", 40.0, "2025Q4"),
        (2, "2026-03-02", "Holder_A", 120.0, "2025Q3"),
        (2, "2026-03-02", "Holder_A", 30.0, "2026Q1"),
        (2, "2026-03-02", "Holder_B", 80.0, "2025Q4"),
        (2, "2026-03-02", "Holder_C", 40.0, "2025Q4"),
        (2, "2026-03-02", "Holder_D", 60.0, "2026Q1"),
    ],
    columns=["stmt", "filed", "holder", "face_mm", "acq_q"],
)
CLASS_FACE_MM, ROUNDING_MM = 1_000.0, 1.0
QTR_PX = {"2025Q3": 88.0, "2025Q4": 71.0, "2026Q1": 58.0}   # synthetic quarterly average prices

wide = (lots.groupby(["stmt", "holder"], as_index=False)["face_mm"].sum()
        .pivot(index="holder", columns="stmt", values="face_mm").fillna(0.0))
theta = wide.sum() / CLASS_FACE_MM
flows = wide[2] - wide[1]
theta_err = (wide > 0).sum() * ROUNDING_MM / (2 * CLASS_FACE_MM)


def blocks(theta_g, turnout):
    """11 U.S.C. 1126(c) amount test: the group alone defeats acceptance if theta > turnout/3."""
    return theta_g > turnout / 3.0


lots["px"] = lots["acq_q"].map(QTR_PX)
last = lots[lots["stmt"] == 2]
basis = (last["face_mm"] * last["px"]).groupby(last["holder"]).sum() / last.groupby("holder")["face_mm"].sum()
hhi_lower = float(((wide[2] / CLASS_FACE_MM) ** 2).sum())   # a lower bound: non-filers are invisible

assert np.isclose(theta[1], 0.24) and np.isclose(theta[2], 0.33)
assert flows.to_dict() == {"Holder_A": 30.0, "Holder_B": 0.0, "Holder_C": 0.0, "Holder_D": 60.0}
assert blocks(theta[2], turnout=0.60) and not blocks(theta[2], turnout=1.00)
assert np.isclose(basis["Holder_A"], 82.0) and np.isclose(basis["Holder_D"], 58.0)
assert np.isclose(theta_err[2], 0.002)
assert 0.0 < hhi_lower < theta[2] ** 2
```

```python
# Block 7: docket state machine, transition intensities (Section 25.7.2) ------
spells = pd.DataFrame(
    [  # case, state, days in state, next state (None = still there: censored)
        ("case1", "Organized", 31.0, "Contested"),    # case1 mimics the Hughes sequence
        ("case1", "Contested", 10.0, "Standstill"),
        ("case2", "Organized", 45.0, "Contested"),
        ("case2", "Contested", 60.0, None),
        ("case3", "Organized", 90.0, None),
    ],
    columns=["case", "state", "days", "next"],
)
T_a = spells.groupby("state")["days"].sum()
N_ab = spells.dropna(subset=["next"]).groupby(["state", "next"]).size()
q_hat = N_ab / T_a.reindex(N_ab.index.get_level_values(0)).to_numpy()
assert np.isclose(q_hat[("Organized", "Contested")], 2 / 166)   # censored days still count in T_a
assert np.isclose(q_hat[("Contested", "Standstill")], 1 / 70)
```

```python
# Block 8: classifier error as an IC tax (Equation 25.3), plus the citation contract --
n_obs, pi, a_sens, b_spec = 400_000, 0.05, 0.90, 0.95
x_true = (rng.random(n_obs) < pi).astype(float)
ret = x_true + rng.standard_normal(n_obs)                     # illustrative units
u = rng.random(n_obs)
x_hat = np.where(x_true == 1.0, u < a_sens, u < 1.0 - b_spec).astype(float)
J = a_sens + b_spec - 1.0
pi_hat = (1.0 - b_spec) + J * pi
ratio_pred = J * math.sqrt(pi * (1 - pi)) / math.sqrt(pi_hat * (1 - pi_hat))
ratio_sim = np.corrcoef(x_hat, ret)[0, 1] / np.corrcoef(x_true, ret)[0, 1]
ppv = a_sens * pi / pi_hat
assert abs(ratio_pred - 0.639) < 1e-3
assert abs(ratio_sim - ratio_pred) < 0.03
assert abs(ppv - 0.486) < 1e-3

for node in baskets:                                           # every number has a source span
    assert node.span in COVENANTS
assert "calculated after giving effect to such adjustments" in rrcs_body
print(f"IC retained: predicted {ratio_pred:.3f}, simulated {ratio_sim:.3f}; flag precision {ppv:.3f}")
```

