# Lessons Edit Log (Edition 2): Chapter 16, Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims

*Lessons editor pass against `state/reviews/ed2/u2_lessons.md`. Verify file is COMPLETE. Line numbers are as of the start of this pass (994 lines); re-grep the quoted phrase before each edit.*

## Audit

### (a) Metric, before

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/16_ch16_post_reorg_equities_and_claims.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre | 15148 | 19.1 | 3.0 | 0.4 | 2.1 | 5.2 | 0 | 0 |
| before (now) | 34641 | 7.2 | 3.6 | 0.8 | 1.6 | 8.3 | 16 | 4 |

Growth 34641 / 15148 = **2.29×**, against the 1.6–1.9× target (24,237–28,781 tool words). Need to retire about 6,000 words by merging. (`wc -w`: 35,812.) Modal density rose 3.0 → 3.6; the templated "When ... breaks" subsections and listing explanations carry most of it.

### (b) Duplication (new telling vs old telling; survivor)

1. Cold-open promise, line 81 ("First, find the holder... Second... Third... We will turn...") vs the sections themselves and the Debrief's closing answer. Survivor: the sections; line 81 cut to two sentences.
2. Plan value negotiated: line 91 ("a negotiated number, not an estimate") vs line 93's last sentence ("treat the plan value as one side's opening bid"). Survivor: 91; 93 keeps AmSurg and the "opening bid" phrase in one clause.
3. "The last column is the chapter": line 111 vs line 113 ("The last column is where the trading lives"). Survivor: 113, absorbing 111.
4. Mean vs median: line 135 ("Mean 40%, median zero ... lottery ticket") vs the line 137 Math, Gently. Survivor: 135, absorbing the three-stock number.
5. Overhang breaks: §16.2.1 "When the overhang model applies, and when it breaks" (lines 166–172) vs cold-open Wolfspeed (hedge-fund fulcrum), line 200 boundary ($Q_0 = 0$), Ways This Blows Up items 4 and 5. Survivor: the cold open and the box; the subsection becomes one Mags beat (the CLO election).
6. Half-life 3.4 / 0.20 y / 2.4 months: line 186 box vs line 230 fit and Ch 1 §1.8.1 box. Survivor: the fit; box becomes a gloss with the bathtub image.
7. Logs-turn-ratios box (line 232) vs the fit in lines 229–230 (same 1.04/5.75, 3.42, third window). Survivor: the fit; one clause carries "A cancels".
8. "The peak is always after the event ... ratio of two speeds" verbatim in line 202 and line 222 (Full Derivation). Survivor: 202.
9. Line 208 ("buying the open is buying before the worst price") vs the Figure 16.1 caption. Survivor: caption; 208 cut to one sentence.
10. §16.3.1 "When the put view applies" (lines 310–316) vs line 347 (fee and discount are substitutes), Desk Myth (370), Harlan's answer (415) and the Trend Watch (365, ConvergeOne, verbatim facts). Survivor: 347, 370, 415, Trend Watch; Judge Hanen and the Oct 2024 mootness ruling move into the Harlan scene in one narration sentence.
11. Harlan scene line 405 ("First, Kaz's six months was wrong... Second... Third...") vs the protected numbered list 407–409. Survivor: the list.
12. Put / risk-neutral box (line 335) vs Kaz/Theo exchange (333), Full Derivation (360), Ch 6 §6.2.1–6.2.2 boxes. Survivor: 333 and the worked number, which take the 37% × 0.20 and the "convention, not a measure" sentence.
13. "Adding a jump to zero makes the call worth more, not less" verbatim in line 464 and line 476. Survivor: 464.
14. Poisson box (line 462) vs line 466 ($e^{-0.6} \approx 0.55$ haircut) and Ch 6 §6.1.4 box. Survivor: 466; one-clause pointer.
15. "The spot was the gift": line 468 last sentence, line 491 ("The systematic desk's lesson is not..."), Theo's scene 495–499. Survivor: 468's bridge and the scene; 491's lesson sentences cut.
16. Hertz at \$3 after the June 2026 drop: Docket Diary (664–665), §16.4.3 coda (505), Street six (720), line 726 (restates the Bloomberg Law adviser hires verbatim). Survivor: Docket Diary; 505 and 726 become pointers.
17. Theo's conflict: line 722 vs Ines's question 732. Survivor: 732; 722 keeps only the wall image the Debrief calls back.
18. Statute framing line 546 ("truncation, a priority switch, or an estimation procedure") vs line 558's closing list. Survivor: 558.
19. Lognormal pool box (568) vs mean-median material and Ch 5 §5.2.3 / Ch 6 §6.1.1 boxes. Survivor: one-sentence gloss.
20. Hazard box (601) vs Ch 6 §6.1.4 box; its 0.93 also computes part of Exercise 5 (h = 1.5, r = 4%, ψ = 8%). Survivor: gloss with different numbers.
21. §16.5.3 "When the pair works, and when it breaks" (607–613) vs the $p_{AI}L_{AI}$ term, the Denomination risk paragraph (615) and the FTX Trend Watch. Survivor: those; the bar-date check becomes a Mags/Theo beat.
22. Spirit line items: line 762 ("receipts by week net of holdbacks, aircraft rent by week, minimum liquidity") vs Theo's page, line 764. Survivor: 764.
23. Line 683: "And it still finished in the money ... The call finished in the money" said twice in two sentences.
24. Half-variance box (820) vs Ch 1 §1.5 and Ch 6 §6.1.1 boxes and line 814. Survivor: two sentences in Kaz's mouth.
25. Mixture box (824) vs line 822's $m \approx -5\%$ and Ch 5 §5.1.1 box. Survivor: one-sentence gloss.
26. §16.8.2 "When Kelly applies, and when it breaks" (890–892) vs Kaz's survivor sample (850–866), §16.8.1 independence (838), Ines's ticket (868–880). Survivor: the scenes; the double-Kelly point goes to Ines.
27. Kelly Full Derivation (888) states the branch weighting twice.
28. §16.8.3 line 898 (five pairs as five questions) vs the protected table 900–906: a table in costume. Survivor: the table plus one dramatized row (Mags's vendor at 30 vs bonds at 38).

### (c) Templates (lesson 4, lesson 5, lesson 12)

- Line 81 "First... Second... Third..." in a paragraph; line 242 "First... Second..."; line 275 "five layers. First... Fifth"; line 427 "three parts. First... Second... Third".
- "It breaks in three places/ways" and "seasoned practitioner checks first": lines 168–172, 312–316, 611–613, 788, 892.
- "Use it for / Do not use it / The edge case that bites": lines 279, 429, 517, 639; line 916 "Remember that".
- Detached judgment subsections a scene already shows: §16.2.1 (166), §16.3.1 (310), §16.5.3 (607), §16.7 (788), §16.8.2 (890).
- Listing explanations that open in manual voice instead of the scene's moment: 273 ("reads like a finished thought"), 425 ("Look at what we just did by hand"), 511 ("the kind of object that a spreadsheet handles"), 916.

### (d) Boxes

- Math, Gently: 15 boxes (the tool's 16 includes one in-text mention at line 360) in 34.6k words, one per 2,300 words, but over the cap of ten. First load-bearing use elsewhere: share-is-call (Ch 1 §1.5), mean/median and lognormal (Ch 5 §5.2.3, Ch 6 §6.1.1), martingale/random walk (Ch 1, Ch 6 §6.1.1), half-life (Ch 1 §1.8.1), logs (fit already shows it), put and risk-neutral (Ch 6 §6.2.1–6.2.2), fixed point (Ch 13 §13.7), Poisson and hazard (Ch 6 §6.1.4), half-variance (Ch 1, Ch 6), mixture (Ch 5 §5.1.1). First load-bearing here: Jensen (582), runway intensity (776), Kelly (858). Plan: keep those 3, demote 12 to one-sentence glosses with pointers, keeping their tiny numbers where they are the chapter's own.
- Near-adjacent pairs: 180/186, 458/462, 820/824.
- Runs of more than two boxed elements: §16.2.4 vignette → Ways This Blows Up → Trend Watch → Spec (four); §16.5.3 FTX Trend Watch → claims-buyer Seat → Spec (three); §16.8.3 Poker Table → dealer Seat → Spec (three).
- Trend Watch placement: CLO-documents Trend Watch sits between the vignette and the Spec, not at the end of §16.2.

### (e) Research-note leaks and fiction labels

- Leaks in non-protected text: line 505 "(per press reports; check against filings)"; Docket Diary line 664 "dates and figures to be checked against filings"; line 738 "verify on the docket". Fix by hedging, and log in `state/research/open_items_ch16_ed2.md`.
- Inside fact-checked Trend Watch wording (protected, left as is, logged): line 130 "(check the exact range in the paper)" (applied_factcheck C5); line 263 "(approx.; secondary summaries, primary source not verified)"; line 621 "(per press reports; verify against FTX Recovery Trust notices)" (B2).
- Label gaps: cold open's label is not in italics and Mags's banker label sits at the end of her story (merge into one top label); §16.6 replay scene has no label; the §16.8 week (whiteboard, Kaz's vendor file, the packaging company and its \$200k ADV) has no label.

### (f) Finder and headings

- No Finder table in §16.9. Add 10 rows (concept · equation · intuition · judgment · code).
- Long scenes and decision points are bold paragraphs: §16.6 "How a systematic desk would have traded each leg" and its October 2026 decision; §16.7 post-mortem and its two-airlines decision. Promote to `####`.

### (g) Cast bible

- Line 21: Kaz asks whether "fulcrum" is a gymnastics term, a second misread of a term Kaz already misread in Ch 1 (C7: one misread per term; later uses are callbacks Kaz pre-empts).
- Line 882: Mags "did this trade with the whole fund ... didn't have a risk committee" contradicts C5 (at a bank through Jan 2021). Make it "the whole book" and a quarterly committee.
- Ines's "cash games for a living" (cast bible cites Ch 16) lives in the put box being demoted; keep it elsewhere.
- Dana (vignette analyst at another firm) is not in the cast bible; add a minor-cast line.

### (h) Relative-value beat

- `state/rv_thread.md` does not exist; no RV item this pass.

## Fix items

- [x] 1. Cold open: italic top label (company, numbers, Mags's banker); Kaz's fulcrum callback; promise paragraph to two sentences (b1, c, e, g). Note: one italic label; Kaz pre-empts misread; syllabus cut to two sentences.
- [x] 2. §16.1.1: demote share-is-call box into the option-language paragraph; trim 93; merge 111 into 113; trim CLO seat box (b2, b3, d). Note: call-on-a-call kept as gloss; opening-bid clause; columns merged.
- [x] 3. §16.1.2: merge the mean-median box into the "Read the third bullet" paragraph (b4, d). Note: three-stock arithmetic and tall-person image now in prose.
- [x] 4. §16.2.1: retire the When-to subsection; Mags's election beat (b5, c). Note: three-conditions template replaced by Mags "Did they elect?" beat.
- [x] 5. §16.2.2: demote martingale and half-life boxes to glosses; cut the duplicate peak sentence in the Full Derivation; trim line 208 (b6, b8, b9, d). Note: two boxes now glosses pointing to Ch 6, Ch 1.
- [x] 6. §16.2.3: demote the logs box to one clause (b7, d). Note: A cancels, two photographs of tub, in one clause.
- [x] 7. §16.2.4: "First... Second" in 242; reorder Ways → narration → vignette → Spec; Trend Watch to the end of §16.2; rewrite the Listing 16.1 explanation (c, d). Note: reordered; Listing 16.1 opens on Dana's Thursday; no template.
- [ ] 8. §16.3.1: retire "When the put view applies"; move Hanen and the mootness ruling into the Harlan scene (b10, c).
- [ ] 9. §16.3.2: demote the put box into 333 and the worked number; fix the Full Derivation's reference to the box (b12, d).
- [ ] 10. §16.3.4: cut the prose copy of the three observations; rewrite the Listing 16.2 explanation (b11, c).
- [ ] 11. §16.4.2: demote fixed-point and Poisson boxes; cut the duplicate sentence in the Full Derivation (b13, b14, d).
- [ ] 12. §16.4.3: cut 491's lesson sentences; coda becomes a pointer; rewrite the Listing 16.3 explanation; drop "check against filings" (b15, b16, c, e).
- [ ] 13. §16.5.2–16.5.3: trim statute framing; demote lognormal and hazard boxes (hazard with numbers that do not solve Exercise 5); move the Jensen box ahead of the result; retire the pair When-to for a bar-date beat (b18–b21, c, d).
- [ ] 14. §16.5 Spec: moment-of-need paragraph moved ahead of the Spec to break the box run; trim the claims-buyer seat; rewrite the Listing 16.4 explanation (c, d).
- [ ] 15. §16.6: `####` long scene with fiction label; fix the doubled "finished in the money"; trim 722 and 726; `####` decision point; Docket Diary hedge (b16, b17, b23, e, f).
- [ ] 16. §16.7: hedge 738; `####` scene heading; trim 762; runway When-to becomes a Mags beat; `####` decision point; Ines's cash-games line (b22, c, e, f, g).
- [ ] 17. §16.8.1: week label; demote half-variance and mixture boxes into Kaz's dialogue and a gloss (b24, b25, d, e).
- [ ] 18. §16.8.2: retire the Kelly When-to; double-Kelly line to Ines; Full Derivation duplicate; Mags's "whole fund" line (b26, b27, c, g).
- [ ] 19. §16.8.3: one dramatized pair row; narration between Poker Table and dealer Seat; trim the dealer seat; rewrite the Listing 16.5 sentence (b28, c, d).
- [ ] 20. §16.9: Finder table at the top of the Desk Debrief (f).
- [ ] 21. State: `state/research/open_items_ch16_ed2.md`; Dana in the cast bible (e, g).
- [ ] 22. Metric after; final greps (templates, leaks, box count, `$$` balance, last line).
