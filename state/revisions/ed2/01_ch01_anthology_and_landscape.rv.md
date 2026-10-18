# RV weave log: Ch 1, The Anthology of the Desk & The Modern Quant Credit Landscape (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry (`state/rv_thread.md` §(e)): box; PB-01 (foreshadow); tool = the flow graph of forced sellers; H: the pod chooses hands at the market maker's table; I: it takes the hand the market maker must offer; L: it needs a short that exists (Law 1); event = Halvorsen lender call, Fri 9 Oct 2026 (fictional, canon); home Ch 8-D §D.1 (in print: §8D.1); figure = flow graph gains the pod node. Preconditions checked: thread COMPLETE; no prior .rv log; `01_ch01_anthology_and_landscape.log.md` ends COMPLETE (no lock).*

*Found on arrival:* a `> **The Pair.**` box for PB-01 already sat at the end of §1.8.2 (after "Mags packed the run sheets", line 662), committed in an autosnap with no .rv log; the ledger recorded it as "written 2026-10-18". It named the two edges and the recall but gave no sizes, no ratio, no use of (1.7), no carry or funding line, and no pointer to the canonical home. Rewritten in place rather than adding a second box.

## What was written, and where

- **§1.8.2, `> **The Pair.**` box at line 662, rewritten in place** (≈370 → 597 words). Lead-in paragraph at line 660 ("A seat that can be short reads the same graph differently...") kept unchanged.
  - **Label:** italic, once, at the top: pod and Vantress Capital Management as fictional composites (Vantress named in Ch 1 for the first time), Kestrel and Halvorsen as fictional issuers, positions, fees and P&L illustrative; Ch 1-B opens the entry with its numbers.
  - **Legs, real short leg named:** long \$60mm Kestrel 6% 2030 from dealers; short \$39mm Halvorsen Packaging 7.25% 2029, the bond itself, borrowed from an asset manager via the platform's prime broker against cash collateral, recallable on demand. In (1.6) the pod is the one node with two edges of opposite sign.
  - **Hedge construction / what it removes:** 0.65 by face, market-value DTS at inception (the sum left to 1-B, one telling). A segment-wide trigger (a redemption wave) dents single-Bs roughly in proportion to DTS, so the pair is flat to it; the market-wide reversal is left to the absorbers built for it (the systematic fund of §1.6; the Fed in April 2020). The 2:58 RFQ was all-to-all and the pod was not obliged to answer: the "chooser of hands" of §1.1's seat.
  - **What idio remains (the chapter's tool doing new work):** (1.7) splits the x-ray's single idio number on Halvorsen's fall to 78 into the permanent part (the $\pi J$ of (1.2), the thesis) and a temporary forced-seller dent: \$390,000 per point on the \$39mm short, half returned to absorbers within about 14 days at the chapter's $\theta = 1/20$, unless the pod covers part of the short into the forced flow and so becomes the absorber. The dealer fears the informed seller; the short pod is on that seller's side and covers only into the forced one: "the hand the market maker must offer and the pod may take."
  - **What leaks:** the short has to exist. The lender as a node with its own trigger (a vote); a recall as a trigger with $f = 1$ and a one-settlement-cycle window that runs the short edge backwards into a forced buyer; tied to Ch 8-D canon, the 9:40 a.m. recall of \$20mm of the pod's GM Financial short that same Friday (§8D.7). Law 1 closes the paragraph.
  - **Costs:** carry, funding and borrow named without re-doing 1-B's dollar sums: April carry roughly flat, 6% earned paying for 7.25% owed to the lender on the smaller face, financing of the long net of the rebate on the cash collateral, and a 50 bp fee on the short's market value; $c(\Delta q)$ paid twice, once per leg. Ines's §1.3.2 question, *whose five days?*, answered for the short leg: the lender's, at a fee that resets overnight (Chapter 1-B).
  - **Cross-reference to the canonical home (one):** "Where a pair like this begins, as a thesis sentence with a date in it, is §8D.1." Pointers to §8D.7 (the recall) and Chapter 1-B (sums, reset) are citations, not re-derivations.
- **Figure placeholder, line 650** (`ch01_forced_seller_flow_graph.png`, not yet drawn): the existing FIGURE comment now also asks for the pod node, PB-01, labeled illustrative: long edge (Kestrel) from the dealer residual, short edge (Halvorsen) from a lender node, dashed recall edge back to the lender ($f = 1$, one settlement cycle). No new figure file, no new embed.

## Retired (one telling per fact)

- From the old box: "the part of a forced-seller reversal that the Fed paid for in April 2020" (now told as the reversal left to the absorbers built for it); "Kestrel's documents against Halvorsen's" (now the permanent $\pi J$ part); "Chapter 8-D follows the pair to its exit" (replaced by the §8D.1 pointer).
- From the first draft of the new box: the exchange-premium gap sentence (cut for length; 1-B tells the ten-point gap and Ch 14 owns T8); "§1.4's ruler" (cut for length).
- Nothing else removed. All topics, numbered equations, Source Extractions, Trend Watches, exercises, figures and figure comments, Appendix F links and URLs untouched. No code blocks added. The chapter's last line is still `<!-- STATUS: COMPLETE -->`.

## Ledger and cast

- `state/rv_pair_book.md`, row PB-01, targeted in-row replacement (other writers active in the file; 13 columns re-verified): the "foreshadowed in Ch 1 §1.8.2" parenthetical now records the rewrite (two-edge node, DTS 0.65 by face, (1.7) permanent/temporary split, \$390k per point, ~14-day half-life, recall as an $f = 1$ trigger, flat April carry, cross-ref §8D.1, figure placeholder). "What leaked" gains a Ch 1 entry: the temporary forced-seller dent inside the idio line returns to absorbers unless the pod covers into the forced flow; the recall runs the short edge backwards. Status unchanged (stressed in Ch 5, 11, 27; opened in 1-B).
- `state/cast_bible.md`, Dov Adler line under Ch 1: the box now names Vantress and cites the §8D.7 recall; no dialogue, no new facts about Dov.

## Flags for other owners (not changed here)

- **Lender-call time:** Ch 1's cold open has the Halvorsen lender call ending at 2:00 p.m. on Fri 9 Oct 2026 (8-K at 4:40); Ch 8-D §8D.7 and the cast bible's Ch 8-D story dates say "At 3:00 that afternoon Halvorsen held its lender call." The box quotes neither time. Ch 8-D should move to "had held" / 2:00.
- **Halvorsen's Friday prices (C9, already open):** Ch 1 prints 91.25 at 2:58 and opens Monday at 78; Ch 1-B has the bonds going 83 → 78 on Friday afternoon and Friday's idio at +\$2.34mm. The box says only "the fall to 78" and prices the dent per point, so it inherits neither version.
- **Halvorsen name:** Ch 1-B line 5 still calls the issuer "Halvorsen Building Products" (canon C9: Halvorsen Packaging Holdings). The box uses "Halvorsen Packaging".
- **Exercise:** the thread asks App Z for one pair exercise per chapter with a beat; none added to Ch 1 (out of this step's scope). A natural one: the per-point dent value and the share returned by day $T$ at a given $\theta$.

<!-- STATUS: COMPLETE -->
