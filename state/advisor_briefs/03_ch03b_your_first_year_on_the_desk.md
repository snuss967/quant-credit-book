# Advisor Brief — Chapter 3-B: Your First Year on the Desk: The Day, the Week, the Quarter, and the Twelve Mistakes Ex-Bankers Make

**Target file:** `book_src/03_ch03b_your_first_year_on_the_desk.md` · **Target length:** 8,000–11,000 words (hard cap 12k) · **Advisor:** Fable, Edition 2 · **Date:** 2026-10-18

Method note: no web research. Facts come from `state/research/` dossiers (cited by slug) and from existing chapters (cited by §). Anything marked **CHECK** carries no number until verified. Obey `state/style_bible.md` §8: scenes first, Math Gently at first use, View From Another Seat, When to Apply It, three figures into `assets/figures/`, code only in Appendix F with a prose Specification block, specific episodes in the Resource Graph. This chapter is Theo's year on one desk. The five-shop ethnography is Chapter 1-B; the pre-seat plan is `00_02`; the mechanics of information walls are §3.6.3 (expanded). Do not duplicate them; point to them.

---

## 1. Thesis and the "aha"

**Thesis.** A systematic credit desk is run by a calendar, not by ideas. The day, the week, the month and the quarter are clocks, and most of what a first-year analyst does is service a clock on time: the 6:45 feed diff, the 7:15 explain, the 7:30 risk pack, the 3 p.m. snap, the Friday markouts, the month-end evaluated-price true-up, the 20 March and 20 September index rolls. The ex-banker's edge is not that they know more math than the people around them; it is that they already know which clocks have **contracts attached** (grace periods, notice periods, record dates, call dates, RSA milestones, cleansing dates), and the desk's models treat those as features only if someone types them in.

**The aha, in four beats.**
1. *You cannot prove yourself by P&L in year one.* §28.8's standard-error argument, read from the analyst's chair: forty bets at a 55% hit rate carry a standard error of about eight points, larger than the edge. So the first year is played for information, not chips (Ines). You are measured on process artifacts: the Edge Ledger (§3.5), the hand history (§3.3), calibration, and whether your unexplained ever got explained.
2. *The boring parts are the job.* The explain that is off by 40 bp, the CUSIP that changed overnight in an exchange, the vendor file that arrived at 7:02 instead of 6:45, the model review that asks "why is this number different from yesterday?". Each is a scene in this chapter and each is where a desk learns whether a new hire can be trusted with a limit.
3. *The information wall is dated.* Restriction is temporary; the NDA has an outside date and the cleansing 8-K follows it (§3.6.3). A desk can forecast when a name comes back. The ex-banker who spent years on the private side will get this wrong in the opposite direction from everyone else: they will assume everything is MNPI.
4. *The twelve mistakes are all the same mistake.* Each is a banker's object mistaken for a desk's object: a composite for a price, face for JTD, a $\mathbb{Q}$ PD for a $\mathbb{P}$ one, a memo for an Edge Ledger entry. The dictionary in App A §A.10 is the chapter's companion.

---

## 2. Section outline

**Cold Open: 6:47 a.m., Day One (≤400 words).** The security-master diff shows a Halvorsen CUSIP that did not exist yesterday (an exchange closed overnight; the old line is now a stub). The vendor file is twelve minutes late. Ines hands Theo yesterday's explain: "We're down 40 and the model knows about 28. Find the other 12. You have until the risk meeting." Kaz: "I wrote the model. The model is fine." Mags, passing: "Back in my day the explain was a phone call and a grudge." ROBO, asked to "build me a calendar," has subscribed the desk to every U.S. federal holiday and flagged Columbus Day as a credit event. Bold question: *what does this desk actually do all day, and which parts of it can an ex-banker do on Tuesday?*

- **3B.1 The Day as a Timeline.** 6:45 feed diffs and corporate actions (§27.2–27.3); 7:15 explain (→ 8-C); 7:30 risk pack against limits (→ 8-B); 8:30 the pre-open calendar (new issues, calls, tenders, coupon and record dates, month-end index rebalance, CDX roll weeks, FOMC); intraday: the fills loop (§27.4), hedge drift (§8.6), RFQ monitoring (18-B); the 3 p.m. snap (one timestamp for risk and P&L); 4–6 p.m. marks, evaluated-price disputes, EOD risk. **Figure 1:** the day as a timeline with the systems that fire at each hour. **Math, Gently:** what a "snap" is and why two systems with two timestamps produce a fake P&L.
- **3B.2 The Week.** Friday markouts by counterparty and by signal (§3.3); hit ratios and cover gaps (18-B); model monitoring (which asserts fired); the Monday research meeting, where the question is "what did we learn," not "what do we think."
- **3B.3 The Month and the Quarter.** Month-end index rebalance flows (§16.2 as supply); the evaluated-price true-up and the dispute process (8-C §8C.4); the factor review; the CDX/iTraxx roll (20 Mar/20 Sep; 10-B); FOMC; quarter-end BDC marks and redemption-request prints (Ch 17, 17-B). **Figure 2:** the year as four nested clocks.
- **3B.4 Clocks With Contracts Attached.** The ex-banker's native advantage: grace periods (12-B §12B.7), notice periods, record dates and consent deadlines, call and make-whole dates (4-B), RSA milestones and joinder deadlines (§13.5.2), NDA outside dates and cleansing 8-Ks (§3.6.3), 3001(e) transfer notices (§25.8). Each becomes an event-calendar feature in $\lambda^{\mathbb{P}}$ (§18.6.2) and a row in the Edge Ledger with decay "days." Add the two Edge Ledger rows the coach asked for: *model audit* (decay: never) and *process clocks* (decay: days), and the column "time to first compute on the new desk."
- **3B.5 The Wall, as a Scene.** Theo is wall-crossed on Brambleworth for a lender call. The desk stops quoting it. He learns, in order: the restricted list; private-side vs public-side; the "public-only" election; what a big-boy letter does and does not cure; the NDA's outside date; and the morning the cleansing 8-K drops (Item 7.01, both term sheets, the company's projections) and the name reopens. Mechanics are in §3.6.3; this section is the experience of it and the trading point: restriction is a dated interval.
- **3B.6 The Twelve Mistakes.** Each a 300–450-word scene with Theo (or a colleague) and one § pointer: (1) a composite treated as a price (§20.2, 17-B); (2) hedged to face, not JTD (§24.3, §8.6); (3) the long-protection sign (§6.8); (4) a spread parsed as a price (§27.4's gateway bug); (5) researching one name while the book needs breadth (§28.2); (6) exercising the PM option in a drawdown (§28.6); (7) $\mathbb{Q}$ PDs in $\mathbb{P}$ sizing (6-B); (8) retuning in a drawdown (Ch 27 §27.9); (9) raw markouts without stripping beta (§3.3.3); (10) trusting anything called "adjusted" (Mags; §25.3); (11) the wall after years on the private side (3B.5); (12) the 40-page memo where the desk wants five lines (§3.5). The twelfth is the chapter's hinge into 3B.7.
- **3B.7 How You Will Be Measured.** The analyst-side standard-error corollary of §28.8; calibration curves on logged views; correlation of your calls with the price factors (if your alpha is beta, say so); the hit rate with its SE; the Edge Ledger as a daily artifact. **Math, Gently:** the standard error of a hit rate, with the forty-bet number.
- **3B.8 The First Ninety Days on the Seat.** Days 1–30: feeds, security master, the explain and the risk pack as a reader; days 31–60: own one clock (the calendar features) and one dispute; days 61–90: ship one feature through the promotion ladder's first rung (Ch 27 §27.9) and present one hand history. The pre-seat plan is in `00_02`; cross-reference, do not repeat.
- **3B.9 Quant-Shop Life, Two Vignettes.** (a) The reconciliation that does not tie: a custodian cash event with no trade behind it (one sentence on the Citi/Revlon wire, canonical home Ch 27 §27.7). (b) The model review: the risk committee asks why the DTS exposure moved 11% overnight when nothing traded; the answer is a rating migration that re-bucketed forty bonds. Label both as fictional composites.
- **3B.10 When to Apply It, and When It Breaks.** The calendar is a model too: it breaks on holidays that differ by venue, on settlement cycles (T+1 bonds vs T+20 loans; App D), on corporate actions nobody entered, and on the day a bond goes from accrual to flat trading. A Trend Watch (dated, sourced): the FINRA TRACE affiliate-principal indicator, voluntary from 31 Aug 2026 and mandatory 2 Aug 2027 (FINRA Regulatory Notice 26-16; SEC Release No. 105991, 24 Jul 2026), which suppresses the inter-affiliate leg of about 5.7% of 2025 secondary transactions in the economic baseline (SR-FINRA-2026-009 pp. 19–21): a calendar item for every desk that counts prints (`trend_part_v_market_structure_2026`).
- **Specification for AI Implementation: `desk_calendar.py`.** Prose only; code to App F. Inputs: a security master with contract dates (grace, notice, record, call, maturity, consent deadlines), an index calendar (roll dates, rebalance dates), a venue holiday table, settlement conventions per instrument. Outputs: (i) a dated event table per issuer, (ii) event-window features (`days_to_next_contract_event`, `in_cleansing_window`, `in_roll_week`), (iii) an Edge Ledger schema (view, date, horizon, hedge, markout at 1/5/20 days, decay class). Edge cases: holidays by venue; events that move (a consent deadline extended three times); the same CUSIP after an exchange. ROBO's vague version: "build me a calendar" (the Columbus Day credit event).
- **Desk Debrief (scene + 5–8 bullets, Laws tagged).** The explain from the cold open, found: a stale CDX series mark (hand off to 8-C's worked day). Ines: "You found twelve basis points nobody wanted. That is the job for a year." Bullets: "The desk is a calendar with a P&L attached"; "Restriction is an interval, not a state"; "Forty bets measure your hit rate to eight points; log the view, not the P&L" (Law 12); "Which clock has a contract attached? That one is yours" (Law 8); "A snap is a treaty between risk and P&L" (Law 9); "The memo is five lines or it is not read" (Law 11).
- **Exercises (4–6, tagged, with Check:).** E.g., compute the SE of a 55% hit rate on 40 and 400 bets (Check: ≈7.9 pts; ≈2.5 pts); build the event table for Halvorsen from 12-B §12B.9; find the fake P&L created by a 3 p.m. futures settle against a 4 p.m. composite on a given DV01.

---

## 3. Key frameworks and formulas (each gets a Math, Gently box at first use)

**The hit-rate standard error.** With $n$ independent views at hit rate $p$, $\text{SE}(\hat p)=\sqrt{p(1-p)/n}$. At $p=0.55$, $n=40$: $\sqrt{0.2475/40}=0.0787$, about 7.9 points; the edge (5 points over a coin) is inside one standard error. At $n=400$ it is 2.5 points. Corollary for 3B.7: year one is measured on inputs because the output is not yet measurable. Full version: §7.8 (deflated Sharpe) and §28.8.

**The snap identity.** If risk marks a hedge at $t_1$ and P&L marks the bond at $t_2$, the day's explain carries a phantom term $\text{DV01}\cdot(\Delta y_{t_2}-\Delta y_{t_1})$ that is neither alpha nor error. State it once, with a worked number (e.g., a \$50mm DV01-matched hedge and a 4 bp move between 3 and 4 p.m. is \$20k of nothing). Full version: 8-C §8C.3.

**The rebalance band, by intuition.** Rebalancing a hedge whenever DV01 drifts costs transactions; never rebalancing costs variance. The optimal band widens with cost and narrows with volatility, roughly as a cube root (the Whalley–Wilmott shape); the point for 3B.1 is only that "hedge less" (§8.6) has a time dimension: rebalance less, too. Full version: 8-B §8B.10 and §8.6 (expanded).

**Event-window features.** For contract event $k$ at date $T_k$, $x_{k}(t)=\mathbf 1\{0\le T_k-t\le w\}$ and $d_k(t)=\max(T_k-t,0)$; they enter $\lambda^{\mathbb{P}}(t)=\lambda_0\exp(\beta^\top x(t))$ exactly as §18.6.2's event-calendar features. Theo's grace-period clock from 12-B §12B.7 is one such $x_k$.

**Calibration.** For logged views with stated probabilities $q_i$ and outcomes $y_i$, the reliability curve bins $q$ and plots mean $y$; the Brier score $\frac1n\sum(q_i-y_i)^2$ decomposes into calibration and resolution. One picture, one number, no derivation (7-B owns the statistics).

---

## 4. Case studies and real events (canonical homes respected: one sentence plus §, then this chapter's lens)

- **The Citi/Revlon wire, 11 Aug 2020** (canonical home Ch 27 §27.7 after WP5; facts in `case_lmt_autopsies_us_2020_2026` §1: about \$894mm of principal sent by mistake; defendants held \$558.6mm; S.D.N.Y. 16 Feb 2021 for the lenders; 2d Cir. No. 21-487, 8 Sep 2022, reversed). Lens here: the reconciliation break that was a cash receipt with no trade behind it, and why "operations are a position" is a first-year lesson, not a Chapter 27 one.
- **Saks Global, Dec 2024 → 2026** (`case_lmt_autopsies` §8; 11% 2029 notes at 47.5 on 16 May 2025, Debtwire): the clock lesson that "new issue" is not a safe label; a fresh CUSIP arrives on the security master with a runway variable already flashing. Hand the dated timeline to 13-B; keep one paragraph.
- **Incora's one-day closing, 28 Mar 2022** (`case_lmt_autopsies` §4): four steps in one day; the calendar feature is "the amendment and the issuance share a date." One sentence; home is 13-B.
- **The T+1 settlement move (U.S., May 2024; CHECK exact date against App D)** as the day every calendar in the shop was wrong by a day.
- **Fictional, labelled:** Halvorsen's overnight exchange (cold open); Brambleworth's lender call and cleansing 8-K (3B.5); the rating-migration DTS jump (3B.9).

---

## 5. Humor beats with the canon cast

- ROBO's vague version: "build me a calendar" → federal holidays as credit events; later, asked to "remind me before anything important," ROBO pages Theo at 3 a.m. for a Treasury auction.
- Kaz asks whether a "record date" is a vinyl thing, then quietly builds the best event-feature table on the desk and refuses to say where the dates came from (Theo).
- Mags: "A limit is something you breach politely, in writing, before lunch." And on the wall: "I have been restricted on names that no longer exist."
- Ines, poker: "The first year you are playing for information. Chips come later, and only if the hand history says so."
- The Ad Hoc Group files a Rule 2019 statement disclosing its position in the desk's seating chart.
- Theo's USB stick: the 13-week model gets a calendar tab, and the calendar tab is the thing the desk actually uses.
- Running gag maintenance: cooperation-agreement counter stays at 1 (Theo has not signed one yet; he signs in Ch 28). "IDO or it didn't happen" once, in the Debrief.

---

## 6. Cross-references into existing chapters

§3.3 (markouts, the hand history), §3.5 (Edge Ledger; add the two rows and the column), §3.6.3 (walls, expanded: mechanics live there), §5.1.5 and §18.6.2 (13-week model and event features in $\lambda^{\mathbb{P}}$), §7.8 (deflated Sharpe), §8.1 and 8-C (the explain), §8.6 and 8-B (hedge drift, limits), §16.2 (index rebalance as supply), §17.x and 17-B (quarterly marks, redemption requests), 18-B (hit ratios, cover), §20.2 (composite as a prior), §24.3 ($N^{\text{JTD}}$), §25.8 (3001(e) notices), §27.2–27.4 and §27.7 (feeds, security master, OMS, kill switches), Ch 27 §27.9 (promotion ladder), §28.2, §28.6, §28.8, §28.9, 12-B §12B.7 (grace periods), 13-B and §13.5.2 (RSA milestones), 10-B (index rolls), App A §A.10 (dictionary), App D (settlement cycles), App E Laws 8, 9, 11, 12, `00_02` (pre-seat plan), 1-B (the other rooms).

**Resource Graph (specific items; from `media_podcasts_credit_quant`):** Odd Lots, "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (25 Jul 2024); Odd Lots, "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (7 Oct 2024, Dan Morillo); Odd Lots, "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (21 Jun 2025); Capital Allocators, "Jonathan Lewinsohn – Credit Microcycles at Diameter (EP.484)" (2 Feb 2026); Cloud 9fin, "LME Doomscrolling — Just because you can, doesn't mean you should" (31 Aug 2026, Bill Derrough); FINRA Regulatory Notice 26-16 (26 Aug 2026). Add the U3 quant-shop-life accounts when that dossier lands.

**Figures (≥3, scripts into `assets/figures/`):** `ch03b_day_timeline.png` (systems firing by hour), `ch03b_year_clocks.png` (nested clocks), `ch03b_hit_rate_se.png` (SE of the hit rate vs number of views, with the edge as a horizontal line).

<!-- STATUS: COMPLETE -->
