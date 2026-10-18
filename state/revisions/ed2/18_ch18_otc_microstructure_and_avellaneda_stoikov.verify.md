# Verification Report, Edition 2 (U2): Chapter 18

*Verifier, 18 Oct 2026. Chapter: `book_src/18_ch18_otc_microstructure_and_avellaneda_stoikov.md`. Pre-revision text: commit 9ac1c37 (saved to /tmp/pre_18_ch18_otc_microstructure_and_avellaneda_stoikov.md). The revision log carried `<!-- STATUS: COMPLETE -->` before I started.*

## 1. Nothing removed

Checked with python3 (headings, display-math blocks, `[SOURCE EXTRACTION]` blocks, Trend Watch boxes, exercises, `#code-` links, Resource Graph, plus a 5-gram shingle coverage test of every pre-revision line and a sentence-level fuzzy match of the 444 pre sentences).

| Item | Pre | Post | Result |
| :--- | ---: | ---: | :--- |
| Headings | 33 | 42 | Every pre heading present. Seven were demoted or renamed by design (Steps 1-4 became `####` under "The Full Derivation"; 18.6.1 and 18.9.1 retitled). |
| Display-math blocks | 37 | 38 | All 37 pre blocks present verbatim (whitespace-normalised); the new one is the "answer first" spread display. Tags (18.1) to (18.9) each appear once. |
| `[SOURCE EXTRACTION]` | 5 | 5 | Man p.19, Ben Dor p.120 (twice), Dynkin p.702, Ben Dor p.364 n.8. Annotation facts unchanged except the sanctioned last-two-sentences swap on the skew. |
| Trend Watch boxes | 4 | 4 | Diffed character by character. Only sanctioned changes: Tradeweb AiEX hedge; internal-source parentheticals reworded; TwentyFour quote corrected to the page; "CHECK" removed. |
| Exercises | 6 | 6 | Text unchanged; difficulty tags added. |
| `#code-18-1` to `#code-18-7` | 7 | 7 distinct | All present; link wording standardised to the Ch 10 pattern. |
| Desk Myth, Units box, both Poker Tables, four Ways This Blows Up, seven Specs | all | all | Present; Desk Myth, Units, Poker Table boxes are byte-identical. |
| Resource Graph | 1 | 1 | Items differ from the pre commit because the earlier resgraph pass (log `...resgraph.md`, before the writer ran) swapped three generic items (Odd Lots, Flirting with Models, Matt Levine) for specific episodes. That is not a writer deletion; recorded here for the record. |
| Figures | 0 | 5 | Added by the figures pass; all five PNGs exist. |

Dropped on purpose and logged by the writer: "at least \$2bn of Altice-linked debt changed hands the following week" (unverifiable, open item 3), the "more than 40%" AiEX share (hedged), the old Case Study paragraphs (replaced by the two scenes; every number reappears in the scenes or the PB-14 box).

No restoration was needed. One duplication was fixed (see section 4).

## 2. Facts

New factual claims about real events, firms, people, dates, amounts and rulings, with how each was checked. Web budget: 14 of 15 calls used.

| Claim | Checked against | Result |
| :--- | :--- | :--- |
| Altice France results and debt-investor call, Wed 20 March 2024, 14:00 CET (13:00 London); results released 13:00 CET | Altice France call invitation (via search) | Confirmed. The scene's London times (call at 13:00) are right. |
| Leverage 6.2x at end-2023 to a target below 4x; creditors must join "discounted transactions"; €1.3bn first-lien 2027 note down 21 cents to 48, biggest drop since 2020 issuance; a 21 March report put the 21-cent fall on unsecured bonds; some bonds later below 30 | BNN Bloomberg 20 Mar 2024 (search summary), 21 and 26 Mar 2024 pieces | Confirmed; the chapter already reports both series attributions. |
| CreditSights: unsecureds "in freefall" | CreditSights notes (search summaries) | Confirmed at summary level; see doubtful list. |
| Debt fell "about 20 cents"; cooperation agreement formed "that evening"; grew to about 200 institutions, €19bn opco-secured | IFR Awards write-up, fetched | Confirmed verbatim in substance. Added attribution "in IFR's account" and a note that Bloomberg's 21 March report still described a group of funds (about €1.5bn) forming, because other press had the co-op less complete than IFR. |
| Capital structure: about €24bn; €10.9bn secured notes in eleven series 2027-2029; €7.1bn term loans; €4bn AFH unsecured | Dossier `case_lmt_private_and_european_2024_2026` §3 (Elevenflo, IFR) | Matches. |
| Plan implemented 1 Oct 2025: opco 7.6% cash, 77% new secured debt, 31% equity; AFH 2.5% cash, 20% 2033 debt, 14% equity | Same dossier (Paperjam, Delano, Elevenflo) | Matches. Internal filename citation replaced by the public sources. |
| AFH missed interest on 15 May 2025; CDS auction 27 Aug 2025 at 87.75 (12.25 paid); DC found Failure to Pay on AFH notes, no AFH auction | Same dossier (DC-Hold, IFR-CDS) | Matches. Internal filename citation replaced by "IFR on the auction; the Determinations Committee's published decisions". |
| Asquith, Au, Covert, Pathak (2013): 18 to 33 bp (median to mean), 173 bp before and 245 bp after bankruptcy, recallable | Dossier R11 (NBER PDF read in full) | Matches. |
| Credit Suisse: Sunday 19 March 2023, UBS takeover, about CHF 16bn AT1 written to zero, shareholders received UBS shares; BCBS report 5 Oct 2023 | Well-documented public record; dossier `media_episodes...` line 85 | Confirmed. |
| *The Credit Edge*, 23 Mar 2023: "pulling the pin on \$17 billion" | Dossier line 86 (episode description wording) | **Fixed.** The chapter had the hosts "recorded four days later" and "called it"; the page is an episode description. Now "in an episode published four days later, described the takeover as including 'pulling the pin on \$17 billion'". |
| TwentyFour AM, 5 Oct 2022 (Aza Teeuwen): buyers quotes, "almost 10% in euros", "the cost of what liquidity there was increased every few hours...", "...the cash price bid would likely still be in the 80s", "some sellers seemed to have no choice but to sell", €1.5bn and €400m figures, "found the bottom for now" | Post fetched in full | All quotes verbatim. **Fixed** "believed to have traded away" to "possibly traded away" (page: "may have"). |
| Reuters 18 Nov 2022 (Nell Mackenzie): Kleinman "800% above average", Athene \$1.1bn AAA/AA CLOs, biggest discounts at the height of the LDI crisis | Syndicated copies (IBTimes, Investing.com, Euronews via search) plus Creditflux 3 Nov 2022 on the \$1.1bn | Confirmed. |
| Elkamhi and Nozawa (2022, JFE 146): CLO fire sales | Abstract (search) | The abstract confirms constrained CLOs sell CCC-downgraded loans, temporary price fall, overlapping holdings bind together; it does not confirm "OC slack" or "within three months". **Softened** the sentence to what the abstract supports. |
| FINRA Rule 6730: 15-minute rule, hours, "late" versus "as/of", "pattern or practice of late reporting" and Rule 2010 | finra.org rule text, fetched | **Fixed three errors in the §18.8 vignette.** (a) A trade before 8:00 a.m. is reported once TRACE opens the same day, not "after the next open"; the roll to next morning applies to the last 15 minutes before the 6:30 p.m. close. (b) A same-day report that misses 15 minutes is designated "late"; "as/of" is for reports made on a later date. Item four (3:44 p.m. trade keyed at 4:03) now "gone out designated late". (c) The closing sentence now says "each late report and each as/of". The Rule 2010 quotation was correct. |
| FINRA Rule 5310: "regular and rigorous", "at a minimum ... quarterly", security-by-security, type-of-order, firms that do not review each order | finra.org rule text, fetched | Correct. |
| Jefferies' Fred Orlan (The DESK, 26 Oct 2023) two quotes; Dimon, 2025 shareholder letter (6 Apr 2026) quote; Jane Street page quotes (\$900bn, 25,000 bonds, "consistent fixed income liquidity provider...") | Dossier `perspectives_dealers_and_systematic_shops` §5B.5 / §1.3 / §2.2 (fetched 18 Oct 2026); all verbatim | Match word for word. Not re-fetched (budget). Both readings are labelled "ours". |
| Galton 1906/1907 *Nature* "Vox Populi", Plymouth, about 800 tickets, median within 1% | Standard record (1207 vs 1198 lb) | Correct. |
| Mini-Budget Fri 23 Sep 2022; BoE temporary gilt purchases announced Wed 28 Sep, due to end 14 Oct | Standard record; TwentyFour note | Correct. |
| "Altice France's is one of the forty-five Chapter 14 counts for 2024"; counter "still two" | Ch 13 line 1016 and Ch 14 line 582 | Consistent. |
| §18.1 "informed" reading of the co-op | Inference, not a source claim | **Reframed** as Ines's bet ("My bet is that nobody in that group needed a secret...") so no unnamed real creditors are asserted to have read anything. |
| "(approx.; industry dossier)" on the non-bank 10% share | Internal-source phrase | Reworded to "industry estimates". |

Arithmetic re-run by hand and correct: 8 sqrt(5/252) = 1.13; the 0.029-point penalty; Kyle 0.2 points per \$mm; Roll average product -0.01; greed 0.333 and bid 90.895; 94/6 split; GLFT alpha 0.0019, eta 0.735, gap 0.075, horizon 13.4 days, 2.7x tilt; (18.7) at q = 5 gives 2.93 points (1.47 + 1.46); the PB-14 hedge (\$0.70mm against \$0.69mm); the coin-toss means 0.5, 0.75, 0.99; e_3, e_5, e_8; \$1.215mm leak; Poker Table -\$390,000 and -\$360,000.

Real people and dialogue: no real person speaks invented words. The only real voices are Orlan and Dimon (published quotations, exact), Teeuwen (cited note), Kleinman and Union Investments (paraphrased, no quotation marks), Galton. Drahi is not named. Fictional composites are all labelled: Halvorsen (top-of-chapter italic note), the Altice desk, Vantress and Owen's pod, the LDI desk and 38-line list, the Credit Suisse weekend position, the 9:31 page ("A fictional first morning"), Marisol Ochoa's box, every illustrative number.

## 3. Hygiene

Code fences: none in the chapter. Display math: 76 `$$` (balanced). Inline math: no paragraph with an odd `$` count; no math span containing prose or an escaped dollar. Currency: one unescaped `$17 billion` in the Resource Graph, fixed to `\$17 billion`. No `---` lines anywhere. No CHECK strings in the text. Last line is `<!-- STATUS: COMPLETE -->`, preceded by a blank line. Cross-references (§3.2.1, §1.4, §6.1.1, §5.1.1, §5.5.2, §6.2.2, §23.8, §8D.3; the external references to §18.3 to §18.10 from other chapters) all resolve; no other chapter cites the renumbered §18.4.x or §18.9.x subsections. Internal-file citations in book text (`case_lmt_...` twice) removed.

## 4. Fixed in the chapter (small Edits, scripted)

1. Deleted the stale pre-revision "By the end of this chapter you will be able to:" paragraph, which had been left directly under its four-sentence replacement (a duplicate, one line with no blank line between them).
2. Rule 6730 errors in the §18.8 vignette (three places).
3. Credit Edge attribution.
4. Elkamhi and Nozawa softened.
5. TwentyFour "believed" to "possibly".
6. `$17 billion` escaped.
7. Altice co-op attribution to IFR plus Bloomberg's 21 March caveat.
8. §18.1 "informed" line reframed as Ines's bet.
9. Two internal filename citations and one "industry dossier" parenthetical removed.
10. Logged resolutions and new items in `state/research/open_items_ch18_ed2.md` (items 12 to 14).

## 5. What remains doubtful

- **Which Altice series fell 21 points.** BNN reports both the 2027 first-lien and the unsecured; S&P's note has the unsecureds falling from above 70 to near 20, which is a larger move than 21. The chapter hedges and attributes neither exclusively, but the scene's pre-call 69 (secured) and 50 (AFH) are inferences or illustrative and are labelled so. Needs TRACE or MarketAxess data.
- **CreditSights "freefall" and the 8% 2027s' fall** rest on search summaries of CreditSights notes, not the notes.
- **Orlan, Dimon, Jane Street** quotes were matched to the dossier's own fetches, not re-fetched.
- **"Tuesday 4 October" for the EUR 400m day** is inferred from the Wednesday 5 October publication date.
- **Elkamhi and Nozawa magnitudes** unverified (the sentence now claims only what the abstract says).
- **Credit Edge**: only the episode description was seen, not the audio.
- **Unchanged pre-revision claims not re-verified here:** Tradeweb AiEX share (hedged), Coalition Greenwich figures, Bessembinder-Spatt-Venkataraman, SCI \$56bn window, the non-bank 10% revenue share.
- **Story clock (open item 7):** the cold open's 91.25 composite conflicts with Ch 1's 78 if placed after Fri 9 Oct 2026; the orchestrator must date it.
- **Name reuse:** "Marisol Ochoa" (Ch 18 operations analyst) shares a first name with the Ch 11 data engineer Marisol (cast bible lines 126 and 219). Different surname and shop; consider renaming if readers may conflate.
- **Other chapters:** the research file `life_quant_shop_daily_life.md` §2.3 equates late reports with "as/of"; Ch 1-B line 175 ("one late report now flagged as/of") may repeat that and should be checked against Rule 6730 (late versus later-date).

<!-- STATUS: COMPLETE -->
