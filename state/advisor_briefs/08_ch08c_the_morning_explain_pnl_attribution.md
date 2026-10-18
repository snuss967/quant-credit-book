# Advisor Brief — Chapter 8-C: The Morning Explain: P&L Attribution That Foots, From One Bond to the Book to the Signal

**Target file:** `book_src/08_ch08c_the_morning_explain_pnl_attribution.md` · **Target length:** 8,000–10,000 words (hard cap 12k) · **Advisor:** Fable, Edition 2 · **Date:** 2026-10-18

Method note: no web research. Facts come from existing chapters (by §) and from `state/research/case_lmt_autopsies_us_2020_2026.md` §1 (Revlon) and `trend_part_v_market_structure_2026.md`. Prerequisites box: §8.1 (the one-bond decomposition), §8.6 (hedge matrix), 8-B (`risk_model.py`, which this chapter imports), 4-B (accrued, clean/dirty, pull-to-par), §3.3 (markouts), App D (settlement, margin). Ships `pnl_explain.py` via App F and `book_src/lib/`. Obey the Voice Amendments: the chapter is a set of mornings, not a procedures manual.

---

## 1. Thesis and the "aha"

**Thesis.** The explain is the daily markout of the whole book against the risk model. It foots to the official P&L, every line has an owner, and the **unexplained** is the one number nobody is allowed to adjust. §8.1 derived the decomposition for one bond and then said of the production version, "nobody reads it, which is why this section exists," and did not write it. This chapter writes it: by position, by book, by signal, with the hedge legs as their own lines, a tolerance on the residual, an escalation rule, the month-end true-up and the dispute process. The PM's actual question, "which signal made the money?", gets an engine.

**The aha for the ex-banker.** Sources and uses. The explain is a sources-and-uses table for one day of P&L: the custodian supplies the facts (cash, accrual, settlements), the model supplies the forecast (pull-to-par, factor moves, idiosyncratic), and the difference is either a mark that moved for no reason or a trade nobody booked. Product control is the auditor. You have built this table before; it was called a bridge.

**Five beats.** (1) Accrual is certain and pull-to-par is a model; a production explain never puts them on one line. (2) A hedge has its own P&L even though "it's a hedge," and in stress the hedge is the liquidity demand (variation margin) while the bond is not. (3) The foot is an identity, not an estimate; the tolerance is a policy. (4) Attribution by signal has a cross-term, and the honest way to split it is to say how you split it. (5) The unexplained clusters around dates (rolls, month-ends, corporate actions); the explain has its own hand history.

---

## 2. Section outline

**Cold Open: Twelve Basis Points Nobody Wanted (≤400 words).** 7:15 a.m., the book is down 40 bp; the explain (8-B's factors) accounts for 28. Ines gives Theo until the 7:30 risk meeting. Kaz proposes a Kalman filter for the residual. Mags: "The unexplained is the only honest line on the page; don't let anyone *adjust* it." ROBO, asked overnight to "make the unexplained zero," has added a line called *Other* and set it equal to minus the residual: product control's oldest sin, invented on its first day. Theo finds it before 7:30: the CDX HY hedge is marked on yesterday's series; the roll was Friday. Bold question: *what does a P&L explain have to contain before anyone is allowed to believe the number at the bottom?*

- **8C.1 From One Bond to a Book.** §8.1 re-derived with production lines: coupon accrual (custodian) separated from pull-to-par and roll-down (model); rates by key rate (4-B); spread by factor via 8-B's loadings; idiosyncratic; convexity; residual. **Math, Gently:** two reasons a bond's price drifts with nothing happening (accrual you are owed, and a price walking toward par), with a tiny worked number.
- **8C.2 The Hedge Legs.** Each with its own lines: Treasury futures (price, variation margin, roll, CTD switch); CDX (coupon accrual, price, series-roll basis, the 20 Mar/20 Sep roll; 10-B); single-name CDS (the JTD hedge, §24.3); ETF (price-to-NAV basis, §20.2); equity puts (theta is a line). The margin asymmetry: an unfunded bond against margined hedges is a cash call in exactly the stress the hedge was for (App D). **View From Another Seat:** the dealer desk's explain (inventory aging, markouts by tier, 18-B); the direct lender's, where the mark *is* the P&L and arrives quarterly (Ch 17, 17-B); the CLO manager's (par building and OC cushion, §21.4); the insurer's (book yield; the mark barely matters).
- **8C.3 Financing, Fees, FX and Day One.** Repo and borrow (§24.1, App D); commissions and fees; FX for non-dollar lines; new-trade P&L against the composite at trade time (day-one P&L) and why it is reported separately; the 3 p.m. snap shared with risk (8-B §8B.3). **Math, Gently:** the phantom term two timestamps create.
- **8C.4 The Foot.** Official P&L (product control) minus the sum of lines equals the unexplained; a tolerance per book (state one, labelled illustrative, e.g., the smaller of 1 bp of NAV and 5% of 1-day ES); the escalation rule when breached (who is told, by when, what is frozen); the month-end evaluated-price true-up and the dispute process (who may challenge a mark, with what evidence, by what deadline); the explain's own ledger. **Figure 1:** the explain as a waterfall from yesterday's P&L to today's official number, unexplained last.
- **8C.5 Which Signal Made the Money?** Positions as sums of signal sleeves, $w=\sum_s w_s$; signal P&L on IDO returns with issuer netting; the cross-term and how to allocate it (equal split, sequential, or Shapley for two or three signals; say which); the link to §8.8's research ledger (monthly IC) versus this daily production ledger; the warning that a signal's P&L is not its edge until the markout agrees (§3.3). **Math, Gently:** why two signals that both "made money" can sum to less than either.
- **8C.6 Two Worked Mornings.** (a) *The stale CDX mark* (the cold open, step by step: series, roll date, basis line, the corrected explain). (b) *The month-end true-up*: an evaluated price moves three points on a bond that has not traded in nine days; the explain shows a loss with no cause; the dispute is filed with TRACE prints and a composite history; the vendor revises; the P&L moves back; Law 9 in action. **Figure 2:** the two mornings side by side, before and after.
- **8C.7 When to Apply It, and When It Breaks.** Illiquid names (the explain explains a mark, not a price); the default day (accrual stops, the bond trades flat, the CDS hedge waits for the auction; App D); corporate actions (an exchange or CUSIP change shows up as a fake loss and a fake gain; App B §B.16); new issues (no history, no loading; 8-B's rule); the day the agent bank wires you money you are not owed (Revlon, one sentence; see §4). Trend Watch (dated, sourced): the composite as a benchmark asset after ICE's acquisition of MarketAxess (announced 30 Jul 2026, \$167 a share, equity value about \$6.0bn, EV about \$5.7bn; monthly volume releases suspended the same morning; MarketAxess Q2-2026 release) and the TRACE affiliate-principal indicator (voluntary 31 Aug 2026, mandatory 2 Aug 2027; FINRA RN 26-16): both change the provenance of the prices the explain is marked against (`trend_part_v_market_structure_2026`). Cross-reference 17-B's thesis that price became contested.
- **8C.8 The Explain's Own Hand History.** Does the unexplained cluster on roll dates, month-ends, Fridays, specific vendors? A table of unexplained by cause over a quarter; the Edge Ledger row for "found the residual" (3-B). **Figure 3:** unexplained by day over a quarter with roll and month-end dates marked.
- **Specification for AI Implementation: `pnl_explain.py`.** Prose; code to App F. Imports `risk_model.py` (8-B) and `ido_engine` (§8.9). Inputs: positions at $t-1$ and $t$ with provenance-typed marks (traded, composite, evaluated, model; §27.2); custodian cash events (coupons, settlements, fees, margin); hedge legs with their own marks and rolls; factor returns; trade blotter with fill prices and composite-at-trade; FX. Outputs: the explain by position and by book (lines above), the foot and the unexplained with a tolerance flag, signal attribution with issuer netting and the stated cross-term rule, and a dispute file (position, mark, evidence) for breaches. Edge cases: a bond that defaulted overnight (accrual to zero; flat trading); an exchange (old CUSIP out, new CUSIP in, no P&L); a CDX roll (series basis line); a cash event with no trade (flag, never plug). ROBO's vague version: "make the unexplained zero" (the *Other* line).
- **Desk Debrief (scene + 5–8 bullets, Laws tagged).** Ines reads the corrected explain aloud: 28 bp model, 11 bp stale CDX series, 1 bp unexplained, inside tolerance. "That is a hand history. You don't get to redeal the hand, but you do get to know what happened." Bullets: "Accrual is a fact; pull-to-par is a model; never one line" (Law 11); "The hedge has its own P&L, and in stress its own cash call" (Law 6); "The foot is an identity; the tolerance is a policy"; "A mark is a moving average of the truth, and the true-up is where the average catches up" (Law 9); "Which signal made the money is a question with a cross-term; say how you split it" (Law 1); "Never plug" .
- **Exercises (4–6, tagged, with Check:).** Separate accrual from pull-to-par for a 7.25% bond at 92 with 3.2 years to maturity over one day (Check: accrual ≈2.0 bp of price per day; pull-to-par ≈0.7 bp/day linear approximation); compute the phantom term for a \$50mm DV01-matched hedge and a 4 bp move between snaps (Check: ≈\$20k); allocate a cross-term under equal split and Shapley for two signals; write the explain for the day Halvorsen exchanged into a new CUSIP (12-B §12B.9).

---

## 3. Key frameworks and formulas

**The production decomposition.** For position $i$ over one day,
$$\Delta P_i=\underbrace{c_i\,\Delta t}_{\text{accrual (custodian)}}+\underbrace{\theta_i\,\Delta t}_{\text{pull-to-par + roll-down (model)}}-\sum_k\text{DV01}_{ik}\,\Delta y_k-\text{CS01}_i\sum_f\beta_{if}\,\Delta s_f+\tfrac12 C_i(\Delta s_i)^2+\varepsilon_i^{\text{idio}}+u_i,$$
with $c_i$ the coupon rate on face, $\theta_i\approx(100-P_i)/T_i$ plus $-D_i\,[s(T_i-\Delta t)-s(T_i)]$ for roll-down (4-B gives the exact forms), the factor terms from 8-B's loadings, and $u_i$ the residual. Book explain is the sum over $i$ plus the hedge, financing, fee, day-one and FX lines.

**Hedge lines.** Futures: $\Delta F\cdot\text{mult}\cdot n$ (settled daily as variation margin) plus roll and CTD-switch lines; CDX: coupon accrual at the fixed coupon, price change on the current series, and a *series-basis* line equal to (new series − old series) on roll day, from which the cold open's eleven bp come; single-name CDS: upfront change, accrual, and the JTD line on a credit event; ETF: price change split into NAV change and premium/discount change (§20.2).

**The foot.** $\text{P\&L}^{\text{official}}=\sum_{\text{lines}}+U$, with $|U|\le\text{tol}$ a policy, not a model. Breach triggers the escalation (freeze new risk in the affected names until explained; product control and the PM notified by a stated time). Never a plug.

**Signal attribution with a cross-term.** With sleeves $w_s$ and IDO returns $r^{\text{IDO}}$ (§8.8, issuer-netted), $\text{P\&L}=\sum_s w_s^\top r^{\text{IDO}}+\text{(beta P\&L)}$ is linear in sleeves for returns; variance and cost are not, so the daily split is linear and the risk-adjusted split needs a rule. For two signals, Shapley gives each $\tfrac12$ of the interaction; state it in the report header.

**Day-one P&L.** $(P^{\text{composite}}_{\text{trade time}}-P^{\text{fill}})\cdot N$, reported separately because it is a markout at horizon zero (§3.3) and because a composite is a prior, not a price (§20.2, Law 9).

**The phantom term.** Two snaps at $t_1$ (hedge) and $t_2$ (bond): a fake line $\text{DV01}\cdot(\Delta y_{t_2}-\Delta y_{t_1})$; remove it by sharing one snap with 8-B.

**The true-up.** Month-end evaluated price $\hat P$ replaces the composite $\bar P$; the line $(\hat P-\bar P)N$ is reported as "mark change, evaluated vs composite," never as spread or idio; the dispute file carries TRACE prints and the composite history (App B).

---

## 4. Case studies and real events (canonical homes respected)

- **The Citi/Revlon wire, 11 Aug 2020** (canonical home Ch 27 §27.7 after WP5; `case_lmt_autopsies` §1: about \$894mm of principal sent instead of interest; defendants held \$558.6mm; Judge Furman for the lenders on 16 Feb 2021; the Second Circuit, No. 21-487, reversed on 8 Sep 2022 on inquiry notice; rehearing denied 12 Oct 2022). Lens here: on the lenders' side, the morning explain showed a cash event with no trade, on a loan the market priced at 20–30 cents; a flag, not a plug.
- **Hertz effective date, 30 Jun 2021** (canonical §16.6): the day old claims became new equity, cash and warrants in the position file; the explain is all corporate action and no market. One sentence plus §.
- **A CDX HY roll (20 Mar / 20 Sep; 10-B)** as the recurring cause of the cold open's residual; generic, dated by convention, no numbers claimed.
- **The default day, generic:** accrual stops, flat trading, the CDS hedge waits for the auction (App D); illustrate with Halvorsen (fictional) rather than a real issuer unless 13-B supplies a dated bond with TRACE prints (Saks 11% 2029, 47.5 on 16 May 2025, `case_lmt_autopsies` §8, is a candidate once its filing date is in the dossier).
- **Fictional:** the two worked mornings (8C.6); Halvorsen's exchange day (exercise).

---

## 5. Humor beats with the canon cast

- ROBO's vague version: "make the unexplained zero" → the *Other* line. Second attempt, "explain everything," → ROBO produces a 4,000-line report in which every bond's residual is explained by "market."
- Kaz: a Kalman filter for the unexplained; later concedes that "the residual is not a state, it is a mistake," which Ines has framed.
- Mags: deeply suspicious of "adjusted P&L"; "In my day the explain was a phone call, a grudge and a Lotus sheet, and the Lotus sheet was the honest one."
- Ines: the explain is the hand history of the whole book; "you don't get to redeal."
- Theo: sources and uses, on the back of the disclosure statement he still carries.
- The Ad Hoc Group: "We neither confirm nor deny that our mark is stale."
- One "IDO or it didn't happen," in the Debrief; counter unchanged.

---

## 6. Cross-references into existing chapters

§8.1 (keeps the one-bond derivation; gains the accrual/pull-to-par split by reference), §8.6 (hedge matrix: gains the back-reference and the margin asymmetry lives in its expansion), §8.8 (IDO ledger: research vs production), §8.9 (`ido_engine`), 8-B (`risk_model.py`, the snap, the limit sheet), 4-B (accrued, clean/dirty, pull-to-par, duration), §3.3 (markouts; day-one P&L as a horizon-zero markout), §3.5 (Edge Ledger), 3-B (the day; the explain at 7:15), §12.5 (desmoothing stale marks), Ch 17 and 17-B (marks as P&L; price contested), §19.x (composite and basket pricing), §20.2 (NAV and premium/discount), §21.4 (par building, OC), §22.3 (settlement fails as a line), §24.1 (funding leg), §24.3 ($N^{\text{JTD}}$), §27.2–27.4 (provenance types, security master, OMS), §27.7 (Revlon wire, canonical), §28.9 (the P&L panel of the dashboard is this chapter's output), 10-B (index rolls), 18-B (dealer metrics), App B §B.16 (corporate actions, evidence for disputes), App D (settlement, margin, auction), App E Laws 1, 6, 9, 11.

**Resource Graph (specific items):** Odd Lots, "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (25 Jul 2024); Odd Lots, "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (21 Jun 2025); Odd Lots, "What David Barse Learned From Watching A Credit Fund Blow Up" (1 Oct 2018; marks and liquidity mismatch); MarketAxess Q2-2026 earnings release (30 Jul 2026); FINRA Regulatory Notice 26-16 (26 Aug 2026); *Citibank, N.A. v. Brigade Capital Management* (2d Cir. No. 21-487, 8 Sep 2022) by docket; U3's quant-shop-life accounts of product control when that dossier lands.

**Figures (≥3):** `ch08c_explain_waterfall.png`, `ch08c_two_mornings.png`, `ch08c_unexplained_by_day.png`.

<!-- STATUS: COMPLETE -->
