# How multi-manager pods run credit relative value: platform structure, risk regimes, economics, crowding

**Item:** How multi-manager pods run credit relative value: platform structure, risk regimes, economics, crowding.
**Prepared:** 2026-10-18 (researcher, Edition 2 pipeline, user directive 13: the relative-value thread). Slug `rv_pod_platforms_and_risk`.
**Feeds:** Ch 8 (isolating IDO), Ch 8-B (risk model and limit sheet, the pod risk regime), Ch 8-C (pair P&L explain), Ch 24 (basis as the short leg), Ch 28 (PM playbook, pod economics and capacity), Ch 1, 1-B, 4, 4-C (the pod seat), Ch 22 (borrow, capital and crowding), App C (trend tracker), App E (laws of the desk).
**Integrity.** Public sources only. Every dated fact has a source in the evidence table (section 8) or the section where it is stated. Press-reported thresholds are marked as such. Anything not confirmed from a page opened this session is marked **CHECK**. Nothing is quoted unless the words appear on a page I opened. Machine transcripts are marked **CHECK** for re-listening before print. Where an existing dossier already holds a fact, it is cited by file name (`life_quant_shop_daily_life`, `trend_systematic_credit_industry`, `perspectives_dealers_and_systematic_shops`, `papers_factor_replication_crisis_and_bond_data`, `media_podcasts_credit_quant`) rather than re-derived.

## 0. Method

Primary pages where they exist (firm sites, Mercer, Cambridge Associates, BIS, the Fed's report page, publisher feeds); otherwise trade-press pages that syndicate Bloomberg, WSJ and FT reporting. Transcripts are machine-made (podscripts.co) and marked **CHECK**. Bloomberg, WSJ, IMF.org and citadel.com returned 403 or worse in this sandbox, so facts resting on them are **CHECK**. Already held elsewhere: the Paleologo and Falk-Wallace quotes and the Millennium 5%/7.5% reports (`life_quant_shop_daily_life` section 5), Billion Dollar Club H1 2025 rows (`trend_systematic_credit_industry`), the podcast catalogue (`media_podcasts_credit_quant` 2.9). I re-verified those pages and add the arithmetic, credit hiring, unwind chronology and capacity data. Pair literature lives in `rv_credit_pairs_literature_and_mechanics`.

## 1. Findings in brief

1. **A platform is a bank trading floor rebuilt as a fund.** Mercer (May 2023): the model "found significant traction following the GFC as many proprietary bank trading groups were shuttered or substantially constrained".
2. **Pass-through is the keystone.** Cambridge Associates (10 Oct 2025): 0.87%-12.99% of assets, mean 5.93%; Barclays via *The Economist*: 6.2%. About 20% gross is needed for 10% net (section 3.2).
3. **The platform buys the residual.** Pods are "purely market neutral and factor neutral" (Paleologo, **CHECK**); "what you're levering is just that residual term" (Falk-Wallace, **CHECK**). The PM keeps 15-25% of own P&L.
4. **Netting risk is the price:** pay is per pod, not per fund; Albourne's simulations say about 1% a year (**CHECK**).
5. **The stop-loss is the risk model.** Reported for Millennium only: lose 5%, capital halved; lose 2.5% more, usually fired. Practitioners quote 3%/5-6% and 7-10%. No firm publishes a rule.
6. **A stop on allocated capital caps single-name credit risk in dollars:** on $200m, a 58-point default loss limits a long to $25.9m before one event breaches the firing line (section 4.4).
7. **Credit RV in pods is described four ways in public:** hedged fundamental long/short (Balyasny, Aug 2026), index and options (ExodusPoint; Millennium's Jun 2025 hire), macro credit, systematic. No pod publishes its credit book.
8. **Crowding is measured for equities and Treasuries, not credit** (93% Citadel-Millennium overlap in US stocks; BIS on swap spreads). Credit is a named gap.
9. **Unwinds are dated:** Mar 2020, Feb-Mar 2025, Apr 2025, Nov 2025, and a reported Mar 2026 episode (**CHECK**).
10. **Capacity and talent bind:** assets +25% against headcount +10-11% (Goldman, Sep 2026); about 20% PM turnover a year.
11. **For the book:** four constraints, each with arithmetic: residual (Ch 8), stop (Ch 8-B), pay (Ch 28), crowd (Ch 22, App E).

## 2. Platform structure as publicly described

**Layers and size.** LPs; a central firm that allocates capital and sets risk limits; PMs who run pods with their own P&L; analysts below them. Self-reported in October 2026: Millennium "$95BN+" and "370+ Investment Teams"; Balyasny $37B; Point72 about $58.5b and 200+ teams; ExodusPoint $14.9BN; D. E. Shaw $103bn of hedge fund assets (evidence table). Goldman counted 55 pod shops with $368bn at mid-2023, from 29 and $149bn in 2018 [S3]; the five biggest employ about 15,000 people on $1.6trn notional [S4].

**Spectrum.** Mercer arrays "centralized" funds against "platforms": more PMs means less collaboration, lower key-person risk, higher compliance cost, more netting risk, more pass-through, tighter liquidity terms, less transparency. eFinancialCareers (20 Oct 2023) reports insiders naming pod autonomy as the main difference: "Citadel is comparatively centralized; Millennium is not"; Paleologo separates a platform (pass-through) from a "multi-manager hedge fund like D. [E.] Shaw" (**CHECK**). *The Economist* adds that hair-trigger risk limits are "truer of firms like Millennium ... than Citadel".

**Credit inside platforms.** Hiring is the public window. Millennium (Jun 2025) added a CDS and CMBS index trader from Brevan Howard, a Laurion corporate-credit partner and LMR's former US head of credit while "down 1.4% through April"; Balyasny (Aug 2026) hired a BlackRock IG co-head to run a team that will "trade both long and short positions in US high-grade corporate bonds and pursue relative-value opportunities"; Jain (Aug 2026) hired Morgan Stanley's London HY head; Verition (Oct 2026) a macro credit PM. Credit stop-outs show too: a former JPMorgan HY trader was "stopped out" and his pod "disbanded" at ExodusPoint [S10]. Not public: any pod's credit gross, net, borrow, hedge ratios or P&L attribution; the pods' share of CDX flow; the number of credit pods per platform. Treat blog numbers on these as unsourced. Rosenberg (BlackRock) was asked about "Equity vs. fixed income: Comparing the pod shop model" on *Flirting with Models* (18 Aug 2025; chapter at 1:06:59; notes: "implementation and transaction costs [are] critical challenges compared to equities").

## 3. Pass-through, and why the platform pays for idiosyncratic return

### 3.1 Mechanism

A classic fund charges a management fee plus a performance fee on net profit. A platform pays each PM a share of that pod's P&L and bills the machine to the fund. Mercer lists the charges: "PM salary and incentive payouts, talent acquisition costs (e.g. hiring bonuses), business professionals' compensation, infrastructure costs such as technology and rent, as well as travel and entertainment." Cambridge: "Variable compensation is generally charged in addition to a fund level incentive fee, exposing investors to possible netting risk." ExodusPoint's page calls it a "Cost pass through structure designed to align interests".

Why LPs accept it (Paleologo, 20 May 2024, **CHECK**): a platform sits between a single manager and a fund of funds; it can watch PM skill daily, "give them more capital" or "take capital away from them or let them go", and pass-through "transfers the risk directly" to LPs. Albourne's Cosgrave (26 May 2025, **CHECK**): "if allocators had their way, they probably wouldn't want to invest in pass-throughs. But the fact is that they don't have a choice"; a pass-through manager "has to be around one-third more levered".

Alternative design (Nickel, a crypto platform; *Hedge Fund Journal*, 21 Apr 2026): pods "are not paid management fees or upfront signing bonuses", are paid performance fees with a "First Loss Deferred" (FLD) holdback, and the fund charges a fixed 2% rather than pass-through. Useful as a contrast, not as evidence about the big five.

### 3.2 Fee waterfall, worked (reproduces Mercer Figure 1)

Inputs from Mercer: management fee 1.0%; operations, talent and retention 3.0%; PM incentive and fund incentive 20% each. My reconstruction that reproduces Mercer's table: PM incentive = 20% x (gross - 3%); fund incentive = 20% x (gross - 1% - 3% - PM incentive).

| Gross | PM incentive | Fund incentive | Total cost | Net to LP | Net / gross |
| --: | --: | --: | --: | --: | --: |
| 5% | 0.40% | 0.12% | 4.52% | 0.48% | 9.6% |
| 10% | 1.40% | 0.92% | 6.32% | 3.68% | 36.8% |
| 15% | 2.40% | 1.72% | 8.12% | 6.88% | 45.9% |
| 20% | 3.40% | 2.52% | 9.92% | 10.08% | 50.4% |
| 25% | 4.40% | 3.32% | 11.72% | 13.28% | 53.1% |

Mercer: "for an investor to achieve a 10% net return, a fund must generate a gross return of approximately 20% or more". So a credit RV pod that "makes 6% on allocated capital" returns the LP about 1.1% (PM incentive 0.60%, fund incentive 0.28%, fixed 4.0%).

### 3.3 Netting risk, worked

Albourne's toy: pods of +$10 and -$10, payout 20%: the winner is paid $2 and the LP is down $2, where a classic fund pays nobody. Morillo (Odd Lots, 7 Oct 2024, **CHECK**): paying 36 PMs on their own P&L costs "about 25% more" than paying on the netted total; teams of three that net internally cost "only 5%, 5% to 6%" more. My simulation (illustrative: 36 PMs, each Sharpe 0.75, 5% vol, 15% payout, 200,000 trials):

| Pairwise correlation | Own-P&L payout / fully netted | Teams of three / fully netted |
| --: | --: | --: |
| 0.0 | 1.17 | 1.04 |
| 0.1 | 1.17 | 1.05 |

Premiums differ from his (inputs unstated), but the shape holds: small-team netting removes most of the cost. For Ch 28, model pay as an option on each pod.

### 3.4 What is bought: low-correlation residual

Aggregate Sharpe = SR x sqrt(N / (1 + (N-1) rho)), capped at SR / sqrt(rho) (Morillo). At SR 0.75:

| rho | Cap | N = 15 | N = 45 | N = 100 |
| --: | --: | --: | --: | --: |
| 0.05 | 3.35 | 2.23 | 2.81 | 3.07 |
| 0.10 | 2.37 | 1.88 | 2.17 | 2.27 |
| 0.20 | 1.68 | 1.49 | 1.61 | 1.64 |

At rho 0.10, 45 risk-takers capture 91% of the cap (he says "about 95%"). "A little bit of correlation has an enormous impact." A credit pod that is secretly long spread beta raises rho for everyone. Paleologo: "if everybody takes a little bit of factor exposure in the same direction and then you sum this across 300 PMs, it becomes a big factor exposure." Yelvington (7 Jul 2025, **CHECK**): if two traders' "month to month return started looking identical", "that would set off a red flag". And idio is only as good as the factor model: "when rates went up, a lot of equity portfolios moved and they really didn't know why, and there was no interest rate sensitivity in commercial factor models" (Paleologo).

## 4. Pod risk regimes

**Control stack.** Mercer: PM-level differences are "overall exposure ranges (i.e. long, short, gross, net), concentration, factor risk, and stop-loss implementation", and "many platforms dictate a factor-neutral positioning or very tight constraints". Paleologo names three jobs for risk: stop-losses (a "primitive tail insurance" for a PM who "is a little bit like somebody who's holding a call option"), true diversification, and keeping people "in scope". Scope bites in credit: Yelvington says a credit PM cannot ask for limits in an unrelated market, and risk reads the return stream for a disguised version of one.

**Reported thresholds (none is a firm disclosure).** WSJ via eFinancialCareers (5 Dec 2025): Millennium PMs who lose 5% "typically have their capital halved. If they lose another 2.5%, they're usually fired"; Hedgeweek (10 Mar 2025) adds that "exceptions can be made". Yelvington: stops "usually somewhere between 7 and 10 percent for what's called a stopout", with capital reduced "well before that three and a half or five", measured peak to trough. Kumar (26 Feb 2024): lose more than 3% and capital "is going to kind of get cut in half"; lose "5, 6%" and "you're probably getting stopped out". Brevan Howard and Schonfeld were described as tolerant; Eisler's COO: "We sat them out for a bit, and then we reloaded." Print the 5%/7.5% as the best-reported Millennium rule, plus the range.

**Stop-out odds, worked.** Probability a PM touches the stop within one year, drawdown peak to trough from zero, 40,000 daily paths (illustrative):

| Sharpe | Vol 4%, stop 5% | Vol 4%, 7.5% | Vol 6%, 5% | Vol 6%, 7.5% |
| --: | --: | --: | --: | --: |
| 0.0 | 37.5% | 10.3% | 71.9% | 37.0% |
| 0.5 | 22.9% | 4.4% | 57.7% | 22.9% |
| 1.0 | 12.4% | 1.5% | 42.6% | 12.4% |
| 1.5 | 6.3% | 0.5% | 29.5% | 6.5% |
| 2.0 | 2.8% | 0.1% | 19.2% | 2.9% |

A Sharpe-1 PM at 6% vol touches a 5% stop in 43% of years; at 4% vol, 12%. Volatility on allocated capital sets the survival rate; the platform pays for Sharpe. Allocated capital is a multiple of LP equity (Yelvington: "three and four times their notional value"). At 3.5x, LP equity $10bn becomes $35bn; if every pod hit 5% together, the loss is $1.75bn (17.5% of equity), 26% at 7.5%. That is an upper bound; compare Griffin's remark in Singapore on 9 Nov 2023 that a joint "10, 15, 20% hit to their equity ... is possible ... painful, but not systemic."

### 4.4 What the stop does to a credit book

Illustrative: capital $200m, halving at 5% ($10m), firing at 7.5% ($15m).

- **Single-name HY long.** A bond at 98 with 40 recovery loses 58 points. $40m long loses $23.2m (11.6% of capital), through both lines. The largest long that does not breach the firing line alone is $15m / 0.58 = $25.9m; limiting one default to 2.5% of capital ($5m) gives $8.6m.
- **Capital-structure pair.** Long $20m first-lien at 98 (recovery 70) loses $5.6m on default; short second-lien at 70 (recovery 20) gains 50 points per dollar, so $11.2m of short offsets it. Jump-neutral by sizing, not beta: "long the fulcrum, short the junior" is pod-compatible (Ch 3, 12-B).
- **Index and ETF legs** hedge spread beta in one ticker but leave basis risk (Ch 20, 24); the stop does not care why P&L moved.

Ironshield (a long/short credit fund, not a pod) gives the same rule: "Maximum position size (% of NAV) = loss budget / downside in points"; 35 points against 50bp caps a position at 1.4% of NAV. For shorts at 3-4 points of capital risk "the loss budget no longer sets the size. How many bonds you can borrow does."

**Centre book.** Mercer: "a central trading portfolio ('center-book') sometimes used in order to enhance or hedge certain exposures". Morillo (ex-Citadel) had "responsibility for the center book where a lot of that central stuff ... happens" (**CHECK**). A rival platform (Nickel, *Hedge Fund Journal*, 21 Apr 2026) says it has "no 'centre book', occasionally used by some funds to replicate pods' trades and/or reverse engineer their intellectual property": a competitor's claim, not a pod shop's admission.

**Leverage.** *The Economist*: funds "can borrow upwards of ten times the capital they raise"; Mercer: under 1x to 6x on regulatory collateral, "plausible" 20-30x with derivatives and repo; JPMorgan's average platform leverage 645% (Hedgeweek, 15 Sep 2026, definition not given); the Fed (8 May 2026): hedge fund leverage "near all-time highs", concentrated in the largest funds.

## 5. How credit relative-value pods are described in public

| Style | Public description | Gap |
| :-- | :-- | :-- |
| Hedged fundamental long/short | Balyasny IG team (Hedgeweek, 20 Aug 2026); ExodusPoint "fundamental long/short" | No gross, net, hedge |
| Index and options | ExodusPoint "credit index and options"; Millennium hire "specialised in trading indices tied to credit-default swaps and commercial mortgage-backed securities" | Pod share of index flow |
| Basis, curve, cross-market | Aviva: "curve relative-value trades, cross-market basis positions, swap-spread strategies, short-dated volatility structures, or carry-oriented exposures in credit indices and single names"; BIS documents the Treasury versions | Credit basis size |
| Capital structure, LME | In Ironshield's walk-through of co-op groups; no pod attributed | Inferred |
| Event, new issue | ExodusPoint "new issuance"; Bloomberg 2023: "high demand for distressed-debt teams at multistrats" | None disclosed |
| Macro credit, systematic | ExodusPoint; Verition hire | No performance |

Kumar's assembly line (**CHECK**): a platform's "core ... is some sort of quant strategy, like a [Stat-Arb] strategy ... And then you have fixed-income RV, credit RV, macro-RV, and then macro-directional."

### 5.2 Worked pair: three hedge ratios, one alpha

Illustrative inputs (mine): long $40.0m issuer A (spread 380bp, spread duration 4.2); hedge with issuer B (520bp, 4.6). P&L = spread change x duration x notional.

| Hedge | Short B | Formula |
| :-- | --: | :-- |
| DV01 neutral | $36.5m | 40 x 4.2 / 4.6 |
| DTS neutral | $26.7m | 40 x (4.2 x 380) / (4.6 x 520) |
| Empirical beta 0.60 | $21.9m | 40 x 4.2 x 0.60 / 4.6 |

| P&L in $m | DV01 | DTS | Beta |
| :-- | --: | --: | --: |
| Both widen proportionally (A +38bp, B +52bp) | +0.24 | 0.00 | -0.11 |
| Parallel +50bp | 0.00 | -0.23 | -0.34 |
| Idio: A tightens 15bp | +0.25 | +0.25 | +0.25 |
| Idio: B widens 20bp | +0.34 | +0.25 | +0.20 |

The alpha ($0.25m for 15bp) is the same size as the hedge-ratio error ($0.2-0.35m): idio is whatever the hedge model leaves. No ratio is right in every state. Carry matters: long A earns $1.52m a year, short $26.7m of B costs $1.39m, and at an assumed 75bp borrow the net is -$0.07m (about -17bp on the long). Add section 4.4: a $40m single-name long already breaches the firing line on $200m.

### 5.3 Shorts, capacity, private credit

Ironshield (E18, 4 Aug 2026): a short "has to clear three hurdles"; the book "ends up net long"; "A bond running from 100 to 20 over two years is a wonderful trade, and almost nobody is still short at 20"; hedging HY with HY "removes the exposure he is paid to hold". A pod needs the hedge inside the book, so it uses index, CDS, ETF and option legs and accepts basis risk. On capacity: "A US credit fund running $13bn has one analyst covering Europe ... a 5% position in a EUR 400m issue is EUR 20m, which is 0.15% of the fund." My inference: a $200m pod can use that corner and a $90bn platform cannot, so platforms keep many small credit pods and struggle to scale them. Platforms are also moving to private credit: Griffin is "wary of getting into private credit, as Millennium and Point72 are doing"; Covenant Lite #8 asks "Should a manager receive a bonus on accrued but unrealized interest?"

**Ironshield's sequence, as a PM checklist (not a pod).** Seven questions in order: does the name fit the fund (size, liquidity, lifecycle); what the business does and its sector KPIs; what is changing; the bear case; scenario-weighted return; what size the downside supports; long, short or neither. Exit rules: thesis wrong, cut at once; thesis intact but moving against you, scale down toward the loss budget; budget breached and you like it more, a unanimous committee. "Running step 6 as a gate instead of a conclusion changes which names reach the model at all."

## 6. Crowding and unwinds

**Mechanism.** Kumar (**CHECK**): risk management "is almost algorithmic ... your P&L kind of drives risk management", so a position that moves against one pod is cut, which moves it against the next. Aviva: "shared stop-loss systems and reliance on short-dated financing can turn dozens of relative-value positions into one crowded trade". Mercer's hedge fund research head, on a *Capital Allocators* episode (he appears in EP.345, 23 Oct 2023; Bloomberg does not name it), as quoted by Bloomberg on 30 Nov 2023: "There's some overcrowding and concern about the amount of leverage ... we are worried about the potential snowball effect." Bailey (11 Feb 2025): pods "deleverage rapidly in stress conditions". IMF (Oct 2026, via coverage, **CHECK**): leverage, crowded positions and redemptions; in VIX spikes the most crowded stocks were 10 points more volatile and lost 4 points more.

**Counter-view.** Morillo: "it's not obvious why they would be all in the same side ... just because they were organized as pods." A new-generation multi-strat CEO: "Everyone says 'We are going to be the one that is able to run out of the crowded theater' ... But it works less well as the theater gets more crowded." Magnetar built a strategy that "tends to make money after multistrats cut their crowded equity positions en-masse". Selling liquidity to a de-grossing platform is a business.

**Credit: the honest gap.** I found no measurement of pod share of CDX, iTraxx, HYG or LQD flow, no credit unwind attributed to platforms by a source I could open, and no disclosed pod credit loss. Aviva says scale "has redefined liquidity and price formation in credit markets, influencing everything from index hedges to single-name credit default swaps". The documented analogue is Treasuries: the swap-spread trade was $281bn in Q1 2024, $707bn in March 2025, and 11% smaller at $631bn by June as "traders were caught wrong-footed" in the April turbulence (BIS, 8 Dec 2025). Proxies to build for the book (not verified here): DTCC swap-data-repository index volume, ETF short interest, TRACE block prints. The chronology is in the evidence table.

## 7. Talent and capacity

- **Churn:** about 20% of PMs "are let go or leave every year"; platforms "act like sieves" (Paleologo, **CHECK**); Mercer: "as high as 20-30% at times".
- **Price:** eight- and nine-figure packages are "dangled" (eFinancialCareers 25 Feb 2026); a bank executive: "For Citadel or Millennium, the cost of hiring our best traders, trying them out and keeping them if they're any good is virtually nothing" (*Economist*). PMs "sign up for lengthy non-compete clauses".
- **Home-grown:** two-thirds of Citadel's fixed income and macro PMs; 60% of Point72's equity PMs. Citadel accepted under 1% of applicants; Balyasny 0.5% of intern applicants.
- **Credit PMs come from banks and rival funds** (hires above): the banks' loss is the pipeline.
- **Capacity:** Paleologo: "everything has a finite capacity". Goldman (Hedgeweek 15 Sep 2026): a "digestion" period when inflows outrun staffing. Platforms fund outsiders (52% allocate externally, Mercer; 40% seed, Economist); *Capital Allocators* EP.501 describes giving asset owners pod access "using the infrastructure, risk systems, and financing capabilities of a multi-strat underneath".
- **Giving money back:** Citadel "handed back $25bn in profits to investors since 2017"; Millennium locks capital "for up to five years" (*Economist*). Hedgeweek (1 Jun 2026) names the "scale paradox".

## 8. Evidence table

[S#] and [P#] keys are defined in Sources and section 9. Q = my computation from the cited inputs. **CHECK** rows rest on aggregators, previews, search summaries or machine transcripts.

| date | fact | source |
| :-- | :-- | :-- |
| Mar 2020 | LMR's main multi-strategy fund "plunged by a record 24%", mostly vol arb; Fed stepped in on the basis trade; Citadel down but "it wasn't meaningful" | [S3] |
| 2020, 2022 | Index-rebalancing crowding lost money; a dozen firms did it in 1998, at least 50 recently | [S3] |
| May 2023 | PM payout 15-25% of own P&L; Barclays sample of 42: 40% no pass-through, 30% partial, 30% full; ~20% gross for 10% net; turnover "20-30% at times"; 52% of platforms allocate externally | [S1] |
| 2 Oct 2023 | Balyasny: "$21 billion", "2,000 employees across 15 global offices" | [P12] |
| 20 Oct 2023 | Citadel "comparatively centralized", Millennium not; Brevan tolerant of stop breaches; Eisler "reloaded" | [S9] |
| 9 Nov 2023 | Griffin: joint "10, 15, 20%" hit to multi-managers' equity "possible ... painful, but not systemic" | [S3] |
| 30 Nov 2023 | 55 pod shops, $368bn (29, $149bn in 2018); 30% of gross US stock value; Citadel-Millennium overlap 93% of $90.7bn; a prime broker limiting leverage; 8% of investors planned to pull | [S3] |
| 11 Jan 2024 | AIMA/bfinance: outside multi-managers fees are "considerably lower" than 2-and-20; "Pass-through is quite polarizing" | [S25] |
| 26 Feb 2024 | Platform assets ~$400bn, growing 10-15% a year; pods run to lose no more than 3% so LP limit of 10% holds **CHECK** | [P1] |
| 2 Apr 2024 | Ten biggest: 15,665 staff (7,103 investment); five biggest added 1,663 in a year; ex-JPMorgan HY trader stopped out at ExodusPoint | [S10] |
| 19 Apr 2024 | Balyasny event-driven book lost $100m; "may also have been linked to" a US credit PM (unconfirmed) | [S11], [S33] |
| 7 Oct 2024 | Sharpe cap SR/sqrt(rho); own-P&L pay ~25% costlier than netted; teams of three 5-6% **CHECK** | [P5] |
| 11 Feb 2025 | Bailey: pods "deleverage rapidly in stress conditions"; MFA: "losses are siloed" | [S7] |
| Feb 2025 | Millennium -1.3%, worst month in six years, ~$900m from two index-rebalancing teams; HFR composite -0.47% | [S5] |
| 1-13 Mar 2025 | Citadel -1.7% in Feb, -1.7% early Mar; Millennium -1.4% to 7 Mar, liquidating a $1bn financials book; Balyasny stopped out PMs; DE Shaw Oculus -4.4% after +36% in 2024 | [S6] |
| 10 Mar 2025 | Griffin: three teams "had been sure of something that turned out to be wrong" | [S4] |
| Apr 2025 | Swap-spread trade fell 11% ($707bn in Mar to $631bn in Jun) as "traders were caught wrong-footed" | [S22] |
| 23 May 2025 | Top-5 staff 6,000 to 15,000 (2019-25); notional $1.6trn; top-10 share of borrowing 32% to 41%; pass-through 6.2% (Barclays); funds borrow "upwards of ten times"; 40% seed external managers | [S4] |
| 26 May 2025 | Albourne: netting cost ~1% a year; pass-through ~one-third more levered **CHECK** | [P6] |
| 2 Jun 2025 | Millennium hires Grau (Laurion), Reich (Brevan; CDS and CMBS indices), ex-LMR credit head; $73bn, 330+ teams; -1.4% to April, +15% in 2024 | [S13] |
| 7 Jul 2025 | Stops "between 7 and 10 percent"; reductions at 3.5-5%; allocations 3-4x notional **CHECK** | [P8] |
| 10 Oct 2025 | Pass-through 0.87%-12.99%, mean 5.93%, median 4.53%; comp the main component | [S2] |
| 5 Dec 2025 | WSJ-sourced 5% halving, +2.5% firing; Millennium +0.5% in Nov after two index pods lost "hundreds of millions" | [S8] |
| 8 Dec 2025 | BIS: swap trade $281bn (Q1 2024) to $631bn (Q2 2025); drove UST exposure growth since Q2 2024; basis trade largest but stagnant | [S22] |
| 13 Jan 2026 | Aviva: $4.3tn industry, $994bn multi-strategy (Mar 2024); pod RV spans curve, basis, swap spread, short vol, index and single names | [S21] |
| 25 Feb 2026 | Two-thirds of Citadel fixed income and macro PMs home-grown; 60% of Point72 equity PMs via LaunchPoint | [S12] |
| Early Mar 2026 | Reported synchronized platform losses (~$1.5bn x2, ~$1bn x2) **CHECK** | [S29], [S28] |
| 8 May 2026 | Fed: hedge fund leverage "near all-time highs", concentrated in largest funds | [S34] |
| Jun-Jul 2026 | "Worst two-week stretch" for momentum since 2023 (systematic equity, not pods) **CHECK** | [S28] |
| 1 Jul 2026 | ExodusPoint $14.9BN, 718 staff; Point72 ~$58.5b, 200+ teams, private credit; ExodusPoint credit = fundamental L/S, index and options, macro, new issue, systematic | [S32] |
| 4 Aug 2026 | Max size = loss budget / downside (35 pts, 50bp = 1.4% NAV); shorts bound by borrow | [P20] |
| 7 Aug 2026 | Jain hires Morgan Stanley's London HY head; credit one of seven "legs" | [S15] |
| 20 Aug 2026 | Balyasny IG team: "long and short" with "relative-value opportunities" | [S14] |
| 15 Sep 2026 | Multi-strat assets +~$500bn (~25%) vs headcount +10-11%; JPM average leverage 645% | [S17] |
| 1-18 Oct 2026 | Balyasny $37B, 2000+ staff; Millennium $95BN+, 7,100+, 370+ teams (firm sites) | [S32] |
| 6-13 Oct 2026 | IMF: hedge fund gross assets ~$13tn, notional >$40tn; Treasury share ~9% (4% in 2022); crowded stocks +10 pts vol, -4 pts in stress **CHECK** | [S19], [S20], [S35] |
| 13 Oct 2026 | Billion Dollar Club $4.6tn (+13% H1); DE Shaw $103bn; Millennium near $100bn | [S24] |
| Q | Fee waterfall: net 0.48/3.68/6.88/10.08/13.28% at gross 5/10/15/20/25% | section 3.2 |
| Q | HY long at 98, recovery 40: $40m loses $23.2m = 11.6% of $200m capital | section 4.4 |

## 9. Podcast episodes and posts (verified 18 Oct 2026)

Each page returned HTTP 200 this session; dates are publisher metadata (Omny `PublishedUtc`, feed `pubDate`, or the on-page date). T = machine transcript read on podscripts.co (**CHECK** before quoting).

| # | Title (show) | Date | URL | Use |
| :-- | :-- | :-- | :-- | :-- |
| P1 | "How the Rise of 'Pod Shops' Is Reshaping the Way Markets Trade" (*Odd Lots*, Krishna Kumar) T | 2024-02-26 | https://omny.fm/shows/odd-lots/022624-odd-lots-krishna-kumar-master-1 | Stop logic, LP 10% vs pod 3%; credit RV named as a sleeve |
| P2 | "How to Succeed at Multi-Strategy Hedge Funds" (*Odd Lots*, Paleologo) T | 2024-05-20 | https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds | Pass-through, factor x-ray, three risk jobs |
| P3 | "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (*Odd Lots*, Falk-Wallace) T | 2024-07-25 | https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really | Leverage on the residual |
| P4 | "How Hedge Funds Discover the Next Superstar Trader" (*Odd Lots*, Joe Peta) | 2024-09-05 | https://omny.fm/shows/odd-lots/how-hedge-funds-discover-the-next-superstar-trader | Talent selection |
| P5 | "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (*Odd Lots*, Dan Morillo) T | 2024-10-07 | https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master | Sharpe cap, netting arithmetic, centre book |
| P6 | "Why Asset Allocators Love Multi-Strategy Hedge Funds" (*Odd Lots*, Ronan Cosgrave, Albourne) T | 2025-05-26 | https://omny.fm/shows/odd-lots/why-asset-allocators-love-multi-strategy-hedge-funds | Netting cost, leverage needed to pay the layer |
| P7 | "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (*Odd Lots*, live 12 Jun 2025) | 2025-06-21 | https://omny.fm/shows/odd-lots/giuseppe-paleologo-on-quant-investing-at-multi-strat-hedge-funds | Quant role at a platform |
| P8 | "How You Get and Actually Keep a Job at a Multi-Strat Hedge Fund" (*Odd Lots*, Brian Yelvington) T | 2025-07-07 | https://omny.fm/shows/odd-lots/how-you-get-and-actually-keep-a-job-at-a-multi-strat-hedge-fund | Stop numbers, scope, credit-trader lore |
| P9 | "Gappy Paleologo" (*Money Stuff: The Podcast*) | 2025-07-04 | https://omny.fm/shows/money-stuff-the-podcast/gappy-paleologo | Factor models, garden leave |
| P10 | "Loads of Vultures: Funds, Agents, Bets" (*Money Stuff: The Podcast*) | 2025-10-03 | https://omny.fm/shows/money-stuff-the-podcast/loads-of-vultures-funds-agents-bets | Multistrategy talent market |
| P11 | "Bespokeness: AI, Passthrough, UST" (*Money Stuff: The Podcast*) | 2025-02-14 | https://omny.fm/shows/money-stuff-the-podcast/bespokeness-ai-passthrough-ust | Pass-through, "paying for hedge funds' photocopies" |
| P12 | "Multi-Strategy Platform at BAM" (*Capital Allocators* EP.341, Dmitry Balyasny) | 2023-10-02 | https://www.capitalallocators.com/podcast/multi-strategy-platform-at-bam/ | Founder on pods, risk, talent |
| P13 | "Inside Mercer Consulting" (*Capital Allocators* EP.345) | 2023-10-23 | https://www.capitalallocators.com/podcast/inside-mercer-consulting/ | Source of the overcrowding quote in Bloomberg, 30 Nov 2023 |
| P14 | "Multi-Strategy Hedge Fund First Principles at Jain Global" (*Capital Allocators* EP.487) | 2026-02-16 | https://www.capitalallocators.com/podcast/multi-strategy-hedge-fund-first-principles-at-jain-global/ | A new platform's design |
| P15 | "Disintermediating Pod Shops" (*Capital Allocators* EP.501) | 2026-05-11 | https://www.capitalallocators.com/podcast/disintermediating-pod-shops/ | Pod access for asset owners; capacity |
| P16 | "Credit Microcycles at Diameter" (*Capital Allocators* EP.484) | 2026-02-02 | https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/ | Credit-focused hedge fund and dislocation |
| P17 | "Private Credit Concerns" (*Capital Allocators* EP.494, Saba) | 2026-03-30 | https://www.capitalallocators.com/podcast/private-credit-concerns/ | Credit and equity dislocation trading |
| P18 | "People, Process, and Fixed Income Arbitrage at Bracebridge" (*Capital Allocators* EP.517) | 2026-09-28 | https://www.capitalallocators.com/podcast/people-process-and-fixed-income-arbitrage-at-bracebridge/ | Fixed-income RV shop |
| P19 | "Jeff Rosenberg - The Past, Present, and Future of Systematic Fixed Income (S7E19)" (*Flirting with Models*) | 2025-08-18 | https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN | Chapter "Equity vs. fixed income: Comparing the pod shop model" |
| P20 | "Inside a Long/Short Credit Hedge Fund: Sizing, Shorts and LME Risk" (*Fixed + Floating*, E18, Ironshield) | 2026-08-04 | https://podcasters.spotify.com/pod/show/fixedfloating/episodes/Inside-a-LongShort-Credit-Hedge-Fund-Sizing--Shorts-and-LME-Risk--Frits-Lieuw-Kie-Song-Ironshield-Capital-e3mncab ; post https://www.fixedandfloating.com/p/how-a-longshort-credit-hedge-fund | Sizing formula, shorts, perimeter |
| P21 | "ALO25: Master Your Hedge Fund Allocation ft. John Jackson" (*Top Traders Unplugged*, Mercer) | 2024-08-14 | https://www.toptradersunplugged.com/captivate-podcast/alo25-master-your-hedge-fund-allocation-ft-john-jackson/ | Allocator's view |
| P22 | "Boaz Weinstein" (*Money Stuff: The Podcast*) | 2026-03-19 | https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein | Credit and closed-end-fund dislocation |
| B1 | "Bond Voyage: Industrialised alpha meets fixed income fragility" (Aviva Investors) | 2026-01-13 | https://www.avivainvestors.com/en-dk/views/aiq-investment-thinking/2026/01/bond-voyage/ | Pods in credit and rates plumbing |
| B2 | "A New Generation Pod Shop" (*The Hedge Fund Journal*, Nickel Digital) | 2026-04-21 | https://thehedgefundjournal.com/nickel-digital-multi-manager-strategy-pod-shop/ | First-loss deferral, no centre book |
| B3 | "Covenant Lite #8: Point72 and other Multistrats Enter the Private Credit Game" | 2025-02-23 | https://covenantlite.substack.com/p/covenant-lite-8-point72-and-other | Pass-through vs illiquid assets |
| B4 | "Crowding Isn't One Trade. March Proved It." (Resonanz Capital) | 2026-07-13 | https://resonanzcapital.com/insights/crowding-isnt-one-trade.-march-proved-it | Secondary; **CHECK** |

Also checked: *Flirting with Models* S7E11, "Giuseppe Paleologo - Multi-Manager Hedge Funds & Thinking Deeply About Simple Things", 2024-09-02, confirmed in the publisher feed only (episode page not located); *Odd Lots* "How Banks Turned Into Giant Synthetic Hedge Funds" (2025-02-21) is in the feed but I did not open it. Paywalled previews opened: Rupak Ghose, "Citadel is from Mars and Millennium is from Venus" (30 Mar 2025, https://rupakghose.substack.com/p/citadel-is-from-mars-and-millennium) and two Quant Enthusiasts posts.

## 10. Book placement

| Chapter | What this dossier serves | Where |
| :-- | :-- | :-- |
| Ch 1, 1-B | The pod as counterparty and competitor of the market maker; a pod day (x-ray, stop, scope call) | 2, 4, evidence |
| Ch 3 | RSSG instinct as a pod trade: long the fulcrum, short the junior, sized to be jump-neutral; the LME perimeter | 4.4, 5.3 |
| Ch 4, 4-C | Who pays whom: fee waterfall, pass-through, credit hiring as industry map | 2, 3.2 |
| Ch 4-B | DV01, DTS and empirical-beta hedge ratios as a scenario table | 5.2 |
| Ch 5 | Pair P&L as a difference of two jump processes; stop-out odds | 4 |
| Ch 7 | Idio is relative to a factor model; the rates-blind factor model | 3.4 |
| Ch 8 (canonical) | Residual, correlation cap on Sharpe, worked pair | 3.4, 5.2 |
| Ch 8-B (canonical) | Thresholds with sources, stop-out table, scope, centre book, leverage | 4 |
| Ch 8-C | Pair explain with carry and borrow lines; netting in the pod's pay | 3.3, 5.2 |
| Ch 12-B, 12-C, 13 | Cap-structure pairs inside the stop; co-op seat versus fund size | 4.4, 5.3 |
| Ch 17 | Pass-through versus illiquid assets (Covenant Lite #8; Mercer) | 5.3 |
| Ch 20, 24 | Index, ETF and CDS legs as the short; Treasury swap-spread analogue (BIS) | 5, 6 |
| Ch 22 | Bailey, IMF, Fed, BIS, the MFA rebuttal; the credit measurement gap | 6, evidence |
| Ch 28 (canonical) | Pay, netting, stop-out odds, talent churn, capacity | 3, 4, 7 |
| App C | Dated rows: 11 Feb 2025, 2 Jun 2025, 15 Sep 2026, 7 and 20 Aug 2026, 6-13 Oct 2026 | evidence |
| App E | Laws: a stop is a short put held by the platform; idio is whatever the hedge leaves; pay is per pod and risk is per fund; crowds exit at the stop, not at the thesis | 3, 4, 5 |

Figures worth drawing: fee waterfall (stacked bars), stop-out heat map, Sharpe-cap curves, pair scenario bars, Treasury swap-trade size ($281bn, $707bn, $631bn).

## 11. Open items and unconfirmed claims

- **Not opened, treat as CHECK:** Bloomberg's 10 Mar 2026 piece "Citadel, Balyasny, Millennium, Point72 Hit by Iran Conflict in Wild Week" (403) and every March 2026 dollar figure; the WSJ original of the 5%/7.5% rule; the BoE text of Bailey's 11 Feb 2025 speech; the IMF chapter and blog (403); the Barclays pass-through survey; the Fed report's own text (only the page and a law-firm summary were read).
- **Machine transcripts** (Odd Lots; podscripts.co) must be re-listened before any quotation is printed. Paywalled previews (Ghose; both Quant Enthusiasts posts) show only intros.
- **No public evidence found** for: pod share of CDX/HYG/LQD flow; a disclosed pod credit loss; any pod's credit gross, net, borrow or hedge ratios; a first-person account of a centre book from a platform.
- **Unresolved dates and bases:** Goldman's "+$500bn, ~25%" base differs from other counts; Kumar's $400bn (Feb 2024) predates it; the Mercer hedge-fund head's quote is from an unnamed Capital Allocators episode.
- **Individuals.** Trade-press names of PMs who were stopped out or lost money are deliberately left out of this file; use the roles.
- *Flirting with Models* S7E11 (Paleologo, 2024-09-02) is confirmed in the feed only.

## Sources (URLs verified this session, 18 Oct 2026; HTTP 200 unless noted)

**Papers and reports.** [S1] Mercer, "Multi-Manager Platforms: A due diligence perspective", May 2023: https://insightcommunity.mercer.com/api/v1/uploads/Multi_Manager_Hedge_Funds_614b3c4909.pdf?public=true . [S2] Cambridge Associates, 10 Oct 2025: https://publishedresearch.cambridgeassociates.com/2024-hedge-fund-discretionary-expense-summary/ . [S4] *The Economist*, special report, 23 May 2025 (reprint hosted by Citadel): https://www.citadel.com/wp-content/uploads/2025/06/131411.pdf . [S21] Aviva Investors, 13 Jan 2026: https://www.avivainvestors.com/en-dk/views/aiq-investment-thinking/2026/01/bond-voyage/ . [S22] BIS Quarterly Review box, 8 Dec 2025: https://www.bis.org/publ/qtrpdf/r_qt2512y.htm . [S23] Fed Financial Stability Report page: https://www.federalreserve.gov/publications/financial-stability-report.htm ; [S34] summary of 8 May 2026 report: https://infobytes.orrick.com/2026-05-22/fed-releases-its-semiannual-financial-stability-report/ . [S24] With Intelligence, 13 Oct 2026: https://www.withintelligence.com/insights/billion-dollar-club-h1-2026/ ; [S25] 11 Jan 2024: https://www.withintelligence.com/insights/pricing-performance/ . [S26] *The Hedge Fund Journal*, 21 Apr 2026: https://thehedgefundjournal.com/nickel-digital-multi-manager-strategy-pod-shop/ . [S27] Covenant Lite #8, 23 Feb 2025: https://covenantlite.substack.com/p/covenant-lite-8-point72-and-other . [S28] Resonanz Capital, 13 Jul 2026: https://resonanzcapital.com/insights/crowding-isnt-one-trade.-march-proved-it . [S29] Quant Enthusiasts, 20 Jun 2026 (preview): https://youngandcalculated.substack.com/p/multi-strategy-hedge-funds-lost-billions . [S31] Rupak Ghose, 30 Mar 2025 (preview): https://rupakghose.substack.com/p/citadel-is-from-mars-and-millennium .

**News.** [S3] Bloomberg, 30 Nov 2023, via The WealthAdvisor: https://www.thewealthadvisor.com/article/citadel-and-its-peers-are-piling-same-trades-regulators-are-taking-notice . Hedgeweek: [S5] 10 Mar 2025 https://www.hedgeweek.com/millennium-posts-rare-monthly-loss-amid-index-rebalancing-trades/ ; [S6] 13 Mar 2025 https://www.hedgeweek.com/multi-strats-troubled-by-trump-trade-war/ ; [S7] 12 Feb 2025 https://www.hedgeweek.com/boes-bailey-warns-of-potential-multi-strat-stability-risks/ ; [S13] 2 Jun 2025 https://hedgeweek.com/news/millennium-bolsters-credit-trading-team-with-high-profile-pm-hires ; [S14] 20 Aug 2026 https://www.hedgeweek.com/balyasny-taps-former-blackrock-credit-chief/ ; [S15] 7 Aug 2026 https://www.hedgeweek.com/jain-global-hires-morgan-stanley-high-yield-trading-chief-for-european-credit-push/ ; [S16] 14 Oct 2026 https://hedgeweek.com/news/verition-sees-five-macro-trader-departures-as-it-adds-london-portfolio-manager ; [S17] 15 Sep 2026 https://hedgeweek.com/news/multi-strats-may-need-to-accelerate-pm-hiring-as-assets-surge ; [S18] 1 Jun 2026 https://www.hedgeweek.com/multi-strat-governance-and-leadership-becoming-key-considerations-for-pms/ ; [S19] 7 Oct 2026 https://hedgeweek.com/news/imf-calls-for-closer-monitoring-as-hedge-funds-expand-market-footprint ; [S33] 24 Apr 2024 https://www.hedgeweek.com/ex-balyasny-pm-who-left-after-100m-loss-joins-millennium/ . eFinancialCareers: [S8] 5 Dec 2025 https://www.efinancialcareers.com/news/pratik-madhvani-glen-scheinberg ; [S9] 20 Oct 2023 https://www.efinancialcareers.com/news/2023/10/citadel-millennium-hedge-funds ; [S10] 2 Apr 2024 https://www.efinancialcareers.com/news/biggest-multistrategy-hedge-funds ; [S11] 19 Apr 2024 https://www.efinancialcareers.com/news/hedge-fund-millennium-hired-balyasny-london-portfolio-manager-who-left-after-100m-loss ; [S12] 25 Feb 2026 https://www.efinancialcareers.com/news/hedge-fund-junior-jobs . IMF coverage: [S20] Opalesque, 8 Oct 2026 https://www.opalesque.com/716669/Hedge_fund_gross_assets_tripled_to_since666.html ; [S35] International Finance https://internationalfinance.com/markets/imf-warns-growing-hedge-fund-footprint-merits-closer-scrutiny/ .

**Firm sites (read 18 Oct 2026).** [S32] https://www.mlp.com/ ; https://www.bamfunds.com/ ; https://point72.com/ ; https://www.exoduspoint.com/ ; https://www.deshaw.com/ (home page, no AUM).

**Podcasts [P#]:** URLs in section 9. Transcripts read: https://podscripts.co/podcasts/odd-lots/how-the-rise-of-pod-shops-is-reshaping-the-way-markets-trade ; .../how-to-succeed-at-multi-strategy-hedge-funds ; .../how-the-hottest-hedge-funds-on-wall-street-really-manage-risk ; .../the-math-that-explains-how-multi-strategy-hedge-funds-make-money ; .../why-asset-allocators-love-multi-strategy-hedge-funds ; .../how-you-get-and-actually-keep-a-job-at-a-multi-strat-hedge-fund . Feeds parsed: https://rss.libsyn.com/shows/94820/destinations/482814.xml (*Capital Allocators*) ; https://anchor.fm/s/10958cc44/podcast/rss (*Fixed + Floating*) ; https://feeds.captivate.fm/flirting-with-models/ ; https://feeds.captivate.fm/top-traders-unplugged/ ; the Omny feeds for *Odd Lots* and *Money Stuff* listed in `media_episodes_posts_parts_I_II`.

**Reached but not usable (403/404/429/503):** the Bloomberg URL above (403), imf.org chapter and blog (403), nasdaq.com, advisorperspectives.com, hedgeco.net pages, selbyjennings.com. Not cited as sources.

<!-- STATUS: COMPLETE -->
