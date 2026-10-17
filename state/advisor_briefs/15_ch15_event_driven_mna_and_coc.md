# Advisor Brief: Chapter 15, Event-Driven M&A, Regulatory Spreads & Change-of-Control

*Fable advisor, Edition 1. Target file: `book_src/15_ch15_event_driven_mna_and_coc.md`. Research date: 2026-10-17. The shared web-search budget was exhausted before this brief started, so every web fact below was pulled directly from primary sources (SEC EDGAR full-text search and filings, FTC/DOJ reports, the European Commission, CourtListener, Crossref). Facts are VERIFIED (document fetched this session, URL given) unless marked CHECK (recalled, or seen only in a listing). Shelf quotations were copied from `state/pdf_pages` text; page numbers are the PDF page indices `tools/pdf_search.py` prints.*

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** A merger is not a stock event with a bond footnote. For a credit desk it is a bundle of *contractual cash flows that fire on a date nobody knows*: the 101 change-of-control (CoC) put, the special mandatory redemption (SMR) at 101, the make-whole, the convertible "fundamental change" put, the CDS successor determination, the ratings trigger, and the loan's CoC event of default. Every one of those is an option whose underlying is a *legal process with a clock*: HSR waiting periods, Second Requests, EU Phase II, CFIUS, the STB, a district-court preliminary-injunction hearing. The chapter's job is to teach the reader to price each contractual payoff as an option, to price the clock as a survival curve, and to notice that the two are coupled: the payoff's moneyness depends on where rates and the acquirer's spread are *when* the clock stops.

**The aha.** The RSSG reader already knows the documents cold. What they have not been made to do is treat the document as a payoff function and the regulator as a hazard rate. Three "aha" moments drive the chapter:

1. **Moneyness is a coupon-vintage accident.** A 101 CoC put on a 1.85% coupon bond issued in February 2021 is deep in the money the moment it is triggered in 2026, because the bond trades in the 80s on rates alone; the same put on a 6.875% 2029 note is worthless because the bond is already above 101 and the acquirer is a better credit. The put does not care about the "credit story"; it cares about $101 - P$. Electronic Arts (EA) and U.S. Steel, both 2025–26 deals, are the two ends of this spectrum (dossier §6.2, §6.6).
2. **The SMR bond is a deal-break probability gauge sitting inside the acquirer's own curve.** Kroger issued \$10.5bn of notes in August 2024; only the four short tranches (\$4.7bn) carried the SMR. The price gap between SMR and non-SMR tranches of the *same issuer*, after curve-matching, is a market-implied probability that the deal dies, and it is a cleaner read than the equity merger-arb spread because it carries no takeover-premium noise. When the Oregon court enjoined the deal on December 10, 2024, Kroger redeemed the SMR notes at 101 on December 18 (dossier §6.1).
3. **The regulator is a hazard rate, and the market underreacts to the passage of time.** Of 1,944 adjusted HSR transactions in FY2025, 41 drew Second Requests (2.1%); that handful of deals is where all the event risk lives and where timelines stretch from 30 days to 18–26 months. Kaplan–Meier on signing-to-close times, Cox regression on deal covariates, and competing-risks cumulative incidence (clear / abandon / block) convert the RSSG reader's process knowledge into priced time. Giglio and Shue (2014) show equity markets systematically underreact to "no news" in pending mergers; the credit analogue (target spreads drifting tighter as milestones pass silently) is the chapter's bridge to Chapter 10's trend material.

The chapter's recurring line: **the CoC put is a covenant, and covenants can be defeased.** In the EA take-private, the sponsors defeased the legacy 2031 and 2051 notes with Treasuries rather than pay 101 on bonds trading far below par (our reading of the August 4, 2026 8-K; see §6.2). Kaz priced the put. Theo read the defeasance section. Theo was right.

---

## 2. Section outline (7,000–10,000 words)

**Cold open (≤400 words).** December 12, 2024, 7:40 a.m. Theo's screen shows an Item 2.04 8-K: Kroger has delivered a notice of special mandatory redemption. Kaz asks why anyone would *mandatorily* redeem bonds at a premium when nothing has defaulted. Mags says the last time she saw a grocer redeem bonds this fast was never. Ines asks the only question that matters: who sold these bonds at 101.5 last week, and what did they know about Judge Nelson's calendar? Ends on: *how do you price a cash flow whose trigger is a federal judge?*

- **15.1 The Event-Driven Credit Map: Six Cash Flows That Fire on a Deal.** Desk framing. Taxonomy of M&A-contingent payoffs in bonds, loans, converts and CDS, each written as a payoff function of (deal closes?, trigger?, price at trigger). Who is the forced seller/buyer in each (IG index funds at the fallen-angel line; CLOs at the loan CoC EoD; convert arbs at the fundamental-change put). **Trend Watch #1: the 2024–26 mega-deal and sponsor take-private wave** (EA \$55bn, WBD's three suitors, UNP–NSC \$85bn, Synopsys–Ansys, HPE–Juniper; HSR aggregate reported value \$1.6tn FY2023 → \$2.1tn FY2024 → \$2.5tn FY2025). Anatomy elements: desk framing, Trend Watch, resource graph.
- **15.2 Anatomy and Pricing of the 101 CoC Put.** IG "double trigger" (CoC *and* a ratings decline below investment grade within the window) versus HY single trigger; the 30–60 day offer mechanics; why 101. Derivation A (below): $V_{\text{CoC}}$ as a compound option; conditional moneyness; coupon-vintage effect. **Source extraction:** Veronesi p.470 (sub-optimal exercise), Schmid p.153 (puts knocked out at default). **Ways This Blows Up:** defeasance and covenant strips kill the put; the put is European-ish in practice; accrued-interest and record-date traps. **Specification for AI Implementation #1:** `price_coc_put`. Case: EA 2025–26.
- **15.3 Portability: The Short Option You Did Not Know You Sold.** The "Specified Change of Control Event" clause: leverage test, time window, one-time use, often sponsor-to-sponsor only. Derivation B: portability as a short digital on pro-forma leverage, and the game-theoretic point that the sponsor chooses leverage *with the test in mind*. Kaz gag ("portability, like a phone number?"). **Trend Watch #2:** portability's migration from European HY to US HY and into loans (data caveats; EDGAR counts; CHECK Covenant Review/9fin shares). Cross-ref Ch 13 (document features as state variables) and Ch 25 (NLP extraction of the leverage test).
- **15.4 Special Mandatory Redemptions: The Deal-Break Gauge in the Acquirer's Curve.** Mechanics (101 + accrued; outside date; no escrow; tranche carve-outs). Derivation C: SMR price decomposition, implied break probability, probabilistic duration, SMR-vs-non-SMR tranche relative value. **Source extraction:** Moyer p.267 (the early-redemption "option" premium reflects the probability). **Docket Diary:** Kroger–Albertsons from October 13, 2022 signing to December 18, 2024 redemption. Also Tapestry (\$6.1bn redeemed, \$61.1mm premium), HPE (SMR on four of six tranches; DOJ suit then settlement), Synopsys (closed; SMR expired worthless). **Specification #2:** `smr_implied_break_prob`, `smr_price`, `smr_duration`.
- **15.5 Antitrust and Regulatory Timelines as Survival Analysis.** HSR mechanics (30-day wait, Second Request, substantial compliance; early termination's disappearance and return). The FY2016–FY2025 HSR table. EU Phase I 25 working days / Phase II 90 (+15/+20); UK CMA, China SAMR, CFIUS, STB (CHECK details). Derivation D: Kaplan–Meier, Nelson–Aalen, Cox PH, competing risks (Aalen–Johansen). **Source extraction:** Bohn–Stein p.232 (Kaplan–Meier arises exactly because firms "drop out of the sample due to, say, a merger"), p.233 (Cox PH), p.228 (right censoring). **Trend Watch #3:** early terminations granted 1,102 (FY2016) → 0 (FY2023) → 265 (FY2025); the new HSR form (effective Feb 10, 2025) vacated by a district court Feb 12, 2026 with the Fifth Circuit denying a stay Mar 19, 2026; regime shifts as shifts in $h_0(t)$. **Poker Table:** Ines on the Second Request as a tell. **Specification #3:** survival engine with synthetic cohort and built-in checks.
- **15.6 Target vs. Acquirer: Spread Compression, Acquirer Widening, and Event Momentum.** Billett–King–Mauer (targets gain, especially sub-IG targets bought by IG acquirers; acquirers lose), Furfine–Rosen (mergers increase default risk), Acharya–Johnson (CDS moves before LBO announcements: Ines's hand history). Bayesian drift of $\pi_d(t)$ as silent milestones pass (Giglio–Shue). Ben Dor p.212 (hedge ratios collapse after rating events) for why the hedge must be re-struck at the trigger. "IDO or it didn't happen": strip the acquirer's beta before claiming event alpha.
- **15.7 When the Deal Dies: The Merger as the Credit.** Spirit–JetBlue: injunction (Jan 16, 2024), termination (Mar 4, 2024), prearranged Chapter 11 (Nov 18, 2024). The target's spread as a mixture of "acquirer's curve" and "standalone distressed curve"; why the post-break jump is a regime switch, not a diffusion. Cross-ref Ch 5 (mixtures) and Ch 14.
- **15.8 Case Study Cluster: Warner Bros. Discovery 2025–26.** Covenant-strip tender (June 2025), a bridge facility literally named "Non-Investment Grade Leveraged Bridge Loan Agreement," Netflix (Dec 4, 2025; all-cash amendment Jan 19, 2026), Paramount Skydance (Feb 27, 2026, \$31 cash plus a ticking fee of \$0.00277778/day after Sept 30, 2026), close Oct 6, 2026. The ticking fee as a contractual price of the hazard rate.
- **15.9 Desk Debrief, The Spec You Hand the Robot, Exercises.**

Six-element coverage: desk framing (15.1, every cold open), derivation (15.2–15.6), AI spec (15.2, 15.4, 15.5), source extraction (15.2, 15.4, 15.5, 15.6), case studies (15.4, 15.7, 15.8 plus EA in 15.2), resource graph (end of 15.1, 15.5, 15.8 and chapter end). Three Trend Watch boxes (15.1, 15.3, 15.5).

---

## 3. Derivation skeletons

### A. The 101 CoC put as a compound option (15.2)

Setup. Bond with coupon $c$, maturity $T$, price $P_t$. Deal announced at $t_0$; closes (if it closes) at random time $\tau_c$. Trigger indicator $\mathbf{1}_{\text{trig}}$ (CoC alone in HY; CoC *and* a below-IG rating event by the named agencies within the window in IG). Strike $K = 101$ plus accrued interest. Under $\mathbb{Q}$ with short rate $r$:

$$
V_{\text{CoC}}(t_0) \;=\; \mathbb{E}^{\mathbb{Q}}\!\left[\, e^{-\int_{t_0}^{\tau_c} r_u\,du}\; \mathbf{1}_{\{\text{deal}\}}\,\mathbf{1}_{\{\text{trig}\mid\text{deal}\}}\,\big(K - P^{\text{post}}_{\tau_c}\big)^{+} \,\right].
$$

Working approximation (state the independence assumptions explicitly, then break them):

$$
V_{\text{CoC}} \;\approx\; \pi_d \cdot \pi_{t\mid d} \cdot B(t_0,\bar\tau_c)\cdot \mathbb{E}^{\mathbb{Q}}\!\left[(K - P^{\text{post}})^{+} \,\middle|\, \text{deal},\text{trig}\right],
$$

where $\pi_d$ is the deal-completion probability, $\pi_{t\mid d}$ the trigger probability given completion, $B$ the discount factor to the expected close, and

$$
P^{\text{post}} \;=\; \sum_{i} c\,e^{-(y^{\text{TSY}}_{t_i} + s^{\text{post}})\,t_i} + 100\,e^{-(y^{\text{TSY}}_{T} + s^{\text{post}})\,T},
\qquad s^{\text{post}} = s_{\text{acq}} + \Delta_{\text{struct}} + \Delta_{\text{lev}}(L_{pf}),
$$

with $L_{pf} = (F_{\text{old}} + F_{\text{new}})/\text{EV}$ the pro-forma leverage (use $F$ for face per the style bible, never $D$), $\Delta_{\text{struct}}$ the structural-subordination penalty for legacy notes left behind at an opco/holdco, and $\Delta_{\text{lev}}$ a Merton-style map from leverage to spread (Ch 6).

Key points to derive, in order:

1. **Conditional moneyness.** $\mathbb{E}[(K-P)^+\mid \text{trig}] \gg \mathbb{E}[(K-P)^+]$ because the ratings trigger fires precisely when $s^{\text{post}}$ is high. Treating trigger and payoff as independent understates the put for LBOs and overstates it for strategic IG buyers. For a strategic IG acquirer with a tighter curve, $P^{\text{post}} > K$ and the put is worthless; the bond instead rallies toward the acquirer's curve (Activision into Microsoft; U.S. Steel into Nippon Steel).
2. **Coupon vintage dominates.** Fix $s^{\text{post}}$; differentiate $P^{\text{post}}$ in $c$. A 1.85% 2031 bond is ~15–20 points below par at 2025–26 Treasury yields before any credit penalty *(illustrative)*; the put is deep ITM on trigger. A 6.875% 2029 note trades above par; the put is OTM. Make the reader compute both.
3. **Double-trigger probability.** $\pi_{t\mid d} = \mathbb{P}(\text{both agencies} < \text{IG within window} \mid \text{deal})$, a logistic in $(L_{pf}, \text{sponsor flag}, \text{acquirer rating})$: near 1 for sponsor LBOs, near 0 for IG strategics. Note the window extension while ratings are "under review" (CHECK exact EA/Activision language; the EA 2021 prospectus supplement confirms the 101% price and the "Change of Control Repurchase Event" term).
4. **Measure.** $\pi_d$ backed out of the equity merger-arb spread is a risk-adjusted ($\mathbb{Q}$-like) number: Mitchell–Pulvino (2001) show risk-arb returns behave like a short index put, so $\mathbb{Q}$ failure probabilities exceed $\mathbb{P}$ ones. Kaplan–Meier hazards from historical deals are $\mathbb{P}$. Never mix them in one formula without saying so.
5. **Error-prone spots.** (a) The put is a *covenant*: legal/covenant defeasance, consent-solicitation strips, and exchange offers can remove it before it pays (EA; WBD June 2025). (b) Accrued interest to, but excluding, the repurchase date; record dates. (c) The offer period makes the put Bermudan-ish; treat as European at $\tau_c$ and bound the error. (d) Legacy notes may be structurally subordinated post-close even when "assumed" (Tapestry prospectus says so in plain words). (e) Do not discount at the target's pre-deal curve; the relevant curve after trigger is the acquirer's.

### B. Portability as a short digital on leverage (15.3)

Portability (a "Specified Change of Control Event") lets the issuer skip the CoC offer if a leverage test holds at the CoC, usually within a window after issue and often only once. Holder's put value becomes

$$
V^{\text{port}}_{\text{CoC}} \;=\; V_{\text{CoC}} \cdot \mathbb{P}\!\left(L_{\tau_c} > \bar L \,\middle|\, \text{deal},\text{trig}\right),
$$

so the issuer holds a digital option struck at $\bar L$ on pro-forma leverage, with value $V_{\text{CoC}}\cdot \mathbb{P}(L_{\tau_c}\le \bar L\mid\cdot)$. Two derivation points: (i) if leverage followed an exogenous diffusion, the digital would be priced like any barrier; (ii) it does not: the acquiring sponsor sets $F_{\text{new}}$ *after* reading $\bar L$, so $\mathbb{P}(L_{\tau_c}\le\bar L)$ is endogenous and close to one whenever the test is loose or uses "Adjusted EBITDA" (Mags: "deeply suspicious of anything called adjusted"). The honest model is a game: sponsor chooses leverage to maximize equity value subject to passing the test; the holder's put is worth roughly its value in the states where the sponsor *cannot* pass, which are the states where the holder most wants it. Error-prone spots: pro-forma EBITDA add-backs (cross-ref Ch 13 add-back caps), the window (often two to three years), "one-time use," and whether the test is net or gross leverage. Measure: this is a contract-design argument under $\mathbb{P}$; pricing the residual put is under $\mathbb{Q}$.

### C. The SMR bond: implied break probability and probabilistic duration (15.4)

Let $\pi_f$ be the probability the deal fails by the outside date $T_f$, $P^{\text{close}}$ the price the bond would carry as an ordinary acquirer bond if the deal closes, and $K_f = 101$ plus accrued. Then

$$
P_0 \;=\; \pi_f\, K_f\, e^{-r T_f} \;+\; (1-\pi_f)\, P^{\text{close}}
\quad\Longrightarrow\quad
\hat\pi_f \;=\; \frac{P^{\text{close}} - P_0}{P^{\text{close}} - K_f\, e^{-rT_f}},
$$

valid when $P^{\text{close}} \ne K_f e^{-rT_f}$ (guard the denominator). Estimate $P^{\text{close}}$ from the issuer's *non-SMR* tranches by curve interpolation, which is why the HPE and Synopsys tranche carve-outs are a gift: same issuer, same day, same ranking, different option. Sign of the option flips with rates: if $P^{\text{close}} > K_f e^{-rT_f}$ (rates fell after issue), holders are *short* a digital call struck at 101 and the SMR hurts; if $P^{\text{close}} < K_f e^{-rT_f}$, the SMR is a free put. Probabilistic duration:

$$
D^{\text{SMR}} \;=\; \pi_f\, D(T_f) + (1-\pi_f)\, D(T), \qquad
\frac{\partial P_0}{\partial \pi_f} = K_f e^{-rT_f} - P^{\text{close}},
$$

so a ruling day moves the hedge ratio discontinuously (Ben Dor p.212's rating-event hedge-ratio collapse is the same phenomenon in a different trigger). Measure: $\hat\pi_f$ is $\mathbb{Q}$. Error-prone: accrued interest convention in $K_f$; no escrow (Synopsys's prospectus says the proceeds are not escrowed), so acquirer credit risk between issue and redemption; the outside date is extendable by mutual agreement (Tapestry: "or such later date mutually agreed"); redemption timing "no earlier than the third business day and no later than 30 days" after notice (Kroger supplemental indenture).

### D. Regulatory timelines as survival analysis (15.5)

Time origin $t=0$ at signing (or HSR filing; say which). Three terminal states: clear/close ($k=c$), abandon ($k=a$), litigated block ($k=b$). Pending deals are right-censored at the data cutoff.

Kaplan–Meier: $\hat S(t) = \prod_{t_i\le t}\big(1 - d_i/n_i\big)$, with Greenwood variance $\widehat{\mathrm{Var}}(\hat S(t)) = \hat S(t)^2\sum_{t_i\le t} \frac{d_i}{n_i(n_i-d_i)}$. Nelson–Aalen: $\hat\Lambda(t)=\sum_{t_i\le t} d_i/n_i$. Cox PH per cause: $h_k(t\mid x) = h_{0,k}(t)\exp(x'\beta_k)$, partial likelihood with Breslow ties; covariates: Second Request flag, horizontal overlap/HHI proxy, deal value, cross-border count of jurisdictions, sponsor flag, administration regime dummy. Competing risks: cause-specific hazards and the cumulative incidence $F_k(t)=\int_0^t S(u^-)\,h_k(u)\,du$ (Aalen–Johansen), with the identity $\sum_k F_k(t) = 1 - S(t)$ as a built-in check. Expected PnL of a long target bond position:

$$
\mathbb{E}[\text{PnL}] = \int_0^\infty e^{-rt}\, S(t)\,\big[\,h_c(t)\,\Pi_c(t) + h_a(t)\,\Pi_a(t) + h_b(t)\,\Pi_b(t)\,\big]\,dt + \text{carry},
$$

where $\Pi_k(t)$ is the price jump on outcome $k$ at $t$. Bayesian drift of the deal probability as silent time passes:

$$
\pi_d(t) = \frac{\pi_d(0)\,\mathbb{P}(\text{no complaint by } t\mid\text{deal})}{\pi_d(0)\,\mathbb{P}(\text{no complaint by } t\mid\text{deal}) + (1-\pi_d(0))\,\mathbb{P}(\text{no complaint by } t\mid\text{break})},
$$

which steps up as the 30-day HSR window, the Second Request compliance date, and the EU Phase I day-25 pass without action. Giglio–Shue (2014) is the empirical anchor for markets underreacting to exactly this.

Error-prone spots: calendar vs. working days (EU and CMA count working days; HSR counts calendar days with a federal-holiday rule); the Second Request restarts the clock from substantial compliance, so "time since signing" is not the right clock for the second waiting period; informative censoring (outside dates get extended when the deal is in trouble, so censoring is not independent of the hazard); immortal-time bias if covariates measured after signing are used (a Second Request is itself a time-varying covariate); small-sample Cox with 40–60 Second Requests per year; regime non-stationarity in $h_{0}(t)$ across administrations. $\mathbb{P}$ throughout; conversion to $\mathbb{Q}$ needs a risk premium (Mitchell–Pulvino).

---

## 4. Code spec: `event_credit_engine.py`

What the reference implementation computes (numpy/scipy/pandas only, seeded):

1. `price_coc_put(deal_prob, trigger_prob_given_deal, post_spread_sampler, coupon, maturity_years, tsy_curve, strike=101.0, n_paths=200_000, seed=7)`: Monte Carlo over post-close spread scenarios, prices the bond at trigger, returns value, standard error, and the conditional moneyness ratio $\mathbb{E}[(K-P)^+\mid\text{trig}]/\mathbb{E}[(K-P)^+]$. Inputs: `post_spread_sampler` returns spreads in decimals (state units); `tsy_curve` as a callable on tenor. Edge cases: `deal_prob` or `trigger_prob` of 0 returns 0 exactly; spreads clipped at 0; maturities shorter than the expected close return 0 with a warning.
2. `smr_price(pi_f, p_close, T_f, r, k=101.0, accrued=0.0)` and `smr_implied_break_prob(p_obs, p_close, T_f, r, ...)`; `smr_duration(pi_f, D_short, D_long)`. Raise if $|P^{\text{close}} - K e^{-rT_f}| < 10^{-6}$ (undefined implied probability); clip $\hat\pi_f$ to $[0,1]$ and report when clipping occurred.
3. `curve_match_close_price(issuer_tranches_df)`: interpolates $P^{\text{close}}$ for an SMR tranche from the issuer's non-SMR tranches by maturity using a monotone spread curve (PCHIP in yield space). Schema: columns `tranche_id, coupon, maturity, price, is_smr`.
4. Survival engine implemented from scratch (no `lifelines`): `kaplan_meier(times, events)` with Greenwood CI; `nelson_aalen`; `aalen_johansen(times, cause)` for CIFs; `cox_ph(times, event, X)` via scipy.optimize on the Breslow partial likelihood with analytic gradient; `synthetic_deal_cohort(n=600, seed=11)` generating cause-specific Weibull times with covariates `second_request, horizontal, log_value, n_jurisdictions, sponsor, regime` and random right-censoring; `bayes_deal_prob_path(pi0, milestone_schedule, p_no_action_given_deal, p_no_action_given_break)`.

Tensor shapes: `times (n,)`, `event (n,) in {0,1}`, `cause (n,) in {0,1,2,3}`, `X (n,p)`; Cox returns `beta (p,)`, `se (p,)`, baseline cumulative hazard `(m,2)`.

Built-in sanity checks (asserted at module run):
- `price_coc_put` with a degenerate sampler ($s^{\text{post}}$ constant) equals the closed-form $\pi_d\pi_{t|d}B\,(K-P)^+$ to within MC error; with a spread so tight that $P>K$ in every path it returns exactly 0.
- `smr_implied_break_prob(smr_price(pi), ...)` round-trips to `pi` within $10^{-10}$ for a grid of $\pi\in\{0,0.1,\dots,1\}$.
- With no censoring, `kaplan_meier` equals $1-$ ECDF at every event time; `aalen_johansen` CIFs sum to $1-\hat S(t)$ within $10^{-12}$; `cox_ph` recovers the synthetic $\beta$ within two standard errors on the seeded cohort; a Schoenfeld-residual slope test is reported (not asserted).
- `bayes_deal_prob_path` is monotone non-decreasing between adverse events and equals `pi0` at $t=0$.

Numerical guards: log-sum-exp in the partial likelihood; ties handled by Breslow; empty risk sets skipped; day-count stated (ACT/365 for survival clocks; 30/360 for accrued on US corporates); working-day calendars passed explicitly as a parameter, never inferred.

---

## 5. Source map (shelf)

| Citation | Why | Verbatim quotation (≤60 words) |
| :--- | :--- | :--- |
| Bohn_Stein_Active_Credit_Portfolio_Management p.232 | Kaplan–Meier motivated by firms leaving the sample through M&A; the chapter's survival section opens on it | "But what happens if some of the firms drop out of the sample due to, say, a merger or acquisition? In this case, adjustments can be made to sample survival functions of the sort shown in Figure 4.3 to account for this censorship. This results in a particular form of survival function estimator called the Kaplan-Meier (sometimes called the product limit) estimator" |
| Bohn_Stein_Active_Credit_Portfolio_Management p.233 | Cox PH statement and the proportional-hazards restriction, reused for deal covariates | "Under this specification, the shape of the hazard function (and the corresponding survival function) is arbitrary, but the impact ratio of the hazards over time is constant" |
| Bohn_Stein_Active_Credit_Portfolio_Management p.228 | Right censoring defined; pending deals are censored observations | "The technical term for this is right censoring, and it is a common feature of many default data sets." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.231 | Duration models model time-to-event, which is what a timeline model is | "Duration specifications directly model the duration of survival (rather than the presence or absence of a default event), so that the dependent variable is taken as the time until default." |
| Veronesi_Fixed_Income_Securities p.470 | Issuer exercise is not guaranteed optimal; sponsors defease instead of paying the put | "The key to the dynamic replication is that the issuer behaves as the model prescribes it should. However, exercising an American option optimally is not mandatory, and it is perfectly reasonable that the issuer may exercise sub-optimally." |
| Veronesi_Fixed_Income_Securities p.467 | OAS is model-dependent; an "event-adjusted spread" inherits the same caveat | "It is also important to realize that the size of the OAS depends on the model used to compute it" |
| Schmid_Credit_Risk_Pricing_Models p.153 | Bond puts as spread hedges; the CoC put is a credit put with a legal trigger | "Credit options offer protection against changing default free interest rates and changing credit spreads. Hence, they allow hedging of mark-to-market exposure to fluctuations in spreads and interest rates: hedging long positions with puts, and short positions with calls." |
| Moyer_Distressed_Debt_Analysis p.267 | The early-redemption option premium encodes a probability; template for the SMR implied probability | "The size of the premium would implicitly reflect the probability that investors placed on the refinancing." |
| Moyer_Distressed_Debt_Analysis p.230 | Time-to-event discipline; process steps take calendar time | "Exchange offers typically take at least 60 days to plan and complete." |
| Ben_Dor_Quantitative_Credit_Portfolio_Management p.212 | Hedge ratios jump at rating events; the CoC/SMR trigger does the same to duration | "For bonds initially rated investment grade, the typical limit hedge ratio (beta) decreased from 1.00 to 0.45 after the" (sentence continues on p.213) |
| Ben_Dor_Quantitative_Credit_Portfolio_Management p.275 | Three adverse credit events; an M&A trigger is the fourth, contractual one | "measuring exposures to three different types of adverse credit events: systematic changes in spreads, either market-wide or across a particular sector; issuer-specific spread changes; and defaults." |
| Dynkin_Systematic_Investing_in_Credit p.411 | Forced-selling price pressure after downgrade; relevant to LBO-driven fallen angels | "bonds downgraded from investment grade to high yield (fallen angels) tend to outperform their new peers after the downgrade due to price pressures around the downgrade event." |
| Houlihan_Lokey_Distressed_MA p.55 | Court-scheduled process dates are survival clocks too (363 timeline) | "The Court denies all objections and approves the break-up fee and bidding procedures, as well as the dates for the auction and final sale hearing." |
| Paleologo_Advanced_Portfolio_Management p.152 | Event-trade sizing heuristics, for the sizing subsection | "If the time from thesis formation to the event is shorter, everything else being equal, the size at the event should be smaller because there is less time to build it" |
| Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.18 | Framework language for idiosyncratic event risk inside a systematic book | "good portfolio management is about understanding the nexus of risks that a credit portfolio faces, both external risks – idiosyncratic and systematic default risk, downgrades and spread volatility – and internal risks" |

---

## 6. RESEARCH DOSSIER

### 6.1 Kroger–Albertsons and the \$4.7bn special mandatory redemption (VERIFIED)

- Merger agreement dated October 13, 2022 (cited in both companies' termination 8-Ks). FTC et al. v. The Kroger Co. and Albertsons Companies, D. Or., Case No. 3:24-cv-00347-AN, filed Feb 26, 2024 (CourtListener docket: https://www.courtlistener.com/docket/68284514/federal-trade-commission-v-kroger-company/). Preliminary injunction granted December 10, 2024; Albertsons terminated the same day under §8.1(e) (Albertsons 8-K, Dec 11, 2024: https://www.sec.gov/Archives/edgar/data/1646972/000164697224000231/aci-20241210.htm). Signing to block: ~26 months.
- Bonds: Kroger issued \$10.5bn on August 27, 2024 in seven tranches: \$1.0bn 4.700% 2026, \$1.0bn 4.600% 2027, \$1.4bn 4.650% 2029, \$1.3bn 4.900% 2031, \$2.2bn 5.000% 2034, \$2.1bn 5.500% 2054, \$1.5bn 5.650% 2064, under the Fiftieth Supplemental Indenture (8-K: https://www.sec.gov/Archives/edgar/data/56873/000110465924093481/tm2421523d7_8k.htm).
- SMR clause (supplemental indenture): redemption "at a redemption price equal to 101% of their principal amount, plus accrued and unpaid interest"; trigger date is the earliest of the company's notice that it will not pursue the merger, the SMR Outside Date, or termination of the merger agreement; the redemption date "shall be no earlier than the third business day and no later than 30 days following the date of such notice" (https://www.sec.gov/Archives/edgar/data/56873/000110465924093481/tm2421523d7_ex4-3d1.htm). Optional redemption otherwise at T+15bp make-whole.
- Trigger: Kroger delivered its termination notice Dec 11, 2024; issued the SMR notice Dec 12; redeemed the SMR Notes (the 2026, 2027, 2029 and 2031 tranches, \$4.7bn) on December 18, 2024 at 101% plus accrued (8-K Item 2.04, Dec 13, 2024: https://www.sec.gov/Archives/edgar/data/56873/000110465924128106/tm2430972d1_8k.htm). The three long tranches (\$5.8bn) had no SMR and stayed outstanding. Kroger simultaneously announced a \$7.5bn buyback including a \$5bn ASR (Dec 11 release: https://www.sec.gov/Archives/edgar/data/56873/000110465924127669/tm2427516d10_ex99-1.htm).
- Side mechanics worth a paragraph: Kroger had launched exchange offers (Aug 15, 2024) for up to \$7,441,608,000 of new Kroger notes in exchange for Albertsons-family notes, with \$6,819,427,000 tendered by the early date (Aug 29, 2024 release: https://www.sec.gov/Archives/edgar/data/56873/000110465924094605/tm2422992d1_ex99-1.htm). The exchange was the acquirer's alternative to a CoC offer on target bonds; settlement was conditioned on closing (CHECK the condition language).
- Bond price paths around Dec 10–18, 2024 are not sourced here; label any numbers *illustrative*.

### 6.2 Electronic Arts: the largest take-private, the ITM put, and the defeasance (VERIFIED, interpretation flagged)

- Sept 29, 2025: EA agreed to be acquired by PIF, Silver Lake and Affinity Partners for \$210/share cash, ~\$55bn enterprise value, 25% premium to the \$168.32 unaffected close of Sept 25, 2025; PIF rolling its 9.9% stake; described as "the largest all-cash sponsor take-private investment in history" (https://www.sec.gov/Archives/edgar/data/712515/000114036125036415/ef20056167_ex99-1.htm).
- Legacy notes: \$750mm 1.850% Senior Notes due 2031 and \$750mm 2.950% Senior Notes due 2051, issued Feb 2021, with a "Change of Control Repurchase Event" offer at "101% of the aggregate principal amount of the notes to be repurchased plus any accrued and unpaid interest" (2021 prospectus supplement: https://www.sec.gov/Archives/edgar/data/712515/000119312521036296/d48559d424b2.htm). The exact IG double-trigger window language: CHECK in that document.
- July 30, 2026: all regulatory approvals obtained; close expected Aug 4, 2026 (https://www.sec.gov/Archives/edgar/data/712515/000114036126030255/ef20078929_8k.htm). Signing to close: ~10 months.
- Aug 4, 2026 closing 8-K (https://www.sec.gov/Archives/edgar/data/712515/000114036126031157/ef20079099_8k.htm): first-lien TLB \$6,125mm plus €1,725mm, TLA \$3,250mm, \$500mm revolver (JPMorgan agent); new notes issued April 8, 2026: \$2,875mm 7.250% senior secured due 2033, €1,080mm 6.250% senior secured due 2033, \$2,500mm 8.750% senior notes due 2034; 40% equity claw at 107.25/106.25/108.75. Tender offers for the legacy 2031s and 2051s launched Feb 10, 2026 and expired July 30, 2026: only \$68.830mm of 2031s and \$7.922mm of 2051s tendered, leaving \$681.170mm and \$742.078mm outstanding; Parent then "caused the Company to defease certain obligations" under the 2016/2021 indenture by irrevocably depositing U.S. Government Obligations sufficient to pay principal, premium, if any, and interest when due.
- Our reading (label as analysis, CHECK against the indenture's defeasance article and the rating actions): with coupons of 1.85% and 2.95%, the legacy notes traded far below par, so a triggered 101 put would have been deeply in the money; defeasing with Treasuries satisfies the payment obligations and, under a covenant-defeasance provision, releases the issuer from the repurchase covenant, so holders receive Treasury-backed scheduled cash flows rather than 101 today. The lesson for the chapter: the CoC put is a covenant, and a sponsor with cash can defease the covenant. Tender price and rating-agency actions: CHECK.

### 6.3 Tapestry–Capri: \$6.1bn redeemed at 101, \$61.1mm premium (VERIFIED)

- Notes issued Nov 2023 (USD and EUR series; EUR notes NYSE-listed as TPR25A, TPR27A, TPR31) with SMR if the Capri acquisition was not completed by February 10, 2025 "(or such later date mutually agreed between us and Capri)", on termination, or on notice; prospectus also warns the notes would be "structurally subordinated to certain indebtedness assumed in connection with the Capri Acquisition" (424B5: https://www.sec.gov/Archives/edgar/data/1116132/000114036123053903/ny20014590x5_424b5.htm).
- FTC v. Tapestry, Inc., S.D.N.Y. 1:24-cv-03109, filed Apr 23, 2024 (https://www.courtlistener.com/docket/68465585/federal-trade-commission-v-tapestry-inc/); PI granted Oct 24, 2024 (CHECK date). Termination Nov 14, 2024; redemption of \$6.1bn "in accordance with the Special Mandatory Redemption feature, for a price equal to 101%"; funded with cash on hand; redemption on or about Nov 25, 2024; \$61.1mm redemption premium and \$57.1mm of unamortized hedge losses/issuance costs expensed; no break fee, ~\$45mm expense reimbursement to Capri (8-K and release: https://www.sec.gov/Archives/edgar/data/1116132/000114036124046713/ef20038690_8k.htm ; https://www.sec.gov/Archives/edgar/data/1116132/000114036124046713/ef20038690_ex99-1.htm). Deal announced Aug 2023 at ~\$8.5bn: CHECK.

### 6.4 HPE–Juniper: SMR on four of six tranches, DOJ suit, settlement (VERIFIED)

- Sept 2024 notes: the 2029, 2031, 2034 and 2054 notes carry the SMR at 101% if the Juniper acquisition has not closed by the later of five business days after Oct 9, 2025 or an extended End Date; the 2026 and 2027 notes do not; the offering also discloses a Change of Control Repurchase Event offer (424B2: https://www.sec.gov/Archives/edgar/data/1645590/000114036124041193/ny20035638x9_424b2.htm).
- Deal announced Jan 9, 2024 at \$40/share, ~\$14bn equity value. DOJ sued Jan 30, 2025 (United States v. Hewlett Packard Enterprise Co., N.D. Cal. 5:25-cv-00951: https://www.courtlistener.com/docket/69592345/united-states-v-hewlett-packard-enterprise-co/ ; HPE response: https://www.sec.gov/Archives/edgar/data/1645590/000164559025000007/pressrelease.htm). Settlement announced June 28, 2025 (release in July 2, 2025 8-K: https://www.sec.gov/Archives/edgar/data/1645590/000114036125024519/ef20051378_ex99-2.htm); closing July 2, 2025 (CHECK). Signing to close: ~18 months. The SMR tranches vs. the 2026/2027 non-SMR tranches are the chapter's worked example for the implied break probability.

### 6.5 Synopsys–Ansys: SMR on the short tranches, closed July 17, 2025 (VERIFIED)

- March 2025 ~\$10bn offering: the 2027, 2028, 2030 and 2032 notes carry the SMR at 101%; the 2035 and 2055 notes do not; "The proceeds from this offering will not be deposited into an escrow account" (424B5: https://www.sec.gov/Archives/edgar/data/883241/000114036125007235/ny20044174x7_424b5.htm).
- Announced Jan 16, 2024; completed July 17, 2025 (https://www.sec.gov/Archives/edgar/data/883241/000114036125026139/ef20051970_ex99-1.htm); an 8-K of July 14, 2025 precedes closing (China SAMR clearance: CHECK). Signing to close: ~18 months; the SMR expired worthless, which is the base case the writer must price too.

### 6.6 U.S. Steel–Nippon Steel: regulatory risk beyond antitrust (VERIFIED)

- June 13, 2025: presidential approval by executive order; National Security Agreement with Treasury and Commerce; a "Golden Share" (Class G preferred) issued to the U.S. Government; ~\$11bn of investment commitments by 2028; DOJ review completed (https://www.sec.gov/Archives/edgar/data/1163302/000110465925059596/tm2518073d1_ex99-1.htm). Closing 8-K June 18, 2025: the 5.00% Senior Convertible Notes due 2026 became convertible solely into cash (a Share Exchange Event); Eleventh Supplemental Indenture for the 6.65% notes due 2037 and 6.875% notes due 2029 (https://www.sec.gov/Archives/edgar/data/1163302/000110465925060674/tm2517314d1_8k.htm). Announced Dec 18, 2023 and blocked by presidential order Jan 3, 2025 before being approved: CHECK. Use as the OTM-put example (high-coupon notes into a stronger acquirer) and as the CFIUS/presidential hazard.

### 6.7 Spirit–JetBlue: the merger as the credit (VERIFIED)

- Jan 16, 2024: D. Mass. granted DOJ's request for a permanent injunction (Spirit 8-K: https://www.sec.gov/Archives/edgar/data/1498710/000149871024000045/save-20240116.htm). Jan 19, 2024 investor update: \$1.3bn liquidity at Dec 31, 2023; sale-leasebacks of 25 aircraft (https://www.sec.gov/Archives/edgar/data/1498710/000149871024000047/investorguidance11924.htm).
- Mar 4, 2024: termination by mutual agreement; JetBlue paid Spirit \$69mm; Spirit stockholders had received ~\$425mm of prepayments while the agreement was in effect; Spirit retained Perella Weinberg and Davis Polk (https://www.sec.gov/Archives/edgar/data/1498710/000149871024000124/a240304pressreleasefinal.htm).
- Nov 18, 2024: prearranged Chapter 11 in S.D.N.Y. with an RSA signed by a supermajority of loyalty and convertible bondholders; \$350mm backstopped equity investment; equitization of \$795mm of funded debt; \$300mm DIP from existing bondholders; aircraft lessors and secured aircraft debt unimpaired (https://www.sec.gov/Archives/edgar/data/1498710/000095010324016405/dp220813_ex9901.htm). Deal terms (July 2022, \$33.50/share) and the 8.00% senior secured loyalty notes due 2025: CHECK. Signing to block: ~18 months; block to bankruptcy: ~10 months.

### 6.8 Microsoft–Activision (partly VERIFIED)

- Microsoft 8-K filed Oct 13, 2023 reporting completion (EDGAR accession 0001193125-23-255762; listed, not opened). Ninth Circuit, FTC v. Microsoft Corp., No. 23-15992, decided May 7, 2025 (https://www.courtlistener.com/opinion/10553007/ftc-v-microsoft-corporation/); it affirmed the denial of the FTC's preliminary injunction (CHECK holding text). District-court PI denial July 10, 2023 and the \$68.7bn deal value: CHECK. Activision's Aug 2020 notes carried a "Change of Control Repurchase Event" (424B5 listed on EDGAR: https://www.sec.gov/Archives/edgar/data/718877/000104746920004447/a2242201z424b5.htm, not opened). Teaching point: a AAA acquirer means the ratings leg of the double trigger cannot fire; the put is worthless and the bonds migrate to the acquirer's curve.

### 6.9 Warner Bros. Discovery 2025–26: covenant strip, three suitors, ticking fee (VERIFIED)

- June 9, 2025 tender offers and consent solicitations for substantially all notes of Discovery Communications, WarnerMedia Holdings, Warner Media LLC and Historic TW; requisite consents received June 16, 2025; supplemental indentures "eliminate substantially all of the restrictive covenants" and certain events of default once operative (https://www.sec.gov/Archives/edgar/data/1437107/000143710725000151/disca-20250613.htm). Whether the CoC put survived the strip for each series: CHECK.
- A \$15bn "Non-Investment Grade Leveraged Bridge Loan Agreement" dated June 26, 2025 was refinanced June 4, 2026 with a 7-year \$13bn TLB (SOFR+250) and €1,717mm TLB (EURIBOR+250) at Discovery Global Holdings, maturing June 4, 2033; a CoC, "such as the consummation of the previously disclosed proposed acquisition of the Company by Paramount Skydance Corporation," permits acceleration (https://www.sec.gov/Archives/edgar/data/1437107/000119312526256559/d11897d8k.htm).
- Dec 4, 2025: merger agreement with Netflix (holdco merger, spin of Global Linear Networks, Netflix acquires Streaming & Studios) (https://www.sec.gov/Archives/edgar/data/1437107/000119312525309873/d73469d8k.htm); Jan 19, 2026: amended so the \$27.75/share consideration is all cash (https://www.sec.gov/Archives/edgar/data/1437107/000119312526015949/d61836d8k.htm).
- Feb 27, 2026: agreement with Paramount Skydance at \$31.00 cash per share plus "Ticking Consideration" of \$0.00277778 per day after Sept 30, 2026, capped at \$0.25 per 90 days (https://www.sec.gov/Archives/edgar/data/1437107/000143710726000018/disca-20260227.htm). Stockholders approved Apr 23, 2026 (1,742,843,087 for; 16,260,135 against) (https://www.sec.gov/Archives/edgar/data/1437107/000119312526173660/d435468d8k.htm). Closed Oct 6, 2026 at \$31.01666668 including \$41,886,975.78 of aggregate ticking consideration; WBD repaid the June 2026 term loans and the Oct 2024 revolver; WBD subsidiaries guaranteed Skydance's new notes (indenture dated Oct 5, 2026) and its April 7, 2026 credit agreement (https://www.sec.gov/Archives/edgar/data/1437107/000119312526415055/d200872d8k.htm). The ticking fee annualizes to roughly 3.3% of \$31 (\$0.00277778 × 365 ≈ \$1.014), a contractual price of delay the chapter can compare with a hazard-rate-implied carry.

### 6.10 Union Pacific–Norfolk Southern: a non-HSR clock (VERIFIED)

- July 29, 2025: agreement valuing NSC at \$85bn EV (\$320/share implied; 25% premium to the 30-day VWAP), ~\$2.75bn synergies (https://www.sec.gov/Archives/edgar/data/100885/000119312525167154/d64537dex991.htm). Nov 14, 2025: 99.5% of UNP votes cast in favor (https://www.sec.gov/Archives/edgar/data/100885/000010088525000332/exhibit991.htm). Dec 19, 2025: ~7,000-page STB application filed, "subject to STB review and approval within its statutory timeline" (https://www.sec.gov/Archives/edgar/data/100885/000010088525000347/exhibit991.htm). STB major-merger statutory schedule (roughly 16 months from acceptance): CHECK. Any acquisition bonds with SMR for this deal: CHECK (none found in EDGAR full-text search through Oct 2026).

### 6.11 HSR statistics, FY2016–FY2025 (VERIFIED from the FTC/DOJ annual reports)

Source PDFs: FY2023 https://www.ftc.gov/system/files/ftc_gov/pdf/fy2023hsrreport.pdf ; FY2024 https://www.ftc.gov/system/files/ftc_gov/pdf/FY24-HSR-ANNUAL-REPORT-FOR-TRANSMITTAL-TO-CONGRESS.pdf ; FY2025 https://www.ftc.gov/system/files/ftc_gov/pdf/fy_2025_hsr_annual_report_for_transmittal_to_congress.pdf (Appendix A, "Summary of Transactions by Fiscal Year").

| FY | Transactions reported | Adjusted (2nd Request possible) | Second Requests (FTC + DOJ) | Share of adjusted | Early terminations granted |
| :-- | --: | --: | --: | --: | --: |
| 2016 | 1,832 | 1,772 | 54 (25+29) | 3.0% | 1,102 |
| 2017 | 2,052 | 1,992 | 51 (33+18) | 2.6% | 1,220 |
| 2018 | 2,111 | 2,028 | 45 (26+19) | 2.2% | 1,170 |
| 2019 | 2,089 | 2,030 | 61 (30+31) | 3.0% | 1,107 |
| 2020 | 1,637 | 1,580 | 48 (23+25) | 3.0% | 861 |
| 2021 | 3,520 | 3,413 | 66 (43+23) | 1.9% | 417 |
| 2022 | 3,152 | 3,029 | 47 (25+22) | 1.6% | 5 |
| 2023 | 1,805 | 1,735 | 37 (26+11) | 2.1% | 0 |
| 2024 | 2,031 | 1,973 | 59 (30+29) | 3.0% | 3 |
| 2025 | 2,006 | 1,944 | 41 (20+21) | 2.1% | 265 |

Notes: the FY2021 report shows 65 Second Requests in the FY2023 table and 66 in the FY2025 table (agency restatement; cite the later table). Aggregate reported transaction value: \$1.6tn (FY2023), \$2.1tn (FY2024), \$2.5tn (FY2025). Share of transactions over \$1bn: "approximately one-fourth" (FY2024), 31.8% (FY2025). FY2024 merger enforcement actions: 32, of which FTC 18 with six litigated (FTC release, Sept 17, 2025: https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-doj-issue-fiscal-year-2024-hart-scott-rodino-annual-report). FY2023: clearance to investigate granted in 10.2% of reported transactions.

### 6.12 HSR form and thresholds, 2025–26 (VERIFIED from https://www.ftc.gov/enforcement/premerger-notification-program)

- New HSR form took effect Feb 10, 2025. A federal district court vacated it (FTC notice dated Feb 12, 2026); the Fifth Circuit granted an administrative stay (Feb 19, 2026) and then denied the Commission's motion for a stay pending appeal (Mar 19, 2026); the agencies now accept filings on the pre-Feb 10, 2025 form and still accept the new form. 2026 filing fees and thresholds effective Feb 17, 2026 (dollar level: CHECK on the "Current Thresholds" page). Statutory waiting periods (30 days; 15 for cash tender offers; Second Request restarts the clock on substantial compliance): CHECK against the statute page; the DOJ page returned HTTP 401 this session.

### 6.13 Non-US clocks

- European Commission: Phase I "25 working days"; Phase II 90 working days from opening, with extensions of 15 or 20 working days (VERIFIED: https://competition-policy.ec.europa.eu/mergers/procedures_en).
- UK CMA: revised jurisdiction and procedure guidance (CMA2, December 2025) applies to Phase 1 cases opened on or after Dec 19, 2025 (VERIFIED page: https://www.gov.uk/government/publications/mergers-guidance-on-the-cmas-jurisdiction-and-procedure); Phase 1 40 working days and Phase 2 24 weeks (+8): CHECK in the PDF.
- China SAMR, CFIUS (45-day review + 45-day investigation + presidential 15 days), STB: CHECK all.

### 6.14 EDGAR full-text time series (approximate; counts filings, not deals; duplicates across preliminary/final prospectuses; most HY indentures are 144A and never filed). Query root: https://efts.sec.gov/LATEST/search-index (UI: https://www.sec.gov/edgar/search/). Run 2026-10-17.

| Year | 424B2/424B5/424B3 mentioning "special mandatory redemption" | 8-Ks containing "notice of special mandatory redemption" (actual triggers) | 424B2/424B5 with "Change of Control Triggering Event" | 424B2/424B5 with "Change of Control Repurchase Event" | Any filing with "Specified Change of Control Event" (portability term) |
| :-- | --: | --: | --: | --: | --: |
| 2018 | 71 | 44 | 229 | 105 | 1 |
| 2019 | 60 | 34 | 245 | 119 | 4 |
| 2020 | 49 | 16 | 409 | 196 | 8 |
| 2021 | 69 | 42 | 265 | 227 | 11 |
| 2022 | 41 | 21 | 179 | 89 | 2 |
| 2023 | 52 | 35 | 234 | 97 | 3 |
| 2024 | 79 | 37 | 278 | 203 | 5 |
| 2025 | 48 | 36 | 268 | 231 | 5 |
| 2026 YTD | 59 | 36 | 219 | 149 | 10 |

Reading: IG CoC-put language is near-universal in registered new issues (the two defined terms are the Triggering-Event and Repurchase-Event variants of the same double trigger); SMR triggers run at roughly 15–45 per year with 2020 the trough (deals that could not be financed) and 2021 a peak (deals that failed in the 2021 regulatory turn). Treat portability counts as unusable for levels and use them only to show that the term now appears in public filings; for shares of HY deals with portability, CHECK Covenant Review / Xtract / 9fin reports (European HY has long run well above US HY in portability incidence; the US share rose through 2021 and again in 2024–25: direction CHECK, numbers CHECK).

### 6.15 Academic literature (Crossref-verified DOIs; use title + author + year + DOI)

Event risk and poison puts: Asquith & Wizman (1990), *Event risk, covenants, and bondholder returns in leveraged buyouts*, JFE, DOI 10.1016/0304-405X(90)90026-V. Crabbe (1991), *Event Risk: An Analysis of Losses to Bondholders and "Super Poison Put" Bond Covenants*, JF, DOI 10.1111/j.1540-6261.1991.tb02680.x. Lehn & Poulsen (1991), *Contractual Resolution of Bondholder-Stockholder Conflicts in Leveraged Buyouts*, JLE, DOI 10.1086/467238. Warga & Welch (1993), *Bondholder Losses in Leveraged Buyouts*, RFS, DOI 10.1093/rfs/6.4.959. Cook & Easterwood (1994), *Poison Put Bonds: An Analysis of Their Economic Role*, JF, DOI 10.1111/j.1540-6261.1994.tb04787.x. David (1998), *Pricing the Strategic Value of Poison Put Bonds*, FEDS 1998-06, DOI 10.17016/feds.1998.06 (the game-theoretic valuation the chapter's §15.2 should cite). Billett, Jiang & Lie (2010), *The effect of change-in-control covenants on takeovers: Evidence from leveraged buyouts*, JCF, DOI 10.1016/j.jcorpfin.2009.09.005. Qiu & Yu (2009), *The market for corporate control and the cost of debt*, JFE, DOI 10.1016/j.jfineco.2008.10.002. Cremers, Nair & Wei (2007), *Governance Mechanisms and Bond Prices*, RFS, DOI 10.1093/revfin/hhm006. Chava, Kumar & Warga (2010), *Managerial Agency and Bond Covenants*, RFS, DOI 10.1093/rfs/hhp072. Bao & Hou (2017), *De Facto Seniority, Credit Risk, and Corporate Bond Prices*, RFS, DOI 10.1093/rfs/hhx082. Alp Paukowits, Helwege & Liu (2025), *Debt Maturity, Takeover Risk, and De Facto Seniority*, SSRN 5016909, DOI 10.2139/ssrn.5016909.

Bondholder wealth in M&A: Billett, King & Mauer (2004), *Bondholder Wealth Effects in Mergers and Acquisitions*, JF, DOI 10.1111/j.1540-6261.2004.00628.x. Renneboog & Szilagyi (2008), *Corporate Restructuring and Bondholder Wealth*, EFM, DOI 10.1111/j.1468-036X.2007.00414.x. Furfine & Rosen (2011), *Mergers increase default risk*, JCF, DOI 10.1016/j.jcorpfin.2011.03.003. Bessembinder, Kahle, Maxwell & Xu (2009), *Measuring Abnormal Bond Performance*, RFS, DOI 10.1093/rfs/hhn105. Chen, Ho, Ho & Nie (2022), *CEO overconfidence and bondholder wealth effects*, JCF, DOI 10.1016/j.jcorpfin.2022.102278. Jankowitsch & Pauer (2023), *The Effect of Credit, Liquidity and Rollover Risk on Bondholder Wealth in M&A*, SSRN 4616953. Acharya & Johnson (2010), *More insiders, more insider trading: Evidence from private-equity buyouts*, JFE, DOI 10.1016/j.jfineco.2010.08.002 (CDS moves before LBO announcements).

Merger arbitrage and deal timing: Mitchell & Pulvino (2001), *Characteristics of Risk and Return in Risk Arbitrage*, JF, DOI 10.1111/0022-1082.00401. Baker & Savaşoglu (2002), *Limited arbitrage in mergers and acquisitions*, JFE, DOI 10.1016/S0304-405X(02)00072-7. Mitchell, Pulvino & Stafford (2004), *Price Pressure around Mergers*, JF, DOI 10.1111/j.1540-6261.2004.00626.x. Hsieh & Walkling (2005), *Determinants and implications of arbitrage holdings in acquisitions*, JFE, DOI 10.1016/j.jfineco.2004.08.003. Officer (2003), *Termination fees in mergers and acquisitions*, JFE, DOI 10.1016/S0304-405X(03)00119-3. Bates & Lemmon (2003), *Breaking up is hard to do?*, JFE, DOI 10.1016/S0304-405X(03)00120-X. Jetley & Ji (2010), *The Shrinking Merger Arbitrage Spread*, FAJ, DOI 10.2469/faj.v66.n2.3. Giglio & Shue (2014), *No News Is News: Do Markets Underreact to Nothing?*, RFS, DOI 10.1093/rfs/hhu052. Bhagwat, Dam & Harford (2016), *The Real Effects of Uncertainty on Merger Activity*, RFS, DOI 10.1093/rfs/hhw061. Dikova, Sahib & van Witteloostuijn (2010), *Cross-border acquisition abandonment and completion*, JIBS, DOI 10.1057/jibs.2009.10 (duration/abandonment modeling). Halskov (2024), *Improving Merger Arbitrage Returns with Machine Learning*, SSRN 4765067.

Antitrust and merger review: Wollmann (2019), *Stealth Consolidation: Evidence from an Amendment to the Hart-Scott-Rodino Act*, AER: Insights, DOI 10.1257/aeri.20180137. Cunningham, Ederer & Ma (2021), *Killer Acquisitions*, JPE, DOI 10.1086/712506. Kepler, Naiker & Stewart (2023), *Stealth Acquisitions and Product Market Competition*, JF, DOI 10.1111/jofi.13256.

Delaware proxy-put cases (CourtListener-listed): *San Antonio Fire & Police Pension Fund v. Amylin Pharmaceuticals* (Del. 2009, No. 268, 2009: https://www.courtlistener.com/opinion/1912459/san-antonio-fire-police-pension-fund-v-amylin-pharmaceuticals-inc/); *Kallick v. SandRidge Energy* (Del. Ch. Mar. 8, 2013, C.A. No. 8182-CS: https://www.courtlistener.com/opinion/5146646/kallick-v-sandridge-energy-inc/). Holdings (boards may not use "continuing director" proxy puts to entrench; duty to consider approving dissident slates): CHECK text; opinion pages are JS-rendered and did not parse this session. *Pontiac General Employees Retirement System v. Healthways* (Del. Ch. 2014): TITLE-ONLY.

### 6.16 Trend summary for the Trend Tracker (App C)

1. **Regulatory regime as hazard regime.** Early terminations granted collapsed from 1,102 (FY2016) to 0 (FY2023) and partly returned (265, FY2025); Second-Request incidence oscillated 1.6%–3.0%; FY2024 saw 32 enforcement actions. Blocks of Kroger–Albertsons (Dec 2024), Tapestry–Capri (Oct 2024, CHECK), JetBlue–Spirit (Jan 2024) versus settlements/clearances of HPE–Juniper (June 2025), Synopsys–Ansys (July 2025), U.S. Steel (June 2025), EA (July 2026), WBD–Paramount Skydance (Oct 2026). Model as a shift in $h_{0,b}(t)$ and in $\pi_{\text{complaint}\mid\text{Second Request}}$.
2. **SMR issuance scales with mega-deal financing;** 2024 was the busiest year for SMR prospectus language in the 2018–26 EDGAR series (79 filings) and FY2025 the largest aggregate HSR value (\$2.5tn).
3. **Sponsor take-privates returned at IG scale** (EA \$55bn; \$20bn+ of new LBO debt including 7.25%/8.75% notes), re-pricing IG event risk and reviving the 1988–89 "event risk covenant" literature; defeasance and covenant strips are the 2025–26 counter-moves.
4. **Ticking fees and all-cash re-cuts** (WBD) price time explicitly; a desk can compare the contractual per-diem with a survival-implied carry.
5. **HSR form churn** (new form Feb 2025, vacated Feb 2026, stay denied Mar 2026) adds procedural variance to the first 30 days of every clock.

---

## 7. Case studies (sourced key facts above)

1. **Kroger–Albertsons (2022–2024): the SMR as deal-break gauge.** Signing Oct 13, 2022; FTC suit Feb 26, 2024; \$10.5bn notes Aug 27, 2024 with SMR on \$4.7bn across four short tranches; PI Dec 10, 2024; termination Dec 10–11; SMR notice Dec 12; redemption Dec 18 at 101. Teach: curve-match the SMR tranches against the 2034/2054/2064 notes to back out $\hat\pi_f$ through the autumn hearing; show the duration jump on Dec 10; discuss who was long the short tranches above 101 (sign flip) and the \$7.4bn ACI exchange offers as the target-bond leg. Price paths: illustrative.
2. **Electronic Arts (2025–2026): the ITM CoC put that got defeased.** \$55bn take-private; legacy 1.85% 2031 and 2.95% 2051 notes with a 101 Change of Control Repurchase Event; tiny tender participation (\$76.8mm of \$1.5bn) then defeasance with Treasuries at closing. Teach: coupon-vintage moneyness; the double trigger; why a sponsor pays Treasuries rather than 101; what a systematic desk should have flagged (a defeasance article in the base indenture is a document feature for Ch 13's state space). Interpretation flagged CHECK.
3. **Warner Bros. Discovery (2025–2026): three suitors, a covenant strip, a ticking fee.** June 2025 tender/consent strip; \$15bn bridge with "Non-Investment Grade" in its name; Netflix Dec 2025 then all-cash Jan 2026; Paramount Skydance Feb 27, 2026 at \$31 plus \$0.00277778/day after Sept 30, 2026; shareholder vote Apr 23, 2026; close Oct 6, 2026 with \$41.9mm of ticking consideration. Teach: competing-bidder optionality in the target's bonds, acceleration-on-CoC in the term loan, and the ticking fee as a contractual hazard-rate price. (Supporting: Spirit–JetBlue as the "deal dies, credit dies" branch; Tapestry/HPE/Synopsys as the SMR outcome distribution: triggered, nearly triggered, expired worthless.)

---

## 8. Humor beats (all ride on a correct idea)

1. **Cold open.** Kaz: "Why would a company that has not defaulted *mandatorily* redeem bonds at a premium?" Theo: "Because the alternative was owning Albertsons." Mags: "Price is what you pay. 101 is what you get, eventually, after the judge."
2. **Kaz vs. legal vocabulary.** Kaz hears "portability" and asks whether bondholders can keep their coupon when they switch carriers. Ines: "Close. It is the issuer who keeps the number and you who gets dropped."
3. **The double trigger.** "An IG change-of-control put is a smoke detector that only goes off if there is a fire *and* two separately licensed inspectors agree it is a fire within 60 days." (Then the derivation of $\pi_{t\mid d}$.)
4. **ROBO literalism.** Vague spec: "price the CoC put." ROBO prices a vanilla put on the bond at 101 with the target's pre-deal vol and returns a large number for the U.S. Steel 6.875% notes, which were going to trade above 101 under a stronger parent. Precise spec follows: payoff conditional on deal × trigger, discounted on the acquirer's curve.
5. **Mags's back-in-my-day.** "In 1988 we learned about event risk from RJR Nabisco and spent two years inventing the poison put. In 2026 a sponsor learned about the poison put and spent one afternoon inventing a Treasury deposit." Grudging respect follows for defeasance mechanics (Veronesi p.470 extraction: exercise need not be optimal, and sometimes the issuer finds a cheaper door).
6. **Ines's hand history.** The Second Request is a tell, but a cheap one: 2–3% of adjusted filings get one, and most of those still close. The real tell is the timing agreement that is not announced. Replay the markouts on a target bond around the Second Request date.
7. **The 13-week model returns** as a Kaplan–Meier curve of deal clocks: Theo renames the columns "weeks since signing" and discovers the model finally has a use for its "regulatory" row.
8. **Ticking fee.** "\$0.00277778 a day is what Paramount Skydance agreed to pay WBD shareholders for the privilege of being late. Annualized it is about 3.3%. Your survival model should be able to tell you whether that was generous." (Compute it.)
9. **"Open market purchase."** EA's tender for the legacy notes drew \$76.8mm of \$1.5bn. The remaining holders were then paid in Treasuries. The most expensive three words in finance have a cousin: "defease certain obligations."
10. **Desk Myth vs. Desk Reality.** *Myth:* the 101 put protects you in an LBO. *Reality:* it protects you if the bond trades below 101, the trigger fires, the covenant survives, and nobody defeases it; otherwise it protects the sponsor's lawyers' billing.

---

## 9. Resource-graph candidates

**Data & Code (VERIFIED-URL):** SEC EDGAR full-text search API root https://efts.sec.gov/LATEST/search-index and UI https://www.sec.gov/edgar/search/ ; FTC Premerger Notification Program https://www.ftc.gov/enforcement/premerger-notification-program ; FTC/DOJ HSR Annual Reports FY2023/FY2024/FY2025 (PDF URLs in §6.11); European Commission merger procedures https://competition-policy.ec.europa.eu/mergers/procedures_en ; CourtListener REST API https://www.courtlistener.com/help/api/ (dockets for FTC v. Kroger, FTC v. Tapestry, U.S. v. HPE in §6); UK CMA merger guidance page (§6.13). Crossref API https://api.crossref.org/ for DOI verification.

**Primary documents (VERIFIED-URL):** all EDGAR filings listed in §6.1–6.10.

**Academic Papers (VERIFIED DOI):** the list in §6.15.

**Practitioner Writing (TITLE-ONLY):** Matt Levine, *Money Stuff* (Bloomberg) columns on the Kroger SMR redemption, the EA take-private and the WBD bidding war (CHECK dates); Covenant Review / Xtract Research / 9fin reports on portability incidence and SMR terms (CHECK); Dechert's DAMITT (Dechert Antitrust Merger Investigation Timing Tracker) annual and quarterly reports on the duration of significant US and EU merger investigations (URL not reachable this session; TITLE-ONLY); Mayer Brown and Sidley client notes on special mandatory redemption drafting (TITLE-ONLY); Moody's Covenant Quality Indicator reports (TITLE-ONLY).

**Podcasts (TITLE-ONLY, CHECK episodes before linking):** *Bloomberg Odd Lots* episodes on merger arbitrage and the Khan-era FTC; *Capital Allocators* conversations with event-driven managers; *Flirting with Models* on event-driven and tail strategies; *Petition* (newsletter, restructuring) coverage of Spirit Airlines' Chapter 11.

---

## 10. Exploratory-space notes (future editions)

1. **Ch 15-B: Convertible "fundamental change" puts, make-wholes and the U.S. Steel cash-conversion template.** Converts' par put and the conversion-rate make-whole table on CoC; the 2025 U.S. Steel Share Exchange Event supplemental indenture as the worked example; interaction with Ch 23's vol surface.
2. **CDS succession events and orphaning in M&A** (ISDA 2014 Definitions successor rules; carve-outs and spin-offs such as WBD's Global Linear Networks and the Discovery Global term loans): a joint section with Ch 24.
3. **Defeasance and covenant strips as the sponsor's counter-option.** A dedicated section (or Ch 13 subsection) turning legal and covenant defeasance, consent solicitations and exit consents into document features and a game tree; EA 2026 and WBD June 2025 as cases.
4. **Non-HSR hazards as separate competing risks:** CFIUS and presidential action (U.S. Steel), the STB (UNP–NSC), state attorneys general (Kroger co-plaintiffs), FCC, and foreign regulators (China SAMR on Synopsys–Ansys); each gets its own cause-specific baseline hazard.
5. **Ticking fees, reverse termination fees and the price of time:** a mini-literature review (Officer 2003; Bates–Lemmon 2003) plus a 2023–26 sample of contractual per-diems, compared with survival-implied carry.
6. **The IG LBO-risk factor (2025–26):** screen IG issuers for take-private vulnerability (low-coupon legacy notes, cash-rich sponsors, no double-trigger ambiguity, weak defeasance protections) and test whether an "event-risk premium" exists in cross-sectional spreads, extending Crabbe (1991) and Billett–Jiang–Lie (2010) to the current wave; link to Ch 9's factor framework.
7. **Target-bond exchange offers as CoC alternatives** (Kroger's \$7.4bn exchange for Albertsons notes): mechanics, consent thresholds, and what happens to tendered-but-unsettled exchanges when the deal dies.
8. **Machine-learned deal-completion models applied to credit** (Halskov 2024; Dikova et al. 2010): purged, deal-grouped cross-validation per Ch 7, with the HSR Appendix A series as regime covariates.
9. **An "event momentum" study for Ch 10:** does the target-bond spread drift tighter through silent regulatory milestones (Giglio–Shue in credit), and does it reverse on Second Request announcements?
10. **Appendix C entries:** the HSR early-termination collapse and return; the HSR-form vacatur of 2026; SMR trigger counts by year from EDGAR.
