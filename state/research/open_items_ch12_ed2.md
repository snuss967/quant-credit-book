# Open Fact Items: Chapter 12 (Edition 2, U2 narrative revision, 18 Oct 2026)

*Items hedged in, or written around in, `book_src/12_ch12_multi_asset_credit_allocation.md` during the U2 pass. No web calls were made this pass; every fact rests on the dossiers named. Nothing in the book text says "CHECK".*

## Hedged or written around in the text

| # | Fact | Where in Ch 12 | How the text carries it | Source and what to verify |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Blue Owl down "as much as 13%" in the Feb 2026 software sell-off; Ares/KKR/Blackstone/TPG/Apollo vehicles 8–10% | §12.7 The Queue, Beat 3 | "trade press reported" | ACI-SW (*Alternative Credit Investor*, 4 Feb 2026), `trend_private_credit_marks_and_redemptions_2025_2026.md` row "4 Feb–16 Mar 2026" |
| 2 | HPS Corporate Lending Fund Q1 2026 requests about 9% of shares, fill a little over half (54%); Q4 2025 cycle about 4% requested, 100% filled | The Queue, Beats 3–4 and grading | "by the fund's tender filings as we read them"; "our computations" | Dossier rows "Mar–May 2026" and "Jan–Feb 2026", computed from Schedule TO-I/A; verify the HLEND filings |
| 3 | Listed externally managed BDCs, median price-to-book about 0.76 on 16 Oct 2026 | §12.5 "The listed twin" | "by one market-data aggregator's count" | Dossier row "16 Oct 2026" (stockanalysis.com pages); re-pull before print |
| 4 | IMF GFSR (14 Apr 2026): perpetual BDCs meet 5% quarterly redemptions for about 9–11 quarters (mild) and 5–7 (moderate) | The Queue, Beat 4 | Cited to the GFSR directly | Dossier [GFSR-A], ch. 1 PDF; confirm page and wording |
| 5 | Ares non-traded BDC requests about 11% of shares from fewer than 5% of investors (Arougheti, 10 Jun 2026 conference) | §12.7 View From Another Seat (direct lender) | "Press accounts of his remarks" | `perspectives_buyside_credit_managers.md` §2, secondary (TIKR) |
| 6 | Cox Capital \$3.80 bid against OBDC II NAV \$5.57, "about 32% below" | The Queue, Beat 3 | "the \$5.57 net asset value the fund reported at the end of March ... (our computation)" | Dossier row "6 Mar–24 Apr 2026": confirm which NAV date the 31.8% discount should reference, given the \$2.50 return of capital in the same quarter |
| 7 | First Brands: about \$5bn sales, about \$12mm cash, over \$9bn liabilities at filing | The Queue, Beat 1 | "by the figures cited since" | Dossier [SDNY-FB] (Jan 2026 indictment release); first-day declaration would be the cleaner source |
| 8 | Q1 2026 request ratios about 22% (OCIC) and about 40% (OTIC); North Haven Q3 resubmissions nearly two thirds | The Queue, Beat 4 | "our computations from the funds' filings" | Dossier rows "Mar–May 2026", "Sep–Oct 2026" |
| 9 | MarketAxess: dealer prices per US HG RFQ 13.2 → 6.6 on 9 Apr 2025, 11.3 within a week | §12.9 Twenty-Five Days, Beat 4 | Cited "(MarketAxess, July 2025)" | `trend_part_v_market_structure_2026.md` row "2025-04-02 to 04-09" (pub. 2025-07-14) |
| 10 | VIX 52.33 on 8 Apr 2025 as the "highest close of the episode" | Twenty-Five Days, Beat 4 | Stated | FRED VIXCLS; confirm no higher close in March–April 2025 |
| 11 | Constant-mix HY OAS about 377 bp on 15 Oct 2026 at Dec 2024 weights (54 bp of mix) | §12.9 Case Study C | "the desk's computation from the FRED bucket series" | `trend_figure_data_series.md` row "2026-10-15" (author computation, regression-implied weights) |
| 12 | Credit Suisse AT1 write-down announced Sunday 19 March 2023 | §12.0 cold open (Mags) | Stated as background | General record (FINMA, 19 Mar 2023) |

## Corrections to the brief applied in the text

- Box 3 (§12.3): the brief's "z = −2 ... gives −89 bp" has the sign reversed under $\mathbb{E}[\Delta s] = -z\sigma_s(1-e^{-\kappa h})$. The box uses $z = +2$ (300 bp wide), expected change about −89 bp.
- Box 4 (§12.4): the between-regime ("which regime am I in") variance of the 95/5 mixture is 0.96 of 4.35, not 0.91 (0.91 is the stress state's share of it alone). The box says 0.96.
- Item 21 (§12.10): the brief mapped Listing 12.2 to Hana's eigenvalue and 12.4 to the 1.9% → 5.7%. By content, Listing 12.2 is desmoothing and 12.3 is the covariance; the openers follow the content (12.2 ↔ 1.9% → 5.7%, 12.3 ↔ eigenvalue, 12.4 ↔ label swap).
- Item 19 (§12.9): the Ed 1 claim that a target-weight rebalance *sells* public credit when an unmarked sleeve "outperforms" only holds for a risk-budget rebalance (public risk shares rise, the private share falls). The scene makes the sleeve's Monday rebalance a risk-budget rebalance; the answer paragraph's repair now reads "rebalance on desmoothed weights and risk."

## Proposed figures (for U4; none embedded)

The brief's five proposed figures (`ch12_regime_duration_geometric.png`, `ch12_mixture_fat_tail.png`, `ch12_desmoothing_thermometer.png`, `ch12_gate_queue.png`, `ch12_first_brands_to_queue_timeline.png`) were not embedded because the PNGs do not exist yet. The boxes' numbers are the ones those figures should plot: geometric sojourns at $P_{kk}$ = 0.97 and 0.5; mixture 95% N(0.5, 1.5) + 5% N(−4, 5) against N(0.275, 2.09), tails 1.7% vs 0.13% below −6%; AR(1) thermometer at φ = 0.5 and 0.8. The RV figure in `state/rv_thread.md` ("spread per unit of DTS across HY, loans, ETFs, CDX") is also open.

<!-- STATUS: COMPLETE -->
