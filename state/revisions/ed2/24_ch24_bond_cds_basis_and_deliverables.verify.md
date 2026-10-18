# Verification report, Edition 2: Ch 24 Bond-to-CDS Basis & Deliverable Obligation Mechanics

Chapter: `book_src/24_ch24_bond_cds_basis_and_deliverables.md` (about 30.3k words after the pass). Pre text: commit 9ac1c379 (saved to /tmp/pre_24_ch24_bond_cds_basis_and_deliverables.md). The revision log carried its completion marker, so the check ran. Web calls used: 8 of 15 (Delphi search, Levine search, Hovnanian 28 Dec 2017 8-K fetch, Windstream DC 21 Dec 2017 decision fetch, Fed/Ford search, SMCCF dates search, Ardagh search, Hovnanian 30 May 2018 8-K fetch). Dossier: `state/research/case_manufactured_credit_events.md` (MCE), `perspectives_dealers_and_systematic_shops.md` 5B.7, `media_episodes_posts_parts_V_VIII.md`.

## 1. Nothing removed

Method: python3 comparison of pre and post (headings, `$$` blocks normalised for whitespace, `[SOURCE EXTRACTION]` lines, Trend Watch lines, Poker Tables, Docket Diary, Spec headings, Appendix F links, URLs, exercises, figures), then a sentence-level pass over every pre line that is not verbatim in post.

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Display-math blocks (`$$`, 24 blocks) | 24 | 24 | all 24 present, content identical; none added |
| [SOURCE EXTRACTION] blocks | 17 | 17 | all 17 lines verbatim |
| Trend Watch boxes | 5 | 5 | 4 verbatim; the 2008/2020/2023 box trimmed as the brief allows (March 2020 narrative moved to Scene A, magnitudes -401/-186 kept in a pointer) |
| Poker Tables / Docket Diary | 2 / 1 | 2 / 1 | verbatim, except the brief's factual corrections to the Diary |
| Spec for AI Implementation blocks | 7 | 7 | headings verbatim, listing links `#code-24-1` to `#code-24-7` all present |
| Exercises 1-6 | 6 | 6 | verbatim (now under `### Exercises`, as the brief directs) |
| Figures 24.1-24.5 | 5 | 5 | captions and PNGs present in `assets/figures/` |
| URLs | 12 | 22 | none lost; 10 added by the Resource Graph upgrade |
| Headings | 30 | 34 | all derivations kept under "The Full Derivation" headings; `## 24.10 Exercises` became `### Exercises` under 24.9 per brief |

The A1-A6 list and the four-bases list became a table and a four-seat scene as briefed; every assumption, formula and the 10-20 bp convention claim survive. Pre sentences that no longer appear verbatim were each located in rewritten form (Docket Diary corrections, Sears paragraph moved to the 24.6 scene, Windstream second act expanded, the three-things-the-transaction-did paragraph carried by Scene B and the dealer/pod seats).

Resource Graph: the U3b upgrade (see `.resgraph.md`) replaced three channel-level pointers with specific items: the generic *Odd Lots* pointer (now a one-line note that no episode was found), the *Petition* pointer (removed, no episode verified), and the generic Levine "columns, 2018" line (replaced by the 17 Nov 2017 column). No URL was lost, so I left that deliberate upgrade in place and did not restore the three generic lines. Say so if you want them back.

## 2. Facts: new claims checked

Verified against the dossier or the web (primary first):

- **Hovnanian 8-K, 28 Dec 2017 (SEC):** subsidiary K. Hovnanian at Sunrise Trail III buys \$26.0mm of the 8% 2019s; the new-notes indenture bars interest on them; \$17.5mm cash termination payment; 5% unsecured term loan maturing on the ninth anniversary of closing; \$125.0mm first-lien revolver. Matches Scene B.
- **Hovnanian 8-K, 30 May 2018 (SEC):** overdue interest originally due 1 May paid 30 May (29 days late); the "Default" cured; stipulation of dismissal with prejudice signed 30 May. The Second Supplemental Indenture amended the indentures for **both** the 13.5% 2026s and the 5% 2040s (the chapter said only the 2040s; fixed). The 8-K does not mention a grace period.
- **Windstream DC decision, 21 Dec 2017 (DC site):** 15 to 0, no Failure to Pay, one-line statement "On the basis of information available"; no reasons given.
- **Delphi (GlobalCapital, Risk.net, American Banker):** filed 8 Oct 2005; auction 3 Nov 2005; 63.375 fixed for index and tranche trades; one report puts CDS at \$27.5bn against \$2.2bn of bonds (another says over \$20bn). The chapter's "by one count" hedge is right.
- **Levine column:** "Blackstone May Do Its Cleverest CDS Trade Again" confirmed by Bloomberg and BloombergQuint pages (17 Nov 2017); the resgraph caveat that the title came only from the URL is now closed. The column compares the plan to GSO's earlier Codere trade, so the Resource Graph sentence is fairly attributed to Levine.
- **Fed, March-April 2020:** PMCCF/SMCCF announced 23 Mar; SMCCF bought ETFs from 12 May and bonds from 16 Jun (NY Fed FAQ and press releases); 9 Apr expansion admitted fallen angels investment grade on 22 Mar; Ford became the largest fallen angel on 25 Mar (PB-03 box).
- **From the dossier (MCE, 5B.7):** LQD "almost 90,000 times" on 12 Mar 2020 and top five holdings 37 trades each (Ramji, iShares, Q1 call 16 Apr 2020); NY Fed terms of assignment to BlackRock FMA 27 Mar 2020; every Sears date, vote, price and dollar figure in the 24.6 scene (45/50 Citi to 59/64 Morgan Stanley, IMM 55.625, \$70.1mm to buy against \$25.1mm to sell, net \$44.9mm, final 79.875, cap floor 54.625, 15-0 / 7-8 / 12-3 votes, 21 Dec panel, \$11.6bn, \$525mm, "40 points above", under \$1mm a day, \$82.5mm Sidley); Hovnanian figures (\$463.7mm cash, 8s near 107, 13.5% 2026s 113.7, 5% 2040s 48.8, 39.5 at 31 Oct 2018, \$90.12mm of 2040s, \$260.5mm Solus, \$333mm GSO, \$170mm / \$133mm arithmetic, Euromoney \$230mm, 0.51% index slot, \$170.226mm tender = 72.14%, \$126.8mm GSO minimum); Windstream calendar (21 Sep, 4 Oct, 7 Dec, 21 Dec 2017; 15, 25, 26, 28 Feb; 6, 11, 13, 19 Mar; 3 Apr 2019; IMM 26.75, final 29.5, \$68.2mm; five 20-March/June/September/December dates in the gap, recomputed).
- **Arithmetic recomputed in python:** 93.3 / 7.2% / 3% replication box; 3.85 and 4.06 annuity, 12.1 lottery, 5.1 points upfront; 95.95 and 50.63 shelf prices; 66 bp carry, 4.4% / 2.4% ROE, 45% equity loss, \$11mm top-up; \$1.04mm = 4% x \$26mm; 35-point subsidy = \$47mm / \$75mm; OU half-life path (-120, -80, -60); toll box (4.69, 2.69, 3.75, 1.75, Sharpe 1.17/0.67/1.88/0.88); PB-03 and PB-11 box sums (\$1.25mm, \$0.75mm, two-thirds; \$14.1mm, \$9.1mm, \$0.55mm); weekday of every dated scene (20, 23, 27, 28, 29 Oct 2026; 12, 20, 23 Mar 2020; 2 Jan 2018; 17 Jan 2019).
- **Cross-references** to Ch 4 s4.6, 5 s5.3.3, 6 s6.1/6.1.4/6.6.3, 6-B.2/6-B.6, 12 s12.3, 20 s20.5, 8 s8.4 all resolve.
- **Fictional composites** are labelled: cold open, Scene A, Sears replay, Scene B, Ruth vignette, the three Pair boxes, the insurer/dealer/pod seats ("generic seat"). No real person speaks invented dialogue: the real people named (Ramji, Levine, Judges Swain and Furman, Arini, GSO, Solus, Aurelius) appear only through documents, headlines or findings. Cast consistent with `state/cast_bible.md` (Theo at PJT in March 2020, Mags at a bank, six years of PJT).

## 2a. Fixed in the chapter

1. Windstream 21 Dec 2017: removed the unsupported reason ("because Windstream disputed the default in court and a committee that reads public text cannot decide a contested question of New York law"); now says the DC gave a one-line statement with no reasons while Windstream disputed the acceleration in court.
2. Scene B outcome: "The company did not default because a trade body and a regulator..." was a causal claim the record cannot support; now "the most plausible reason visible from outside", with a note that the record shows statements and the cure, not motive.
3. Scene B: "before the grace period ran out" replaced by "twenty-nine days late and with the grace period still open" (the 8-K gives the date and the cure, not the grace term).
4. Scene B opening: the jump in the desk's cost of buying protection back is now marked illustrative (the dossier forbids quoting any Hovnanian CDS level).
5. Docket Diary: amendment was to the indentures for the new 2026 **and** 2040 notes, citing the company 8-K.
6. Ardagh: removed "exchanged for equity in a new entity" (only "converted into equity" is sourced) and the gloss "the final price would have to come from somewhere else"; the argument is stated as the sources state it (zero outstanding principal balance, so not deliverable); "had not yet closed on the date of the credit event".
7. Sears: "reference entity for most Sears swaps" became "for the swaps in this auction".
8. Resource Graph: Weinstein career line now attributed to the episode page.
9. Hygiene: two stray `\"` escapes in the Spec for the successor map replaced by plain quotes.

## 3. Hygiene

No code fences anywhere (none are ```text either; the chapter has no diagrams). `$$` count 48, even, every fence paired; no line has an odd number of unescaped `$`; the 30 `$`+digit hits are all inline-math openers (checked), currency is `\$` throughout. No `---` lines. The chapter's last line is its completion marker, present once. Eight Math, Gently boxes, three View From Another Seat boxes, three Pair boxes; no banned template openers remain.

## 4. What remains doubtful

- **Press and secondary figures** carried as hedged: GSO's \$333mm (K&L Gates / Sidley citing press), Euromoney's "\$230 million", Delphi \$27.5bn against \$2.2bn (GlobalCapital), the Sidley quotations on the Sears note sale, Creditflux on Windstream. None is a primary source.
- **Ardagh dissenters:** 9fin and Bloomberg Law report Citi and Pimco dissenting; the DC's own statement was not retrieved, so the chapter still says "with dissents". Bloomberg Law dates the credit trigger differently from the Resource Graph's August 2025 DC meeting; not touched.
- **Not independently re-fetched:** the WHO pandemic declaration (11 Mar 2020), the "before the US open" timing of the 23 Mar Fed release, ESL as Sears's largest shareholder, Hovnanian's CDX HY membership (court's finding, per the dossier), and the clock times in the Sears replay (10:30 a.m. IMM, 2:00 p.m. final), which follow the standard timetable rather than the Sears terms document.
- **Windstream "64%"** is Aurelius's share of the original notes (about \$465mm), not of the notes including the \$553.7mm disputed New Notes; the sentence is loose but not wrong.
- **PB-03 clock:** Ch 8 s8.4 treats PB-03 as a 2020 replay while Ch 8-D (line 41) appears to run a live 2026 pair; Ch 24 follows Ch 8 (open item logged in the cast bible).
- **Calendar crowding (outside this chapter's remit):** Scene A is Fri 23 Oct 2026 at 3:05 p.m.; Ch 19 (cold open, after the close) and Ch 21 (a replay "run on" that day) also sit on 23 Oct. Consider moving one.
- **Resource Graph:** the Weinstein "founded Saba Principal Strategies inside Deutsche Bank in 1998" wording is the episode page's, not independently confirmed; the three removed generic items (see section 1) were replaced on purpose by the U3b upgrade.

<!-- STATUS: COMPLETE -->
