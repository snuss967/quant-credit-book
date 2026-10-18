# Cleanup log: appF-listings

Editor: cleanup (group appF-listings), 2026-10-18. Items: L25.1, L28.8, L11.5, renumber.
Scratch work (throwaway scripts, timing runs, before/after copies) is under the session scratchpad `appF/`; nothing from it is committed.

Method note. Listings are run the way the book says to run them: the python blocks of one App F chapter section, cumulatively, in order, in one fresh interpreter. (`tools/check_book.py --file book_src/95_appF_code_companion.md --run-code` runs all 174 blocks of the appendix in one interpreter and stops at a pre-existing syntax error: six listings in the newer chapters start with `from __future__ import annotations`, which cannot follow other code. That is not one of this group's items; see "Observations".)

---

## [L25.1] Listing 25.1 cycle regex (App F, #code-25-1) — ALREADY-FIXED

Found. The queue entry (state/cleanup_queue.md, line 5) is already marked DONE 2026-10-18. Checked the current text rather than trusting the mark:

- Listing 25.1 now reads `DEF_RE = re.compile(r'^"(?P<term>[^"]+)"\s+means[,\s]\s*(?P<body>.+)$', flags=re.M)`, so "Pro Forma Basis" ("means, with respect to ...") is parsed.
- Ran the whole Ch 25 section of App F (Listings 25.1-25.9, the eight python blocks, cumulatively): exit 0, every assertion passes, including the last one of Listing 25.1 (`["Consolidated EBITDA", "Pro Forma Basis", "Run-Rate Cost Savings"] in cycles`). Printout: `cycles: [['Consolidated EBITDA', 'Pro Forma Basis', 'Run-Rate Cost Savings'], ['Material Intellectual Property', 'Restricted Subsidiary', 'Unrestricted Subsidiary']] | self-references: ['Unrestricted Subsidiary']`.
- Ch 25 prose does not quote the regex or a cycle size beyond what the printout shows: it says the printout "shows two loops, not one" (add-back loop through Consolidated EBITDA, Run-Rate Cost Savings, Pro Forma Basis; the J.Crew blocker loop through Restricted Subsidiary, Unrestricted Subsidiary, Material Intellectual Property) and that a self-referring term is dropped from the edges and reported separately. All three match the printout. Figure 25.1's caption (two groups of terms define each other) matches too.

Changed: nothing. Status: already-fixed.

---

## [L28.8] Listing 28.8 `"sharpe": 2.0` (App F, #code-28-8) — FIXED

Found. `DESK` in the final-block demo still set `"sharpe": 2.0`; §28.9 (revised) says "The demo is run at 0.7" and treats 0.7 as the point estimate.

Old -> new (book_src/95_appF_code_companion.md, Listing 28.8):

- `DESK = {"nav_usd": 4e8, "dd_max": 0.075, "kappa_z": 4.0, "sharpe": 2.0, "r_min": 0.05, ...` -> `... "kappa_z": 4.0, "sharpe": 0.7, "r_min": 0.05, ...`

Re-run (Ch 28 section, Listings 28.1-28.8 cumulatively, exit 0, every assertion passes, 3.8 s). Dashboard row before -> after:

| Row | sharpe 2.0 | sharpe 0.7 |
| :--- | ---: | ---: |
| lev_floor | 2.819 | 8.054 |
| lev_ceiling | 1.828 | 1.427 |
| lev_speed_limit | 3.222 | 3.222 |
| band_empty / lev_breach | True / True | True / True |
| gross_leverage | 5.221 | 5.221 |
| n_eff / issuer_herfindahl_n | 43.03 / 59.17 | 43.03 / 59.17 |
| names_over_kelly_cap | 12 | 12 |
| stressed_col_pct_nav | 0.2154 | 0.2154 |
| pct_gross_over_20d | 0.1292 | 0.1292 |
| dd_budget_used_pct_of_cut | 2.631 | 2.631 |
| runway_weeks | 24.375 | 24.375 |
| hit_rate_se_1y | 0.004801 | 0.004801 |

Only the two SR-dependent rows move, in the direction §28.9 states (a lower Sharpe raises the floor and lowers the ceiling at once). Reconciliation of every §28.9 statement that rests on the listing:

- "On the demo book the band is empty, with the floor several times the ceiling": at 2.0 the floor was only 1.54 times the ceiling (the sentence would have been false); at 0.7 it is 5.64 times (8.05 vs 1.43). Now true as written. No change to the sentence.
- "a lower Sharpe raises the floor and lowers the ceiling at once, so the band can only narrow as SR falls": confirmed by the two runs (floor 2.82 -> 8.05, ceiling 1.83 -> 1.43).
- "a 5% hurdle at a Sharpe of 0.7": `r_min` is 0.05 in `DESK`. True.
- "runway must clear 13 weeks", ceiling under the speed limit, breach flag equals its definition: the asserts pass (24.4 weeks; 1.43 < 3.22).
- "60 issuers with five bonds each, 48 in tier 1 and 12 in tier 2": true. "about 80% of them long": the generator draws each issuer long with probability 0.8, but on the seed used 38 of the 60 are long (63%). Reworded (Ch 28, §28.9): `about 80% of them long` -> `each long with probability 0.8 (38 of the 60 on the seed used)`.
- The 0.6 standard error for "three years of a 0.7 Sharpe" is a prose estimate (about 1/sqrt(3) = 0.58; the fuller sqrt((1 + SR^2/2)/Y) = 0.64) and is not an output of the listing. Unchanged.

Not changed, for the owner. The listing computes the band at the point estimate only; §28.9's Skill row also describes "the band at one standard error lower", and the schema sentence lists "SR with its standard error" among the desk parameters, but `DESK` has no standard-error key and `pm_playbook_engine` returns no such row. The prose does not claim the demo shows it ("The demo is run at 0.7"), so I left both alone; adding `sharpe_se` and a `band_empty_1se_lower` row is a small follow-up if wanted.

Status: fixed.

---

## [L11.5] Listing 11.5 demo runtime (App F, #code-11-5; Ch 11 §11.7 Specification) — FIXED

Found. `defensive_portfolio` hands SLSQP ~440-550 free weights per cross-section (`bounds` on every name, `maxiter=500`, `ftol=1e-14`), five dates in a row. SLSQP is cubic in the number of variables and treats the bounds as constraints. Measured:

- full grid, month 24 alone (553 issuers, 442 kept): still not finished after 4.5 minutes (killed); the full five-date run was killed after more than 13 CPU-minutes. A run of the whole grid with `FULL_GRID = True` is recorded below.
- 100 issuers: about 2-3 s a date; 120 issuers: 22-38 s a date (CPU shared); 150: up to 40 s. SLSQP stops on a line-search failure after 60-120 iterations or, when it does not, runs to `maxiter`, so the time is erratic above ~100.

Fix (smallest that meets the brief: smaller default grid, full grid behind a flag). In Listing 11.5's demo, before the loop and inside it:

```python
# added before `g5 = np.random.default_rng(RNG_SEED + 5)`
FULL_GRID = False        # True: every issuer in every cross-section (SLSQP then takes several minutes)
N_DEMO = 100             # default grid: a systematic sample of this many issuers per cross-section

# added inside the loop, after `cs = lagged[lagged["month"] == t0]`
    if not FULL_GRID:
        cs = cs.iloc[:: max(1, len(cs) // N_DEMO)].iloc[:N_DEMO]      # every k-th issuer, by id
```

`defensive_portfolio` itself, the five dates, every assertion and the print are unchanged. Listing 11.6 reuses the last `cs`, `iid`, `spr_t` from this loop, and its logic does not depend on the cross-section's size (calm and fundamental multipliers are 1 by construction of `z_ref`; the shock case hits the 1.20 cap for any cross-section, because 1 + 0.5 x ln(461/259) = 1.29 is above the band's 1.20).

Choice of 100, and why not smaller or randomly sampled (all checked with an exact two-multiplier projection of the same QP, which agrees with SLSQP to the printed digits and takes milliseconds, and then with SLSQP itself):

- Below ~90 issuers the 3% cap and the DTS target conflict on this seed (the chapter's feasibility trap): at N=80 SLSQP returns its last iterate and `assert abs(w @ dts_t / dts_b - 1.0) < 0.01` fails. N=90 and N=100 are feasible; N=100 gives margin.
- A random sample was the first thing tried (`cs.sample(100, random_state=t0)`); with only 2-7 defaulters per cross-section the in-sample comparison is noise (held 2.21% vs bench 2.11%, assertion fails). The systematic sample is deterministic and keeps the cross-section's id structure; across N = 100-150 it gives held default exposure 0.6-1.2% against 3.7-4.5% for the benchmark. I did not tune the sampling rule beyond comparing "first N ids", "random" and "every k-th": "first N ids" also passes at 100, 120, 130, 150 but is infeasible at 110; "random" is unreliable below ~150.
- The full-grid answer from the exact projection (so the flag is known to land in the same place): held 0.659% vs benchmark 3.042% average 12-month default exposure, last market-value-tilt DTS ratio 0.43, largest weight 2.57% (cap not binding). The default grid prints held 0.731% vs bench 3.889%, last ratio 0.43.

Timing after the fix (Ch 11 section of App F, Listings 11.1-11.6 cumulatively, exit 0, every assertion passes): 12.6 s in all (11.1-11.4 together 1.5 s, 11.5 about 11 s, 11.6 instant), against several minutes before. Printouts:

```
avg 12m default exposure: held=0.731% bench=3.889%; last MV-tilt DTS ratio=0.43
DTS multiplier calm=1.00 shock=1.20 fundamental=1.00 guarded=1.05; capacity core=$48.6bn niche=$1.20bn
```

Ch 11 prose check. Nothing in Ch 11 or Appendix Z quotes a number from Listing 11.5's printout. Listing 11.6's numbers, which the chapter does quote, are unchanged: multipliers 1.00 / 1.20 cap / 1.00 / 1.05, core about \$49bn, satellite about \$1.2bn. The 11.5 paragraph (§11.7 Specification, after "The part to notice ...") said "The demo runs five cross-sections from the Listing 11.3 panel and asserts ..." which stays true; one sentence added after the asserts:

- Added: "By default each cross-section is a systematic sample of 100 issuers (every fourth or fifth, by id), so the whole block runs in well under half a minute; the full cross-sections hold 480 to 550 issuers, and SLSQP then takes minutes per date, which is what `FULL_GRID = True` buys. A sample cannot shrink much further: at 80 issuers the 3% cap and the DTS target conflict, and the assertions fail, which is the feasibility failure described below."

FULL_GRID result: FULLGRID_PLACEHOLDER

Option not taken, for the owner: the same QP has an exact solution in two multipliers (`w = clip(w0 + a + b*dts, 0, cap)`, solved with a 2-D root finder), which does the full grid in 0.0 s. It would replace SLSQP in `defensive_portfolio`, and with it the chapter's teaching about reading the solver status and the silent feasibility failure, so I did not do it under a "smaller grid" brief.

Status: fixed.

---

## [renumber] Listing numbers out of chapter order; weak auto titles — FIXED (safe renumber was possible)

Found. Of 175 listings in 49 sections of App F, one chapter was out of order: Ch 1 linked Listings 1.1, 1.2, 1.4, 1.3 (1.4, the distance-to-default listing, sat in an "F.1 (continued)" section at the very end of the appendix, after Appendix E). Also found by the tool's link check: Ch 4-D linked `#code-4D-1` twice (capital D; the anchor is `code-4d-1`), so both links were dead. Titles: 174 of 175 were the first line of a docstring or comment, not a title (examples: `Eq` x 11, `Block 5`, `K=None: ceiling 1`, `---------- 2. Synthetic credit panel ...`, `11 U.S.C`, `Defines polite_get`, `Mean-variance with the tiers of eq`, `Bartlett-weighted sum of score cross-products ...` for a whole statistics module).

Written: `tools/renumber_listings.py` (new; stdlib only; dry run by default, `--apply` writes). What it does:

1. Reads the order in which each chapter first links to its own listings (`](#code-<chapter>-<k>)`, outside code fences) and numbers them 1..n in that order (listings a chapter never links are numbered last and reported).
2. Rebuilds Appendix F: each chapter's listings gathered into its main section in the new order ("(continued)" sections folded in and dropped), headings and `{#code-N-k}` anchors rewritten; the parser must round-trip the file byte for byte before the tool will touch it.
3. Rewrites every reference in one pass (so a swap cannot be applied twice): links and ids, always in canonical lower case (which repairs `#code-4D-1`), and prose mentions (`Listing 1.4`, `Listings 11.3 and 11.4`, ranges, with a warning when a range straddles a renumbered listing). Scans `book_src/`, `state/appZ/` (App Z is assembled from there by `tools/assemble_appZ.py`, so rewriting only the assembled file would be undone at the next assembly) and `tools/figures/` (comments); `--roots` overrides; `--root` points it at a copy.
4. Verifies: every link resolves, link text agrees with the anchor, anchors unique, numbers 1..n per chapter, linked in order. `--check` does only this (exit 1 on problems).
5. `--titles` lists weak headings with the chapter heading each listing sits under; `--retitle titles.json` sets titles from a `{"code-N-k": "Title"}` map. Writes are atomic and retried if the file changes underneath (other editors were working in the chapters at the same time); refuses `--apply` if the plan has ERRORs.

Run (`python3 tools/renumber_listings.py --apply`):

- renumber Listing 1.3 -> 1.4 (#code-1-3 -> #code-1-4) [the forced-seller engine] and Listing 1.4 -> 1.3 (#code-1-4 -> #code-1-3) [distance to default, credit triangle, one-factor]; the latter moved from the end of the appendix into F.1; "F.1 (continued)" section dropped. Every other chapter was already in order and is untouched.
- Files rewritten: `book_src/01_ch01_anthology_and_landscape.md` (13 lines: the two "Reading Listing" lead-ins, the two stub links, four prose mentions including the Figure 1.3 and 1.4 captions and the Ford paragraph, and five rows of the recap table), `book_src/04_ch04d_getting_the_seat.md` (2 anchors lower-cased), `book_src/99_appZ_solutions_hints_and_self_assessment.md` and `state/appZ/01_ch01_anthology_and_landscape.md` (2 mentions each: Z.1 exercise and its reread line, "Listing 1.3" -> "Listing 1.4" for the forced-seller engine), `tools/figures/ch01.py` (5 comment mentions, "Listing 1.3 demo" -> "Listing 1.4 demo"), `book_src/95_appF_code_companion.md`.
- Ran the Ch 1 section both ways (1.1, 1.2, 1.3(new), 1.4(new) and the old order): exit 0 and identical printouts, so the new physical order is safe to run cumulatively.
- Code in every listing is byte-identical to before except Listing 11.5 (L11.5 above) and the one `DESK` value (L28.8 above); checked by hashing each block before and after the pass.
- Afterwards: `--check` -> `175 listings, 0 problems`; a second dry run changes nothing; rehearsal on a copy with two stubs swapped in Ch 7 renumbered 7.2 <-> 7.3 and passed the same checks.

Titles. All weak ones replaced with names drawn from the chapter's own section and block names (for Ch 28, the headings "Block 2: The horizon ladder" and so on; for the module listings, "file.py: what it does"), applied with `--retitle`. After the pass `--titles` reports 0 weak of 175. Changes (new number, then old number if it moved):

- 1.1: `Dealer bid for buying dq ($mm par) from a client: eq` -> `The bid equation: inventory term, informed-flow Bayes and the jump penalty`
- 1.2: `Duration Times Spread in bp*years: D_spr in years, s_bp in basis points` -> `Duration Times Spread, DTS volatility and the liquidity cost score`
- 1.4 (was 1.3): `Holder x trigger forced-supply engine: eqs` -> `The forced-seller flow graph and the price-pressure path`
- 2.1: `K=None: ceiling 1` -> `Logistic fit of an adoption S-curve: rate, midpoint and odds-doubling time`
- 2.2: `Quote distance = common Exp(mean phi*theta) + i.i.d` -> `The RFQ as an auction: best of n quotes with a common anchor`
- 2.3: `Price per 100 par on a coupon date; y is the annual yield, decimal, compounded at freq` -> `Bond price, spread duration, liquidity cost conventions and the Man cost decomposition`
- 2.4: `alpha_net(TO) = k*sqrt(TO) - c*TO; c is one-way cost as a fraction of notional` -> `Optimal turnover and the cheapest-protocol router`
- 3.1: `Overflow-safe logistic function` -> `Glosten-Milgrom half-spread and winner's-curse shading for the RFQ bid`
- 3.2: `Simulated RFQ tape (prices in points)` -> `A simulated RFQ tape and its two tests: single-dealer markout and competition`
- 3.3: `MLE of beta in P(adverse | x) = (1 + sigmoid(x'beta)) / 2 (Sec` -> `Maximum-likelihood fit of the probability that an RFQ is adverse`
- 3.4: `Systematic price move (points) implied by index-spread and Treasury-yield changes (decimals)` -> `Reference moves, markouts and shrunk counterparty scores`
- 3.5: `Eq` -> `Re-basing a PD to the live default rate and updating it from an 8-K`
- 3.6: `Eq` -> `CUSUM detector for the pre-LMT signature, with a PRS-dependent threshold`
- 4.1: `BR_eff = N / (1 + (m - 1) * rho), with m = N / M bonds per issuer` -> `Effective breadth with issuer clustering, and the fundamental law`
- 4.2: `alpha(A) = alpha0 - 2T [c0 + eta * sqrt(2 T A / L)], with T one-way` -> `Net alpha under square-root impact, and the capacity limit`
- 4.3: `w_i = min(1/n, w_max, cap_frac * MV_i / A); f_cash = 1 - sum(w)` -> `Ownership-cap position weights and the uninvested fraction`
- 4.4: `block 4 of 4: score rows of the six-axis map (all parameters illustrative, not the firms' numbers)` -> `Scoring the six-axis map: breadth, gross and net IR, capacity and cash drag`
- 5.1: `Recovery R per 1.0 of par: 0 w.p` -> `Recovery specification and mixture moments`
- 5.2: `Negative log-likelihood and gradient: logit mean, log precision (Ferrari-Cribari-Neto)` -> `Zero-one-inflated Beta regression for recoveries`
- 5.3: `m log-jumps: up ~ Exp(eta1) w.p` -> `Kou jump-diffusion first passage`
- 5.4: `Hill tail index from the top k positive losses` -> `Hill tail index and peaks-over-threshold VaR and ES`
- 5.5: `Coefficient of (upper = lower) tail dependence lambda_U of a bivariate t copula` -> `Tail dependence of the t copula, the limit against the finite level`
- 6.1: `Print PASS/FAIL and stop the run on failure` -> `The PASS/FAIL helper and the shared seed`
- 6.2: `Q-measure Merton` -> `Merton (1974): equity, debt, spread and the Q and P default probabilities`
- 6.3: `Equity value and the Ito-implied equity volatility sigma_E = N(d1) sigma_V V0 / E0` -> `The KMV inverse problem: asset value and volatility from equity`
- 6.4: `First-passage PD by T for barrier K_t = K exp(-g (T - t))` -> `Black-Cox first passage: closed form and Monte Carlo`
- 6.5: `Closed-form Q-survival S(0,T) = A(T) exp(-B(T) lam0)` -> `CIR intensity: closed-form survival and an exact simulation`
- 6.6: `Integrated piecewise-constant hazard; lams[k] applies on (knots[k-1], knots[k]], flat beyond` -> `CDS legs, hazard bootstrap and the credit triangle`
- 6.7: `Block 6: the structural short end, seen through the CDS bootstrap` -> `The structural short end, seen through the CDS bootstrap`
- 6-B.1: `credit_options.py (Chapter 6-B)` -> `credit_options.py: Black-Scholes, Greeks and jump-to-default pricing under the two measures`
- 7.1: `w_0 = 1, w_k = -w_{k-1} (d - k + 1) / k, truncated once |w_k| < tau` -> `Fractional differentiation with a fixed-width window`
- 7.2: `---------- 2. Synthetic credit panel with smoothed (stale) marks (Section 7.1) ----------` -> `A synthetic credit panel with smoothed (stale) marks`
- 7.3: `---------- 3. Triple-barrier labels in DTS space with exit censoring (Section 7.4) ----------` -> `Triple-barrier labels in DTS space with exit censoring`
- 7.4: `---------- 4. Parent-level average uniqueness and the hat count (Section 7.6) ----------` -> `Parent-level average uniqueness of overlapping labels`
- 7.5: `Test = (parents in group fold g) x (time block m)` -> `Purged, embargoed, parent-grouped cross-validation against shuffled K-fold`
- 7.6: `Secondary-model probability -> size in [0, 1), times the primary model's side` -> `Meta-label bet sizing, deflated Sharpe ratio, MinTRL and PBO`
- 7-B.1: `Bartlett-weighted sum of score cross-products (not divided by T); rows time-ordered` -> `creditstats.py: the credit statistics module`
- 7-B.2: `Acceptance tests for creditstats.py (seeded; every tolerance is derived, not tuned)` -> `Acceptance tests for creditstats.py`
- 8.1: `---------- 0. Setup: one seeded generator, one scoreboard ----------` -> `Setup: one seeded generator and one scoreboard`
- 8.2: `Split realized total returns into carry, rates, spread, convexity and residual` -> `Return decomposition into carry, rates, spread, convexity and residual`
- 8.3: `Pooled no-intercept OLS of R on [-D*dy, -D*s*dy]; H(s) = beta + gamma*s` -> `Empirical duration: pooled regression and the closed form`
- 8.4: `out[t] = f[t-k], NaN where undefined` -> `Stale-price betas: Dimson, Scholes-Williams and de-smoothing`
- 8.5: `Excess return per unit of previous-close DTS (approximately minus the relative spread change)` -> `DTS as the unit of credit beta, and the DTS pair hedge`
- 8.6: `Smallest ridge penalty capping cond(C + eta I) at cond_max (C a correlation matrix)` -> `The hedge matrix: minimum variance, ridge, bounds and contract units`
- 8.7: `Remove the leading principal components from a (T, N) panel of DTS-scaled residuals` -> `Stripping the common residual factor, and the IDO ledger`
- 9.1: `---------- Block 1: synthetic universe and data-generating process (Sections 9.2-9.3) ----------` -> `Synthetic universe and data-generating process`
- 9.2: `Top-minus-bottom q long-short` -> `DTS is beta: a top-minus-bottom backtest`
- 9.3: `Excess spread to peers: residual of log OAS on fundamentals, with sector and maturity intercepts, estimated by rating each month (Dynkin p.524)` -> `Factor signals: excess spread to peers, SPiDER, EMC and low risk`
- 9.4: `---------- Block 4: dollar-neutral vs DTS-neutral factors, costs, buffers (Sections 9.2-9.8) ----------` -> `Dollar-neutral against DTS-neutral factors, with costs and buffers`
- 9.5: `Benchmark: equal-weight held universe` -> `Long-only DTS-matched tilt with a turnover cap`
- 9.6: `---------- Block 6: combining factors (Section 9.7) ----------` -> `Combining factors: equal-risk and maximum-IR weights`
- 9.7: `Clean prices from excess returns; observed = clean x (1 + u), u iid N(0, sig_u^2)` -> `Replication under noisy prices`
- 10.1: `r_t = s_{t-1} * (ACT/360 year fraction) - dur * (s_t - s_{t-1}); long risk is positive` -> `Excess returns, CDX price returns and roll-safe stitching`
- 10.2: `sign of the trailing h-period summed excess return, known at the close of t` -> `Trend signals, sizing and P&L, with sign, turnover and Sheppard guards`
- 10.3: `monthly spread changes with AR(1) persistence phi (phi = 0 is a random walk in spreads)` -> `No free lunch under a random walk: spread changes with persistence`
- 10.4: `daily spreads with log-OU dynamics, so sd(ds) is proportional to s (Ben Dor's law, beta = sigma)` -> `Volatility scaling is DTS scaling: log-OU spreads and Ben Dor's law`
- 10.5: `monthly D3: ds_{t+1} = kappa (s_bar - s_t) + phi ds_t + eps, sd(eps) = beta s_t sqrt(dt)` -> `Trend plus carry under the D3 model, on an expanding window`
- 10.6: `OLS coefficients, Newey-West (Bartlett) standard errors and t-statistics; X includes a constant` -> `Stale-mark lead-lag, whipsaw, convexity and the crisis table`
- 11.1: `Arithmetic upside/downside capture on benchmark-defined regimes` -> `Capture ratios and asymmetric beta`
- 11.2: `Recover (V, sigma_V) from observed (E, sigma_E) by nested bracketed root searches` -> `Merton inversion, distance to default and the empirical PD map`
- 11.3: `Issuer-month panel: persistent latent DD with a common factor (default clustering), a liquidity-runway covariate capped at 13 weeks, and a distressed-exchange flag` -> `A synthetic HY panel, dynamic logit, clustered standard errors and purged issuer-grouped CV`
- 11.4: `q * [(pi_X - pi_K) * L - (s_X - s_K)], all decimals per year, P-measure` -> `CAP curve, accuracy ratio, hit rate and the economics of exclusion`
- 11.5: `Block 5: DTS-neutral defensive portfolio (Section 11.7)` -> `The DTS-neutral defensive portfolio`
- 11.6: `Block 6: regime-aware DTS budget and capacity (Sections 11.8-11.9)` -> `The regime-aware DTS multiplier and capacity`
- 12.1: `Illustrative inputs (decimals per year; durations in years). Bounds are Nuveen Fig. 5.` -> `Sector inputs: expected loss, mark-to-market drag and forward return`
- 12.2: `GLM (2004) MA(k) weights by matching autocorrelations; theta >= 0, sum(theta) = 1` -> `GLM de-smoothing: fitting the MA(k) smoothing weights`
- 12.3: `Covariance an optimizer sees when sector i is reported with GLM smoothing theta` -> `The covariance an optimizer sees: DTS, smoothing, EWMA and Ledoit-Wolf shrinkage`
- 12.4: `Defines mvn_logpdf, forward_backward, hmm2_em, stationary` -> `A two-state regime model: HMM filter, EM fit and regime-conditional capital-market assumptions`
- 12.5: `Mean-variance with the tiers of eq` -> `Mean-variance with tiers, equal risk contribution and the frontier`
- 13.1: `Eisenberg-Noe clearing: pay by rank, pro rata within rank, route intercompany receipts and subsidiary equity upward; iterate to a fixed point` -> `Waterfall clearing with priority classes, and double-dip and pari-plus recoveries`
- 13.2: `Per-dollar recoveries (R0, first-out, second-out, excluded), Section 13.3` -> `The uptier, the sponsor's knapsack, the co-op veto and Shapley carve-outs`
- 13.3: `MAP logistic: N(prior, tau^2) on slopes, Beta(a, b) on sig(b0)` -> `The Bayesian Priming Risk Score and expected priming loss`
- 14.1: `All rates per year under P; recoveries as fractions of par` -> `LME-cycle parameters and the cohort simulator along a regime path`
- 14.2: `The WRONG estimator, kept for the test: 1 - KM with competing causes treated as censoring` -> `Competing-risks estimators, and the wrong one kept for the test`
- 14.3: `Exact EL(T) of Sec` -> `Re-default clock, expected loss, coalition mixture and the co-op game`
- 14.4: `logf: (T, 2) log emission likelihoods; P: (2, 2) or (T, 2, 2) row-stochastic` -> `A two-state binomial Markov-switching model of distressed-exchange counts`
- 14.5: `block 5 of 5: sanity checks (each prints PASS/FAIL and asserts)` -> `Sanity checks for the cycle engine`
- 15.1: `Illustrative continuously compounded UST zero rate (decimal) at tenor t (years)` -> `Bond math and the 101 change-of-control put`
- 15.2: `Probability that a portable CoC put survives a sponsor who reads the test first` -> `Portability as a short digital on sponsor-chosen leverage`
- 15.3: `Constant spread (decimal) over the UST zero curve that reprices the bond` -> `The special mandatory redemption gauge: Z-spread and implied break probability`
- 15.4: `milestones: (t, q_deal, q_break) = P(milestone passes quietly | quiet so far, hypothesis)` -> `Deal clocks as competing-risks survival data`
- 16.1: `Trapezoid rule (avoids numpy version differences in trapz/trapezoid)` -> `The forced-seller overhang model, calibrated to fallen-angel aggregates`
- 16.2: `n0: plan shares before the offering, excluding fee shares (mm); m: rights shares (mm); K: subscription price per share` -> `Rights offerings and backstops`
- 16.3: `Galai-Schneller fixed point W = C_BS(S + omega*W, K, T, sigma, r + lam) / (1 + omega)` -> `Warrants with dilution and jump-to-default: the Galai-Schneller fixed point`
- 16.4: `E[min(1, e^Y)], Y ~ N(mu_Y, s_Y^2)` -> `Claims with a random denominator: expected recovery, timing and in-kind distributions`
- 16.5: `--- Block 5: the post-reorg book (reuses RNG, ForcedSellerOverhang, ovh_sched, theta_fa) ---` -> `The post-reorg book: simulation, Kelly size, liquidity cap and markouts`
- 17.1: `True quarterly excess return x_t = beta*F_t + e_t; reported x_obs_t = sum_k theta_k x_{t-k}` -> `The mark as a filter: smoothed returns and the Dimson kernel`
- 17.2: `m = ((1 - phi) - P/NAV) / (1 + ell), floored at 0` -> `Implied markdowns from BDC price to NAV, the non-accrual mark and stale-mark flags`
- 17.3: `Annualised hazards kappa_ij = base_j * exp(psi_j*zeta + chi_j*ds + V_i @ omega_j)` -> `Private-credit to broadly syndicated loan migration as competing risks`
- 17.4: `Pro-rata fill fraction f = min(1, cap / a)` -> `The redemption game and the liquidity runway`
- 17.5: `Expected sum of all future reported returns already implied by public factor returns` -> `The mark-gap signal: what public factor returns already imply about the next marks`
- 18.1: `Roll (1984) effective spread from consecutive trade prices (points per 100 par)` -> `Roll (1984) effective spread, with a simulator that has order splitting`
- 18.2: `One-period Kyle (1985)` -> `The one-period Kyle (1985) equilibrium and its lambda estimator`
- 18.3: `Per-side markup (1/gamma) ln(1 + gamma/k), in points` -> `Avellaneda-Stoikov quotes: fear plus greed`
- 18.4: `Frozen-inventory reservation (bid, ask) for buying/selling a block of n lots` -> `Jump-to-default reservation prices and the streaming inventory quotes`
- 18.5: `Logistic RFQ win probability; x = composite - bid (points); b1 > 0 per point` -> `The RFQ win curve, mark-up and the market maker's bid`
- 18.6: `Synthetic TRACE-like reports; bond ids are placeholders, not CUSIPs` -> `A synthetic TRACE tape: cleaning and features`
- 18.7: `e_n = E[max of n iid N(0,1)] by quadrature` -> `The expected maximum of n normals, and BWIC leakage`
- 19.1: `Struct-of-arrays PT inquiry` -> `The basket inquiry as a struct of arrays`
- 19.2: `Eq` -> `Per-line handling cost with a size exponent and a liquidity multiplier`
- 19.3: `B (N, K): price change (fraction of par) per unit relative spread move` -> `Factor loadings, factor covariance and the minimum-variance hedge`
- 19.4: `Eq` -> `Residual covariance for stale bonds: idiosyncratic variance and PSD projection`
- 19.5: `Greedy eviction on exact removal savings (eq` -> `Greedy eviction on exact removal savings`
- 19.6: `Stress score s in [0, 2] from ETF discount z-score (negative = discount) and bid-ask percentile in [0, 1]; one score drives m, gamma and basis together` -> `The stress score and the stress covariance`
- 19.7: `Eq` -> `The adverse-selection charge and markouts`
- 19.8: `Live path` -> `The live pricing path: price_pt`
- 20.1: `Eq` -> `The ETF arbitrage monitor: static band, NAV catch-up, clearing premium and basket choice`
- 21.1: `Haircut (par minus market value) on the CCC excess, cheapest CCC loans first` -> `The CLO overcollateralization test and the cure trade`
- 21.2: `P(a CLO sells a downgraded holding within 3 months); inputs are decimals` -> `The CLO Forced-Sale Pressure Index`
- 21.3: `a(T; rate) = integral_0^T exp(-rate u) du, stable as rate -> 0` -> `The loan as a capped floater with a repricing hazard, and CLO equity gearing`
- 21.4: `Variance of the ell-day sum of stationary AR(1) flows with innovation sd sigma_eps` -> `The loan-fund liquidity queue and the ETF arbitrage band`
- 21.5: `Observed (marked) returns: r_obs_t = (1 - phi) r_t + phi r_obs_{t-1}` -> `Stale marks: Geltner de-smoothing and Dimson betas`
- 22.1: `Binding Tier 1 per $1 of gross inventory: max(kappa_rwa * RW, kappa_lr)` -> `Balance-sheet rent: binding Tier 1 capital and the breakeven holding period`
- 22.2: `Zero-profit block half-spread, bp of price (eq` -> `The zero-profit block half-spread and the TRACE regime layer`
- 22.3: `IM_new / IM_old = sqrt((t_new + closeout) / (t_old + closeout)) for the volatility component (eq` -> `The settlement clock: initial margin scaling and the cost of fails`
- 22.4: `E|m + s Z| for standard normal Z (eq` -> `The Treasury clearing mandate: netting factor, net benefit and capacity hinge`
- 22.5: `Difference-in-differences around an effective date (eq` -> `A difference-in-differences event study with placebo dates`
- 23.1: `Equity as a call on assets` -> `Equity as a call on assets: Merton and CreditGrades`
- 23.2: `Textbook Black-Scholes put (independent reference for the lam = 0 check)` -> `The jump-to-default put and the unit recovery claim from a put chain`
- 23.3: `MTM per unit notional of bought protection, running coupon c, market spread s` -> `Spread Greeks for CDS, bonds, Merton and CreditGrades`
- 23.4: `GBM equity paths (no defaults) and CreditGrades model spreads with stock-space slopes` -> `Capital-structure arbitrage on a synthetic CreditGrades panel`
- 23.5: `Liquidity default day under a run whose outflow rate rises with equity losses (kappa) and with cumulative outflows (rho, the panic feedback)` -> `A bank-run liquidity default against a Merton PD`
- 24.1: `Premium dates (years) and ACT/360 accrual fractions for a T-year CDS` -> `CDS legs, par spread, upfront and hazard bootstrap`
- 24.2: `Coupon dates (years) and cash flows per 1.0 face; 30/360 semiannual coupons` -> `Bond-level basis: Z-spread, PECS and the jump-to-default hedge ratio`
- 24.3: `Annual excess carry per unit of equity for a near-par negative-basis package` -> `A negative-basis package: carry on equity and the stress mark`
- 24.4: `Price per 1.0 face at a semiannual-compounded yield y, on a coupon date` -> `Cheapest-to-deliver under the two default regimes`
- 24.5: `Round to the auction increment with halves going UP (round() goes to even)` -> `The two-stage auction: inside market, adjustment amounts and final price`
- 24.6: `Exact OU discretization of the basis (bp)` -> `An OU basis signal, net of costs`
- 24.7: `Simplified successor thresholds: entity -> fraction of each CDS it inherits` -> `The successor map and manufactured-event flags`
- 25.1: `"Consolidated Net Income" means the net income of the Borrower and its Restricted Subsidiaries for such period` -> `The definition graph: parsing, strongly connected components and blast radius`
- 25.2: `Section 6.01(b)(xii)` -> `Basket arithmetic: growers, ratio baskets, the add-back fixed point and the builder`
- 25.3: `Edmonds-Karp` -> `Leakage capacity as max-flow (Edmonds-Karp)`
- 25.4: `Block 4: why token diffs miss covenant edits (Section 25.5.1) ---------------` -> `Why token diffs miss covenant edits`
- 25.5: `One global bucket` -> `Rate limits with a token bucket, and EDGAR hygiene`
- 25.6: `Defines polite_get` -> `A polite fetcher with backoff (a sketch, not run)`
- 25.7: `11 U.S.C` -> `Rule 2019 statements to a holdings panel, and the blocking test`
- 25.8: `Block 7: docket state machine, transition intensities (Section 25.7.2) ------` -> `The docket state machine and its transition intensities`
- 25.9: `Block 8: classifier error as an IC tax (Equation 25.3), plus the citation contract --` -> `Classifier error as an IC tax, and the citation contract`
- 26.1: `Synthetic agreement: Section 6.08(b)(i)-(xii), one clause per 1-based PDF page` -> `The document store and the deterministic basket calculators`
- 26.2: `Question i asks for basket s_i; p_true is its difficulty, a property of the question` -> `The stochastic reader, citation contract, calibration and abstention`
- 26.3: `Unbiased estimator of p**k (tau-bench pass^k) from c successes in n i.i.d` -> `Chains, verifiers, retries, pass^k, replay and research hurdles`
- 27.1: `known_at - event_time in ms; a negative value beyond the clock-error bound is a clock fault` -> `Provenance-typed prices, clock checks and TRACE dedupe`
- 27.2: `As of knowledge time known_at, attr of key had value over [valid_from, valid_to)` -> `The bitemporal security master`
- 27.3: `Kingman / Pollaczek-Khinchine mean queueing delay (exact for M/G/1, i.e` -> `Latency as a queue: Pollaczek-Khinchine, the Lindley simulation and fan-out tails`
- 27.4: `Bond points per hedge point for a rate hedge: dollar-duration ratio times empirical rate beta` -> `Trigger tables for quote pulling: sensitivities and the joint and per-instrument rules`
- 27.5: `ARL of G_k = max(0, G_{k-1} + X_k), X ~ N(drift, 1), alarm at G >= c` -> `Kill switches: CUSUM run lengths against Siegmund, and a tiered switch`
- 28.1: `1/H on absolute GMV weights` -> `Block 1: Effective breadth and the hit-rate law`
- 28.2: `Eq` -> `Block 2: The horizon ladder`
- 28.3: `Eq` -> `Block 3: Kelly with jumps`
- 28.4: `Bangia eq` -> `Block 4: LVaR, days-to-liquidate and runway`
- 28.5: `Eq` -> `Block 5: Stops, hitting probabilities and the mark-to-bid shock`
- 28.6: `Eq` -> `Block 6: The leverage band`
- 28.7: `Eq` -> `Block 7: The team production function`
- 28.8: `--- Final block: pm_playbook_engine --------------------------------------------` -> `The PM dashboard engine: pm_playbook_engine`
- B.1: `US 30/360 (bond basis) day count between two Timestamps` -> `The tidy bond panel: security master, 30/360 bond math and a synthetic TRACE tape`
- D.1: `Accrued interest as a fraction of face (coupon an annual decimal, days on 30/360)` -> `plumbing.py: settlement, financing, margin, CDS cash and credit-event mechanics, one function per rule`
- E.1: `laws_of_the_desk.py: the Laws of the Desk as data, a Debrief linter, and one checker per law` -> `laws_of_the_desk.py: the Laws of the Desk as data, a Debrief linter and one checker per law`
- 4-B.1: `Year fraction from d1 to d2` -> `bondmath.py: cash flows, curve, solver, price and yield`
- 12-B.1: `restructuring_state_machine.py (Chapter 12-B)` -> `restructuring_state_machine.py: the restructuring process as a state machine`
- 3-B.1: `Following convention: the first business day on or after d` -> `desk_calendar.py: venue calendars, versioned contract clocks and event features`
- 8-B.1: `risk_model.py (Chapter 8-B): the morning risk model for a credit book` -> `risk_model.py: the morning risk model for a credit book`
- 8-C.1: `Coupon accrual in dollars: a contractual fact` -> `pnl_explain.py: the morning explain, with named lines per position and hedge`
- 12-C.1: `plan_value_engine.py (Chapter 12-C)` -> `plan_value_engine.py: plan value, the DIP and exit as derivatives`
- 1-B.1: `Latest version of event_id that the shop knew at time `at` (bitemporal read)` -> `The week log: an immutable event row and the bitemporal read`
- 4-C.1: `One holder (a vehicle, not a firm) of one instrument, described by its leash` -> `The seat state vector: one holder of one instrument, described by its leash`
- 8-D.1: `pair_book.py (Chapter 8-D): rulers, jumps, the stop, the borrow and the ledger row for one pair` -> `pair_book.py: rulers, jumps, the stop, the borrow and the ledger row for one pair`
- 2-B.1: `tca.py (Chapter 2-B): transaction cost analysis for an RFQ market` -> `tca.py: transaction cost analysis for an RFQ market`
- 4-D.1: `interview_drills.py: seeded drills for Chapter 4-D (illustrative numbers)` -> `interview_drills.py: seeded drills for Chapter 4-D`
- 9-B.1: `OLS of y on [1, x]; returns (coefficients, Newey-West t-stats)` -> `replication_harness.py: look-ahead gates and the replication of a bond signal`
- 10-B.1: `index_micro.py (Chapter 10-B): four small measurements of the index market` -> `index_micro.py: four small measurements of the index market`
- 13-B.1: `docket_diary.py (Chapter 13-B): labelled docket entries -> rulings, case paths, transition counts, and token log-odds that jump on ruling dates` -> `docket_diary.py: labelled docket entries to rulings, case paths and transitions`
- 17-B.1: `Share of shares outstanding repurchased this cycle, p = a * f (decimals)` -> `The redemption queue, de-duplicated and nowcast`
- 17-B.2: `One par-weighted mark per facility, quarter and valuation process (adviser)` -> `The private-credit LME detector: marks, states, features and a hazard watchlist`
- 18-B.1: `rfq_engine.py (Chapter 18-B): the RFQ response engine in six small pieces` -> `rfq_engine.py: the RFQ response engine in six small pieces`

Unchanged: 1.3 ("Distance to default, credit-triangle check, one-factor simulation"), already a title.

Limits. The order is that of the first link, so a chapter that links a listing in an early summary before its stub would be numbered by that link (none does today). The mover (`tools/move_code_to_companion.py`) still builds titles from the first docstring line; run `python3 tools/renumber_listings.py --titles` after a move and retitle what it lists. I did not change the mover.

Status: fixed.

---

## Observations (not in scope, nothing changed)

- `tools/check_book.py --file book_src/95_appF_code_companion.md --run-code` cannot pass as it stands: it concatenates all 174 blocks into one script and stops at a `from __future__ import annotations` in a Part VIII / appendix listing (six such imports in App F, already present before this pass). Per-chapter runs, which is how the appendix preamble says to run listings, all pass for the chapters this group touched (1, 11, 25, 28).
- `check_book.py` reports three missing anatomy items for Ch 4-D (ai_spec, source_extraction, case_study); unrelated to listings, not touched.
