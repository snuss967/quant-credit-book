# Verification report, Edition 2: Chapter 11, Defensive Systematic High Yield

Verifier pass. Pre text: `git show 9ac1c379:book_src/11_ch11_defensive_systematic_high_yield.md` (saved to /tmp/pre_11_ch11_defensive_systematic_high_yield.md). Post text: `book_src/11_ch11_defensive_systematic_high_yield.md`. Revision log carried `<!-- STATUS: COMPLETE -->`; no prior verify file existed.

Note on the baseline: the pre commit (4:25 UTC) predates the figures pass, the Resource Graph pass and the code-mover/explainer pass (U1), so some differences between pre and post are not the writer's: five figures, eight new Resource Graph items, `The full listing is [Listing 11.n in Appendix F]` lines replacing `<!-- EXPLAIN -->` + Code Companion lines, and the longer Specification paragraphs.

## 1. Nothing removed (python3 comparison)

| Item | Pre | Post | Result |
| --- | --- | --- | --- |
| Headings (all levels) | 39 | 47 | none missing; 8 new (4 Full Derivation, 2 Long Scene, 2 Decision point) |
| Display-math blocks (`$$` lines) | 50 (25 blocks) | 50 (25 blocks) | every block present after whitespace normalisation, none new |
| `[SOURCE EXTRACTION]` blocks | 15 | 15 | same 15 (author, page) |
| Trend Watch boxes | 4 mentions | 4 mentions | three boxes (Whipsaw, Soft-Default, Electronic HY) plus one annotation line that names the Trend Watch below; wording unchanged |
| Docket Diary | 1 | 2 | one new reference to it in prose; box intact |
| Ways This Blows Up | 2 | 2 | intact |
| Exercises | 6 | 6 | text identical |
| Appendix F anchors `#code-11-1`..`#code-11-6` | 6 unique | 6 unique | all present (14 mentions) |
| URLs | 24 | 32 | none missing, 8 new (Resource Graph pass) |
| Resource Graph | 25 bullets | 30 bullets | 3 channel-level podcast placeholders replaced by 5 specific episodes and 3 practitioner items by the Resource Graph pass (resgraph.md), not by the writer |

Paragraph-level check: 49 pre lines are no longer verbatim. All were reviewed. Each is either (a) intentionally dying per the brief (objectives paragraph, "Three errors", "Three traps", the "Where the structural PD breaks" paragraph, "three honest exits", "That ranks the defensive toolkit"), (b) split and moved under a "The Full Derivation" heading with the same equations, or (c) reworded with the same numbers. Spot-checked survivors: 784/576 issuers (Dynkin p.651), 47-bond issuer rule, Ben Dor p.104 and p.177, Nuveen 51%/37%, 6.41%/4.20%/+44bp and 5.8%/-9bp, 17.7%, 112bp/14bp/72bp, 31.58%/55.82%, 4.23%/4.28%, Paleologo p.99, Moyer 0.87, Engelmann-Hayden-Tasche credit, Bohn-Stein p.426, "leaving the casino", all present. Nothing needed restoring.

## 2. Facts (new claims versus dossiers and web)

Web calls used: 13 of 15 (TCW episode page; S&P Saks CC/SD search; Retail Dive fetch; IADS fetch, 404; December payment search; August SD search; S&P CLO 2023 search; S&P CLO 2025 search; Saks filing search; Saks plan search; The Fashion Law timeline fetch; DIP terms search; Neiman deal search).

Verified (dossier and/or primary or press source):
- Saks issue terms (23 Dec 2024, $2.7bn EV, $2.2bn 11.000% secured notes due 2029, Jefferies, Latham; Amazon, Authentic, Salesforce as investors); 16 May 2025 at 47.5 and the 51% group (dossier, Debtwire; a vendor indication, labeled as such); 21 Jul and 8 Aug 2025 exchange grid and settlement (dossier, company releases; 98% tendered and the first $300mm confirmed by IADS headline); S&P CCC+ to CC in July 2025 and "tantamount to a default" (Retail TouchPoints, found); S&P SD on 7 Jan 2026 "down from CCC" (Retail Dive, fetched); Chapter 11 on 13 Jan 2026, S.D. Tex., Judge Perez, case 26-90103 (Law360 scorecard 4:26-bk-90103), about $3.4bn debt; RSA 2 Apr with $500mm exit financing, plan confirmed 5 Jun, $20mm litigation trust, juniors owed about $1.5bn, emergence 26 Jun 2026 as Exemplar Luxury Group (The Fashion Law timeline, Reuters via search).
- Weekday checks: 23 Dec 2024 Mon, 16 May 2025 Fri, 21 Jul 2025 Mon, 8 Aug 2025 Fri, 30 Jun 2022 Thu, 22 Jan 2025 Wed, 31 Mar 2025 Mon, 2 Apr Wed, 7 Apr Mon, 15 Oct 2026 Thu, 16 Oct 2026 Fri, 7 Jul 2026 Tue: all correct.
- TCW/Whalen: episode page fetched; "$160 billion fixed-income group has slashed credit risk to the lowest in three decades amid valuation and contagion concerns", "That is the weakest borrower, and they cry uncle first", "your single B borrower is going to feel it next, and then your double B borrowers" are verbatim. The page shows no date; 15 Oct 2026 comes from the media dossier.
- CLO seat: S&P Sep 2023 (554 CLOs, 42% above 7.5%, just over 1% failing junior OC) and Apr 2025 vintage numbers (2.76%/7.08% versus 3.94%/5.70%) found on S&P pages by search; Kundu (ESRB WP 141: 85 versus 58) and Elkamhi-Nozawa (JFE 146) from the dossier's primary reads.
- Insurer seat: NAIC June 2026 C-1 factors, 11.77% surcharge on BSL tranches 4% thick or thinner, effective YE2026 (dossier trend_insurance_capital_forced_flow.md S14 and perspectives file; Sidley 9 Jul 2026).
- Moody's 46% re-default and 70% inside 24 months (dossier, Bloomberg Law 23 Apr 2025; Moody's 18 May 2026).
- Tariff scene: FRED closes (259, 355, 445, 461, 306, 486, 1,137, 120), VIX 46.98 and 52.33, HYG -0.66% and +1.49%, +0.135% mean over 448 days, TRACE $62.1bn versus $77.2bn and ATS 5.8% versus 7.4%, implied index weights 53.4/34.0/12.6 and 60.1/31.8/8.1, 377bp versus 323bp, HYG CCC 7.35%: all in trend_figure_data_series.md. Tariff announcement (2 Apr after close) and 90-day pause (9 Apr afternoon) are public record.
- Arithmetic re-computed and correct: mixture mean 1.40% and skew -5.5; 300/180/120bp; 2.4bp/month and 29bp/year; kink numbers (+0.28%, -0.25%, -0.20%); 196/84/36 paths and 8-point drag; sigma_V = 25%; 0.003% versus about 1%; 0.997^12 = 3.5%; odds shift 6.5%; 34/40 = 0.85 and AR 0.70; 23/200 = 11.5%, 23/400 = 5.8%; 4.3% and 7.7% break-evens; z = 0.58 and multiplier 1.29 capped 1.2; PB-01 DTS sizing ($19mm MV, $26mm face, $33.6mm, $8.8mm, $0.44mm friction).
- Code claims in the Specifications: Listing 11.2 re-run in a clean directory prints V = 4,016, sigma_V = 0.275, DD 2.44, 4.562% versus 0.738%, and a 2% stale sigma_E gives DD 71.2 and the 1bp floor, as the text says. Listings 11.1 and 11.3 to 11.6 were started together but did not finish inside the time limit (heavy simulation), so the AR 0.773, hit-rate, clustering 2.8x, AUC 0.89 and capacity ($1.2bn/$49bn) statements are not re-verified here.

Fixed in the chapter:
1. Beat 4 of the Saks scene said about $126mm of December interest went unpaid. Bloomberg Law and the other press accounts say "more than $100 million" due 30 December; $126mm is a single secondary case summary. Now "more than $100mm ... (Bloomberg Law, as reported; one case summary puts the figure at $126mm)".
2. DIP description said "$1.75bn DIP, $1bn new-money first-out at SOFR plus 11%, paid in kind". Press accounts disagree on the tranche split and none found confirms the pricing. Now "about $1.75bn of financing commitments, most of it from an ad hoc group of senior secured bondholders (press accounts differ on the split into tranches and on the pricing)".
3. Date arithmetic: Theo's label (21 Jul 2025) was said to fire "eight months before the courtroom"; it is almost six (13 Jan 2026). Fixed.
4. S&P SD source for 7 Jan 2026 switched from Bondoro to Retail Dive (fetched, "down from CCC").
5. S&P's August 2025 SD could not be dated; now "Around the settlement S&P moved the issuer to selective default (as WWD reported in August 2025)".
6. Equity holders list (HBC, Amazon, Authentic, G-III) not named in the sources fetched; now "the old equity, the 2024 investors' included, cancelled".
7. Kaz's trade grading implied his held bond shared the $20mm junior trust; the trust belongs to unsecured juniors. Reworded: a holder who simply held ended with a stripped note under everything new, in a case where even the juniors got a $20mm trust.
8. Theo's line "In 2026 it'll be four bankruptcy claims" leaked the future into a tape cut at 8 Aug 2025; now "If this ends in a courtroom, it's four bankruptcy claims."
9. "A downgrade to CCC can hit four at once" (unsourced count) softened to "several".
10. Kaz's "few basis points a year" overlay cost marked *(illustrative)*.

Real people and invented speech: the only real person quoted is Bryan Whalen (verbatim from the episode page). Judge Alfredo Perez, Saks and the named bondholders, advisers and investors appear only in narrated facts; the scene label says nobody outside the desk is given a word. The Ad Hoc Group lines are the book's standing gag with an unnamed, generic group (pre-existing wording). All dialogue casts (Theo, Ines, Kaz, Mags, Marisol, Dov, the risk-committee chair, the vendor reps, the consultant) are labeled fictional or composite at the scene or box head.

## 3. Hygiene

- Code fences: none in the chapter (no ```text diagrams either). Pass.
- `$$` count 50 (even); every paragraph has an even number of unescaped `$` after removing display blocks; `\left` 6, `\right` 6. Pass.
- Currency: all dollar amounts are `\$`; no inline math span contains words or bn/mm outside \text. Pass.
- No `---` line anywhere. Pass.
- Last line is `<!-- STATUS: COMPLETE -->`. Pass.
- No CHECK, TODO or TBD in book text. Pass.
- Box discipline: 34 quoted blocks, none adjacent without narration; 9 Math, Gently boxes (item 19's box is the one-sentence pointer to §4.8, as the log says); 3 View From Another Seat boxes; 1 labeled vignette. Pass.

## What remains doubtful

- Issue price and rating at issue of the Saks notes: not stated in the chapter (open_items.md item 1); fine.
- Saks plan class details (the "crammed down" old-notes class) and the roughly $51mm left outside come from an AI-assisted case tracker; both are hedged as "by the case trackers' accounts" / "Case trackers put".
- The 47.5 quote is a Debtwire indication read through a dossier; no independent price source (labeled "not a TRACE print").
- Exact date of S&P's August 2025 SD action not confirmed.
- TCW episode date (15 Oct 2026) rests on the media dossier; the page shows no date.
- Chapter 3-B (line 161) also states "about $126mm of interest went unpaid" in December 2025; should be harmonised to "more than $100mm" by whoever owns Ch 3-B.
- Brookfield, Fridson, Seix, Marks and other Resource Graph items were added by the Resource Graph pass from the media dossier (each URL reported HTTP 200 there); not re-fetched here.
- Python listings 11.1 and 11.3 to 11.6 not re-run to completion.

<!-- STATUS: COMPLETE -->
