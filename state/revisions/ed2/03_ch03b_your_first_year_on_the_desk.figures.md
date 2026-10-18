# Figures log: Chapter 3-B (ed2 U4)

Plan (no brief file existed for U4; the advisor brief state/advisor_briefs/03_ch03b_your_first_year_on_the_desk.md names three figures, and the chapter already embeds three captions for them, but none of the three PNGs had ever been drawn: ch03b_day_timeline.png, ch03b_year_clocks.png, ch03b_hit_rate_se.png were broken links). So this pass (a) draws the three missing PNGs exactly as their captions describe, and (b) adds five new figures where the chapter's own mathematics and real events call for a picture. Existing captions keep their text; only the label changes from "Figure 3B.k" to the book's "Figure 3-B.k" form, and the numbers shift to stay in order of appearance.

New figures chosen:
1. ch03b_snap_phantom (3B.1): the two-photograph ghost P&L, one simulated day and the square-root growth with the gap.
2. ch03b_event_windows (3B.4): Halvorsen's contract windows x_k(t) and the intensity they imply, lambda^P(t) = lambda_0 exp(beta' x(t)).
3. ch03b_saks_calendar (3B.4 case study): Saks Global, Dec 2024 to Jun 2026, dates written in advance versus what happened.
4. ch03b_wall_interval (3B.5): Brambleworth's wall as a dated interval, plus the survival curve whose area is the expected restriction (15.5 days).
5. ch03b_jtd_hedge (3B.6, mistake 2): JTD-neutral protection against bond price, and the accidental default bet a face hedge leaves.
Skipped on purpose: settlement-calendar strip for Columbus Day and the 28 May 2024 T+1 switch (3B.10; the listing's own tests already carry it), and beta-stripped markouts (3B.2/mistake 9; the box has the one-line arithmetic).

## Embedded figures

Pass notes: the three PNGs the chapter already linked (day_timeline, year_clocks, hit_rate_se) had never been drawn; they now exist and keep their caption text, relabelled 3B.k -> 3-B.k and renumbered in order of appearance. tools/figures/ch03b.py now reads Listing 3-B.1 from Appendix F (the listing moved out of the chapter); the 2026 FOMC mid-dates for September and October were corrected against federalreserve.gov (15-16 Sep, 27-28 Oct). All eight PNGs were opened and checked; label collisions fixed in event_windows (grace-alone label) and wall_interval (no-deal note).

1. Figure 3-B.1, ch03b_snap_phantom (3B.1, after the phantom-P&L paragraph): left, one simulated day of the 10-year yield with futures marked 3:00 and bond 4:00 (a 4 bp rally between the marks gives phantom +$88,000 on $22,000 DV01); right, phantom standard deviation vs minutes between photographs (square-root rule, $52k at one hour vs $20k straight line). Data: Illustrative random walk; 6 bp/day scale checked against FRED DGS10 (daily sigma 6.2 bp, 15 Oct 2021 to 15 Oct 2026, 1,248 changes; cached tools/figures/data/ch03b_DGS10.csv, re-fetched and matched).
2. Figure 3-B.2, ch03b_day_timeline (3B.1, existing embed): the desk's day, scheduled jobs, intraday loops, after-close work, venue and vendor clocks, the 3:00 snap. Data: Illustrative (times from the chapter).
3. Figure 3-B.3, ch03b_year_clocks (3B.3, existing embed): four nested clocks (day, week, month, year) with the desk's clocks, others' clocks (index rolls, quarter-ends, eight 2026 FOMC meetings) and four contract-clock hands. Data: Illustrative; 2026 FOMC dates from federalreserve.gov/monetarypolicy/fomccalendars.htm.
4. Figure 3-B.4, ch03b_event_windows (3B.4, after the lambda^P paragraph): Halvorsen's four windows x_k(t) and the stepped intensity they imply (4% baseline to 13.3%, 24.2% one-day spike, 29.6%). Data: Illustrative; dates computed with Listing 3-B.1 (Appendix F) from the chapter's Halvorsen dates; only the grace coefficient 1.2 is the chapter's, the others (0.4, 0.6, 0.8) are stated as assumed.
5. Figure 3-B.5, ch03b_saks_calendar (3B.4 case study, after the second-year paragraph): Saks Global, 23 Dec 2024 to 26 Jun 2026, contract clocks vs events vs processes, with a zoom on Dec 2025 to Jan 2026. Data: real dates and the 47.5 quote from state/research/case_lmt_autopsies_us_2020_2026.md section 8 (RSA 2 Apr and plan 5 Jun 2026 from the same section); December interest drawn as the month because the dossier gives no date.
6. Figure 3-B.6, ch03b_wall_interval (3B.5, after the cleansing paragraph): Brambleworth's restriction as an interval (day 0 to day 20, outside date day 30) and the survival curve whose area is the 15.5-day expected restriction; 22% of the time the outside date ends it. Data: Illustrative; the box's exponential model (mean 20 days, H = 30).
7. Figure 3-B.7, ch03b_jtd_hedge (3B.6 mistake 2, after the JTD box): JTD-neutral protection vs bond price (R = 40; 30 and 50 thin) with the face hedge's extra bet, and the face-hedged book's default P&L ($1.2mm at 88, $3.0mm at 70). Data: Illustrative; the box's formula N = (P - R)/(1 - R).
8. Figure 3-B.8, ch03b_hit_rate_se (3B.7, existing embed): SE of a measured hit rate and the +/-2 SE band vs logged views at a true 55%; band spans 39% to 71% at 40 views and clears 50% near 396 views. Data: formula SE = sqrt(p(1-p)/n).

<!-- STATUS: COMPLETE -->
