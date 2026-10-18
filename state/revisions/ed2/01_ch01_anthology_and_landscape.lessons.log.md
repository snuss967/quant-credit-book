# Lessons Pass, Edition 2: Chapter 1

*Lessons editor pass against `state/reviews/ed2/u2_lessons.md` (including the orchestrator ruling on lesson 1: the band measures duplication, not length), run 2026-10-18 on `book_src/01_ch01_anthology_and_landscape.md` (854 lines, after the U2 fixer pass logged in `01_ch01_anthology_and_landscape.fix.log.md`). Verify log is COMPLETE. Worked examples read: `u2_quality_read.md` (b)–(d) and the Ch 1 table in `u2_fixes_ch01_05_06.md`; the fixer pass already applied that table, so this audit looks for what it left and what it introduced. Line numbers are the file as of the audit; re-grep the quoted phrase before each edit.*

## Audit

### (a) Metric

- [x] A1. **Before** (`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71`): pre 9,923 words, bullets 14.3%, modal 2.9, imper 1.2, rule 1.8, dialog 7.5, Math Gently 0, Seat 0. Now 25,603 words, bullets 5.5%, modal 3.9, imper 0.9, rule 1.6, dialog 12.8, Math Gently 16, Seat 4 (file 854 lines, 26,912 wc words). **Growth 2.58×** against the 1.6–1.9× band (15,877–18,854 words). Per the orchestrator ruling, cuts below come only from duplicate tellings, templates and the box budget; single-telling scenes and protected items stay.

### (b) Duplication (new telling vs old telling, and which survives)

- [x] B1. "Three bets stacked on top of each other": the promise (L29) and the table lead-in (L51), 22 lines apart. **Survivor:** L29; L51 becomes a plain lead-in to the owners table. *Done: L51 now "each term has an owner and a home".*
- [x] B2. §1.2 says each thing twice: Ines's "Nobody here is stupid. Most of them are just not free" (L91) and the narrator's "Everyone in that table is smart. Most of them are not the problem" (L118); "The table below is the map" (L91, Ines speaking about the book's table) and "it is the chapter's map" (L107); "The last column is the one that matters most" (L107) and "The problem is the last column" (L118). **Survivor:** Ines's line and L118's last-column sentence; L107 and L91 trim. *Done: one "map", one last-column sentence, tied to "not free".*
- [x] B3. §1.3.3 Theo's six-feature walk (L195–219, "the first feature ... the sixth") is a table in costume, and the Serta decision point relists the same features in Theo's voice (L742). **Survivor:** a six-row table in §1.3.3 with two rows dramatized (Rule 2019; five dealers); Serta's Theo points back to the whiteboard and adds only the new row (the document sets $J$). With C2. *Done: six-row table, two rows dramatized; Serta adds document row.*
- [x] B4. The seven-year BBB versus four-year single-B: Mags's circled lines (L308–310), the p.61 annotation (L328), and the Desk Myth box (L356), whose second half ("the four-year CCC is mostly an equity claim with a coupon") is the CCC-wears-a-tie paragraph (L342). **Survivor:** Mags's scene, the annotation and L342; the Desk Myth box retires. *Done: Desk Myth box deleted; nothing in it was told once.*
- [x] B5. Phantom position: L350 ("a small Treasury position that nobody had chosen") and the Veronesi annotation (L354, "leave a residual that nobody chose"; "The spec must name..."). **Survivor:** the narration; the annotation drops the restatement and gives the rule to Kaz's wiki page. *Done: residual restatement cut; rule now Kaz's wiki page line.*
- [x] B6. Fat tails: the box (L408) ends with "a DD of 4 ... almost 1 in 100 ... a factor of about 300", which the p.138 annotation (L412) states again two lines later; the annotation also repeats the "Let's just assume Gaussian... I regret it already" gag already spent in the Ways This Blows Up box (L253). **Survivor:** the annotation's numbers; the box becomes a gloss (D3) without them; the second gag goes. *Done: box now Kaz-paragraph gloss; 300x told once; gag cut.*
- [x] B7. The risk-neutral box's last sentence ("Kaz's 12 bp is a $\mathbb{P}$ number fed into a $\mathbb{Q}$ formula", L430) restates Ines's "Kaz just fed the forecast into the price formula" (L428). **Survivor:** Ines. With D2. *Done: sentence cut in the merged box; Ines's line stands alone.*
- [x] B8. §1.6: Theo's "Fallen angels beat high yield by three percent a year" is quoted at L468 and again inside the Paleologo annotation (L496). **Survivor:** L468; the annotation keeps only Kaz's reply. *Done: Theo's repeat cut; Kaz's one typed line kept.*
- [x] B9. The flow-graph demo numbers (\$12.9bn sell, \$6.5bn capacity, \$6.4bn dealer, 5.12 points, 4.87 by day 60) are told four times: the conservation box (L538), the half-life box (L555), Reading Listing 1.3 (L571) and Act 3 (L633). **Survivor:** Act 3 (12.9 / 6.5 / 6.4 / 5.12) and the listing paragraph (the 4.87 reversal only, pointing to Act 3); the conservation box gets its own number (D4); the half-life gloss carries none. *Done: Act 3 holds the numbers; box 10/7/3; listing points back.*
- [x] B10. §1.8.1 "The Spec You Hand the Robot" (L565) duplicates §1.10 Spec item (4) (the fixer's open item; lesson 11), and the bridge (L567) restates ROBO's one-node graph and the conservation law. **Survivor:** the §1.10 Spec, gaining the validation clauses only §1.8.1 had (no negative holdings or capacity, fractions in $[0,1]$, positive windows, no holder sells more than it holds, a holder with no rule sells nothing, edges sum to total sells); L567 cut to two sentences. *Done: body Spec deleted; §1.10 item 4 gained its clauses.*
- [x] B11. Ford "What happened, and the answer" (L673–675): restates Kaz's hypothetical absorber (L661) as fact in the same words, and "How a systematic desk would have flagged it / would have traded it" restates Mags's falling-knife checks (L653) and Kaz's card (L647) before the cards are turned over. **Survivor:** Mags and the cards; the answer keeps the April extension, the forced-buyer sentence, HY inclusion, the calendar flag and the IDO line. *Done: absorber restatement and "would have traded it" cut.*
- [x] B12. Serta: Mags's "On 22 June the transaction closed..." (L770) restates the Docket Diary's 52.6%, \$200mm and 47.4%; Ines's action item (L780) restates the Poker Table's "the average markout on each feature bucket *is* $-\pi J$" (L247). **Survivor:** the Diary and the Poker Table; Mags keeps "*Including* the ten million I bought from the CLO". *Done: Mags drops Diary percentages; action item drops −πJ restatement.*
- [x] B13. "Where this blows up" (L557) lists the double-count and the wrong window and points to Act 3; Act 3's last sentence (L639) points back and lists them again. **Survivor:** Act 3 shows them; §1.8.1 keeps state-dependent capacity and Moyer's CLO quote. With C4. *Done: list and back-pointer cut; Act 3 ends on census.*

### (c) Templates (lesson 4) and detached judgment paragraphs (lesson 5)

Grep for "It breaks in", "seasoned", "the first question", "Use it for/as", "do not mistake", "edge case that bites", "When to reach for it": no hits (the fixer removed the four judgment paragraphs). Remaining templates:

- [x] C1. L165 "Three things fall out immediately. First... Second... Third...": recast as one reading of (1.1) without enumerators. *Done: enumerators gone; long desk, block discount, reservation mid kept.*
- [x] C2. L197–217 "the first feature ... the sixth": with B3. *Done under B3: the six ordinals are now table rows.*
- [x] C3. L420 Schmid annotation "It invites two errors. Kaz commits the first a few paragraphs from here... The second is...": recast without enumerators (Kaz's error moves to the next paragraph under D2). *Done: "Kaz is about to"; recovery becomes "the quieter trap".*
- [x] C4. L557 "the first two failures ... The third is worse": with B13. *Done under B13: census sentence, then "the worse failure".*
- [x] C5. L289 Listing 1.1 closer "In production it is the pricing kernel... It estimates none of `pi`, `J` or `sigma_ido`...": the U1 "what it is not" template. Recast through Kaz's sticky note from §1.3.2 (*hedge, horizon, jump*), which already names the kernel's three blind spots. *Done: limits now read through Kaz's sticky note; facts kept.*

### (d) Boxes (lessons 6–8, 10)

Count: 16 Math, Gently (L37, 139, 145, 183, 251, 318, 344, 368, 390, 408, 422, 430, 444, 482, 538, 555) against a cap of ten; L139 and L145 sit one paragraph apart, L422 and L430 three short paragraphs apart. One run of three boxed elements (L251 Normal/Poisson → L253 Ways This Blows Up → heading → L265 Quant-Shop Life); every other run is two. Equations (1.3) and (1.4) live only inside blockquoted annotations (lesson 10).

- [x] D1. Merge "What is a distribution, and what is a certainty equivalent?" (L139) and "Pricing by indifference" (L145), two building blocks needed at once for (1.1), into one box in two parts at L139 (lesson 6); retire the "each gets its own box" promise, since fat tails will not. *Done: one two-part box (bag; indifference price); promise now points fat tails to Ch 5.*
- [x] D2. Merge "Waiting for the phone to ring" (L422) and "What 'risk-neutral' really means" (L430) into one two-part box placed after Kaz's 12 bp beat, signing off "next" into the credit-triangle Full Derivation, which then follows it directly (lesson 10 order: statement in the annotation, box, derivation). With B7. *Done: phone/whose-phone box after Kaz's beat; derivation directly below.*
- [x] D3. Demote six survey-mention boxes to one- or two-sentence glosses that keep the picture and the tiny number, with pointers to the chapter that owns the first load-bearing use: regression slope (L344 → §7-B.1), Monte Carlo (L368 → §6.5 and Chapter 7-B), fat tails (L408 → §5.7 and §6.4; with B6), correlation and the common factor (L444 → §5.5's weather box; the Full Derivation keeps 9.7%), decile sort and IR (L482 → Chapter 9), exponential decay and half-life (L555 → §9.4, which cites Ch 1's cooling cup, so the gloss keeps the coffee). Result after D1–D3: 8 Math, Gently. *Done: six glosses with pictures, numbers, pointers; count now 8.* *Revised at Z1: the regression-slope box is restored (pointer now §7-B.1), because Ch 9 (twice), Ch 18 and Ch 20 cite "Chapter 1's box on regression slopes" and Ch 7-B has no such box; final count 9. Ch 16's pointer to "Chapter 1's box in §1.8.1" now meets the half-life gloss; queued in `state/cleanup_queue.md`.*
- [x] D4. The conservation box (L538) uses the Listing 1.3 demo's numbers (lesson 7): give it its own tiny number. With B9. *Done under B9: sell 10, absorb 7, dealers take 3.*
- [x] D5. Run of three at L251–265: thread one line of narration between the Normal/Poisson box and the Ways This Blows Up box. *Done: Kaz tries the fifty-point jump; run now two.*
- [x] D6. Move eq. (1.3) out of the Ben Dor p.61 annotation and eq. (1.4) out of the Bohn–Stein p.128 annotation into body text; extraction and the annotation's first sentence stay boxed; equation numbers unchanged. *Done: both equations and their derivations now in body text.*
- [x] D7. Refresh the Finder's intuition column for D1–D3, then re-run the box-run and adjacency script. *Done: five Finder cells renamed; longest run two; none adjacent.* (Eight Math, Gently in about 24k words, one per 3,000; the tightest local gaps are 605 and 1,013 words inside §1.3, three load-bearing first uses, none adjacent.)

### (e) Research-note leaks and fiction labels (lesson 13)

- [x] E1. Grep: no "CHECK", "search summary" or "as summarized"; "secondary" appears only in the facility's name and the Fifth Circuit's quoted words. Process voice remains in two Resource Graph lines: L689 "(search the archive by topic; we do not cite episode numbers)" and L849 "(search by topic; episode numbers deliberately omitted)". Remove it; log the U3 episode-level item in `state/cleanup_queue.md`. *Done: both process parentheticals cut; U3 item queued in cleanup_queue.*
- [x] E2. The cold open's label sits mid-paragraph ("(Halvorsen is fictional. ...)", L5). Move it to an italic line at the top of the scene naming what is invented; keep the "genre" joke. *Done: italic label tops the scene; genre joke kept in place.*

### (f) Finder table and headings (lessons 11, 12)

- [x] F1. The Finder exists at the top of §1.10 (ten rows, concept · eq · box · scene · code); its rows stay, refreshed under D7. Checked, no other change. *Done under D7: ten rows kept, intuition cells updated.*
- [x] F2. The cold open is a bold line, not a heading: promote to `## Cold Open: The Halvorsen RFQ` (Ch 3 and Ch 5 precedent). Long Scenes 1 and 2, both decision points and the Serta coda are already `####`. *Done: "## Cold Open: The Halvorsen RFQ" heading added above label.*
- [x] F3. Lesson 12: §1.8.1's "Specification for AI Implementation" block (ROBO's vague version, bridge, Reading Listing 1.3, link; L561–575) explains a listing by a scene the reader has not reached ("(Act 3, below)"). Move the block to after Case Study B, so Act 3's double-counted fund comes first; fix Act 3's "demo numbers from Listing 1.3". With B9, B10. *Done: spec block follows Case Study B; pointers now say "above".*

### (g) Cast-bible contradictions

- [x] G1. C9: "Halvorsen Building Products" (L5) → "Halvorsen Packaging Holdings" (canon; 7.25% senior unsecured 2029, B3/B- already match). *Done: RFQ now names Halvorsen Packaging Holdings; terms unchanged.*
- [x] G2. C10 and rule 3: the cold open names no story date; canon is Friday 9 October 2026, week three. *Done: dateline reads Friday 9 October 2026, third week.*
- [x] G3. C14: "Once a quarter, on a Saturday, Ines runs what the desk calls a replay" makes the quarterly Saturday the only replay; canon is Friday-afternoon replays, with the long quarterly one on a Saturday. *Done: Friday replays; the long quarterly one on Saturday.*
- [x] G4. Record in `state/cast_bible.md`: C9, C10 and C14 applied in Ch 1; new open contradiction, Ch 1-B §1B.2 has Halvorsen going "from 83 to 78" on the Friday, against Ch 1's 2:58 p.m. print at 91.25 and Monday open at 78 (for the 1-B pass); Dov Adler and PB-01 now named in Ch 1. Checked, no change needed: Kaz they/them throughout; Mags's Serta \$10mm from the CLO on the bank's loan book (C4); co-op counter 0 (C6); the fulcrum misread at its first appearance (C7); Mags's employers unnamed (rule 4); "When I started" (C5). *Done: C9, C10, C14 annotated; 1-B contradiction logged; Dov under H1.*

### (h) Relative-value beat

- [x] H1. `state/rv_thread.md` exists and assigns Ch 1 a **box**: PB-01 (foreshadow), tool = the forced-seller flow graph, H: the pod is the chooser of hands at the market maker's table; I: it takes the hand the market maker must offer; L: it needs a short that exists (Law 1); event = the Halvorsen lender call, Fri 9 Oct 2026; home = Ch 8-D §D.1. The chapter has no beat (only §1.1's generic pod Seat box). Write a `> **The Pair.**` box at the end of Case Study A, threaded by one line of narration, pointing back to §1.1's seat instead of retelling it and leaving 1-B's numbers to 1-B; update PB-01 in `state/rv_pair_book.md`. The optional RV figure (pod node with two arrows) is deferred: no build or figure script in this pass. *Done: Pair box closes Case Study A; PB-01 row and cast bible updated.*

### (z) Close

- [x] Z1. Re-run the metric and record **after**; check protected items (18 Source Extractions with page numbers, 4 Trend Watches verbatim, 6 exercises, 7 `\tag`s, `$$` balance, 28 URLs, 4 `#code-1-k` links, 3 figure comments, no code fences), box runs and Math, Gently adjacency. *Done: after recorded; every protected item identical; longest run two.*

## Metrics

- **before** (`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71`): words 25,603 · bullets 5.5% · modal 3.9 · imper 0.9 · rule 1.6 · dialog 12.8 · mathgently 16 · seat 4 (file 854 lines, 26,912 wc words); growth 2.58× on pre 9,923.
- **after**: words 24,646 · bullets 5.7% · modal 3.7 · imper 0.9 · rule 1.5 · dialog 12.5 · mathgently 9 · seat 4 (file 851 lines, 26,165 wc words); growth **2.48×** against the 1.6–1.9× band. Per the orchestrator ruling on lesson 1, the remaining excess is single-telling scenes (Ford in four acts, Serta's two RFQs, the Quant-Shop Life morning), sourced cases and protected text; no duplicate telling found in the audit is left.

## Fix notes

- Protected-item check against the pre-pass snapshot: 18 Source Extraction quote lines identical (page numbers intact), 4 Trend Watches verbatim, Exercises 1–6 identical, 7 `\tag`s (1.1)–(1.7) with numbers unchanged, 28 URLs identical, 4 `#code-1-k` links, 3 figure comments, no code fences, no em dashes, every inline `$` balanced. `$$` lines rose from 22 to 26 only because (1.3) and (1.4) left their blockquotes (D6).
- The §1.8.1 spec block now follows Case Study B (F3), so §1.8 runs model → Ford → Pair box → LQD post-mortem → spec and Listing 1.3 → Resource Graph.
- Kaz's new beat (D5: the fifty-point jump in both bags) and the Pair box's lead-in (H1) are the only new narration; both are one or two sentences.

## Open items

- The RV figure for Ch 1 (the flow graph gains the pod node with two arrows) is deferred; no figure script was run in this pass.
- Ch 1-B §1B.2's "from 83 to 78" on the Friday contradicts Ch 1's 91.25 print and Monday open at 78; logged under C9 in `state/cast_bible.md` for the 1-B pass.
- Ch 16's "Chapter 1's box in §1.8.1" and the Ch 1 *Odd Lots* entries (channel-level) are queued in `state/cleanup_queue.md`.

