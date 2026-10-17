# Style Bible (v0, Edition 1)

Every writer reads this before writing a word. It keeps 28 independently written chapters sounding like one brilliant, funny author with one notation. The Fable Showrunner may enrich it in later editions, but **the cast, gags, and notation below are canon and must not be renamed.**

## 1. The Voice

Think of Matt Levine's deadpan explaining stochastic calculus at 1 a.m. on a closing night, to a restructuring banker who is very smart, very tired, and slightly annoyed at being taught. The reader is an ex-PJT RSSG banker moving to a systematic desk. They know credit agreements cold and have never been made to price adverse selection in three seconds.

- **Rigor is the product; humor is the delivery mechanism.** Every joke rides on a correct idea. A joke that teaches ("a CCC bond is an equity option that wears a tie to work") beats three hedged sentences.
- **Concrete over abstract.** Say "an RFQ for \$15mm of a B3 bond at 2:58 p.m. on the Friday before a lender call," not "a large trade."
- **Talk to the reader as a peer.** Never condescend. Mock institutions, incentives, conventions, and ourselves. Never mock the reader, protected groups, or real named individuals.
- **No fake quotes.** Real people and firms appear only with verifiable facts. All dialogue belongs to the fictional cast.
- **Joke density:** high in chapter openers and boxes; roughly one good line per 500 words in technical sections; none inside the load-bearing step of a derivation (put the joke after the step).

Calibration, good:

> Itô's lemma is the tax code of stochastic calculus. You thought you could just take a derivative, but the IRS of randomness shows up with a $\tfrac12\sigma^2$ correction, and it is not optional. Here is where the tax comes from: $(dW_t)^2 = dt$, so the second-order Taylor term that ordinary calculus throws away is now first-order...

Calibration, bad: "Obviously, as any competent quant knows..." (snark at the reader); "As Ken Griffin once said..." (fabricated quote); a pun stuffed into the middle of the HJB ansatz.

## 2. The Cast (fictional; pronouns are canon)

| Character | Who | Quirks & catchphrase | Where they appear |
| :--- | :--- | :--- | :--- |
| **Theo Marsh** (he/him) | Ex-PJT RSSG vice president, three weeks into a systematic credit desk. The reader's stand-in. | Carries his old 13-week cash flow model on a USB stick "for emotional support." Asks, "But what does the credit agreement say?" Usually right. | Cold opens, Desk Debriefs, learning moments |
| **Ines Okafor** (she/her) | Head of credit market making, ex-professional poker player, Theo's mentor. | Frames everything as a hand: "What's the pot, what are the odds, and who at this table knows more than you?" Calls markouts "the hand history." | Microstructure, adverse selection, sizing, Poker Table boxes |
| **Dr. Kasimir "Kaz" Lind** (they/them) | Quant PhD in stochastic analysis, the desk's model builder. | Brilliant; has never read a credit agreement. Once asked whether "sacred rights" required a priest. Says "Let's just assume Gaussian," then regrets it. | Derivations, model failures, Ways This Blows Up |
| **Marguerite "Mags" Dunleavy** (she/her) | Distressed PM since the 1990s; remembers pricing bonds "by phone and by grudge." | "Price is what you pay. Recovery is what you get, eventually, after the lawyers." Deeply suspicious of anything called "adjusted." | Distressed, LMTs, post-reorg, war stories |
| **ROBO** (it/its) | The AI coding agent Theo specifies work to. | Implements exactly what was asked. "Minimize drawdown" makes it hold cash forever. It never complains and never guesses. | Every "Spec You Hand the Robot" box |
| **The Ad Hoc Group** | A Greek chorus of lenders, always "represented by counsel." | Speaks in unison, mostly in Rule 2019 statements. Forms, splits, signs cooperation agreements. | Docket Diaries, LMT chapters |

## 3. Running Gags (build them across chapters)

1. **The 13-week model that refuses to die.** Theo's cash flow model shows up in every part, each time reborn as something more rigorous: a survival curve (Ch 5–6), a state-space feature (Ch 3, 25), a liquidity runway variable in the Priming Risk Score (Ch 13), and finally the PM dashboard (Ch 28).
2. **ROBO literalism.** Each spec box can include a one-line "what ROBO built from the vague version" before the precise spec. Funny and pedagogical: it shows why specs need units, boundary conditions, and edge cases.
3. **The cooperation-agreement counter.** Whenever a cooperation agreement is signed in a chapter, increment the joke: "(Cooperation agreements signed in this book so far: N.)" Use it sparingly, mostly in Part IV.
4. **"Open market purchase."** The most expensive three words in finance. Recurs in LMT, CDS, and NLP chapters.
5. **Kaz vs. legal vocabulary.** Kaz misreads one legal term per appearance: "sacred rights," "springing lien," "blocker," "fulcrum."
6. **Ines's hand histories.** Every adverse-selection lesson ends with the hand replayed through markouts.
7. **Mags's "back in my day."** Each new technology is met with a war story about how it used to be worse, followed by grudging respect.
8. **"IDO or it didn't happen."** The desk motto: until you strip carry, rates, and factor beta, it isn't alpha.

## 4. Box Types (exact Markdown)

Use blockquotes with a bold label. They render in Pandoc and on GitHub.

```text
> **Desk Myth vs. Desk Reality.** *Myth:* ... *Reality:* ...

> **Poker Table.** (game-theory intuition, usually Ines)

> **Docket Diary.** (bankruptcy/court process facts with dates; the Ad Hoc Group may comment)

> **Ways This Blows Up.** (numerical instability, model failure, operational risk)

> **Trend Watch.** (a dated, sourced market-structure or strategy trend: what changed, when, how big, and what it means for the desk)

> **[SOURCE EXTRACTION]** *Book_id p.N:* "short exact quotation, at most ~80 words"
>
> **Annotation.** Our analysis: why it matters on a 2026 desk, where the modern desk departs from it.
```

The mandatory code section is a heading, not a box: `### Specification for AI Implementation`. It may open with a **The Spec You Hand the Robot** paragraph before the full schema and code.

## 5. Notation (canonical for the whole book)

| Concept | Symbol | Notes |
| :--- | :--- | :--- |
| Physical / risk-neutral measure | $\mathbb{P}$ / $\mathbb{Q}$ | Always say which one an expectation uses. |
| Filtration (information at $t$) | $\mathcal{F}_t$ | |
| Firm asset value | $V_t$ | |
| Debt face value (structural models) | $F$ | Never $D$ (that letter is duration). |
| Equity value | $E_t$ | |
| Asset / equity volatility | $\sigma_V$, $\sigma_E$ | Annualized, decimal. |
| Short rate / risk-free rate | $r_t$ / $r$ | Continuously compounded unless stated. |
| Default time | $\tau$ | |
| Default intensity (hazard rate) | $\lambda_t$ | Reserved for default. Never use $\lambda$ for order arrival. |
| Survival probability | $S(t) = \mathbb{Q}(\tau > t)$ | Use $S^{\mathbb{P}}$ for physical. |
| Recovery rate / loss given default | $R$, $L = 1 - R$ | Fraction of par unless stated (RMV, RFV, RT conventions named explicitly). |
| Credit spread | $s$ | Decimal in formulas, bp in prose and tables. Always state units. |
| Option-adjusted spread / Z-spread | $\text{OAS}$, $Z$ | |
| Modified duration / spread duration / empirical duration | $D^{\text{mod}}$, $D^{\text{spr}}$, $D^{\text{emp}}$ | |
| Duration Times Spread | $\text{DTS}_i = D^{\text{spr}}_i \cdot s_i$ | |
| Yield / Treasury yield | $y$, $y^{\text{TSY}}$ | |
| Price | $P$ (bond), $S_t$ (generic mid/underlying) | In market making, $S_t$ is the mid. |
| Inventory / risk aversion | $q$ / $\gamma$ | |
| Order-arrival intensity | $\Lambda(\delta) = A e^{-k\delta}$ | $A$, $k$ are arrival parameters; $\delta$ is the quote distance from mid. |
| Reservation price | $r^{\text{res}}$ | Not $r$, which is the interest rate. |
| Brownian motion / Poisson process | $W_t$ / $N_t$ | |
| Factor returns / loadings / idiosyncratic return | $F_{k,t}$ / $\beta_{i,k}$ / $\epsilon_{i,t}$ | |
| Idiosyncratic alpha | IDO | |
| Priming Risk Score | $\text{PRS} \in [0,1]$ | |
| Enterprise value (restructuring) | $\text{EV}$ | Expected value is $\mathbb{E}[\cdot]$, never "EV". |
| Information coefficient / ratio, breadth | IC, IR, BR | |
| Time | $t$ in years | State the day count (ACT/360 for CDS premium, 30/360 for US corporates) when it matters. |

Resolve any new collision by adding a superscript or subscript, and add a sentence saying so.

## 6. Formatting Conventions

- Headings: `# Chapter N: Title`, `## N.M Section Title`, `### Subsection`. Part openers are `# Part X: Title`.
- Math is Pandoc LaTeX: `$...$` inline (no space after the opening `$` or before the closing one), and `$$...$$` display math on its own lines. Escape currency outside math as `\$15mm`. Use `\tag{N.M}` sparingly.
- Code fences always carry a language. ```` ```python ```` blocks in one chapter run in order in one interpreter, so define before you use. Sketches go in ```` ```cpp ````, ```` ```rust ````, ```` ```text ````, or a python block whose first line is `# sketch`.
- Never put `---` on a line directly followed by text; leave a blank line after it.
- Cite sources as `Book_id p.N` (the PDF page from `tools/pdf_search.py`). Cite papers as Author (Year), *Title*.
- Mark numbers as *(illustrative)* or *(approx.; source: ...)* when they are not from a cited source.
- Cross-reference with "see §13.4" or "Chapter 18".
- Close every major section, or at minimum the chapter, with `### Deep-Dive Resource Graph`, grouped into **Podcasts**, **Practitioner Writing**, **Academic Papers**, and **Data & Code**. Include URLs only if verified this session or they are canonical roots; otherwise give the title and author without a link.

## 7. Chapter Formula

**Open:** a cold-open desk scene of at most 400 words with the cast, ending on the question the chapter answers. Follow it with a short paragraph: "By the end of this chapter you will be able to..."

**Body:** numbered sections, each carrying the six anatomy elements across the chapter: desk framing, derivation, AI spec, source extraction, case study, and resource graph. Include at least one Trend Watch box, with dated and sourced figures, showing how the topic changed over 2018–2026.

**Close:**
1. `## N.X Desk Debrief`: 5–8 bullets with takeaways sharp enough to tape to a monitor.
2. **The Spec You Hand the Robot**: a compact, prompt-ready summary spec for the chapter's main engine.
3. 3–6 exercises, some funny, all real.
