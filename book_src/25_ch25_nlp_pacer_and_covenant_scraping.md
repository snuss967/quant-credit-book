# Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets


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

Real agreements have cycles. Halyard's Run-Rate Cost Savings cap refers to Consolidated EBITDA "after giving effect to" the cost savings, and Pro Forma Basis refers to Consolidated EBITDA, which is calculated on a Pro Forma Basis. The standard fix is to compute the **strongly connected components** (Tarjan's algorithm, $O(|V| + |\mathcal{E}^{\text{dep}}|)$), collapse each component into a single super-node, and evaluate the resulting condensation, which is a directed acyclic graph by construction. Inside each component you solve a fixed point. Section 25.3 shows the fixed point for the add-back cap is a contraction, so the iteration converges, and it also shows the cap ends up larger than it looks. Figure 25.1 draws the synthetic Section 1.01 of Listing 25.1 with both of its loops.

![Figure 25.1: In the synthetic Section 1.01 of Listing 25.1, two groups of terms define each other (dashed loops: the add-back cap through Consolidated EBITDA, and the J.Crew blocker), and amending Consolidated EBITDA reaches only three other terms (shaded, β = 3) while Excluded Taxes reaches none. Illustrative: edges produced by the Listing 25.1 term matcher on the book's synthetic agreement text; an arrow runs from a term to each term its definition uses.](assets/figures/ch25_definition_graph.png)

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
> The phrase "unrestricted subsidiary" appears in 1,931 8-K filings from 2024-01-01 through 2026-10-17 (an exact count). *What changed:* J.Crew-blocker vocabulary in 8-K exhibits rose about 37% from 2018 to 2025, while 8-K filings mentioning a first-lien credit agreement fell to about 65% of their 2018 level. The 2021 all-forms spike probably reflects the SPAC wave (S-4 and S-1 registrations), not loans. As a *crude* density, the ratio of blocker mentions to first-lien agreement mentions in 8-Ks went from $847/223 \approx 3.8$ to $1{,}157/146 \approx 7.9$. *What it means:* the public filer base for leveraged loans is shrinking as deals move to private credit (Chapter 17), while the agreements that remain are full of LMT defenses. Two cautions belong in the same box. The numerator and denominator are different document sets. And the API caps `hits.total` at 10,000, so a broad normalizer like "credit agreement" silently returns "≥10,000." The ratio is a picture, not a statistic.

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

At the margin, each dollar of add-back buys $4.50 + 0.35 = 4.85$ dollars of debt capacity, and every one of those dollars can sit ahead of you. Figure 25.2 shows both halves of the arithmetic.

![Figure 25.2: Measuring the 25% cap "after giving effect" lets add-backs reach 33.3% of pre-add-back EBITDA instead of 25% (left), and at Halyard those extra dollars of EBITDA lift incremental debt capacity from \$75mm to \$393.3mm (right). Illustrative: the Halyard terms of §25.3.4, with pre-add-back EBITDA E₀ = \$200mm, a 4.50x first-lien test on \$900mm of net debt with proceeds not netted, and a general basket at the greater of \$75mm and 35% of EBITDA.](assets/figures/ch25_addback_capacity.png)

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

The trapdoor did not create new capacity. It moved the min cut upstream to two baskets that everyone had priced as "small baskets for foreign subsidiaries" rather than as leakage. A list-of-baskets parser sees \$150mm and \$100mm of investment capacity in non-guarantors and moves on. A flow parser sees \$250mm of capacity to unrestricted subsidiaries, and the IP was worth \$250mm. Figure 25.3 draws the two readings side by side.

![Figure 25.3: Reading the trapdoor as capacity zero puts the minimum cut on the trapdoor and gives Φ = 0 (top); reading it as unbounded moves the cut upstream onto the \$150mm and \$100mm baskets and gives Φ = \$250mm (bottom), the value of the IP that moved. Source: basket sizes and the \$250mm IP interest as disclosed in J.Crew's filings and summarized by Torys (May 2019) and King & Spalding; the three-node graph is the stylized model of §25.4.2, solved with the Edmonds-Karp routine of Listing 25.3.](assets/figures/ch25_jcrew_mincut.png)

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

where the inequality is Cauchy–Schwarz, $\|x\|^2 \ge n^2/d$. For a 300-page agreement with $n \approx 150{,}000$ tokens and $d \approx 10{,}000$, the bound gives $1 - \cos \le 4.4 \times 10^{-7}$. At Halyard's $\mathcal{E} = \$266.7$mm, the same edit adds $0.75 \times 266.7 = \$200$mm of ratio capacity. The most expensive token in the document moves cosine similarity by less than one part in two million. Figure 25.4 sets the two measuring sticks against each other.

![Figure 25.4: Swapping one token for another moves a 150,000-token agreement's cosine similarity by about 4 × 10⁻⁷, and it would take roughly 155 amended occurrences of the ratio to move it by 1% (left), while the same edit from 4.50x to 5.25x adds \$200mm of ratio-basket capacity (right). Illustrative: the §25.5.1 count-vector model with 150,000 tokens over a 10,000-word vocabulary (‖x‖² ≈ 2.4 × 10⁶), and Halyard's covenant EBITDA of \$266.7mm against \$900mm of first-lien net debt.](assets/figures/ch25_token_vs_capacity.png)

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

> **Trend Watch. Docket access, 2005–2026: from per-page phone-book to throttled API.** In 2005 Moyer described PACER fees as "reasonable" with "few practical alternatives" (Moyer_Distressed_Debt_Analysis p.286). Free Law Project's RECAP archive has run "since 2009." Its browser extension adds users' PACER purchases to a free mirror that now holds "tens of millions of PACER documents" (free.law/recap; no as-of date given). On 2026-10-17, a single anonymous CourtListener v4 search for `"rule 2019" "verified statement"` returned a count in the high hundreds to low thousands (1,868 on that day), with the newest hits dated September 2026. The feed is current to within weeks, and bankruptcy courts (`txsb`, `njb`, `miwb`, `okwb`) are in it. The shock came on August 7, 2025, when the Administrative Office of the U.S. Courts cited "escalated cyberattacks of a sophisticated and persistent nature on its case management system" (as reported by CNN). Secondary reporting says more than 20 courts then issued standing orders that sealed documents may be filed in CM/ECF but not viewed electronically. *What it means:* the public docket is now cheap, fast and machine-readable, and it can change shape overnight. A feed that silently drops sealed exhibits looks the same as a feed in which nothing happened.

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

and setting $\partial \log \mathcal{L}/\partial q_{ab} = N_{ab}/q_{ab} - T_a = 0$ gives $\hat q_{ab} = N_{ab}/T_a$. This is the right estimator for "how long after a group organizes does it attack exclusivity," and it stays honest about cases still in progress, because their time in state counts in $T_a$ even if no transition has happened yet. Figure 25.5 draws the chain with the Hughes case below it.

![Figure 25.5: The docket state machine runs from Quiet to Confirmed, and the Hughes Satellite Systems case of the Docket Diary below walked Organized to Contested in 31 days and Contested to Standstill in 10, each step marked by a docketed entry. Source: Hughes Satellite Systems Corp., Bankr. S.D. Tex. No. 26-90739, Docs. 154 (2026-08-10), 320 (2026-09-10) and 369 (2026-09-20), as cited in §25.7.2.](assets/figures/ch25_docket_state_machine.png)

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

Go back to the morning Theo spent on page 19. Kaz's first parser found a number and stopped. Theo's method was slower and better: open Section 1.01, read "Consolidated EBITDA," note every defined term inside it, and then do the same for each of those terms until the list stops growing. A human can do that for one agreement in an afternoon with a highlighter and a mild grudge. The desk has to do it for every agreement in the universe, and again whenever an amendment lands at 7:41 a.m. So the first block of the engine is Theo's afternoon compressed into milliseconds, with one extra duty his highlighter never had: it must announce, loudly, when the definitions loop back on themselves, because the EBITDA definition does.

Listing 25.1 builds the definition graph from a short synthetic Section 1.01 written for this book. The input is raw text. The outputs are a dictionary of definitions, a directed edge list, the strongly connected components, and a blast radius for any term. `parse_definitions` finds each line of the form `"Term" means ...` and stores the body together with its character offset, which is the citation anchor that every later number will point back to. `find_references` then scans each body for the other terms. The matcher is case-sensitive, word-bounded and tolerant of plurals. It takes the longest terms first and marks the characters it has consumed, so that "Unrestricted Subsidiary" cannot leave a "Restricted Subsidiary" hiding inside it. The listing asserts that the naive case-insensitive test would draw the wrong edge. `tarjan_scc` then collapses each loop into one component and emits components with dependencies first, which is the evaluation order for Section 25.3; the asserts check that ordering edge by edge. Two adjacency matrices confirm Lemma 25.1: the matrix over terms is not nilpotent, because loops exist, and the matrix over components is, because the condensation is a DAG. Finally `blast_radius` walks the edges backwards, so amending Consolidated EBITDA reaches the First Lien Net Leverage Ratio and amending Excluded Taxes reaches nothing.

The printout shows two loops, not one. Beyond the add-back loop through Consolidated EBITDA and Run-Rate Cost Savings, there is the J.Crew blocker: a Restricted Subsidiary is a Subsidiary that is not an Unrestricted Subsidiary, an Unrestricted Subsidiary may not own Material Intellectual Property, and that term is defined by reference to the Restricted Subsidiaries. A term that mentions itself is dropped from the edges and reported separately.

Use this before any basket arithmetic, on any agreement whose Section 1.01 follows the usual shape. Do not mistake it for a reader of the agreement; it knows the dictionary and nothing else. The edge case that bites is the one-line body. The pattern reads from the opening quotation mark to the end of the physical line, so a definition that wraps onto a second line contributes only its first line, and one that begins "has the meaning assigned to such term in Section 7.02" contributes nothing. Every edge hiding in the lost text vanishes without an error. Count the parsed terms against the quoted terms in Section 1.01 before you believe a graph.

*The full listing is [Listing 25.1 in Appendix F](#code-25-1).*

The graph tells ROBO which terms to evaluate and in what order. It does not say how many dollars the borrower can raise, and "thirty percent of what?" only gets answered once a sentence has become a function with units. Agreements state their baskets in several dialects, and each dialect has a trap that costs real money: a floor-or-percentage ratchet, a leverage test that forgot to say "without netting," an add-back cap measured on the wrong base, a cumulative builder computed over a trailing window. Theo's sticky note says a basket is a function. This is the block where the function is written down and tested, in millions, against the Halyard numbers of Section 25.3.4.

Listing 25.2 turns two synthetic covenant lines and the add-back definition from the previous listing into the capacity table of Section 25.3.4. Three small regular expressions turn sentences into typed objects. A `Grower` holds a fixed floor and a percentage of EBITDA and returns the larger. A `RatioBasket` holds the permitted multiple, the debt in scope, the cash it may net, and a flag for whether the cash proceeds of the new debt count; it returns zero when EBITDA is zero or negative, and it returns infinity when proceeds are netted and the test passes at all. `parse_baskets` converts dollars to millions and percentages to fractions, and sets the netting flag to true unless the clause contains the words "without netting." The scope debt of \$900mm is not in the text at all; the caller supplies it from the capital structure.

`addback_fixed_point` evaluates the cap on Run-Rate Cost Savings. If the definition says "after giving effect," it iterates the map of Section 25.3.3 until it stops moving, and it refuses any cap outside zero to one, because then the map is not a contraction and a human should read the definition. Otherwise it takes the simple minimum. The listing reads the cap and the "after giving effect" phrase from the Run-Rate Cost Savings body parsed in Listing 25.1, so the blocks are chained. On \$200mm of base EBITDA with \$80mm claimed, the add-back is \$66.7mm after giving effect and \$50mm before. Total incremental capacity moves from \$75.0mm to \$393.3mm, and a finite-difference check recovers the 4.85 slope. `builder_available` implements Equation (25.2) over the whole quarterly history, so losses count double and the result is floored at zero.

Use it to turn parsed text into a capacity vector you can diff and price. A clause the expressions never match produces no node and no error. The edge case that bites is infinity. A ratio test that nets the proceeds of the new debt really does allow unlimited borrowing, and a parser that reports so is reading a badly drafted document correctly. But the netting flag is set by the literal words "without netting," so a clause that reaches the same protection in other words comes back infinite, and a single `inf` poisons every sum it enters. Treat any infinity as a ticket for a human to read the clause, never as a number.

*The full listing is [Listing 25.2 in Appendix F](#code-25-2).*

"So the borrower's lawyers solved a max-flow problem," said Kaz, and the sentence is the whole design brief for the next block. A list of baskets cannot say how much value can leave the collateral pool, because the binding constraint depends on how the baskets connect. A \$150 million basket and a \$100 million basket look like small change for foreign subsidiaries until a third provision connects the room they open onto to the exit. The desk wants two outputs: a dollar figure for leakage capacity, $\Phi$, and, more usefully, the name of the basket that binds, because that is the sentence worth a lawyer's afternoon.

Listing 25.3 implements the Edmonds-Karp form of max-flow on a graph whose arcs are baskets. Each arc is a tuple of from-entity, to-entity, basket name and dollar capacity in millions. The function first builds a residual graph, adding a zero-capacity reverse arc for every forward arc so that flow sent down a poor route can be taken back later. Then it loops. A breadth-first search finds the shortest path with spare capacity from source to sink. The smallest residual on that path is pushed through, the residuals update, and the pushed amount joins the running total. When no path remains, the total is $\Phi$. One more search from the source, across arcs that still have slack, marks the reachable side, and the original arcs that cross from the reachable side to the unreachable side are the minimum cut, returned by basket name. If an uncapped route runs all the way from source to sink, the function returns infinity and an empty cut, because there is no basket to name.

The sample is the J.Crew route of Section 25.4.2: two parallel arcs from the loan parties to a non-guarantor restricted subsidiary, at 150 and 100, and a trapdoor arc onward to the unrestricted subsidiary. With the trapdoor at zero, the answer is zero and the cut is the trapdoor. With the trapdoor at infinity the answer is \$250mm and the cut is the two upstream baskets, whose capacities sum to the flow, as the theorem promises. The trapdoor created no capacity. It moved the cut onto baskets everyone had filed under "small."

Use it on any permissions network where the question is how much can pass and through which door. Do not use it where the arcs are not capacities in one currency. The edge case that bites is in the last lines. The listing models a blocker by rerunning the same single-commodity graph, once with the trapdoor shut and once open, and relabelling the answers as "IP blocked" and "cash open." It does not solve a real multi-commodity flow. A blocker closes the Material Intellectual Property route and leaves cash routes alone, but the two commodities draw on the same \$250mm of basket capacity, so their capacities cannot be added. Read the pair as an upper bound for each, never as a sum.

*The full listing is [Listing 25.3 in Appendix F](#code-25-3).*

*Lazy Prices* made money from the observation that firms which rewrite their filings underperform firms which don't, and the tempting port is to run the same similarity score on every credit-agreement amendment and sort by change. Anyone who has watched a sponsor amend a leverage multiple knows why that fails, and a desk that has never watched one learns it from a backtest, which is the expensive way. The amendment that moves \$200 million of capacity changes one number in a document of 150,000 words. Before ROBO builds a diff, it should be shown the size of the problem.

Listing 25.4 is that demonstration, and it is a test rather than a tool. It draws a synthetic agreement as a count vector over a 10,000-word vocabulary with 150,000 tokens, plants the token "4.50" exactly once and "5.25" not at all, and then swaps one for the other, which is the amendment. It computes the cosine similarity of the two versions and asserts two things: that one minus the cosine equals one over the squared length of the count vector, and that this sits below the Cauchy-Schwarz bound of vocabulary size over token count squared. The printed gap is about 4 x 10^-7, a number no sane similarity threshold will flag.

Then it measures the same edit the way the desk should. It builds a ratio basket with the amended multiple using the `RatioBasket` class and the add-back-adjusted EBITDA from Listing 25.2, and takes the difference in capacity: exactly \$200mm. One edit, two measuring sticks. The first reads zero for practical purposes, and the second reads a fifth of a billion dollars. That is the argument for diffing the capacity vector of Section 25.5.1 and not the tokens.

The edge case that bites is the setup that makes the identity exact. The old number appears once and the new one never. In a real agreement a ratio literal recurs in the incurrence test, the pricing grid and a definition, and an amendment may touch one occurrence or all of them. So treat the toy as the cleanest case for the argument, and treat the capacity change, not the cosine, as the measurement. The block also draws its counts from the generator seeded in Listing 25.1, so run out of order it sees different random numbers, though the conclusion does not change.

*The full listing is [Listing 25.4 in Appendix F](#code-25-4).*

A desk that reads every filing every morning makes a great many requests before breakfast, to a regulator that has published its patience in one sentence: ten requests per second. The penalty for exceeding it is not a fine. It is a block, and a blocked desk reads nothing, which on a docket-driven strategy is indistinguishable from a quiet week. ROBO's first ingest gave every worker its own limiter and set the burst allowance equal to the rate, which broke the limit in two different ways at once. Lemma 25.2 explains why, and the next block lets you watch it happen.

Listing 25.5 implements the token bucket of Section 25.6.2 and tests the lemma against it. `TokenBucket` holds a rate, a burst size and a current level. Each call to `try_acquire(now)` first tops up the level by the elapsed time multiplied by the rate, capped at the burst, then spends one token if at least one is there and reports yes or no. The clock is passed in, not read, which keeps the class deterministic and testable.

The test throws 6,000 request attempts uniformly across 60 seconds, a demand of 100 per second, at two buckets. The naive bucket has rate 10 and burst 10, which is what a developer would write after reading "ten requests per second." The safe bucket has rate 8 and burst 2, chosen so that the burst plus one second of refill stays within the limit of 10. `max_in_window` slides a one-second window across the admitted timestamps and finds the busiest one. The naive bucket reaches 19 requests inside a single second, comfortably under the lemma's ceiling of 20 and nearly double what EDGAR allows. The safe bucket peaks at 9. The listing asserts all three facts. It closes with the User-Agent header the SEC asks for, carrying a placeholder mailbox that must be replaced by a real one, and a function that builds the submissions URL by zero-padding the CIK to ten digits, which is the classic ROBO bug.

Put a bucket like this in front of every external host, one per host, set from that host's own published limit. The edge case that bites is the word "global." The class is a single object in a single process. Several workers with private copies admit several times the budget, and the docstring itself says to move the state behind a lock or into a shared store before going to production. A per-second bucket also says nothing about a daily cap, which is the problem the next listing walks into.

*The full listing is [Listing 25.5 in Appendix F](#code-25-5).*

A limiter in a test harness is not an ingest. The live version has to wait its turn, survive the 403s and 503s that public data sources hand out whenever their hosting is in a mood, and decide when to stop retrying and tell a person, because a feed that silently stops looks exactly like a quiet docket. (The list of ways this blows up in Section 25.6 ends with three words: alert on silence.) The smallest honest version of that loop is short enough to read in one sitting, and it is run against the two sources the engine needs.

Listing 25.6 is a sketch. It is not executed with the other blocks, because it needs network access, a real contact mailbox and a CourtListener token. `polite_get` creates a bucket at the safe EDGAR setting and wraps `requests.get` in three behaviors. It waits, polling every ten milliseconds, until the bucket releases a token. It sends the request with a thirty-second timeout. And if the status is 403, 429 or 503 it sleeps for two to the power of the attempt number, so one, two, four, eight and sixteen seconds, then tries again; any other bad status raises, and success returns the parsed JSON. After five failures it raises a `RuntimeError` naming the URL, which is where a real deployment would page a person.

Two calls follow. The first asks EDGAR full-text search for the phrase "unrestricted subsidiary" in 8-Ks filed from 2024-01-01 to 2026-10-17, which is the query behind the Trend Watch box in Section 25.2. The second asks CourtListener for Rule 2019 "verified statement" documents in the Serta Simmons docket, 23-90020, in the Southern District of Texas. The `type` of `rd` returns documents rather than dockets, which is the only way to list every Rule 2019 filing in a case.

Use it as the template for per-host adapters, not as it stands. The edge case that bites is that one bucket serves two hosts. Eight requests per second with a burst of two is shaped for EDGAR. CourtListener's default tier allows 5 requests per minute and 125 per day, and this bucket would happily release a day's allowance in about sixteen seconds. Each host needs its own bucket, set from its own published limits. Retrying a 403 also deserves suspicion: against a portal that has decided you are a bot, five polite retries just make a longer log.

*The full listing is [Listing 25.6 in Appendix F](#code-25-6).*

Section 25.7 made a promise. The Rule 2019 statements an ad hoc group files disclose quantities and dates but never prices, and from them a desk can build a holdings time series, a blocking test and an imputed cost basis. Ines's line was that a cost basis is a hand and Rule 2019 makes the group show you half of it. The catch is one a poker player knows: the information arrives in installments, rounded, from people who file when they have a reason to. Below are two statements from one synthetic group and the arithmetic a desk runs on them before anyone calls the group's counsel.

Listing 25.7 starts from eight synthetic lots across two verified statements, filed 2026-01-15 and 2026-03-02, against a class with \$1,000mm of face. Each lot has a holder, a face amount and an acquisition quarter. A pivot sums face by holder and statement, which gives the panel of Section 25.7.1. From the panel the code takes three things. The first is the group's share of the class, $\theta$, which moves from 24% to 33%. The second is each holder's flow, the difference between statements: Holder_A adds \$30mm and a new member, Holder_D, arrives with \$60mm. The third is a rounding interval. Statements say "approximately," so each member's figure is good to half a million dollars, and with four members that is 0.2 points of the class.

`blocks` is the amount test of 11 U.S.C. 1126(c): a group defeats acceptance when its share exceeds a third of the face that votes. At 60% turnout, 33% blocks. At full turnout it falls short of 33.3% by a third of a point, which is the sort of margin lawyers bill for. The numerosity prong, more than half in number, is not coded. The imputed basis maps each lot's acquisition quarter to a synthetic quarterly average price and takes the face-weighted average per holder from the latest statement: 82 for Holder_A and 58 for Holder_D. Last comes a Herfindahl index of the disclosed holdings, labelled a lower bound, because a holder who never filed is invisible and every added holder can only raise the sum of squares.

Use it to turn each new statement into a panel row within minutes of filing. Do not read the output as the whole class; it is the filers. The edge case that bites is the price map. Rule 2019 excuses the acquisition quarter for interests acquired more than a year before the petition, so some lots will arrive without one. Here a missing quarter becomes a missing price, which pandas skips in the numerator of the weighted average but not in the denominator, so the basis sinks toward zero with no warning. Leave a single \$30mm lot unpriced and Holder_A's basis of 82 reads as 70.4. Make the code refuse a lot it cannot price.

*The full listing is [Listing 25.7 in Appendix F](#code-25-7).*

Hughes took 31 days to go from Organized to Contested and ten more to reach Standstill. One case is an anecdote. A panel of cases is a rate, and a rate is what lets a desk ask how long after a group organizes it usually attacks exclusivity, and how nervous to be when day 60 passes with nothing on the docket. The estimator is a division. The interesting part is the denominator.

Listing 25.8 runs the maximum-likelihood estimator of Section 25.7.2 on a three-case toy panel. Each row is a spell: a case, the state it was in, the days it spent there, and the state it moved to, with a blank meaning it is still there. Case 1 mimics the Hughes sequence. Case 2 contests after 45 days and has sat in contest for 60 more. Case 3 has been Organized for 90 days and nothing has happened. The code sums days by state to get the exposure $T_a$, counts transitions by pair of states for $N_{ab}$, and divides. Organized to Contested comes out at 2 over 166 per day, because all 166 days count, including case 3's silent 90. Contested to Standstill comes out at 1 over 70. Drop the unfinished spells, the tempting move, and the first rate becomes 2 over 76, more than double, because only the cases that moved survive to be counted.

Use it to put an expected clock on a docket stage, and to flag a case that has outlived its peers. Do not trust three cases, and do not forget the model's assumption: the intensity is constant within a state, so waits are exponential, and a hearing date set by a judge's calendar is not memoryless. The edge case that bites is censoring. Cases in progress carry the most recent information and the least complete one, and an estimator that discards them overstates how fast dockets move.

*The full listing is [Listing 25.8 in Appendix F](#code-25-8).*

Everything before this point assumed the clause classifier was right. It will not be. The question for the desk is not whether the classifier errs but what the errors cost in alpha, and Section 25.9.1 puts the price in one formula built on Youden's index. A formula is a claim, though, and a simulation is evidence. The engine also needs one last assertion before it ships a number: that the sentence the number points to exists. That assertion is the citation contract, and it is what keeps the model's mistakes from becoming the desk's.

Listing 25.9 has two jobs. The first simulates the IC tax of Equation (25.3). It draws 400,000 synthetic documents with a true feature at a 5% base rate, builds a forward return equal to the feature plus unit-variance noise, and generates a classifier flag with 90% sensitivity and 95% specificity, each flag drawn independently of the return once the truth is known. It computes the predicted retention from $J = 0.85$ and the flagged rate of 9.25%, and compares it with the ratio of correlations in the simulation: 0.639 predicted, about 0.647 simulated, inside the 0.03 tolerance the assert allows. At that retention you need roughly 2.45 times the breadth to break even. It also confirms the flag precision of 0.486, which is the number that surprises people who hear "95% specific": about half the flags are false.

The second job is the citation contract in miniature. For every parsed basket it asserts that the stored span is a substring of the covenant text, and it asserts that the phrase "calculated after giving effect to such adjustments" is in the Run-Rate Cost Savings body that the fixed point relied on. A number whose sentence cannot be found fails the build.

Use the simulation to translate a validation-set confusion matrix into the extra breadth you must find, and use the assertions at every stage that emits a number. The edge case that bites is the assumption the simulation builds in by construction: errors are independent of the return once the truth is known. If the classifier misses more often on unusual documents, and unusual documents are where the returns are, the errors correlate with the outcome and Equation (25.3) flatters you. The span check has its own limit. It proves the sentence exists, not that the number was computed from it.

*The full listing is [Listing 25.9 in Appendix F](#code-25-9).*


## 25.11 Desk Debrief

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
- Bloomberg *Odd Lots* (Joe Weisenthal and Tracy Alloway). Search the archive for episodes on liability management, J.Crew, Serta and private credit. No specific episode is cited here.
- Bloomberg *Credit Edge*. Interviews on leveraged finance and restructuring. No specific episode is cited here.

**Practitioner Writing**
- Torys LLP (May 2019), "The J.Crew 'trap door' and its implications for the future of leveraged finance": https://www.torys.com/our-latest-thinking/publications/2019/05/the-j-crew-trap-door-and-its-implications-for-the-future-of-leveraged-finance
- King & Spalding, "How did they do it: J. Crew": https://www.kslaw.com/attachments/000/008/521/original/How_did_they_do_it_J._Crew.pdf
- Locke Lord (October 2017), "J.Crew Group, Inc.": https://www.lockelord.com/newsandevents/publications/2017/10/jcrew-group-inc
- Cleary Gottlieb (March 13, 2007), *Bankruptcy Court Requires Ad Hoc Equity Committee Members to Submit Detailed Information on Holdings Under Bankruptcy Rule 2019(a)*.
- Paul Weiss / Practical Law (2025), *Covenant-Lite Loans: Overview* (PitchBook|LCD figures).
- Griffin, Nini & Smith, Harvard Law School Forum on Corporate Governance post (November 4, 2022).
- Huang, Lewellen & Wang, Harvard Law School Bankruptcy Roundtable post (February 11, 2025).
- Matt Levine, *Money Stuff* (Bloomberg Opinion), on J.Crew, Serta and "open market purchase."

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
