# Shelf digest: foundations_shelf_pages (primer source pages for Ch 4-B, 6-B, 7-B, 12-B, App E)

Researcher run date: 2026-10-18. Queue slug: `foundations_shelf_pages`. Feeds: `04_ch04b_bond_math_for_the_desk`, `06_ch06b_options_and_measures_for_credit`, `07_ch07b_statistics_for_credit_panels`, `12_ch12b_the_restructuring_process_as_a_state_machine`, `94_appE_laws_of_the_desk`.

Citation convention: `book_id p.N` where N is the PDF page index used by `tools/pdf_search.py` (1-based), as the [SOURCE EXTRACTION] boxes require.

## 0. Method and shelf inventory

Walked with `pdf_search.py` (`--toc`, `--page`, term search) and `pdftotext -layout` for equations; every quotation in section 10 was machine-checked against `state/pdf_pages/` (ligatures, hyphenation and whitespace normalised). Web used only for the Brownian-bridge citation and for dated/superseded checks (section 9).

| Requested | On the shelf? | Used |
|---|---|---|
| Moyer (classes, voting, cramdown, plan process) | Yes, 453 p. | s.1 |
| Bohn-Stein / Schmid (lien subordination, hazard-rate change of measure) | Yes | s.2 |
| Tuckman-style price-yield, duration, convexity, OAS | **Veronesi only** (no Tuckman) | s.3 |
| Natenberg / Hull Greeks | **No**; Veronesi Ch 16, Bohn-Stein BSM, Dynkin p.87 partial | s.4 |
| Grinold-Kahn fundamental law | **No**; Paleologo p.149, Ben Dor p.239 partial | s.5 |
| Beaglehole-Dybvig-Zhou | **No**; web-verified citation | s.6 |
| Bolder (threshold, tail dependence) | Yes | s.7 |
| Dynkin empirical duration | Yes (Ben Dor Ch 7; Dynkin Ch 10) | s.8 |

## 1. Moyer: classes, voting, cramdown, plan process (Ch 12-B)

Source: `Moyer_Distressed_Debt_Analysis` (S. Moyer, *Distressed Debt Analysis*, J. Ross, 2005; 453 PDF p., no TOC; PDF page = printed + 17). Running example "Boxco": operating company with secured bank claim A and trade claim B under a holdco with unguaranteed senior notes C, plus equity (Figures 3-6, 12-1 to 12-3).

**Process and timing.** Four objectives: stabilise, plan the business, fix liabilities and priority, "create and allocate a new capital structure" (p.97). Filing ladder: free-fall (1-3 years, a warning sign, p.94), prenegotiated, prepackaged (solicitation under section 1126(b); under 45 days, p.94, p.335-336); "Full prepacks are not common", under 7% of cases in 1998-2002 (p.336). Stay freezes creditors (p.97). DIP lenders get super-priority "priming"; prepetition lenders become DIP lenders for a roll-up (p.98); worked priming test: lender owed $65 with $150 of receivables, $75 DIP primes $75 of collateral and the lender stays adequately protected (p.98). Exclusivity 120 days plus 60 to solicit, extended "virtually indefinitely" (p.94, p.346; dated, section 9). Preferences 90 days, insiders one year (p.101, p.304). Substantive consolidation removes structural priority and can make B and C pari passu (p.304-305; Figure 12-3, p.360).

**Classes, impairment, voting (p.106-107, p.334, p.356-358, p.361).** Unimpaired means paid in full or reinstated on identical terms, "even improvements" impair (p.356-357); unimpaired classes are deemed to accept, zero-recovery classes to reject, so only impaired classes with some recovery vote (p.106). A class accepts with more than 50% in number and at least 66 2/3% in amount of those voting (p.107, p.357); acceptance binds dissenters and non-voters (p.334). 33.4% of a class blocks; the proponent's counter is to merge classes (Block Partners holds 45% of C, bonds merged with trade claims) but secured claims cannot be merged across collateral (p.358). Tipping: warrants struck at a value of 60 given to out-of-the-money equity (p.357); a 2-point give-up by a $250 senior class is a 10-point gain for a $50 preferred class (p.361); count votes exactly because tipped plans need every impaired class.

**Confirmation and cramdown (p.107-108, p.359-362).** Section 1129 is "limited democracy" (p.359): procedural items plus best-interests (chapter 7 comparison, weak for unsecured, p.107-108), good faith, feasibility ("most contentious", p.108) and consent or cramdown. Cramdown gate: one impaired accepting non-insider class, no unfair discrimination (between same-priority classes, p.360: trade claims offered 70% but demanding 75%), fair and equitable (strict absolute priority for unsecured, p.360). Secured cramdown (p.362): lien on sale proceeds, or retained lien with deferred payments of present value equal to the lesser of collateral and claim; the 1111(b) election swaps the deficiency claim for a lien and payments of face amount; administrative claims must be paid in cash at confirmation, hence rights offerings (p.362). Valuation fights go to court as expert testimony and usually settle (p.356).

**Priority and the waterfall (p.68, p.158-161).** Four priority techniques: collateral, maturity, contract, corporate structure (p.158-159). Subordination exists only by express clause and only to the debt defined as "Senior Debt" (p.159-160). Dead Co. (Figure 7-2, Table 7-1, p.160-161): assets 75; bank 50, trade 50, sub 100; pro rata 37.5% each; sub subordinated to bank only, so the sub's 31.25 is turned over: bank 50.00 (100%), trade 18.75 (37.5%), sub 6.25 (6.3%); subordinated to both, bank and trade recover 75%. This is subordination as a transfer, not a rank, and the regression test for any waterfall engine. Pricing paradox: senior at 50, sub at 20, equity positive, implied asset value 290 (p.68).

**Out-of-court holdouts (p.85-87).** Boxco's $700 of bonds exchanges into new debt and stock worth 41 (287/700); participants hold 36.5 while a holdout keeps 100; if too many hold out, chapter 11 costs cut value 287 to 215 and recovery 41.0% to 30.4% (p.85). Remedies: repeated-game reputation (p.86) and covenant stripping plus a prepack threat (p.86). Unanimity friction versus bankruptcy cramdown (p.334) is the economic root of the LMT era (Ch 13).

**Claims (p.310-312).** Trade claims rank with general unsecured claims and trade at a discount; purchase risks are disallowance and invalid transfer (Rule 3001(e)). No 503(b)(9) in the book (section 9).

## 2. Bohn-Stein and Schmid: seniority/lien subordination and the P-to-Q change of measure (Ch 6-B, 12-B)

Sources: `Bohn_Stein_Active_Credit_Portfolio_Management` (Bohn and Stein, Wiley 2009; printed = PDF - 32) and `Schmid_Credit_Risk_Pricing_Models` (Schmid, Springer 2004; printed about PDF - 6 to - 8). The text layer drops Greek letters; use `pdftotext -f N -l N -layout` for equations (the h^Q multiplier is psi, the market price of risk lambda).

**Structural P to Q (Bohn-Stein p.131, p.66, p.209-211).** Physical PD is a transformation of DD for risk and portfolio use; PD^Q is used only for valuation, so cash flows can be discounted at the risk-free rate (p.131). Under BSM pd = N(-DD). With CAPM, mu_A - r = beta (mu_M - r), R the correlation of assets with the market and lambda = (mu_M - r)/sigma_M, one gets r = mu_A - sigma_A R lambda, DD^Q = DD - R lambda sqrt(T) and

pd^Q = Phi(Phi^-1(pd) + R lambda sqrt(T)) (p.210-211).

A four-line corollary of Merton and the Wang-transform form. The page prints "R^2" in the definition although R is a correlation; do not copy. Related: Black-Cox p.150-156, empirical DD-to-PD p.161-177.

**Reduced-form P to Q (p.342-344).** D(T) = E^Q[exp(-integral (r + h^Q L) dt)], spread s = h^Q L (p.342-343). No CAPM link exists, so two ad hoc maps: h^Q = psi h with psi >= 1, or h^Q = psi_0 h + psi_1 X_c with a common state variable (p.343-344). Estimate by triangulating: CDS gives risk-neutral intensity, equity gives physical, and the functional form backs out the premium parameters (p.344). Valuation alone needs no transformation (p.342).

**Schmid (p.71, p.129, p.189-195, p.263).** Cox construction: T^d = inf{t: integral lambda_s ds = E}, E ~ Exp(1); constant intensity gives survival e^{-lambda(T-t)} and mean time 1/lambda (p.71). Zero-recovery defaultable zero = E^Q[exp(-integral (r + lambda~) dl)] (Lando 1998), default is also Cox under Q (p.129). The three-factor model starts in the real world and uses Girsanov; under Q only the mean-reversion constants change (p.189, p.195). Real-world transition data identify only the P-parameter, so the Q-parameter is fitted from observed spreads (p.263). Recovery conventions (par, market value, equivalent default-free bond) are interchangeable numeraires; "recovery rates are as important as the probabilities of default" in loss, and bankruptcy lasts about two years (p.95-96).

**Seniority and recovery as data.** Bohn-Stein p.289: LGD mostly 30-70% while PDs span 1-3,500 bp; senior subordinated bonds in 2000 had median recovery 32% and typical error about 70% of that. p.298-299: recovery is U-shaped (masses at 0 and 100%); use the 30-day post-default price for liquid books and ultimate recovery for hold-through books; Varma-Cantor single-B spread equates post-default price and emergence value. p.305: seniority/collateral look-up tables carry about 40% of LossCalc's power. p.309: the better regressor is the **relative debt cushion** below the instrument; APR footnote defines it as satisfaction "in accordance with the seniority of the lien", and non-US or small-firm lenders consolidate debt. Schmid p.97: Eberhart-Weiss find APR violated in 65-80% of bankruptcies; Moody's syndicated loans recover 70% (senior secured) versus 52% (senior unsecured). Beta LGD: Bohn-Stein p.313-315, p.526.

## 3. Veronesi (the shelf's Tuckman-style source): price-yield, duration, convexity, OAS (Ch 4-B)

Source: `Veronesi_Fixed_Income_Securities` (Veronesi, Wiley 2010; 841 PDF p.; printed = PDF - 36). **Tuckman-Serrat is not on the shelf.** Not in Veronesi: G/I-spread, Z-spread as an object, discount margin, YTW, make-whole, CS01 (no hits); DV01 only in Dynkin p.214, p.226.

**Price-yield (Ch 2, p.78-87).** Coupon bond = portfolio of zeros (eq. 3.11); bootstrap Z(t,T_i) = [P_c - (c_i/2)100 sum Z_j]/[100(1 + c_i/2)] needs every bond (eq. 2.27, p.83). Semi-annual YTM is the single rate that discounts cash flows to price (eq. 2.30) and is not the spot curve; Fact 2.10: same maturity, different coupons, different yields (p.83-84). Check: 9.5-year 4.750% and 8.875% Treasuries, fair prices 107.8906 and 141.5267, yields 3.7548% and 3.6603%; the old high-coupon bond traded at 140.0781, about 1% under fair, an illiquidity discount (p.84). YTM assumes coupons reinvested at y, a poor return measure (p.86). Clean + accrued = invoice; Actual/Actual, 30/360, Actual/360; T-bill d = (100 - P)/100 x 360/n, 97.477 for 182 days is 4.99% (p.87).

**Duration (Ch 3, p.111-126).** D = -(1/P) dP/dr, dP = -D P dr, modified duration against the continuously compounded spot shift (eq. 3.1-3.2, p.112); $100m at D = 10 loses $100,000 per bp. Zero: D = T - t (p.113); portfolio: value-weighted average (p.114-115; $100m 5y plus $200m 10y STRIPS gives 8.3, $249,000 per bp); 10-year 6% bond priced 107.795 has D = 7.762 (p.116). Duration equals average payment time only for fixed cash flows; a floater has D = time to next reset (eq. 3.16, p.117-118). Table 3.2 (p.119): duration falls with coupon (0%: 10.00, 6%: 7.76, 12%: 6.88) and with yield level. Against the semi-annual yield, MD = Macaulay/(1 + y/2); Veronesi prefers the spot shift because YTM is bond-specific and undefined for floaters and optioned bonds (p.119-120). Dollar duration D$ = P x D covers zero-value positions (p.120).

**Convexity (Ch 4, p.149-153).** C = (1/P) d2P/dr2 (eq. 4.1); dP/P = -D dr + (1/2) C dr^2 (Fact 4.1); zero C = (T - t)^2. Test case (Example 4.1): 20-year zero, r from 5% to 2.5%: price 36.79 to 60.65; duration alone 55.18; duration plus convexity (C = 400) 59.78 (the page prints 36.76 once, a typo). Finite-difference convexity C ~ [P(+x) + P(-x) - 2P]/[P x^2] (p.366). Spot-rate duration on a tree D = -(1/V)(V_u - V_d)/(r_u - r_d) (eq. 10.14-10.15, p.408).

**Callable bonds and OAS (Ch 12.1, p.459-470).** Callable = non-callable minus American call on a recombining tree; issuers wait when waiting beats exercise (node (15,5): call 8.37 versus 7.404 immediate, p.463). Example 12.2: 7.5% Treasury due 15 Aug 2014, first call 2009, simple-BDT tree fitted to 8 Jan 2002: 169.732 - 22.33 = 147.40 versus quote 146.5 (p.463-466). Negative convexity below about 14% as price converges to 100 (p.464, Figure 12.1). OAS is the parallel spot-curve increase that equates model and traded price; here 11 bp moves the model to 146.55; liquidity can produce a positive OAS and OAS is model-dependent (p.467). Relative value: buy the cheap callable, short the replicating non-callable position N^L = (V_u - V_d)/(P_u - P_d) with coupons (eq. 12.3-12.5, p.468-469; three-period example 100.3564 versus 100.1, N0^L = 0.5852). Risk-neutral probabilities price, physical probabilities assess risk (p.408; Example 10.3: structured zero value 79.88 versus plain 79.77, spot-rate duration 2.08 versus 4.62).

**Spread vocabulary elsewhere.** Bohn-Stein p.68-69: bid-offer, total (to Treasuries or a corporate-risk-free curve 10-20 bp under swaps), expected (total minus EL), credit, liquidity (residual), zero-coupon and par spreads; OAS needs a lattice and Z-spread is the lattice fit without optionality. Schmid p.159-161: par and market asset swaps (Libor + spread), born in the early 1990s. Ben Dor p.51, p.267-270 (spread duration, DTS); Dynkin p.333 (key-rate durations).

## 4. Greeks and option measures (Ch 6-B)

**Gap.** Natenberg and Hull are not on the shelf (Hull appears only in reference lists). Greeks must be built from four anchors plus the web.
- **BSM as the credit Greek machine (Bohn-Stein p.135-137).** PDE (1/2) sigma_A^2 A^2 E_AA + r A E_A + E_t - rE = 0; equity-delta identity sigma_E = (dE/dA)(A/E) sigma_A; zero to 50% leverage roughly doubles equity volatility; asset volatility matters far more than drift inside 2-3 years (p.136-137). Solving for implied A and sigma_A is the credit analogue of implied volatility.
- **Credit delta = hedge ratio (Dynkin p.87).** Bond is short a put on V plus a riskless asset, equity a call; the analytical Merton hedge ratio (Schaefer-Strebulaev 2008) rises as ratings worsen and ran about 5% below empirical ones in IG and HY (Table 1.6).
- **Theta-gamma (Veronesi p.611-612, eq. 16.17-16.18).** Delta-hedged: (1/Pi) dPi/dt + (1/2)(1/Pi) d2Pi/dr2 sigma^2 = r, so high theta means low or negative gamma; a short call on a zero hedged with the zero earns carry for negative convexity (the book's "HY is a short put" line).
- **Replication (Veronesi Ch 9-10, p.599-601, p.626; eq. 12.5).** Delta N^L and bond N^S at each node; model value 2.2921 against a 3.00 option price gives a 0.7079 edge with Delta_0 = 0.4731 (p.611). Black's cap and swaption formulas: Veronesi Ch 20. No vega, skew or smile text exists on the shelf.
- **Change of measure (Bolder p.478).** The likelihood ratio f/h is the Radon-Nikodym derivative, "closely related to the Girsanov theorem", usable to move from P to Q; importance sampling is a change of measure.

## 5. Fundamental law of active management (Ch 2, 4, 28, App E)

**Gap.** Grinold and Kahn are cited, not on the shelf (Paleologo p.205; Ben Dor p.239, p.398). Derive IR = IC x sqrt(BR) once and source it to Grinold (1989); the shelf supplies four credit-relevant partial anchors.
- **Paleologo p.149-150 (section 8.2.2).** IR = (2p - 1) sqrt(252 N_e). Numbers: p = 51% with 70 names gives 2.6; p = 50.5% gives 1.3; N_e = 3,000 reaches about 8. Diversification is "a skill multiplier", but hit rate falls with breadth beyond a threshold, the standard error of an annual hit rate with 90 names is 0.33% against a 0.5% edge, and a PM can see a lower measured IR after raising breadth almost half the time. Effective names N_e = 1/H, H = sum of squared GMV weights (Procedure 8.1, p.150): the breadth input for correlated bond positions.
- **Ben Dor p.239-240.** Skill = correlation of predictions and realisations (Grinold-Kahn); conditional idiosyncratic variance (1 - rho^2) sigma^2; pairs hedge H = (beta_l/beta_s)/(1 + (1 - rho^2) sigma_s^2/(beta_s^2 sigma_m^2)), half the beta ratio as rho goes to 0 (eq. 8.8).
- **Dynkin p.345.** Desclee et al. (2014): issuer selection beats market timing and sector rotation because breadth is larger; concession alpha averaged 14 bp a year since 2008 and needs no manager skill under current index rules.
- **Man 2022 p.28.** Single-factor IRs: value 2.15, momentum 1.69, quality 1.55, informed investor 0.79; combined 2.35 (back-test IRs).
- **Limits (web).** Independent bets, constant IC and no constraints; the transfer coefficient (Clarke et al. 2002) and issuer clustering (Ch 7-B) qualify it.

## 6. Brownian-bridge first-passage correction (Ch 7-B Monte Carlo, Ch 6-B Black-Cox)

**Citation to use (web-verified):** Beaglehole, D. R., Dybvig, P. H., Zhou, G. (1997), "Going to Extremes: Correcting Simulation Bias in Exotic Option Valuation", *Financial Analysts Journal* 53(1), 62-68, DOI 10.2469/faj.v53.n1.2057 (IDEAS record fetched). Abstract: for options on extremes, simulation converges slowly as the grid is refined and even daily intervals give unacceptable errors; fix: draw the extreme on each sub-interval from the known distribution of the extreme of a Brownian bridge. Andersen and Brotherton-Ratcliffe (1996) share the credit (named in Shevchenko 2003; not opened). QuantLib documents its barrier engine's "Brownian-bridge correction" as this paper.

**Formula (Shevchenko 2003, arXiv:0904.1157, Eq. 11, verified).** With x = ln S_m, y = ln S_{m+1}, b = ln(barrier), constant volatility on the step and x, y on the same side, P(touch) = exp(-2 (b - x)(b - y)/(sigma^2 dt)); declare default on the step with that probability using one uniform draw. Naive discrete monitoring has a bias that decays only like 1/sqrt(M) (Broadie-Glasserman-Kou).

**Alternative.** Broadie, Glasserman, Kou (1997), "A continuity correction for discrete barrier options", *Mathematical Finance* 7(4), 325-349: shift the barrier by exp(+/- beta sigma sqrt(dt)), beta = -zeta(1/2)/sqrt(2 pi) = 0.5826 (constant and reference confirmed in Howison-Steinberg 2005, who note the exponential form is only first-order accurate). Use BGK when covenants are tested on discrete dates; use the bridge when the model barrier is continuous (Black-Cox). Glasserman (2004), *Monte Carlo Methods in Financial Engineering*, section 6.4, is the textbook home (not opened; confirm the section number).

**Shelf anchors.** Bohn-Stein p.150-152: zero drift with an absorbing barrier gives pd_a = 1 - [P(ln A_T > ln X) - P(ln A_T < ln X)] = 2 pd, the reflection principle (printed 119). Schmid p.62-66: explicit first-passage solutions are mostly unknown so use Monte Carlo; a pure diffusion makes instantaneous default probability zero (p.66). Bolder p.260: first passage as a stopping time, {tau <= T} = {A_T <= K}; Bolder Ch 8 has no barrier-bias section, so BDZ is the only fix.

## 7. Bolder and Bohn-Stein: threshold models, copulas, tail dependence (Ch 7-B, Ch 5, Ch 6)

Source: `Bolder_Credit_Risk_Modelling` (Bolder, Springer 2018; 704 PDF p.; printed about PDF - 25 to - 29; Python code boxes).
- **Gaussian threshold (PDF p.180-183).** y_n = sqrt(rho) G + sqrt(1 - rho) eps_n (eq. 4.8), pairwise correlation rho, default below Phi^-1(p_n); obligor loadings give sqrt(rho_n rho_m) (eq. 4.11-4.12). Merton "reduces to a one-factor threshold model" (p.283; first passage p.260).
- **Tail dependence (p.204-212).** Lambda_upper = lim P(Y > F^-1(q) | X > F^-1(q)); lower = lim C(q,q)/q; exchangeable: Lambda = 2 lim P(U1 <= q | U2 = q) (eq. 4.56-4.63; the proof sketch for dC/du = P(U1 <= u1 | U2 = u2) is "neither precise, nor probably even exactly true", fn.11). **Gaussian: Lambda = 0 for rho < 1** (eq. 4.66, p.208-209). **Student-t: Lambda = 2 F_{T_{nu+1}}(-sqrt((nu+1)(1 - rho)/(1 + rho)))** (eq. 4.68, p.209; Algorithm 4.8, p.211): positive for all rho in (-1,1), rising in rho, falling in nu (Figure 4.6, p.210). t-threshold: y_n = sqrt(nu/W)(sqrt(rho) G + sqrt(1 - rho) eps_n), var = nu/(nu - 2) (eq. 4.69-4.72, p.212-213).
- **Size of the effect (Table 1.2, p.61).** At the 99.97th percentile VaR is $84.7 independent, $229.1 threshold, $197.3 mixture; expected shortfall $92.3, $270.0, $222.9.
- **Further:** normal-variance mixtures and multi-factor (p.222-254); correlation estimation by moments, likelihood and transition likelihood (Ch 10, p.597-655); Monte Carlo and importance sampling (Ch 8, p.454-511). Bohn-Stein Ch 8: bivariate-normal default correlation (p.501), DD transition densities (p.502-507), copulas and frailty (p.566-571).

## 8. Dynkin and Ben Dor: empirical duration regimes (Ch 4-B, Ch 8)

Sources: Ben Dor et al., *Quantitative Credit Portfolio Management* (Wiley; page headers dated Oct 2011; Ch 7, PDF p.190-193; printed = PDF - 30) and Ben Dor, Desclee, Dynkin, Hyman, Polbennikov, *Systematic Investing in Credit* (Wiley 2021; Ch 10, PDF p.429-453).
- **Derivation (Ben Dor p.190-191).** R_i ~ -D_i dy - D_i s_i ds_rel (7.1); d s_rel/dy ~ rho sigma_s/sigma_y (7.2); **empirical duration = -D_i (1 + s_i rho_{y,s} sigma_s/sigma_y)** (7.3). Regression R_i = beta D dy + gamma D s dy + eps (7.4); hedge ratio H(s) = beta + gamma s (7.5).
- **Table 7.1 (p.192; Barclays daily, Aug 1998 to Nov 2009).** Beta by Aaa-Aa, A, Baa, Ba, B, Caa: 0.94, 0.92, 0.85, 0.41, 0.15, 0.07; hedge ratio at average OAS 0.88, 0.85, 0.80, 0.22, -0.03, -0.15; at maximum OAS Ba -0.26, B -0.42, Caa -0.52; model-based 0.95, 0.93, 0.88, 0.24, -0.04, -0.23; rho(y,s) -0.14, -0.17, -0.23, -0.50, -0.56, -0.40; relative-spread volatility 1.6-2.5% in every bucket (DTS); R^2 0.79 (Aaa-Aa) falling to 0.01 (B, Caa). IG stays rate-sensitive at all spreads; HY is "almost completely disconnected" (p.193). Baa: 0.83 at 1% spread, 0.75 at 5% (p.193).
- **Dynkin Ch 10 (p.435-438).** Pooled monthly regression, noncallable bonds in the Bloomberg Barclays US IG Corporate Index, Jan 1992 to Apr 2014, carry-adjusted returns: base hedge ratio 0.97 (t = 405), spread sensitivity -0.13 per point; premium bonds are more rate-sensitive when yields rise and less when they fall, discount bonds the reverse; coupon effect on spread about 10 bp per 1% of coupon since 2008. Mechanism: negative rate-spread correlation plus proportional (DTS) spread moves.
- **Original paper:** Ambastha, Ben Dor, Dynkin, Hyman, Konstantinovsky (2010), *J. Fixed Income* 20(1):5-27 (in Dynkin p.449; not web-verified).
- **Use:** Ch 4-B states analytical duration then eq. 7.3; Ch 8's sign discipline (negative empirical duration for CCC) rests on the B and Caa rows.

## 9. Where the shelf is dated or superseded (2018-2026, web-confirmed)

- **Moyer exclusivity (p.94, p.346).** "120 days ... additional 60 days", extended "virtually indefinitely". Superseded by 11 U.S.C. 1121(d)(2): the 120-day period "may not be extended beyond ... 18 months", the 180-day period beyond 20 months, added by Pub. L. 109-8 s.411 (2005; effective for cases filed after 17 Oct 2005) (LII, fetched).
- **Moyer claims (p.310-312, p.416).** Predates 503(b)(9), the 20-day goods administrative expense added by Pub. L. 109-8 s.1227(b) (LII 503, fetched).
- **Moyer cramdown and insiders (p.359).** *U.S. Bank v. Village at Lakeridge*, No. 15-1509 (decided 5 Mar 2018): non-statutory insider status, which decides whether an accepting class counts under 1129(a)(10), gets clear-error appellate review (opinion text fetched). *Czyzewski v. Jevic*, No. 15-649 (22 Mar 2017): structured dismissals may not skip priority without consent of affected creditors (opinion text fetched). *Harrington v. Purdue Pharma*, No. 23-124 (27 Jun 2024): no non-consensual third-party releases in a plan (syllabus fetched). Moyer p.362 leaves cramdown present value open; *In re MPM Silicones (Momentive)* (2d Cir., 20 Oct 2017): market rate where an efficient market exists, otherwise the Till formula (Skadden, fetched).
- **Moyer on out-of-court holdouts (p.85-87, p.334).** Exit-consent stripping and unanimity friction are the LMT mechanism; the 2020-2026 case law (Serta, 5th Cir. 31 Dec 2024, and Wesco/ConvergeOne) is already in `state/research/trend_lmt_default_recovery_cycle.md` (Serta fetched there). Prepack share (<7% of cases, 1998-2002, p.336) is stale; no fresh series was fetched, so treat it as an open data task.
- **Spread and curve vocabulary (Bohn-Stein p.68, Schmid p.159-161, Veronesi App. 6.5).** Libor/swap-curve benchmarks and Libor+ asset swaps: USD LIBOR panel settings ceased 30 Jun 2023 and the ARRC had selected SOFR in 2017 (NY Fed ARRC page, fetched). Rewrite discount-margin and asset-swap boxes on SOFR or Treasury benchmarks.
- **Empirical duration (Ben Dor Table 7.1: 1998-2009; Dynkin Ch 10: 1992-2014).** Samples pre-date the 2022 shock (10-year Treasury 1.52% on 31 Dec 2021 to 3.88% on 30 Dec 2022, peak 4.25% on 24 Oct 2022; FRED DGS10, fetched). Rudin (2025, Springer, *Derivatives Applications in Asset Management*, ch. "Hedging Interest Rate Risk in High-Yield Bonds") still finds HY empirical duration far below analytical, even negative, and that Treasury-futures hedges by analytical duration can raise volatility (abstract fetched). Re-estimate on 2022-2026 data before printing Table 7.1 values as current.
- **Structural models (Bohn-Stein p.150, printed 118).** Their note that empirical research "continues to cast doubt" on structural models (Huang-Huang, Eom et al.) is balanced by Schaefer-Strebulaev (2008, *JFE* 90(1):1-19): structural models give poor price predictions yet accurate equity hedge ratios (abstract via search); Dynkin p.87 uses that result.
- **Fundamental law (Paleologo p.149).** The unconstrained IC x sqrt(BR) form is extended by the transfer coefficient (Clarke, de Silva and Thorley 2002, *FAJ* 58(5):48-66; IDEAS record seen in search): IR = TC x IC x sqrt(BR).
- **Pure-vintage caveats.** Bohn-Stein (2009) and Moyer (2005) pre-date the post-2008 LGD and bankruptcy-venue data; Veronesi (2010) pre-dates negative-rate regimes; Schmid (2004) uses pre-crisis Moody's recovery tables; Bolder (2018) is current on copulas.

## 10. Quotation bank (verbatim, book_id p.N; PDF page numbers; footnote markers omitted)

1. "any investor (or group thereof) that accumulates a 33.4% position in the claims of a class can prevent approval by voting no. This is a blocking position; the investor cannot enforce its will, but can stymie the process." (Moyer_Distressed_Debt_Analysis p.358)
2. "For a plan to be crammed down on an objecting class, there are three requirements: (1) at least one impaired class must vote in favor of the plan, without counting the votes of insiders; (2) the plan may not unfairly discriminate against the objecting class; and (3) the plan must be fair and equitable with respect to the objecting class." (Moyer_Distressed_Debt_Analysis p.359)
3. "No claim junior to the objecting class can receive any recovery unless the objecting class’s claims are paid in full — essentially, strict enforcement of the absolute priority rule." (Moyer_Distressed_Debt_Analysis p.360)
4. "since “tipping” is a very common, if not expected, part of the plan consensus-building process, investors in more senior claims may want to budget in potential “tip giving” that could reduce their expected recovery." (Moyer_Distressed_Debt_Analysis p.361)
5. "a class minority can effectively defeat the wishes of the majority to effect an out-of-court restructuring. In bankruptcy, minority rights are significantly reduced." (Moyer_Distressed_Debt_Analysis p.334)
6. "Essentially, the law assumes that all liabilities of a firm are equal unless the holders of those liabilities explicitly agree to reduce the priority, or subordinate their claim." (Moyer_Distressed_Debt_Analysis p.160)
7. "those not participating in the exchange may be better off than those that do, but if too many hold out, all will be worse off." (Moyer_Distressed_Debt_Analysis p.85)
8. "the debtor has the exclusive right to propose a plan of reorganization for 120 days following the filing of the petition and then an additional 60 days to solicit acceptances of the plan." (Moyer_Distressed_Debt_Analysis p.346)
9. "The risk-neutral DD is smaller than the physical DD, reflecting the adjustment that results in a higher PD, all else equal." (Bohn_Stein_Active_Credit_Portfolio_Management p.210)
10. "In the reduced-form framework, we do not have the same kind of direct connection between the physical and risk-neutral worlds." (Bohn_Stein_Active_Credit_Portfolio_Management p.343)
11. "The word spread is perhaps the most overloaded (and sometimes abused) word in finance." (Bohn_Stein_Active_Credit_Portfolio_Management p.68)
12. "Another form of seniority analysis involves considering the relative debt cushion below the instrument of interest." (Bohn_Stein_Active_Credit_Portfolio_Management p.309)
13. "However, this rule is more a theoretical than a practical one. E.g., Eberhart & Weiss (1998) find that in 65% - 80% of all bankruptcies the absolute priority rule is violated" (Schmid_Credit_Risk_Pricing_Models p.97)
14. "Different recovery models can be transformed into each other. Basically, the value of the defaultable security at default is expressed using different numeraires." (Schmid_Credit_Risk_Pricing_Models p.95)
15. "if we model the firm value process only with a continuous diffusion the probability of a firm to default in the next instant is zero. Hence, firms would never default unexpectedly." (Schmid_Credit_Risk_Pricing_Models p.66)
16. "Pricing (task 1) is performed by using risk neutral probabilities, as shown earlier. Risk assessment (task 2) is performed by using risk natural, i.e., true, probabilities." (Veronesi_Fixed_Income_Securities p.408)
17. "Securities with embedded American options are often traded on an option-adjusted-spread (OAS) basis." (Veronesi_Fixed_Income_Securities p.467)
18. "While lower interest rates still increase the price of the bond, they do so at an increasingly lower rate, as opposed to an increasing rate as for any non callable bond." (Veronesi_Fixed_Income_Securities p.464)
19. "no arbitrage implies that a large convexity (Gamma) is always counterbalanced by a large, and opposite, portfolio sensitivity to time, Theta." (Veronesi_Fixed_Income_Securities p.611)
20. "Based on Merton, a corporate bond (D) is short a put on the underlying asset (V) plus a risk‐free asset, while the equity (E) is equivalent to a call option on V." (Dynkin_Systematic_Investing_in_Credit p.87)
21. "If this correlation is negative, the empirical duration would be lower than the analytical one and may even end up being negative." (Ben_Dor_Quantitative_Credit_Portfolio_Management p.191)
22. "The power of diversification is great. It is not a skill: it is a skill multiplier." (Paleologo_Advanced_Portfolio_Management p.149)
23. "in the large, pricing applications employ the equivalent martingale, or risk-neutral, measure, Q. Risk managers, conversely, typically use the physical measure, P." (Bolder_Credit_Risk_Modelling p.37)
24. "The consequence is that the Gaussian distribution does not exhibit tail dependence, since the tail-dependence coefficient has a zero value." (Bolder_Credit_Risk_Modelling p.208)
25. "On average, the risk-neutral estimates are a factor of 30 to almost 70 times larger than the physical-measure equivalents." (Bolder_Credit_Risk_Modelling p.592)

## 11. Chapter map (shelf content by book chapter number)

| Book chapter | Shelf pages to quote or derive from |
|---|---|
| 1 (anthology) | Bolder p.37; Moyer p.68 (pricing paradox) |
| 2, 4, 28, App E (fundamental law) | Paleologo p.149-150; Ben Dor p.239; Dynkin p.345; Man 2022 p.28; derive IC x sqrt(BR) once, cite Grinold 1989 |
| 4-B (bond math) | Veronesi p.83-87, p.112-120, p.151-153, p.366, p.408, p.464-470; Bohn-Stein p.68-69; Schmid p.159-161; Ben Dor p.190-193 |
| 5 (distributions) | Bohn-Stein p.289, p.298-299, p.309, p.313-315; Schmid p.95-97 |
| 6 (Merton, intensity) | Bohn-Stein p.135-137, p.150-152, p.209-211, p.342-344; Schmid p.62-66, p.71, p.129; Bolder p.260 |
| 6-B (options, two measures) | Bohn-Stein p.131, p.209-211, p.342-344; Bolder p.37, p.590-592; Schmid p.189-195, p.263; Veronesi p.408, p.611; Dynkin p.87 |
| 7-B (statistics, MC) | Bolder p.204-214 (tail dependence), p.454-480 (MC, importance sampling), p.597-655 (correlation estimation); BDZ and BGK (web) |
| 8 (IDO, empirical duration) | Ben Dor p.190-193 (eq. 7.1-7.5, Table 7.1); Dynkin p.435-438 |
| 12-B (restructuring state machine) | Moyer p.94-108, p.158-161, p.334-336, p.346, p.356-362; Bohn-Stein p.309 |
| 13-14 (LMTs, default cycle) | Moyer p.85-87, p.334, p.336; Bohn-Stein p.289 |
| 16 (post-reorg) | Moyer p.362 (rights offerings, exit financing); Bohn-Stein p.299 (post-default price versus ultimate recovery) |
| App E laws | "say which measure": Veronesi p.408, Bolder p.37; "charge the jump once": Schmid p.66; "default is a menu, recovery is a U": Bohn-Stein p.298-299; "the court is a random variable with timestamps": Moyer p.94, p.346, p.356 |

## Sources

Shelf (local, read this session): `source_pdfs/` Moyer, Bohn_Stein, Schmid, Veronesi, Bolder, Ben_Dor, Dynkin (epub), Paleologo, Man_Quantitative_Credit_Alpha_Early_Mover_2022. Internal: `state/research/trend_lmt_default_recovery_cycle.md`.

Web, fetched and read this session:
- https://ideas.repec.org/a/taf/ufajxx/v53y1997i1p62-68.html (Beaglehole, Dybvig, Zhou 1997)
- https://ar5iv.arxiv.org/html/0904.1157 (Shevchenko, Brownian-bridge formula, Eq. 11)
- https://quantlib.js.org/docs/classes/_ql_pricingengines_barrier_mcbarrierengine_.mcbarrierengine.html
- https://people.maths.ox.ac.uk/howison/papers/discbarrier.pdf (Howison and Steinberg 2005; BGK constant and reference)
- https://www.law.cornell.edu/uscode/text/11/1121 ; /1129 ; /503
- https://www.supremecourt.gov/opinions/23pdf/23-124_8nk0.pdf (Purdue)
- https://www.govinfo.gov/content/pkg/USREPORTS-583/pdf/USREPORTS-583-387.pdf (Lakeridge)
- https://www.govinfo.gov/content/pkg/USREPORTS-580/pdf/USREPORTS-580-451.pdf (Jevic)
- https://www.skadden.com/insights/publications/2019/01/2019-insights/second-circuit-adopts-secured-creditor (Momentive)
- https://www.newyorkfed.org/arrc/sofr-transition
- https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
- https://ideas.repec.org/h/spr/sprchp/978-3-031-86354-7_24.html (Rudin 2025)

Seen in search results only (not opened; confirm before citing): CFA Institute record of BDZ; IDEAS records for Clarke-de Silva-Thorley 2002 (https://ideas.repec.org/a/taf/ufajxx/v58y2002i5p48-66.html) and Schaefer-Strebulaev 2008 (https://ideas.repec.org/a/eee/jfinec/v90y2008i1p1-19.html); Columbia record of BGK (volume/pages taken from Howison-Steinberg: *Math. Finance* 7, 325). Not found: Ambastha et al. (2010) and Grinold (1989) volume/pages (Ambastha is in the Dynkin p.449 reference list; the Grinold (1989) journal volume and pages were not verified).

## Book placement

1. **Ch 12-B** is the main Moyer consumer: build the state machine from p.94-108 and p.334-362; test the waterfall code on Table 7-1 (Dead Co.: bank 50.00, trade 18.75, sub 6.25), the voting and blocking arithmetic (p.107, p.358), tipping (p.361) and the secured-cramdown rule (p.362); put the 2005-2024 updates of section 9 in one "what changed since Moyer" box.
2. **Ch 4-B** should follow Veronesi's order (discount factors, YTM, duration, convexity, callable tree, OAS) with the 20-year-zero test (36.79 / 60.65 / 55.18 / 59.78) and the Aug-2014 callable (169.732 - 22.33 = 147.40 against 146.5, OAS 11 bp). Add G/I/Z/DM/YTW/CS01/make-whole from outside the shelf; Bohn-Stein p.68 supplies the spread taxonomy and Ben Dor Ch 7 the bridge to empirical duration.
3. **Ch 6-B** gets the P-to-Q section from Bohn-Stein (pd^Q = Phi(Phi^-1(pd) + R lambda sqrt(T)); h^Q = psi h) and Bolder p.592 (risk-neutral PD 27 to 66 times physical for four large banks over an 18-month CDS sample), with Veronesi p.408 as the one-line rule; Greeks need a non-shelf textbook.
4. **Ch 7-B** takes Bolder Ch 4 and Ch 8 plus the Brownian-bridge box (BDZ 1997; BGK 1997 as the monitoring-shift alternative).
5. **Ch 8 and App E**: Table 7.1 as the empirical-duration regime table with the 2022 re-estimation task; the five law-to-page mappings in section 11.
6. **New sections justified:** (a) a one-page "What changed since the shelf" box in each primer (section 9); (b) a "Fundamental law, derived once" section (Ch 2, with Ch 4 and Ch 28 pointing to it) with the transfer coefficient; (c) a "Tail dependence in one page" box (Bolder Table 1.2: 99.97th-percentile VaR 84.7 versus 229.1) in Ch 7-B; (d) a data task: re-estimate Ben Dor Table 7.1 and Moyer's prepack share on 2022-2026 data. Gaps needing non-shelf sources: Tuckman/Serrat, Natenberg/Hull, Grinold-Kahn.

<!-- STATUS: COMPLETE -->
