# RV weave log: Ch 1-B, A Week in Five Quant Shops (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry (`state/rv_thread.md` §(e)): existing box 1B-1, keep it and number it PB-01; tool = the x-ray, the FCM roll, the 2:40 trim; already written: DTS drift, jump, borrow; home Ch 8-D and 8-C; figure = existing Fig 1-B.2. Preconditions checked: thread COMPLETE; no prior .rv log; no .log.md lock for this chapter.*

## What was written, and where

- **§1B.2, the `> **The Pair.**` box after Figure 1-B.2 (line 91), rewritten in place** (494 → about 575 prose words, 600 by `wc` including math tokens). No new box, no new scene, no new figure; the beat stays where the thread puts it, between the diagnosis (7:15 x-ray, DTS Math Gently, Fig 1-B.2) and the day that plays each leak out (9:30 FCM roll, 1:15 lender email, Bea's documents, 2:40 trim, 3:00 Gordon).
  - **Label:** now *Pair Book entry PB-01 (box 1B-1)*, so Ch 5 §5.1.4 and Ch 11 §11.6.2, which cite "box 1B-1", still resolve. Names the platform, Vantress Capital Management, for the first time in the chapter, and labels pod, platform, Kestrel, Halvorsen and every number as fictional or illustrative.
  - **Thesis:** keeps the canon description and adds Dov's dated ledger sentence verbatim from §8D.6 ("Halvorsen needs its lenders before Kestrel does, and the market prices it before the 2027 revolver is due").
  - **Legs, with the real short leg named:** long \$60mm Kestrel 6% 2030 at 96; short \$39mm Halvorsen 7.25% 2029 at 90, ratio 0.65 by face; the short is the bond itself, borrowed from an asset manager through Vantress's prime broker against 102% cash collateral and recallable on demand (mechanics per R11 / §8D.2); Halvorsen's CDS named as the alternative short, short the issuer's deliverables, not these bonds, with a basis (Ch 24).
  - **Hedge construction / what it removes:** market-value DTS at inception (72,600 vs 71,600, unchanged), removing HY spread beta, most of the sector factor, most of rates. New: the x-ray (the chapter's tool) as the factor-model audit of that claim; Friday's explain puts 96 cents of each dollar of gross attribution on the idio line (2.34 / (2.34 + 0.10) = 0.959; the dollar figures themselves stay told once, in the narrative paragraph above).
  - **What idio remains:** the view (documents, maturity walls, sponsor), plus one sentence that idio is "whatever the x-ray's factor list cannot name" (T3 foreshadow, no derivation).
  - **What leaks:** the ruler (70,200 vs 98,000; net short about 40% of a leg, now tied to the orange line as "a market position nobody chose"); the jump (10-point exchange gap, \$3.9mm, half the distance to Dov's line; no DTS ratio hedges it); the borrow (lenders recall to vote).
  - **Costs:** carry, financing net of rebate and borrow fee kept as before (illustrative; arithmetic re-checked: 3.6 − 2.83 − 0.6 − 0.91 ≈ −0.74mm/yr ≈ −\$2,960 per business day). New: a week earlier (Tue 6 Oct, Ch 8-D cold open) the borrow sheet said 50 bp with 61% on loan; the 300 bp reset is set against Asquith, Au, Covert and Pathak (JFE 2013, R11): 173 bp average in the thirty days before a bankruptcy filing; the fee as the only crowding gauge the pod can see (T5, T11 foreshadow).
  - **Cross-reference to the canonical home (one):** "The life of a pair, from the short-leg menu (§8D.2) to the ledger row this box becomes (§8D.6), is Chapter 8-D's"; it replaces the old pointer to "Chapter 8" for the pair's mechanics. Pointers to Ch 24 (CDS alternative) and Ch 8-C (the explain) kept.
  - Phrase changed after the first draft: "is the hedge doing its job" → "is the isolation working", to avoid echoing "the hedge had done its job" two paragraphs earlier.

## Retired (one telling per fact)

- From the box: "it is a bet on the shape of a liability-management transaction, which is not the bet he wrote down in April". Bea and Dov's exchange at Tuesday midday ("We're short a guess about who gets invited" / "That's not the trade" / "a different trade wearing the old trade's name") tells it better.
- From the box: "Halvorsen's next move is unlikely to be a diffusion", cut for length; the Math, Gently on the stop already makes the point that a ten-point gap goes straight through a stop.
- From the box: the generic "the pair's mechanics have a canonical home in Chapter 8", replaced by the 8-D pointer.
- Nothing else removed. All topics, equations, exercises, figures (1-B.1, 1-B.2 and the rest), Source Extractions, Trend Watches, Appendix F links and URLs are untouched. No code blocks were added. The last line of the chapter is still `<!-- STATUS: COMPLETE -->`.

## Ledger

- `state/rv_pair_book.md`, row PB-01, updated by targeted in-row replacement (other writers were editing the file at the same time; columns re-verified at 15 fields). Opened-in cell now records the 1-B rewrite. Status: "stressed (Ch 5, 11, 27); opened in Ch 1-B, numbered PB-01 there (box 1B-1)". Ratio: 0.65 by face (0.58 after the 2:40 trim, plus CDX HY). Idio share: 0.96 of gross attribution on Fri 9 Oct (one day), 0.71 of September variance (§8D.6). Capture: 0.41 (Sept., §8D.6). What leaked: added the Ch 1-B ledger of ruler drift, jump, recall, 300 bp fee and carry, and the CDX mop's own roll leak (\$140k OMS/FCM mismatch, Ch 8-C).

## Flags for other owners (not changed here)

- **Halvorsen CDS level, Ch 24:** Ch 24's cold open (Tue 20 Oct 2026) buys five-year Halvorsen CDS at 370 bp against the 6% 2031s at 88 (Z 480). In Ch 1-B and Ch 11 the 7.25% 2029s are at 78 / about 1,400 bp that same month, and Ch 4-C has the 6% 2031s at 55. The box names the CDS only as an alternative and quotes no level, so it does not inherit the conflict. Ch 24 / continuity should reconcile.
- **Cast:** in 1-B, Dov's analyst is Bea Castellanos and the risk manager is Gordon Pike; the thread's Wen Zhao and Marcus Oyelaran are not in 1-B. Ch 8-D reconciles this (two analysts; Marcus reports to Gordon), so neither Wen nor Marcus was added here. The cast bible's "first on the page in Ch 13" for Wen and Marcus is now out of date because of Ch 8-D. That is for the cast-bible owner.
- **Roll week vs. the story clock:** 1-B's Tuesday is 13 Oct 2026 (the week after the Fri 9 Oct lender call), but §1B.2 calls it "roll week" (rolls around 20 Mar / 20 Sep). The thread's "Index roll week, Sept 2026" inherits this. Left alone, since the FCM roll vignette is canon in Ch 8-C and Ch 27.
- **JTD vs mandate:** the PB-01 ledger flag still stands. Kestrel's JTD (about \$33.6mm) is far above the thread's \$5mm single-issuer jump line. 8-B and 8-D should reconcile it with the 1-B sizes and the \$400mm allocation.

<!-- STATUS: COMPLETE -->
