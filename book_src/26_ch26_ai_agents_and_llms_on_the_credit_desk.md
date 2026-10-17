# Chapter 26: AI Agents & LLMs on the Credit Desk

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 26.x" section):
26.0 Cold open; 26.1 What a language model is, for a specifier; 26.2 Trend Watch: adoption 2022-2026;
26.3 The tool stack: what is sold vs. what it is; 26.4 Citation contract; 26.5 Hallucination controls + Trend Watch 2;
26.6 Workflows first, agents last; 26.7 Agentic alpha research & multiple testing; 26.8 Model risk for stochastic readers;
26.9 The AI-specifier's operating manual; 26.10 Prompt injection in the data room; 26.11 Case studies;
26.12 Specification for AI Implementation (cumulative python); 26.13 Desk Debrief, Spec You Hand the Robot, Exercises;
Deep-Dive Resource Graph. -->

## 26.0 Cold Open: Section 6.08(b)(xiv)

The summary came back in eleven seconds. That was the first warning sign: nothing true about a restricted payments covenant has ever taken eleven seconds.

Theo had given ROBO the credit agreement for Halyard Holdings, a fictional sponsor-backed widget maker the desk uses as its practice dummy (312 pages, two amendments, and one "technical" amendment that was not), and typed: *Summarize the restricted payments covenant.* ROBO returned four clean paragraphs: a builder basket, a ratio-based unlimited basket at 5.25x, a general basket at "the greater of \$40mm and 30% of Consolidated EBITDA," and a management-equity basket. Every paragraph had a citation. The general basket cited §6.08(b)(xiv).

Theo opened the PDF. Section 6.08(b) ran from (i) to (xii) and then stopped, with the calm of a document that has said everything it means to say.

"There is no fourteen," he said.

Kaz leaned over. "It's within two of the right answer."

"So is a bluff," said Ines, without looking up.

"The builder basket is real, though," Kaz went on. "Who's the builder? Does the contractor need to be bonded?"

"It builds from retained excess cash flow."

"So it's a contractor who only works with your money." Kaz thought about it. "That's every contractor."

Mags spoke from two desks over, in the voice she saves for things that used to be worse. "Back in my day, an associate who made up a section number got fired by phone, and by grudge, before the closing dinner. This thing makes one up in eleven seconds, and nobody gets fired."

Theo checked the other three paragraphs. They were right: the right numbers, the right sections, the right cross-references to the definition of Available Amount. That made it worse. A summary that is wrong everywhere gets thrown away. A summary that is right three times out of four teaches you to stop checking, and the fourth paragraph is the one that sizes the position.

Ines finally turned around. "What's the pot, what are the odds, and who at this table knows more than you? Right now, the document does. The robot is just the one talking loudest."

So here is the question this chapter answers: **how do you put a machine that is sometimes wrong, and confident when it is, into a process that may never be wrong silently?**

By the end of this chapter you will be able to:

- treat a language model as a *stochastic reader* with measurable power, calibration, and failure modes, and validate it the way Bohn and Stein validate a PD model;
- write a **citation contract** that makes every machine claim checkable by code, and measure the three rates (accuracy, validity, support) together with the one that hurts, the "footnoted hallucination";
- set an **abstention threshold** from the desk's own costs instead of from vibes, and see why benchmark scoring trains models to guess;
- compute the reliability of an agent chain with an imperfect verifier, and explain why "workflows first, agents last" is arithmetic and not taste;
- govern an LLM like a vendor model (SR 11-7 lineage, FINRA Notice 24-09, FINRA's 2026 oversight report) and wire it into the desk like an untrusted data feed;
- hand ROBO a specification it cannot misread, which turns out to be a skill you already have: you used to call it reading a credit agreement.

## 26.1 What a Language Model Is, for a Specifier

Strip away the marketing and a language model is one object: a conditional distribution over the next token given everything before it. Write $x_{1:t}$ for the token sequence so far (the prompt, the retrieved pages, the model's own output to date) and $\theta$ for the frozen weights. The model supplies

$$
p_\theta(x_{t+1} = v \mid x_{1:t}), \qquad v \in \mathcal{V},
$$

a probability for every token $v$ in a vocabulary $\mathcal{V}$ of order $10^5$ entries. Generation samples one token, appends it, and repeats. The *temperature* $T>0$ reshapes the distribution before sampling,

$$
p_T(v \mid x_{1:t}) = \frac{p_\theta(v \mid x_{1:t})^{1/T}}{\sum_{u \in \mathcal{V}} p_\theta(u \mid x_{1:t})^{1/T}},
$$

so $T \to 0$ concentrates all mass on the most likely token (greedy decoding) and $T = 1$ samples from the model as trained. Three consequences matter for anyone who will specify work to one of these.

**First, the model produces text that is probable given the text, and "probable" equals "true" only under conditions.** When the answer is stated in the context, is salient, and is determinate, the most probable continuation is usually the correct one. When any of those fails, the model still produces the most probable continuation, and the most probable continuation of "the general basket appears in Section 6.08(b)(" is a plausible roman numeral. That is why fabricated citations look right: they are draws from the distribution of real citations. §6.08(b)(xiv) is not a random error. It is a *typical* one, and that is the bad news.

**Second, the model is a reader, not a calculator.** Arithmetic done "in its head" is next-token prediction over digits. On a credit desk this rule has no exceptions: the model may *locate* the "greater of \$40mm and 30% of Consolidated EBITDA" clause and *extract* its parameters into a typed record, but the capacity is computed by deterministic code (§26.12), and so are the waterfall, the leverage ratio, and the make-whole. The model calls tools; it does not impersonate them.

**Third, a token is both the unit of cost and the unit of attention.** Vendors price per million input and output tokens, and a model's context window, its working memory, is measured in tokens too. A 300-page credit agreement is roughly 150,000 words, or 200,000 to 260,000 tokens depending on the tokenizer *(approx.; one vendor's pricing page notes that its newer tokenizer produces about 30% more tokens for the same text)*. "It fits in the context window" is now true of most single documents. Whether the model *used* what was in the window is a different question.

### Reading is not using

Liu et al. (2023), *Lost in the Middle* (TACL), put the relevant fact for a question at different positions in a long context and measured accuracy. The curve is U-shaped: facts near the start or the end of the context are used, and facts in the middle are used much less, even by models built for long contexts. A credit agreement's definitions sit at the front, its covenants in the middle, and its signature pages at the end. The U-curve therefore puts the least attention on the part of the document that decides recoveries. Liu and Liu (2026), *Reading Is Not Using*, sharpen the point for financial documents: as unrelated context grows from 2,000 to 128,000 tokens, a risk disclosure's influence on the model's judgment decays to the noise floor, *even though the model can still retrieve the disclosure when asked*. Retrieval accuracy and decision influence are different measurements, and only the second one moves money.

> **Desk Myth vs. Desk Reality.** *Myth:* "We gave it the whole agreement, so it considered the whole agreement." *Reality:* You gave it the whole agreement the way you give a summer analyst the whole data room. What was actually read depends on position, on salience, and on what was asked. Ask narrow questions against retrieved spans, with the span's location logged, and measure accuracy by position (§26.12 includes a toy U-curve test).

### The stochastic reader, formally

For the rest of the chapter, a *reader* is a randomized map

$$
\mathcal{R}_\theta : (q, \mathcal{D}, \xi) \mapsto y,
$$

from a question $q$, a document store $\mathcal{D}$, and the sampling randomness $\xi$ (temperature, seed, and, as §26.9 shows, the inference server's batch composition) to an output $y$. The desk cares about the physical-measure probability $\Pr^{\mathbb{P}}\big(A(y) = 1 \mid q, \mathcal{D}\big)$ that the output is correct, about how that probability varies with the question type, the position of the evidence, and the document length, and about whether the reader *knows* it. One convention, stated once: every probability in this chapter is a $\mathbb{P}$ quantity, an error rate, an agreement rate, or a cost. No LLM output is ever a $\mathbb{Q}$ object. Spreads, hazard rates, and implied vols enter the chapter only as inputs to, or outputs of, the deterministic pricers that the reader feeds.

This framing has a payoff that the rest of the chapter collects. A reader with a measurable hit rate, a measurable calibration curve, and measurable failure modes is a *model*, and credit has a mature discipline for validating models of exactly this type: binary outcomes, rare costly errors, and a regulator who wants documentation.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.394:* "Diagnosability: In conjunction with transparency, the ability to drill into a model's behavior is an important aspect of validation. To the extent that a model's behavior cannot be diagnosed quickly and efficiently, the portfolio manager or risk manager will face more model risk."
>
> **Annotation.** Bohn and Stein list five validation dimensions for PD models on the same page: robustness, power, calibration, transparency, and diagnosability. A large language model scores worst on the fifth. Its weights are not inspectable in any useful sense, its reasoning trace (when it shows one) is itself generated text with no guaranteed causal link to the answer, and its behavior shifts with the vendor's version. You cannot drill into the reader. So the desk makes every *output* diagnosable: each claim carries a document id, page, and character span that code can resolve and check (§26.4). Diagnosability moves from the model to the claim, and that is the central engineering move of this chapter. The other four dimensions map over almost unchanged: power is the reader's ability to separate right answers from wrong ones by its stated confidence, calibration is whether "90% sure" is right 90% of the time, robustness is behavior under a bad scan or an adversarial PDF (§26.10), and transparency is whether a human can trace a claim back to the page.

## 26.2 Trend Watch: The Reading Machine Arrives on the Desk, 2022–2026

> **Trend Watch.** *From chatbot to connector to agent, with the regulators one step behind and then, briefly, one step back.*
>
> - **Nov 30, 2022.** ChatGPT launches. Within months, every credit desk has an analyst pasting covenants into it and a compliance officer drafting a memo about why they shouldn't.
> - **Mar 30, 2023.** BloombergGPT (Wu et al., arXiv:2303.17564): 50 billion parameters, trained on a 363-billion-token financial corpus plus 345 billion general tokens. It is the high-water mark of "train your own finance model"; the next three years mostly belong to general models with retrieval.
> - **Apr 2023 onward.** Lopez-Lira and Tang (arXiv:2304.07619; v6 Oct 28, 2025) show GPT-class models can read post-cutoff headlines into next-day return predictions, and, in later versions, that the returns decline as LLM adoption grows. A trend that eats itself is still a trend.
> - **Jul 26, 2023.** The SEC proposes rules on conflicts of interest from "predictive data analytics" at broker-dealers and advisers (Federal Register Aug 9, 2023). **Jun 17, 2025:** the SEC withdraws the proposal, with others from 2022–23 (Federal Register 2025-11110), saying it does not intend to issue final rules.
> - **Mar 18, 2024.** First SEC "AI-washing" settlements: Delphia (\$225,000) and Global Predictions (\$175,000), for claiming AI capabilities they did not have (SEC press release 2024-36).
> - **Jun 27, 2024.** FINRA Regulatory Notice 24-09: the rules are technology-neutral; supervision under Rule 3110 should cover model risk management, data integrity, and the reliability and accuracy of AI models; Rule 2210 applies to AI-generated communications.
> - **Nov 14, 2024.** The FSB's report on AI and financial stability names third-party dependency and concentration, market correlation, cyber risk, and model risk as the vulnerabilities, and notes how thin the usage data is.
> - **Nov 21, 2024.** The third Bank of England/FCA survey (118 firms): 75% already use AI and 10% plan to within three years (58% and 14% in 2022). A third of use cases are third-party implementations, foundation models are 17% of use cases, and the top three providers account for 73% of reported cloud providers and 44% of model providers.
> - **Nov 25, 2024.** Anthropic open-sources the Model Context Protocol (MCP), a standard port between models and data sources. **Dec 19, 2024:** its "Building effective agents" essay draws the line between *workflows* (LLM steps on predefined code paths) and *agents* (the model directs its own tool use).
> - **2024–2025.** Stanford's AI Index 2025: the inference cost of GPT-3.5-level performance fell more than 280-fold between Nov 2022 and Oct 2024; 78% of organizations reported using AI in 2024, up from 55% in 2023.
> - **Jul 15, 2025.** Anthropic's "Claude for Financial Services" ships connectors to FactSet, S&P Global, PitchBook, Morningstar, Daloopa and others; named customers include Bridgewater's AIA Labs, AIG, and Commonwealth Bank of Australia.
> - **Dec 9, 2025.** FINRA's 2026 Annual Regulatory Oversight Report adds a GenAI section. The top use case among member firms is "Summarization and Information Extraction." Among the agent risks it lists: "AI agents acting autonomously without human validation and approval."
> - **2026.** Stanford's AI Index 2026 reports 88% organizational adoption and SWE-bench Verified rising from about 60% to near 100% in one year, with agents still failing about one in three structured-benchmark tasks. **Jun 4, 2026:** the Vals AI Finance Agent benchmark (537 questions, built with Stanford researchers and a G-SIB) has a top score of 64.37%. **Oct 2026:** the fifth Evident AI Index ranks 50 banks, with JPMorganChase first.
>
> *What it means for the desk.* Reading got cheap (two orders of magnitude in two years) and checking did not. The binding constraint moved from "can we read every 8-K and every docket entry?" to "can we prove what the machine said about them?" The firms that pulled ahead were the ones that treated the model as a component behind contracts, logs, and tests. In July 2026 Acadian's systematic credit PM Michael Doros said, in an FI Desk interview, that "AI itself is unlikely to be the competitive advantage." On a desk where everyone rents the same three models, the edge is in the spec, the eval, and the data. *(Sources: the primary documents named in each line; URLs in §26.14.)*

Two numbers from the desk's own plumbing put this in perspective. Tradeweb's FY2025 10-K reports that over 40% of its institutional credit trades went through AiEX, its rules-based automated execution tool, and in October 2026 Vanguard described about 70% of its fixed-income desk volume as low- or no-touch (Chapter 2). None of that automation is a language model. The rules-based kind arrived first, and it is held to deterministic standards: every AiEX ticket follows a rule a human wrote and can replay. The question for 2026 is whether the reading machine can be held to the same standard. Most of this chapter argues that it can, *for its outputs*, if you build the harness, but not for its internals.

There is a market-structure point too, and it belongs on the risk committee's agenda next to the bid-ask. The BoE/FCA figure, three providers behind 44% of reported model providers in the UK survey, is a concentration statistic of the kind Chapter 22 tracks for dealers and venues. If every desk's covenant reader runs on one of three models, then every desk's covenant reader misreads the same unusual clause in the same way on the same morning. That is correlated model error, which is what the FSB report means by "market correlation." For a credit desk the concrete version is a novel LMT structure that every model classifies as "permitted" because the training data is full of sponsor-side memos saying so. The market then learns the reading is wrong all at once, the way markets learn everything important.

## 26.3 The Tool Stack: What Is Sold vs. What It Is

Every vendor deck in 2026 has the word "agentic" on slide two. Take the products apart and almost all of them are the same three components bolted together: a **retriever** that finds relevant records (TRACE prints, filings, research notes, docket entries) in a store the vendor controls; a **reader** that turns those records plus your question into text; and a **narrator** that makes the text sound like a senior analyst. LTX, the Broadridge-owned bond platform, describes BondGPT on its own site as "LTX's generative and agentic AI application for corporate bond trading." Terminal vendors and portfolio-platform vendors ship assistants in the same mold. (Their launch dates are not verified here, and this book does not guess them.) Then there are general-purpose models wired to data vendors through connectors, the July 2025 financial-services packages being the clearest example. The shape is the same everywhere: structured data in, retrieval in the middle, language out.

"So BondGPT prices bonds?" Kaz asked, the first time Theo showed him the demo.

"It talks about prices. The pricing is done by things that can be fined."

That is the rule this chapter is built on, and it needs a box of its own:

> **The Loop Rule.** The language model sits *around* the pricing loop, never *in* it. It may emit structured features with provenance that deterministic pricers consume: basket capacities, change-of-control trigger flags, a J.Crew-blocker indicator, a Rule 2019 holder table, an "LMT chatter" score from a docket. It may narrate what a deterministic pricer did and why. It never emits a price, a spread, a hedge ratio, or a size, and nothing it writes reaches an order without passing a typed, bounded, logged gate.

The reason is not that models are bad at numbers, although they are worse at arithmetic than at reading. The reason is accountability geometry. A quote has to be reproducible: the desk must be able to say, for any RFQ answered at 2:58 p.m., exactly which inputs produced which price. A deterministic pricer satisfies that by construction. A stochastic reader satisfies it only if its output is logged as a point-in-time datum and treated as an *input* (§26.9). Put the reader inside the loop and every quote inherits its nondeterminism. Put it around the loop and the nondeterminism is quarantined in a feature column with a provenance pointer, where it can be audited, ablated, and turned off.

Where does the reader earn money on a credit desk? In roughly descending order of 2026 return on effort:

1. **Documents to features.** Covenant terms, definitions, baskets, and amendments extracted into typed records with spans (Chapter 25 builds the parser; this chapter builds the contract that keeps it honest). This is the RSSG reader's home ground, and the place where the shelf says quant credit had barely started.
2. **Surveillance triage.** Every 8-K, every docket entry on CourtListener/RECAP, every Rule 2019 statement, read within minutes and routed by a classifier with a measured false-negative rate. The machine does not decide; it ranks what a human reads first.
3. **Post-trade narration.** RFQ post-mortems, markout commentary, and "why did we lose that PT" notes drafted from the hand history (Chapter 3), with every number pulled from the database rather than typed by the model.
4. **Research synthesis.** Literature and filing summaries with citations under the contract of §26.4.
5. **Code and tests for ROBO.** The highest-leverage use of all, and the subject of §26.9.

The evidence on what readers are *bad* at in credit is just as useful. Drinkall, Pierrehumbert, and Zohren (2024) find that generative LLMs forecast corporate credit ratings worse than gradient-boosted trees fed fundamentals, macro data, and text embeddings. Baesens et al. (2026) find that *tabular* foundation models, which are a different architecture from a chat model, are generally the best out-of-the-box PD and LGD predictors, and that their edge grows as datasets shrink, which is exactly the low-default-portfolio problem of Chapters 5 and 11. Omega² (Majumdar et al., 2025) gets test AUC above 0.93 on 7,800 agency ratings by pairing boosted trees with LLM reasoning, not by replacing them. The pattern is consistent: language models win where the input is language, and trees still win where the input is a table. On the microstructure side, FinDialogLens (2026) extracts trade events from multi-party dealer chatrooms with 92.1% accuracy on the final price and 94.3% on the outcome, which makes Ines's hand histories partly machine-readable and is a preview of where Chapter 18's RFQ data is heading.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.32:* "The relatively few alternative data approaches that we have seen applied to quant credit strategies thus far include: analysing company linkages (suppliers and customers) from the Revere dataset (Bloomberg also offers a competing dataset); bond short interest information; text-mining credit analysts' reports."
>
> **Annotation.** In 2022, Man Group's survey of the field found text mining on a *short* list, and the text being mined was analysts' reports: other people's reading. The four years since have moved the frontier from mining what analysts wrote about documents to reading the documents themselves: credit agreements, indentures, dockets, and transcripts. That shift matters for this book's reader. A model that summarizes sell-side research inherits the research's lags and biases. A model that reads the credit agreement inherits only its own errors, which can be measured. The modern desk departs from the 2022 picture in a second way as well: the text-derived feature is no longer an exotic alt-data column. It is the first stage of the covenant pipeline, and its error rates belong in the same model inventory as the PD model's.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.42:* "Quant credit is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention, but further data capture and analysis around restructurings and recovery may make this possible."
>
> **Annotation.** This is the most consequential sentence on the shelf for this chapter. "High-touch" in distressed means *reading-intensive*: the touch is a person reading an intercreditor agreement, a cooperation agreement, a disclosure statement, or a first-day declaration. The reading machine is precisely the "further data capture" Man anticipated. It does not make distressed investing systematic, because the judgment is still the scarce input. It does make the *state vector* systematic: the Priming Risk Score of Chapter 13 needs basket capacities, blocker flags, and lender-group composition for hundreds of issuers each quarter, which nobody could read by hand at that breadth and which a reader under contract can. The ex-RSSG specifier is the person who knows which clauses belong in the vector.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.155:* "How do you tell whether a new piece of data is useful? All data vendors promise great value added (always in hindsight)."
>
> **Annotation.** Replace "data vendors" with "AI vendors" and the sentence needs no other edit. A vendor's accuracy figure is computed on a question set the vendor chose, often refined while the product was built, and graded by a rubric the vendor wrote: in-sample three times over. The desk's answer is the one Paleologo gives for alt data: your own holdout, from your own documents, with dates after the product's last update, scored by your own deterministic checks. §26.4 turns that into a contract, and the code in §26.12 makes it a function.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.747:* "In 2018, for example, we applied natural language processing to examine whether sentiment extracted from earnings call transcripts is predictive of subsequent returns of stocks and corporate bonds."
>
> **Annotation.** NLP on the credit desk predates ChatGPT by four years, and the Barclays design is worth copying for a better reason than seniority. The same page argues that running the signal on both stocks and bonds gives an out-of-sample validation that more issuers, more geographies, or more years cannot, because those robustness dimensions are correlated with each other. For an LLM-derived feature, the analogous design is a *second document type*: a covenant reader validated on credit agreements should be re-scored on indentures, where the vocabulary overlaps and the drafting conventions differ. If accuracy collapses, the reader learned the drafting firm's templates, not the covenant.

## 26.4 Document QA With Provenance: The Citation Contract

Moyer, writing for analysts who are not lawyers, gives the instruction that makes document QA work and document summarization fail:

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.303:* "It is very difficult to simply read an indenture. Instead, one must have a question in mind to be answered and then seek the answer in the document."
>
> **Annotation.** "Summarize the restricted payments covenant" is not a question. It is an invitation to produce a plausible covenant summary, and the model did exactly that, roman numerals included. "What is the fixed-dollar component of the general RP basket, in which clause, as amended through Amendment No. 2?" is a question. It has a determinate answer, a location, and a date, so it can be checked. The modern desk departs from Moyer only in scale: he imagined one analyst asking one question of one indenture, and the reader asks four hundred questions of six hundred agreements every quarter. That scale is exactly why each answer must carry its own proof.

### The claim tuple

A claim is a tuple

$$
c = (\text{text},\ d,\ \pi,\ [a, b),\ \hat p),
$$

where *text* is the asserted sentence or typed value, $d$ is a document id in the store, $\pi$ is a 1-based PDF page index, $[a,b)$ are character offsets into the *canonical normalized text* of page $\pi$ of $d$, and $\hat p \in [0,1]$ is the reader's stated confidence. Define three indicators per claim:

- $A(c) = 1$ if the assertion is correct (against a labelled answer);
- $V(c) = 1$ if the pointer *resolves*: $d$ exists in the store, page $\pi$ exists, and $0 \le a < b \le \text{len}(\text{page})$;
- $S(c) = 1$ if the span $d[\pi][a{:}b]$ *supports* the assertion under a fixed, versioned support test.

By construction $S = 1 \Rightarrow V = 1$, since an unresolvable pointer cannot support anything. Over $N$ labelled claims, report all four rates:

$$
\text{acc} = \frac{1}{N}\sum_{i=1}^N A_i, \qquad
\text{valid} = \frac{1}{N}\sum_{i=1}^N V_i, \qquad
\text{support} = \frac{1}{N}\sum_{i=1}^N S_i, \qquad
\text{FH} = \frac{1}{N}\sum_{i=1}^N V_i\,(1 - S_i).
$$

The last one, **FH**, is the *footnoted hallucination* rate: a real page that does not say what the claim says it says. It is the dangerous one because it survives every cheap check. A human spot-checker clicks the link, sees a real clause in the right neighborhood, and moves on. §6.08(b)(xiv) was a $V = 0$ error, embarrassing and easy to catch. A citation to the real §6.08(b)(xii) for a claim that (xii) does not make is a $V = 1, S = 0$ error, and it can go all the way to the investment committee.

The joint distribution of $(A, V, S)$ sorts every claim into one of four cells, and each cell has a credit-specific name:

| $V$ | $S$ | $A$ | Name | Credit-desk example | Who catches it |
| :-: | :-: | :-: | :-- | :-- | :-- |
| 0 | 0 | any | **Fabricated pointer** | §6.08(b)(xiv) | Code (pointer resolution) |
| 1 | 0 | any | **Footnoted hallucination** | Cites the real general basket for a builder-basket claim | Code (support test), if the test is good |
| 1 | 1 | 0 | **Stale support** | Quotes the original basket that Amendment No. 2 replaced | Point-in-time store ("as amended through") |
| 1 | 1 | 1 | **Good claim** | The right number, the right span, the right date | Nobody needs to |

The third row is the RSSG reader's private joke. A span can be real, can say exactly what the claim says, and can still be wrong, because a credit agreement is a living document and the span was amended out in 2024. Charlotin's legal database calls this category "outdated advice," and a credit desk meets it every quarter. The fix is in the store, not in the model: the canonical text of $d$ must be the conformed copy *as amended through a stated date*, and every claim carries that date.

**Edge cases ROBO must be told about.** (i) Offsets computed on a different text normalization than the store's: PDF extraction splits hyphenated words across lines, turns "efficiently" into "eﬃciently" with a ligature, and moves footnotes. Compute offsets on the stored normalized text and nowhere else. (ii) Page numbering: the PDF index and the printed folio differ, often by the length of the table of contents. Use the PDF index, 1-based, always (this book does the same with its own citations). (iii) The support test itself: if it is an LLM, its biases are now inside the metric. Version it, benchmark it on a hand-labelled set, and report its own error rate next to FH. (iv) A claim with no citation is a *failed* claim, not a neutral one. Treat $V = 0$.

### What the evidence says about document QA in finance

The published benchmarks agree on the shape of the problem, if not the level. FinanceBench (Islam et al., 2023) built 10,231 questions over public filings, and on a 150-case sample GPT-4-Turbo with retrieval answered incorrectly or refused 81% of the time. By August 2026 a self-improving three-agent RAG system reports 86% oracle-guided accuracy on the same benchmark (arXiv:2608.26706), along with a 36.4% "Lazarus rate," the share of initially wrong answers recovered on retry, which §26.6 will treat with suspicion. KG-MuLQA (Tatarinov et al., 2025) is the closest public yardstick to this book's use case: 20,139 question–answer pairs over *credit agreements*, 16 models evaluated. The models fail on set operations and multi-hop reasoning across long contexts. That is the structure of every real basket question: "the greater of \$X and Y% of Consolidated EBITDA, *less* amounts used under clause (b)(iii), *plus* the Available Amount, as of the last test date." And VeriFin (2026) shows how far a deterministic check can carry you. By verifying LLM financial claims symbolically against XBRL facts, it accepted *zero* incorrect claims on a 600-question benchmark where baseline pipelines accepted between 6 and 92. The lesson for the desk is the Loop Rule from the other side: wherever a claim can be checked against a structured fact, check it in code, and the false-acceptance rate drops to the error rate of the structured data.

### Calibration and selective prediction

The stated confidence $\hat p$ is useful only if it means something. Two properties matter, and they are Bohn and Stein's power/calibration split exactly.

**Calibration.** Partition claims into $B$ bins by $\hat p$, with $n_b$ claims in bin $b$, empirical accuracy $\text{acc}_b$, and mean stated confidence $\bar{\hat p}_b$. The expected calibration error is

$$
\text{ECE} = \sum_{b=1}^{B} \frac{n_b}{N}\,\big\lvert \text{acc}_b - \bar{\hat p}_b \big\rvert .
$$

A reader that says "90%" and is right 70% of the time has a large ECE even if it ranks claims perfectly.

**Power, via selective prediction.** Let the reader answer only claims with $\hat p \ge \theta$ and abstain on the rest. The *coverage* is $\phi(\theta) = \frac1N\sum_i \mathbf{1}\{\hat p_i \ge \theta\}$, and the *selective risk* is the error rate on the answered set,

$$
R(\theta) = \frac{\sum_{i} \mathbf{1}\{\hat p_i \ge \theta\}\,(1 - A_i)}{\sum_{i} \mathbf{1}\{\hat p_i \ge \theta\}} .
$$

Tracing $\theta$ from 1 down to 0 traces the risk–coverage curve from (0 coverage, undefined risk) to (full coverage, unconditional error rate). A reader with power has a curve that rises slowly: abstaining on its least-confident claims removes a disproportionate share of its errors. The area under the curve (AURC) summarizes it; lower is better. A reader with no power has a flat curve: confidence is uncorrelated with correctness, and abstention removes errors only in proportion to coverage. The two properties are independent. Calibration can be repaired after the fact by a monotone remap of $\hat p$ (temperature or Platt scaling); power cannot be repaired after the fact at all.

> **Ways This Blows Up.** Post-hoc calibration fitted on the same questions used to choose the prompt is in-sample twice: once for the prompt and once for the calibrator. It produces a beautiful reliability diagram and an ECE that doubles on the first new quarter's filings. Hold out documents by *date*, filed after both the prompt freeze and the model's training cutoff, and by *issuer*, as in Chapter 7's grouped CV. The reader has almost certainly seen the old filings during training. It has not seen the new ones.

## 26.5 Hallucination Is an Incentive Problem: Abstention, Controls, and the Cases Curve

Kalai, Nachum, Vempala, and Zhang (2025), *Why Language Models Hallucinate*, make an argument every market maker will recognize: models guess because the scoring rule pays them to. Most benchmarks grade 0/1, with no credit for "I don't know." Let $p$ be the model's probability that its best candidate answer is right. Then

$$
\mathbb{E}[\text{score} \mid \text{answer}] = p, \qquad \mathbb{E}[\text{score} \mid \text{abstain}] = 0,
$$

so the score-maximizing policy answers whenever $p > 0$. A model tuned to such leaderboards learns to bluff, which is exactly what a 0/1-scored poker tournament with no folding would teach a person. Kalai et al. propose stating a confidence target $t$ in the instructions: a correct answer scores $+1$, "I don't know" scores $0$, and a wrong answer scores $-t/(1-t)$. Answering is then worth $p - (1-p)\,t/(1-t)$, which is positive if and only if $p > t$.

**The desk's version uses costs instead of points.** A wrong claim that ships costs $C_{\text{FP}}$: a mis-sized position, a bad hedge, a compliance incident. An abstention costs $C_{\text{abs}}$: a human reads the page. A correct claim costs nothing. Answering beats abstaining when

$$
(1-p)\,C_{\text{FP}} < C_{\text{abs}}
\quad\Longleftrightarrow\quad
p > p^\ast = 1 - \frac{C_{\text{abs}}}{C_{\text{FP}}} .
$$

This is Kalai's rule with $t/(1-t) = (C_{\text{FP}} - C_{\text{abs}})/C_{\text{abs}}$, so that $t = p^\ast$. If a wrong basket number costs twenty times an analyst's fifteen minutes, $p^\ast = 0.95$. If it costs five times, $p^\ast = 0.80$. Boundary conditions: $C_{\text{FP}} \le C_{\text{abs}}$ gives $p^\ast \le 0$, so always answer (the claim is so cheap to get wrong that checking it costs more); $C_{\text{abs}} \to 0$ gives $p^\ast \to 1$, so never trust the machine when checking is free.

Three things go wrong in practice. First, $p$ is not observable; only $\hat p$ is, so the threshold applies to a *calibrated* $\hat p$ (§26.4), and verbalized confidence from a chat model is often not calibrated. Second, the model's incentives are not the desk's. The desk's threshold must be imposed by the harness, which drops sub-threshold claims in code, and not requested in the prompt, where it is a suggestion. Third, the threshold is a *policy parameter* and belongs in the model inventory with its cost assumptions written down.

ROBO illustrates both ways to get this wrong. Told to "maximize accuracy on the eval," it answered every question, including the ones it could not know, because abstaining scored zero. Told instead to "never hallucinate," it abstained on everything and reported a hallucination rate of 0.0% at a coverage of 0.0%. Both outputs were correct responses to the scoring rule, and both were useless. The risk–coverage curve is the honest report, because it shows the whole trade-off and not one point on it.

### Why published hallucination rates are not comparable

General chatbots hallucinated on 58% (GPT-4) to 88% (Llama 2) of verifiable questions about federal cases (Dahl, Magesh, Suzgun, and Ho, *J. Legal Analysis* 2024). Retrieval-based commercial legal research tools hallucinated on 17% to 33% of queries in a preregistered audit (Magesh et al., 2024). On short-document summarization, Vectara's HHEM leaderboard (updated October 16, 2026) ranges from 1.8% to 13.6% across the models it lists. Several frontier models score *worse* than smaller ones on that leaderboard, because summarization faithfulness rewards terse copying and penalizes the elaboration that bigger models like to add. The three numbers measure different tasks, different graders, and different definitions. None of them predicts your reader's FH rate on your agreements.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.397:* "What is interesting in this context is not the absolute level of the performance statistics, but their levels relative to the benchmark."
>
> **Annotation.** Bohn and Stein are explaining why an accuracy ratio means nothing until a benchmark model has been scored on the same sample: an easy sample flatters every model and a hard one punishes every model. Hallucination leaderboards are the purest example of the problem. The desk's practice follows directly. Fix a labelled document set; score the production reader, a cheaper reader, and a deterministic baseline (regex plus the definition graph from Chapter 25) on the same claims; and report the differences. The champion/challenger language on the same page carries over unchanged: a new model version is a challenger until it beats the champion on the desk's own holdout.

### Controls, in order of leverage

1. **Retrieval with provenance.** The reader answers from retrieved spans, and every claim carries the tuple of §26.4. This turns invisible errors into checkable ones.
2. **Deterministic post-checks.** Pointers are resolved in code. Arithmetic is redone in code. Section numbers are checked against the document's own index, and numbers against XBRL or the security master. This is where VeriFin's zero comes from.
3. **Abstention at a paid threshold,** enforced by the harness, with the abstained claims routed to a human queue sized for them.
4. **Cross-model agreement.** Two readers from different model families answer independently, and disagreement routes to a human. This is the LLM version of Bolder's prescription, below.
5. **LLM-as-judge, with its biases priced in.** Zheng et al. (2023) find that strong judges agree with humans over 80% of the time, about the rate at which humans agree with each other. The same paper documents position bias, verbosity bias, and self-enhancement bias: a judge prefers the first answer, the longer answer, and answers from its own family. A judge from the generator's family shares the generator's blind spots, which shows up as low detection power exactly on the cases that matter (§26.6).

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.11:* "The punchline is that, in real-life settings, we literally never know the right model. Moreover, we do know that our model is likely to be flawed, often in important ways."
>
> **Annotation.** Bolder's remedy, in the next sentence on the page, is to examine many models with differing assumptions and structures. For readers, "differing structure" has a precise meaning: different model families, different retrieval pipelines, and at least one deterministic baseline. Two prompts on the same model are not two models; their errors are highly correlated, and their agreement says little. The desk metric is the *disagreement rate* on production claims, tracked daily. A jump in disagreement after a vendor update is the cheapest model-change alarm there is.

> **Trend Watch.** *The hallucination-cases curve, 2023–2026: the first honest error time series the legal profession ever kept.*
>
> - **Jun 2023.** *Mata v. Avianca, Inc.*, No. 1:22-cv-01461 (S.D.N.Y.): counsel file a brief citing cases generated by ChatGPT that do not exist, and the court sanctions them. This is the case that made "hallucination" a legal term of art.
> - **Jan 30, 2024.** *Park v. Kim* (2d Cir.): a federal appellate court refers counsel for discipline over an AI-generated citation to a non-existent case.
> - **Oct 16, 2026.** Damien Charlotin's AI Hallucination Cases database lists **2,199** court decisions involving hallucinated content: 1,501 in the US, 232 in Canada, 112 in Australia, and 76 in the UK. By party: 1,266 pro se litigants, **871 lawyers**, 32 judges, 16 experts. By nature (categories overlap): fabricated 1,803, **misrepresented 931**, false quotes 586, outdated advice 36.
>
> *What it means for the desk.* Two numbers carry the lesson. First, 871 decisions involve professionals with malpractice insurance, ethical duties, and every incentive to check. The failure is not ignorance; it is a process with no verification step. Second, "misrepresented" (931) is the courtroom name for the footnoted hallucination: real authority, cited for something it does not say. A covenant summary that cites the real §6.08(b)(xii) for a claim (xii) does not make is the same error, and the desk metric for it is FH $= \frac1N\sum V(1-S)$. *(Sources: Charlotin database, fetched Oct 17, 2026; CourtListener docket and opinion pages; URLs in §26.14.)*

Mags, reading the Trend Watch over Theo's shoulder, said her line ("back in my day the associate who made up a case got fired by phone; now the machine does it two thousand times and gets a database") and then, a beat later, gave the grudging respect that always follows. "Mind you, nobody ever kept a database of the associates."
