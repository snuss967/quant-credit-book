# Figures log: Chapter 3 (ed2 U4)

Plan: five figures from section 3 of 03_ch03_pjt_rssg_cognitive_bridge.brief.md, in order of appearance. The chapter had no figures before this pass. Script: tools/figures/ch03.py (run: python3 tools/figures/ch03.py).

1. ch03_mixture_vs_gaussian (3.1.2, after the 93%/7% paragraph): the three-scenario mixture against a normal with the same mean and standard deviation.
2. ch03_gm_half_spread (3.2.1, after the "lopsided bond" paragraph): the asymmetric Glosten-Milgrom half-spread against pi and against q, with the Serta point.
3. ch03_hand_replayed (3.3.5, after "The hand, replayed"): Theo's Friday as a waterfall of the winner's five-day markout, raw and IDO.
4. ch03_svb_filings_timeline (3.4, end of the SVB scene): the seven SVB Financial 8-Ks of March 2023 as a one-row-per-event calendar ladder with EDGAR acceptance times.
5. ch03_cusum_detector (3.6.2, after the PRS threshold paragraph): Page's CUSUM on a simulated tranche, two PRS thresholds.
Skipped on purpose: the Serta uptier waterfall (brief idea 6), because Chapter 13 already carries assets/figures/ch13_serta_uptier_waterfall.png.

Data note: tools/figures/data/ch03_svb_8k_filings.csv is the seven March 2023 8-Ks of SVB Financial Group (CIK 719739) from data.sec.gov/submissions (acceptance times converted to New York time); filing text spot-checked against the documents on sec.gov.

## Embedded figures

Pass notes: all five PNGs were opened and checked; label collisions fixed in the mixture figure (spike, mean and normal labels), the SVB timeline (rebuilt as a one-row-per-event ladder after the first stagger layout collided), and the CUSUM figure (alarm labels moved off the event line; the tally is drawn only to a few days past the second alarm). Each embed is one Edit after the paragraph it illustrates, with one short pointer sentence appended to that paragraph; nothing else in the chapter changed.

1. Figure 3.1, ch03_mixture_vs_gaussian (3.1.2, after the 93%/7% paragraph): the mixture (p = 0.55/0.25/0.20, mu = 100/70/45, sigma = 0.5/6/12) against a normal with the same mean 81.5 and sd 22.9. Shows that the mixture's density at 81.5 is 16% of the normal's, 3.5% vs 17% of outcomes within five points of the price, and 21% of the normal's mass above par. Data: Illustrative (the chapter's stated model; numbers computed in tools/figures/ch03.py).
2. Figure 3.2, ch03_gm_half_spread (3.2.1, after the "lopsided bond" paragraph): the asymmetric Glosten-Milgrom half-spread at gap 20, against pi for q = 0.3/0.5/0.7 (q = 0.5 is the symmetric rule (3.1); Serta point q = 0.7, pi = 0.3 gives 2.9 points) and against q for pi = 0.1 and 0.3 (peak near a coin flip, q about 0.52 and 0.58). Data: Illustrative (formula of 3.2.1; asserted against the chapter's 2.9-point Serta and 1.9-point SVB-drill values).
3. Figure 3.3, ch03_hand_replayed (3.3.5, after "The hand, replayed"): a waterfall of the winner's five-day markout in points: +1.25 captured, -0.48 market move, -5.52 issuer-specific, raw -4.75, IDO -4.27 (-498bp), with Theo's counterfactual -4.02 (-470bp). Replaces the brief's t+1/t+5/t+20 path idea, because the chapter fixes only the endpoints (87, 85 3/4, 85 1/2, 81) and a path would invent numbers. Data: Illustrative (the chapter's own hand; asserted against its -0.48, -4.27 and -4.02).
4. Figure 3.4, ch03_svb_filings_timeline (3.4, after the coda's closing paragraph): the seven SVB Financial Group 8-Ks of 8-22 March 2023 at their EDGAR acceptance times (New York time) with items, plus the 9 and 12 March events and the drill (Saturday 11 March, 9:02 a.m. Monday). No price band: the 37-42 / 47-50 / 60 holdco prices are CHECK in the dossier and the chapter does not quote them. Data: Real, SEC EDGAR submissions API for CIK 719739 (tools/figures/data/ch03_svb_8k_filings.csv); the 9 and 12 March events from the chapter's own sources.
5. Figure 3.5, ch03_cusum_detector (3.6.2, after the PRS-threshold paragraph): Page's CUSUM on one simulated tranche (mu1 = sigma_y from day 41, h0 = 6) with the thresholds for PRS 0.9 (h = 3.8, alarm day 47, 7 days in) and PRS 0.1 (h = 8.2, alarm day 53, 13 days in); expected delays 7.6 and 16.4 (Exercise 5). Data: Illustrative (seed 3 qualified at the first try: no false alarm before day 40 at either threshold, delays near expectation).

Observations for the chapter's writer (not acted on; figures pass changes nothing else):
- EDGAR shows the restructuring-committee 8-K (Item 8.01, with Centerview, Sullivan & Cromwell and Alvarez & Marsal named) was accepted at 8:27 a.m. ET on Monday 13 March, 35 minutes before the 9:02 drill, and only the CRO appointment (Item 5.02) at 4:59 p.m. The scene's note says "EDGAR accepted the Item 5.02 filing at 4:59 p.m. ... the drill moves the news to the morning" and describes the committee 8-K as public "for forty minutes (illustrative)"; the true gap for the committee filing is 35 minutes, and the CRO part is the piece the drill pulls forward. Figure 3.4 shows this and its caption says so.
- The chapter's Item 3.01 claim for 17 March checks out against EDGAR (items 1.03, 3.01, 5.02, 9.01 that day); the 22 March 8-K carries Items 2.04 and 7.01, and the 8 March 8-K is Items 7.01 and 9.01 (capital raise announced; the AFS sale itself is in the 14 March Item 2.01).
- The brief's "cooperation agreements signed so far: 1" is still "0" at the Serta counter in the chapter (outside this pass).

<!-- STATUS: COMPLETE -->
