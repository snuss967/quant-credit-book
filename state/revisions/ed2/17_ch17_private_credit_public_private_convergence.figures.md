# Figures log: Chapter 17 (ed2 U4)

Plan (no brief file existed; figures chosen from the chapter text; sourced data come from state/research/trend_private_credit_marks_and_redemptions_2025_2026.md, which cites EDGAR 10-Q and Schedule TO-I/A filings and the Fed FEDS Note of 16 Oct 2026):
1. ch17_z1_holders (17.1.1): US private-credit loans by holder, Z.1 2023-2025. Source: Brinkman et al. FEDS Note.
2. ch17_smoothing_staircase (17.2.2): simulated true vs marked index, and the pending mark after one shock. Illustrative.
3. ch17_implied_markdown (17.3.2): implied asset markdown vs equity discount at three leverages, with sourced price points.
4. ch17_medallia_marks (17.3.3): one loan, seven BDC marks, Dec 2024 to Jun 2026. Source: BDC 10-Q schedules of investments.
5. ch17_redemption_queue (17.6.2): tender requests vs the 5% cap by fund, Q1 to Q3 2026 (sourced) and the backlog recursion (illustrative).

## Embedded figures

All five drawn by tools/figures/ch17.py; each PNG viewed, label collisions fixed (smoothing end-labels replaced by a legend, implied-markdown labels moved below the curves, Medallia end labels re-anchored, redemption panel titles and key shortened, Z.1 legend reordered to match bar order). All under 125 KB.

- **Figure 17.1, ch17_z1_holders.png** (§17.1.1, after the market-sizing paragraph): US private-credit loans by holder at end 2023/2024/2025 (private debt funds 532.2, BDCs 455.9, rest of world 375.5, interval and tender-offer funds 76.3, MM CLOs 53.7; totals 1,042.6 / 1,253.6 / 1,493.5 $B), with growth multiples since 2023 (BDCs 1.9x, interval 2.2x). Data: Brinkman et al., FEDS Note 16 Oct 2026, Table F4.4.s, via dossier trend_private_credit_marks_and_redemptions_2025_2026.md.
- **Figure 17.2, ch17_smoothing_staircase.png** (§17.2.2, after the "not exotic numbers" paragraph): left, simulated true vs reported index under theta = (0.5, 0.3, 0.2) with two stress quarters; right, a 4% shock recognised as 2.0 / 3.2 / 4.0 with 2.0 and 0.8 still to come (the pending mark of §17.8.3). Data: Illustrative, N(1.8%, 1.2%) true returns, seed 17, shocks -6% and -4%.
- **Figure 17.3, ch17_implied_markdown.png** (§17.3.2, after the Numbers paragraph): implied markdown m vs discount to NAV at leverage 0.6x / 1.1x / 1.6x with phi = 5%, against the 1-for-1 line, with three plotted market points (OBDC 86% of book at 1.19x -> 4.1%; Octus 20% -> 7.1%; Octus 50% -> 21.4%). Data: the chapter's formula (illustrative phi and leverage) plus Blue Owl release 18 Feb 2026 and Octus 16 Apr 2026 as quoted in the chapter.
- **Figure 17.4, ch17_medallia_marks.png** (§17.3.3, after the Octus cross-holder paragraph): Medallia first-lien term loan fair value / par at seven BDCs over six quarter-ends (Dec 2024 to Jun 2026), high-low range 5 to 14 points each date, two camps (49-50 vs 39-41) at Jun 2026. Data: each BDC's 10-Q schedule of investments (EDGAR), via dossier; Monroe June 2026 par change flagged in the caption.
- **Figure 17.5, ch17_redemption_queue.png** (§17.6.2, after "The model mapping" paragraph): left, tender requests as % of shares by fund for Q1-Q3 2026 against the 5% cap with Q2 fill rates (OTIC, OCIC, ADS, ASIF, HLEND, BPCC, BCRED); right, backlog recursion (5% cap, 10% new requests per quarter) showing the fill rate falling 50% -> 13% over eight quarters. Data: left, Schedule TO-I/A filings via dossier (Q3 preliminary; BCRED Q1 omitted because its filing says only "above 5%"); right, Illustrative.

Chapter edits: five embeds, each with one pointer sentence appended to the paragraph it follows; nothing else changed.
<!-- STATUS: COMPLETE -->
