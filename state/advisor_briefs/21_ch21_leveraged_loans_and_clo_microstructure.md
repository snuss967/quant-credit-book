# Advisor Brief — Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure (TREND)

**Target file:** `book_src/21_ch21_leveraged_loans_and_clo_microstructure.md` (7,000–10,000 words)
**Advisor:** Fable, Edition 1 editorial board. Research date: 2026-10-17.
**TOC scope:** Loan settlement, CLO constraints (CCC buckets, OC/IC tests), loan and CLO ETFs, repricing waves, and loan e-trading.
**Status key:** VERIFIED = fetched or read this session; SEARCH-LISTED = URL appeared in a search result but the page was not fetched; CHECK = plausible but unconfirmed, do not state as fact without a source.
**Neighbors:** Ch 20 owns ETF creation/redemption mechanics and March 2020 (BKLN settlement mismatch is flagged there; this chapter owns the loan-side *cause*). Ch 22 owns T+1 for securities and regulation. Ch 13–14 own LMT game theory and the default/recovery cycle; this chapter owns the *CLO constraint* channel through which LMTs and downgrades move loan prices. Ch 12 owns the Nuveen allocation framework; this chapter supplies the loan and CLO-tranche inputs it consumes.

---

## 1. Thesis and the "aha"

**Thesis.** The leveraged loan market is the one corner of credit where the *holder's rulebook*, not the borrower's fundamentals, sets the marginal price. About two-thirds of the ~$1.5tn Morningstar/LSTA index sits inside CLOs whose indentures convert ratings and prices into mandatory trades through piecewise tests (the 7.5% CCC bucket, OC haircuts on defaulted and discount obligations). The loan itself is a floating-rate note the borrower can call at par after a six-month 101 soft call, so its price lives under a ceiling. And the plumbing is two decades behind bonds: median settlement around T+20 against bonds' T+1, no TRACE, prices that are dealer-composite marks rather than prints. Put those three facts together and loan prices carry three structural signatures a systematic desk can model and trade: a **ceiling** near 100.5 that truncates upside momentum and turns every rally into a repricing wave; a **cliff** at the CCC bucket that turns a one-notch downgrade of one borrower into a market-wide forced sale of *other* borrowers; and a **settlement lag** that makes every daily-liquid loan vehicle a liquidity-transformation machine whose exchange price is the only real-time print in the asset class.

**Four "aha" moments for the ex-RSSG reader:**

1. **The OC test is not a ratio; it is an option book written by the CLO equity.** Adjusted collateral par is par minus a sum of haircuts, each piecewise-linear in a loan's price or rating (`Schmid p.176` gives the clean ratio; the Creditflux guide and Kundu 2023 give the modern haircut rules). Once the CCC bucket is full, the next downgrade marks the *cheapest* CCC loan from par to market. The cure is mechanical: sell the CCC loan with the *highest* price, buy a B at par, and the lowest-priced CCC climbs back into the bucket at par. Because the cure is deterministic, the flow is predictable, and predictable flow is a factor. Elkamhi–Nozawa (JFE 2022) measure it: loans widely held by constrained CLOs earn 3.4% lower cumulative abnormal returns around downgrade weeks, the price impact is temporary, and the median CLO sits within a few percent of its most binding test (Kundu: within 4%). The RSSG reader already knows these indentures as "the reason the CLOs can't fund the new money"; the chapter turns that into $\partial(\text{OC})/\partial(\text{price})$.

2. **A par loan is a short call struck at 100.** With soft-call protection of 101 for six months, the borrower reprices the moment the loan trades through par and the protection lapses, cutting 40–53 bp of margin (2024 wave: $756.8bn repriced; 2025: $503.6bn). So $P_t \approx \min(\text{PV of the floater}, 100 + \text{call premium}_t)$, the return distribution of a performing loan is left-skewed by construction, and "trend" in loans is asymmetric: winner momentum is capped at the ceiling while loser momentum is amplified by the CLO cliff. Beyhaghi–Ehsani (RAPS 2017) find exactly this: a 122 bp/month momentum premium concentrated in the lowest-rated loans. The 2022 experience is the same fact from the other side: total return −0.6% while the price component was −6.2%, because carry is most of a loan's return and price is a bounded nuisance until it isn't.

3. **Liquidity moved up the capital stack.** Retail money did not leave loans; it left the *loan* and bought the *tranche*. Bank-loan mutual funds shrank 21% to $71bn (2019–2025), BKLN and SRLN together hold about $12bn, while CLO ETFs passed $50bn in mid-2026 with JAAA alone above $30bn. The reason is settlement: a loan settles in ~20 days, a CLO note settles like a bond, so a AAA CLO ETF can redeem in kind and a loan ETF cannot. April 2025 was the live test: JAAA traded >1% below NAV on 2025-04-04, lost ~$600mm in a day, and had $850mm back by May, almost all in-kind. The chapter derives the liquidity buffer a loan fund needs as a queue with service time equal to settlement time; that queue is why the SEC's 2022 proposal to call loans "illiquid" would, in the LSTA's words, have "effectively shut down open-end loan funds."

4. **The CLO rulebook is the hidden player in every LMT.** Who can fund new money, who cannot hold equity or a long-dated reinstated loan, who gets "snooze-dragged" into an extension: these are CLO indenture terms (Weil, May 2024). The ex-RSSG reader built uptier math on the other side of this table; the systematic desk should carry the CLO share of each tranche's holder base as a state variable in the Priming Risk Score (Ch 13), because a tranche held 70% by CLOs with full CCC buckets has a different non-pro-rata equilibrium from one held by three hedge funds.

**The PJT bridge in one line:** at RSSG you asked "what does the credit agreement say?"; on this desk you also ask "what does the *CLO indenture* say?", because the second document decides who is a forced seller of the first.

**The trend arc the chapter must carry (2018–2026):** loans went from a bank-and-fund asset class to a CLO-and-ETF asset class (CLO share ~50% in 2018 per the Fed, ~65% by 2025); settlement barely moved (T+12 → T+9 medians after 2016; a 10-year par average near 20 days) while e-trading finally arrived (Octaura from zero in April 2023 to 6.4% share in July 2025; secondary volume a record $971bn in 2025, trailing-12-month volume above $1tn in Q1 2026); the loan's economics were rewritten by LIBOR's end (June 2023) and then stripped by the 2024–2025 repricing wave; and private credit became a two-way refinancing partner (>$30bn each way in 2025). Every section should say which of these it is riding.

## 2. Section outline, anatomy mapping, Trend Watch boxes

Legend: **DF** desk framing · **DER** derivation · **SPEC** AI-coder spec · **SRC** source extraction · **CASE** case study · **RG** resource graph (close every major section) · **TW** Trend Watch. Target 7,000–10,000 words; the derivation sections (21.4, 21.5, 21.6) carry the weight.

**Cold open (≤400 words).** Mags hands Theo a trade ticket dated 23 business days ago: a $7mm piece of a B2 term loan B they *bought* and that still has not settled; the agent bank wants a $3,500 transfer fee and the KYC packet again. Ines asks what the loan is "worth" today when nothing has printed since the trade. Kaz: "It's a floating-rate bond with a slightly odd call; I'll have a price in ten minutes." Theo: "It's a loan. Nobody has a price. There's a mark." Then the Bloomberg headline: 62% of the index bid above par and three repricings launched before lunch. Question the chapter answers: *who sets the price of a loan when two-thirds of its holders cannot choose what they buy, the borrower can call it at par, and the trade settles in three weeks?*

"By the end of this chapter you will be able to..." price a loan as a capped floater, compute an OC test with haircuts and the cure trade, size a loan fund's liquidity buffer, build the CLO forced-sale and repricing-hazard signals, and read a CLO indenture the way you used to read a credit agreement.

- **21.1 The leveraged loan as an instrument (DF, DER, SRC).** Floating over SOFR + margin (+ CSA), secured, cov-lite (>90% of the index), callable at par with 101 soft call for six months, amortizing 1%; return decomposition $r = \text{carry} + \Delta P$ with 2022 as the worked example (−0.6% total, −6.2% price). Loan vs bond: duration ≈ reset period, spread duration ≈ bond, negative convexity from the call. `Nuveen p.6`, `p.9` for how an allocator treats the sleeve. **TW #1 "From bank asset to CLO asset, 2018–2026":** index ~$1.0tn (2018) → ~$1.5tn (2025); CLO share ~50% → ~65%; bank-loan mutual funds $90bn → $71bn; cov-lite >90%; LIBOR cessation 2023-06-30 and the CSA; private credit two-way takeouts (>$30bn each way, 2025).
- **21.2 Plumbing: settlement, marks, and the arrival of e-trading (DF, DER, SRC, TW).** No TRACE; marks from LSTA/LSEG MTM and Markit composites (`Man_Quantitative p.41` on 6,500 facilities); bid-ask 72 bp mean / 50 bp median (June 2025); turnover 65%; settlement conventions (T+7 par, T+20 distressed, delayed comp) vs reality (`Moyer p.322`; 2016 T+12 → T+9; "10-year average 20 days"); the economics of delayed compensation as a funding transfer (D5); Octaura, Versana (CHECK), BWICs with 14,000 dealer responses. **TW #2 "Settlement and e-trading, 2004–2026":** T+10/T+30 (Moyer 2004) → T+12/T+9 (2016) → ~20 days (2015–2025 average) while bonds went T+3 → T+2 (2017) → T+1 (2024); Octaura 0% (Apr 2023) → 4.6% (Q1 2025) → 6.4% (Jul 2025); secondary volume $824bn (2022) → $971bn (2025) → LTM >$1tn (Q1 2026).
- **21.3 CLO anatomy and the arbitrage (DF, DER, SRC).** Stack (AAA 60–63% ... equity 8–10%), reinvestment 4–5y, non-call ~2y; the arbitrage $\text{WAS} - \text{WACC} - \text{EL} - \text{fees}$ geared ~10× to equity; `Moyer p.53–54` 2004 numbers (535 bp collateral, ~110 bp blended funding) vs 2025 (B− new-issue spread 354 bp, AAA mid-120s); why a 50 bp repricing costs equity ~5%; Moody's BET and the diversity score (`Schmid p.183–184`) as the reason all CLOs own the same 200 names; issuance records (2024 $202bn / 2025 $209bn new issue; resets $223bn / $232bn) and "near-anaemic" net supply.
- **21.4 The tests as an option book (DER, SPEC, SRC, CASE, Ways This Blows Up).** OC/IC definitions (`Schmid p.175–176`), the modern numerator with four haircuts (Academy: ZAIS6 2017-1A, 5.72% total haircut), the CCC cliff, the cure-trade ordering theorem (D2), interest diversion, maintain-or-improve; Loumioti–Vasvari on manipulation; Elkamhi–Nozawa and Kundu magnitudes; the **CLO Forced-Sale Pressure Index** signal. Case: COVID 2020 (CCC 12.31%, junior cushion 1.13%) and the 2022–2023 junior-test failures (42 deals). *Desk Myth vs Desk Reality:* "CLOs are buy-and-hold." *Poker Table:* Ines on knowing which seat at the table *must* fold.
- **21.5 Repricing waves (DER, SPEC, SRC, CASE, TW).** The loan as a capped floater (D3); repricing hazard as a function of price-over-par, soft-call expiry, spread tightness and arranger incentives; the CSA strip; CLO equity's exposure; expected-loss-of-carry signal. **TW #3 "The repricing machine, 2021–2026":** 2024 $756.8bn repriced (institutional volume incl. repricings ~$1.4tn), Jan 2025 record $215bn month, Q2 2025 trough $28.5bn, FY2025 $503.6bn, June 2025 above-par share 37% vs 8% in April; banks offering to do deals for free (Jan 2025). Case: the January–April 2025 round trip.
- **21.6 Loan ETFs vs CLO ETFs: liquidity transformation (DER, SPEC, CASE).** Cross-reference Ch 20 for AP mechanics; here the loan-side cause: a buffer-queue model (D4) with service time = settlement time; cash vs in-kind redemption; why JAAA can and BKLN cannot; SEC 2022 proposal and the 15% illiquid cap; Fed FEDS (2026-08-19) on bank-loan fund liquidity ratios 10% → 4.5%. Case: JAAA, April–May 2025. *Ways This Blows Up:* a loan ETF in a T+20 market during a 25%-of-NAV outflow week.
- **21.7 Trend and momentum in loans (DER, SPEC, SRC).** Beyhaghi–Ehsani; stale-mark autocorrelation and the Dimson-style correction (D6); asymmetric momentum under the ceiling; equity → loan lead–lag (cross-ref Ch 10); CLO-flow-driven momentum; capacity given 65% turnover and 72 bp bid-ask. `Man_Quantitative p.41` for the data problem.
- **21.8 CLOs inside the LMT (DF, SRC, CASE, Docket Diary).** What a CLO can and cannot do in a restructuring (Weil: >90% senior secured, CCC 7.5%, PIK bucket ≤5%, long-dated bucket 2.5–7.5%, fixed-rate bucket 10–15%, loss-mitigation loans, snooze-drag); implications for ad hoc group formation, non-pro-rata uptiers and cooperation agreements (increment the counter once); the CLO-share state variable for the PRS (Ch 13). Case: Serta's holder base (cross-ref Ch 13–14 dossier facts) and a 2024–2025 "CLO-friendly" LME structure (CHECK for a sourced example; otherwise keep generic).
- **21.9 Desk Debrief, The Spec You Hand the Robot (the OC-test and repricing engine), exercises.**

Anatomy coverage check: DF in 21.1/21.2/21.4/21.8; DER in 21.1–21.7; SPEC in 21.4/21.5/21.6/21.7 (one consolidated code block, see §4); SRC in every section from the source map (§5); CASE in 21.4/21.5/21.6/21.8; RG at the end of 21.2, 21.4, 21.6, 21.8 and the chapter; three TW boxes (minimum two).

## 3. Derivation skeletons

(pending)

## 4. Code spec and sanity check

(pending)

## 5. Source map (shelf pages, exact quotations)

(pending)

## 6. RESEARCH DOSSIER (dated, sourced; CHECK = unconfirmed)

Facts are appended in the order found; the writer should cite the source column, not this brief. Shelf citations are `book_id p.N` as printed by `tools/pdf_search.py`.

### 6.0 Shelf facts (VERIFIED, read this session)

| Source | Fact | Use |
| :-- | :-- | :-- |
| `Schmid p.175` | Two coverage tests "intended as a warning if the cash flows from the collateral pool are running short"; on failure "the cash flows from the collateral are redirected... to repay the outstandings on the tranches according to their seniority." OC test "is done for every single tranche but the equity tranche." | Definition of OC/IC and the cash-diversion consequence. |
| `Schmid p.176` | OC ratio for senior tranche A = par value of collateral pool / par value of tranche A; for B = pool par / (A+B); test fails if ratio < lower boundary. IC ratio = (expected interest from pool over 1 year − annual fees) / expected interest to tranche(s). | The textbook formula the chapter upgrades with CCC haircuts, defaulted-asset haircuts and discount-purchase rules. |
| `Schmid p.177` | S&P CDO surveillance (2002): top-decile vs bottom-decile managers held 0.10% vs 13.91% defaulted securities; net sales losses 0.02% vs 1.29%; recoveries 49.49% vs 2.55%. "The quality of the collateral manager is one of the most important but unfortunately only badly predictable factors." | Manager dispersion is old news; ties to Cordell–Roberts–Schwert (2023). |
| `Schmid p.178` | S&P Arbitrage CLO Index introduced Aug 2001, data from April 2000; tracks sales of "credit risk," "credit improved," "defaulted," and "discretionary" collateral, and "average senior overcollateralization ratio test spread." | The four sale categories are still the indenture's vocabulary. |
| `Moyer p.53–54` | CDOs "frequently face purchase and sale pressures not driven by return maximization"; debt finances "85–90% of the purchase"; worked example: collateral spread 535 bp, IG tranches 87% at ~88 bp, BB/B at 750 bp, blended ~110 bp, net spread ~425 bp to a 10% equity. | The CLO arbitrage, 2004 vintage numbers; contrast with 2024–2025 AAA ~130–150 bp (see 6.x). |
| `Moyer p.55` | CDOs held ~3% of low-rated loan and bond market in 1993 rising to "over 20%" by 2003 (CSFB/LPC chart). "CDO-ORs typically limit the percentage of the CDO's portfolio that can be rated in the lowest rating categories. When an investment... is downgraded to B– or CCC, the manager may be forced to sell something." | The forced-seller thesis, written in 2004; today's CLO share is ~2/3 of the market. |
| `Moyer p.322` | Bonds settle T+3 (2004); par loans "typically is 10 days (T+10), but modest delays are common"; distressed convention 30 days "but delays (sometimes of up to 120 days) are fairly common"; agent transfer fee "$2500–$5000"; loan holders identifiable from amendment signature pages. | Settlement baseline for the Trend Watch; bonds are now T+1 (Ch 22) and loans are still ~T+20. |
| `Moyer p.150` | Lender's ability to act depends on whether the agent "has syndicated the loan to other participants (particularly collateralized loan obligations) or if the loan has changed hands." | Holder composition as a state variable (CLO share of a tranche → LMT dynamics, Ch 13). |
| `Bohn_Stein p.14` | Duffie's June 2008 foreword: "by mid-2008 the issuance of bank-loan collateralized loan obligations (CLOs) has fallen off significantly"; CLOs are "well suited to transferring credit risk... to buy-and-hold investors who are less crucial to the provision of liquidity." | The 2008 trough that frames the 2012–2025 rebuild. |
| `Bohn_Stein p.42` | "The draining of liquidity in the structured credit market in 2007 and 2008, particularly for collateralized loan obligations, has set the market back somewhat." | Same. |
| `Nuveen p.6` | MAC allocation constraints: leveraged loans 5–25%, CLO BBB-B 0–10%, middle-market direct lending 0–35%. | Loans and CLO mezz as sleeves in Ch 12's optimizer. |
| `Nuveen p.9` | Index definitions: loans = "S&P UBS Leveraged Loan Index (Formerly Credit Suisse Leveraged Loan Index)"; CLO AA-A = JPM CLOIE AA/A (50/50); CLO BBB-B = JPM CLOIE BBB/BB/B (33/33/33); private credit proxied by "S&P UBS Leveraged Loan B Index." | Data atlas (App B); the "private credit = single-B loans" proxy is a joke that teaches. |
| `Veronesi p.322` | Table 8.1: CLO collateral = "Corporate loans"; SPV, trustee, bankruptcy-remoteness. | One-line structural definition. |

### 6.1 Loan settlement (the slowest thing in credit)

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| 2004 | Par convention T+10, distressed T+30, delays to 120 days. | `Moyer p.322` VERIFIED |
| 2016 | LSTA's first settlement study: only 29% of par trades settled within the T+7 target. After the Sept 2016 delayed-compensation ("requirements-based") rule, median par settlement fell to T+9 from T+12; 37% of September trades settled within T+7. | WebSearch summary of Markets Media / LSTA (SEARCH-LISTED; CHECK exact dates) |
| 2015–Jan 2025 | LSTA April 2025 welcome address chart: mean and median par settlement times, "10 yr average: 20 days." | LSTA events PDF (SEARCH-LISTED; fetch to read yearly values) |
| 2020s | Vendor factsheet: "for many firms, the average par trade settlement time remains upwards of 20 days"; guide: 15–20 business days common. | WSO/IHS Markit factsheet (SEARCH-LISTED) |
| CHECK | LSTA rule shortening the buyer's funding window from seven to five days (effective date unconfirmed). | asreport.americanbanker.com (SEARCH-LISTED) |

### 6.2 CLO tests and the CCC bucket

| Fact | Source / status |
| :-- | :-- |
| Typical CCC cap 7.5% of collateral par (some 5%); excess carried at market value (or agency recovery if lower) in the OC numerator; the excess is drawn from the lowest-market-value CCC loans first. | Academy Securities / Creditflux CLO guide (SEARCH-LISTED; fetch for exact wording) |
| Cliff: with the bucket full, a B– → CCC+ downgrade of one loan converts par to market value for the cheapest CCC loan in the pool. | Same |
| S&P (Apr 2023): at the 2020 peak, BSL CLO exposure to CCC-range companies peaked at 12.31% and average junior OC cushion fell to 1.13%; average junior cushion 4.5% at publication. | S&P Global Ratings, "Scenario Analysis: How Rising U.S. BSL CLO 'CCC' Baskets Could Affect Junior Overcollateralization Test Cushions" (2023-04-28), VERIFIED-URL via search; fetch for details |
| S&P (Jul 2020, European CLOs): CCC haircuts explained 39% of the average OC numerator decline; a further 5% rise in CCC holdings would push 16% of rated European CLOs through their most junior OC test. | S&P Global Ratings (2020-07-09), SEARCH-LISTED |
| A breach of the Class D OC test typically still pays Class D interest but defers Class E interest, subordinated management fees and equity distributions. | Academy Securities note (SEARCH-LISTED) |
| Academic: because haircuts apply piecewise, managers improve covenants most by selling risky loans in descending order of market value. | AEA materials link (SEARCH-LISTED; identify paper, CHECK) |

### 6.3 Repricing waves

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| 2024 | US institutional loan volume including repricings and extensions via amendment "almost $1.4 trillion," by far a record; repricing volume $756.8bn. | William Blair Lev Fin newsletters Q4-2024 and Q4-2025 (SEARCH-LISTED; PitchBook LCD data) |
| Jan 2025 | Record $215bn month of volume; repricings 52% of YTD volume, refinancings 18%; activity "came to a halt in March." | Matrix CMG Q1-2025 citing PitchBook LCD (SEARCH-LISTED) |
| Q2 2025 | Repricing activity fell to a multiyear low of $28.5bn after the tariff shock. | William Blair Q2-2025 (SEARCH-LISTED) |
| FY 2025 | Repricing volume $503.6bn (second only to 2024); refinancing $191.8bn (second highest on record). | William Blair Q4-2025 (SEARCH-LISTED) |
| 2024–2025 | European loans: record gross volume €202.9bn in 2024 (through early Dec, incl. extensions and repricings), second consecutive record in 2025. | PitchBook LCD articles (SEARCH-LISTED) |

### 6.4 Loan e-trading

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| Apr 2023 | Octaura (bank-backed: Citi, BofA, Credit Suisse, Goldman, JPM, Morgan Stanley, Wells Fargo, Moody's; CHECK founder list) launched loan trading. | Octaura / fi-desk (SEARCH-LISTED) |
| 2024 | ~$14bn traded on Octaura for the year. | Markets Media quoting CEO Brian Bejile (SEARCH-LISTED, self-reported) |
| H1 2025 | ~$19bn; ~$1bn/week; ~4.6% of LSTA secondary volume in Q1; 6.4% share in July 2025; Bloomberg: >$4bn a month, ~6% share by July. | Octaura posts, Markets Media, Bloomberg abstract (SEARCH-LISTED, self-reported) |
| Jun 2025 | Octaura raised $46.5m to add a CLO trading platform and data/analytics. | fintech.global (SEARCH-LISTED) |
| Dec 2025 | Largest day: >$1.4bn in a single session, week of 2025-12-08. | Octaura "2025 in review" (SEARCH-LISTED, self-reported) |

### 6.5 Loan funds and ETFs (from the electronification dossier, VERIFIED there)

| Date | Fact | Source |
| :-- | :-- | :-- |
| 2019–2025 | Bank-loan mutual fund assets fell 21% to $71bn while HY mutual fund assets rose 13% to $263bn; bank-loan fund liquidity ratio fell from ~10% (2021) to ~4.5%; in the April 2025 tariff week outflows did not concentrate in illiquid funds. | Federal Reserve FEDS Note (2026-08-19), per `state/research/trend_electronification_pt_etf_liquidity.md` |
| 2026-10-15 | **SRLN** (State Street Blackstone Senior Loan ETF): net assets $5,384.74mm; inception 2013-04-03; gross expense ratio 0.70%; 30-day SEC yield 7.11%; 731 holdings; actively managed, "normally investing at least 80% of its net assets in Senior Loans," benchmark Morningstar LSTA U.S. Leveraged Loan Index. | ssga.com SRLN page, VERIFIED-URL (fetched 2026-10-17): https://www.ssga.com/us/en/intermediary/etfs/spdr-blackstone-senior-loan-etf-srln |
| Apr 2025 | **JAAA stress test:** US-listed CLO ETFs swung to discounts averaging >1% on 2025-04-04; JAAA (~$20bn, the largest CLO ETF) traded >1% below NAV; JAAA's biggest single-day outflow (~$600mm; etf.com daily flows put 2025-04-08 at $585mm). Janus Henderson (CEO Ali Dibadj, PM John Kerschner) said redemptions were absorbed with "very little impact." May 2025: ~$850mm inflows to JAAA, "vast majority" in-kind creates; Barclays counted $663mm into AAA CLO ETFs in one May week; total CLO-ETF assets stayed below the Q1 peak. | etf.com, Octus, ETF Trends (SEARCH-LISTED; the manager's framing is the manager's) |

### 6.6 Secondary loan trading volume (LSTA)

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| 2022 | Prior record year: $824bn. | LSTA (SEARCH-LISTED) |
| 2024 | $821.4bn, +15% vs 2023, $3bn short of the 2022 record. | LSTA 2024 summary (SEARCH-LISTED) |
| Q2 2025 | Record quarter: $262bn (+~26% YoY). | LSTA "2Q25 Secondary Trading Monthly Executive Summary" (VERIFIED-URL via search: https://www.lsta.org/content/lsta-secondary-trading-monthly-executive-summary-2q25-secondary-loan-trading-volumes-spike-again-to-a-record-262-billion/) |
| Q3 2025 | $233bn, −18% QoQ, +~11% YoY. | LSTA (SEARCH-LISTED) |
| Oct 2025 | $95.1bn, +25% MoM, fourth-busiest month ever; three of the four busiest months were in 2025. | LSTA; Octaura blotter corroborates the +25% (VERIFIED) |
| FY 2025 | Record **$971bn**, ~18% above the prior record. LSTA's post-Q3 projection had been $965bn; Octaura's blotter said "on track to hit $1T." | LSTA secondary pages (SEARCH-LISTED); Octaura (VERIFIED) |
| Q1–Q2 2026 | Q1 2026 another record, trailing-12-month volume above $1tn for the first time; Q2 2026 volume −18% as volatility subsided. | LSTA (SEARCH-LISTED; CHECK exact figures) |

### 6.7 Loan e-trading, continued (Octaura blotter, VERIFIED: https://news.octaura.com/on-the-blotter-2025-in-review)

| Date | Fact |
| :-- | :-- |
| Jan 2025 | Secondary volume on Octaura +83% MoM; primary market (per JPM) second-highest month on record. |
| Mar 2025 | Octaura volume +120% MoM and +1,222% YoY; 70% of inquiry was customer selling. |
| Apr / Jun 2025 | Inquiry balanced in April (55% sellers); June 72% buyers. |
| Jul 2025 | Octaura share of LSTA secondary volume "spiked at 6.4%." |
| Aug 2025 | 159 BWICs ("WICs") on the platform; dealers provided >14,000 responses. |
| Dec 2025 | Largest day ever: >$1.4bn traded in one session (week of 2025-12-08). |
| Note | Page does not mention settlement, RFQ or list trading by name, and does not date the CLO platform launch. |

### 6.8 CLO tests, continued (Creditflux CLO Guide ch. 6, VERIFIED: https://cloguide.creditflux.com/6-understanding-the-tests)

- OC test = adjusted collateral par / (outstanding amount of that class + all senior classes), run at each payment date from the effective date; "the most junior OC test will fail first." Par includes cash and unsettled purchases.
- Defaulted assets carried at the lower of market value or an assumed rating-agency recovery. Worked example: $500mm par with one $5mm loan in default at MV 80% and recovery 40% → haircut $3mm, adjusted par $497mm.
- CCC bucket: Caa1/CCC+ or lower; above a threshold such as 7.5% of par, the excess is haircut by (par − MV), with the lowest-MV assets deemed the excess. Some deals include B3/B− on watch.
- Discount obligations: purchased below 85 are carried at purchase price, not par; later variants allow swaps up to a cap or define the discount by reference to the loan index.
- On OC failure: equity distributions, junior management fees and junior-note interest stop; cash pays down the most senior notes; principal receipts go to paydown, not reinvestment; successive failures reach successively more senior liabilities. Post-crisis US deals test each class except a combined AAA/AA test and usually no test for a single-B tranche.
- Interest diversion (reinvestment OC) test triggers earlier, suspends equity distributions and diverts interest into new assets (raising the numerator instead of shrinking the denominator).
- IC test computed monthly, numerator = interest proceeds available at that point in the waterfall, denominator = interest due on the next tranche; applied roughly AA down to BBB; "historically rarely failed."
- Maintain-or-improve tests: once failing, the manager may not trade in a way that worsens the metric.

### 6.9 CLO issuance and holders

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| End-2018 | US CLOs outstanding $617bn; US investors held 88%; foreign ~12% ($76bn); CLOs about half of US leveraged loans outstanding. | Liu & Schmidt-Eisenlohr, FEDS Note (2019), via GARP summary (SEARCH-LISTED) |
| 2020-06-25 | FEDS Note by tranche (DeMarco, Liu, Schmidt-Eisenlohr): institutional investors hold "sizable exposures to risky CLO tranches," larger than market participants believed. | VERIFIED-URL via search: https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-an-update-by-tranche-20200625.html (fetch for numbers) |
| 2024 | US CLO new issuance record $202bn (Eagle Point) / $203bn (Maples). | Eagle Point Income Co N-CSR FY2025 on EDGAR (VERIFIED-URL via search); Maples (SEARCH-LISTED) |
| 2025 | New issuance record $209bn; resets $232bn; refinancings $105bn; resets/refis lulled around the April tariff shock and recovered later. JPMorgan (via Maples) called net new supply "near-anaemic" after liquidations and re-issuances. | Eagle Point N-CSR FY2025: https://www.sec.gov/Archives/edgar/data/1754836/000199937126004310/eic_ncsr-123125.htm (VERIFIED-URL via search); Maples |
| Q1 2026 | YTD new issuance ~$73.3bn across ~163 deals through mid-March, −4–5% YoY; refi/reset activity ~45% lower YTD on wider spreads. | Maples Q1-2026 review (SEARCH-LISTED) |
| Dec 2018 (holders by tranche) | Identified US holdings $328.8bn: senior 61.8%, mezz/junior 30.0%, equity 7.8%. Banks: $59.3bn, 95.4% senior. Insurers: $108.9bn, 49.3% senior / 49.1% mezz. Mutual funds: $59.3bn, 66.4% senior, 12.5% equity. Pensions: $22.1bn, 76.6% senior. "Fund or other investment vehicle" (incl. hedge funds): $19.5bn, 35.8% equity. US loans underlying KY-issued CLOs: $457.1bn vs $616.9bn CLOs outstanding. "U.S investors hold the vast majority, almost 80 percent, of outstanding U.S. CLO securities." | FEDS Note 2020-06-25 (VERIFIED, fetched): https://www.federalreserve.gov/econres/notes/feds-notes/who-owns-us-clo-securities-an-update-by-tranche-20200625.html |
| 2025 H1 | CLO issuance $98bn, ~3% below the 2024 record run-rate (LSTA, July 2025). | LSTA 2Q25 summary (VERIFIED) |
| Early 2025 | Opal conference delegates expected BSL CLO AAA spreads to reach 3m SOFR + 110 bp in H1 2025 (Deutsche Bank flow, 2025-02-11); Bain Capital's Jeff Garver expected AAAs to test +110 in Q1. The April tariff shock widened CLO spreads and stalled deals (KBRA); Q3 2025 BSL AAAs "tested the mid-120-basis point range" (KBRA, Oct 2025); VanEck: spreads widened after "Liberation Day" but ended Q2 tighter than they started. **CHECK** the exact April 2025 AAA print. | Deutsche Bank flow, KBRA, VanEck (SEARCH-LISTED) |

### 6.10 Loan market size, prices, bid-ask (LSTA 2Q25 Secondary Trading Monthly Executive Summary, published 2025-07-24; VERIFIED, fetched)

- Morningstar/LSTA Leveraged Loan Index (LLI) outstandings up 5% to a record "approaching $1.5 trillion"; about 5% larger than in 2022.
- Turnover ratio = annual trading volume / LTM average monthly LLI outstandings: 58% in 2022 ($824bn / $1.4tn); LTM 65% ($979bn / $1.43tn), a five-year best equal to 2020. (The same page quotes LTM volume as $925bn in another section; unreconciled.)
- April 2025 volume $109.2bn (second only to March 2020's $119.3bn monthly record); May–June averaged $76.4bn/month.
- Daily average bid of the LLI "fluctuated 3.5% from crest to trough"; "V-shaped recovery" from the mid-April low; LLI average bid 97.6 on 2025-07-24, 10 bp lower YTD.
- June 2025: average trade level 97.2 (−80 bp YTD), median 99.6 (−56 bp YTD); average bid-ask (LSTA/LSEG mark-to-market) 72 bp, median 50 bp, both flat YoY; **share of June activity priced above par 37%, vs 8% in April 2025.**
- H1 2025 loan mutual fund and ETF gross flows $22.5bn, net −$5.5bn. June 2025 refinancing and repricing activity $45bn, a four-month high.

### 6.11 Above-par share and repricing eligibility

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| End-Dec 2024 | ~62% of loans traded above par, near the year's high. | Guggenheim 1Q25 Bank Loans FISV citing LCD/BofA (SEARCH-LISTED) |
| Apr → Jun 2025 | Share of trading activity above par 8% → 37%. | LSTA (VERIFIED) |
| Mid-Jul 2025 | More than half of outstanding loans priced at par or above. | PitchBook LCD commentary on LSTA site (SEARCH-LISTED) |
| 2024–2025 | Repricings were half of 2025 BSL activity; ~$1.3tn of term loan B repriced over the two years. | Kirkland & Ellis citing PitchBook (SEARCH-LISTED) |
| Nov 2025 (Europe) | Just over half of the Morningstar European Leveraged Loan Index above par. | PitchBook (SEARCH-LISTED) |

### 6.12 CLO and loan ETFs: AUM snapshot

| Fund | Fact | Source / status |
| :-- | :-- | :-- |
| JAAA (Janus Henderson AAA CLO ETF) | Surpassed $30bn AUM (press release 2026-08-13; "world's largest CLO ETF"); >$5.7bn 2026 inflows by 2026-08-10; dividend.com $30.2bn (2026-09-15); $26.9bn in the 2026-04-30 SEC portfolio report. ~$20bn in April 2025. | Janus Henderson press release (VERIFIED-URL via search: https://www.janushenderson.com/en-us/advisor/press-releases/janus-hendersons-aaa-clo-etf-jaaa-the-worlds-largest-clo-etf-surpasses-30-billion-in-assets-under-management/); aggregators SEARCH-LISTED |
| US CLO ETFs, total | >$35bn by Feb 2026 (~$4bn inflows in the first six weeks of 2026); >$50bn around end-Q2 2026 with ~$10bn H1-2026 inflows (BofA via Octus). JBBB ~$1.3bn and CLOZ ~$0.7bn (Octus table, 2026-07-01). | Octus, ETF Trends, Advisor Perspectives (SEARCH-LISTED) |
| BKLN (Invesco Senior Loan ETF) | Net assets ~$6.7–6.8bn mid-2026 ($6.82bn at 2026-06-30 per MarketXLS; $6.75bn at 2026-07-31 per stockanalysis); expense ratio 0.65% (some aggregators 0.67%); tracks Morningstar LSTA US Leveraged Loan 100 Index, ≥80% of assets in index components. Inception 2011-03-03 (**CHECK**). | Aggregators (SEARCH-LISTED); Invesco page returned no data |
| SRLN | $5.38bn (2026-10-15), see 6.5. | VERIFIED |
| Context | CLO ETFs ($50bn+) now exceed loan ETFs (BKLN + SRLN ≈ $12bn) by roughly 4×, and bank-loan mutual funds ($71bn, 2025) have shrunk 21% since 2019: retail money left the loan and went to the tranche. | Derived from the above; label as approximate |

### 6.13 Academic anchors (identified this session)

| Paper | Finding | Status |
| :-- | :-- | :-- |
| Loumioti & Vasvari (2019), "Portfolio performance manipulation in collateralized loan obligations," *Journal of Accounting and Economics* 67(2–3), 438–462, DOI 10.1016/j.jacceco.2018.09.003 | CLO managers use discretionary loan fair valuation and strategic trading to avoid monthly OC test violations; the association varies with junior noteholders' influence and market conditions; strategic trading (not fair-valuation discretion) predicts worse future CLO performance. Accepted manuscript open-access at LBS Research Online. | VERIFIED-URL via search (DOI); LBS eprint https://lbsresearch.london.edu/id/eprint/1014 |
| Elkamhi & Nozawa (2022), "Fire-sale risk in the leveraged loan market," *Journal of Financial Economics* 146(3), 1120–1147 | Leverage limits force constrained CLOs to sell loans downgraded to CCC or below; widely held loans lose value temporarily; diversification requirements make CLOs hold similar loans so constraints bind together, letting idiosyncratic shocks to large borrowers spread market-wide. Earlier title: "Too Big to Diversify: A Stress Test on Collateralized Loan Obligations" (NBER 2020). Replication package on Mendeley. | VERIFIED-URL via search (IDEAS: https://ideas.repec.org/a/eee/jfinec/v146y2022i3p1120-1147.html); Rotman PDF SEARCH-LISTED |
| Kundu (ESRB WP 141), covenant-driven fire sales | After a negative shock to oil and gas, CLOs exposed to those loans fire-sell *unrelated* loans. | SEARCH-LISTED: https://www.esrb.europa.eu/pub/pdf/wp/esrb.wp.141.en.pdf (CHECK title/year) |
| Liu & Schmidt-Eisenlohr (2019), FEDS Note "Who owns U.S. CLO securities?" and DeMarco–Liu–Schmidt-Eisenlohr (2020) update by tranche | See 6.9. | VERIFIED (2020 note fetched) |
| Cordell, Roberts & Schwert, "CLO Performance" (*Journal of Finance*, 2023) | Wharton Rodney White working paper 10-20 surfaced in search. CHECK volume/pages before citing. | SEARCH-LISTED |

### 6.14 Regulation touching loan funds

| Date | Fact | Source / status |
| :-- | :-- | :-- |
| Nov 2022 | SEC proposal (File S7-26-22) to amend the open-end fund liquidity rule would remove the "less liquid" category in which most loans sit; loans would likely become "illiquid investments," capped at 15% of an open-end fund. LSTA: this "effectively shuts down open-end loan funds." LSTA proposed a standardized expedited settlement arrangement (ESA) giving settlement certainty by T+3 between a dealer and a loan fund. ICI: in ~25 years no bank loan fund has suspended redemptions. | LSTA posts; SEC comment file S7-26-22 (VERIFIED-URL roots: https://www.sec.gov/comments/s7-26-22/) |
| 2025 | **CHECK**: whether the SEC formally withdrew the 2022 proposal (reported mass withdrawal of pending proposals in June 2025). Confirm before stating. | — |

### 6.15 Settlement, continued (Markets Media, 2016-11-02; VERIFIED: https://www.marketsmedia.com/lstas-delayed-comp-protocol-shows-encouraging-progress-moves-phase-ii/)

- LSTA delayed-compensation protocol Phase I applied to trades entered on and after 2016-09-01; Phase II effective 2016-11-01.
- Under the protocol the buyer must, by T+5 (previously T+6), execute the Confirmation and Assignment Agreement and select a settlement date of T+7 or earlier; lead times longer than one day are no longer accepted; the buyer "will not be entitled to delayed compensation for the lead time during which the loan remained on the balance sheet of the Seller."
- Result: median par settlement T+9 for September 2016 trades vs T+12 for Jan–Aug 2016; share settled within T+7 rose to 37% from 23%.
- LSTA's quarterly Secondary Trading & Settlement Studies (Q4-2024 dated 2025-01-24; Q1-2025 2025-04-22; Q2-2025 2025-07-23; Q3-2025 2025-10-27) are members-only PowerPoints; the index page is public: https://www.lsta.org/content-category/quarterly-secondary-settlement-data-study/ (VERIFIED-URL). Contacts listed: Ted Basta, Hugo Pereira.
- Implication for the chapter: the only robust public statements are (a) the 2016 medians above, (b) the "10-year average: 20 days" slide (SEARCH-LISTED, 404 on fetch), and (c) vendor claims of "upwards of 20 days." Write the Trend Watch with those three plus `Moyer p.322` and mark any 2025 median as CHECK.

### 6.16 SOFR transition and the credit spread adjustment (CSA)

- ARRC static spread adjustments: 11.448 bp (1m), 26.161 bp (3m), 42.826 bp (6m), the five-year median LIBOR–SOFR gap fixed on 2021-03-05. Loan market convention diverged: "10/15/25" CSA curve (1m/3m/6m), and a flat 10 bp was the most common alternative in April 2022 (Paul Hastings); some SOFR deals priced at the same margin as LIBOR loans, which the LSTA described as a transfer from lenders to borrowers. Sources: White & Case, Ropes & Gray ("No Way CSA," Sept 2022), CAIA, LSTA posts (all SEARCH-LISTED). Creditflux: "Investors caught out by vanishing spread adjustments" (SEARCH-LISTED).
- Use: the 2024–2025 repricing wave stripped CSAs as well as margins; a repricing engine must model margin *and* CSA as separate state variables. **CHECK** any statistic on share of loans with CSA removed.

### 6.17 CLO structure facts (primers, SEARCH-LISTED; Barings "What is a CLO" June 2025 is the cleanest)

- Typical BSL CLO capital stack: AAA 60–63%, AA 10–13%, A 7–9%, BBB 4–6%, BB 4–6%, B 1–2%, equity 8–10% (Barings). AAA subordination typically 35–40% (credit enhancement, not the tranche's share). Reinvestment period ~4–5 years (Invesco, SSGA); non-call 1–2 years, two years common.
- CLO share of the loan market: Nuveen via Maples (late 2025): US CLOs ~$1tn outstanding vs ~$1.5tn institutional loans, "roughly 65%"; Deutsche Bank flow (Oct 2025): CLO managers buy "nearly three-quarters" of new issuance; older: Western Asset 2019 ~68%, BAML 65%. State "about two-thirds of outstandings, roughly three-quarters of new issue (approx.)."
- Loss-mitigation / workout loans: post-2020 indentures allow purchase of "loss mitigation loans"/"workout loans" tied to an existing distressed position, often funded from interest proceeds (with transfer back to the interest account at market value once the asset performs, if the deal is above target par); principal use for rescue financing typically capped at 1–3% and subject to extra OC haircuts; CCC bucket (7.5%) and "equity" treatment of restructured assets remain obstacles; investor pushback on LMLs, up-tiered assets, privately rated assets (Schulte, Weil June 2024 "CLOs as restructuring," O'Melveny alert, Fitch "U.S. CLO Indenture Features Explained"; all SEARCH-LISTED). This is the PJT bridge: an RSSG banker knows exactly which lenders cannot fund new money, and the CLO indenture is why.

### 6.18 Loan momentum (academic)

- Beyhaghi & Ehsani (2017), "The Cross-Section of Expected Returns in the Secondary Corporate Loan Market," *Review of Asset Pricing Studies* 7(2), 243–277, DOI 10.1093/rapstu/raw010 (VERIFIED-URL via search: https://academic.oup.com/raps/article/7/2/243/2966151). Abstract: a 3-month-formation momentum strategy earns a monthly premium of 122 bp; momentum concentrated in loans of the lowest-rated borrowers; expected loan returns *decrease* with default beta; loan and stock momentum are cross-market correlated but each has independent information; loser-loan portfolios are riskier but earn lower returns. Hypothetical, backtested; sample period not confirmed here (CHECK).
- Mählmann, "Factor based private debt investing at the industry and country level" (KU Eichstätt working paper, SEARCH-LISTED): value and momentum in US industry and European industry/country leveraged-loan indexes predict credit excess returns.
- `Man_Quantitative p.41` (VERIFIED): "funds targeting opportunities in leveraged loans and, particularly, convertible bonds, where we see the potential for significant alpha. While loans and other private credit instruments are obviously problematic from a data availability perspective at present... Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities."

### 6.19 Shelf, continued: Moody's BET and the diversity score (`Schmid p.183–184`, VERIFIED)

- BET replaces $m$ correlated credits with $n<m$ independent credits matching the first two moments of the loss distribution; $n$ "is called diversity score of the collateral pool." Formulas: $\mathrm{EL}^{\text{orig}} = \sum_i (1-w_i) N_i P(\tau_i \le T)$, $\mathrm{Var}L^{\text{orig}} = \sum_i \mathrm{Var}L_i + \sum_{i\ne j}\rho^d_{ij}\sqrt{\mathrm{Var}L_i\,\mathrm{Var}L_j}$, with $\mathrm{Var}L_i = (1-w_i)^2 N_i^2 P_i(1-P_i)$; modified pool $\mathrm{EL} = (1-\bar w) N n P$, $\mathrm{Var} = (1-\bar w)^2 N^2 n P (1-P)$. Solve for $n$ and $P$.
- `Schmid p.174`: "Sometimes specific industry and diversity score tests or obligor concentration tests are applied." `Schmid p.172`: amortization "typically lasts 6–7 years"; waterfall figures from Fabozzi & Goodman (2001). `Schmid p.173`: Promise-A-2002-1 (KfW/HVB synthetic partially funded CLO, ~€1.62bn risk transfer) as a balance-sheet CLO example.
- Use in chapter: the diversity score is why Elkamhi–Nozawa's "too big to diversify" result bites: the test forces every CLO toward the same ~200-name pool, so the constraints correlate.

### 6.20 Kundu (2023), ESRB Working Paper No. 141, "The externalities of fire sales: evidence from collateralized loan obligations" (VERIFIED, PDF text extracted; https://www.esrb.europa.eu/pub/pdf/wp/esrb.wp.141.en.pdf)

- Abstract: covenants "intrinsic to Collateralized Loan Obligation (CLO) indentures, may amplify idiosyncratic shocks, imposing negative externalities on unrelated firms"; after the 2014 oil & gas price plunge, exposed CLOs "fire-sell unrelated loans in the secondary loan market to alleviate these constraints."
- Mechanism as written (p.2): covenants are piecewise; a defaulted loan "is marked to the lower of its market value or recovery value"; a discount obligation "is marked at the purchase price until the loan trades above a specified threshold (typically 90 ¢/$) for more than 30 days"; above the CCC/Caa1 limit the excess "is marked to the lowest market value among the CCC/Caa1 loans"; managers "can loosen their covenants by selling loans which exhibit higher market values than accounted values." She calls this "contractual arbitrage."
- Magnitudes: a 1 pp increase in a CLO's O&G share is associated with a 0.22%–0.52% decline in distance to the most stringent capital covenant; "the median CLO operates within 4% of the most stringent covenant threshold." A 1 pp increase in a (non-O&G) firm's exposure to O&G through CLOs is associated with a 61 bp decline in its secondary loan price; IV estimates 0.81%–2.54%; Amihud illiquidity rises 180–404 bp per $1mm sold after the shock; pass-through to primary spreads (+56 bp all-in-spread-drawn) and a 1.28 pp decline in investment. Defaulted loans in CLOs priced at 58 ¢/$ on average (IQR 34–?); ~30% of defaulted loans report a market price above 60.
- Use: the quantitative anchor for "forced selling of innocent bystanders," and the IV design is a template for the chapter's event-study spec. Elkamhi & Nozawa (JFE 2022) is the complementary paper on CCC-downgrade fire sales (PDF fetch failed twice, 503; cite from the IDEAS record).

### 6.21 Academy Securities, "OC Triggers: Subtle Thresholds Come to the Fore as Collateral Distress Builds Up" (VERIFIED, PDF text extracted; 2023, date to CHECK)

- "42 CLO deals that fail their junior OC test, based on recent trustee reports"; junior cushions from −3 bp (SRANC 2014-2A, just failed class E) to −104.7 bp (HLA 2012-1A, failing class C since August 2022); some failing deals also have low senior cushions (ECLO 2018-3A 2.72%, CECLO 2018-28A 3.73%).
- Worked deal: ZAIS6 2017-1A, required OC ratios from 122.6% (class A/B) to 103.7% (class E); current class E ratio 103.56% → failed. Numerator haircuts: defaulted −$13.5mm, deferring −$0.12mm, discount 0, excess CCC adjustment −$5.0mm; total haircut 5.72% of aggregate principal. Liabilities: A-1-R $146.6mm, A-2 $25mm, B-R $45mm, C-R $30mm, D $25mm, E $25mm.
- ZCCP 2019-1A class E breached in Feb 2023 and cured the following month via cash diversion.
- S&P expected CCC+ and lower share of companies to expand 5–6% in 2023; deals carry 5.0% or 7.5% CCC thresholds; "higher thresholds would cause OC tests to fail later."

### 6.22 Market events for case studies (VERIFIED via search summaries; primary pages SEARCH-LISTED)

| Date | Fact | Source |
| :-- | :-- | :-- |
| 2020-02-29 → 2020-03-23 | S&P/LSTA LLI weighted average bid fell from 95.18 to 76.23; March 2020 return −12.4% (second only to Oct 2008's −13.2%); distress ratio peaked at 57% (data as of 3/23); LSTA (2020-03-19): record volumes, record price volatility, bid-ask "widened beyond 300 basis points"; index rebounded to 82.9 by 3/31. | S&P Global LCD 1Q20 review, S&P MI "From trough to froth" (Mar 2021), LSTA posts |
| 2022 | Morningstar/LSTA LLI total return −0.6% (third negative year since 1997 inception) vs US HY −11%+; market-value component −6.2% (worst since 2008); monthly interest return rose 40 bp to 0.73%, a two-decade high. Europe: loans −3.5% vs euro HY ~−11%. | Morningstar Indexes, LSTA citing Citi Research |
| 2024 | >$350bn of institutional term debt repriced (Guggenheim); because 101 soft call lasts six months, borrowers cut contractual spread by 53 bp (Guggenheim) / typical cut 40–50 bp (CreditSights); some borrowers repriced several times in a year; banks pitched repricings timed to the soft-call expiry and offered to do deals for free (Bloomberg, 2025-01-30). "A 50 bp reduction in spreads means a potential 5% reduction in [CLO] equity returns" (TwentyFour AM). | Guggenheim 1Q25, TwentyFour AM blog, BNN Bloomberg (SEARCH-LISTED) |
| 2024 CLO | Gross new issuance $202bn (record), net ~$70bn after par repayments; refinancings $84bn (second-highest), resets $223bn; sum ≈ $509bn (my arithmetic). | Eagle Point Credit Co N-CSR FY2024 on EDGAR (VERIFIED-URL via search) |
| 2025 CLO BWICs | US CLO BWIC volume +21% YoY to ~$55bn YTD (JPM via Structured Credit Investor, ~Nov 2025); AAA = 51% of US BWIC flow; top-20 managers' deals = 47% of BWIC volume; October US BWICs $5.6bn. PGIM: >$230bn total US CLO secondary trading in the prior year; BWICs are "indicative" not total. | SCI, PGIM (SEARCH-LISTED) |
| 2024 defaults (from Ch 14 dossier) | Loan default rate incl./excl. DEs 4.0% vs 1.5% (Marquette, CHECK vendor); nearly 60% of defaulted US loans since early 2024 were distressed exchanges (Fitch via FTI); Moody's loan default forecast 7.5% YE2025 vs 3.4% historical average; >90% of LLI cov-lite (Wellington). | `state/research/trend_lmt_default_recovery_cycle.md` |
| 2024–2025 PC↔BSL (from Ch 17 dossier) | BSL↔DL takeouts "considerably balanced" in 2024–9M2025; >$30bn refinanced between the markets in 2025 (William Blair Q4-25); PC prices ~S+500 vs ~S+400 for LL; LL→PC migration peaked ~50% in early 2023 when BSL shut; Fed Z.1 now carries MM CLOs at $54bn (2025). | `state/research/trend_private_credit_convergence.md`; William Blair Q4-2025 (VERIFIED text) |
| 2023-04-04 | Academy Securities note date (Stav Gaon): "Securitized Products Special Topics: OC Triggers," figures as in 6.21. | VERIFIED (PDF text) |

### 6.23 William Blair Leveraged Finance Newsletter Q4-2025 ("Going for Gold"; VERIFIED, PDF text; PitchBook LCD-based)

- US institutional loan volume $439.1bn in 2025, 13% below 2024's $501.7bn, but above the 10-year average and above 2022 and 2023 totals. "Including repricings and extensions, annual volume surpassed $1.0 trillion, the second-highest total on record but 25% off 2024's total of $1.4 trillion."
- Refinancing $191.8bn (second highest ever, behind 2024); repricing $503.6bn vs $756.8bn in 2024; "76% of all activity during the year was related to refinancings, amendments or repricings."
- M&A-tied institutional volume $142.4bn (+~10% YoY); LBO $59.4bn (flat, below 10-year average); dividend recap $80.1bn; non-refinancing issuance $247.3bn (highest since 2021).
- Q4 2025 institutional volume $70.7bn, lowest since Q4 2023, down >50% QoQ; M&A $26.7bn, non-refi $48.6bn, refi $22.2bn all LTM lows.
- "Spreads for B-minus-rated borrowers fell to 354 basis points during the quarter, the lowest level since the Global Financial Crisis"; private credit pricing many deals at ≤500 bp, best quality "as low as the mid-400s."
- Cross-market refinancing "peaking in 2025 with over $30 billion being refinanced between each of the two markets." Lender survey borrower-friendliness index 4.3, highest since 2021; 68% saw higher Q4 volumes.

### 6.24 Elkamhi & Nozawa (JFE 2022), "Fire-Sale Risk in the Leveraged Loan Market" (VERIFIED, Feb 2022 draft PDF text; data: trustee reports via Acuris/Creditflux, 51,860 CLO transactions in sample)

- Loans widely held by constrained CLOs earn **3.4% lower CARs over the 20-week window leading to the downgrade** than loans that are not; fire-sale price impact of CCC-downgraded loans **−3.35%** (Table 6), with probability of forced sale 3.53% (Table 11, CCC column; IG 0.22%/0.82%, BB 0.76%/1.09%, B 0.23%/0.13% for impact/probability).
- "The average ratio of CCC loans to asset varies from 7.4% to 14.7%... the average CLO exceeds the threshold value for CCC loan ratio of 7.5% most of the time." Average CLO: 3.7% IG, 19.0% BB, 64.1% B, 7.5% CCC loans. Senior OC slack 8.8–30.0%; junior slack 0.9–6.5%, thinner in 2009 and 2020.
- Junior OC slack SD 3.26%, IQR 2.34%; a one-SD (IQR) decrease raises the chance of selling a downgraded loan by 1.56 (1.12) pp against an unconditional 13.27% over three months; top-to-bottom tercile move raises it by 3.53 pp. In the downgrade week 0.94% of widely-held-by-constrained-CLO loans' issue amount trades.
- Average price impact in downgrade weeks: 17.31% (2008–09), 1.26% (2010–19), 4.41% (2020). Once a CLO violates the 7.5% threshold it "faces another portfolio constraint which prohibits" certain trades (trading restrictions).
- Use: calibrate the Forced-Sale Pressure Index and its expected reversal; cite alongside Kundu's 61–180 bp per pp exposure.

### 6.25 Weil, "CLOs as Restructuring Participants" (May 2024; VERIFIED, PDF text)

- "The vast majority of a CLO portfolio – typically in excess of 90% – is required to consist of senior secured debt obligations."
- "A primary driver of CLO collateral managers in a restructuring will be to procure that the reinstated first lien debt has a rating that is high enough to keep it out of the 'CCC' buckets, which are typically set at 7.5% of the CLO portfolio. Any excess... will be subject to haircuts for the purpose of overcollateralisation tests and may subject the collateral manager to trading restrictions."
- Equity received in a restructuring "may be discounted entirely or (if it qualifies as a loss mitigation loan) be subject to punitive treatment"; HoldCo PIK structured to fit the "PIK Security" bucket "typically sized at up to a maximum of 5% of the portfolio"; fixed-rate bucket "typically sized at 10-15%"; long-dated bucket "typically ranging from 2.5-7.5%" with haircuts; "snooze-drag" transparency now demanded by investors; schemes/plans used to bind CLO lenders who cannot vote for maturity extensions.

## 7. Case studies

(pending)

## 8. Humor beats using the canon cast

(pending)

## 9. Resource candidates

(pending)

## 10. Exploratory-space notes

(pending)
