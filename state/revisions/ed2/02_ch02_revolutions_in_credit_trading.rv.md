# RV weave log: Ch 2 (02_ch02_revolutions_in_credit_trading), Edition 2, user directive 13

*RV weaver, 2026-10-18.*

## Preconditions

`state/rv_thread.md` present and COMPLETE; this log had only its header (an earlier attempt stopped before writing); `02_ch02_revolutions_in_credit_trading.log.md` is COMPLETE, so no other agent was mid-revision. The chapter had no pair, pod or relative-value content before this pass (grep: "hedge" appears only for dealers, PT baskets and non-bank LPs; "idiosyncratic" only in the RFQ anchor model and the PT risk charge).

## What was written, and where

- **New subsection §2.9.4, "The Pair Book: The Short Leg on the Wire"** (scene, about 1,920 words including label, table, card and display equation), inserted after §2.9.3's "The lesson" paragraph and before "### Specification for AI Implementation". Thread row: scene, PB-01, tool = execution revolutions (A2A, PT, ETF); H = the hedge exists only because the short leg became tradeable (Dov's 2:40 all-to-all cover is the anchor row); I = none new; L = ETF premium, PT basket adverse selection; event = Man 2023 framework (§2.1's two conditions) and the April 2025 shock (§2.9.3).
  - Label at the top in italics (fictional pod, platform, issuers; illustrative numbers; real rules, protocol dates and April 2025 figures; the April 2025 passage a replay cut at the close of Wed 9 Apr 2025).
  - Story clock: Wed 21 Oct 2026, 8:05 to 8:32 a.m. at Vantress, the morning after Ch 22's recall (§22.6.2: \$3.5mm of the \$35mm recalled, due Thursday; Dov chose to cover in the market rather than re-borrow at 450 bp). No conflict found with other dated pod scenes (21 Oct was unused).
  - Wen's "exit column" table: when each piece of PB-01 got a wire (cash bonds: TRACE 2002, all-to-all 2013; CDX HY: Big Bang Apr 2009, SEFs 2014, 96.5–98.0% SEF share H1 2025 per ISDA as in Ch 10; HYG: Rule 6c-11 Sept 2019, one-cent spreads Apr 2025; PT: Tradeweb 2019, TRACE flag 15 May 2023; the borrow: never, Rule 10c-1a pushed to 28 Sep 2028). This table replaces the thread's optional RV figure (timeline of when each short leg became electronic); no figure was scripted.
  - Man 2023 p.4 (two conditions) applied to two legs: the borrow has neither certainty (recall) nor a modelable cost (no tape). Truth stated once: "The wire made every trade in this pair cheaper. It never touched the loan." The pair's $c$ in §2.9.2 is two half-spreads plus a fee, and only the half-spreads fell.
  - Decision card (8:20 a.m.): door for the bonds, what to do with the index sale, order. Posed before the argument.
  - Chapter tool, stress-tested: the §2.5.1 router. Inputs (illustrative): $c_A$ = 3/8 pt, $\pi_A$ = 0.6; dealers 3/4 pt at 90%; $\kappa$ = 2 pts (Thursday buy-in); $J_R$ = 0.875; savings 0.5; line leakage 1/4 pt. Single line: threshold 0.5 vs odds 1.5, all-to-all first. New display equation $\chi^{\text{pair}}_A = \chi^{\text{line}}_A N_{\text{leg}}/N_{\text{ticket}}$ = 0.25 × 35/3.5 = 2.5 pts: threshold 5, sequential cost 1.575 vs 0.875, dealers first. Contrast: the 13 Oct trim passed (utilization in the sixties, 1/16 pt × 39/4 ≈ 0.6, threshold ≈ 1.2 vs odds ≈ 2.3). The crowd raises $\chi$; the pair multiplies it by ten.
  - Leaks named and declined: PT (pointer to §19.6.2, the May 2022 short basket whose Halvorsen line was evicted); HYG as a second beta hedge with its own premium (pointer to §20.5.1, HYG +0.85% on 19 Mar 2020), via Marcus's email ending on his canonical line.
  - April 2025 replay (pod's log, illustrative): on 9 Apr 2025 (13.2 → 6.6 prices per HG RFQ; ETFs \$98.9bn at one cent two days earlier) index trims filled in seconds, bond tickets drew about half their responders; pod rule "the leg without a wire goes first"; tied to Man 2022 p.19 (§2.1) on unfilled orders as unintended positions. Consistent with Ch 10's coda (twelve pairs, small CDX HY trim; no execution story there to contradict).
  - Outcome (illustrative): 8:31 disclosed RFQ to three dealers, \$3.5mm bought at 78.875 (7/8 over the screen, ≈ \$31k); 8:32 about half the CDX HY sale bought back on the SEF (short DTS 31.5 × 0.78 × 2.3 × 1,400 ≈ 79,100 vs 70,200; gap 17,700 → 8,900). Cards graded.
  - Isolation paragraph (Dov's ledger line): legs (long \$60mm Kestrel 6% 2030; short \$31.5mm Halvorsen 7.25% 2029, borrowed from one agent lender via the prime broker at 300 bp, recallable; ratio 0.525 by face); hedge (market-value DTS plus CDX HY, cut to ≈ 8,900 DTS); removes HY beta, most of the housing-cycle sector factor, most of rates; idio unchanged in content, \$315k per point of Halvorsen vs \$600k per point of Kestrel; leaks (execution leakage × leg; ETF premium and PT adverse selection declined; the borrow); carry ≈ +\$0.08mm/yr after the cover (Kestrel \$3.6mm; coupon owed \$2.28mm; fee ≈ \$0.74mm on \$24.6mm MV; financing net of rebate ≈ \$0.5mm) vs about −\$0.25mm before (§22.6.2); cover ≈ \$31k once; exit half-spreads ≈ \$0.39mm by the end-March 2027 thesis date.
  - Cross-reference to the canonical home: "The full menu of short legs, row by row with the basis each one brings, is Chapter 8-D's (§8D.2)"; Chapter 20 named for the ETF. Ch 2-B (the thread's other home) is not yet in `book_src/`, so it is not cited.
- **§2.10 Finder table, Router row**: judgment cell extended with "a pair's leg leaks on the whole leg, $\chi^{\text{pair}} = \chi^{\text{line}} N_{\text{leg}}/N_{\text{ticket}}$ (Dov's recall cover, §2.9.4)".

## Retirements

None. No paragraph in Ch 2 told any fact the scene now tells (no pair, borrow or pod content existed). Facts already told elsewhere in the chapter are cited by section, not retold (13.2 → 6.6 and the ETF record in §2.9.3; Open Trading's 1,800 firms in §2.4; Man's two conditions and the unfilled-order sentence in §2.1); the futures-block figure in §2.7.1 was deliberately left out of the table to avoid a second telling. Nothing protected was touched: display-math blocks 26 → 27 (one added), all Source Extractions, Trend Watches, exercises, URLs and `#code-2-k` links unchanged. Last line of the chapter is still the STATUS marker.

## State files updated

- `state/rv_pair_book.md`: PB-01 row (Stressed-in gains Ch 2 §2.9.4 with the router numbers; status "stressed (Ch 2, 5, 11, 27)"; ratio column gains "0.525 after the Ch 2 recall cover"; What-leaked gains the Ch 2 execution entry and post-cover carry); new chapter note "Ch 2 §2.9.4 ... PB-01 on the wire" under Chapter notes.
- `state/cast_bible.md`: new bullet before "## Ch 23 additions" (Wed 21 Oct 2026 times, Dov's ex-dealer line, Wen's exit column and April 2025 log, the pod rule, Marcus's email, outcome).

## Open items (not fixed here)

- "SEFs from 2014" rests on Ch 10's CFTC Bloomberg-SEF study window (May 2014); the CFTC made-available-to-trade date for CDX was not re-checked against a primary source in this pass.
- Ch 22's PB-01 box says the CDX sale covers "the beta the September trim left behind"; Ch 1-B dates the trim Tue 13 Oct 2026. Ch 2 follows 1-B ("last Tuesday", eight days before 21 Oct). For the Ch 22 owner.
- Ch 22's weave lists "22" in PB-01's Stressed-in column without detail; its recall and 300 bp numbers are used here as canon.

<!-- STATUS: COMPLETE -->
