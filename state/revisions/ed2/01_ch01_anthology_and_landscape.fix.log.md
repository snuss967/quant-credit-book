# Fix Log (Edition 2 fixer): Chapter 1, `book_src/01_ch01_anthology_and_landscape.md`

*Fix list: `state/reviews/ed2/u2_fixes_ch01_05_06.md`, Chapter 1 section. Rules: `state/reviews/ed2/u2_lessons.md`; style bible §8; user directive 12. Started 18 Oct 2026.*

## Metrics

- **before** (`python3 tools/prescriptiveness.py`): words 26,823 · bullets 5.3% · modal 4.2 · imper 1.0 · rule 1.7 · dialog 11.7 · mathgently 18 · seat 4 (file: 805 lines, 27,720 wc words)

## Items

- [x] P1 · §1.8.3, line 655, first paragraph · Delete paragraph 1; keep paragraphs 2–3; retitle "Case Study B: Post-mortem of Act 1 (LQD at a 5% discount)". — *Paragraph cut, retitled; "NAV was mispriced" line kept; SMCCF date now points to Act 2.*
- [x] P1 · §1.8.2, lines 647–649, "What happened, and the answer" · Cut SMCCF 23 Mar / rebalance date / HY outflow sentences; keep April extension, "forced-seller event became a forced-buyer event by announcement", systematic-flag paragraph, IDO line. — *Cut SMCCF/rebalance/outflow restatements; kept April extension, HY inclusion fact, flags.*
- [x] P1 · §1.2, lines 91–115, six-chair walk · Keep chairs 1, 3, 6 as Halvorsen counterfactuals; drop chairs 2, 4, 5 from the walk; keep Ines's "Laws are what you call observations that have cost you money twice." — *Walk now three Halvorsen counterfactuals (chairs 1, 3, 6); table carries rest.*
- [x] P1 · §1.9.1, line 748, "The market maker's version" · Cut to last two sentences (Ch 3 / Ch 13 pointers, hand-history loop), or give them to Ines as the scene's close. — *Paragraph deleted; Ines's action-item line now closes the scene.*
- [x] P1 · §1.3, line 261, "The Spec You Hand the Robot" · Delete the §1.3 copy; vignette says "The chapter's spec (§1.10) says". — *§1.3 spec cut to pointer; §1.10 gains sigma_ido units, jump_penalty_ratio.*
- [x] P1 · Line 29, promise paragraph · Replace with two sentences (the number is three bets; the chapter builds each); move five outcomes to §1.10 train scene. — *Two-sentence promise; five outcomes now Theo's train-scene paragraph in §1.10.*
- [x] P1 · §1.9.1, line 764, co-op counter note · Reword: "no cooperation agreement before the deal; the excluded lenders organized afterwards, as plaintiffs, which is why the counter stays at 0." — *Verifier already reworded; kept, no unverified pre-deal claim added.*
- [x] P1 · §1.9.1, Serta scene, 11:45 a.m. RFQ (~698) · Second account explicitly "a fund I later learned had been pitched and passed". — *Verifier already made it pitched-and-passed; wording confirmed, unchanged.*
- [x] P1 · Docket Diary, line 676 · Add the \$734mm / \$875mm reconciliation clause. — *Reconciliation clause added, pointing to Ch 5 §5.6.2 wording.*
- [x] P2 · §1.3.2 l.169; §1.4 l.350; §1.5 l.398; §1.6 l.480 · Four "When to reach for it" paragraphs: inventory → 150-word "Whose five days?" beat; DTS delete; DD → Mags's "lottery ticket on the plan"; fallen angel delete; add four judgments as Finder rows. — *Inventory now 'Whose five days?' beat; DTS, fallen-angel cut; DD to Mags.*
- [x] P2 · §1.5, lines 376–380 · Keep "Equity is a call option" box; reduce random walk and Itô boxes to one sentence each in Kaz's dialogue with pointers to §6.1.1. — *Two boxes became Kaz's dialogue: square-root horizon, half-variance drag, §6.1.1.*
- [x] P2 · §1.5, lines 402, 406, 442 · P/Q told thrice: add 80-word beat (Kaz feeds vendor EDF, gets 12 bp at 100; Mags: "Which number is lying?"); annotation and listing point to "Kaz's 12 bp". — *Beat added; Schmid annotation, risk-neutral box, Listing 1.4 cite Kaz's 12 bp.*
- [x] P2 · §1.6, lines 468–470 · Man Numeric 30/60→90 and Blackstone quote only in seat box; annotation keeps aphorism; §1.8 intro says "the Blackstone sentence from §1.6". — *Man 30/60→90 and Blackstone quote only in seat box; pointers elsewhere.*
- [x] P2 · §1.6, lines 470–476 · Move both Trend Watches to the end of §1.6; add one line of narration before Paleologo extraction ("Kaz's reply arrived at 11:40."). — *Trend Watches moved to section end; 11:40 line and two narration threads added.*
- [x] P2 · §1.3.3, line 179, Bayes box · Change to prior 5%, LRs 6 and 2 (odds 0.0526 × 12 = 0.63, π ≈ 0.39). Leave Exercise 2 and Serta arithmetic. — *Box now 5% prior, LRs 6 and 2, π≈0.39; exercise intact.*
- [x] P2 · §1.3 Specification, lines 257–287 · Move vignette to open the Specification section; delete Listing 1.1 "edge case that bites" sentence. — *Vignette opens section; edge-case sentence cut, double-counting folded into bridge.*
- [x] P2 · Reading Listing 1.2, 1.3, 1.4 · Open each with the chapter moment; drop template phrases. — *1.2 opens on Mags's lines, 1.3 on Act 3, 1.4 on Kaz's 12 bp.*
- [x] P2 · §1.8.1, line 533, "Where this blows up" · Cut to Moyer quote + state-dependent-capacity sentence + "Act 3 shows the first two happening on a Saturday." — *Cut to Act 3 pointer, state-dependent capacity (with kappa), Moyer quote.*
- [x] P2 · §1.10 Desk Debrief · Add Finder table before the bullets (concept · eq · box · scene · listing). — *Ten-row Finder table added above train scene, carrying four judgments.*
- [x] P2 · Lines 555 and 680, Long Scene bold paragraphs · Make them `####` headings; add `####` for each decision point. — *Both scenes, two decision points, Serta coda now #### headings; reader card.*
- [x] P2 · §1.4, line 352 · Replace manual-voice bridge with Theo's spreadsheet DTS-in-percent slip, Kaz catching it, then the function. — *Bridge replaced by Theo's percent-column slip, Kaz's catch, row 3,112.*
- [x] P3 · 17 of 18 Math, Gently sign-offs · Vary; "next" where the derivation follows immediately. — *No 'full version' left; 'next' where derivations follow; others varied.*
- [x] P3 · §1.4, line 338, regression-slope box · Add worked number (yields +100 bp, HY price +1 point → slope +1, "negative duration"). — *Two-dot example added: slope +1, empirical duration −1, negative duration.*
- [x] P3 · §1.3.2 box vs cold open in numbers · Link 0.19 and 0.317 in one sentence. — *Box now adds 5 × 0.025 to reach the desk's 0.317.*
- [x] P3 · Ford scene, lines 559, 651 · Trim ~150 words of framing padding. — *Pastries, USB, door pause and Kaz's dated notebook cut; content kept.*
- [x] P3 · Serta scene, lines 680–686 · Trim opening 300 words to ~150; keep "I have. Twice in one afternoon. Only one of them was." — *Opening cut from 231 to 129 words; key line and analyst kept.*
- [ ] P3 · §1.4, line 346, Veronesi annotation · Lead with the phantom position (Tuesday's markout residual), then the rule.
- [ ] P3 · Appendix F · Title Listing 1.4 properly; trim 1.2's stray prose and duplicate block.
- [ ] P3 · Resource Graphs (289, 661, 798) · U3 item; do not invent episodes.

## Open items

## Notes
