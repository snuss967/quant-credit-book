## Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets

Six exercises: one on a recursive cap, one on a regex, one on a min cut, one on a cosine, one on a vote, and one on a pager. Every number below was recomputed from the chapter's inputs and from Listings 25.1 to 25.9 (Appendix F), run in order in one interpreter. Write your own answer before you read ours; on this chapter the trap is usually the answer that arrives first.

**Z.25.1: The four most expensive words, again**

**Answer:** Measured "after giving effect," a 30% cap lets add-backs reach $c/(1-c) = 0.3/0.7 = 42.9\%$ of pre-add-back EBITDA $\mathcal{E}_0$, against 30% on the "before" reading. The gap is 12.9 points of $\mathcal{E}_0$, which is exactly $c^2/(1-c) = 0.09/0.7$. The "after" reading doubles the "before" reading at $c = 1/2$ (50% becomes 100%). At Halyard's $\mathcal{E}_0 = \$200$mm, the cap goes from \$60mm to \$85.7mm, so the sponsor's whole \$80mm claim now fits under it, and incremental debt capacity goes from \$361mm to \$458mm.

**How:** The add-back counts toward the base that caps it, so the constraint is $A \le c(\mathcal{E}_0 + A)$. Collect $A$ on the left:

$$
A(1-c) \le c\,\mathcal{E}_0 \quad\Longrightarrow\quad A \le \frac{c}{1-c}\,\mathcal{E}_0 .
$$

Subtract the "before" cap $c\,\mathcal{E}_0$ and put it over one denominator: $\frac{c}{1-c} - c = \frac{c - c(1-c)}{1-c} = \frac{c^2}{1-c}$. For doubling, set $\frac{c}{1-c} = 2c$; divide by $c > 0$ to get $1 - c = \tfrac12$. Notice that the ratio of the two readings is $1/(1-c)$, so it climbs steeply: 1.33 at 25%, 1.43 at 30%, 2 at 50%. The iteration $A_{k+1} = \min\big(80,\ 0.3(200 + A_k)\big)$ in `addback_fixed_point` (Listing 25.2) agrees: it stops at the \$80mm claim, because the fixed point (85.7) is above it.

**The trap:** Running one round of the loop and stopping: $0.3 \times (1 + 0.3) = 39\%$. That is the cap after the add-back has been fed back once, not after it has settled; the remaining 3.9 points come from feeding the extra back again, and again. The geometric series $c + c^2 + c^3 + \dots = c/(1-c)$ is the same answer written as an iteration. On the doubling question, the slip is to solve $c/(1-c) = 2$ and report $c = 2/3$. That doubles $\mathcal{E}_0$, not the "before" reading.

**If you got this wrong, read:** §25.3.3 (Equation 25.1 and the "Fixed points and contractions" box), then the Full Derivation "the cycle as a contraction"; §25.3.4 for what each added dollar of EBITDA buys in capacity.

**Z.25.2: Break Kaz's regex**

**Answer:** Block 1 (Listing 25.1) passes two of the five tests and fails three.

- *Passes:* "Affiliated Lender". With "Affiliated Lender" and "Lender" both in the dictionary, `find_references("no Affiliated Lender shall vote", …)` returns only `{"Affiliated Lender"}`, because the longer term is matched first and its span is consumed. The plural "Affiliated Lenders" passes too.
- *Passes:* the possessive. "the Restricted Subsidiaries' assets" maps to `{"Restricted Subsidiary"}`, because the plural stem accepts "-ies" and the lookahead `(?![A-Za-z])` lets the apostrophe through.
- *Fails:* the inline definition. `(any such transaction, a "Specified Investment")` never becomes a vertex, because `DEF_RE` only reads lines that begin `"Term" means`.
- *Fails:* the redefinition, in either phrasing. Written as `"Indebtedness" means, for purposes of this Article VII, …`, it silently overwrites the Section 1.01 definition: the dict keeps the last one, with "for purposes of this Article VII" glued onto the body. Written as `For purposes of this Article VII, "Indebtedness" means …`, it is never parsed at all.
- *Fails:* the hyphenation, twice. Inside a definition, the body stops at "Unre-", so the edge is lost. Fed the broken text directly, `find_references("any Unre-\nstricted Subsidiary", TERMS)` returns `{"Subsidiary"}`: an edge to the wrong term, which is the substring night again in a third costume.

Two side findings came out of the tests. First, if "Affiliated Lender" is defined in another document, so that it is missing from the dictionary, "Affiliated Lenders" draws an edge to "Lenders". The fix for that is the dictionary, not the regex. Second, the synthetic agreement defines "Lenders" in the plural, so a singular "each Lender" matches nothing.

**How:** Write each case as an assert on `find_references` or `parse_definitions`, run it against Block 1 unchanged, and see which ones fail. The patch makes four changes, all in Block 1:

1. Join a line-break hyphen only when the next fragment starts in lower case, so "Run-\nRate" keeps its hyphen. Do the join inside `find_references`, so the character offsets into the raw text, which are the citation anchors, do not move.
2. Let `DEF_RE`'s body run (with `re.S`) up to the next line that opens a definition, instead of stopping at the end of the physical line. This also fixes the wrapped-definition weakness that §25.10 flags.
3. Accept an optional scope in either position. Store scoped definitions under (term, scope) in a second dict, and raise if a global term is defined twice instead of letting the later definition win.
4. Add a second regex for parenthetical definitions. Each match becomes a vertex, with the enclosing clause as its body and the opening parenthesis as its anchor.

After the patch all five tests pass, every assert in Listings 25.1 to 25.9 still passes, and the definitions and edge set for the synthetic agreement come out identical to the original's.

**The trap:** The first trap is to expect the matcher tests (Affiliated Lender, the possessive) to fail and to "fix" the matcher. Block 1 was built for exactly those cases. The three failures are in the parser that feeds the matcher: a term that never becomes a vertex can have no edges, and nothing raises an error. The second trap is the tempting patch for the hyphenation case: dropping the word boundary, or matching case-insensitively, so that "stricted Subsidiary" can be caught. That breaks the existing `"any Unrestricted Subsidiary"` assert and replays Paloma's night. The third is to join every "-\n": that turns "Run-Rate Cost Savings" into "RunRate Cost Savings" whenever a line happens to wrap at the hyphen.

**If you got this wrong, read:** §25.2.4, Paloma's 4:10 a.m. diff and the "Ways This Blows Up" box; then the commentary on Listing 25.1 in §25.10 (the paragraph on the one-line body).

**Z.25.3: Move the cut**

**Answer:** $\Phi = \$100$mm, and the min cut is {trapdoor (\$60mm), direct basket (\$40mm)}. The two upstream baskets (\$250mm) carry only \$60mm and have \$190mm of slack. Add a J.Crew blocker, which sets the IP capacity of every arc into the unrestricted subsidiary to zero, and $\Phi^{\text{IP}} = 0$. The cut is the same two arcs, now at zero for IP. Cash is untouched: $\Phi^{\text{cash}}$ is still \$100mm, and so is $\Phi$.

**How:** Extend Listing 25.3. Give `jcrew_arcs` a fourth arc, ("LoanParties", "Unrestricted", "direct basket", 40), set the trapdoor to 60, and call `max_flow_min_cut`. It returns 100.0 and names the trapdoor and the direct basket. By hand, every $s$–$t$ cut has to contain the direct arc, because that arc runs straight from $s$ to $t$. What remains is to cut the $s \to N \to t$ route at its narrowest point, which gives

$$
\Phi = c_{s\to t} + \min\big(c_1 + c_2,\; c_{N\to t}\big) = 40 + \min(250, 60) = 100 .
$$

For IP, rerun with both arcs into $t$ at zero. That returns 0.0 with the same two arcs in the cut. The theorem's sensitivity statement checks out numerically too: raising either cut arc by \$1mm raises $\Phi$ to 101, and raising an upstream basket changes nothing.

**The trap:** In the first part, the usual wrong answers are 290 (treating the trapdoor as uncapped, as in the chapter's original J.Crew case) and 60 (forgetting that the direct basket is a parallel route, so it sits in every cut). In the second part, the expensive mistake is to model the blocker as "shut the trapdoor". That leaves IP flowing through the direct basket, so $\Phi^{\text{IP}} = 40$, not 0. The mirror image is a blocker drafted only against Loan Party investments in unrestricted subsidiaries. That gives $\Phi^{\text{IP}} = 60$ through the trapdoor, which is exactly the route J.Crew used. Finally, do not add $\Phi^{\text{IP}}$ to $\Phi^{\text{cash}}$. The two commodities draw on the same baskets, so each figure is an upper bound on its own commodity, and they never sum.

**If you got this wrong, read:** §25.4.1 (the pipes box and max-flow min-cut), then "Blockers are commodity-specific cuts" in §25.4.2, and the Listing 25.3 commentary in §25.10 on why the listing's blocker is two single-commodity runs.

**Z.25.4: How loud must a covenant shout?**

**Answer:** $1 - \cos(x, x') = k^2/\|x\|^2$, so for a 1% move you need $k^2 = 0.01 \times 2.4 \times 10^6 = 24{,}000$, or $k \approx 154.9$: about **155** occurrences, every one of them amended. One occurrence moves cosine by $4.2 \times 10^{-7}$ (Listing 25.4 prints $4.17 \times 10^{-7}$ with $\|x\|^2 = 2{,}399{,}897$).

**How:** "4.50" appears $k$ times ($x_i = k$), "5.25" never ($x_j = 0$), and the amendment moves all $k$: $x' = x - k\,e_i + k\,e_j$. The dot product loses $k \cdot k$ on coordinate $i$ and gains nothing on $j$. The new length loses $k^2$ on $i$ and gains $k^2$ on $j$:

$$
x \cdot x' = \|x\|^2 - k^2, \qquad \|x'\|^2 = \|x\|^2 - k^2 + k^2 = \|x\|^2,
$$

so $1 - \cos = 1 - (\|x\|^2 - k^2)/\|x\|^2 = k^2/\|x\|^2$. Setting that equal to 0.01 gives $k = \sqrt{24{,}000}$. The 2.4 million comes from $n^2/d + n \approx 2.25 \times 10^6 + 1.5 \times 10^5$: Cauchy–Schwarz's floor plus the multinomial noise. If you plant the $k$ copies into Listing 25.4's vector, they add their own $k^2$ to $\|x\|^2$, so 155 copies give 0.991% and 156 give 1.004%. "About 155" is the right level of precision.

**The trap:** The usual wrong answer is to scale the one-token result linearly: $0.01 / (4.2 \times 10^{-7}) \approx 24{,}000$ occurrences. The drop grows with $k^2$, not $k$, because the edit takes $k$ away from the dot product on a coordinate that is itself $k$ long. The quieter wrong answer is 150, from plugging in the Cauchy–Schwarz bound $n^2/d$ as if it were $\|x\|^2$. That bound is a floor on $\|x\|^2$, so it understates both the length and the $k$ needed. And neither number changes the conclusion: the capacity change is \$200mm whether the ratio appears once or 155 times.

**If you got this wrong, read:** §25.5.1, the shopping-list box and the Full Derivation "one swapped token" (redo it with $k$ in place of 1); then the commentary on Listing 25.4 in §25.10.

**Z.25.5: Is the group a blocker?**

**Answer:** The group's true share is somewhere in $[32.8\%, 33.2\%]$.

- **"Blocks" is robust** for every turnout $\varphi < 98.4\%$, down to the group's own 33% (if the group votes, turnout cannot be below its holding).
- **"Does not block" is robust** for $\varphi \ge 99.6\%$.
- **The ambiguous band** is $98.4\% \le \varphi < 99.6\%$, just 1.2 points of turnout wide.

PACER fees to resolve it: at most \$3 a document, however long the PDF. That is \$3 for the latest statement, or \$6 for both, to see whether the amounts are exact or "approximately". The balloting agent's tabulation declaration, which is where the turnout comes from, is one more document at \$3 or less. If that is all the desk buys this quarter, PACER's waiver of bills of \$30 or less makes the invoice \$0. Less than the coffee indeed.

**How:** The group blocks on amount when $\theta > \varphi/3$. A verdict is robust only if it holds at both ends of the interval. "Blocks" needs the *smallest* share to clear the bar, $0.328 > \varphi/3$, so $\varphi < 0.984$. "Does not block" needs the *largest* share to miss it, $0.332 \le \varphi/3$, so $\varphi \ge 0.996$. Between those two turnouts the answer depends on rounding you cannot see. A grid check against `blocks` in Listing 25.7 reproduces both edges. The ±0.2% comes from four members each good to \$0.5mm on \$1,000mm. If you think rounding applies per *lot* rather than per member, Holder_A's two lots make five roundings, the interval becomes ±0.25%, and the band widens to 98.25%–99.75%. Either way, the band sits near full turnout because 33% is so close to a third.

**The trap:** The first trap is to use the point estimate and report one cutoff, "blocks below 99%, not above". That skips the band, which is the whole point of carrying an interval. The second is to treat "exactly a third" as a block. At $\theta = 33.2\%$ and $\varphi = 99.6\%$ the group holds exactly one third of the vote, and §1126(c) needs more than one third, so it does not block. The third is to get the direction backwards: a fuller room raises the bar, so higher turnout makes blocking harder. On the fees, the slip is to price the PDF by the page (a 40-page statement at \$0.10 a page would be \$4). The \$3 cap applies first.

**If you got this wrong, read:** §25.7.1, the "fuzzy slices" box, the blocking arithmetic and the rounding bound $n\delta/(2F_c)$; then §25.6.1 (Friday: PACER's fees, the cap and the waiver) and Mags's grade in §25.7.3.

**Z.25.6: Spec ROBO into sleeping through the utilities**

**Answer:** Theo's sticky note, as a spec:

1. *Page only for a Rule 2019 statement whose filer discloses a class on the desk's watchlist* (here the first-lien term loan and the 2020 super-priority debt), reading the class from the statement's first page, not from the entry text.
2. *Within those, page on the first statement from a group not yet seen in the case, and on any amended or supplemental statement (ordinal ≥ 1) from a group already on the watchlist.*
3. *Every other Rule 2019 entry (utilities, equity, trade, landlords) goes to the 7 a.m. digest. Never page on `doc_class` alone.*

Key on these fields: `doc_class`; the filer, resolved from `description` to a stable group id; the amendment ordinal, also parsed from `description` ("amended", "second amended", "supplemental"); the disclosed `class` from `r2019_lots`; and the `docket_number` on the watchlist. Run on the seven Serta rows, the spec pages for Docs. 69, 75, 389 and 1116 and sends Docs. 273, 289 and 311 to the digest. Theo sleeps through all three 2 a.m. pages and still gets the second amended priority-lender statement eight days before emergence.

**How:** Ask what makes a statement matter to a term-loan position. The answer is who holds what, and what changed. The class field answers "what". The group id plus the ordinal answers "who" and "what changed". The doc class only says the paper is the right shape. Test the rule against the `type=rd` table in §25.7.3 row by row, including the two rows it must not suppress: the excluded lenders' original (Doc. 75) and the priority group's amendments (Docs. 389 and 1116). Reading the class means opening the PDF, at up to \$3 a statement. That is the same lesson Kaz's card learned: the free docket text says who filed, not what they hold.

**The trap:** Most wrong specs key on the filer's name. A deny-list on "utility" fails the next time the filer is the Ad Hoc Committee of Trade Creditors. An allow-list on "Ad Hoc" still pages at 2:11 for Doc. 289, the Ad Hoc *Equity* Group. Keying on "amended" alone pages at 2:26 for the utilities' supplement (Doc. 311) and stays silent for the day-one original from the excluded lenders (Doc. 75). Quiet hours are not a fix either: they delay the page that matters along with the ones that don't.

**If you got this wrong, read:** §25.7.3, beat three (the 2 a.m. page) and the `type=rd` table; §25.7.1 on endogenous sampling (why an amendment from a known group is the event); and the `docket_entries` and `r2019_lots` schemas in §25.10.

<!-- STATUS: COMPLETE -->
