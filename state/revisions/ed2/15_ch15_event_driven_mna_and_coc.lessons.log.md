# Lessons Edit (Edition 2), Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control

*Lessons editor pass against `state/reviews/ed2/u2_lessons.md`. Verify file has STATUS: COMPLETE. Read: user directive 12, u2_lessons, u2_quality_read (b)-(d), the Ch 1 fix table, cast_bible, style bible §8. `state/rv_thread.md` does not exist, so (h) has no item.*

## Audit

### (a) Metric, before

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/15_ch15_event_driven_mna_and_coc.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre | 11,020 | 14.0 | 3.2 | 1.4 | 0.8 | 8.1 | 0 | 0 |
| before | 33,525 | 3.9 | 3.0 | 1.1 | 0.9 | 7.9 | 19 | 6 |

Growth 3.04x against the 1.6-1.9x target (17,630-20,940 words). Heaviest sections: §15.2.2 (3,329), §15.5.2 (2,768), EA case (2,625), cold open (2,558, against an 800-1,500 budget), §15.4.2 (2,510), ICE scene (2,408), §15.8 (2,195).

### (b) Duplication (new telling vs old telling; survivor)

- D1 Kroger redemption-window quote: cold open l.13 and §15.4.1 l.450. Survivor: cold open; §15.4.1 points back.
- D2 Kroger timeline: cold open l.81 and Docket Diary l.525 (plus l.7, 11, 59). Survivor: Docket Diary; l.81 cut to its last sentence.
- D3 Kroger buyback contaminating the control group: cold open l.61, "When the gauge" l.515, Ways (1) l.521. Survivor: cold open scene; Ways (1) one line pointing to it; l.515 cut.
- D4 Kroger extrapolation (non-SMR starts 2034): l.515 and Ways (2) l.521. Survivor: Ways (2).
- D5 Mutually extendable outside date: Tapestry scene l.456, l.515, Ways (3) l.521. Survivor: l.456 scene; Ways (3) one line.
- D6 Blind gauge / denominator: box l.489, l.497, l.515, Ways (5) l.521, listing l.562, l.566. Survivor: l.497 and the ruler box; l.515 becomes one Ines beat; l.562/566 merged and point back.
- D7 Tapestry \$61.1mm "101 in its purest form": cold open l.31, l.159, l.527, table l.532, l.536. Survivor: cold open and table; l.536 deleted; l.527 trimmed.
- D8 Probabilistic duration 2.3: l.509, seesaw box l.511, Full Derivation l.540. Survivor: l.509 (seesaw folded in) with the Full Derivation moved directly below; box retired.
- D9 EA price path (65 to 90, tender near 74, saving over \$250mm): l.338, l.344, l.352, l.364. Survivor: l.344 (Fancourt, Feb. 16); others point to it.
- D10 The four conditions for the put: "When the put matters" l.197, Desk Myth l.378, EA "What the desk could have flagged" l.370. Survivor: EA scene plus Desk Myth; l.197 deleted (Finder row); l.370 folded into the replay's grading.
- D11 Risk-neutral measure: box l.105 and P-vs-Q box l.277, plus Step 6 l.275 and l.513. Survivor: Step 6 text (with the box's 25%/15% numbers); l.105 keeps one sentence; l.277 retired; l.513 points back.
- D12 Informative censoring: Bohn-Stein annotation l.599, ICE scene l.643-645, censoring box l.671, "When the survival toolkit" l.713, listing l.757. Survivor: annotation, ICE scene, merged censoring box; l.713 cut; l.757 one clause.
- D13 Early-termination counts: table l.584-593, ICE scene l.615, Trend Watch l.711, l.713. Survivor: table, Trend Watch (protected), Mags's line; l.713 cut.
- D14 Second Request base rate 41 of 1,944: ICE scene l.631, distributions box l.681, l.713. Survivor: ICE scene.
- D15 Cox multiplier e^-1.2 = 0.30 and 2.1x: l.683, Cox box l.685, l.761. Survivor: one telling in the cause-specific paragraph; l.761 points to it.
- D16 Portability barriers 1.21/1.01 and 81%: box l.406, l.414, l.430. Survivor: box; l.414 and l.430 point to it.
- D17 Spirit: \$425mm prepayments (l.805, l.809), \$1.3bn liquidity and 25 aircraft (l.809, l.813), prearranged RSA supermajority (l.809, l.819). Survivor: l.805 for the prepayments, l.809 for the dated facts; repeats cut.
- D18 WBD consent launch, four issuers listed twice: scene l.825 and "The strip came first" l.845. Survivor: scene; l.845 keeps consents date and 8-K quote.
- D19 WBD "the strip was the credit event": dialogue l.872-874 and "What the desk missed" l.876. Survivor: dialogue, with l.876's hedge folded in.
- D20 WBD loan clause quote "such as the consummation...": l.117 and l.849. Survivor: l.849; l.117 paraphrases with a pointer.
- D21 Cold open three bets: Ines's sizing l.49 and Theo's "three bets" l.55. Survivor: one merged telling before the decision card.
- D22 Syllabus: cold open l.85 (three movements) and l.89 ("By the end of this chapter you will be able to"). Survivor: l.85; l.89 cut (the Finder carries the outcomes).

### (c) Templates (lesson 4) and detached judgment paragraphs (lesson 5)

- l.197 "When the put matters, and when it is decoration" ("Four things have to be true... a seasoned analyst checks the third condition first").
- l.390 "When portability bites, and when it is a footnote" ("Three conditions have to line up... The seasoned check").
- l.515 "When the gauge reads true" ("The first item... The second... The third... a fourth... The check a seasoned hand runs first").
- l.713 "When the survival toolkit earns its keep" ("three conditions... The check a seasoned hand runs first").
- l.821 Spirit: "The judgment the case teaches is about when to trust the mixture" appended after the scene showed it.
- Listing explanations on the U1 template: l.324 (Use it to / The edge case that bites), l.426 (It earns its keep / the wrong tool / The edge case that bites), l.562 (Use it to / The edge case that bites), l.757 (Use it to / The edge case that bites).
- First/Second inside paragraphs: l.328 ("Two things to notice... First... Second"), l.416 ("Two conclusions. First... Second").
- Imperatives in derivations: l.275 ("Never put the two in one formula"), l.233 ("never on the target's pre-deal curve" is fine as a statement; kept).

### (d) Boxes (lesson 6 budget: at most 10, at most one per 1,200 words, never adjacent; lesson 8: no runs over two)

19 Math, Gently against a cap of 10. First load-bearing use belongs elsewhere for: present value and annuity l.235 (Ch 4-B), logistic l.273 (§7-B.3), P vs Q l.277 (Ch 6, §6-B.6), random walk l.281 (§6.1.1), lognormal l.322 (Ch 5, Ch 6), duration seesaw l.511 (duplicate of l.509), survival/hazard l.669 and Cox l.685 (§7-B.4), four distributions l.681 (Ch 5), Bayes l.699 (Ch 1's odds box), jump l.795 (Ch 5 mixtures). Keep: l.105 (trimmed), l.213+l.222 (one box in two parts), l.402 (trimmed), l.489, l.671 (absorbing l.669 as a gloss), l.687, l.857. Target 7.
Adjacent pairs: l.669/671, l.685/687. Runs over two: l.281-291 (Math, Gently, Ways, Veronesi, Schmid: four). l.517-525 is Moyer, Ways, narration, Docket Diary (fine once l.515 shrinks). Seats l.779/781 and l.863/865 are pairs (allowed).

### (e) Research-note leaks and fiction labels

- l.344 "We do not reproduce the tender consideration from the offer documents here; pull them before citing it." (leak; hedge, log open item).
- l.845 "must be checked supplemental indenture by supplemental indenture" (hedge in research voice; recast).
- Resource Graphs l.177, 178, 571, 765, 766, 956, 957: "to be confirmed before linking", "(title-only)", "confirm episodes before linking" (cut placeholders without a title, drop the tags; log in `state/research/ch15_open_items.md`).
- Protected Trend Watch wording left as is and logged: l.171 "(approx.; FY2023 report, not rechecked)" (fact-checker's hedge C4); l.443 "we have not verified their figures for this edition... should be checked against their data before it is quoted".
- Fiction labels missing at the top of: cold open, EA case, Theo's three-prospectus evening (§15.4.1), ICE scene (label only at the end), Spirit scene, WBD case.

### (f) Finder and headings

- No Finder table at the top of §15.9.
- Decision points as bold or bare paragraphs: cold open l.57, EA l.354, ICE l.647, WBD l.843. Promote to `####`. Spirit scene has no heading.

### (g) Cast-bible contradictions

- C1 story clock: cold open (Aug-Dec 2024), §15.4.1 (Mar. 2025), EA (Sept. 2025-Aug. 2026) and WBD (June 2025-May 2026) put Theo on the desk before Day One (22 Sep 2026). Canon: label them replays. Quant-Shop Life l.893 puts "a vice president with a USB stick" on a dealer desk in Dec. 2024 (Theo was at PJT). Debrief l.903 "sticky note from December 13, 2024".
- C5 Mags's career: l.193 "Mags was there" in 1988; canon start 1996: "learned it from people who were there".
- C7 Kaz misread: l.128 "Make-whole. Is that a spa?" is a second misread of a term Ch 4-B owns (insurance); make it a pre-empted callback.
- C8 Kaz pronoun: l.460 "the question he asked".
- C11 Priya: Quant-Shop Life l.883 makes Priya a data engineer (fourth role); rename.

### (h) Relative-value beat

`state/rv_thread.md` does not exist: no item.

## Fix items

- [x] 1. Cold open: replay label at top (C1); merge D21; cut D2 and D22; promote decision point; trim toward 1,500 words. Done: replay label added; timeline, syllabus cut; card promoted; ~1,800 words.
- [x] 2. §15.1.1 box: risk-neutral part to one sentence with a Ch 6 pointer (D11); vary sign-off. Done: risk-neutral cut to one pointer sentence; tiny number kept; sign-off varied.
- [x] 3. §15.1.2: shorten the three-instrument walk; D20 pointer; Kaz make-whole callback (C7). Done: walk cut to one paragraph; WBD quote left to §15.8; callback.
- [x] 4. §15.2.1: delete "When the put matters" (D10, template); Mags RJR to "learned it from people who were there" (C5). Done: template deleted; Mags learned RJR secondhand, started 1996.
- [x] 5. §15.2.2: merge raffle and umbrella boxes into one two-part box; trim Step 2 to the statement. Done: raffle and umbrella now one box; Step 2 is the statement.
- [x] 6. §15.2.2: demote PV/annuity, logistic, P-vs-Q and random-walk boxes to glosses with pointers; Step 6 carries the 25%/15% example (D11). Done: four boxes now glosses in Steps 4-7, numbers kept, pointers added.
- [x] 7. §15.2.2: break the four-box run: move the Schmid extraction under the vintage table; thread narration between Ways and Veronesi. Done: Schmid under vintage table; Kaz line threads Ways and Veronesi.
- [x] 8. §15.2 listing: trim bridge; demote lognormal box; rewrite template and First/Second paragraphs. Done: bridge trimmed; lognormal now a gloss; grid bug told as event.
- [ ] 9. EA case: replay label (C1); D9 and D10 merges; leak at l.344; Hana's ticket; promote decision point; trim.
- [ ] 10. §15.3.1: recast "When portability bites" as a beat at the decision point; keep the podcast references.
- [ ] 11. §15.3.2: trim Phi box; D16 pointers; recast "Two conclusions"; rewrite the Listing 15.2 template; fix lognormal-box pointers.
- [ ] 12. §15.4.1: replay framing for the three-prospectus evening (C1); D1; Kaz pronoun (C8).
- [ ] 13. §15.4.2: fold seesaw box into the duration paragraph and move its Full Derivation below it (D8); cut "When the gauge" to one Ines beat (D3-D6); Ways points to scenes.
- [ ] 14. §15.4.2: D7 (delete l.536, trim l.527).
- [ ] 15. §15.4 listing: rewrite template, merge l.566 (D6).
- [ ] 16. ICE scene: fiction label at top; promote decision point; trim; give Mags the "why is it pending" check (from l.713).
- [ ] 17. §15.5.2: merge survival into the censoring box; demote distributions, Cox and Bayes boxes; delete l.713 (D12-D15).
- [ ] 18. §15.5 listing: trim ROBO repeat; rewrite template; D15 pointer.
- [ ] 19. §15.7: demote jump box into the text; Spirit fiction label; D17 cuts; cut the appended judgment (l.821).
- [ ] 20. §15.8 WBD: replay label (C1); D18, D19; leak at l.845; promote decision point; trim.
- [ ] 21. Quant-Shop Life: rename Priya (C11); remove the USB-stick VP (C1); trim.
- [ ] 22. Desk Debrief: Finder table; replay sticky note (C1).
- [ ] 23. Resource Graphs: remove placeholder notes; log open items in `state/research/ch15_open_items.md`.
- [ ] 24. Cast bible: add the Ch 15 facts and mark C1, C5, C7, C8, C11 resolved for Ch 15.
- [ ] 25. Hygiene: math delimiters, \$ escapes, no code fences, last line; metric "after".
