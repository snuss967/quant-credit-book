# Ch 15 RV weave log (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread entry (`state/rv_thread.md` §(e), row `15_ch15_event_driven_mna_and_coc`): two boxes, PB-09 and PB-10; tool = SMR as a digital, CoC put as a compound option; H = the issuer, by same-issuer legs; I = break probability (PB-09), the put's moneyness (PB-10); L = acquirer-curve duration jump at termination, the defeasance article; home "—" (the chapter itself).*

## Preconditions

- `state/rv_thread.md` ends with STATUS: COMPLETE. No `.rv.md` log existed. `15_..._log.md` (U2 log) is COMPLETE, so not busy.

## What was already in the chapter

Both beats were already in `book_src/15_ch15_event_driven_mna_and_coc.md`, written by an earlier weave that was swept into commit 566b474 (the Ch 8-D commit) without a log or a ledger update (ledger still said `planned`). Verified rather than rewritten:

- **PB-10 box**, §15.2, directly after the EA case study's "They were handed duration" paragraph and before the View From Another Seat (insurer, opportunistic fund; the RV seat there was retired in favour of the box when it was written). About 600 words. Replay cut Fri 3 Oct 2025, run to the 4 Aug 2026 close. Re-casts the planned pair honestly: Wen reads the 2016 base indenture and finds both series carry the same put and the same defeasance article ("There is no second bond"), so the pair is long \$20mm 2.950% 2051s at 90 / short \$50mm 1.850% 2031s at 98.5, borrowed from an insurer's lending program at 30 bp. Tool: the §15.4.2 ruler applied to defeased-vs-101 (62% vs 78%). Hedge: event-jump weights $h = 29/11.5 \approx 2.5$ (Owen's recovery weights, §4C.3). Removes EA's credit and the sponsor's choice (+\$0.95mm paid / +\$0.90mm defeased). Idio: the 16-point gap between two prices of one decision; unequal treatment −\$4.85mm, sized inside the \$5mm line. Leaks: duration on the closing date (\$10k vs \$8k/bp → \$23k vs \$19k/bp, a curve trade nobody chose), recall risk around the tender, the rating trigger. Costs: coupons −\$0.34mm/yr, fee \$0.15mm/yr, rebate, half-spreads \$0.33mm; capture ≈0.2. Arithmetic re-checked: every number ties to the case study (9% of 2031s tendered; 4 Aug 2026 close; defeased values low 70s / 89–90).
- **PB-09 box**, §15.4.2 "Reading the gauge", after the four-deal SMR table and before the Specification. About 600 words. Replay cut Tue 26 Nov 2024. Long \$50mm 2027 SMR notes at 99.90 / short ≈\$34mm MV legacy non-SMR Kroger note of similar maturity, borrowed at 25 bp. Tool: the gauge (36%) and probabilistic duration, $h = 1.9/2.8 \approx 0.68$ by MV, against the risk system's 2.8 (the cold open's one-column report). Removes Kroger spread and 3y Treasuries on average (assumption B2). Idio: the judge coin, +\$0.80mm / −\$0.45mm. Leaks: the ratio wrong in both worlds; the 11 Dec buyback hitting the short the day it was bought back (blow-up 1). Costs and capture ≈0.8. Cross-reference to the canonical home: §8D.2 (short-leg menu; CDS alternative). Arithmetic re-checked against the cold open (99.90, 101.5, 99.00, 36%, 2.8).
- **Finder row** "Same-issuer event pair" in the §15.9 Desk Debrief table already present.

## What this pass changed in the chapter

1. PB-09 box: the pod's competing-risks fit labeled "its fictional run" (u2 lesson 13: invented model outputs on real names).
2. PB-09 box: the capture ratio now says it is struck "before the buyback-day leak line, which the replay deals no prints to price" (the cold open and the "Kroger 2034s prints on Dec. 11, 2024" item in `state/research/open_items_ch15_ed2.md` say the replay has no 2034s/legacy prints for 11 Dec 2024; the box had booked that line as leak but then silently netted it at zero). Three trims elsewhere in the box to hold it at about 600 words ("Dov's dated sentence"; Ines's three-bets clause; the control-group clause).
3. §15.6 View From Another Seat (the generic multi-strategy pod): one clause tying the long-target / short-acquirer pair to Theo's stripped backtest and to the chapter's two same-issuer Pair Book entries (PB-10 §15.2, PB-09 §15.4.2), and a cross-reference to the canonical home for the stop's arithmetic, **Chapter 8-D §8D.5** ("Sizing to the Stop"). No paragraph retired: the seat tells an inter-issuer event pair, which neither box tells.

Nothing removed: all topics, equations, Source Extractions, Trend Watches, exercises, figures, Appendix F links and URLs untouched. No code blocks added. No figure added (the thread's optional "implied break probability from the SMR pair" is already carried by Figure 15.3). Chapter's last line is still the STATUS marker.

## State files

- `state/rv_pair_book.md`: PB-09 and PB-10 rows rewritten from `planned` to `closed (Ch 15)`, with legs, ratio and method, chapter locations, idio share, capture ratio and what leaked; PB-10 records that the thread's planned short ("notes the defeasance article governs") is retired because the article governs both series.
- `state/cast_bible.md`: one bullet in the Ch 8-D additions block ("Ch 15 Pair Book") recording Dov's, Wen's and Marcus's Ch 15 facts and that Wen and Marcus are at Vantress by Oct 2025.

## Open items

- The PB-09 leak line (legacy Kroger note on 11 Dec 2024) stays unpriced until someone pulls the TRACE prints; same open item as the cold open's 2034s.
- PB-10's defeased values (≈72 and ≈89.5) are the case study's illustrative Treasury-flat numbers; if the EA indenture check in `open_items_ch15_ed2.md` item 2 changes the reading of covenant defeasance, the box's thesis survives (both series alike) but the leak paragraph's rating-trigger sentence should be re-read.

<!-- STATUS: COMPLETE -->
