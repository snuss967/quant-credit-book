# Advisor Brief — Chapter 13: Codifying Liability Management Transactions (LMTs)

**Target file:** `book_src/13_ch13_codifying_lmt_game_theory.md` · **Target length:** 7,000–10,000 words · **Advisor:** Fable, Edition 1 · **Date:** 2026-10-17

Method note: web facts below come from primary-source fetches (Fifth Circuit opinion text, CourtListener dockets, SEC EDGAR, Federal Reserve FSR/FEDS pages, Harvard Law School Bankruptcy Roundtable posts, a Wachtell memo, 9fin; Wikipedia for background only) plus the shelf. Anything I could not open is marked **CHECK** and must not carry a number until verified.

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** An LMT re-allocates recovery among claims drafted to be equal, through the gap between what a credit agreement says and what its drafters assumed. Every species in the zoo is **the difference between two waterfalls** on the same $V$: the one the document promised and the one the amendment produced. That difference is a derivative on $V$ whose strike is set by document capacity and whose counterparty is chosen by a game. The chapter turns clauses into state variables, prices the difference of waterfalls, solves the coalition game, and attaches a hazard so the desk carries one number: the **Priming Risk Score** $\text{PRS}\in[0,1]$.

**The aha, in five beats.**
1. *You already know where the trapdoors are.* The new move is to treat the Restricted Payments builder, the unrestricted-sub basket, the §9.05(g) buyback exception and the sacred-rights list as **numbers and thresholds**: $C^{\text{unsub}}$ (dollars that can leave the collateral), $\theta$ (required-lender fraction), the scope of sacred rights, and a binary for whether the buyback exception says "open market purchase" (Serta) or merely "purchase" (Mitel). On the same day, Dec 31, 2024, the Fifth Circuit and New York's First Department decided that this one word is worth the entire priming loss.
2. *The sponsor is not a player; it is the house.* A non-pro-rata uptier is a procurement auction: the borrower buys a bare majority's consent and lets lender groups bid for the right to be inside. Your Rule 2019 instincts are inputs to a **minimal-winning-coalition** problem.
3. *A cooperation agreement is a cartel* that turns an $n$-player prisoner's dilemma into two-player bargaining. Once a blocking minority ($>1-\theta$) commits, the auction collapses and surplus is split by Nash bargaining with outside options; carve-out premiums are the steering committee's Shapley value. The 2025–26 antitrust challenges to co-ops (Optimum, Selecta) attack the commitment device itself.
4. *The court is a random variable with a forum feature.* Texas bankruptcy court (2023) blessed Serta's "open market purchase"; the Fifth Circuit (2024/25) reversed; the First Department (Mitel, 2024) upheld a near-identical deal under a "purchase" clause; Isgur's "domino theory" in Incora was reversed by District Judge Crane (2025) and is before the Fifth Circuit (No. 26-20018, docketed Jan 13, 2026); a New York court in STG Logistics (2025) collapsed a drop-down's steps anyway. PRS needs a `governing_law × forum` term.
5. *The LMT is not the terminal state.* Roe & Rotaru (2026; 89 coercive LMEs): only 22% avoid both re-default and bankruptcy within two years. The question is "what is the hazard of the *next* event and where do I sit after this one". Theo's 13-week model returns as the liquidity-runway covariate.

---

## 2. Section outline (7,000–10,000 words), anatomy map, Trend Watch boxes

**Cold open (≤400 words).** Friday 2:58 p.m., RFQ to sell \$15mm of a sponsor-owned B3 first-lien loan at 78. Ines: "Who at this table knows more than you?" Theo: "What does the credit agreement say about open market purchases?" Kaz: "Is a Serta blocker a mattress protector?" Mags: "It is now." The Ad Hoc Group, offstage, represented by counsel. Question: *how do you turn 300 pages and a rumor into a number you can quote against?*

- **13.1 The LMT Zoo, Seen From the Desk.** Taxonomy table (what moves, who loses, enabling clause, canonical case). *Desk framing; Moyer p.228, p.165.* Box: Desk Myth vs. Desk Reality ("LMEs avoid bankruptcy" vs. Roe–Rotaru's 22%).
- **13.2 Legal Prose to State Space.** Five clause families → features: pro rata and sacred rights; thresholds $\theta$; buyback exceptions (Dutch auction / "open market purchase" / "purchase"); investments, RP builder, unrestricted subs; lien and guarantor release. *Capacity arithmetic; Moyer p.168, p.173.* Kaz "blocker" gag.
- **13.3 The Uptier as a Recovery Transfer.** Difference-of-waterfalls on Serta's numbers; "the excluded lender is short a digital put on $V$". **Trend Watch #1:** blockers 40%→85% (Buccola–Nini); LME counts 38 (2024) → 24 (2025) → 25 in H1 2026.
- **13.4 Game Theory I: Threshold Games and the Sponsor's Auction.** $2\times2$ matrix, minimal winning coalition, Bertrand competition between groups, litigation as outside option, Buccola–Kahan's four levers. *Moyer p.85–87.* Box: Poker Table (Ines).
- **13.5 Game Theory II: Cooperation Agreements as Commitment Devices.** Blocking minority, Nash bargaining, carve-out premiums, open/closed/tiered co-ops, antitrust, deals-away with six-month par calls. **Trend Watch #2:** co-ops, deals away, equity handovers (9fin H1 2026), re-default hazard. Cooperation-agreement counter.
- **13.6 Drop-Downs: Collateral Leakage Arithmetic.** $C^{\text{unsub}}$, transfer $T$, structurally senior UnSub debt; J.Crew 72.04%; PetSmart 20% + 16.5%; Envision; Pluralsight (CHECK); STG Logistics. *Moyer p.244.* Box: Docket Diary (J.Crew, Feb 1 → July 13, 2017).
- **13.7 Double-Dips and Pari-Plus: A Waterfall Engine That Conserves Value.** Eisenberg–Noe clearing with priority classes; closed form $2V/(F_1+2F_2)$; Trinseo 2023 → 2026; Sabre 2023. *AI spec (engine).* Box: Ways This Blows Up (circular guarantees, deficiency claims, substantive consolidation; Moyer p.305, p.351).
- **13.8 The Priming Risk Score.** Hazard/logistic with Bayesian priors on ~100 events; PRS → expected priming loss → price; momentum and liquidity covariates. *`### Specification for AI Implementation` with full code; Bohn–Stein p.233, p.447; Schmid p.35; Bolder p.554; Dynkin p.139, p.605; Ben Dor p.112.* Box: Ways This Blows Up (separation with 89 events).
- **13.9 Autopsies.** Serta, Incora, Mitel, plus a 2026 coda (Lions Gate/Starz, Mar 17, 2026; ConvergeOne; Trinseo's double-dip in Chapter 11), each with how a systematic desk would have flagged and traded it. Three Docket Diaries.
- **13.10 Desk Debrief · The Spec You Hand the Robot · Exercises.**

Every section closes with `### Deep-Dive Resource Graph` (see §9).

---

## 3. Derivation skeletons

Expectations are under $\mathbb{P}$ unless stated. $V$ = distributable enterprise value at resolution, $F$ = face, $R$ = recovery (fraction of par). $\text{EV}$ is enterprise value only.

### 3.1 Uptier as a difference of waterfalls
One secured class, face $F$, pre-deal $R_0=\min(V,F)/F$. Uptier: new money $N$ (first-out), fraction $p$ of face exchanged at ratio $x$ into second-out, non-participants $(1-p)F$ left third-out. Serta (Fifth Circuit): $N=\$200$mm; \$1.2bn exchanged into ≈\$875mm, so $x\approx0.73$ *(blended across liens, approx.)*; participants held "a bare majority" of the 1L.
$$
R^{\text{FO}}=\frac{\min(V,N)}{N},\quad
R^{\text{SO}}=\frac{\min\!\big((V-N)^+,\,xpF\big)}{xpF},\quad
R^{\text{excl}}=\frac{\big(V-N-xpF\big)^+}{(1-p)F}.
$$
Priming loss $\Delta R^{\text{excl}}(V)=R_0-R^{\text{excl}}$: zero for $V\ge F+N$, equal to $R_0$ for $V\le N+xpF$, linear between. Conservation: payouts sum to $\min(V,\,N+xpF+(1-p)F)$; total face shrinks by $(1-x)pF$ (the advertised "deleveraging"). Participant gain per original dollar is $xR^{\text{SO}}-R_0$ plus new-money economics; for high $V$ they *lose* face. The excluded lender is **short a soft digital put struck near $N+xpF$**. Error-prone spots: blended 1L/2L ratios; accrued interest and make-wholes; ignoring the indemnity, which the Fifth Circuit held was itself unequal treatment under §1123(a)(4) and excised.

### 3.2 Game Theory I: threshold game and the sponsor's auction
Weights $w_i$, $\sum w_i=1$; amendment passes iff $\sum_{i\in S}w_i>\theta$ ($\tfrac12$ typical; $\tfrac23$ for many indenture lien releases; $1$ for sacred rights). Per-dollar payoffs $u^{\text{in}}>u^{0}>u^{\text{out}}$ for inside a winning coalition / status quo / primed. Against "the rest of the class" this is a prisoner's dilemma with an invitation list: *Join* weakly dominates whenever you expect to be invited (Moyer p.85 names the exchange-offer version exactly that). **Sponsor's problem:** $\min_S\sum_{i\in S}c_iw_i$ s.t. $\sum_{i\in S}w_i\ge\theta+\varepsilon$, a 0–1 knapsack; $c_i$ differs by lender type (CLOs cannot fund new money; hedge funds can), which predicts who is excluded. **Auction between groups:** coalitions $A,B$ bid packages; Bertrand logic pushes the winner's rents toward the loser's outside option, the expected value of litigation $\pi^{\text{lit}}=q\,\mathbb{E}[\text{damages}]-\text{cost}$, where $q$ depends on the clause and the forum (high after Serta; low under a Mitel-style "purchase" clause). Buccola & Kahan's (2025) levers map onto the matrix: *ranking* (moves $u^{\text{out}}$), *conditioning*, *exclusivity* (raises $u^{\text{in}}-u^0$), *vote manipulation* (shifts the effective $\theta$; Incora's add-on notes). Optional: a global-games refinement (noisy signals $s_i=V+\sigma\epsilon_i$) yields a unique threshold equilibrium, coalition iff $V<V^*$, which explains pre-announcement drift; cite Morris & Shin by title.

### 3.3 Game Theory II: cooperation agreements
A co-op is a set $C$ with $\sum_{i\in C}w_i>1-\theta$ plus a no-separate-deal covenant, transfer restrictions and a sunset. The sponsor's feasible set now requires $S\cap C\neq\emptyset$ and $C$ acts as one player, so the game is bilateral Nash bargaining: $\Pi_C=d_C+\tfrac12(\Pi-d_C-d_{\text{sp}})$, with $d_{\text{sp}}$ = deal-away or Chapter 11 and $d_C$ = bankruptcy recovery or litigation. Deals-away with **six-month par calls** (Wachtell, Feb 2026) are a cheap way to raise $d_{\text{sp}}$. Inside the co-op, **carve-out premiums** are the Shapley value of a weighted-majority game (pivotal members earn more). Error-prone spot: a *closed* co-op is a non-pro-rata uptier in waiting (Miller 2025: "inclusive, but unequal").

### 3.4 Drop-down arithmetic
$C^{\text{unsub}}=B^{\text{gen}}+B^{\text{builder}}+B^{\text{ratio}}\mathbf 1[\text{test}]+B^{\text{unsub}}$, with the builder accruing per Moyer p.173 (carve-out + 50% CNI + 100% equity proceeds − RPs − investments in unrestricted subs). Transfer $T\le C^{\text{unsub}}$; UnSub borrows $D_u$ against $T$ and returns $\phi D_u$:
$$
R^{\text{post}}=\frac{\min\!\big(V-T+\phi D_u+(T-D_u)^+,\;F\big)}{F}.
$$
The J.Crew trapdoor is $\phi\to$ small, $D_u\to T$: the IP leaves, is levered, and the proceeds fund a different class's exchange. Sanity: $T=0$ recovers $R^{\text{pre}}$; $\phi=1,D_u=T$ keeps dollars but degrades collateral quality (an LGD-variance effect).

### 3.5 Double-dip and pari-plus: the clearing vector
SPV issues $F_2$, lends proceeds to OpCo as an intercompany note pari with existing 1L $F_1$; OpCo also guarantees the SPV debt pari. Pro rata payout per dollar $\rho=\min(1,V/(F_1+2F_2))$; SPV lenders get $\min(F_2,2\rho F_2)$, so while $V<(F_1+2F_2)/2$:
$$
R^{\text{DD}}=\frac{2V}{F_1+2F_2},\qquad R^{\text{1L}}=\frac{V}{F_1+2F_2}.
$$
Above that the DD claim is full and the excess on the intercompany note is SPV equity flowing back to a parent that may itself sit in the collateral, so the solution is a **fixed point**: Eisenberg & Noe (2001) with priority classes, $p=\min(\bar p,\Pi^\top p+e)$ class by class, iterated to convergence. Conservation: external distributions $=\min(\text{total value},\text{total external claims})$; no claim above face. Pari-plus adds a structurally senior guarantee from a non-guarantor foreign sub ($V_f$): the new lender takes $\min(F_2,V_f)$ first, then dips twice for the deficiency. State the assumption that a creditor may assert full face against each obligor until paid in full; flag jurisdiction. Trinseo 2026 is the first full-cycle test (§6.2).

### 3.6 Priming Risk Score
Cox template (Bohn–Stein p.233): $\lambda^{\text{LMT}}_i(t)=\lambda_0(t)e^{\beta^\top x_i(t)}$, $\text{PRS}_i(t,h)=1-\exp(-\int_t^{t+h}\lambda_i)$. With ~100–150 observed LMTs (89 coercive in Roe–Rotaru) use a fixed-horizon logistic with **Gaussian priors on $\beta$** (MAP) and a **Beta prior on the base rate** (Bohn–Stein p.447's framing), shrink toward a published prior as Schmid p.35 shrinks matrices, $\hat\beta=\Lambda\beta^{\text{prior}}+(I-\Lambda)\hat\beta^{\text{MLE}}$, and bootstrap the errors (Bolder p.554). What the desk prices:
$$
\text{EPL}_i=\underbrace{\Pr(\text{LMT})}_{\text{PRS}}\cdot\Pr(\text{non-pro-rata}\mid\text{LMT})\cdot\Pr(\text{excluded}\mid\text{NPR})\cdot\mathbb{E}[\Delta R^{\text{excl}}],
$$
and $P\approx P_{\text{no-LMT}}-\text{EPL}-$ risk premium. **Measure:** PRS is a $\mathbb{P}$-forecast; the price impact is $\mathbb{Q}$-flavoured because the marginal holder is averse to exactly this jump; never calibrate PRS to prices. Features: `has_serta_blocker`, `buyback_exception`∈{dutch_only, open_market, purchase, none}, `sacred_rights_scope`∈{payments, +liens, +subordination}, `theta_required`, `unsub_capacity_pct_ev`, `rp_builder_pct_ev`, `jcrew/chewy/envision_blocker`, `non_pro_rata_extension_allowed`, `loan_px`, `months_to_maturity`, `runway_months` (Theo's model), `sponsor_repeat_lme`, `holder_hhi`, `coop_reported`, `equity_mom_3m` (Dynkin p.605), `lcs` (Ben Dor p.112), `forum_ny_vs_tx`. Expect near-separation on `loan_px<80 & runway<9`; the prior keeps the fit finite.

---

## 4. Code spec and built-in sanity checks

One file, `lmt_engine.py`, numpy/scipy only, `rng=np.random.default_rng(13)`, runs top to bottom.

**(a) `waterfall_clearing(entities, claims, V)`** — Eisenberg–Noe with priority classes. Inputs: entity table (`id`, `external_value`); claims table (`creditor`, `debtor_entity`, `face`, `priority_rank`, `kind`∈{debt, guarantee, intercompany}). Pay classes in order, pro rata within class, route intercompany receipts, iterate until $\|p^{k+1}-p^k\|_\infty<10^{-10}$ (cap 10,000). Checks: conservation to $10^{-8}$; no claim above face; reproduces $2V/(F_1+2F_2)$ and $V/(F_1+2F_2)$ in the uncapped regime; monotone in $V$; pari-plus with $V_f=0$ collapses to the double-dip.

**(b) `uptier_game(weights, costs, theta, V, N, x)`** — payoffs from §3.1, minimal-cost winning coalition (brute force $n\le12$, greedy beyond), co-op of share $s_C$. Checks: $s_C>1-\theta$ empties the feasible set (assert); payouts sum to $\min(V,\text{total face})$; $x=1,N=0,p=1$ gives zero transfer; Serta parameters ($N=200$, $F=2{,}400$, $1{,}200\to875$) give a priming loss of zero at $V\ge F+N$ and $R_0$ at $V\le N+875$.

**(c) `prs_model`** — synthetic 400 borrower-years, 60 events from a known $\beta^\star$, MAP logistic with $\mathcal N(\beta^{\text{prior}},\tau^2I)$ and Beta(2,38) base-rate prior, 200 bootstraps, then `expected_priming_loss()` composing (a) and (b). Checks: $\hat\beta$ inside the bootstrap 90% band; $\partial\text{PRS}/\partial\texttt{has\_serta\_blocker}<0$ and $\partial\text{PRS}/\partial\texttt{unsub\_capacity}>0$ at the mean; PRS at $\bar x$ within 1 pp of the base rate; $\tau\to\infty$ matches MLE, $\tau\to0$ returns the prior; Brier beats the base rate on a seeded holdout.

ROBO line: "flag every borrower that could be primed" flags the whole index (any agreement can be amended with 100% consent); the precise spec adds $\theta$, the buyback enum and a horizon.

---

## 5. Source map (shelf; quotations verbatim, ≤60 words)

| Citation | Why | Quote |
| :-- | :-- | :-- |
| Moyer p.85 | Holdout problem is the uptier's ancestor (§13.4) | "those not participating in the exchange may be better off than those that do, but if too many hold out, all will be worse off. This is the general game theory problem known as the 'prisoner's dilemma.'" |
| Moyer p.86 | Repeated game, poker, bluffing (Ines's box); covenant stripping | "as in poker, which is analogous because the 'multiple-hand' format of the game is similar to the series of transactions in the distressed marketplace, to be effective one must have a credible 'bluff.'" / "The most common coercive tactic is to 'strip' the covenant protections of nontendering bonds." |
| Moyer p.87 | Participation thresholds → $\theta$ and $\varepsilon$ | "the 'conscious' participation rate must make up for certain 'innocent' holdouts." |
| Moyer p.228 | Definition used verbatim in §13.1 | "Exchange offers are 'coercive' when they compel cooperation by exposing nonparticipants to the risk of being made worse off." |
| Moyer p.165 | Liens and guarantees as overrides of pro rata (double-dip setup) | "Grants of security interests can similarly be viewed as provisions to override the general rule that property in an estate is shared pro rata among creditors." |
| Moyer p.168 | The two priority covenants → drop-down features | "There are two basic priority-related covenants: restricted payment provisions and negative pledge clauses." |
| Moyer p.173 | Builder-basket formula → $B^{\text{builder}}$ | "50% of all net income earned 100% of proceeds from the sale of common or preferred stock ... Less: ... 100% of all amounts contributed or loaned to (or amounts guaranteed on behalf of) unrestricted subsidiaries" |
| Moyer p.244 | Why drop-downs manufacture unencumbered collateral | "if the existing bank debt has a lien on substantially all the assets, there may be little or nothing to offer." |
| Moyer p.351 | Challenge checklist → Ways This Blows Up | "Invalidity of guarantees · Substantive consolidation · Critical creditor/vendor status · Interpretation of contractual subordination language · Violations of covenants · Transfers that might be deemed fraudulent conveyances" |
| Houlihan_Lokey_Distressed_MA p.21 | In-court priming vs. out-of-court priming | "Priming Lien: The Company can threaten to raise new money senior to the Bank. Under Section 364(d)(1) of the Bankruptcy Code..." |
| Bohn_Stein p.233 | Cox template for PRS | "the impact ratio of the hazards over time is constant: hi(t)/hj(t) = exp(x′iβ)/exp(x′jβ)." |
| Bohn_Stein p.447 | Bayesian base rate with few events | "the Bayesian approach answers the question, 'Given that I know that I have already observed zero defaults, what is the highest probability of default that I could expect with 95 percent certainty?'" |
| Dynkin p.139 | Forced-seller price pressure → holder-type features, post-LMT drift | "downgraded bonds that were widely held by constrained insurance companies experienced significantly elevated selling pressures and larger price reversals." |
| Dynkin p.605 | Equity momentum as a lead indicator | "equity returns tend to predict subsequent returns of corporate bonds, especially in lower‐quality sectors." |
| Ben_Dor p.112 | LCS as the liquidity covariate | "a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction." |

Also usable: Schmid p.35 (prior-matrix shrinkage), Bolder p.554 (bootstrap), Moyer p.305 (structural-priority hedge: "buying the lower priced bond and shorting the higher priced debt"), Moyer p.336 (prepacks "less than 7% of cases" in 1998–2002).

---

## 6. RESEARCH DOSSIER

### 6.1 Court rulings

**Serta — *Excluded Lenders v. Serta Simmons Bedding*, 5th Cir. No. 23-20181 c/w 23-20363, 23-20450, 23-20451.** Filed Dec 31, 2024; revised Jan 21 and Feb 14, 2025; Haynes, Willett, Oldham, JJ.; opinion by Oldham. Full text read at https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf (rev. 2/14/2025); CourtListener id 10333637.
- Facts: 2016 Refinancing of "$1.95 billion in first-lien syndicated loans and $450 million in second-lien syndicated loans"; §2.18 pro rata; §9.02(b)(A) affected-lender unanimity to alter pro rata sharing; §9.05(g) exceptions: Dutch auctions "open to all Lenders" or "open market purchases" by an Affiliated Lender (including SSB). 2020 Uptier: "The Prevailing Lenders provided SSB with $200 million in new financing in exchange for $200 million in first-out, super-priority debt. The Prevailing Lenders also traded in $1.2 billion of their first-lien and second-lien loans for approximately $875 million in second-out, super-priority debt." They "held a bare majority of the outstanding first-lien debt"; the contract was titled the "Open Market Purchase and Cashless Exchange Agreement"; SSB indemnified them. Chapter 11 January 2023, S.D. Tex.; the bankruptcy court (2023 WL 3855820) held "open market purchase" "clear and unambiguous" and satisfied.
- Holding 1: "an open market purchase is a purchase of corporate debt that occurs on the secondary market for syndicated loans. Thus, the 2020 Uptier was not a permissible open market purchase." "Having chosen to privately engage individual lenders outside of this market, SSB lost the protection of § 9.05(g)." The expansive reading would render the Dutch-auction exception "surplusage."
- Holding 2: the plan indemnity violated §1123(a)(4): "the unequal treatment in this case implicates both opportunity and result"; "we choose to excise the offending indemnity in Section 8.5 of the Plan." Footnote: Prevailing Lenders "held at least 81% of SSB's first-lien, first out debt and at least 77% of the SSB's first-lien, second out debt" (June 2023), "with the remainder probably held by entities like Citadel that did not participate."
- Market dictum: "The 2020 Uptier was the first major uptier... today's decision suggests that such exceptions will often not justify an uptier."
- Parties: appellees Barings, Boston Management and Research, Credit Suisse Asset Management, Eaton Vance, Invesco; appellants Excluded Lenders, LCM Lenders, Citadel Equity Fund; an "Apollo Proceeding" is referenced (role CHECK).

**Mitel — *Ocean Trails CLO VII v. MLN TopCo Ltd.*, 2024 NY Slip Op 06660 (1st Dep't, Dec 31, 2024), Index No. 651327/23.** Listed at CourtListener id 10309794 (text blocked to my fetcher; nycourts.gov and Justia returned 403). Per Wachtell (Feb 3, 2026): the court "fully upheld an uptier transaction, holding that the transaction complied with the 'purchase' exception to the general requirement of ratable treatment in Mitel's credit agreement and that none of the alleged sacred-rights violations could survive a motion to dismiss." Deal amounts CHECK. Aftermath (Wikipedia citing Bloomberg and Mitel): Chapter 11 filed March 10, 2025; emerged June 20, 2025; ownership from Searchlight to lenders; debt cut ≈\$1.15bn.

**Incora / Wesco Aircraft.** Isgur's summary-judgment opinion sent to trial whether the 2022 deal was an "open market purchase" or a "redemption" and whether it was a "single, integrated transaction" needing a two-thirds pre-transaction vote (Ropes & Gray via HLS, May 21, 2024). His "domino theory": if a first step (an amendment "to issue additional debt to increase the holdings of a majority group to a two-thirds threshold necessary to strip liens") necessarily causes the last, the steps collapse; "the majority group did not have the requisite two-thirds majority at the time of the first amendment" (Wachtell). District Judge Crane (S.D. Tex., 2025, date CHECK) reversed, looking "no further than the language of the agreements, the sophistication of the parties, and the 'direct effect' of a specific amendment." Fifth Circuit appeal *Wesco v. 2026 Noteholders*, No. 26-20018, docketed Jan 13, 2026; parties include the 2026 Noteholders, First Lien Noteholder Group, Citadel Equity Fund, WSFS (CourtListener docket 74956914). Deal specifics (\$250mm add-on 2024 notes; PIMCO/Silver Point/Platinum) CHECK.

**STG Logistics (N.Y. Sup. Ct., 2025; date/justice CHECK).** Per Wachtell, the court "did view a series of separate but related steps in a transaction – amendments permitting a covenant strip, a drop-down exchange, and an intercompany loan – as a single integrated plan for purposes of analyzing 'sacred rights' (i.e., unanimous lender vote) claims"; motion to dismiss denied; "Shortly following the decision, the company filed for bankruptcy."

**ConvergeOne (S.D. Tex. district court, 2025; date CHECK).** Reversed confirmation: backstop fees on a \$245mm exit rights offering were "a form of recovery on participating creditors' pre-bankruptcy debt claims, and therefore had to be open to all creditors in the applicable class, absent robust market testing" (Wachtell); RSA with ≈81% of 1L/2L; ≈11% of 1L excluded; appealed to the Fifth Circuit (Goodwin via HLS, Nov 25, 2025).

**Robertshaw.** *Invesco v. Robertshaw*, 5th Cir. No. 26-20422, docketed Aug 3, 2026 (CourtListener docket 74695342). Underlying facts CHECK.

**Lions Gate / Starz — *CPPIB Credit Investments II Inc. v. Deutsche Bank Trust Co. Americas*, 2026 NY Slip Op 50460(U) (Sup. Ct. N.Y. Cnty., Cohen, J., Mar 17, 2026), Index No. 654398/2024.** CourtListener digest heading: "Performance of Contract—Uptiering Transaction—Sacred Rights Provision"; caption includes Starz Entertainment Corp. (f/k/a Lions Gate Entertainment Corp.), plaintiffs CPPIB Credit Investments II and III and Thebes Offshore Master Fund, and ~200 fund parties. Underlying transaction (Lions Gate 8-K, May 8, 2024, acc. 0001193125-24-134381): private exchange of "$389,861,000 aggregate principal amount of 5.500% senior notes due 2029" for new notes of Lions Gate Capital Holdings 1, Inc.; majority consent "amended the terms thereof to remove certain restrictive covenants and events of default"; new notes "guaranteed exclusively by entities which are part of the Studio Business" after separation, coupon to 6.000%, maturity to April 15, 2030. **Holding CHECK** (text not opened). The chapter's bond-side exit-consent case for 2026.

**Trinseo (Bankr. S.D. Tex., lead case 26-90545, Judge Christopher Lopez, filed May 26, 2026)** and adversary *CastleKnight Master Fund LP, Elevation CLO 2013-1 v. Trinseo Holding S.à r.l.*, No. 26-03208 (declaratory judgment; lien validity/priority; subordination); plaintiffs opposed judgment-on-the-pleadings motions by the debtors and "Super HoldCo Lender Defendants" (June 23, 2026) (CourtListener dockets 73388469, 73394456). Also verified for Ch 14: *First Brands Group*, No. 25-90399 (Sept 28, 2025); *Wolfspeed*, No. 25-90163 (June 30, 2025).

### 6.2 Deal facts from EDGAR

- **J.Crew.** Dec 5, 2016: "invest[ed] certain intellectual property in the Company's wholly owned unrestricted subsidiary, J.Crew Domestic Brand, LLC," asserting it "fully complied with the Company's Term Loan Agreement"; Feb 1, 2017 suit against Wilmington Savings Fund Society as successor agent in N.Y. Commercial Division (8-K Ex. 99.1, acc. 0001564590-17-000864). July 13, 2017 closing (8-K, acc. 0001564590-17-013589): \$565.7mm of 7.75%/8.50% PIK toggle notes due 2019 exchanged for \$249.596mm 13% Senior Secured Notes due 2021 issued by J.Crew Brand, LLC / J.Crew Brand Corp. "secured on a first priority lien basis by a 72.04% interest in the Licensed Marks," plus \$189.688mm 7% preferred and ≈15% of parent equity; \$150mm of term loans repurchased; \$97mm new-money notes at a 3% discount; sponsors added \$30mm; licence fees \$42.5mm + \$16.5mm per year; agent directed "to dismiss, with prejudice, certain litigation." Chapter 11 May 4, 2020, E.D. Va. (Chinos Holdings, No. 20-32181); emerged Sept 2020. IP valuation ≈\$250mm CHECK (press).
- **PetSmart / Chewy.** LBO \$8.7bn (BC Partners, March 2015); Chewy acquired May 2017 for \$3.35bn; June 2018: 20% of Chewy to parent (Argos Holdings), 16.5% to a wholly owned unrestricted subsidiary; PetSmart sued Citibank (agent) June 2018; debt ≈\$8.0–8.6bn (Wikipedia citing Reuters June 6, 2018; FT Alphaville June 5, 2018; WSJ June 28, 2018; Bloomberg May 1, 2019). Chewy S-1 (Apr 29, 2019, acc. 0001193125-19-124430): "PetSmart settled existing litigation with the agent for its term loan lenders regarding these transfers in April 2019"; "there can be no assurance that other PetSmart creditors may not seek to challenge these transfers." IPO June 2019 at \$22.
- **Sabre (pari-plus), May 25, 2023 (8-K Ex. 99.1, acc. 0001193125-23-153616):** "$665 million new senior secured credit facility" from "lenders led by affiliates of Centerbridge Partners, L.P." to Sabre Financial Borrower, LLC, "a newly created wholly-owned subsidiary of Sabre GLBL"; "secured by an intercompany loan by the Borrower to Sabre GLBL" plus "direct guarantees from, and security interest in assets of, certain foreign subsidiaries of Sabre"; proceeds fund tenders capped at \$615mm for the 9.250% 2025s (\$970), 7.375% 2025s (\$920), 11.250% 2027s (\$840).
- **Trinseo (double-dip), Sept 8, 2023 (8-K acc. 0001104659-23-099167):** "a senior secured term loan facility of $1,077 million" to Trinseo Luxco Finance SPV S.à r.l. and Trinseo NA Finance SPV LLC; \$948mm on-lent as "2023 Term Loans" under the 2017 OpCo agreement; Term SOFR+8.50% (SPV, May 3, 2028) and Adjusted Term SOFR+9.66% (intercompany, May 3, 2030); repaid the 2018 term loans and redeemed \$385mm of 5.375% 2025 notes. **May 25, 2026 disclosure statement (8-K Ex. 99.2, acc. 0001104659-26-066376):** funded debt ≈\$2.9bn; RCF \$348mm (est. recovery 99–100%); Super HoldCo 1L term loans \$1,266mm incl. \$115mm Tranche C (Jan 2025) (est. **60–78%**); OpCo 2028 term loans \$716mm (est. **2–9%**); OpCo intercompany term loans \$1,508mm pledged to Super HoldCo; 7.625% 2029 notes \$390mm (0%); RSA May 13, 2026 with 100% of RCF, ≈99.9% of Super HoldCo 1L, ≈86% of OpCo term loans; DIPs \$157.5mm + \$270mm; exit term loan \$850mm; 2025 adjusted EBITDA \$162.5mm; intercompany make-wholes flagged by the "OpCo Investigation" and settled via "a gift through a carve-out of the Collateral securing the Allowed OpCo Intercompany Term Loan Claims." CastleKnight (OpCo 2028 loans, 2029 notes) objects.
- **Lumen, Mar 22, 2024 (8-K acc. 0001193125-24-080820):** "SUPERPRIORITY REVOLVING/TERM A CREDIT AGREEMENT dated as of March 22, 2024," BofA agent; Wachtell lists Lumen among LME "success stories." Aggregate size CHECK.
- **Atos (Wikipedia, background):** debt "almost €5 billion" (Apr 2024); July 4, 2024 plan: ≈€2.8bn debt-to-equity, €233mm new creditor equity; Bull sale to the French state completed Mar 31, 2026. **Not a drop-down**; keep as the European *sauvegarde accélérée* contrast and use Pluralsight (2024, private credit, CHECK), Del Monte (2024 → Ch 11 D.N.J. 2025, CHECK) and STG Logistics as modern drop-downs.
- **Envision (Wikipedia, background):** KKR \$9.9bn (June 2018); Moody's warning Sept 22, 2022; Chapter 11 May 15, 2023; Oct 2023 plan splitting Envision Physician Services and AMSURG. 2022 AmSurg drop-down/uptier amounts CHECK.

### 6.3 Trend data

- **Counts.** 38 LMEs in 2024 (high-water mark), 24 in 2025 (Wachtell, *Liability Management 2026: For Better or Worse*, Feb 3, 2026, https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf). 25 completed in H1 2026 vs 24 in H1 2025; "the coercive uptier structures that defined 2025 have all but vanished"; equity handovers and consensual amend-and-extends dominate (9fin, Aug 28, 2026, https://9fin.com/insights/h1-2026-lme-update).
- **Share of defaults.** "LMEs still accounted for two-thirds of default activity by issuer count in 2025 and exceeded both payment defaults and bankruptcies on a rolling 12-month basis for each month of 2025" (Wachtell). Fed FSR Nov 7, 2025: the volume-weighted leveraged-loan default rate "stayed well below its historical median" while "defaults including distressed exchanges... continued to be elevated relative to history (figure 2.9)"; FSR May 8, 2026 repeats this and notes in private credit "the elevated usage of payment-in-kind (PIK) provisions indicates some borrowers may face repayment difficulties" (https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf and ...-20260508.pdf; the distressed-exchange series begins Dec 2016).
- **Re-default.** Roe & Rotaru (HLS, Feb 24, 2026; SSRN 6103369): 89 hand-collected coercive non-pro-rata LMEs; within one year fewer than half avoided both bankruptcy and re-default; "Within two years, only 22% avoided both"; 56% of firms with ≥2 years of history had filed; ratings flat; leverage did not fall; LME debtors spent 2–3× longer in bankruptcy than non-LME prepacks. Wachtell quotes the FT: "around 80% of companies default on their restructured debt within three years of an LME" (CHECK the FT piece). Antill–Jiang–Wang quote S&P: 63% of LME users avoid Chapter 11 (CHECK).
- **Documents.** Buccola & Nini (53 J. Legal Stud. 489 (2024); HLS Apr 8, 2025): 600+ agreements, 2016–2022; "Prior to 2020, only 40% of loans restricted uptiers, often inadvertently"; "By mid-2022, 85% of new loans explicitly blocked uptiers, with 70% requiring unanimous lender consent for subordination"; outright unrestricted-sub bans rare; IP blockers rising. 2024–26 blocker adoption CHECK.
- **Structures after Serta.** Within a month: "amend-extend-and-exchange" (majority extends into a separate class → amends away covenants/liens → that class is refinanced with super-senior or drop-down money), "deployed throughout 2025" (Wachtell). **Deals away** returned (Optimum/Altice USA, Altice International, Liberty Puerto Rico, KIK), often with six-month par calls, "no more than a detour in a continuing negotiation."
- **Co-ops.** Three flavours (open / closed / carve-out-premium or tiered); "Antitrust challenges in connection with cooperation agreements (Optimum and Selecta) are in their early days" (Wachtell). Seaton (SSRN 5247506): defensive co-ops trace to SpectraSite; WBD's 2025 bonds pioneered an "anti-cartel" provision; equity falls on co-op news, firm value modestly up. Miller (SSRN 5549919): "By operating collectively, incumbent lenders outbid third-party financing offers." Parikh (SSRN 4410235): "Utilization of coercive exchanges began in earnest around 2015."
- **Maturity wall.** "$580 billion of loans and $625 billion of high-yield bonds mature between 2027 and 2029" (Wachtell).
- **Theory.** Antill, Jiang & Wang (SSRN 4821620; HLS June 30, 2026): three-period model in which permitting LMEs cures a "renegotiation debt overhang" and non-pro-rata uptiers are the structures most likely to be banned ex ante. Buccola & Kahan (SSRN 5014946): four coercion sources, three dominant practices. Huang, Lewellen & Wang (SSRN 4854111): Rule 2019 data; coalition announcements lift bond prices across classes.
- **Private-credit adjacency.** FEDS Notes on private credit (Feb 23, 2024; May 23, 2025; Aug 11, 2026); 9fin BDC Watchlist Q2 2026 (Sept 30, 2026): 118 credits, \$4.19bn, falling valuations; Petition, Oct 4, 2026: Leslie's Chapter 11 hands keys to term lenders.

---

## 7. Case studies

**A. Serta Simmons (2016 → 2020 → 2023 → 2024/25).** Use the Fifth Circuit's numbers and sentences (§6.1). Tranches: 2016 First Lien Term Loan (\$1.95bn), 2016 Second Lien Term Loan (\$450mm), 2020 First-Out (\$200mm) and Second-Out (≈\$875mm from \$1.2bn) Super-Priority. Loans were "trading far below par" pre-deal (prices CHECK/illustrative). Desk flags: `buyback_exception=open_market`; sacred rights covering pro rata *payments* only; sponsor-owned with a COVID liquidity shock; price <80; a live SDNY docket from 2021. The excluded dollar is the short digital put of §3.1; the indemnity was the participants' tail hedge, and the court cancelled it.

**B. Incora / Wesco (2022 → 2024 → 2025 → 2026).** The "ballot stuffing" archetype: issue add-on notes to reach two-thirds, then strip liens. Teach **domino theory vs. step-by-step** as a binary forum feature with a live appeal (No. 26-20018). Docket Diary: Isgur SJ (early 2024), trial ruling (2024, CHECK), Crane reversal (2025, CHECK), appeal docketed Jan 13, 2026. Amounts CHECK.

**C. Trinseo (2023 → 2026): the double-dip survives contact with Chapter 11.** The §3.5 engine should reproduce the ordering Super HoldCo 1L 60–78% ≫ OpCo 2028 TL 2–9% from the claim stack; the "OpCo Investigation" settlement of intercompany make-wholes is the Ways-This-Blows-Up for anyone modelling the second dip at face plus premium. Sidebars: Mitel (same-day contrast; 2025 Chapter 11, \$1.15bn cut), Lions Gate/Starz (bond-side sacred rights, 2026), ConvergeOne (equal treatment inside Chapter 11).

---

## 8. Humor beats (each rides on a correct idea)

1. **Kaz vs. vocabulary:** "I assumed a Serta blocker was a mattress protector." Mags: "It is. It protects the mattress company's lenders from the mattress company." (A Serta blocker makes priority a sacred right.)
2. **"Open market purchase," the most expensive three words in finance:** 54 pages, three dictionaries and the Fed's open-market operations to conclude an open market is "a designated market, not merely the background concept of free competition." Use the court's opener: "Given the complexities, we will not even try to summarize our various holdings here. So read on."
3. **Ines's Poker Table:** "The sponsor isn't a player. The sponsor is the dealer, and the dealer chooses who sees the flop. A co-op is the players agreeing not to play heads-up against the house." Epigraph: Moyer p.86 on bluffing.
4. **Mags's back-in-my-day:** "We did this in 1991 with exit consents and called it an exchange offer. The innovation was doing it to the *bank group*, which used to be the one holding the knife."
5. **Cooperation-agreement counter:** increment per flavour (open, closed, carve-out), once for Trinseo's three ad hoc groups, once for WBD's anti-cartel clause: "(Cooperation agreements signed in this book so far: 5. Antitrust complaints about them: 2, and counting.)" Coordinate the start count with Chapters 3 and 14.
6. **ROBO literalism:** "Flag every borrower that could be primed" returns the whole index; with $\theta$, the buyback enum and a horizon it returns 11 names, one of which is the desk's own warehouse line.
7. **The Louisiana note:** the Fifth Circuit's parody of "equal opportunity," a plan note paying "$5 million in one year if the member is headquartered in Louisiana." (§1123(a)(4) means opportunity *and* result.)
8. **Double-dip definition:** "A guarantee and an intercompany loan walk into the same collateral pool and order twice. Pari-plus is the same two, plus a foreign subsidiary that buys the first round." Sourced punchline: in Trinseo the dip that double-dipped is slated for 60–78 cents; the loans it was 'pari' with, 2–9.
9. **Theo's 13-week model** returns as `runway_months`, the covariate that makes the logistic separate; the only thing keeping $\hat\beta$ finite is a prior, and the prior is Theo's spreadsheet.
10. **"IDO or it didn't happen":** an LMT P&L is the one place where "idiosyncratic" has been defined by three courts, in two states, on the same day.

---

## 9. Resource-graph candidates

**VERIFIED-URL (opened this session):** Fifth Circuit Serta PDF (above); CourtListener opinion pages for Serta (id 10333637), Mitel (10309794), CPPIB/Starz (11001279) at `https://www.courtlistener.com/opinion/<id>/`; CourtListener dockets 74956914 (Wesco v. 2026 Noteholders), 74695342 (Invesco v. Robertshaw), 73388469 and 73394456 (Trinseo), 71483359 (First Brands) at `https://www.courtlistener.com/docket/<id>/`; EDGAR documents by accession number in §6.2 (root `https://www.sec.gov/Archives/edgar/data/`; full-text search `https://efts.sec.gov/LATEST/search-index?q=`); Wachtell memo PDF; 9fin H1 2026 LME update; Fed FSR PDFs (Nov 7, 2025; May 8, 2026); FEDS Notes index `https://www.federalreserve.gov/econres/notes/feds-notes/`; the HLS Bankruptcy Roundtable posts cited in §6 (indexed at `https://bankruptcyroundtable.law.harvard.edu/category/liability-management/`); `https://www.petition11.com/archive`.

**VERIFIED-VIA-HLS (SSRN ids printed on HLS pages; SSRN returned 403 directly):** 4143928 Buccola–Nini; 4821620 Antill–Jiang–Wang; 6103369 Roe–Rotaru; 5247506 Seaton; 5549919, 6204978, 5041522 Miller; 5014946 Buccola–Kahan; 4854111 Huang–Lewellen–Wang; 4410235 Parikh. Present as "SSRN abstract id" with the HLS post as pointer, or title-only.

**CITATION-VERIFIED-IN-OPINION (journal cites copied from the Fifth Circuit text; no link):** Buccola, *Efficacious Answers to the Non-Pro Rata Workout*, 171 U. Pa. L. Rev. 1859 (2023); Buccola, *Sponsor Control*, 90 U. Chi. L. Rev. 1 (2023); Dick, *Hostile Restructurings*, 96 Wash. L. Rev. 1333 (2021); Skeen, *Uptier Exchange Transactions: Lawful Innovation or Lender-on-Lender Violence?*, 40 Yale J. Reg. 408 (2023); Lubben, *Holdout Panic*, 96 Am. Bankr. L.J. 1 (2022); Parikh, 73 Duke L.J. Online 1 (2023); Buccola & Nini, 53 J. Legal Stud. 489 (2024); Sunuu, S&P Global Ratings (June 15, 2021); *LCM XXII v. Serta*, 2022 WL 953109 (S.D.N.Y. Mar. 29, 2022); LSTA *Complete Credit Agreement Guide* (2017).

**TITLE-ONLY:** Coffee & Klein, *Bondholder Coercion* (1991); Gertner & Scharfstein, *A Theory of Workouts* (1991); Roe, *The Voting Prohibition in Bond Workouts* (1987); Eisenberg & Noe, *Systemic Risk in Financial Systems* (2001); Morris & Shin on global games; Ayotte & Ellias, *Bankruptcy Process for Sale* (2022); Mengden, *The Development of Collateral Stripping by Distressed Borrowers* (2021); *Marblegate* (2d Cir. 2017); *Katz v. Oak Industries* (Del. Ch. 1986). Podcasts (titles CHECK): *Odd Lots* on creditor-on-creditor violence, *Cloud 9fin*, Octus. Data (2024–26 numbers CHECK): Covenant Review, Xtract, LevFin Insights, Moody's/S&P/Fitch default studies.

---

## 10. Exploratory-space notes (future sections and chapters)

1. **Ch 13-B: The LMT Litigation Map as a Markov Model.** States {announced, challenged by forum, MTD denied, trial, reversed, settled, Ch 11}; transitions from Serta, TriMark (CHECK), Boardriders (CHECK), Mitel, Incora, Robertshaw, Del Monte (CHECK), STG, Lions Gate/Starz, ConvergeOne; output a forum-conditional $q$ for §3.2.
2. **Cooperation Agreements as Cartels:** Shapley/Nash formalism; the Optimum and Selecta antitrust suits (dockets CHECK); WBD's anti-cartel covenant; a co-op-detection feature from Rule 2019 filings and press.
3. **Deals Away and the Six-Month Par Call:** price the sponsor's unwind option; when a deal-away is a threat point rather than a financing.
4. **Private-Credit LMEs, PIK and BDC Marks** (bridge to Ch 17): Pluralsight (CHECK), 9fin BDC non-accruals, FEDS Aug 2026 note.
5. **European LMEs:** UK Part 26A (Fossil Group, HLS Mar 31, 2026), French *sauvegarde accélérée* (Atos), Dutch WHOA, Altice France (CHECK); why drop-downs are rarer where maintenance covenants persist.
6. **Bond-Side Uptiers and Exit Consents after Marblegate:** Lions Gate/Starz 2024 → 2026 as template; TIA §316(b) boundaries.
7. **The Double-Dip in Chapter 11:** Trinseo 2026 as the first full-cycle test; deficiency-claim treatment; substantive consolidation; the intercompany make-whole challenge.
8. **Equity Handovers as the Modal 2026 LME** (bridge to Ch 16): pricing the lender-owned company; CLO equity-holding constraints.
9. **LMTs and CDS** (bridge to Ch 24): succession events, orphaned CDS, deliverables after drop-downs.
10. **Text-to-Feature at Scale** (bridge to Ch 25): extract the §13.2 feature table from EDGAR credit agreements and measure blocker adoption by vintage past Buccola–Nini's 2022 cut-off.
11. **Re-Default Hazard as a Regime Variable** (bridge to Ch 14): Roe–Rotaru's 22% two-year survival as a second-stage hazard; prepack vs. LME with Moyer p.336's <7% prepack base rate as the historical anchor.
12. **TREND/MOMENTUM: Pre-Announcement Drift and Post-LME Momentum in Loan Prices** (bridge to Ch 10): event study of loan marks around co-op announcements and LME closings, participating vs. excluded tranches, and whether time-series momentum signals degrade across LME jumps.
