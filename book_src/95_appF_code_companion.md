# Appendix F: The Code Companion

Every reference implementation in the book lives here, chapter by chapter. The chapters explain what each listing does, why it is built that way, and when to use it; this appendix holds the code itself so the story is never interrupted by a wall of syntax. Listings within a chapter build on each other: run them in order in one interpreter (`python3 tools/check_book.py --file book_src/95_appF_code_companion.md --run-code` runs them all).

## F.1: Chapter 1: The Anthology of the Desk & The Modern Quant Credit Landscape {#code-1}

Listings from `01_ch01_anthology_and_landscape.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 1.1: The bid equation: inventory term, informed-flow Bayes and the jump penalty {#code-1-1}

```python
import numpy as np
import pandas as pd

RNG_SEED = 20261017


def reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c=0.0):
    """Dealer bid for buying dq ($mm par) from a client: eq. (1.2), measure P.

    S, J, c, sigma_ido in price points per 100 par (sigma_ido per sqrt(year), post-hedge);
    q, dq in $mm par (long positive; dq > 0 means the client sells to us);
    gamma in 1/($mm * pt) of P&L; h_years in years.
    """
    if dq <= 0:
        raise ValueError("dq must be > 0: the client sells dq to the desk")
    if not 0.0 <= pi <= 1.0:
        raise ValueError("pi must lie in [0, 1]")
    if h_years <= 0:
        raise ValueError("h_years must be > 0")
    if min(gamma, sigma_ido, J, c) < 0:
        raise ValueError("gamma, sigma_ido, J and c must be non-negative")
    m = S - pi * J                                   # Glosten-Milgrom posterior mean
    inventory = 0.5 * gamma * sigma_ido**2 * h_years * (2.0 * q + dq)
    return m - inventory - c


def posterior_informed(mu, log_lr):
    """Bayes in logit form: logit(pi) = logit(mu) + log(a_I / a_U)."""
    if not 0.0 < mu < 1.0:
        raise ValueError("prior mu must lie strictly inside (0, 1)")
    z = np.log(mu / (1.0 - mu)) + log_lr
    return 1.0 / (1.0 + np.exp(-z))


def glosten_milgrom_markout(pi, J, sigma_ido=8.0, h_years=5 / 252, n=200_000, seed=7):
    """Simulated markout (points) of buying at mid from a seller who is informed w.p. pi."""
    rng = np.random.default_rng(seed)
    informed = rng.random(n) < pi
    noise = sigma_ido * np.sqrt(h_years) * rng.standard_normal(n)
    markout = -J * informed + noise                  # S_{t+h} - S_t from the buyer's side
    return markout.mean(), markout.std(ddof=1) / np.sqrt(n)


def jump_penalty_ratio(gamma, q, ell):
    """Exact CARA jump penalty / quadratic approximation (common factor lambda*h cancels)."""
    x = gamma * q * ell
    exact = (np.expm1(x) - x) / gamma
    quadratic = 0.5 * gamma * (q * ell) ** 2
    return exact / quadratic


# --- the cold open, in numbers (illustrative) ---
base = dict(S=91.97, q=5.0, dq=15.0, gamma=0.02, sigma_ido=8.0, h_years=5 / 252, c=0.25)
engine_bid = reservation_bid(pi=0.0, J=13.0, **base)
theo_bid = reservation_bid(pi=0.6, J=13.0, **base)
assert abs(engine_bid - 91.40) < 0.01, engine_bid
assert abs(theo_bid - 83.60) < 0.01, theo_bid

# --- comparative statics are the unit tests ---
assert reservation_bid(**{**base, "q": 6.0}, pi=0.1, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**base, pi=0.2, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**{**base, "dq": 20.0}, pi=0.1, J=13.0) < reservation_bid(**base, pi=0.1, J=13.0)
assert reservation_bid(**base, pi=0.1, J=13.0) <= base["S"]          # q >= 0 never bids above mid
zero = reservation_bid(S=91.97, q=0.0, dq=15.0, gamma=0.0, sigma_ido=8.0, h_years=0.02, pi=0.0, J=13.0, c=0.25)
assert abs(zero - (91.97 - 0.25)) < 1e-12
short_desk = reservation_bid(**{**base, "q": -20.0, "c": 0.0}, pi=0.0, J=0.0)
assert short_desk > base["S"]                                        # a short desk pays up to cover

# --- Bayes and the hand history ---
assert abs(posterior_informed(0.05, 0.0) - 0.05) < 1e-12              # uninformative features
assert posterior_informed(0.05, np.log(30.0)) > 0.6                   # 'was on the call' LR of 30
mean_mo, se_mo = glosten_milgrom_markout(pi=0.3, J=13.0)
assert abs(mean_mo - (-0.3 * 13.0)) < 3 * se_mo, (mean_mo, se_mo)

# --- Kaz's Gaussian regret ---
r_small = jump_penalty_ratio(0.02, 0.01, 30.0)
r_mid = jump_penalty_ratio(0.02, 1.0, 30.0)
r_big = jump_penalty_ratio(0.02, 5.0, 30.0)
assert abs(r_small - 1.0) < 1e-2 and 1.0 < r_mid < r_big
print(f"engine bid {engine_bid:.2f} | toxicity-aware bid {theo_bid:.2f} | "
      f"jump under-charge x{r_mid:.2f} at 1mm, x{r_big:.2f} at 5mm")
```


### Listing 1.2: Duration Times Spread, DTS volatility and the liquidity cost score {#code-1-2}

```python
def dts(D_spr, s_bp):
    """Duration Times Spread in bp*years: D_spr in years, s_bp in basis points."""
    return D_spr * s_bp


def dts_vol(D_spr, s_bp, sigma_rel):
    """Eq. (1.3): excess-return volatility in bp per period of sigma_rel (unitless)."""
    return dts(D_spr, s_bp) * sigma_rel


def lcs(bid, ask, oasd=None, price_quoted=False):
    """Ben Dor liquidity cost score in % of price.

    Spread-quoted: bid/ask are spreads in bp (bid spread > ask spread), LCS = OASD * (bid - ask) / 100.
    Price-quoted: bid/ask are prices, LCS = 100 * (ask - bid) / bid.
    """
    if price_quoted:
        return 100.0 * (ask - bid) / bid
    if oasd is None:
        raise ValueError("spread-quoted LCS needs OASD")
    return oasd * (bid - ask) / 100.0


# BBB at 120bp, 7y versus single-B at 450bp, 4y (illustrative)
v_bbb, v_b = dts_vol(7.0, 120.0, 0.08), dts_vol(4.0, 450.0, 0.08)
assert v_b > 2.0 * v_bbb                       # DTS: the short single-B is the riskier bond

# Monte Carlo check: lognormal relative spread moves reproduce DTS * sigma_rel within 2%
rng = np.random.default_rng(RNG_SEED)
for sigma_rel in (0.05, 0.10):
    z = rng.standard_normal(200_000)
    ds = 450.0 * (np.exp(sigma_rel * z - 0.5 * sigma_rel**2) - 1.0)   # bp
    r_xs = -4.0 * ds                                                    # bp of excess return
    assert abs(r_xs.std() / dts_vol(4.0, 450.0, sigma_rel) - 1.0) < 0.02

# Ben Dor p.61 issuer limit: MV% x spread(%) x duration <= 5
assert abs(5.0 / (1.00 * 5.0) - 1.0) < 1e-12 and abs(5.0 / (1.50 * 10.0) - 0.3333) < 1e-3
assert abs(lcs(bid=455.0, ask=445.0, oasd=4.0) - 0.40) < 1e-12      # 10bp wide x 4y = 0.40%
assert abs(lcs(bid=62.0, ask=64.0, price_quoted=True) - 100 * 2 / 62) < 1e-12
```


### Listing 1.3: Distance to default, credit-triangle check, one-factor simulation {#code-1-3}

```python
from scipy.integrate import trapezoid
from scipy.stats import norm


def distance_to_default(V, F, mu_V, sigma_V, T=1.0):
    """Eq. (1.4): physical distance to default (unitless)."""
    return (np.log(V / F) + (mu_V - 0.5 * sigma_V**2) * T) / (sigma_V * np.sqrt(T))


def credit_triangle_check(lam=0.03, R=0.40, r=0.04, T=5.0, n=200_001):
    """Numerically integrate both CDS legs (measure Q) and return the par spread."""
    t = np.linspace(0.0, T, n)
    disc_surv = np.exp(-(r + lam) * t)
    prem_annuity = trapezoid(disc_surv, t)
    protection = (1.0 - R) * trapezoid(lam * disc_surv, t)
    return protection / prem_annuity


dd = distance_to_default(V=150.0, F=100.0, mu_V=0.06, sigma_V=0.10)   # illustrative IG-like firm
assert dd > 4.0 and norm.cdf(-dd) < 1e-4                               # Gaussian: 'immortal'
assert abs(credit_triangle_check() - 0.03 * 0.60) < 1e-10              # s = lambda (1 - R)

# One-factor threshold model: Monte Carlo default rate matches p; tails fatten with rho
rng = np.random.default_rng(RNG_SEED + 1)
p, rho, n_sims, n_firms = 0.02, 0.20, 20_000, 500
Y = rng.standard_normal(n_sims)
p_cond = norm.cdf((norm.ppf(p) - np.sqrt(rho) * Y) / np.sqrt(1.0 - rho))
loss_frac = rng.binomial(n_firms, p_cond) / n_firms
assert abs(loss_frac.mean() - p) < 4 * loss_frac.std() / np.sqrt(n_sims)
assert np.quantile(loss_frac, 0.99) > 5 * p                            # herds, not coin flips
```


### Listing 1.4: The forced-seller flow graph and the price-pressure path {#code-1-4}

```python
class ForcedSellerGraph:
    """Holder x trigger forced-supply engine: eqs. (1.6)-(1.7). Units: $bn par, days, points."""

    def __init__(self, holdings, rules, capacity):
        self.H = holdings.astype(float)
        if (self.H.values < 0).any():
            raise ValueError("holdings must be non-negative")
        for holder, by_trigger in rules.items():
            for trig, (frac, window) in by_trigger.items():
                if not 0.0 <= frac <= 1.0:
                    raise ValueError(f"{holder}/{trig}: fraction must lie in [0, 1]")
                if window <= 0:
                    raise ValueError(f"{holder}/{trig}: window_days must be > 0")
        for trig, cap in capacity.items():
            if (cap.values < 0).any():
                raise ValueError(f"{trig}: capacity must be non-negative")
        self.rules, self.capacity = rules, capacity

    def forced_supply(self, trigger, segment):
        """Q^sell_k(tau) by holder, eq. (1.6)."""
        frac = {h: self.rules.get(h, {}).get(trigger, (0.0, 1))[0] for h in self.H.columns}
        return self.H.loc[segment] * pd.Series(frac)

    def run(self, trigger, segment, stress=False):
        sells = self.forced_supply(trigger, segment)
        assert (sells <= self.H.loc[segment] + 1e-12).all()             # (b)
        Q = float(sells.sum())
        cap = self.capacity.get(trigger)
        caps = cap.loc[segment].astype(float) if cap is not None else pd.Series(dtype=float)
        if stress:
            caps = caps * 0.0                                            # March 2020 toggle
        total_cap = float(caps.sum())
        absorbed = min(Q, total_cap)
        buys = caps * (absorbed / total_cap) if total_cap > 0 else caps * 0.0
        residual = Q - float(buys.sum())
        edges = []
        if Q > 0:
            for s, sz in sells[sells > 0].items():
                edges += [(s, b, sz * bz / Q) for b, bz in buys[buys > 0].items()]
                if residual > 0:
                    edges.append((s, "dealer_residual", sz * residual / Q))
        assert abs(Q - (buys.sum() + residual)) < 1e-9                   # (a) conservation
        assert abs(sum(e[2] for e in edges) - Q) < 1e-9
        return {"sells": sells, "buys": buys, "dealer_residual": residual, "edges": edges}

    @staticmethod
    def price_path(imbalance, adv, kappa, theta, days, p_star=100.0):
        """Eq. (1.7): temporary price pressure decaying at rate theta per day."""
        if adv <= 0 or theta <= 0:
            raise ValueError("adv and theta must be > 0")
        t = np.arange(days + 1, dtype=float)
        return p_star - kappa * max(imbalance, 0.0) / adv * np.exp(-theta * t)


# --- a Ford-sized fallen angel, March 2020 style (all numbers illustrative) ---
seg = "BBB- auto issuer, $36bn"
holdings = pd.DataFrame({"insurers": [12.0], "ig_active_funds": [8.0], "ig_index_funds_etfs": [5.0],
                         "banks_foreign_other": [9.0], "hy_funds": [2.0]}, index=[seg])
rules = {"insurers": {"IG_to_HY": (0.25, 90)}, "ig_active_funds": {"IG_to_HY": (0.50, 30)},
         "ig_index_funds_etfs": {"IG_to_HY": (1.00, 5)}, "banks_foreign_other": {"IG_to_HY": (0.10, 60)}}
capacity = {"IG_to_HY": pd.DataFrame({"hy_index_inclusion": [3.0], "fallen_angel_programs": [1.5],
                                      "crossover_distressed": [2.0]}, index=[seg])}
g = ForcedSellerGraph(holdings, rules, capacity)
base_run, stress_run = g.run("IG_to_HY", seg), g.run("IG_to_HY", seg, stress=True)
Q = float(g.forced_supply("IG_to_HY", seg).sum())
assert abs(Q - 12.9) < 1e-12 and abs(base_run["dealer_residual"] - 6.4) < 1e-9
assert abs(stress_run["dealer_residual"] - Q) < 1e-12                    # (d)

theta = 1 / 20                                                           # ~14-day half-life
path = ForcedSellerGraph.price_path(base_run["dealer_residual"], adv=0.5, kappa=0.4, theta=theta,
                                    days=int(10 / theta))
assert abs(path[-1] - 100.0) < 0.01                                      # (c) reversal
drop, recovered_60d = 100.0 - path[0], path[60] - path[0]
assert abs(recovered_60d - drop * (1 - np.exp(-theta * 60))) < 1e-9     # absorber's expected gain
assert reservation_bid(**base, pi=0.5, J=13.0) < reservation_bid(**base, pi=0.4, J=13.0)
print(f"forced supply {Q:.1f}bn | dealer residual {base_run['dealer_residual']:.1f}bn "
      f"(stress {stress_run['dealer_residual']:.1f}bn) | drop {drop:.2f}pt | 60d reversal {recovered_60d:.2f}pt")
```


## F.2: Chapter 2: The Revolutions in Credit Trading {#code-2}

Listings from `02_ch02_revolutions_in_credit_trading.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 2.1: Logistic fit of an adoption S-curve: rate, midpoint and odds-doubling time {#code-2-1}

```python
# ch02_electronification_trend.py -- block 1: the adoption S-curve (measure: P)
import warnings
import numpy as np
import pandas as pd
from scipy.optimize import OptimizeWarning, curve_fit

SEED = 7
CLIP = 1e-4
T_REF = 2015.0      # centre time so the optimiser is well conditioned
CHECKS = []         # rows of the sanity table: (check, value, passed)


def check(name, value, passed):
    CHECKS.append((name, float(value), bool(passed)))
    assert passed, f"sanity check failed: {name} ({value})"


OBS = pd.DataFrame(
    [(2015.0, "US_IG", 0.20, "Greenwich, McPartland 2025-06-10"),
     (2024.0, "US_IG", 0.48, "Greenwich FY2024, Jan 2025"),
     (2025.0, "US_IG", 0.48, "Greenwich, McPartland 2025-06-10"),
     (2015.0, "US_HY", 0.06, "Greenwich, McPartland 2025-06-10"),
     (2024.0, "US_HY", 0.33, "Greenwich FY2024, Jan 2025"),
     (2025.0, "US_HY", 0.32, "Greenwich, McPartland 2025-06-10")],
    columns=["year", "segment", "share", "source"])


def logistic(t, K, r, t0):
    return K / (1.0 + np.exp(-r * (t - t0)))


def _logit_ols(t, e, K):
    z = np.log(e / (K - e))                  # generalised logit; caller guarantees e < K
    r, b = np.polyfit(t, z, 1)
    return float(r), float(-b / r)


def fit_adoption(years, shares, K=None):
    """K=None: ceiling 1. K=float: fixed ceiling. K='fit': 3-parameter fit (a diagnostic)."""
    years = np.asarray(years, dtype=float)
    raw = np.asarray(shares, dtype=float)
    if years.size < 2:
        return None                           # one point identifies nothing
    if np.any((raw <= 0.0) | (raw >= 1.0)):
        warnings.warn("shares at 0 or 1 were clipped")
    e = np.clip(raw, CLIP, 1.0 - CLIP)
    t = years - T_REF
    fit_K = isinstance(K, str) and K == "fit"
    K_val = 1.0 if (K is None or fit_K) else float(K)
    if not (e.max() < K_val <= 1.0):
        raise ValueError("ceiling K must exceed every observed share and be <= 1")
    r, t0 = _logit_ols(t, e, K_val)
    if r <= 0.0:
        raise ValueError("series is not increasing: nothing to fit")
    resid = np.log(e / (K_val - e)) - r * (t - t0)
    note = ""
    if fit_K:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", OptimizeWarning)
                p, _ = curve_fit(logistic, t, e, p0=(0.9, min(r, 1.9), t0),
                                 bounds=([0.05, 1e-6, -50.0], [1.0, 2.0, 100.0]),
                                 maxfev=10000)
            K_val, r, t0 = (float(v) for v in p)
            if K_val - e.max() < 0.02 or r > 1.9:
                note = "K not identified: ceiling ~ last observation or rate at bound"
        except (RuntimeError, ValueError):
            note = "curve_fit failed; kept the logit-OLS fit with K = 1"
    years_out = np.arange(2026, 2031)
    proj = pd.DataFrame({"year": years_out,
                         "share_hat": logistic(years_out - T_REF, K_val, r, t0),
                         "K": K_val})
    return {"K": K_val, "r": r, "t0": t0 + T_REF, "odds_doubling_years": np.log(2.0) / r,
            "logit_resid": resid, "projection": proj, "note": note}


def two_points(seg):
    return OBS[(OBS.segment == seg) & OBS.year.isin([2015.0, 2025.0])]


ig2, hy2 = two_points("US_IG"), two_points("US_HY")
fit_ig = fit_adoption(ig2.year, ig2.share)
fit_hy = fit_adoption(hy2.year, hy2.share)


def zlogit(e, K=1.0):
    return np.log(e / (K - e))


r_closed = (zlogit(0.48) - zlogit(0.20)) / (2025.0 - 2015.0)
check("(a) OLS slope equals two-point slope", fit_ig["r"], abs(fit_ig["r"] - r_closed) < 1e-12)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", OptimizeWarning)
    p2, _ = curve_fit(lambda t, r, t0: logistic(t, 1.0, r, t0),
                      ig2.year.to_numpy() - T_REF, ig2.share.to_numpy(),
                      p0=(0.5 * fit_ig["r"], fit_ig["t0"] - T_REF + 2.0), maxfev=10000)
gap_b = max(abs(p2[0] - fit_ig["r"]), abs(p2[1] + T_REF - fit_ig["t0"]))
check("(b) curve_fit at K=1 reproduces logit-OLS", gap_b, gap_b < 1e-6)

for name, f in (("IG", fit_ig), ("HY", fit_hy)):
    s = f["projection"]["share_hat"].to_numpy()
    check(f"(c) {name} projection monotone and inside (0, K)", s[-1],
          np.all(np.diff(s) > 0.0) and np.all((s > 0.0) & (s < f["K"])))
check("IG 2030 at K=1 is about 64%", fit_ig["projection"].share_hat.iloc[-1],
      abs(fit_ig["projection"].share_hat.iloc[-1] - 0.64) < 0.01)
check("HY odds double in about 3.5 years", fit_hy["odds_doubling_years"],
      abs(fit_hy["odds_doubling_years"] - 3.47) < 0.05)
fit_ig80 = fit_adoption(ig2.year, ig2.share, K=0.80)
check("a lower ceiling implies a faster rate", fit_ig80["r"], fit_ig80["r"] > fit_ig["r"])

robo_2030 = 0.33 * (0.33 / 0.06) ** (6.0 / 9.0)        # what ROBO built from the vague spec
check("ROBO's constant-growth projection leaves [0, 1]", robo_2030, robo_2030 > 1.0)

fit_ig3 = fit_adoption(OBS[OBS.segment == "US_IG"].year, OBS[OBS.segment == "US_IG"].share, K="fit")
check("3-parameter K stays inside its bounds", fit_ig3["K"], 0.05 <= fit_ig3["K"] <= 1.0)
print("3-parameter IG fit: K =", round(fit_ig3["K"], 3), "|", fit_ig3["note"] or "no warning")
print(fit_ig["projection"].round(3).to_string(index=False))
```


### Listing 2.2: The RFQ as an auction: best of n quotes with a common anchor {#code-2-2}

```python
# block 2: the RFQ as an auction, with an anchoring share phi
def rfq_best_of_n(theta, n, phi=0.0, n_sims=200_000, seed=SEED):
    """Quote distance = common Exp(mean phi*theta) + i.i.d. Exp(mean (1-phi)*theta)."""
    if theta <= 0.0 or n < 2 or not 0.0 <= phi < 1.0:
        raise ValueError("need theta > 0, n >= 2 and 0 <= phi < 1")
    rng = np.random.default_rng(seed)
    common = rng.exponential(phi * theta, size=(n_sims, 1)) if phi > 0.0 else 0.0
    quotes = common + rng.exponential((1.0 - phi) * theta, size=(n_sims, n))
    q = np.partition(quotes, 1, axis=1)       # q[:, 0] = best, q[:, 1] = cover
    return {"mc_best": float(q[:, 0].mean()),
            "mc_gap": float((q[:, 1] - q[:, 0]).mean()),
            "cf_best": phi * theta + (1.0 - phi) * theta / n,
            "cf_gap": (1.0 - phi) * theta / (n - 1),
            "n_eff": n / (1.0 + (n - 1) * phi)}


for n in (3, 5, 8, 12):
    res = rfq_best_of_n(1.0, n)
    err = max(abs(res["mc_best"] / res["cf_best"] - 1.0),
              abs(res["mc_gap"] / res["cf_gap"] - 1.0))
    check(f"(d) best-of-{n} and cover gap vs closed form", err, err < 0.02)

n_eff_11 = rfq_best_of_n(1.0, 11, phi=0.45, n_sims=10)["n_eff"]
check("n_eff(n=11, phi=0.45) = 2", n_eff_11, abs(n_eff_11 - 2.0) < 1e-12)
anchored, indep = rfq_best_of_n(1.0, 11, phi=0.5), rfq_best_of_n(1.0, 2)
check("11 anchored dealers quote worse than 2 independent", anchored["mc_best"],
      anchored["mc_best"] > indep["mc_best"])
```


### Listing 2.3: Bond price, spread duration, liquidity cost conventions and the Man cost decomposition {#code-2-3}

```python
# block 3: LCS conventions and the Man cost decomposition (units!)
def bond_price(coupon, maturity, y, freq=2):
    """Price per 100 par on a coupon date; y is the annual yield, decimal, compounded at freq."""
    n = int(round(maturity * freq))
    t = np.arange(1, n + 1) / freq
    cf = np.full(n, 100.0 * coupon / freq)
    cf[-1] += 100.0
    return float(np.sum(cf * (1.0 + y / freq) ** (-freq * t)))


def spread_duration(coupon, maturity, y_tsy, s, h=1e-5):
    p0 = bond_price(coupon, maturity, y_tsy + s)
    up = bond_price(coupon, maturity, y_tsy + s + h)
    dn = bond_price(coupon, maturity, y_tsy + s - h)
    return -(up - dn) / (2.0 * h * p0)


def lcs_spread_quoted(D_spr, s_bid, s_ask):
    """Round-trip LCS as a fraction of price; spreads in decimal, never bp."""
    if s_bid < s_ask:
        raise ValueError("the bid spread must be >= the ask spread")
    return D_spr * (s_bid - s_ask)


def lcs_price_quoted(P_bid, P_ask):
    if not P_ask >= P_bid > 0.0:
        raise ValueError("need P_ask >= P_bid > 0")
    return (P_ask - P_bid) / P_bid


def man_tc_bp(inside_spread_bp, slippage_bp, calibration_bp):
    """One-way cost in bp of price; calibration may be negative (prints better than runs)."""
    if inside_spread_bp < 0.0 or slippage_bp < 0.0:
        raise ValueError("inside spread and slippage are nonnegative")
    return inside_spread_bp + slippage_bp + calibration_bp


cpn, mat, y_tsy, s_mid = 0.05, 5.5, 0.040, 0.012          # illustrative BBB
D = spread_duration(cpn, mat, y_tsy, s_mid)
s_bid, s_ask = s_mid + 0.0005, s_mid - 0.0005               # 10 bp bid-offer in spread
lcs_s = lcs_spread_quoted(D, s_bid, s_ask)
lcs_p = lcs_price_quoted(bond_price(cpn, mat, y_tsy + s_bid), bond_price(cpn, mat, y_tsy + s_ask))
check("(e) LCS conventions agree within 5%", lcs_p / lcs_s, abs(lcs_p / lcs_s - 1.0) < 0.05)
one_way_bp = 1e4 * lcs_s / 2.0
check("one-way cost = LCS / 2, in a sane bp range", one_way_bp, 10.0 < one_way_bp < 40.0)
check("Man TC adds like units", man_tc_bp(6.0, 2.5, -1.0), abs(man_tc_bp(6.0, 2.5, -1.0) - 7.5) < 1e-12)
```


### Listing 2.4: Optimal turnover and the cheapest-protocol router {#code-2-4}

```python
# block 4: the data-exhaust theorem and the protocol router
def optimal_turnover(k, c):
    """alpha_net(TO) = k*sqrt(TO) - c*TO; c is one-way cost as a fraction of notional."""
    if k <= 0.0 or c <= 0.0:
        raise ValueError("k and c must be positive")
    return k ** 2 / (4.0 * c ** 2), k ** 2 / (4.0 * c)


k_sig = 0.0048                                               # illustrative signal strength
to_old, a_old = optimal_turnover(k_sig, 12e-4)
to_new, a_new = optimal_turnover(k_sig, 7.5e-4)
grid = np.linspace(0.01, 30.0, 300_001)
to_grid = grid[np.argmax(k_sig * np.sqrt(grid) - 7.5e-4 * grid)]
check("closed-form TO* matches grid search", to_grid, abs(to_grid / to_new - 1.0) < 1e-3)
check("cost 12 -> 7.5 bp: TO* rises 2.56x", to_new / to_old, abs(to_new / to_old - 2.56) < 1e-9)
check("cost 12 -> 7.5 bp: net alpha rises 1.6x", a_new / a_old, abs(a_new / a_old - 1.6) < 1e-9)


def route(lines, kappa_bp):
    """One-shot router: J = pi*c + (1 - pi)*kappa, minimised per line."""
    df = lines.copy()
    if not df["pi_fill"].between(0.0, 1.0).all():
        raise ValueError("fill probabilities must lie in [0, 1]")
    df["J_bp"] = df["pi_fill"] * df["c_fill_bp"] + (1.0 - df["pi_fill"]) * kappa_bp
    best = df.loc[df.groupby("line_id")["J_bp"].idxmin()].reset_index(drop=True)
    return best, df


def try_a2a_first(pi_a, c_a, chi_a, J_r):
    """Sequential rule: odds of an A2A fill must beat leakage / saving."""
    if J_r <= c_a:
        return False                          # nothing to save, so leakage buys nothing
    if pi_a >= 1.0:
        return True
    return pi_a / (1.0 - pi_a) > chi_a / (J_r - c_a)


lines = pd.DataFrame({"line_id": ["BBB_7Y"] * 3, "protocol": ["A2A", "RFQ", "VOICE"],
                      "pi_fill": [0.55, 0.90, 0.98], "c_fill_bp": [4.0, 7.0, 12.0]})
best, table = route(lines, kappa_bp=20.0)
J_r = float(table.loc[table.protocol == "RFQ", "J_bp"].iloc[0])
J_seq = 0.55 * 4.0 + 0.45 * (1.5 + J_r)
check("one-shot router picks disclosed RFQ", J_r, best.protocol.iloc[0] == "RFQ")
check("A2A first beats RFQ when the odds clear the threshold", J_seq,
      try_a2a_first(0.55, 4.0, 1.5, J_r) and J_seq < J_r)
check("stressed name: the threshold flips", 0.25, not try_a2a_first(0.25, 4.0, 6.0, J_r))

print(pd.DataFrame(CHECKS, columns=["check", "value", "passed"]).to_string(index=False))
```


## F.3: Chapter 3: Cognitive Rewiring, From PJT RSSG to Systematic Desk Head {#code-3}

Listings from `03_ch03_pjt_rssg_cognitive_bridge.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 3.1: Glosten-Milgrom half-spread and winner's-curse shading for the RFQ bid {#code-3-1}

```python
import numpy as np
import pandas as pd
from scipy import optimize

rng = np.random.default_rng(3)


def sigmoid(z):
    """Overflow-safe logistic function."""
    return 0.5 * (1.0 + np.tanh(0.5 * np.asarray(z, dtype=float)))


def gm_half_spread(pi, q, delta):
    """Exact Glosten-Milgrom half-spread m - b for a SELL RFQ (eq. 3.1, asymmetric form).
    pi: P(sender informed); q: P(V = V+); delta: V+ - V- in price points.
    For a BUY RFQ the ask-side half-spread is gm_half_spread(pi, 1 - q, delta)."""
    pi, q, delta = (np.asarray(a, dtype=float) for a in (pi, q, delta))
    if np.any((pi < 0) | (pi > 1)) or np.any((q <= 0) | (q >= 1)) or np.any(delta < 0):
        raise ValueError("require 0 <= pi <= 1, 0 < q < 1, delta >= 0")
    return delta * q * (1.0 - q) * pi / (0.5 * (1.0 - pi) + pi * (1.0 - q))


def winners_curse_w(n_dealers, w_per_log=0.15):
    """Shading in units of sigma_v: w(1) = 0, increasing in n. Calibrate w_per_log from cover prices."""
    n = np.maximum(np.asarray(n_dealers, dtype=float), 1.0)
    return w_per_log * np.log(n)


def gm_bid(mid, sigma_v, pi_hat, n_dealers, q_inv, size, gamma, sigma_ido, w_per_log=0.15):
    """Eq. (3.2), vectorized over RFQs. Prices and sigmas in points over the holding horizon;
    q_inv and size in $mm face (size > 0 means the dealer buys); gamma in 1/(point * $mm)."""
    sigma_v = np.asarray(sigma_v, dtype=float)
    adverse = gm_half_spread(pi_hat, 0.5, 2.0 * sigma_v)
    curse = winners_curse_w(n_dealers, w_per_log) * sigma_v
    inventory = 0.5 * gamma * np.asarray(sigma_ido, dtype=float) ** 2 * (2.0 * np.asarray(q_inv, dtype=float) + size)
    return np.asarray(mid, dtype=float) - adverse - curse - inventory


# Sanity checks against the closed forms in the text
assert np.isclose(gm_half_spread(0.12, 0.5, 2 * 1.5), 0.12 * 1.5)          # eq. (3.1): pi * sigma_v
assert np.isclose(gm_half_spread(0.3, 0.7, 20.0), 20 * 0.063 / 0.44)       # Serta stylized: ~2.86 points
ratio = gm_half_spread(1e-5, 0.7, 20.0) / (2 * 1e-5 * 0.7 * 0.3 * 20.0)
assert abs(ratio - 1.0) < 1e-3                                              # small-pi approximation
assert np.all(np.diff(gm_half_spread(np.linspace(0, 1, 11), 0.5, 3.0)) > 0)  # monotone in pi
assert np.isclose(gm_bid(87.0, 1.5, 0.0, 1, 0.0, 0.0, 0.0, 1.0), 87.0)      # no information, no risk: bid = mid
```


### Listing 3.2: A simulated RFQ tape and its two tests: single-dealer markout and competition {#code-3-2}

```python
BETA_TRUE = np.array([-2.5, 0.6, 1.0, 1.2])   # intercept, size z-score, event window, distressed counterparty
SIGMA_V = 1.5                                  # points over the horizon


def simulate_rfq_flow(n_rfq=200_000, sigma_v=SIGMA_V, noise_sd=0.25, rho=0.3, rng=rng):
    """Simulated RFQ tape (prices in points). eta = +1 when the DEALER buys (client sells)."""
    size_z = rng.standard_normal(n_rfq)
    event = (rng.random(n_rfq) < 0.20).astype(float)        # within 72h of a scheduled event
    distressed = (rng.random(n_rfq) < 0.25).astype(float)   # distressed-fund counterparty flag
    X = np.column_stack([np.ones(n_rfq), size_z, event, distressed])
    pi_true = sigmoid(X @ BETA_TRUE)
    informed = rng.random(n_rfq) < pi_true
    u = np.where(rng.random(n_rfq) < 0.5, 1.0, -1.0)        # V = mid + u * sigma_v
    mid = rng.uniform(70.0, 100.0, n_rfq)
    client_sells = np.where(informed, u < 0, rng.random(n_rfq) < 0.5)
    eta = np.where(client_sells, 1.0, -1.0)
    n_dealers = rng.integers(2, 9, n_rfq)                   # 2..8 dealers in competition
    mid_h = mid + u * sigma_v + noise_sd * rng.standard_normal(n_rfq)
    # Competitors' price concessions (lower = better for the client); they share a signal about u.
    conc = sigma_v * (0.08 + 0.10 * np.abs(rng.standard_normal((n_rfq, 7))))
    conc[np.arange(7)[None, :] >= (n_dealers - 1)[:, None]] = np.inf
    eff = conc - (eta * rho * sigma_v * u)[:, None]
    eff_sorted = np.sort(eff, axis=1)
    tape = pd.DataFrame({"size_z": size_z, "event": event, "distressed": distressed,
                         "pi_true": pi_true, "informed": informed, "mid": mid, "eta": eta,
                         "n_dealers": n_dealers, "mid_h": mid_h,
                         "best_comp": eff_sorted[:, 0], "second_comp": eff_sorted[:, 1]})
    return tape, X


def se(x):
    x = np.asarray(x, dtype=float)
    return x.std(ddof=1) / np.sqrt(x.size)


df, X = simulate_rfq_flow()

# Test A: a single dealer that fills every RFQ. GM with the true pi(x) is zero-profit; quoting mid is not.
h_gm = gm_half_spread(df["pi_true"].to_numpy(), 0.5, 2 * SIGMA_V)
px_gm = df["mid"].to_numpy() - df["eta"].to_numpy() * h_gm       # bid if the dealer buys, ask if it sells
mo_gm = df["eta"].to_numpy() * (df["mid_h"].to_numpy() - px_gm)
mo_mid = df["eta"].to_numpy() * (df["mid_h"].to_numpy() - df["mid"].to_numpy())
assert abs(mo_gm.mean()) < 3 * se(mo_gm), mo_gm.mean()
assert abs(mo_mid.mean() - (-SIGMA_V * df["pi_true"].mean())) < 3 * se(mo_mid)
assert mo_mid.mean() < -10 * se(mo_mid)                           # assuming pi = 0 loses, unmistakably


# Test B: competition. Outcomes follow the Done / Covered / Traded Away taxonomy.
def rfq_outcomes(h_ours, best_comp, second_comp):
    done = h_ours < best_comp
    covered = (~done) & (h_ours < second_comp)
    return np.where(done, "Done", np.where(covered, "Covered", "Traded Away"))


df["outcome"] = rfq_outcomes(h_gm, df["best_comp"].to_numpy(), df["second_comp"].to_numpy())
df["mo_gm"] = mo_gm
fills = (df["outcome"] == "Done").to_numpy()
mo_fill, mo_lost = mo_gm[fills], mo_gm[~fills]                    # lost RFQs: counterfactual markouts
assert 0.02 < fills.mean() < 0.98
assert mo_fill.mean() < -3 * se(mo_fill)        # right pi(x), still losing on fills: the winner's curse
assert mo_lost.mean() > mo_fill.mean()          # the hands you lose are better than the hands you win
h_shaded = h_gm + winners_curse_w(df["n_dealers"].to_numpy()) * SIGMA_V
fills_shaded = h_shaded < df["best_comp"].to_numpy()
print(df["outcome"].value_counts(normalize=True).round(3).to_dict())
print(f"fills {fills.mean():.3f}, mean markout {mo_fill.mean():+.3f} pts; "
      f"lost (counterfactual) {mo_lost.mean():+.3f} pts; "
      f"with w(n) shading: fills {fills_shaded.mean():.3f}, "
      f"markout {(df['eta'].to_numpy() * (df['mid_h'].to_numpy() - (df['mid'].to_numpy() - df['eta'].to_numpy() * h_shaded)))[fills_shaded].mean():+.3f} pts")
```


### Listing 3.3: Maximum-likelihood fit of the probability that an RFQ is adverse {#code-3-3}

```python
def fit_pi(X, adverse):
    """MLE of beta in P(adverse | x) = (1 + sigmoid(x'beta)) / 2 (Sec. 3.2.2).
    Returns (beta_hat, standard errors from the expected Fisher information)."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(adverse, dtype=float)
    n, eps = X.shape[0], 1e-12

    def nll_and_grad(b):
        s = sigmoid(X @ b)
        p = np.clip(0.5 * (1.0 + s), eps, 1.0 - eps)
        dp = 0.5 * s * (1.0 - s)
        nll = -np.mean(y * np.log(p) + (1.0 - y) * np.log(1.0 - p))
        grad = -(X.T @ ((y / p - (1.0 - y) / (1.0 - p)) * dp)) / n
        return nll, grad

    res = optimize.minimize(nll_and_grad, np.zeros(X.shape[1]), jac=True, method="L-BFGS-B")
    assert np.isfinite(res.fun)
    s = sigmoid(X @ res.x)
    p = 0.5 * (1.0 + s)
    weight = (0.5 * s * (1.0 - s)) ** 2 / (p * (1.0 - p))
    info = X.T @ (X * weight[:, None])
    return res.x, np.sqrt(np.diag(np.linalg.inv(info)))


adverse = (df["eta"].to_numpy() * (df["mid_h"].to_numpy() - df["mid"].to_numpy()) < 0).astype(float)
beta_hat, beta_se = fit_pi(X, adverse)
assert np.all(np.abs(beta_hat - BETA_TRUE) < 4 * beta_se), (beta_hat, beta_se)
pi_hat = sigmoid(X @ beta_hat)
assert np.corrcoef(pi_hat, df["pi_true"].to_numpy())[0, 1] > 0.95

# Theo's Friday RFQ: large, inside a lender-call window, from a distressed-fund account; 8 dealers.
x_theo = np.array([1.0, 1.5, 1.0, 1.0])
pi_theo = float(sigmoid(x_theo @ beta_hat))
bid_theo = float(gm_bid(87.0, 6.0, pi_theo, 8, q_inv=5.0, size=15.0, gamma=0.002, sigma_ido=3.0))
assert 0.0 < pi_theo < 1.0 and bid_theo < 87.0
print(f"pi_hat = {pi_theo:.2f}; GM bid with a weekend sigma_v of 6 points = {bid_theo:.2f}")
```


### Listing 3.4: Reference moves, markouts and shrunk counterparty scores {#code-3-4}

```python
def ido_reference_move(p_ref, d_spr, beta, d_index_spread, d_mod, d_tsy):
    """Systematic price move (points) implied by index-spread and Treasury-yield changes (decimals)."""
    return p_ref * (-d_spr * beta * d_index_spread - d_mod * d_tsy)


def markouts_bp(fills_df, horizons=(1, 5, 20)):
    """Columns needed: p0, eta, mid_{h}d; optional sys_{h}d (systematic move, points) for IDO markouts."""
    out = {}
    for h in horizons:
        ref = fills_df[f"mid_{h}d"] - fills_df.get(f"sys_{h}d", 0.0)
        out[f"mo_{h}d_bp"] = fills_df["eta"] * (ref - fills_df["p0"]) / fills_df["p0"] * 1e4
    return pd.DataFrame(out, index=fills_df.index)


hand = pd.DataFrame({"p0": [85.75], "eta": [1.0], "mid_5d": [81.0],
                     "sys_5d": [ido_reference_move(87.0, 3.5, 1.3, 0.0020, 3.6, -0.0010)]})
assert np.isclose(hand["sys_5d"].iloc[0], -0.4785, atol=1e-3)
assert -510 < markouts_bp(hand, horizons=(5,)).iloc[0, 0] < -490     # about -500bp of price


def shrunk_cpty_scores(fills_df, col="mo_bp"):
    """Empirical-Bayes shrinkage of per-counterparty mean markouts (Sec. 3.3.4)."""
    g = fills_df.groupby("cpty")[col]
    n_c, mean_c = g.size(), g.mean()
    dof = (n_c - 1).sum()
    sigma2 = float((g.var(ddof=1).fillna(0.0) * (n_c - 1)).sum() / max(dof, 1))   # pooled per-fill variance
    tau2 = max(float(mean_c.var(ddof=1) - (sigma2 / n_c).mean()), 0.0)
    k = n_c / (n_c + sigma2 / tau2) if tau2 > 0 else n_c * 0.0
    return pd.DataFrame({"n": n_c, "raw": mean_c, "shrink": k, "theta_hat": k * mean_c}), tau2, sigma2


n_cp, tau_true, sig_mo = 400, 20.0, 150.0                    # bp
theta = rng.normal(0.0, tau_true, n_cp)
n_fills = rng.geometric(1 / 40, n_cp)                        # every counterparty has at least one fill
cp = np.repeat(np.arange(n_cp), n_fills)
panel = pd.DataFrame({"cpty": cp, "mo_bp": theta[cp] + sig_mo * rng.standard_normal(cp.size)})
scores, tau2_hat, sigma2_hat = shrunk_cpty_scores(panel)
assert scores["shrink"].between(0.0, 1.0).all() and tau2_hat >= 0.0
mse_raw = np.mean((scores["raw"].to_numpy() - theta) ** 2)
mse_eb = np.mean((scores["theta_hat"].to_numpy() - theta) ** 2)
assert mse_eb < mse_raw
print(f"tau_hat = {np.sqrt(tau2_hat):.1f}bp (true {tau_true}); MSE raw {mse_raw:.0f} vs shrunk {mse_eb:.0f}")
```


### Listing 3.5: Re-basing a PD to the live default rate and updating it from an 8-K {#code-3-5}

```python
def elkan(p, S, T):
    """Eq. (3.4): re-base a PD calibrated to sample default rate S onto live base rate T."""
    p = np.asarray(p, dtype=float)
    return T * (p - p * S) / (S - p * S + p * T - S * T)


def update_pd_from_8k(p_prior, lr, S=None, T=None):
    """Eq. (3.3). Optional Elkan re-basing of the prior first. lr = P(E | default) / P(E | no default)."""
    p = np.asarray(p_prior, dtype=float)
    lr = np.asarray(lr, dtype=float)
    if np.any((p < 0) | (p > 1)) or np.any(lr < 0):
        raise ValueError("require p in [0, 1] and lr >= 0")
    if S is not None and T is not None:
        p = elkan(p, S, T)
    return lr * p / (1.0 - p + lr * p)


def hazard_from_pd(p, horizon_years=1.0):
    return -np.log1p(-np.asarray(p, dtype=float)) / horizon_years


grid = np.linspace(0.0, 1.0, 101)
assert np.allclose(update_pd_from_8k(grid, 1.0), grid)                         # LR = 1 is no news
assert np.all(np.diff(update_pd_from_8k(0.06, np.linspace(0.1, 10.0, 50))) > 0)  # monotone in LR
p_post = float(update_pd_from_8k(0.06, 2.5))
assert np.isclose(p_post, 0.1376, atol=5e-4)
ds_bp = 0.6 * 2.0 * (hazard_from_pd(p_post) - hazard_from_pd(0.06)) * 1e4      # L = 0.6, kappa = 2
assert 1000 < ds_bp < 1070                                                       # about 1,030bp
S_, T_ = 0.02, 0.05
e = elkan(grid, S_, T_)
assert np.all((e >= -1e-12) & (e <= 1 + 1e-12)) and np.isclose(elkan(0.5, 0.2, 0.2), 0.5)
assert np.all((T_ / S_) * grid[grid > S_ / T_ + 1e-9] > 1.0)                    # the T/S shortcut breaks the bound
odds = lambda z: z / (1.0 - z)
inner = grid[1:-1]
assert np.allclose(odds(elkan(inner, S_, T_)), odds(inner) * odds(T_) / odds(S_))  # (3.4) is an odds update
print(f"posterior PD {p_post:.4f}; implied spread move {ds_bp:,.0f}bp")
```


### Listing 3.6: CUSUM detector for the pre-LMT signature, with a PRS-dependent threshold {#code-3-6}

```python
def cusum_lmt_detector(y, mu1, sigma_y, h):
    """Eq. (3.5) on a (T,) or (T, n_paths) array of ADV-scaled net informed-type buying.
    Returns (statistic path, first alarm index per path or -1)."""
    y = np.asarray(y, dtype=float)
    y2 = y.reshape(y.shape[0], -1)
    llr = (mu1 / sigma_y ** 2) * (y2 - 0.5 * mu1)
    stat = np.empty_like(y2)
    s = np.zeros(y2.shape[1])
    for t in range(y2.shape[0]):
        s = np.maximum(0.0, s + llr[t])
        stat[t] = s
    thresh = np.broadcast_to(np.asarray(h, dtype=float), (y2.shape[1],))
    hit = stat > thresh[None, :]
    first = np.where(hit.any(axis=0), hit.argmax(axis=0), -1)
    return stat.reshape(y.shape), first


def prs_threshold(prs, h0=6.0, h_min=2.5, h_max=10.0):
    """h(PRS) = h0 - logit(PRS), floored so that one noisy day cannot fire the alarm."""
    prs = np.clip(np.asarray(prs, dtype=float), 1e-6, 1.0 - 1e-6)
    return np.clip(h0 - np.log(prs / (1.0 - prs)), h_min, h_max)


h_design, mu1, sig_y, t_max, n_paths = 4.0, 1.0, 1.0, 6000, 500
_, first_h0 = cusum_lmt_detector(rng.standard_normal((t_max, n_paths)), mu1, sig_y, h_design)
run_len = np.where(first_h0 >= 0, first_h0 + 1, t_max)       # censored paths count as t_max (conservative)
assert run_len.mean() >= np.exp(h_design)                     # Lorden: ARL to false alarm >= e^h
_, first_h1 = cusum_lmt_detector(mu1 + rng.standard_normal((400, n_paths)), mu1, sig_y, h_design)
kl = mu1 ** 2 / (2 * sig_y ** 2)
assert np.all(first_h1 >= 0) and (first_h1 + 1).mean() < 2 * h_design / kl + 5
p_grid = np.linspace(0.05, 0.95, 19)
assert np.all(np.diff(prs_threshold(p_grid)) <= 0) and np.isclose(prs_threshold(0.5), 6.0)
print(f"ARL0 >= {run_len.mean():.0f} days (bound {np.exp(h_design):.0f}); "
      f"mean detection delay {(first_h1 + 1).mean():.1f} days (h/KL = {h_design / kl:.0f})")
```


## F.4: Chapter 4: Inside the Systematic Credit Industry {#code-4}

Listings from `04_ch04_inside_the_systematic_credit_industry.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 4.1: Effective breadth with issuer clustering, and the fundamental law {#code-4-1}

```python
# capacity_breadth_engine.py, block 1 of 4: breadth and the fundamental law, eq. (4.1)
import numpy as np
from dataclasses import dataclass

SEED = 404

def effective_breadth(n_bonds, n_issuers, rho):
    """BR_eff = N / (1 + (m - 1) * rho), with m = N / M bonds per issuer."""
    if n_issuers <= 0 or n_bonds < n_issuers:
        raise ValueError("need n_bonds >= n_issuers > 0")
    if not 0.0 <= rho <= 1.0:
        raise ValueError("rho must lie in [0, 1]")
    m = n_bonds / n_issuers
    return n_bonds / (1.0 + (m - 1.0) * rho)

def fundamental_law_ir(ic, br_eff, tc):
    """IR = IC * sqrt(BR_eff) * TC; annual, gross of costs."""
    return ic * np.sqrt(max(br_eff, 0.0)) * tc

assert abs(effective_breadth(1800, 800, 1.0) - 800.0) < 1e-12    # (a) rho = 1: one bet per issuer
assert abs(effective_breadth(1800, 800, 0.0) - 1800.0) < 1e-12   # (a) rho = 0: every bond counts
assert abs(effective_breadth(47, 1, 1.0) - 1.0) < 1e-12          # ROBO's 47 bonds are one bet
assert abs(effective_breadth(1800, 800, 0.7) - 960.0) < 1e-9     # the worked example in 4.3
```


### Listing 4.2: Net alpha under square-root impact, and the capacity limit {#code-4-2}

```python
# block 2 of 4: capacity under square-root impact, eq. (4.2). Units: $mm and annual decimals.
def net_alpha(aum, alpha0, turnover, cost0, eta, liquidity):
    """alpha(A) = alpha0 - 2T [c0 + eta * sqrt(2 T A / L)], with T one-way."""
    liq = max(float(liquidity), 1e-12)
    part = np.sqrt(np.maximum(2.0 * turnover * np.asarray(aum, dtype=float) / liq, 0.0))
    return alpha0 - 2.0 * turnover * (cost0 + eta * part)

def net_alpha_curve(alpha0, turnover, cost0, eta, liquidity, aum_grid):
    aum = np.asarray(aum_grid, dtype=float)
    a = net_alpha(aum, alpha0, turnover, cost0, eta, liquidity)
    return {"aum": aum, "alpha": a, "dollar_alpha": aum * a}

def aum_star_closed_form(alpha0, turnover, cost0, eta, liquidity):
    """A* = L g^2 / (18 T^3 eta^2), g = alpha0 - 2 T c0. Zero if costs eat the edge."""
    g = alpha0 - 2.0 * turnover * cost0
    if g <= 0.0:
        return 0.0
    if turnover <= 0.0 or eta <= 0.0:
        return np.inf
    return liquidity * g**2 / (18.0 * turnover**3 * eta**2)

P = dict(alpha0=0.015, turnover=0.6, cost0=0.0025, eta=0.02, liquidity=20_000.0)  # illustrative HY row
g = P["alpha0"] - 2.0 * P["turnover"] * P["cost0"]
a_star = aum_star_closed_form(**P)
grid = np.linspace(1.0, 3.0 * a_star, 300_001)
curve = net_alpha_curve(aum_grid=grid, **P)
a_num = grid[np.argmax(curve["dollar_alpha"])]
assert abs(a_num / a_star - 1.0) < 0.01                  # (b) numeric argmax matches closed form
assert abs(net_alpha(a_star, **P) - g / 3.0) < 1e-9      # (b) the client keeps one third
assert abs(net_alpha(1e-9, **P) - g) < 1e-6              # (c) a tiny book keeps spread-net alpha
assert abs(net_alpha(2.25 * a_star, **P)) < 1e-9         # net alpha is zero at 9/4 of A*
print(f"A* = ${a_star:,.0f}mm; net alpha at A* = {1e4 * net_alpha(a_star, **P):.1f}bp")
```


### Listing 4.3: Ownership-cap position weights and the uninvested fraction {#code-4-3}

```python
# block 3 of 4: Dynkin cap weights and the non-invested fraction, eq. (4.3)
def dynkin_cap_weights(mv, aum, cap_frac=0.05, w_max=None):
    """w_i = min(1/n, w_max, cap_frac * MV_i / A); f_cash = 1 - sum(w). mv and aum in $mm."""
    mv = np.asarray(mv, dtype=float)
    if mv.ndim != 1 or mv.size == 0 or np.any(mv <= 0.0):
        raise ValueError("mv must be a non-empty 1-D array of positive market values")
    n = mv.size
    cap = 1.0 if w_max is None else float(w_max)
    w = np.minimum.reduce([np.full(n, 1.0 / n), np.full(n, cap),
                           cap_frac * mv / max(float(aum), 1e-12)])
    return w, max(0.0, 1.0 - float(w.sum()))

rng = np.random.default_rng(SEED)
mv_fa = rng.lognormal(mean=np.log(300.0), sigma=1.0, size=60)   # 60 fallen-angel issuers (illustrative)
w_tiny, cash_tiny = dynkin_cap_weights(mv_fa, aum=1.0)
assert np.allclose(w_tiny, 1.0 / 60) and cash_tiny < 1e-12      # (d) tiny book: equal weights
w_huge, _ = dynkin_cap_weights(mv_fa, aum=1e9)
assert np.corrcoef(w_huge, mv_fa)[0, 1] > 1.0 - 1e-12           # (d) huge book: market-value weights
w_a, _ = dynkin_cap_weights(mv_fa, aum=500.0, cap_frac=0.05)
w_b, _ = dynkin_cap_weights(mv_fa, aum=250.0, cap_frac=0.025)
assert np.allclose(w_a, w_b)                                     # (e) only c / A matters
for A in (125.0, 500.0, 1000.0, 2000.0):
    print(f"AUM ${A:,.0f}mm: invested {1.0 - dynkin_cap_weights(mv_fa, A)[1]:.0%}")
```


### Listing 4.4: Scoring the six-axis map: breadth, gross and net IR, capacity and cash drag {#code-4-4}

```python
# block 4 of 4: score rows of the six-axis map (all parameters illustrative, not the firms' numbers)
@dataclass
class FrameworkScore:
    name: str
    br_eff: float
    ir_gross: float
    ir_net_at_aum: float
    aum_star: float
    cash_drag: float

COST_KEYS = ("alpha0", "turnover", "cost0", "eta", "liquidity")

def framework_score(name, row, seed=SEED):
    br = effective_breadth(row["n_bonds"], row["n_issuers"], row["rho"])
    ir_g = fundamental_law_ir(row["ic"], br, row["tc"])
    kw = {k: row[k] for k in COST_KEYS}
    a_net = float(net_alpha(row["aum"], **kw))
    ir_n = ir_g * a_net / row["alpha0"]      # assumes costs leave tracking error unchanged (Dynkin p.711)
    mv = np.random.default_rng(seed).lognormal(np.log(row["mv_median"]), 1.0, row["n_issuers"])
    _, f_cash = dynkin_cap_weights(mv, row["aum"], cap_frac=row.get("cap_frac", 0.05))
    return FrameworkScore(name, br, ir_g, ir_n, aum_star_closed_form(**kw), f_cash)

ROWS = {
    "IG long-only value": dict(n_bonds=6000, n_issuers=1000, rho=0.8, ic=0.02, tc=0.4,
                               alpha0=0.006, turnover=0.4, cost0=0.0008, eta=0.008,
                               liquidity=150_000.0, aum=5_000.0, mv_median=3_000.0),
    "HY long/short multi-factor": dict(n_bonds=1800, n_issuers=800, rho=0.7, ic=0.03, tc=0.5,
                                       **P, aum=1_500.0, mv_median=1_500.0),
    "HY equity momentum": dict(n_bonds=1800, n_issuers=800, rho=0.7, ic=0.04, tc=0.4,
                               alpha0=0.04, turnover=2.5, cost0=0.0025, eta=0.02,
                               liquidity=20_000.0, aum=100.0, mv_median=1_500.0),
    "Multi-asset allocator": dict(n_bonds=8, n_issuers=8, rho=0.0, ic=0.10, tc=0.7,
                                  alpha0=0.01, turnover=0.3, cost0=0.002, eta=0.005,
                                  liquidity=2_000_000.0, aum=10_000.0, mv_median=50_000.0,
                                  cap_frac=1.0),
    "Smart-beta HY ETF": dict(n_bonds=1800, n_issuers=800, rho=0.7, ic=0.015, tc=0.8,
                              alpha0=0.005, turnover=0.5, cost0=0.001, eta=0.01,
                              liquidity=20_000.0, aum=1_500.0, mv_median=1_500.0),
}

print(f"{'row':<28}{'BR_eff':>8}{'IR_g':>7}{'IR_net':>8}{'A* $mm':>14}{'cash':>7}")
for name, row in ROWS.items():
    s = framework_score(name, row)
    assert row["n_issuers"] - 1e-9 <= s.br_eff <= row["n_bonds"] + 1e-9
    assert s.ir_net_at_aum <= s.ir_gross + 1e-12 and 0.0 <= s.cash_drag < 1.0
    print(f"{s.name:<28}{s.br_eff:>8.0f}{s.ir_gross:>7.2f}{s.ir_net_at_aum:>8.2f}"
          f"{s.aum_star:>14,.0f}{s.cash_drag:>7.1%}")
```


## F.5: Chapter 5: Probability Distributions in Distressed & High-Yield Credit {#code-5}

Listings from `05_ch05_credit_probability_distributions.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 5.1: Recovery specification and mixture moments {#code-5-1}

```python
# credit_mixture_lab.py, block 1 of 5: mixture moments, recovery spec, Monte Carlo.
# Blocks run in order in one interpreter; every random draw flows from SEED.
import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import optimize, special, stats

SEED = 7


@dataclass(frozen=True)
class RecoverySpec:
    """Recovery R per 1.0 of par: 0 w.p. pi0, 1.0 (par) w.p. pi1,
    otherwise support_max * Beta(a, b). The convention is named, never implied."""
    a: float
    b: float
    pi0: float = 0.0
    pi1: float = 0.0
    support_max: float = 1.0
    convention: str = "RFV"

    def __post_init__(self):
        if not (self.a > 0 and self.b > 0):
            raise ValueError("Beta parameters must be positive")
        if self.pi0 < 0 or self.pi1 < 0 or self.pi0 + self.pi1 >= 1.0:
            raise ValueError("need pi0, pi1 >= 0 and pi0 + pi1 < 1")
        if not 1.0 <= self.support_max <= 1.5:
            raise ValueError("support_max must lie in [1.0, 1.5]")
        if self.convention not in ("RFV", "RMV", "RT"):
            raise ValueError("convention must be RFV, RMV or RT")


def beta_mom(mu, sd, support_max=1.0):
    """Method-of-moments Beta(a, b) for a recovery with mean mu, s.d. sd on [0, support_max]."""
    m, s = mu / support_max, sd / support_max
    if not (0.0 < m < 1.0 and s > 0.0):
        raise ValueError("need 0 < mu < support_max and sd > 0")
    if s**2 >= m * (1.0 - m):
        raise ValueError("variance at or above the Bernoulli bound: the data are "
                         "all-or-nothing; add inflation masses, do not clip")
    k = m * (1.0 - m) / s**2 - 1.0
    return m * k, (1.0 - m) * k


def central_from_raw(m1, m2, m3, m4):
    """(mean, variance, mu3, mu4) from raw moments E[Z], E[Z^2], E[Z^3], E[Z^4]."""
    return (m1, m2 - m1**2, m3 - 3 * m1 * m2 + 2 * m1**3,
            m4 - 4 * m1 * m3 + 6 * m1**2 * m2 - 3 * m1**4)


def recovery_moments(rec):
    """Exact (mean, var, mu3, mu4) of R under the inflated, rescaled Beta."""
    w = 1.0 - rec.pi0 - rec.pi1
    raw = [rec.pi1 + w * rec.support_max**k
           * np.prod([(rec.a + j) / (rec.a + rec.b + j) for j in range(k)])
           for k in range(1, 5)]
    return central_from_raw(*raw)


def gaussian_moments(mean, sd):
    return mean, sd**2, 0.0, 3.0 * sd**4


def survival_moments_dts(spread, h, spr_dur, spr_conv, kappa, roll=0.0):
    """Exact moments of X = s*h + roll - D*ds + 0.5*C*ds**2, ds ~ N(0, (kappa*s)**2 * h)."""
    if spread <= 0 or h <= 0 or kappa <= 0:
        raise ValueError("spread (decimal), horizon (years) and kappa must be positive")
    v, c, D = (kappa * spread) ** 2 * h, 0.5 * spr_conv, spr_dur
    return (spread * h + roll + c * v,
            D**2 * v + 2 * c**2 * v**2,
            6 * D**2 * c * v**2 + 8 * c**3 * v**3,
            3 * D**4 * v**2 + 60 * D**2 * c**2 * v**3 + 60 * c**4 * v**4)


def mixture_moments(q, price0, surv, rec):
    """Closed-form moments of R_h = (1-D) X + D Y with Y = R/price0 - 1, D ~ Bernoulli(q).
    q is a PHYSICAL horizon default probability; surv = (mean, var, mu3, mu4) of X."""
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be a probability")
    if not 0.0 < price0 <= 1.5:
        raise ValueError("price0 is per 1.0 of par and must lie in (0, 1.5]")
    mx, vx, m3x, m4x = surv
    mr, vr, m3r, m4r = recovery_moments(rec)
    my, vy, m3y, m4y = mr / price0 - 1.0, vr / price0**2, m3r / price0**3, m4r / price0**4
    J, qc = mx - my, 1.0 - q
    var = qc * vx + q * vy + q * qc * J**2
    mu3 = -q * qc * (1 - 2 * q) * J**3 + 3 * q * qc * J * (vx - vy) + qc * m3x + q * m3y
    mu4 = (qc * (q**4 * J**4 + 6 * q**2 * J**2 * vx + 4 * q * J * m3x + m4x)
           + q * (qc**4 * J**4 + 6 * qc**2 * J**2 * vy - 4 * qc * J * m3y + m4y))
    return {"mean": mx - q * J, "vol": np.sqrt(var), "skew": mu3 / var**1.5,
            "exkurt": mu4 / var**2 - 3.0}


def sample_recovery(rec, n, rng):
    u = rng.random(n)
    r = rec.support_max * rng.beta(rec.a, rec.b, size=n)
    r[u < rec.pi0] = 0.0
    r[(u >= rec.pi0) & (u < rec.pi0 + rec.pi1)] = 1.0
    return r


def gaussian_sampler(mean, sd):
    return lambda m, rng: mean + sd * rng.standard_normal(m)


def simulate_mixture(q, price0, surv_sampler, rec, n=1_000_000, seed=SEED):
    """Monte Carlo of R_h, stratified on D (exactly round(q*n) defaults) so a test of the
    closed form is not swamped by binomial noise. Returns (returns, default flags)."""
    rng = np.random.default_rng(seed)
    n_def = int(round(q * n))
    dflag = np.zeros(n, dtype=bool)
    dflag[:n_def] = True
    ret = np.empty(n)
    ret[~dflag] = surv_sampler(n - n_def, rng)
    ret[dflag] = sample_recovery(rec, n_def, rng) / price0 - 1.0
    return ret, dflag


def sample_moments(x):
    c = x - x.mean()
    var = np.mean(c**2)
    return {"mean": x.mean(), "vol": np.sqrt(var), "skew": np.mean(c**3) / var**1.5,
            "exkurt": np.mean(c**4) / var**2 - 3.0}


def var_es(x, p):
    """Lower-tail VaR and expected shortfall of returns x at confidence p, as returns."""
    v = np.quantile(x, 1.0 - p)
    return v, x[x <= v].mean()


def horizon_value(price0, ret, dflag, carry, call_price=None):
    """Horizon value per 1.0 par. In default it is R exactly; in survival the call
    caps the clean price, not the coupons already collected (carry)."""
    v = price0 * (1.0 + ret)
    if call_price is not None:
        v = np.where(dflag, v, np.minimum(v - carry, call_price) + carry)
    return v


# ---- Sanity check 1: Theo's bond (5.1.4), closed form vs. the table vs. Monte Carlo
a_su, b_su = beta_mom(0.40, 0.275)                      # Schmid p.103 senior unsecured moments
assert abs(a_su - 0.87) < 0.01 and abs(b_su - 1.30) < 0.01
a_fam, b_fam = beta_mom(0.5021, 0.2646, support_max=1.2)
assert abs(a_fam - 1.68) < 0.01 and abs(b_fam - 2.33) < 0.01
try:
    beta_mom(0.50, 0.55)
    raise AssertionError("beta_mom must refuse all-or-nothing moments")
except ValueError:
    pass

rec_su = RecoverySpec(a=a_su, b=b_su)
theo_surv = gaussian_moments(0.07, 0.041)
theo = mixture_moments(0.04, 0.92, theo_surv, rec_su)
assert abs(theo["mean"] - 0.0446) < 5e-4 and abs(theo["vol"] - 0.144) < 2e-3
assert abs(theo["skew"] + 5.1) < 0.1 and abs(theo["exkurt"] - 28.0) < 1.0

m0 = mixture_moments(0.0, 0.92, theo_surv, rec_su)      # q = 0: the survival world
assert abs(m0["vol"] - 0.041) < 1e-12 and abs(m0["skew"]) < 1e-12 and abs(m0["exkurt"]) < 1e-9
m1 = mixture_moments(1.0, 0.92, theo_surv, rec_su)      # q = 1: the default world
beta_skew = (2 * (b_su - a_su) * np.sqrt(a_su + b_su + 1)
             / ((a_su + b_su + 2) * np.sqrt(a_su * b_su)))
assert abs(m1["skew"] - beta_skew) < 1e-8

for q in (0.0005, 0.01, 0.04):                          # Bernoulli skeleton (5.1.3)
    skel = mixture_moments(q, 1.0, gaussian_moments(0.05, 1e-6), RecoverySpec(a=4e6, b=6e6))
    assert abs(skel["skew"] / (-(1 - 2 * q) / np.sqrt(q * (1 - q))) - 1) < 1e-3
    assert abs(skel["exkurt"] / ((1 - 6 * q * (1 - q)) / (q * (1 - q))) - 1) < 1e-3

ret, dflag = simulate_mixture(0.04, 0.92, gaussian_sampler(0.07, 0.041), rec_su)
mc = sample_moments(ret)
assert abs(mc["mean"] - theo["mean"]) < 1e-3
for key, tol in (("vol", 0.02), ("skew", 0.02), ("exkurt", 0.05)):
    assert abs(mc[key] / theo[key] - 1) < tol, (key, mc[key], theo[key])
print(pd.DataFrame({"closed_form": theo, "monte_carlo": mc}).round(4))

var99, es99 = var_es(ret, 0.99)                         # 1% / 4%: inside the default lump
r25 = stats.beta.ppf(0.25, a_su, b_su)
es_exact = 0.40 * stats.beta.cdf(r25, a_su + 1, b_su) / 0.25 / 0.92 - 1.0
assert abs(var99 - (r25 / 0.92 - 1.0)) < 0.01 and abs(es99 - es_exact) < 0.01

# DTS survival leg of a callable (negative convexity): left-skewed before any default
dts = survival_moments_dts(spread=0.055, h=1.0, spr_dur=3.5, spr_conv=-8.0, kappa=0.35)
ds = 0.35 * 0.055 * np.random.default_rng(SEED).standard_normal(2_000_000)
emp = sample_moments(0.055 - 3.5 * ds + 0.5 * (-8.0) * ds**2)
assert abs(emp["mean"] - dts[0]) < 2e-4 and abs(emp["vol"] / np.sqrt(dts[1]) - 1) < 0.01
assert dts[2] < 0 and abs(emp["skew"] - dts[2] / dts[1] ** 1.5) < 0.02

value = horizon_value(0.92, ret, dflag, carry=0.08, call_price=1.04)
assert value.min() >= 0.0 and value[~dflag].max() <= 1.04 + 0.08 + 1e-12
assert abs(value[dflag].mean() - 0.40) < 0.005
```


### Listing 5.2: Zero-one-inflated Beta regression for recoveries {#code-5-2}

```python
# credit_mixture_lab.py, block 2 of 5: zero-one-inflated Beta regression for recoveries.
TARGETS = ("rec_ultimate_disc", "rec_trading_30d")      # never pooled in one fit (5.5.6)


def _beta_nll(params, X, y):
    """Negative log-likelihood and gradient: logit mean, log precision (Ferrari-Cribari-Neto)."""
    k = X.shape[1]
    phi = np.exp(params[k])
    mu = np.clip(special.expit(X @ params[:k]), 1e-10, 1 - 1e-10)
    a, b = mu * phi, (1.0 - mu) * phi
    ly, l1y = np.log(y), np.log1p(-y)
    ll = (special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)
          + (a - 1.0) * ly + (b - 1.0) * l1y)
    dg_a, dg_b = special.digamma(a), special.digamma(b)
    g_beta = X.T @ (phi * ((ly - l1y) - (dg_a - dg_b)) * mu * (1.0 - mu))
    g_phi = np.sum(special.digamma(phi) - mu * dg_a - (1.0 - mu) * dg_b
                   + mu * ly + (1.0 - mu) * l1y)
    return -ll.sum(), -np.append(g_beta, g_phi * phi)


def _mnl_nll(params, X, cls):
    """Multinomial logit over {0: interior, 1: exact zero, 2: exact par}; class 0 is the base."""
    k = X.shape[1]
    eta = X @ np.column_stack([np.zeros(k), params.reshape(2, k).T])
    logp = eta - special.logsumexp(eta, axis=1, keepdims=True)
    resid = np.exp(logp) - np.eye(3)[cls]
    return -logp[np.arange(cls.size), cls].sum(), (X.T @ resid)[:, 1:].T.ravel()


def _num_hessian(f, x, args, eps=1e-5):
    """Central-difference Hessian from an analytic gradient, symmetrized."""
    H = np.empty((x.size, x.size))
    for j in range(x.size):
        e = np.zeros(x.size)
        e[j] = eps
        H[:, j] = (f(x + e, *args)[1] - f(x - e, *args)[1]) / (2 * eps)
    return 0.5 * (H + H.T)


def _mle(f, x0, args):
    res = optimize.minimize(f, x0, args=args, jac=True, method="BFGS")
    if not res.success:
        warnings.warn(f"optimizer: {res.message}; inspect before use")
    return res.x, np.linalg.inv(_num_hessian(f, res.x, args))


def fit_beta_regression(panel, target, covariates, eps=1e-6, inflate=True):
    """Zero-one-inflated Beta regression (Ospina-Ferrari). Returns coefficient and
    standard-error Series for the masses ('mass', 'mass_se') and the Beta part ('beta', 'beta_se')."""
    if target not in TARGETS:
        raise ValueError(f"target must be one of {TARGETS}: name the measure")
    if set(covariates) & set(TARGETS):
        raise ValueError("a recovery column cannot be a covariate")
    df = panel.dropna(subset=[target])
    names = ["const"] + list(covariates)
    if len(df) < 20 * len(names):
        raise ValueError("too few non-missing observations for this many covariates")
    y = df[target].to_numpy(dtype=float)
    if y.min() < 0.0 or y.max() > 1.0:
        raise ValueError("rescale recoveries to [0, 1] (divide by support_max) first")
    X = np.column_stack([np.ones(len(df))] + [df[c].to_numpy(dtype=float) for c in covariates])
    cls = np.where(y <= eps, 1, np.where(y >= 1.0 - eps, 2, 0))
    out = {}
    if inflate:
        if min((cls == 1).sum(), (cls == 2).sum()) < 5:
            raise ValueError("fewer than 5 exact zeros or pars: use inflate=False or pool more data")
        g, cov_g = _mle(_mnl_nll, np.zeros(2 * X.shape[1]), (X, cls))
        idx = [f"zero:{n}" for n in names] + [f"one:{n}" for n in names]
        out["mass"] = pd.Series(g, index=idx)
        out["mass_se"] = pd.Series(np.sqrt(np.diag(cov_g)), index=idx)
    elif (cls != 0).any():
        raise ValueError("exact zeros or pars present: a plain Beta has log-likelihood -inf there")
    inner = cls == 0
    coef, cov_b = _mle(_beta_nll, np.append(np.zeros(X.shape[1]), np.log(5.0)),
                       (X[inner], y[inner]))
    idx = names + ["log_phi"]
    out["beta"] = pd.Series(coef, index=idx)
    out["beta_se"] = pd.Series(np.sqrt(np.diag(cov_b)), index=idx)
    return out


TRUE_BETA = np.array([-1.0, 0.8, 0.9, 1.2, -2.0])      # const, 1L, coverage, cushion, out-of-deal
TRUE_LOG_PHI = np.log(10.0)
TRUE_G0 = np.array([-3.0, -1.0, -0.8, -1.0, 2.0])      # exact-zero mass
TRUE_G1 = np.array([-3.5, 1.0, 0.5, 0.5, -1.5])        # exact-par mass
COVS = ["first_lien", "collateral_cov", "debt_cushion", "participant_out"]


def synthetic_recovery_panel(n=6000, seed=SEED):
    """RecoveryPanel-shaped frame with known parameters; trading-price recoveries left NaN."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "issuer_id": rng.integers(0, 1500, n),
        "first_lien": rng.random(n) < 0.5,
        "collateral_cov": rng.uniform(0.2, 1.6, n),
        "debt_cushion": rng.uniform(0.0, 0.6, n),
        "participant_out": rng.random(n) < 0.15,
    })
    X = np.column_stack([np.ones(n)] + [df[c].to_numpy(dtype=float) for c in COVS])
    mu, phi = special.expit(X @ TRUE_BETA), np.exp(TRUE_LOG_PHI)
    r = rng.beta(mu * phi, (1.0 - mu) * phi)
    eta = np.column_stack([np.zeros(n), X @ TRUE_G0, X @ TRUE_G1])
    prob = np.exp(eta - special.logsumexp(eta, axis=1, keepdims=True))
    u = rng.random(n)
    df["rec_ultimate_disc"] = np.where(u < prob[:, 1], 0.0,
                                       np.where(u < prob[:, 1] + prob[:, 2], 1.0, r))
    df["rec_trading_30d"] = np.nan
    return df


# ---- Sanity check 2: parameter recovery on a synthetic panel; refusals on unnamed measures
panel = synthetic_recovery_panel()
fit = fit_beta_regression(panel, "rec_ultimate_disc", COVS, eps=1e-9)
z_b = (fit["beta"].to_numpy() - np.append(TRUE_BETA, TRUE_LOG_PHI)) / fit["beta_se"].to_numpy()
z_m = (fit["mass"].to_numpy() - np.append(TRUE_G0, TRUE_G1)) / fit["mass_se"].to_numpy()
assert np.all(np.abs(z_b) < 4) and np.all(np.abs(z_m) < 4), (z_b.round(2), z_m.round(2))
assert fit["beta"]["participant_out"] < -1.0 and fit["mass"]["zero:participant_out"] > 1.0
for bad_target in ("recovery", "rec_trading_30d"):     # unnamed measure; all-NaN column
    try:
        fit_beta_regression(panel, bad_target, COVS)
        raise AssertionError(f"must refuse target={bad_target}")
    except ValueError:
        pass
```


### Listing 5.3: Kou jump-diffusion first passage {#code-5-3}

```python
# credit_mixture_lab.py, block 3 of 5: Kou jump-diffusion first passage (P-measure risk run).
def kou_jump_sizes(m, p, eta1, eta2, rng):
    """m log-jumps: up ~ Exp(eta1) w.p. p, down ~ -Exp(eta2) w.p. 1 - p."""
    up = rng.random(m) < p
    return np.where(up, rng.exponential(1.0 / eta1, m), -rng.exponential(1.0 / eta2, m))


def simulate_kou_jd(V0, barrier, mu, sigma, lam, p, eta1, eta2, T, n_steps, n, seed=SEED):
    """Time-stepped first passage of x = log(V/B). Returns dict of (n,) arrays: default,
    tau (inf if alive), via_jump, ratio = V_tau/B (nan if alive; 1.0 for diffusive hits)."""
    if not V0 > barrier > 0:
        raise ValueError("need V0 > barrier > 0")
    if not (eta1 > 1 and eta2 > 0 and 0 <= p <= 1 and lam >= 0 and sigma >= 0):
        raise ValueError("Kou parameters out of range (eta1 > 1 keeps E[exp(Y)] finite)")
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    zeta = p * eta1 / (eta1 - 1) + (1 - p) * eta2 / (eta2 + 1) - 1.0   # E[e^Y] - 1
    drift = (mu - 0.5 * sigma**2 - lam * zeta) * dt
    x = np.full(n, np.log(V0 / barrier))
    alive = np.ones(n, dtype=bool)
    tau, ratio = np.full(n, np.inf), np.full(n, np.nan)
    via_jump = np.zeros(n, dtype=bool)
    for step in range(1, n_steps + 1):
        idx = np.flatnonzero(alive)
        x[idx] += drift + sigma * np.sqrt(dt) * rng.standard_normal(idx.size)
        hit = idx[x[idx] <= 0.0]
        tau[hit], ratio[hit], alive[hit] = step * dt, 1.0, False
        idx = np.flatnonzero(alive)
        n_j = rng.poisson(lam * dt, idx.size)
        if n_j.sum() == 0:
            continue
        sizes = kou_jump_sizes(int(n_j.sum()), p, eta1, eta2, rng)
        x[idx] += np.bincount(np.repeat(np.arange(idx.size), n_j), weights=sizes,
                              minlength=idx.size)
        hit = idx[x[idx] <= 0.0]                       # alive after diffusion, so jump-driven
        tau[hit], ratio[hit], alive[hit] = step * dt, np.exp(x[hit]), False
        via_jump[hit] = True
    return {"default": ~alive, "tau": tau, "via_jump": via_jump, "ratio": ratio}


# ---- Sanity check 3: short-maturity jump-to-default intensity and the exponential undershoot
kou = dict(V0=1.5, barrier=1.0, mu=0.05, sigma=0.25, lam=0.5, p=0.4, eta1=10.0, eta2=4.0)
lam_jtd = kou["lam"] * (1 - kou["p"]) * (kou["barrier"] / kou["V0"]) ** kou["eta2"]
assert abs(lam_jtd - 0.059) < 1e-3                                  # table in 5.3.3
short = simulate_kou_jd(**kou, T=1 / 52, n_steps=4, n=2_000_000)
assert abs(short["default"].mean() * 52 / lam_jtd - 1) < 0.10
assert short["via_jump"].sum() >= 0.99 * short["default"].sum()    # diffusion can't get there in a week
undershoot = short["ratio"][short["via_jump"]].mean()
assert abs(undershoot - kou["eta2"] / (1 + kou["eta2"])) < 0.025

# PD-LGD correlation for free: fatter down-jumps raise PD and lower V_tau/B together
runs = {e2: simulate_kou_jd(**{**kou, "eta2": e2}, T=1.0, n_steps=52, n=200_000)
        for e2 in (4.0, 2.0)}
pd_by = {e2: r["default"].mean() for e2, r in runs.items()}
und_by = {e2: r["ratio"][r["via_jump"]].mean() for e2, r in runs.items()}
assert pd_by[2.0] > pd_by[4.0] and und_by[2.0] < und_by[4.0], (pd_by, und_by)
```


### Listing 5.4: Hill tail index and peaks-over-threshold VaR and ES {#code-5-4}

```python
# credit_mixture_lab.py, block 4 of 5: Hill and peaks-over-threshold, with a bounded-support refusal.
def hill_estimator(x, k, support_max=None, tol=1e-3):
    """Hill tail index from the top k positive losses. Returns nan (and warns) when the
    sample maximum sits at a declared support bound: that tail is a lump, not a power law."""
    x = np.sort(np.asarray(x, dtype=float))[::-1]
    x = x[x > 0]
    if not 1 <= k < x.size:
        raise ValueError("need 1 <= k < number of positive losses")
    if support_max is not None and x[0] >= support_max - tol:
        warnings.warn("bounded support: sample maximum at the cap; EVT not applicable")
        return np.nan
    return 1.0 / np.mean(np.log(x[:k] / x[k]))


def hill_table(x, ks, **kw):
    return pd.Series({k: hill_estimator(x, k, **kw) for k in ks}, name="alpha_hat")


def gpd_var_es(x, u, p):
    """POT VaR and ES (as losses) at confidence p from losses x over threshold u."""
    x = np.asarray(x, dtype=float)
    exc = x[x > u] - u
    if exc.size < 50:
        raise ValueError("fewer than 50 exceedances: lower u or get more data")
    xi, _, beta_gpd = stats.genpareto.fit(exc, floc=0.0)
    if xi >= 1.0:
        raise ValueError("xi >= 1: expected shortfall is infinite")
    tail = x.size / exc.size * (1.0 - p)
    if not 0.0 < tail < 1.0:
        raise ValueError("p must lie beyond the threshold's empirical level")
    if abs(xi) < 1e-6:
        var = u - beta_gpd * np.log(tail)              # exponential-tail limit
    else:
        var = u + beta_gpd / xi * (tail ** (-xi) - 1.0)
    return {"xi": xi, "beta_gpd": beta_gpd, "VaR": var,
            "ES": (var + beta_gpd - xi * u) / (1.0 - xi)}


# ---- Sanity check 4: Hill finds alpha = 3 in t(3); refuses, and drifts, on the bounded bond
t3 = np.random.default_rng(SEED).standard_t(3, size=500_000)
alphas = hill_table(t3, [500, 1000, 2000])
assert alphas.between(2.5, 3.5).all(), alphas
pot = gpd_var_es(t3, np.quantile(t3, 0.99), 0.999)
var_true = stats.t.ppf(0.999, 3)
es_true = stats.t.pdf(var_true, 3) / 0.001 * (3 + var_true**2) / 2
assert 0.2 < pot["xi"] < 0.5
assert abs(pot["VaR"] / var_true - 1) < 0.10 and abs(pot["ES"] / es_true - 1) < 0.15

loss = -ret                                            # Theo's bond, from block 1
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    refused = hill_estimator(loss, 1000, support_max=1.0)
assert np.isnan(refused) and any("bounded support" in str(w.message) for w in caught)
drift = hill_table(loss, [1000, 5000, 20000])
assert drift.max() / drift.min() > 3.0, drift          # no plateau, only a cliff
```


### Listing 5.5: Tail dependence of the t copula, the limit against the finite level {#code-5-5}

```python
# credit_mixture_lab.py, block 5 of 5: tail dependence, the limit vs. the finite level.
def t_copula_tail_dep(rho, nu):
    """Coefficient of (upper = lower) tail dependence lambda_U of a bivariate t copula."""
    if not (-1.0 < rho < 1.0 and nu > 0):
        raise ValueError("need -1 < rho < 1 and nu > 0")
    return 2.0 * stats.t.cdf(-np.sqrt((nu + 1.0) * (1.0 - rho) / (1.0 + rho)), df=nu + 1.0)


def simulate_copula_pairs(rho, nu, n, seed=SEED):
    """(n, 2) draws with t (finite nu) or Gaussian (nu = inf) dependence."""
    rng = np.random.default_rng(seed)
    chol = np.linalg.cholesky(np.array([[1.0, rho], [rho, 1.0]]))
    g = rng.standard_normal((n, 2)) @ chol.T
    return g if np.isinf(nu) else g * np.sqrt(nu / rng.chisquare(nu, n))[:, None]


def conditional_exceedance(z, level):
    """chi_hat(level) = Pr(Z2 above its level-quantile | Z1 above its level-quantile)."""
    first = z[:, 0] > np.quantile(z[:, 0], level)
    return np.mean(z[first, 1] > np.quantile(z[:, 1], level))


# ---- Sanity check 5: the t copula keeps tail dependence; the Gaussian loses it only in the limit
lam_t = t_copula_tail_dep(0.5, 4.0)
assert 0.2 < lam_t < 0.3 and t_copula_tail_dep(0.5, 1e4) < 1e-6
chi_t = conditional_exceedance(simulate_copula_pairs(0.5, 4.0, 2_000_000), 0.999)
chi_g = conditional_exceedance(simulate_copula_pairs(0.5, np.inf, 2_000_000), 0.999)
assert abs(chi_t - lam_t) < 0.08 and 0.0 < chi_g < chi_t - 0.08, (lam_t, chi_t, chi_g)
print(f"lambda_U(t4, rho=0.5) = {lam_t:.3f}; chi_hat(0.999): t = {chi_t:.3f}, Gaussian = {chi_g:.3f}")
```


## F.6: Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks {#code-6}

Listings from `06_ch06_merton_and_intensity_models.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 6.1: The PASS/FAIL helper and the shared seed {#code-6-1}

```python
# Block 0: imports, seed, and the PASS/FAIL helper
import warnings
import numpy as np
from scipy.stats import norm, spearmanr
from scipy.optimize import fsolve, brentq

rng = np.random.default_rng(42)


def check(label, ok, detail=""):
    """Print PASS/FAIL and stop the run on failure."""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}  {detail}")
    assert ok, label
```


### Listing 6.2: Merton (1974): equity, debt, spread and the Q and P default probabilities {#code-6-2}

```python
# Block 1: Merton (1974)
def _d1d2(V0, F, r, sigma_V, T):
    V0, F, T = np.asarray(V0, float), np.asarray(F, float), np.asarray(T, float)
    sigma_V = np.clip(np.asarray(sigma_V, float), 1e-4, 5.0)
    if np.any(V0 <= 0) or np.any(F <= 0) or np.any(T <= 0):
        raise ValueError("V0, F and T must be strictly positive")
    srt = sigma_V * np.sqrt(T)
    d1 = (np.log(V0 / F) + (r + 0.5 * sigma_V**2) * T) / srt
    return d1, d1 - srt


def merton_prices(V0, F, r, sigma_V, T):
    """Q-measure Merton. Returns (E0, B0, spread, pd_Q); spread is decimal, continuously compounded."""
    d1, d2 = _d1d2(V0, F, r, sigma_V, T)
    T = np.asarray(T, float)
    disc_F = F * np.exp(-r * T)
    E0 = V0 * norm.cdf(d1) - disc_F * norm.cdf(d2)
    B0 = disc_F * norm.cdf(d2) + V0 * norm.cdf(-d1)
    put_frac = norm.cdf(-d2) - V0 * norm.cdf(-d1) / disc_F          # put / (F e^{-rT}), >= 0
    spread = -np.log1p(-np.maximum(put_frac, 0.0)) / T
    return E0, B0, spread, norm.cdf(-d2)


def merton_pd_P(V0, F, mu, sigma_V, T):
    """P-measure distance to default and PD at horizon T."""
    sigma_V = np.clip(np.asarray(sigma_V, float), 1e-4, 5.0)
    T = np.asarray(T, float)
    dd = (np.log(np.asarray(V0, float) / F) + (mu - 0.5 * sigma_V**2) * T) / (sigma_V * np.sqrt(T))
    return dd, norm.cdf(-dd)


V0, F, r, sV, T = 100.0, 80.0, 0.04, 0.25, 1.0
E0, B0, s1, pdQ = map(float, merton_prices(V0, F, r, sV, T))
dd_P, pd_P = map(float, merton_pd_P(V0, F, 0.08, sV, T))
print(f"E0={E0:.4f}  B0={B0:.4f}  s={1e4 * s1:.1f} bp  PD_Q={pdQ:.4f}  DD_P={dd_P:.3f}  PD_P={pd_P:.4f}")
check("A: E0 + B0 = V0", abs(E0 + B0 - V0) < 1e-10, f"err={abs(E0 + B0 - V0):.1e}")

n_half = 100_000
z = rng.standard_normal(n_half)
z = np.concatenate([z, -z])                                            # antithetic pairs
VT = V0 * np.exp((r - 0.5 * sV**2) * T + sV * np.sqrt(T) * z)
pay = np.exp(-r * T) * np.minimum(VT, F)
pair = 0.5 * (pay[:n_half] + pay[n_half:])
mc, se = pair.mean(), pair.std(ddof=1) / np.sqrt(n_half)
check("B: MC debt within 3 SE of closed form", abs(mc - B0) < 3 * se,
      f"MC={mc:.4f} CF={B0:.4f} SE={se:.4f}")

s_short = float(merton_prices(V0, F, r, sV, 1e-3)[2])
check("C: Merton short-end spread -> 0", abs(s_short) < 1e-8, f"s(0.001y)={s_short:.1e}")
```


### Listing 6.3: The KMV inverse problem: asset value and volatility from equity {#code-6-3}

```python
# Block 2: KMV inverse problem
def merton_equity_vol(V0, F, r, sigma_V, T):
    """Equity value and the Ito-implied equity volatility sigma_E = N(d1) sigma_V V0 / E0."""
    d1, _ = _d1d2(V0, F, r, sigma_V, T)
    E = merton_prices(V0, F, r, sigma_V, T)[0]
    return E, norm.cdf(d1) * np.asarray(sigma_V, float) * V0 / E


def solve_kmv(E0, sigma_E, F, r, T=1.0):
    """Solve E0 = C(V0, sigma_V) and sigma_E E0 = N(d1) sigma_V V0 on log-parameters."""
    if not (0.05 <= sigma_E <= 3.0):
        raise ValueError(f"sigma_E={sigma_E} outside [5%, 300%]: is it annualized?")
    sq, disc_F = np.sqrt(T), F * np.exp(-r * T)

    def resid(zz):
        V, s = np.exp(zz)
        d1, d2 = _d1d2(V, F, r, s, T)
        return np.array([(V * norm.cdf(d1) - disc_F * norm.cdf(d2)) / E0 - 1.0,
                         norm.cdf(d1) * s * V / (sigma_E * E0) - 1.0])

    def jac(zz):
        V, s = np.exp(zz)
        d1, d2 = _d1d2(V, F, r, s, T)
        Nd1, nd1 = norm.cdf(d1), norm.pdf(d1)
        return np.array([[V * Nd1 / E0, s * V * nd1 * sq / E0],
                         [(s * V * Nd1 + V * nd1 / sq) / (sigma_E * E0),
                          s * V * (Nd1 - nd1 * d2) / (sigma_E * E0)]])

    V_init = E0 + disc_F
    z0 = np.log([V_init, max(sigma_E * E0 / V_init, 0.01)])
    zz = fsolve(resid, z0, fprime=jac, xtol=1e-10)
    V, s = np.exp(zz)
    if np.max(np.abs(resid(zz))) > 1e-9 or not (0.01 <= s <= 3.0) or V < E0:
        raise RuntimeError(f"KMV solve failed: V={V:.4g}, sigma_V={s:.4g}; fall back to naive DD and flag")
    return float(V), float(s)


def invert_equity(E, F, r, sigma_V, T, tol=1e-12, max_iter=100):
    """Vectorized Newton for V with C(V) = E. C is increasing and convex in V, so Newton
    started right of the root (V = E + F e^{-rT}) converges monotonically."""
    E = np.asarray(E, float)
    disc_F = F * np.exp(-r * T)
    V = E + disc_F
    for _ in range(max_iter):
        d1, d2 = _d1d2(V, F, r, sigma_V, T)
        step = (V * norm.cdf(d1) - disc_F * norm.cdf(d2) - E) / np.maximum(norm.cdf(d1), 1e-12)
        V = V - step
        if np.max(np.abs(step) / V) < tol:
            return V
    raise RuntimeError("equity inversion did not converge")


def kmv_iterate(E_series, F, r, T=1.0, periods_per_year=52, tol=1e-6, max_iter=100):
    """Vasicek-Kealhofer iteration. Returns (implied asset path, sigma_V, iterations)."""
    E = np.asarray(E_series, float)
    sig_E = np.std(np.diff(np.log(E)), ddof=1) * np.sqrt(periods_per_year)
    sig = max(sig_E * E[-1] / (E[-1] + F * np.exp(-r * T)), 0.01)
    for it in range(1, max_iter + 1):
        V = invert_equity(E, F, r, sig, T)
        sig_new = np.std(np.diff(np.log(V)), ddof=1) * np.sqrt(periods_per_year)
        if abs(sig_new - sig) < tol:
            return V, float(sig_new), it
        sig = sig_new
    raise RuntimeError("VK iteration did not converge")


def naive_dd(E0, sigma_E, F, mu, T=1.0):
    """Bharath-Shumway (2008) naive distance to default (P-measure; mu = past equity return)."""
    w = E0 / (E0 + F)
    sig_V = w * sigma_E + (1.0 - w) * (0.05 + 0.25 * sigma_E)
    return (np.log((E0 + F) / F) + (mu - 0.5 * sig_V**2) * T) / (sig_V * np.sqrt(T))


E_true, sE_true = map(float, merton_equity_vol(V0, F, r, sV, T))
V_hat, sV_hat = solve_kmv(E_true, sE_true, F, r, T)
err_D = max(abs(V_hat / V0 - 1.0), abs(sV_hat / sV - 1.0))
check("D1: KMV round trip recovers (V0, sigma_V)", err_D < 1e-6,
      f"sigma_E={sE_true:.3f} -> V0={V_hat:.6f}, sigma_V={sV_hat:.6f}")

n_weeks, dt_w = 156, 1.0 / 52
steps = (0.08 - 0.5 * sV**2) * dt_w + sV * np.sqrt(dt_w) * rng.standard_normal(n_weeks - 1)
V_path = V0 * np.exp(np.concatenate([[0.0], np.cumsum(steps)]))
E_path = merton_prices(V_path, F, r, sV, T)[0]
_, sV_vk, n_it = kmv_iterate(E_path, F, r, T)
check("D2: VK iteration recovers sigma_V", abs(sV_vk - sV) < 0.05,
      f"sigma_V={sV_vk:.4f} after {n_it} iterations")

F_x = rng.uniform(10.0, 90.0, 200)
sV_x = rng.uniform(0.10, 0.50, 200)
E_x, sE_x = merton_equity_vol(V0, F_x, r, sV_x, T)
dd_true, _ = merton_pd_P(V0, F_x, r, sV_x, T)
rho_E, _ = spearmanr(dd_true, naive_dd(E_x, sE_x, F_x, r, T))
check("E: naive DD ranks like the solved DD", rho_E > 0.8, f"Spearman={rho_E:.3f}")
```


### Listing 6.4: Black-Cox first passage: closed form and Monte Carlo {#code-6-4}

```python
# Block 3: Black-Cox first passage
def black_cox_pd(V0, K, g, mu, sigma_V, T):
    """First-passage PD by T for barrier K_t = K exp(-g (T - t)). Use mu = r - q under Q."""
    x0 = np.log(V0 / (K * np.exp(-g * T)))
    if np.any(x0 <= 0):
        raise ValueError("asset value is already at or below the barrier")
    m, srt = mu - 0.5 * sigma_V**2 - g, sigma_V * np.sqrt(T)
    second = np.exp(-2.0 * m * x0 / sigma_V**2 + norm.logcdf((-x0 + m * T) / srt))
    return norm.cdf((-x0 - m * T) / srt) + second


def black_cox_mc(V0, K, g, mu, sigma_V, T, n_paths=200_000, n_steps=12, bridge=True):
    """Monte Carlo on the log distance to the barrier, with optional Brownian-bridge correction."""
    dt = T / n_steps
    m = mu - 0.5 * sigma_V**2 - g
    x = np.full(n_paths, np.log(V0 / (K * np.exp(-g * T))))
    alive = np.ones(n_paths, dtype=bool)
    for _ in range(n_steps):                                    # the only Python loop: time steps
        x_new = x + m * dt + sigma_V * np.sqrt(dt) * rng.standard_normal(n_paths)
        hit = x_new <= 0.0
        if bridge:
            p_cross = np.exp(-2.0 * np.maximum(x, 0.0) * np.maximum(x_new, 0.0) / (sigma_V**2 * dt))
            hit |= rng.uniform(size=n_paths) < p_cross
        alive &= ~hit
        x = x_new
    pd_hat = 1.0 - alive.mean()
    return pd_hat, np.sqrt(pd_hat * (1.0 - pd_hat) / n_paths)


bc = dict(V0=100.0, K=70.0, g=0.02, mu=0.06, sigma_V=0.25, T=5.0)
pd_cf = float(black_cox_pd(**bc))
pd_br, se_br = black_cox_mc(**bc, n_steps=12, bridge=True)
pd_nv, _ = black_cox_mc(**bc, n_steps=12, bridge=False)
check("F1: bridge MC within 3 SE of closed form", abs(pd_br - pd_cf) < 3 * se_br,
      f"CF={pd_cf:.4f} bridge={pd_br:.4f} SE={se_br:.4f}")
check("F2: naive discrete monitoring is biased low", pd_nv < pd_cf, f"bias={pd_nv - pd_cf:+.4f}")

mu_zero = 0.5 * 0.25**2 + 0.02                                  # makes m = 0
x0_g = np.log(100.0 / (70.0 * np.exp(-0.02 * 5.0)))
pd_m0 = float(black_cox_pd(100.0, 70.0, 0.02, mu_zero, 0.25, 5.0))
check("G: m = 0 gives twice the terminal PD",
      abs(pd_m0 - 2.0 * norm.cdf(-x0_g / (0.25 * np.sqrt(5.0)))) < 1e-12, f"PD={pd_m0:.6f}")
```


### Listing 6.5: CIR intensity: closed-form survival and an exact simulation {#code-6-5}

```python
# Block 4: CIR intensity
def cir_survival(lam0, kappa, theta, sigma, T):
    """Closed-form Q-survival S(0,T) = A(T) exp(-B(T) lam0)."""
    eta = np.sqrt(kappa**2 + 2.0 * sigma**2)
    e = np.expm1(eta * T)
    den = (eta + kappa) * e + 2.0 * eta
    B = 2.0 * e / den
    A = (2.0 * eta * np.exp(0.5 * (kappa + eta) * T) / den) ** (2.0 * kappa * theta / sigma**2)
    return A * np.exp(-B * lam0)


def cir_mc(lam0, kappa, theta, sigma, T, n_paths=50_000, n_steps=100):
    """Exact noncentral chi-square transitions; trapezoid rule for the integrated intensity."""
    if 2.0 * kappa * theta < sigma**2:
        raise ValueError("Feller condition violated: 2 kappa theta < sigma^2")
    dt = T / n_steps
    c = sigma**2 * (1.0 - np.exp(-kappa * dt)) / (4.0 * kappa)
    dof = 4.0 * kappa * theta / sigma**2
    lam = np.full(n_paths, float(lam0))
    integral = np.zeros(n_paths)
    for _ in range(n_steps):
        lam_new = c * rng.noncentral_chisquare(dof, lam * np.exp(-kappa * dt) / c)
        integral += 0.5 * (lam + lam_new) * dt
        lam = lam_new
    disc = np.exp(-integral)
    return disc.mean(), disc.std(ddof=1) / np.sqrt(n_paths)


def cir_euler_negative_share(lam0, kappa, theta, sigma, T, n_paths=20_000, n_steps=260):
    """Diagnostic only: share of naive-Euler paths that visit lambda < 0."""
    dt = T / n_steps
    lam = np.full(n_paths, float(lam0))
    went_negative = np.zeros(n_paths, dtype=bool)
    for _ in range(n_steps):
        shock = sigma * np.sqrt(np.maximum(lam, 0.0) * dt) * rng.standard_normal(n_paths)
        lam = lam + kappa * (theta - lam) * dt + shock
        went_negative |= lam < 0.0
    return went_negative.mean()


cir = dict(lam0=0.03, kappa=0.5, theta=0.04, sigma=0.10, T=5.0)
S_cf = float(cir_survival(**cir))
S_mc, se_cir = cir_mc(**cir)
check("H: CIR closed form vs exact-sampling MC", abs(S_mc - S_cf) < 3 * se_cir,
      f"CF={S_cf:.5f} MC={S_mc:.5f} SE={se_cir:.5f}")
print(f"Euler paths visiting lambda<0 with sigma=0.30 (Feller fails): "
      f"{cir_euler_negative_share(0.03, 0.5, 0.04, 0.30, 5.0):.1%}")
```


### Listing 6.6: CDS legs, hazard bootstrap and the credit triangle {#code-6-6}

```python
# Block 5: CDS legs, hazard bootstrap, credit triangle
def cum_hazard(t, knots, lams):
    """Integrated piecewise-constant hazard; lams[k] applies on (knots[k-1], knots[k]], flat beyond."""
    t = np.atleast_1d(np.asarray(t, float))
    knots, lams = np.asarray(knots, float), np.asarray(lams, float)
    lo = np.concatenate(([0.0], knots[:-1]))
    hi = knots.copy()
    hi[-1] = np.inf
    overlap = np.clip(np.minimum(t[:, None], hi[None, :]) - lo[None, :], 0.0, None)
    return overlap @ lams


def cds_legs(knots, lams, T, c, R, discount, freq=4, n_sub=12):
    """Returns (pv_premium, pv_protection, rpv01) per unit notional. T must be a multiple of 1/freq."""
    pay = np.arange(1, int(round(T * freq)) + 1) / freq
    prev = np.concatenate(([0.0], pay[:-1]))
    S_pay = np.exp(-cum_hazard(pay, knots, lams))
    S_prev = np.exp(-cum_hazard(prev, knots, lams))
    rpv01 = np.sum((pay - prev) * discount(pay) * (S_pay + 0.5 * (S_prev - S_pay)))
    grid = np.linspace(0.0, T, int(round(T * freq * n_sub)) + 1)
    S_g = np.exp(-cum_hazard(grid, knots, lams))
    pv_prot = (1.0 - R) * np.sum(discount(0.5 * (grid[1:] + grid[:-1])) * (S_g[:-1] - S_g[1:]))
    return c * rpv01, pv_prot, rpv01


def par_spread(knots, lams, T, R, discount):
    _, prot, rpv01 = cds_legs(knots, lams, T, 1.0, R, discount)
    return prot / rpv01


def bootstrap_hazard(tenors, spreads_bp, R, discount):
    """Sequential Brent bootstrap. Negative buckets are flagged and warned, never silently floored."""
    tenors = np.asarray(tenors, float)
    s = np.asarray(spreads_bp, float) / 1e4
    lams = np.zeros(tenors.size)
    negative = np.zeros(tenors.size, dtype=bool)
    for k in range(tenors.size):
        def err(lk, k=k):
            trial = lams.copy()
            trial[k] = lk
            return par_spread(tenors, trial, tenors[k], R, discount) - s[k]
        lams[k] = brentq(err, -1.0, 5.0, xtol=1e-14)
        if lams[k] < 0.0:
            negative[k] = True
            warnings.warn(f"negative hazard {lams[k]:.4f} on bucket ending {tenors[k]}y: check quotes/recovery")
    return lams, negative


def credit_triangle(s, R):
    return s / (1.0 - R)


disc4 = lambda t: np.exp(-0.04 * np.asarray(t, float))
disc0 = lambda t: np.ones_like(np.asarray(t, float))
ten = np.array([1.0, 3.0, 5.0, 7.0, 10.0])
quotes = np.array([150.0, 210.0, 260.0, 290.0, 310.0])
lam_k, neg_k = bootstrap_hazard(ten, quotes, 0.4, disc4)
reprice = max(abs(par_spread(ten, lam_k, T_k, 0.4, disc4) - q / 1e4) for T_k, q in zip(ten, quotes))
check("I: bootstrap reprices every quote", reprice < 1e-8 and not neg_k.any(),
      f"max err={reprice:.1e}; lambdas={np.round(lam_k, 5)}")

tri = credit_triangle(0.03, 0.4)
lam_f0, _ = bootstrap_hazard([5.0], [300.0], 0.4, disc0)
lam_f4, _ = bootstrap_hazard([5.0], [300.0], 0.4, disc4)
check("J1: credit triangle exact with flat discounting", abs(lam_f0[0] - tri) < 2e-4,
      f"lambda={lam_f0[0]:.5f} vs s/(1-R)={tri:.5f}")
check("J2: credit triangle approximate with r = 4%", abs(lam_f4[0] - tri) < 1e-3,
      f"lambda={lam_f4[0]:.5f} (discrete coupons paid in arrears)")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    lam_inv, neg_inv = bootstrap_hazard([1.0, 3.0, 5.0], [1500.0, 300.0, 250.0], 0.4, disc4)
check("K: inverted curve trips the negative-hazard flag", bool(neg_inv.any()),
      f"lambdas={np.round(lam_inv, 4)}")
```


### Listing 6.7: The structural short end, seen through the CDS bootstrap {#code-6-7}

```python
# Block 6: the structural short end, seen through the CDS bootstrap
ten_m = np.array([0.05, 0.25, 1.0, 3.0, 5.0, 7.0, 10.0])
s_m = merton_prices(V0, F, r, sV, ten_m)[2]
for T_k, s_k in zip(ten_m, s_m):
    print(f"  Merton T={T_k:5.2f}y  s={1e4 * s_k:7.1f} bp")
peak = int(np.argmax(s_m))
check("L: structural short end ~0 and hump-shaped curve",
      s_m[0] < 0.05 * s_m.max() and 0 < peak < ten_m.size - 1,
      f"s(0.05y)={1e4 * s_m[0]:.2f} bp, peak at {ten_m[peak]}y")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    lam_m, neg_m = bootstrap_hazard(ten_m[2:], 1e4 * s_m[2:], 0.4, disc4)
print("CDS-style hazards implied by Merton spreads (R = 40% convention):", np.round(lam_m, 4),
      "| negative buckets:", neg_m)
print("All chapter 6 checks passed.")
```


## F.6-B: Chapter 6-B: Options for Credit People: Replication, Black–Scholes, Greeks, Jump-to-Default and the Two Measures {#code-6b}

Listings from `06_ch06b_options_and_measures_for_credit.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 6-B.1: credit_options.py: Black-Scholes, Greeks and jump-to-default pricing under the two measures {#code-6b-1}

```python
"""credit_options.py (Chapter 6-B). Units as in the spec; every PD is measure-tagged."""
import math
from dataclasses import dataclass

import numpy as np

SQRT2 = math.sqrt(2.0)
EPS_T = 1e-10                 # below this an option is at expiry
VOL_LO, VOL_HI = 1e-4, 10.0   # implied-vol bracket
MEASURES = ("P", "Q", "Q_nominal")


def norm_cdf(x):
    """N(x) via erfc, accurate in the far left tail where 1 - N(-x) is not."""
    return 0.5 * math.erfc(-x / SQRT2)


def norm_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_ppf(p, lo=-12.0, hi=12.0):
    """Inverse normal CDF by bisection: slow, monotone, and never wrong by much."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must lie in (0, 1)")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _d1_d2(S, K, T, sigma, rate):
    sig_rt = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (rate + 0.5 * sigma * sigma) * T) / sig_rt
    return d1, d1 - sig_rt


def bs_price(S, K, T, sigma, rate, kind="call"):
    """Black-Scholes European price. `rate` may be r, or r + lambda (6B.1)."""
    if S <= 0.0 or K <= 0.0:
        raise ValueError("S and K must be positive; default states belong to jtd_price")
    disc_K = K * math.exp(-rate * T)
    if T < EPS_T or sigma * math.sqrt(T) < 1e-12:       # zero-vol limit
        fwd = S - disc_K
        return max(fwd, 0.0) if kind == "call" else max(-fwd, 0.0)
    d1, d2 = _d1_d2(S, K, T, sigma, rate)
    if kind == "call":
        return S * norm_cdf(d1) - disc_K * norm_cdf(d2)
    if kind == "put":
        return disc_K * norm_cdf(-d2) - S * norm_cdf(-d1)
    raise ValueError("kind must be 'call' or 'put'")


def bs_greeks(S, K, T, sigma, rate, kind="call"):
    """Delta, gamma, vega (per 1.00 vol), theta (per year), rho (per 1.00 rate)."""
    if T < EPS_T:
        raise ValueError("Greeks undefined at expiry: report intrinsic and a JTD line")
    d1, d2 = _d1_d2(S, K, T, sigma, rate)
    pdf1, rt = norm_pdf(d1), math.sqrt(T)
    disc_K = K * math.exp(-rate * T)
    out = {"gamma": pdf1 / (S * sigma * rt), "vega": S * pdf1 * rt}
    decay = -S * pdf1 * sigma / (2.0 * rt)
    if kind == "call":
        out.update(delta=norm_cdf(d1), theta=decay - rate * disc_K * norm_cdf(d2),
                   rho=T * disc_K * norm_cdf(d2))
    else:
        out.update(delta=-norm_cdf(-d1), theta=decay + rate * disc_K * norm_cdf(-d2),
                   rho=-T * disc_K * norm_cdf(-d2))
    return out


def implied_vol(price, S, K, T, rate, kind="call", tol_price=1e-6, max_iter=100):
    """Safeguarded Newton. Returns (sigma, status); status is 'ok' or a reason."""
    disc_K = K * math.exp(-rate * T)
    lower = max(S - disc_K, 0.0) if kind == "call" else max(disc_K - S, 0.0)
    upper = S if kind == "call" else disc_K
    if not lower < price < upper:
        return float("nan"), "outside no-arbitrage bounds (stale, American, borrow or crossed)"
    lo, hi = VOL_LO, VOL_HI
    if bs_price(S, K, T, hi, rate, kind) < price:
        return float("nan"), "price needs a vol above VOL_HI"
    sigma = min(max(math.sqrt(2.0 * math.pi / T) * price / S, 0.05), 3.0)  # Brenner-Subrahmanyam
    for _ in range(max_iter):
        diff = bs_price(S, K, T, sigma, rate, kind) - price
        if abs(diff) < tol_price:
            return sigma, "ok"
        if diff > 0.0:
            hi = sigma
        else:
            lo = sigma
        vega = bs_greeks(S, K, T, sigma, rate, kind)["vega"]
        step = sigma - diff / vega if vega > 1e-12 else -1.0
        sigma = step if lo < step < hi else 0.5 * (lo + hi)
    return sigma, "max_iter reached"


@dataclass(frozen=True)
class MeasuredPD:
    """A cumulative default probability that always knows its measure (Law 4)."""
    value: float
    measure: str
    horizon: float

    def __post_init__(self):
        if self.measure not in MEASURES:
            raise ValueError(f"measure must be one of {MEASURES}")
        if not 0.0 <= self.value < 1.0 or self.horizon <= 0.0:
            raise ValueError("need 0 <= PD < 1 and a positive horizon")

    def hazard(self):
        return -math.log1p(-self.value) / self.horizon

    def to_q(self, xi, source):
        """P -> Q through (6B.4), S^Q = (S^P)**xi. Refuses to convert twice."""
        if self.measure != "P":
            raise ValueError("only a P probability converts; this one already holds a premium")
        if xi <= 0.0 or not source:
            raise ValueError("xi must be positive and sourced")
        return MeasuredPD(1.0 - (1.0 - self.value) ** xi, "Q", self.horizon)


def merton(V, F, T, sigma_V, r):
    """Merton (1974): debt = riskless bond - put on assets (sections 6.2, 6-B.3.4)."""
    put = bs_price(V, F, T, sigma_V, r, "put")
    g = bs_greeks(V, F, T, sigma_V, r, "put")
    d1, d2 = _d1_d2(V, F, T, sigma_V, r)
    riskless = F * math.exp(-r * T)
    B = riskless - put
    return {"E": V - B, "B": B, "put": put, "spread": -math.log(B / riskless) / T,
            "pd": MeasuredPD(norm_cdf(-d2), "Q", T),
            "bond_delta": -g["delta"], "bond_gamma": -g["gamma"],
            "bond_vega_per_pt": -g["vega"] / 100.0,
            "spread_vega_bp_per_pt": g["vega"] / (B * T) * 100.0,
            "bond_per_equity": norm_cdf(-d1) / norm_cdf(d1)}


def urc_eur(T, r, lam):
    """European unit recovery claim: $1 at T if default by T."""
    return math.exp(-r * T) * (1.0 - math.exp(-lam * T))


def urc_am(T, r, lam):
    """Unit recovery claim paid at default: the American corridor claim (23.3)."""
    if r + lam <= 0.0:
        return lam * T
    return lam / (r + lam) * (1.0 - math.exp(-(r + lam) * T))


def jtd_price(S, K, T, sigma, r, lam, kind="call"):
    """Merton (1976) with one jump to zero at Q-intensity lam (6B.1)."""
    if kind == "call":
        return bs_price(S, K, T, sigma, r + lam, "call")
    return K * urc_eur(T, r, lam) + bs_price(S, K, T, sigma, r + lam, "put")


def corridor_leak(S, A, B, T, sigma, r, lam):
    """epsilon(A, B) in (6B.2): the diffusive part of a put spread per unit width."""
    upper = bs_price(S, B, T, sigma, r + lam, "put")
    lower = bs_price(S, A, T, sigma, r + lam, "put") if A > 0.0 else 0.0
    return (upper - lower) / (B - A)


def corridor_leak_bound(S, B, T, sigma, r, lam):
    _, d2 = _d1_d2(S, B, T, sigma, r + lam)
    return math.exp(-(r + lam) * T) * norm_cdf(-d2)


def hazard_from_put(put_price, S, K, T, sigma, r, american=True, lam_hi=5.0):
    """Q-intensity of equity wipe-out from a low-strike put (6-B.8): put/K = U(lam)
    + diffusive put at r + lam over K. American early exercise of the diffusive
    part is ignored. The right side increases in lam, so bisection is safe."""
    urc = urc_am if american else urc_eur

    def gap(lam):
        return urc(T, r, lam) + bs_price(S, K, T, sigma, r + lam, "put") / K - put_price / K

    lo, hi = 0.0, lam_hi
    if gap(lo) > 0.0:
        raise ValueError("put is cheaper than its diffusive part: check vol, borrow, quote")
    if gap(hi) < 0.0:
        raise ValueError("put implies a hazard above lam_hi")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gap(mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def wing_floor_vol(S, K, T, r, lam):
    """Lower bound (6B.3) on the BS implied vol of a put on a defaultable stock."""
    L = math.log(S * math.exp(r * T) / K)
    if L <= 0.0:
        return 0.0
    c = norm_ppf(math.exp(-lam * T))
    return (-c + math.sqrt(c * c + 2.0 * L)) / math.sqrt(T)


def jump_hedge_ratio(f_S, f_alive, f_dead, S, sigma, lam_P):
    """Min-variance share hedge under P (section 6-B.5.6). Takes lam_P, not lam_Q."""
    j = (f_alive - f_dead) / S
    w = sigma * sigma + lam_P
    delta = (sigma * sigma * f_S + lam_P * j) / w
    resid_var = sigma * sigma * lam_P / w * S * S * (f_S - j) ** 2
    return delta, resid_var


def spread_decomposition(s, lam_Q, lam_P, L_P):
    """(6B.5) in decimals per year; the market's L^Q is implied as s / lam_Q."""
    L_Q = s / lam_Q
    parts = {"expected_loss": lam_P * L_P,
             "hazard_premium": (lam_Q - lam_P) * L_P,
             "recovery_premium": lam_Q * (L_Q - L_P)}
    assert abs(sum(parts.values()) - s) < 1e-12
    parts.update(L_Q=L_Q, xi=lam_Q / lam_P, premium_ratio=s / (lam_P * L_P))
    return parts


def harvest_sharpe(xi, lam_P):
    """(6B.6): single-name Sharpe of selling protection, Poisson approximation."""
    return (xi - 1.0) * math.sqrt(lam_P)


def mc_jtd_put(S, K, T, sigma, r, lam, n_paths=400_000, seed=6):
    """Seeded Monte Carlo of the jump put under Q; returns (price, standard error)."""
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n_paths)
    if lam > 0.0:
        alive = rng.exponential(1.0 / lam, n_paths) > T
    else:
        alive = np.ones(n_paths, dtype=bool)
    s_T = S * np.exp((r + lam - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z) * alive
    pay = math.exp(-r * T) * np.maximum(K - s_T, 0.0)
    return float(pay.mean()), float(pay.std(ddof=1) / math.sqrt(n_paths))


def _self_test():
    # 1. Put-call parity: the model-free check of the pricer.
    c = bs_price(100.0, 90.0, 1.0, 0.3, 0.04, "call")
    p = bs_price(100.0, 90.0, 1.0, 0.3, 0.04, "put")
    assert abs((c - p) - (100.0 - 90.0 * math.exp(-0.04))) < 1e-10
    # 2. The section 6.2.4 firm and its CCC cousin (table in 6-B.3.4).
    bb = merton(100.0, 80.0, 1.0, 0.25, 0.04)
    assert abs(bb["E"] - 24.78) < 0.02 and abs(bb["spread"] * 1e4 - 216.0) < 1.0
    assert abs(bb["spread_vega_bp_per_pt"] - 26.5) < 0.2
    ccc = merton(100.0, 95.0, 1.0, 0.40, 0.04)
    assert abs(ccc["spread"] * 1e4 - 1307.0) < 2.0 and abs(ccc["bond_per_equity"] - 0.502) < 0.005
    # 3. JTD: reduces to BS at lam = 0, keeps parity, and its floor is the URC.
    assert abs(jtd_price(100, 80, 1.0, 0.3, 0.04, 0.0, "put") - bs_price(100, 80, 1.0, 0.3, 0.04, "put")) < 1e-12
    cj = jtd_price(100, 80, 1.0, 0.3, 0.04, 0.05, "call")
    pj = jtd_price(100, 80, 1.0, 0.3, 0.04, 0.05, "put")
    assert abs((cj - pj) - (100.0 - 80.0 * math.exp(-0.04))) < 1e-10
    assert abs(jtd_price(100, 1.0, 1.0, 0.3, 0.04, 0.05, "put") - urc_eur(1.0, 0.04, 0.05)) < 1e-6
    # 4. Implied vols of jump puts round-trip and respect the wing floor (6B.3).
    for K in (40.0, 60.0, 100.0):
        target = jtd_price(100.0, K, 1.0, 0.3, 0.04, 0.05, "put")
        iv, status = implied_vol(target, 100.0, K, 1.0, 0.04, "put")
        assert status == "ok" and iv >= wing_floor_vol(100.0, K, 1.0, 0.04, 0.05) - 1e-9
    # 5. The $1 put on a $6 stock (6-B.5.4): the leak sits inside its bound.
    leak = corridor_leak(6.0, 0.0, 1.0, 1.0, 0.8, 0.04, 0.145)
    assert 0.0 <= leak <= corridor_leak_bound(6.0, 1.0, 1.0, 0.8, 0.04, 0.145)
    assert abs(leak - 0.0037) < 0.0005
    # 6. Halvorsen (6-B.8): put -> lam_Q; decomposition; the measure guard bites.
    lam_Q = hazard_from_put(0.136, 6.0, 1.0, 1.0, 0.8, 0.04, american=True)
    assert abs(lam_Q - 0.145) < 0.01
    pd_P = MeasuredPD(0.06, "P", 1.0)
    dec = spread_decomposition(0.115, 0.145, pd_P.hazard(), 0.60)
    assert abs(dec["L_Q"] - 0.793) < 0.001 and abs(dec["xi"] - 2.34) < 0.01
    try:
        MeasuredPD(0.10, "Q", 1.0).to_q(2.0, "Driessen 2005")
        raise AssertionError("a Q -> Q conversion must be refused")
    except ValueError:
        pass
    # 7. Monte Carlo agrees with (6B.1) within four standard errors.
    mc, se = mc_jtd_put(100.0, 80.0, 1.0, 0.3, 0.04, 0.05)
    assert abs(mc - jtd_price(100.0, 80.0, 1.0, 0.3, 0.04, 0.05, "put")) < 4.0 * se
    return "credit_options self-test passed"


print(_self_test())
```


## F.7: Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data {#code-7}

Listings from `07_ch07_ml_on_small_sample_credit_data.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 7.1: Fractional differentiation with a fixed-width window {#code-7-1}

```python
import numpy as np
import pandas as pd
from itertools import combinations
from scipy import special, stats

# ---------- 1. Fractional differentiation with a fixed-width window (Section 7.3) ----------
def ffd_weights(d, tau=1e-4, k_max=100_000):
    """w_0 = 1, w_k = -w_{k-1} (d - k + 1) / k, truncated once |w_k| < tau."""
    w = [1.0]
    for k in range(1, k_max):
        w_k = -w[-1] * (d - k + 1) / k
        if abs(w_k) < tau:
            break
        w.append(w_k)
    return np.array(w)

def frac_diff(x, d, tau=1e-4):
    """x_tilde_t = sum_k w_k x_{t-k}. The first K values are NaN (warm-up), never zero."""
    x = np.asarray(x, dtype=float)
    w = ffd_weights(d, tau)
    K = len(w) - 1
    out = np.full(len(x), np.nan)
    if len(x) > K:
        out[K:] = np.convolve(x, w, mode="valid")
    return out

DF_CRIT_5PCT = -2.86  # approximate Dickey-Fuller 5% critical value (constant, no trend)

def df_tstat(x):
    """t-stat of b in dx_t = a + b x_{t-1} + e_t (no augmentation lags)."""
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    dx, xl = np.diff(x), x[:-1]
    X = np.column_stack([np.ones_like(xl), xl])
    beta, *_ = np.linalg.lstsq(X, dx, rcond=None)
    resid = dx - X @ beta
    s2 = resid @ resid / (len(dx) - 2)
    return beta[1] / np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])

def min_d(x, grid=np.round(np.arange(0.0, 1.0001, 0.05), 2), tau=1e-4):
    """Smallest d whose FFD series rejects a unit root -> (d_star, memory correlation)."""
    x = np.asarray(x, dtype=float)
    for d in grid:
        xd = frac_diff(x, d, tau)
        ok = ~np.isnan(xd)
        if ok.sum() > 100 and df_tstat(xd) < DF_CRIT_5PCT:
            return float(d), float(np.corrcoef(xd[ok], x[ok])[0, 1])
    return 1.0, float("nan")

w = ffd_weights(0.5)
k = np.arange(len(w))
assert np.allclose(w, (-1.0) ** k * special.binom(0.5, k), rtol=0, atol=1e-12)  # recursion = binomial
K = len(w) - 1
assert abs(w.sum() - (-1.0) ** K * special.binom(0.5 - 1, K)) < 1e-9             # partial-sum identity
assert 0 < w.sum() < 0.1                                   # the 'memory sliver' truncation keeps
assert 250 <= len(ffd_weights(0.4, 1e-4)) - 1 <= 320       # ~280-day warm-up at tau = 1e-4
assert 45 <= len(ffd_weights(0.4, 1e-3)) - 1 <= 65         # ~54-day warm-up at tau = 1e-3
rw = np.cumsum(np.random.default_rng(1).normal(0, 0.02, 2000))   # log-spread-like random walk
assert np.allclose(frac_diff(rw, 1.0)[1:], np.diff(rw))          # d = 1 is ordinary differencing
assert df_tstat(frac_diff(rw, 1.0)) < -10 < df_tstat(rw)         # change stationary, level not
print("FFD on a random walk: d* = %.2f, memory retained rho = %.2f" % min_d(rw))
```


### Listing 7.2: A synthetic credit panel with smoothed (stale) marks {#code-7-2}

```python
# ---------- 2. Synthetic credit panel with smoothed (stale) marks (Section 7.1) ----------
def simulate_panel(n_issuers=120, T=1260, seed=11):
    rng = np.random.default_rng(seed)
    n_bonds = 1 + rng.poisson(2.0, n_issuers)                       # bonds per ultimate parent
    issuer_of = np.repeat(np.arange(n_issuers), n_bonds)
    NB = issuer_of.size
    base = np.exp(rng.uniform(np.log(0.01), np.log(0.08), n_issuers))  # 100-800bp (illustrative)
    D = rng.uniform(2.0, 8.0, NB)                                   # spread duration, years
    theta = rng.uniform(0.2, 1.0, NB)                               # mark adjustment speed; 1 = live
    basis = rng.normal(0.0, 0.05, NB)
    f, a, e = np.zeros(T), np.zeros((T, n_issuers)), np.zeros((T, NB))
    for t in range(1, T):
        f[t] = 0.995 * f[t - 1] + rng.normal(0, 0.010)             # common log-spread factor
        jump = (rng.random(n_issuers) < 0.10 / 252) * 0.5           # LMT/downgrade-style jump
        a[t] = 0.99 * a[t - 1] + rng.normal(0, 0.012, n_issuers) + jump
        e[t] = 0.95 * e[t - 1] + rng.normal(0, 0.010, NB)           # bond-level basis noise
    L_true = np.log(base)[issuer_of] + basis + f[:, None] + a[:, issuer_of] + e
    L_mark = np.empty_like(L_true)
    L_mark[0] = L_true[0]
    for t in range(1, T):                                           # partial adjustment = smoothing
        L_mark[t] = L_mark[t - 1] + theta * (L_true[t] - L_mark[t - 1])
    s_true, s_mark = np.exp(L_true), np.exp(L_mark)

    def excess(s):                                                  # carry minus D * spread change
        xs = np.zeros_like(s)
        xs[1:] = s[:-1] / 252 - D * (s[1:] - s[:-1])
        return xs

    xs_true, xs = excess(s_true), excess(s_mark)
    exit_day = np.full(NB, T + 1)
    leaves = rng.random(NB) < 0.30
    exit_day[leaves] = rng.integers(T // 4, T, leaves.sum())
    tender = rng.random(NB) < 2 / 3                                 # otherwise a distressed exchange
    for b in np.flatnonzero(leaves):
        xs[exit_day[b], b] += 0.02 if tender[b] else -0.15          # illustrative exit returns
        xs[exit_day[b] + 1:, b] = 0.0
    return dict(xs=xs, xs_true=xs_true, spread=s_mark, dts=D * s_mark, issuer_of=issuer_of,
                exit_day=exit_day, theta=theta, T=T, NB=NB, n_issuers=n_issuers)

P = simulate_panel()
stay = np.flatnonzero(P["exit_day"] > P["T"])
b_slow = stay[np.argmin(P["theta"][stay])]
lag1 = lambda x: np.corrcoef(x[1:-1], x[2:])[0, 1]
assert P["xs"][1:, b_slow].std() < 0.8 * P["xs_true"][1:, b_slow].std()   # marks understate vol
assert lag1(P["xs"][:, b_slow]) > lag1(P["xs_true"][:, b_slow]) + 0.2     # and fake autocorrelation
```


### Listing 7.3: Triple-barrier labels in DTS space with exit censoring {#code-7-3}

```python
# ---------- 3. Triple-barrier labels in DTS space with exit censoring (Section 7.4) ----------
def triple_barrier(xs, dts, issuer_of, exit_day, h=63, step=10, m_up=1.0, m_dn=1.0, sigma_rel_m=0.09):
    T, NB = xs.shape
    C = np.cumsum(xs, axis=0)                          # cumulative excess return through day t
    scale = sigma_rel_m * np.sqrt(h / 21.0)            # monthly relative vol -> horizon (21 d/month)
    cols, frames = np.arange(NB), []
    for t0 in range(0, T - h, step):                   # vertical barrier always inside the sample
        alive = exit_day > t0
        path = C[t0 + 1:t0 + h + 1] - C[t0]            # (h, NB): X(u), u = 1..h
        width = scale * dts[t0]                        # barrier half-width, decimal return
        days = np.arange(t0 + 1, t0 + h + 1)[:, None]
        hits = {"upper": path >= m_up * width, "lower": path <= -m_dn * width,
                "exit": days >= exit_day[None, :]}
        first = {name: np.where(M.any(0), M.argmax(0), h) for name, M in hits.items()}
        k_ev = np.minimum(np.minimum(first["upper"], first["lower"]), first["exit"])
        k_end = np.where(k_ev >= h, h - 1, k_ev)
        touch = np.where(k_ev >= h, "vertical",
                         np.where(first["exit"] == k_ev, "exit",
                                  np.where(first["lower"] == k_ev, "lower", "upper")))
        ret = path[k_end, cols]
        label = np.where(touch == "upper", 1, np.where(touch == "lower", -1, np.sign(ret))).astype(int)
        frames.append(pd.DataFrame({"bond": cols, "issuer": issuer_of, "t0": t0, "t1": t0 + 1 + k_end,
                                    "label": label, "ret": ret, "touch": touch})[alive])
    out = pd.concat(frames, ignore_index=True)
    out["censored"] = out["touch"].eq("exit")
    return out

labels = triple_barrier(P["xs"], P["dts"], P["issuer_of"], P["exit_day"])
assert labels["label"].isin([-1, 0, 1]).all() and (labels["t1"] > labels["t0"]).all()
assert labels.loc[labels.touch == "upper", "ret"].min() > 0 > labels.loc[labels.touch == "lower", "ret"].max()
shares = labels["touch"].value_counts(normalize=True)
assert 0.05 < shares.get("vertical", 0.0) < 0.95 and shares.get("exit", 0.0) > 0
print("touch shares:", shares.round(3).to_dict())
```


### Listing 7.4: Parent-level average uniqueness of overlapping labels {#code-7-4}

```python
# ---------- 4. Parent-level average uniqueness and the hat count (Section 7.6) ----------
def issuer_uniqueness(labels, T):
    u = np.empty(len(labels))
    t0_all, t1_all = labels["t0"].values, labels["t1"].values
    for _, idx in labels.groupby("issuer").indices.items():
        t0, t1 = t0_all[idx], t1_all[idx]
        diff = np.zeros(T + 2)
        np.add.at(diff, t0, 1.0)
        np.add.at(diff, t1 + 1, -1.0)
        conc = np.cumsum(diff)[:T + 1]                 # live labels of this parent on each day
        inv = np.concatenate([[0.0], np.cumsum(1.0 / np.maximum(conc, 1.0))])
        u[idx] = (inv[t1 + 1] - inv[t0]) / (t1 - t0 + 1)
    return u

toy = pd.DataFrame({"issuer": [0, 0, 1], "t0": [0, 0, 0], "t1": [9, 9, 9]})
assert np.allclose(issuer_uniqueness(toy, 20), [0.5, 0.5, 1.0])   # siblings share a hat; others don't
labels["u"] = issuer_uniqueness(labels, P["T"])
n_eff = labels["u"].sum()
assert ((labels["u"] > 0) & (labels["u"] <= 1 + 1e-12)).all() and n_eff < 0.25 * len(labels)
print(f"label rows {len(labels):,}   N_eff {n_eff:,.0f}   ratio {n_eff / len(labels):.3f}")
```


### Listing 7.5: Purged, embargoed, parent-grouped cross-validation against shuffled K-fold {#code-7-5}

```python
# ---------- 5. Purged, embargoed, parent-grouped CV vs shuffled K-fold (Section 7.7) ----------
def shuffled_kfold(n, k=5, seed=0):
    fold = np.random.default_rng(seed).permutation(n) % k
    for i in range(k):
        yield np.flatnonzero(fold != i), np.flatnonzero(fold == i)

def purged_group_kfold(t0, t1, groups, n_group_folds=5, n_time_blocks=4, embargo=21, seed=0):
    """Test = (parents in group fold g) x (time block m). Train = other parents whose label
    windows neither overlap the test span nor start within `embargo` days after it."""
    t0, t1, groups = np.asarray(t0), np.asarray(t1), np.asarray(groups)
    parents = np.unique(groups)
    gfold = pd.Series(np.random.default_rng(seed).permutation(parents.size) % n_group_folds, index=parents)
    gf = gfold.loc[groups].values
    edges = np.linspace(t0.min(), t0.max() + 1, n_time_blocks + 1)
    for g in range(n_group_folds):
        for m in range(n_time_blocks):
            test = (gf == g) & (t0 >= edges[m]) & (t0 < edges[m + 1])
            if not test.any():
                continue
            T0, T1 = t0[test].min(), t1[test].max()
            leaks = (t0 <= T1 + embargo) & (t1 >= T0)      # purge and embargo in one condition
            yield np.flatnonzero((gf != g) & ~leaks), np.flatnonzero(test)

def knn_scores(Xtr, ytr, Xte, k=10, batch=500):            # a flexible model that can memorize
    sq, out = (Xtr ** 2).sum(1), np.empty(len(Xte))
    for s in range(0, len(Xte), batch):
        xb = Xte[s:s + batch]
        d2 = (xb ** 2).sum(1)[:, None] + sq[None, :] - 2.0 * xb @ Xtr.T
        out[s:s + batch] = ytr[np.argpartition(d2, k, axis=1)[:, :k]].mean(1)
    return out

def auc(y, score):
    r = stats.rankdata(score)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)

def cv_auc(X, y, splits, k=10):
    score = np.full(len(y), np.nan)
    for tr, te in splits:
        if len(tr) > k and len(te) > 0:
            score[te] = knn_scores(X[tr], y[tr], X[te], k)
    ok = ~np.isnan(score)
    return auc(y[ok], score[ok])

rng = np.random.default_rng(23)
keep = rng.choice(P["n_issuers"], 25, replace=False)
L = labels[labels["issuer"].isin(keep)].reset_index(drop=True)
F = 4
z_parent = rng.normal(0.0, 1.0, (P["n_issuers"], F))                     # persistent parent traits
drift = np.cumsum(rng.normal(0.0, 0.02, (P["T"], P["NB"], F)), axis=0)   # slowly wandering noise
drift += rng.normal(0.0, 0.3, (1, P["NB"], F))
X = z_parent[L["issuer"].values] + drift[L["t0"].values, L["bond"].values]   # PURE NOISE features
y = (L["label"].values > 0).astype(int)
auc_naive = cv_auc(X, y, shuffled_kfold(len(y)))
auc_purged = cv_auc(X, y, purged_group_kfold(L["t0"], L["t1"], L["issuer"]))
print(f"pure-noise AUC: shuffled K-fold {auc_naive:.3f}   purged + grouped {auc_purged:.3f}")
assert auc_naive > auc_purged + 0.03          # overlapping labels leak through shuffled folds
assert abs(auc_purged - 0.5) < 0.06           # the honest splitter finds nothing, correctly
```


### Listing 7.6: Meta-label bet sizing, deflated Sharpe ratio, MinTRL and PBO {#code-7-6}

```python
# ---------- 6. Meta-label bet sizing, deflated Sharpe, MinTRL, PBO (Sections 7.5, 7.8) ----------
def bet_size(p, side):
    """Secondary-model probability -> size in [0, 1), times the primary model's side."""
    p = np.clip(p, 1e-6, 1 - 1e-6)
    z = (p - 0.5) / np.sqrt(p * (1 - p))
    return np.maximum(2 * stats.norm.cdf(z) - 1, 0.0) * side

assert abs(bet_size(0.75, 1) - 0.4364) < 1e-3 and abs(bet_size(0.9, -1) + 0.8176) < 1e-3
assert bet_size(0.4, 1) == 0.0                # the meta-model may veto, never reverse

EULER_GAMMA = 0.5772156649015329

def sharpe(R):
    return R.mean(0) / R.std(0, ddof=1)

def psr(sr, T, skew, kurt, sr0=0.0):
    return stats.norm.cdf((sr - sr0) * np.sqrt(T - 1) / np.sqrt(1 - skew * sr + (kurt - 1) / 4 * sr ** 2))

def expected_max_sr(n_trials, var_sr):
    g = EULER_GAMMA
    return np.sqrt(var_sr) * ((1 - g) * stats.norm.ppf(1 - 1 / n_trials)
                              + g * stats.norm.ppf(1 - 1 / (n_trials * np.e)))

def deflated_sharpe(R):
    """R: (T, N) returns of EVERY trial evaluated; reports the best trial, deflated."""
    T, N = R.shape
    srs = sharpe(R)
    b = int(np.argmax(srs))
    sk, ku = stats.skew(R[:, b]), stats.kurtosis(R[:, b], fisher=False)
    sr_star = expected_max_sr(N, srs.var(ddof=1))
    return dict(sr=srs[b], sr_star=sr_star, psr0=psr(srs[b], T, sk, ku), dsr=psr(srs[b], T, sk, ku, sr_star))

def min_trl(sr, sr0, skew, kurt, alpha=0.05):
    return 1 + (1 - skew * sr + (kurt - 1) / 4 * sr ** 2) * (stats.norm.ppf(1 - alpha) / (sr - sr0)) ** 2

def pbo_cscv(R, S=10):
    T, N = R.shape
    blocks = np.array_split(np.arange(T), S)
    logits = []
    for ins in combinations(range(S), S // 2):
        tr = np.concatenate([blocks[i] for i in ins])
        te = np.concatenate([blocks[i] for i in range(S) if i not in ins])
        n_star = np.argmax(sharpe(R[tr]))
        omega = stats.rankdata(sharpe(R[te]))[n_star] / (N + 1)
        logits.append(np.log(omega / (1 - omega)))
    return float(np.mean(np.array(logits) <= 0))

rng = np.random.default_rng(42)
T_m, N_tr = 120, 1000                                         # 10 years of months, 1,000 trials
maxes = [sharpe(rng.normal(0, 0.02, (T_m, N_tr))).max() for _ in range(40)]
assert abs(np.mean(maxes) / expected_max_sr(N_tr, 1 / T_m) - 1) < 0.10    # extreme-value formula holds
noise = rng.normal(0, 0.02, (T_m, N_tr))
rep = deflated_sharpe(noise)
assert rep["psr0"] > 0.95 and rep["dsr"] < 0.95               # 'significant' naively; a coin flip deflated
print({key: round(float(val), 3) for key, val in rep.items()})
pbo_noise = pbo_cscv(noise[:, :200])
skilled = np.column_stack([noise[:, :200], rng.normal(0.012, 0.02, T_m)])   # one real edge, SR 0.6/month
pbo_skill = pbo_cscv(skilled)
assert 0.10 < pbo_noise < 0.90 and pbo_skill < 0.25
print(f"PBO noise {pbo_noise:.2f}   PBO with one real strategy {pbo_skill:.2f}   "
      f"MinTRL(SR 0.3 vs 0.1, skew -0.5, kurt 5) {min_trl(0.3, 0.1, -0.5, 5):.0f} months")
```


## F.7-B: Chapter 7-B: The Statistician's Toolbox for Credit Panels: Regression, Logistic Models, Survival Analysis, Shrinkage, PCA, Bootstrap and Monte Carlo {#code-7b}

Listings from `07_ch07b_statistics_for_credit_panels.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 7-B.1: creditstats.py: the credit statistics module {#code-7b-1}

```python
# creditstats.py: the statistics toolbox imported by Chapters 8-12, 14 and 15 (Chapter 7-B)
import numpy as np
from scipy import stats


# ---------- 7-B.1 / 7-B.2: OLS and sandwich covariances ----------
def ols(y, X):
    y, X = np.asarray(y, float), np.asarray(X, float)
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return b, y - X @ b


def _codes(g):
    return np.unique(np.asarray(g), return_inverse=True)[1].ravel()


def _cluster_meat(S, g):
    inv = _codes(g)
    sums = np.zeros((inv.max() + 1, S.shape[1]))
    np.add.at(sums, inv, S)
    return sums.T @ sums, sums.shape[0]


def nw_meat(S, lags):
    """Bartlett-weighted sum of score cross-products (not divided by T); rows time-ordered."""
    meat = S.T @ S
    for j in range(1, int(lags) + 1):
        G = S[j:].T @ S[:-j]
        meat += (1.0 - j / (lags + 1.0)) * (G + G.T)
    return meat


def _psd_clip(V):
    w, Q = np.linalg.eigh((V + V.T) / 2.0)
    return (Q * np.clip(w, 0.0, None)) @ Q.T, bool((w < 0).any())


def vcov(X, u, kind="hc1", groups=None, groups2=None, lags=0):
    """Sandwich covariance of OLS coefficients, eq. (7B.1)."""
    X, u = np.asarray(X, float), np.asarray(u, float)
    n, K = X.shape
    bread = np.linalg.inv(X.T @ X)
    S = X * u[:, None]
    info = {"kind": kind, "clipped": False}
    if kind == "classical":
        V = bread * (u @ u) / (n - K)
    elif kind == "hc1":
        V = bread @ (S.T @ S) @ bread * n / (n - K)
    elif kind == "cluster":
        meat, G = _cluster_meat(S, groups)
        V = G / (G - 1.0) * (n - 1.0) / (n - K) * bread @ meat @ bread
        info.update(clusters=G, few_clusters=G < 50)
    elif kind == "twoway":
        a, c = _codes(groups), _codes(groups2)
        V1, i1 = vcov(X, u, "cluster", groups=a)
        V2, i2 = vcov(X, u, "cluster", groups=c)
        V12, _ = vcov(X, u, "cluster", groups=a * (c.max() + 1) + c)
        V, info["clipped"] = _psd_clip(V1 + V2 - V12)
        info.update(clusters=(i1["clusters"], i2["clusters"]),
                    few_clusters=i1["few_clusters"] or i2["few_clusters"])
    elif kind == "nw":
        V = bread @ nw_meat(S, lags) @ bread * n / (n - K)
        info["lags"] = int(lags)
    else:
        raise ValueError(f"unknown kind {kind!r}")
    return V, info


def nw_lags(T, overlap=1):
    """max(floor(4 (T/100)^(2/9)), 2h - 1): the overlap term dominates for overlapping returns."""
    return int(max(np.floor(4.0 * (T / 100.0) ** (2.0 / 9.0)), 2 * overlap - 1))


# ---------- 7-B.3: logistic regression and calibration ----------
def expit(z):
    return 0.5 * (1.0 + np.tanh(0.5 * np.asarray(z, float)))       # overflow-safe


def logit_fit(y, X, ridge=0.0, groups=None, max_iter=50, tol=1e-10):
    """Newton/IRLS; ridge penalizes slopes only (column 0 is the constant)."""
    y, X = np.asarray(y, float), np.asarray(X, float)
    K = X.shape[1]
    P = ridge * np.eye(K)
    P[0, 0] = 0.0
    b = np.zeros(K)
    b[0] = np.log((y.mean() + 1e-12) / (1.0 - y.mean() + 1e-12))
    for _ in range(max_iter):
        p = expit(X @ b)
        H = X.T @ (X * (p * (1.0 - p))[:, None]) + P
        step = np.linalg.solve(H, X.T @ (y - p) - P @ b)
        b = b + step
        if np.max(np.abs(step)) < tol:
            break
    else:
        raise RuntimeError("IRLS did not converge: check for separation (7-B.3)")
    p = expit(X @ b)
    bread = np.linalg.inv(X.T @ (X * (p * (1.0 - p))[:, None]) + P)
    if groups is None:
        return b, bread, p
    meat, G = _cluster_meat(X * (y - p)[:, None], groups)
    return b, G / (G - 1.0) * bread @ meat @ bread, p


def platt_calibrate(p_hat, y):
    """Fit logit p_cal = a + c logit p_hat on a holdout; returns the calibrator."""
    lg = lambda q: np.log(np.clip(q, 1e-6, 1 - 1e-6) / (1 - np.clip(q, 1e-6, 1 - 1e-6)))
    (a, c), _, _ = logit_fit(y, np.column_stack([np.ones(len(p_hat)), lg(np.asarray(p_hat, float))]))
    return lambda q: expit(a + c * lg(np.asarray(q, float)))


# ---------- 7-B.4: survival ----------
def kaplan_meier(times, events, entry=None):
    """Product-limit estimator, Greenwood variance, Nelson-Aalen; entry handles left truncation."""
    times, events = np.asarray(times, float), np.asarray(events, int)
    entry = np.full_like(times, -np.inf) if entry is None else np.asarray(entry, float)
    t_ev = np.unique(times[events == 1])
    n = np.array([((entry < t) & (times >= t)).sum() for t in t_ev])
    d = np.array([((times == t) & (events == 1)).sum() for t in t_ev])
    S = np.cumprod(1.0 - d / n)
    with np.errstate(divide="ignore", invalid="ignore"):          # n == d: Greenwood undefined
        gw = np.cumsum(np.where(n > d, d / (n * (n - d)), np.inf))
        var = np.where(S > 0, S ** 2 * gw, 0.0)
    return {"t": t_ev, "n": n, "d": d, "S": S, "var": var, "H_na": np.cumsum(d / n)}


def cox_ph(times, events, Z, max_iter=50, tol=1e-9):
    """Cox partial likelihood with Breslow ties, Newton steps, eq. (7B.7)."""
    t, e = np.asarray(times, float), np.asarray(events, int)
    Z = np.asarray(Z, float)
    Z = Z[:, None] if Z.ndim == 1 else Z
    b = np.zeros(Z.shape[1])
    t_ev = np.unique(t[e == 1])
    for _ in range(max_iter):
        r = np.exp(Z @ b)
        grad, info = np.zeros_like(b), np.zeros((len(b), len(b)))
        for s in t_ev:
            R, D = t >= s, (t == s) & (e == 1)
            w, ZR = r[R], Z[R]
            zbar = w @ ZR / w.sum()
            grad += Z[D].sum(axis=0) - D.sum() * zbar
            info += D.sum() * ((ZR.T * w) @ ZR / w.sum() - np.outer(zbar, zbar))
        step = np.linalg.solve(info, grad)
        b = b + step
        if np.max(np.abs(step)) < tol:
            break
    r = np.exp(Z @ b)
    H0 = np.cumsum([((t == s) & (e == 1)).sum() / r[t >= s].sum() for s in t_ev])
    return b, np.linalg.inv(info), {"t": t_ev, "H0": H0}


# ---------- 7-B.5: covariance ----------
def ledoit_wolf(R):
    """Ledoit-Wolf (2004) shrinkage toward m I, eq. (7B.8); returns (Sigma, delta)."""
    X = np.asarray(R, float)
    X = X - X.mean(axis=0)
    T, N = X.shape
    S = X.T @ X / T
    F = np.trace(S) / N * np.eye(N)
    d2 = np.sum((S - F) ** 2)                                      # noise + misspecification
    noise = (np.sum(np.sum(X ** 2, axis=1) ** 2) - T * np.sum(S ** 2)) / T ** 2
    delta = min(noise, d2) / d2 if d2 > 0 else 1.0
    return delta * F + (1.0 - delta) * S, delta


def mp_edge(N, T, sigma2=1.0):
    return sigma2 * (1.0 + np.sqrt(N / T)) ** 2


def residual_pca(E, k=1, margin=1.10):
    """PCA of a standardized (T, N) residual panel; counts eigenvalues above margin * MP edge."""
    E = np.asarray(E, float)
    T, N = E.shape
    Ec = E - E.mean(axis=0)
    scale = Ec.std(axis=0)
    Z = Ec / scale
    _, s, Vt = np.linalg.svd(Z, full_matrices=False)
    omega = s ** 2 / T
    V = Vt[:k].T
    V = V * np.where(V.sum(axis=0) < 0, -1.0, 1.0)
    G = Z @ V
    return {"omega": omega, "V": V, "G": G, "cleaned": (Z - G @ V.T) * scale,
            "n_above_mp": int((omega > margin * mp_edge(N, T)).sum())}


# ---------- 7-B.6: bootstrap ----------
def stationary_bootstrap_indices(T, mean_block, rng):
    new_block, starts = rng.random(T) < 1.0 / mean_block, rng.integers(T, size=T)
    idx = np.empty(T, dtype=int)
    idx[0] = starts[0]
    for t in range(1, T):
        idx[t] = starts[t] if new_block[t] else (idx[t - 1] + 1) % T
    return idx


def block_bootstrap(stat, data, rng, B=2000, mean_block=None, method="stationary"):
    """Resample rows (dates, with the whole cross-section): 'stationary', 'block' or 'iid'."""
    data = np.asarray(data)
    T = len(data)
    L = mean_block or max(1, int(round(T ** (1.0 / 3.0))))
    def draw():
        if method == "stationary":
            return stationary_bootstrap_indices(T, L, rng)
        if method == "block":
            starts = rng.integers(T, size=int(np.ceil(T / L)))
            return ((starts[:, None] + np.arange(L)) % T).ravel()[:T]
        return rng.integers(T, size=T)
    return np.array([stat(data[draw()]) for _ in range(B)])


# ---------- 7-B.8: Monte Carlo ----------
def mc_estimate(samples):
    """Mean, standard error and the book's 4-s.e. assertion tolerance."""
    x = np.asarray(samples, float)
    se = x.std(ddof=1) / np.sqrt(len(x))
    return x.mean(), se, 4.0 * se


def control_variate(g, y, mu_y):
    g, y = np.asarray(g, float), np.asarray(y, float)
    c = np.cov(g, y)[0, 1] / np.var(y, ddof=1)
    return mc_estimate(g - c * (y - mu_y))


def bridge_hit_prob(x0, x1, b, sigma, dt):
    """Eq. (7B.9); equals 1 when either endpoint is at or below the barrier."""
    a0, a1 = np.maximum(np.asarray(x0, float) - b, 0.0), np.maximum(np.asarray(x1, float) - b, 0.0)
    return np.exp(-2.0 * a0 * a1 / (sigma ** 2 * dt))


def first_passage_mc(x0, b, mu, sigma, T, n_steps, n_paths, rng, method="bridge_rb"):
    """P(min X <= b), X = x0 + mu t + sigma W: 'naive' grid, 'bridge' coin flips, 'bridge_rb' weights."""
    dt = T / n_steps
    steps = mu * dt + sigma * np.sqrt(dt) * rng.standard_normal((n_paths, n_steps))
    X = np.column_stack([np.full(n_paths, x0), x0 + np.cumsum(steps, axis=1)])
    if method == "naive":
        return mc_estimate((X[:, 1:] <= b).any(axis=1))
    p = bridge_hit_prob(X[:, :-1], X[:, 1:], b, sigma, dt)
    if method == "bridge":
        return mc_estimate((rng.random(p.shape) < p).any(axis=1))
    return mc_estimate(1.0 - np.prod(1.0 - p, axis=1))


def first_passage_exact(x0, b, mu, sigma, T):
    d, s = x0 - b, sigma * np.sqrt(T)
    return (stats.norm.cdf((-d - mu * T) / s)
            + np.exp(-2.0 * mu * d / sigma ** 2) * stats.norm.cdf((-d + mu * T) / s))
```


### Listing 7-B.2: Acceptance tests for creditstats.py {#code-7b-2}

```python
# Acceptance tests for creditstats.py (seeded; every tolerance is derived, not tuned)
streams = [np.random.default_rng(s) for s in np.random.SeedSequence(707).spawn(6)]
r_ols, r_nw, r_logit, r_cox, r_cov, r_mc = streams

# 7-B.1: the Moulton factor, issuer-level signal, 200 issuers x 11 bonds, sibling corr 0.6
G, m, rho_u = 200, 11, 0.6
issuer = np.repeat(np.arange(G), m)
x_iss = r_ols.standard_normal(G)[issuer]
u = np.sqrt(rho_u) * r_ols.standard_normal(G)[issuer] + np.sqrt(1 - rho_u) * r_ols.standard_normal(G * m)
X = np.column_stack([np.ones(G * m), x_iss])
b_hat, res = ols(0.05 * x_iss + u, X)
ratio = np.sqrt(vcov(X, res, "cluster", groups=issuer)[0][1, 1] / vcov(X, res, "classical")[0][1, 1])
print(f"Moulton: clustered/classical s.e. {ratio:.2f}; formula {np.sqrt(1 + (m - 1) * rho_u):.2f}")
assert 1.9 < ratio < 3.4

# 7-B.2: Newey-West on 12-period overlapping sums recovers ~8.0 (L=11) and ~10.0 (L=23) of 12
h, T = 12, 12_000
Rh = np.convolve(r_nw.standard_normal(T + h - 1), np.ones(h), mode="valid")
Xc = np.ones((T, 1))
_, res = ols(Rh, Xc)
v_hc = vcov(Xc, res, "hc1")[0][0, 0]
m11, m23 = (vcov(Xc, res, "nw", lags=L)[0][0, 0] / v_hc for L in (h - 1, 2 * h - 1))
print(f"NW multipliers: L=11 {m11:.1f} (theory 8.0), L=23 {m23:.1f} (theory 10.0), truth {h}")
assert 6.8 < m11 < 9.2 and 8.5 < m23 < 11.5 and m11 < m23

# 7-B.3: logit recovers its coefficients; calibration in the large is exact in sample
n = 20_000
Xl = np.column_stack([np.ones(n), r_logit.standard_normal((n, 2))])
b_true = np.array([-3.5, 0.8, -0.5])
yl = (r_logit.random(n) < expit(Xl @ b_true)).astype(float)
b_l, V_l, p_l = logit_fit(yl, Xl)
assert np.all(np.abs(b_l - b_true) < 4.0 * np.sqrt(np.diag(V_l)))
assert abs(p_l.sum() - yl.sum()) < 1e-6 * n

# 7-B.4: the practice cohort (Calloway, Quillfeather, Larkspur, Halvorsen, Halyard, Brambleworth)
km = kaplan_meier([9, 14, 22, 27, 30, 36], [0, 1, 1, 1, 0, 0])
assert np.allclose(km["S"], [0.8, 0.6, 0.4]) and np.isclose(km["var"][-1], 0.048)
print(f"Practice cohort PD(36m) = {1 - km['S'][-1]:.0%} +/- {np.sqrt(km['var'][-1]):.0%}")

# 7-B.4: Cox recovers the runway hazard ratio e^1.1 under independent censoring
n = 3_000
z = (r_cox.random(n) < 0.3).astype(float)
tau = r_cox.exponential(1.0 / (0.05 * np.exp(1.1 * z)))
cens = r_cox.uniform(0.0, 15.0, n)
b_c, V_c, _ = cox_ph(np.minimum(tau, cens), (tau <= cens).astype(int), z)
print(f"Cox hazard ratio {np.exp(b_c[0]):.2f} (true {np.exp(1.1):.2f})")
assert abs(b_c[0] - 1.1) < 4.0 * np.sqrt(V_c[0, 0])

# 7-B.5: shrinkage is invertible when N > T; one planted factor clears Marchenko-Pastur, noise does not
T_c, N_c = 120, 400
Rp = 0.6 * r_cov.standard_normal((T_c, 1)) * r_cov.uniform(0.5, 1.5, N_c) + r_cov.standard_normal((T_c, N_c))
Sig_lw, delta = ledoit_wolf(Rp)
assert 0.0 <= delta <= 1.0 and np.linalg.eigvalsh(Sig_lw).min() > 0
assert residual_pca(Rp)["n_above_mp"] == 1
assert residual_pca(r_cov.standard_normal((T_c, N_c)))["n_above_mp"] == 0
print(f"LW delta {delta:.2f}; MP edge {mp_edge(N_c, T_c):.1f}")

# 7-B.6: block bootstrap sees AR(1) dependence that the iid bootstrap misses (theory ratio 1.73)
rho, T_b = 0.5, 2_000
e = r_mc.standard_normal(T_b)
ar = np.zeros(T_b)
for t in range(1, T_b):
    ar[t] = rho * ar[t - 1] + e[t]
se_iid = block_bootstrap(np.mean, ar, r_mc, B=1000, method="iid").std()
se_sb = block_bootstrap(np.mean, ar, r_mc, B=1000, mean_block=25).std()
assert se_sb / se_iid > 1.35

# 7-B.8: tolerances, control variates, and the Brownian bridge
zz = r_mc.standard_normal(1_000_000)
est, se, tol = mc_estimate(zz > 2.0)
assert abs(est - stats.norm.sf(2.0)) < tol
plain, cv = mc_estimate(np.exp(zz[:100_000])), control_variate(np.exp(zz[:100_000]), zz[:100_000], 0.0)
assert abs(cv[0] - np.exp(0.5)) < cv[2] and cv[1] < 0.8 * plain[1]
exact0 = first_passage_exact(0.30, 0.0, 0.0, 0.25, 1.0)
naive = first_passage_mc(0.30, 0.0, 0.0, 0.25, 1.0, 12, 40_000, r_mc, method="naive")
bridge = first_passage_mc(0.30, 0.0, 0.0, 0.25, 1.0, 12, 40_000, r_mc)
print(f"First passage: exact {exact0:.3f}, monthly grid {naive[0]:.3f}, grid + bridge {bridge[0]:.3f}")
assert abs(bridge[0] - exact0) < bridge[2] and naive[0] < exact0 - 0.03
coin = first_passage_mc(0.30, 0.0, -0.05, 0.25, 1.0, 4, 40_000, r_mc, method="bridge")
assert abs(coin[0] - first_passage_exact(0.30, 0.0, -0.05, 0.25, 1.0)) < coin[2]   # drift cancels
print("creditstats: all checks passed")
```


## F.8: Chapter 8: Stripping Beta to Isolate Pure IDO {#code-8}

Listings from `08_ch08_isolating_ido_and_empirical_duration.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 8.1: Setup: one seeded generator and one scoreboard {#code-8-1}

```python
# ---------- 0. Setup: one seeded generator, one scoreboard ----------
import numpy as np
from scipy import optimize, stats

RNG = np.random.default_rng(8)
CHECKS = {}


def report(name, ok, detail=""):
    CHECKS[name] = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name:<40s} {detail}")
```


### Listing 8.2: Return decomposition into carry, rates, spread, convexity and residual {#code-8-2}

```python
# ---------- 1. Return decomposition with the right signs (Section 8.1) ----------
def decompose_returns(total_ret, y, s, dy_tsy, ds, D_mod, D_spr, convexity, dt):
    """Split realized total returns into carry, rates, spread, convexity and residual.

    Shapes: every argument is a float scalar or an array of shape (T,).
    Units: y, s, dy_tsy, ds in DECIMAL (0.0018 = 18 bp); durations in years;
    convexity in years^2; dt in years under the bond's day count (30/360).
    carry_oas is reported for excess-return work but is NOT part of the total-return sum.
    """
    total_ret, y, s, dy_tsy, ds = (np.asarray(a, dtype=float) for a in (total_ret, y, s, dy_tsy, ds))
    if np.any(np.abs(dy_tsy) > 0.05) or np.any(np.abs(ds) > 0.05):
        raise ValueError("a daily move above 500 bp: inputs are probably in bp, not decimal")
    parts = {
        "carry_yield": y * dt,
        "rates_pnl": -D_mod * dy_tsy,            # the minus sign ROBO forgets
        "spread_pnl": -D_spr * ds,
        "convexity_pnl": 0.5 * convexity * (dy_tsy + ds) ** 2,
    }
    parts["residual"] = total_ret - sum(parts.values())
    parts["carry_oas"] = s * dt
    recon = sum(parts[k] for k in ("carry_yield", "rates_pnl", "spread_pnl", "convexity_pnl", "residual"))
    assert np.allclose(recon, total_ret, atol=1e-10, rtol=0.0), "decomposition does not foot"
    return parts


# The cold-open bond (illustrative inputs from Section 8.1)
cold = decompose_returns(total_ret=-0.0039, y=0.111, s=0.062, dy_tsy=0.0018, ds=-0.0009,
                         D_mod=4.1, D_spr=4.0, convexity=20.0, dt=1.0 / 360.0)
cents = {k: 95.0 * 100.0 * float(v) for k, v in cold.items()}      # cents on a 95-dollar price
report("8.1 decomposition foots",
       abs(cents["rates_pnl"] + 70.1) < 0.5 and abs(cents["residual"] + 4.1) < 0.5,
       f"rates {cents['rates_pnl']:.1f}c, spread {cents['spread_pnl']:.1f}c, resid {cents['residual']:.1f}c")
```


### Listing 8.3: Empirical duration: pooled regression and the closed form {#code-8-3}

```python
# ---------- 2. Empirical duration: regression and closed form (Section 8.2) ----------
def empirical_duration(R, dy, D, s):
    """Pooled no-intercept OLS of R on [-D*dy, -D*s*dy]; H(s) = beta + gamma*s.

    R, dy, D, s: 1-D float arrays of equal length (stack bonds and days).
    Returns (beta, gamma, H) where H maps a spread grid (decimal) to hedge ratios.
    """
    R, dy, D, s = (np.asarray(a, dtype=float).ravel() for a in (R, dy, D, s))
    X = np.column_stack([-D * dy, -D * s * dy])
    (beta, gamma), *_ = np.linalg.lstsq(X, R, rcond=None)
    return float(beta), float(gamma), (lambda grid: beta + gamma * np.asarray(grid, dtype=float))


def h_closed_form(s, rel_ds, dy):
    """H = 1 + s * rho * sig_s / sig_y from sample moments (Ben Dor's two-factor result)."""
    c = np.cov(rel_ds, dy)
    rho = c[0, 1] / np.sqrt(c[0, 0] * c[1, 1])
    return 1.0 + np.asarray(s, dtype=float) * rho * np.sqrt(c[0, 0] / c[1, 1])


T = 2500
SIG_Y, SIG_S, RHO = 0.0006, 0.02, -0.4          # 6 bp/day yield vol; 2%/day relative-spread vol
D_BOND, S_BOND = 4.0, 0.06
LINK = RHO * SIG_S / SIG_Y                       # linkage factor: -13.3 per unit of decimal spread
dy = SIG_Y * RNG.standard_normal(T)
x = LINK * dy + SIG_S * np.sqrt(1.0 - RHO ** 2) * RNG.standard_normal(T)   # relative spread change
S_LEVELS = np.array([0.01, 0.03, 0.06, 0.09])
R_panel = np.stack([-D_BOND * dy - D_BOND * sl * x + 0.0005 * RNG.standard_normal(T) for sl in S_LEVELS])

beta_hat, gamma_hat, H_of = empirical_duration(
    R_panel.ravel(), np.tile(dy, len(S_LEVELS)), np.full(R_panel.size, D_BOND), np.repeat(S_LEVELS, T))
H_true = 1.0 + S_BOND * LINK                     # = 0.20
H_reg, H_cf = float(H_of(S_BOND)), float(h_closed_form(S_BOND, x, dy))
report("8.2 regression H matches closed form",
       abs(H_reg - H_cf) < 0.05 and abs(beta_hat - 1.0) < 0.05,
       f"H_reg {H_reg:.3f}, H_closed {H_cf:.3f}, beta {beta_hat:.3f}")
report("8.2 H near population value", abs(H_reg - H_true) < 0.15, f"H_true {H_true:.2f}")
```


### Listing 8.4: Stale-price betas: Dimson, Scholes-Williams and de-smoothing {#code-8-4}

```python
# ---------- 3. Stale-price betas: Dimson, Scholes-Williams, de-smoothing (Section 8.5) ----------
def lagged(f, k):
    """out[t] = f[t-k], NaN where undefined. k > 0 is a lag, k < 0 a lead."""
    f = np.asarray(f, dtype=float)
    out = np.full(f.shape, np.nan)
    if k >= 0:
        out[k:] = f[:len(f) - k]
    else:
        out[:k] = f[-k:]
    return out


def ols_slope(yv, xv):
    ok = ~(np.isnan(xv) | np.isnan(yv))
    xc, yc = xv[ok] - xv[ok].mean(), yv[ok] - yv[ok].mean()
    return float(xc @ yc / (xc @ xc))


def dimson_beta(r_obs, f, lags=2, leads=0):
    """Sum of slopes from ONE regression of r_obs[t] on f[t+leads], ..., f[t-lags] (Dimson 1979)."""
    if lags > 5 or leads > 5:
        raise ValueError("refusing more than 5 lags or leads: estimation noise dominates the sum")
    r_obs = np.asarray(r_obs, dtype=float)
    ks = list(range(-leads, lags + 1))
    X = np.column_stack([np.ones(len(f))] + [lagged(f, k) for k in ks])
    ok = ~np.isnan(X).any(axis=1) & ~np.isnan(r_obs)
    coef, *_ = np.linalg.lstsq(X[ok], r_obs[ok], rcond=None)
    b = dict(zip(ks, coef[1:]))
    return float(sum(b.values())), b


def scholes_williams_beta(r_obs, f):
    """(b_lead + b_0 + b_lag) / (1 + 2 rho_f), each slope from its own univariate regression."""
    b = [ols_slope(r_obs, lagged(f, k)) for k in (-1, 0, 1)]
    rho_f = np.corrcoef(f[1:], f[:-1])[0, 1]
    return float(sum(b) / (1.0 + 2.0 * rho_f))


def desmooth(r_obs, theta):
    """Invert r_obs[t] = sum_k theta[k] * r[t-k] recursively; theta must be invertible."""
    theta = np.asarray(theta, dtype=float)
    if np.any(np.abs(np.roots(theta[::-1])) <= 1.0):
        raise ValueError("MA polynomial not invertible: the de-smoothed series would explode")
    q = len(theta) - 1
    r_hat = np.array(r_obs, dtype=float)
    for t in range(q, len(r_hat)):
        r_hat[t] = (r_obs[t] - theta[1:] @ r_hat[t - q:t][::-1]) / theta[0]
    return r_hat


DTS_BOND = D_BOND * S_BOND                       # 0.24
THETA = np.array([0.5, 0.3, 0.2])                # 50% of news priced today, 30% tomorrow, 20% the day after
r_true = -D_BOND * dy - DTS_BOND * x + 0.0005 * RNG.standard_normal(T)
r_obs = np.convolve(r_true, THETA)[:T]           # r_obs[t] = sum_k THETA[k] * r_true[t-k]
burn = slice(10, None)
beta_true = ols_slope(r_true[burn], x[burn])
beta_ols = ols_slope(r_obs[burn], x[burn])
beta_dim, b_lags = dimson_beta(r_obs[burn], x[burn], lags=2)
beta_sw = scholes_williams_beta(r_obs[burn], x[burn])
vol_ratio = r_obs[burn].std() / r_true[burn].std()
report("8.5 OLS beta attenuated to theta_0", abs(beta_ols / beta_true - THETA[0]) < 0.05,
       f"OLS/true {beta_ols / beta_true:.3f}")
report("8.5 Dimson(2) recovers beta", abs(beta_dim / beta_true - 1.0) < 0.10,
       f"Dimson/true {beta_dim / beta_true:.3f}")
report("8.5 Scholes-Williams catches one lag", 0.70 < beta_sw / beta_true < 0.90,
       f"SW/true {beta_sw / beta_true:.3f}")
report("8.5 stale vol ratio", abs(vol_ratio - np.sqrt(np.sum(THETA ** 2))) < 0.03,
       f"{vol_ratio:.3f} vs {np.sqrt(np.sum(THETA ** 2)):.3f}")

theta_hat = np.array([b_lags[k] for k in range(3)]) / beta_dim
r_hat = desmooth(r_obs, theta_hat)
tail = slice(50, None)
vr = r_hat[tail].std() / r_true[tail].std()
report("8.5 de-smoothing restores vol",
       abs(vr - 1.0) < 0.10 and np.corrcoef(r_hat[tail], r_true[tail])[0, 1] > 0.9,
       f"vol ratio {vr:.3f}, theta_hat {np.round(theta_hat, 3)}")
```


### Listing 8.5: DTS as the unit of credit beta, and the DTS pair hedge {#code-8-5}

```python
# ---------- 4. DTS: the unit of credit beta (Section 8.4) ----------
def dts(D_spr, oas):
    oas = np.asarray(oas, dtype=float)
    if np.any(oas <= 0.0):
        raise ValueError("non-positive OAS: use absolute spread changes for these bonds, with a warning")
    return np.asarray(D_spr, dtype=float) * oas


def dts_scale(xs_returns, dts_lag):
    """Excess return per unit of previous-close DTS (approximately minus the relative spread change)."""
    return np.asarray(xs_returns, dtype=float) / np.asarray(dts_lag, dtype=float)


def dts_pair_hedge(dts_long, dts_short):
    """Notional of the short bond per 1 unit of long notional that zeroes net DTS."""
    return float(dts_long / dts_short)


h_pair = dts_pair_hedge(dts(2.0, 0.02), dts(4.0, 0.01))        # 200 bp x 2y vs 100 bp x 4y
h_carry = dts_pair_hedge(dts(5.0, 0.03), dts(5.0, 0.015))      # equal durations, 300 vs 150 bp
report("8.4 DTS equivalence and zero carry",
       np.isclose(h_pair, 1.0) and np.isclose(0.03 - h_carry * 0.015, 0.0),
       f"pair hedge {h_pair:.2f}, carry-pair hedge {h_carry:.2f}")

# Beta to the market equals the DTS ratio when relative spread shocks are common.
x_m = SIG_S * RNG.standard_normal(T)
dts_cs = np.array([0.05, 0.12, 0.24, 0.40])
xs_cs = -dts_cs[:, None] * (x_m[None, :] + 0.005 * RNG.standard_normal((4, T)))
xs_mkt = xs_cs.mean(axis=0)
beta_cs = np.array([ols_slope(xs_cs[i], xs_mkt) for i in range(4)])
report("8.4 beta equals DTS ratio", np.allclose(beta_cs, dts_cs / dts_cs.mean(), rtol=0.10),
       f"betas {np.round(beta_cs, 2)} vs {np.round(dts_cs / dts_cs.mean(), 2)}")
```


### Listing 8.6: The hedge matrix: minimum variance, ridge, bounds and contract units {#code-8-6}

```python
# ---------- 5. The hedge matrix: min-variance, ridge, bounds, units (Section 8.6) ----------
def cond_number(M):
    w = np.linalg.eigvalsh(M)
    return float(w.max() / max(w.min(), 1e-300))


def eta_for_condition(C, cond_max=50.0):
    """Smallest ridge penalty capping cond(C + eta I) at cond_max (C a correlation matrix)."""
    w = np.linalg.eigvalsh(C)
    return max(0.0, float((w.max() - cond_max * w.min()) / (cond_max - 1.0)))


def _moments(r_p, R_H):
    S = np.cov(np.column_stack([R_H, r_p]), rowvar=False)
    return S[:-1, :-1], S[:-1, -1]


def hedge_matrix(r_p, R_H, eta=None, cond_max=50.0):
    """Variance-scaled ridge hedge. r_p: (T,), R_H: (T, m), returns per 1 unit of notional.

    Returns h (notional of each instrument to SHORT per unit of target), in-sample residual
    variance, cond(C) before and after regularization, and the penalty eta used.
    """
    r_p, R_H = np.asarray(r_p, dtype=float), np.asarray(R_H, dtype=float)
    S_HH, S_Hp = _moments(r_p, R_H)
    sd = np.sqrt(np.diag(S_HH))
    C = S_HH / np.outer(sd, sd)
    if eta is None:
        eta = eta_for_condition(C, cond_max)
    h = np.linalg.solve(S_HH + eta * np.diag(np.diag(S_HH)), S_Hp)
    resid_var = float(np.var(r_p - R_H @ h, ddof=1))
    return h, resid_var, cond_number(C), cond_number(C + eta * np.eye(len(sd))), eta


def hedge_qp(r_p, R_H, bounds, eta=0.0):
    """Ridge hedge with per-instrument bounds [(lo, hi), ...], solved by L-BFGS-B."""
    S_HH, S_Hp = _moments(np.asarray(r_p, dtype=float), np.asarray(R_H, dtype=float))
    A = S_HH + eta * np.diag(np.diag(S_HH))
    k = 1.0 / np.mean(np.diag(A))                # rescale so the optimizer sees O(1) numbers
    res = optimize.minimize(lambda h: k * (h @ A @ h - 2.0 * h @ S_Hp), np.zeros(len(S_Hp)),
                            jac=lambda h: k * (2.0 * A @ h - 2.0 * S_Hp),
                            bounds=bounds, method="L-BFGS-B")
    return res.x


def futures_contracts(dv01_target, dv01_ctd_per_contract, conv_factor, hedge_ratio=1.0):
    """N = H * DV01_target / (DV01_CTD / CF)."""
    return hedge_ratio * dv01_target / (dv01_ctd_per_contract / conv_factor)


def etf_shares(h, target_notional, etf_price):
    return h * target_notional / etf_price


# Four instruments plus a near-copy (JNK ~ HYG), all built from the same rate and spread factors.
dyH = SIG_Y * RNG.standard_normal(T)
xH = LINK * dyH + SIG_S * np.sqrt(1.0 - RHO ** 2) * RNG.standard_normal(T)


def noise(sd):
    return sd * RNG.standard_normal(T)


cdx = -0.14 * xH + noise(0.0005)                 # CDX HY, long risk: ~RPV01 4 x spread 3.5%
ty = -6.5 * dyH + noise(0.0001)                  # TY future, per unit of face
hyg = -3.2 * dyH - 0.11 * xH + noise(0.0012)     # HYG: rates + spread beta + NAV basis
put = 0.30 * xH + noise(0.004)                   # equity put proxy: gains when spreads widen
jnk = hyg + noise(0.000002)                      # the collinearity trap
R_H = np.column_stack([cdx, ty, hyg, put, jnk])
r_book = -D_BOND * dyH - DTS_BOND * xH + noise(0.003)   # B book with 30 bp/day of IDO

tr, te = slice(0, 2000), slice(2000, None)
h_ols, _, cond_raw, _, _ = hedge_matrix(r_book[tr], R_H[tr], eta=0.0)
h_rdg, _, _, cond_rdg, eta = hedge_matrix(r_book[tr], R_H[tr])


def oos(h):
    return float(np.var(r_book[te] - R_H[te] @ h, ddof=1))


v_un, v_ols, v_rdg = float(np.var(r_book[te], ddof=1)), oos(h_ols), oos(h_rdg)
report("8.6 collinearity detected and capped", cond_raw > 1e3 and cond_rdg <= 50.0 * (1 + 1e-6),
       f"cond {cond_raw:.1e} -> {cond_rdg:.1f}, eta {eta:.3f}")
report("8.6 ridge hedges out of sample", v_rdg < 0.6 * v_un and v_rdg <= 1.15 * v_ols,
       f"vs unhedged {v_rdg / v_un:.2f}, vs OLS {v_rdg / v_ols:.3f}")

half_a, half_b = slice(0, 1000), slice(1000, 2000)


def drift(e):
    ha = hedge_matrix(r_book[half_a], R_H[half_a], eta=e)[0]
    hb = hedge_matrix(r_book[half_b], R_H[half_b], eta=e)[0]
    return float(np.linalg.norm(ha - hb))


report("8.6 ridge weights are stable", drift(eta) < drift(0.0),
       f"weight drift ridge {drift(eta):.2f} vs OLS {drift(0.0):.2f}")

# Paleologo's attenuation: one noisy proxy, so hedge less than the naive amount.
f_true = 0.01 * RNG.standard_normal(T)
proxy = f_true + 0.01 * RNG.standard_normal(T)   # omega^2 = sigma_f^2, so attenuation is one half
target = 0.8 * f_true + 0.005 * RNG.standard_normal(T)
h_star = hedge_matrix(target, proxy[:, None], eta=0.0)[0][0]
report("8.6 hedge less than naive",
       abs(h_star - 0.4) < 0.05 and np.var(target - h_star * proxy) < np.var(target - 0.8 * proxy),
       f"h* {h_star:.3f} vs naive 0.8")

bounds = [(0.0, 1.0), (-1.0, 1.0), (-0.5, 0.5), (-0.5, 0.0), (-0.5, 0.5)]   # liquidity and mandate limits
h_box = hedge_qp(r_book[tr], R_H[tr], bounds, eta=eta)
inside = all(lo - 1e-9 <= hb <= hi + 1e-9 for hb, (lo, hi) in zip(h_box, bounds))
report("8.6 bounded hedge respects limits", inside and oos(h_box) < 0.8 * v_un,
       f"h_box {np.round(h_box, 2)}")

dv01_bond = 40e6 * 4.1 * 1e-4                    # the cold-open bond: 16,400 per bp
n_full = futures_contracts(dv01_bond, 63.0, 0.89)
n_emp = futures_contracts(dv01_bond, 63.0, 0.89, hedge_ratio=0.73)
report("8.6 futures sizing matches Table 8.2", round(n_full) == 232 and round(n_emp) == 169,
       f"{n_full:.1f} and {n_emp:.1f} TY contracts")
```


### Listing 8.7: Stripping the common residual factor, and the IDO ledger {#code-8-7}

```python
# ---------- 6. Common residual factor and the IDO ledger (Section 8.8) ----------
def strip_common_factor(eps_scaled, n_pc=1):
    """Remove the leading principal components from a (T, N) panel of DTS-scaled residuals."""
    X = np.asarray(eps_scaled, dtype=float)
    X = X - X.mean(axis=0)
    U, sv, Vt = np.linalg.svd(X, full_matrices=False)
    share = sv ** 2 / np.sum(sv ** 2)
    return X - (U[:, :n_pc] * sv[:n_pc]) @ Vt[:n_pc], share


def ido_ledger(ido, signal, min_names=10):
    """ido, signal: (T, N). signal[t] must be known before ido[t] is realized."""
    ics = []
    for t in range(ido.shape[0]):
        ok = ~(np.isnan(ido[t]) | np.isnan(signal[t]))
        if ok.sum() >= min_names:
            ics.append(stats.spearmanr(signal[t, ok], ido[t, ok])[0])
    ics = np.asarray(ics)
    return {"resid_vol": float(np.nanstd(ido)), "ic_mean": float(ics.mean()),
            "ic_t": float(ics.mean() * np.sqrt(len(ics)) / ics.std(ddof=1)), "months": len(ics)}


TM, NB = 60, 200
g = 0.02 * RNG.standard_normal(TM)                               # the CDGM common residual factor
eps_scaled = np.outer(g, RNG.uniform(0.5, 1.5, NB)) + 0.03 * RNG.standard_normal((TM, NB))
clean, share_before = strip_common_factor(eps_scaled)
_, share_after = strip_common_factor(clean)
ido = clean * RNG.uniform(0.05, 0.40, NB)[None, :]              # back to returns with each bond's DTS
signal = 0.15 * ido / ido.std() + RNG.standard_normal((TM, NB))  # a planted, modest edge
ledger = ido_ledger(ido, signal)
report("8.8 common residual factor stripped", share_before[0] > 0.2 and share_after[0] < 0.1,
       f"PC1 share {share_before[0]:.2f} -> {share_after[0]:.2f}")
report("8.8 IDO ledger finds the planted IC", ledger["ic_mean"] > 0.05 and ledger["ic_t"] > 3.0,
       f"IC {ledger['ic_mean']:.3f}, t {ledger['ic_t']:.1f} over {ledger['months']} months")

print(f"\n{sum(CHECKS.values())}/{len(CHECKS)} checks passed")
assert all(CHECKS.values()), [k for k, v in CHECKS.items() if not v]
```


## F.9: Chapter 9: Factor Investing in Corporate Credit {#code-9}

Listings from `09_ch09_factor_investing_in_credit.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 9.1: Synthetic universe and data-generating process {#code-9-1}

```python
# ---------- Block 1: synthetic universe and data-generating process (Sections 9.2-9.3) ----------
import numpy as np
import pandas as pd

SEED = 20261018
rng = np.random.default_rng(SEED)
pd.set_option("display.width", 140)

J, T, K_SEC = 400, 240, 8                  # issuers, months, sectors
RATINGS = ["A", "BBB", "BB", "B", "CCC"]   # index 0..4; 2 and above is high yield
P_RATING = np.array([0.20, 0.30, 0.22, 0.18, 0.10])
BASE_S = np.array([0.0085, 0.0140, 0.0260, 0.0400, 0.0850])   # median OAS, decimal (illustrative)
LAMBDA = np.array([0.0005, 0.0020, 0.0080, 0.0250, 0.0600])   # P-measure default intensity, 1/yr
BIDASK = np.array([0.0005, 0.0007, 0.0012, 0.0018, 0.0035])   # bid-ask quoted in spread, decimal
LEV_MU = np.array([0.25, 0.35, 0.45, 0.55, 0.70])             # leverage, decimal
NDE_MU = np.array([1.5, 2.5, 3.5, 5.0, 7.0])                  # net debt / EBITDA, turns
ICOV_MU = np.array([12.0, 7.0, 4.5, 2.5, 1.4])                # interest coverage, times
RECOVERY = 0.40                                               # fraction of par
PHI_C, SIG_C, A0, A1 = 0.98, 0.04, 0.03, 0.005   # issuer residual AR(1); equity news now / next month
PHI_M, SIG_M, PHI_S, SIG_S = 0.97, 0.08, 0.95, 0.03
BOND_NOISE = 0.03          # CUSIP-level relative spread noise per month
NDE_CAP = 15.0             # turns for negative-EBITDA issuers, applied BEFORE any floor (Section 9.3.2)
DTS_TARGET = 12.0          # years x percent (Dynkin p.739)


def build_issuers(rng):
    r = rng.choice(5, size=J, p=P_RATING)
    lev = np.clip(LEV_MU[r] + 0.07 * rng.standard_normal(J), 0.05, 0.95)
    nde = NDE_MU[r] * np.exp(0.25 * rng.standard_normal(J))
    nde = np.where(rng.random(J) < 0.02, -nde, nde)          # negative EBITDA -> negative ratio
    icov = ICOV_MU[r] * np.exp(0.30 * rng.standard_normal(J))
    hidden = (r >= 3) & (rng.random(J) < 0.15)               # undisclosed priming risk (Chapter 13)
    prs = np.clip(0.2 + 0.6 * hidden + 0.15 * rng.standard_normal(J), 0.0, 1.0)
    nde_eff = np.where(nde > 0, nde, NDE_CAP)
    log_fair = (np.log(BASE_S[r]) + 0.8 * (lev - LEV_MU[r]) + 0.05 * (nde_eff - NDE_MU[r])
                - 0.03 * (icov - ICOV_MU[r]) + 0.6 * hidden)  # the market prices the hidden risk
    lam = LAMBDA[r] * np.where(hidden, 3.0, 1.0)
    sector = rng.integers(0, K_SEC, size=J)
    return pd.DataFrame(dict(rating=r, sector=sector, lev=lev, nde=nde, nde_eff=nde_eff,
                             icov=icov, hidden=hidden, prs=prs, log_fair=log_fair, lam=lam))


def build_bonds(iss, rng):
    nb = 1 + rng.poisson(4, size=J)                          # bonds per issuer, mean 5
    iid = np.repeat(np.arange(J), nb)
    r = iss.rating.values[iid]
    mat = np.where(r >= 2, rng.uniform(2, 10, iid.size), rng.uniform(1, 20, iid.size))
    dur = (1.0 - 1.05 ** (-mat)) / 0.05                      # spread-duration proxy, years
    log_s0 = (iss.log_fair.values[iid] + 0.15 * np.log(mat / 7.0)
              + 0.05 * rng.standard_normal(iid.size))         # issuer curve slope + CUSIP noise
    return pd.DataFrame(dict(issuer=iid, rating=r, sector=iss.sector.values[iid], mat=mat,
                             dur=dur, log_s0=log_s0, lcs=BIDASK[r] * dur,
                             mbucket=np.digitize(mat, [5.0, 10.0])))


def simulate(iss, bonds, rng):
    n, iid = len(bonds), bonds.issuer.values
    M, S = np.zeros(T + 1), np.zeros((T + 1, K_SEC))
    news = rng.standard_normal((T + 1, J))
    c = np.zeros((T + 1, J))
    c[0] = rng.standard_normal(J) * np.sqrt((SIG_C**2 + A0**2 + A1**2) / (1 - PHI_C**2))
    eq_m = 0.045 * rng.standard_normal(T + 1)               # market equity return, monthly
    for t in range(1, T + 1):
        zM = -0.5 * eq_m[t] / 0.045 + np.sqrt(0.75) * rng.standard_normal()
        M[t] = PHI_M * M[t - 1] + SIG_M * zM
        S[t] = PHI_S * S[t - 1] + SIG_S * rng.standard_normal(K_SEC)
        c[t] = PHI_C * c[t - 1] + SIG_C * rng.standard_normal(J) - A0 * news[t] - A1 * news[t - 1]
    eq_ret = 0.006 + eq_m[:, None] + 0.08 * news            # issuer equity return over (t-1, t]
    log_s = bonds.log_s0.values[None, :] + M[:, None] + S[:, bonds.sector.values] + c[:, iid]
    log_s = np.maximum(log_s, np.log(1e-4))                 # floor OAS at 1bp
    s = np.exp(log_s)
    p_def = 1.0 - np.exp(-iss.lam.values / 12.0)
    hit = rng.random((T, J)) < p_def[None, :]
    drow = np.where(hit.any(axis=0), hit.argmax(axis=0), T + 10)   # row of the default-month return
    drow_b = drow[iid]
    rows = np.arange(T)[:, None]
    dur = bonds.dur.values[None, :]
    xs = (s[:-1] / 12.0 - dur * s[:-1] * np.diff(log_s, axis=0)
          + dur * s[:-1] * BOND_NOISE * rng.standard_normal((T, n)))
    xs = np.where(rows == drow_b[None, :], RECOVERY - 1.0, xs)     # default: recovery minus par
    held = rows <= drow_b[None, :]                                  # in universe at start of row t
    xs = np.where(held, xs, np.nan)
    return dict(s=s, xs=xs, held=held, eq_ret=eq_ret, drow_b=drow_b)


iss = build_issuers(rng)
bonds = build_bonds(iss, rng)
sim = simulate(iss, bonds, rng)
N = len(bonds)
s, xs, held, drow_b = sim["s"], sim["xs"], sim["held"], sim["drow_b"]
D, RAT, IID = bonds.dur.values, bonds.rating.values, bonds.issuer.values
DTS = D[None, :] * s[:-1] * 100.0                      # (T, N) years x percent, START of month
r_mkt = np.array([xs[t, held[t]].mean() for t in range(T)])     # equal-weight market excess return
dts_mkt = np.array([DTS[t, held[t]].mean() for t in range(T)])
assert np.isfinite(xs[held]).all() and not np.isfinite(xs[~held]).any()
print(f"{N} bonds, {J} issuers, {T} months; mean market DTS {dts_mkt.mean():.1f} (yrs x %); "
      f"{int((drow_b < T).sum())} bonds default in sample")
```


### Listing 9.2: DTS is beta: a top-minus-bottom backtest {#code-9-2}

```python
# ---------- Block 2: DTS is beta (Section 9.2) ----------
def ols(y, x):
    X = np.column_stack([np.ones_like(x), x])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[1], coef[0]                                # slope, intercept


def soft_check(ok, msg):
    print(("PASS " if ok else "WARN ") + msg)


def backtest(score, kind="dts", q=0.10, buffer=0.0, ret=None):
    """Top-minus-bottom q long-short. score (T, N): higher = buy, NaN = ineligible.
    kind 'mv': $1 per leg. kind 'dts': each leg scaled to DTS_TARGET with START-of-month DTS.
    buffer: hysteresis; a held bond stays until its percentile leaves [1-q-buffer, 1] (long)."""
    ret = xs if ret is None else ret
    out = {k: np.zeros(T) for k in ("gross", "cost", "to", "dL", "dS")}
    w_prev = np.zeros(N)
    inL, inS = np.zeros(N, bool), np.zeros(N, bool)
    for t in range(T):
        ok = held[t] & np.isfinite(score[t])               # never condition on the future return
        w_prev = np.where(held[t], w_prev, 0.0)            # defaulted bonds leave at no cost
        pct = np.full(N, -1.0)
        if ok.sum() >= 20:
            pct[ok] = pd.Series(score[t][ok]).rank(pct=True).values
        inL = ok & ((pct >= 1 - q) | (inL & (pct >= 1 - q - buffer)))
        inS = ok & ((pct <= q) | (inS & (pct <= q + buffer)))
        w = np.zeros(N)
        if inL.any() and inS.any():
            dL, dS = DTS[t, inL].mean(), DTS[t, inS].mean()
            sL, sS = (1.0, 1.0) if kind == "mv" else (DTS_TARGET / dL, DTS_TARGET / dS)
            w[inL], w[inS] = sL / inL.sum(), -sS / inS.sum()
            out["dL"][t], out["dS"][t] = dL, dS
        dw = np.abs(w - w_prev)
        out["to"][t] = dw.sum() / (2.0 * max(np.abs(w).sum(), 1e-12))
        out["cost"][t] = (dw * bonds.lcs.values / 2.0).sum()        # one-way cost = LCS / 2
        out["gross"][t] = np.nansum(w * ret[t])
        w_prev = w
    return out


dts_score = np.where(held, DTS, np.nan)
mv_dts = backtest(dts_score, "mv", q=0.20)
beta_hat = ols(mv_dts["gross"], r_mkt)[0]
beta_th = ((mv_dts["dL"] - mv_dts["dS"]) * dts_mkt).sum() / (dts_mkt ** 2).sum()
print(f"DTS-sorted dollar-neutral L/S: OLS beta {beta_hat:.3f} vs (DTS_L - DTS_S)/DTS_m = {beta_th:.3f}")
assert abs(beta_hat / beta_th - 1.0) < 0.10, "beta is not (DTS_L - DTS_S) / DTS_m"
beta_dn = ols(backtest(dts_score, "dts", q=0.20)["gross"], r_mkt)[0]
print(f"DTS-sorted DTS-neutral L/S: OLS beta {beta_dn:.4f}")
assert abs(beta_dn) < 0.05, "DTS-neutral legs should have no market beta"

not_def = np.arange(T)[:, None] != drow_b[None, :]
clean = np.where(held & not_def, xs, np.nan)
keep = np.isfinite(clean).sum(axis=0) >= 24
vol_i = np.nanstd(clean[:, keep], axis=0, ddof=1) * 100.0      # percent per month
dts_i = np.nanmean(np.where(held, DTS, np.nan)[:, keep], axis=0)
bk = pd.qcut(dts_i, 30, labels=False)
vb = pd.Series(vol_i).groupby(bk).mean().values
db = pd.Series(dts_i).groupby(bk).mean().values
slope, icpt = ols(vb, db)
r2 = np.corrcoef(vb, db)[0, 1] ** 2
print(f"vol(%/mo) = {icpt:.3f} + {slope:.4f} x DTS   R^2 = {r2:.3f}   (slope = sigma_eta)")
assert slope > 0 and r2 > 0.90, "excess-return vol should be linear in DTS (Ben Dor p.51)"
soft_check(abs(icpt) < 0.15 * vb.mean(), "vol-DTS intercept is near zero")
```


### Listing 9.3: Factor signals: excess spread to peers, SPiDER, EMC and low risk {#code-9-3}

```python
# ---------- Block 3: signals (Sections 9.3-9.6) ----------
FUND = iss[["lev", "nde_eff", "icov"]].values[IID]
PRS = iss.prs.values[IID][:, None]
SEC_D = np.eye(K_SEC)[bonds.sector.values]          # sector intercepts
MAT_D = np.eye(3)[bonds.mbucket.values][:, 1:]      # maturity-bucket shifts


def winsorize(v, lo=1.0, hi=99.0):
    a, b = np.percentile(v, [lo, hi])
    return np.clip(v, a, b)


def esp_score(with_prs=False, min_cell=30):
    """Excess spread to peers: residual of log OAS on fundamentals, with sector and maturity
    intercepts, estimated by rating each month (Dynkin p.524). Fundamentals are static here;
    in production they are point-in-time and lagged at least three months."""
    X_all = np.hstack([SEC_D, MAT_D, FUND] + ([PRS] if with_prs else []))
    out = np.full((T, N), np.nan)
    for t in range(T):
        y = np.log(s[t])
        for g in range(5):
            m = held[t] & (RAT == g)
            if m.sum() < min_cell:                 # production: pool into the adjacent rating
                continue
            coef, *_ = np.linalg.lstsq(X_all[m], y[m], rcond=None)
            out[t, m] = y[m] - X_all[m] @ coef
        ok = np.isfinite(out[t])
        out[t, ok] = winsorize(out[t, ok])
    return out


def zscore_within(x, groups, mask):
    z = np.full(x.shape, np.nan)
    for g in np.unique(groups[mask]):
        m = mask & (groups == g)
        sd = x[m].std()
        z[m] = (x[m] - x[m].mean()) / sd if sd > 0 else 0.0
    return z


def spider_score():
    lev_mult = np.clip(iss.nde_eff.values[IID], 0.1, None)   # Man p.24 floor, AFTER the NDE_CAP fix
    return np.vstack([zscore_within(np.log(s[t] / lev_mult), RAT, held[t]) for t in range(T)])


def emc_score():
    """Equity momentum in credit: mean of 1-, 3-, 6-month issuer equity returns, each per month."""
    eq, out = sim["eq_ret"], np.full((T, N), np.nan)
    for t in range(5, T):
        r1, r3, r6 = eq[t], eq[t - 2:t + 1].sum(axis=0), eq[t - 5:t + 1].sum(axis=0)
        out[t] = ((r1 + r3 / 3.0 + r6 / 6.0) / 3.0)[IID]
    return np.where(held, out, np.nan)


def low_risk_score():
    z = (D - D.mean()) / D.std() + (RAT - RAT.mean()) / RAT.std()
    return np.where(held, -z[None, :], np.nan)            # short duration, high rating = buy


def zrow(score):
    out = np.full(score.shape, np.nan)
    for t in range(T):
        ok = np.isfinite(score[t])
        if ok.sum() > 1:
            v = score[t, ok]
            out[t, ok] = (v - v.mean()) / v.std()
    return out


SIG = {"ESP": esp_score(False), "ESP+PRS": esp_score(True), "SPiDER": spider_score(),
       "EMC": emc_score(), "LowRisk": low_risk_score()}
stack = np.stack([zrow(SIG[k]) for k in ("ESP+PRS", "EMC", "LowRisk")])
cnt = np.isfinite(stack).sum(axis=0)
SIG["Composite"] = np.where(cnt > 0, np.nansum(stack, axis=0) / np.maximum(cnt, 1), np.nan)
hid_b = iss.hidden.values[IID]
top_esp = (zrow(SIG["ESP"]) > 1.28) & held
print(f"share of hidden-risk bonds in ESP top decile: {np.broadcast_to(hid_b, (T, N))[top_esp].mean():.0%} "
      f"(universe: {hid_b.mean():.0%})")
```


### Listing 9.4: Dollar-neutral against DTS-neutral factors, with costs and buffers {#code-9-4}

```python
# ---------- Block 4: dollar-neutral vs DTS-neutral factors, costs, buffers (Sections 9.2-9.8) ----------
def summarize(res, name):
    g, net = res["gross"], res["gross"] - res["cost"]
    vol = g.std(ddof=1) * np.sqrt(12)
    return {"factor": name, "gross_%": 1200 * g.mean(), "net_%": 1200 * net.mean(),
            "vol_%": 100 * vol, "IR_gross": 12 * g.mean() / vol, "IR_net": 12 * net.mean() / vol,
            "beta": ols(g, r_mkt)[0], "TO_%/mo": 100 * res["to"].mean()}


RUNS, rows = {}, []
for name, sc in SIG.items():
    for kind in ("mv", "dts"):
        RUNS[(name, kind)] = backtest(sc, kind)
        rows.append(summarize(RUNS[(name, kind)], f"{name} [{kind}]"))
table = pd.DataFrame(rows).set_index("factor")
print(table.round(2))

assert ols(RUNS[("ESP", "mv")]["gross"], r_mkt)[0] > 0.1, "dollar-neutral value should be long beta"
for (name, kind), res in RUNS.items():
    assert (res["cost"] >= 0).all() and res["cost"].sum() > 0
    if kind == "dts":
        assert abs(ols(res["gross"], r_mkt)[0]) < 0.10, f"{name}: DTS-neutral beta too large"
soft_check(table.loc["ESP+PRS [dts]", "IR_gross"] > table.loc["ESP [dts]", "IR_gross"],
           "adding the document-risk regressor improves value (Section 9.3.4)")

buf = []
for b in (0.0, 0.05, 0.10, 0.20):
    res = backtest(SIG["EMC"], "dts", buffer=b)
    buf.append({"buffer": b, "gross_%": 1200 * res["gross"].mean(), "cost_%": 1200 * res["cost"].mean(),
                "net_%": 1200 * (res["gross"] - res["cost"]).mean(), "TO_%/mo": 100 * res["to"].mean()})
buf = pd.DataFrame(buf).set_index("buffer")
print(buf.round(2))
assert (np.diff(buf["TO_%/mo"].values) < 0).all(), "turnover must fall as the buffer widens"
soft_check(buf.loc[0.10, "net_%"] > buf.loc[0.0, "net_%"], "a 10% buffer beats no buffer net of cost")
```


### Listing 9.5: Long-only DTS-matched tilt with a turnover cap {#code-9-5}

```python
# ---------- Block 5: long-only DTS-matched tilt with a turnover cap (Section 9.8) ----------
def long_only_tilt(score, k=0.5, to_cap=0.10):
    """Benchmark: equal-weight held universe. Tilt by score, cap one-way turnover, then re-match
    each rating cell's DTS contribution to the benchmark (Ben Dor p.33-34). Any weight not in
    bonds sits in duration-matched Treasuries, whose excess return is zero."""
    act, cost, to, err = np.zeros(T), np.zeros(T), np.zeros(T), np.zeros(T)
    w_prev, wmin = held[0] / held[0].sum(), np.inf
    for t in range(T):
        h = held[t]
        bm = h / h.sum()
        wp = np.where(h, w_prev, 0.0)
        z = np.where(h & np.isfinite(score[t]), score[t], 0.0)
        w = bm * np.clip(1.0 + k * z, 0.0, None)
        want = 0.5 * np.abs(w - wp).sum()
        if want > to_cap:
            w = wp + (to_cap / want) * (w - wp)
        for g in range(5):
            m = h & (RAT == g)
            if not m.any():
                continue
            tgt, got = (bm[m] * DTS[t, m]).sum(), (w[m] * DTS[t, m]).sum()
            w[m] = w[m] * (tgt / got) if got > 0 else bm[m]
            err[t] = max(err[t], abs((w[m] * DTS[t, m]).sum() - tgt))
        dw = np.abs(w - wp)
        to[t], cost[t] = 0.5 * dw.sum(), (dw * bonds.lcs.values / 2.0).sum()
        act[t] = np.nansum((w - bm) * xs[t])
        wmin, w_prev = min(wmin, w.min()), w
    return dict(active=act, cost=cost, to=to, err=err, wmin=wmin)


lo = long_only_tilt(SIG["Composite"])
te = lo["active"].std(ddof=1) * np.sqrt(12)
lo_net = lo["active"] - lo["cost"]
print(f"long-only tilt: active gross {1200 * lo['active'].mean():.2f}%/yr, net {1200 * lo_net.mean():.2f}%/yr, "
      f"TE {100 * te:.2f}%, IR net {12 * lo_net.mean() / te:.2f}, turnover {100 * lo['to'].mean():.1f}%/mo")
assert lo["wmin"] >= 0.0 and lo["err"].max() < 1e-9, "long-only and cell-DTS matching violated"
soft_check(abs(ols(lo["active"], r_mkt)[0]) < 0.05, "long-only active beta ~ 0 after cell DTS matching")
```


### Listing 9.6: Combining factors: equal-risk and maximum-IR weights {#code-9-6}

```python
# ---------- Block 6: combining factors (Section 9.7) ----------
names = ["ESP+PRS", "SPiDER", "EMC", "LowRisk"]
Fm = pd.DataFrame({k: RUNS[(k, "dts")]["gross"] for k in names}).iloc[6:]   # drop momentum warm-up
mu, sd = Fm.mean(), Fm.std(ddof=1)
IR = np.sqrt(12) * mu / sd
rho = Fm.corr().values
w_eq = np.full(len(names), 1.0 / len(names))
combo = (Fm / sd).values @ w_eq
ir_direct = np.sqrt(12) * combo.mean() / combo.std(ddof=1)
ir_formula = (w_eq @ IR.values) / np.sqrt(w_eq @ rho @ w_eq)        # equation (9.5)
w_opt = np.linalg.solve(rho, IR.values)
ir_opt = np.sqrt(IR.values @ w_opt)
print(pd.DataFrame(rho, index=names, columns=names).round(2))
print("single-factor IRs:", IR.round(2).to_dict())
print(f"equal-risk combo IR {ir_formula:.2f}; max-IR combo {ir_opt:.2f}")
assert abs(ir_direct - ir_formula) < 1e-8, "combination formula does not match the data"
assert ir_opt >= IR.abs().max() - 1e-9, "max-IR combination must beat every single factor in-sample"
off = rho[~np.eye(len(names), dtype=bool)]
if off.max() < 0.3 and ir_formula < IR.max():
    print("WARN equal-risk combo lost to the best single factor: IRs too unequal for 1/K weights")
```


### Listing 9.7: Replication under noisy prices {#code-9-7}

```python
# ---------- Block 7: the replication module, noisy prices (Section 9.9) ----------
def noisy_returns(sig_u, rng):
    """Clean prices from excess returns; observed = clean x (1 + u), u iid N(0, sig_u^2)."""
    P = 100.0 * np.vstack([np.ones(N), np.cumprod(1.0 + np.nan_to_num(xs, nan=0.0), axis=0)])
    Pn = P * (1.0 + sig_u[None, :] * rng.standard_normal(P.shape))
    rc, rn = P[1:] / P[:-1] - 1.0, Pn[1:] / Pn[:-1] - 1.0
    return np.where(held, rc, np.nan), np.where(held, rn, np.nan)


su = 0.01
rc, rn = noisy_returns(np.full(N, su), np.random.default_rng(SEED + 1))
mask = held & not_def
bias = rn[mask].mean() - rc[mask].mean()
print(f"Blume-Stambaugh: measured bias {1e4 * bias:.3f}bp/mo vs sigma_u^2 = {1e4 * su**2:.3f}bp/mo")
assert abs(bias / su**2 - 1.0) < 0.20, "noisy-price bias should be sigma_u^2 (equation 9.6)"

sig_u = np.where(RAT >= 2, 0.012, 0.004)                 # noisier marks in high yield (illustrative)
_, rn2 = noisy_returns(sig_u, np.random.default_rng(SEED + 2))
lag1 = np.full((T, N), np.nan); lag1[1:] = -rn2[:-1]     # last month's loser = buy (shares a price)
lag2 = np.full((T, N), np.nan); lag2[2:] = -rn2[:-2]     # skip a month: no shared price
tstat = lambda x: x.mean() / x.std(ddof=1) * np.sqrt(len(x))
t1 = tstat(backtest(lag1, "dts", ret=rn2)["gross"][1:])
t2 = tstat(backtest(lag2, "dts", ret=rn2)["gross"][2:])
print(f"short-term reversal on noisy prices: t = {t1:.1f}; skip-month version: t = {t2:.1f}")
assert t1 > 5.0, "the shared-price reversal 'alpha' should be large"
soft_check(abs(t2) < 3.0, "skip-month reversal is near zero: the 'alpha' was the pricing error")
print("All hard checks passed.")
```


## F.10: Chapter 10: Trend-Following & Time-Series Momentum in Credit {#code-10}

Listings from `10_ch10_trend_and_time_series_momentum.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 10.1: Excess returns, CDX price returns and roll-safe stitching {#code-10-1}

```python
# credit_tsmom.py, block 1 of 6: conventions, return construction, carry and roll guards (Sections 10.1-10.2)
# Optional data preamble. Run once, outside the chapter; nothing below touches the network.
#   import pandas as pd
#   for sid in ["BAMLH0A0HYM2", "BAMLC0A0CM"]:
#       pd.read_csv(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}").to_csv(f"{sid}.csv", index=False)
# FRED values are OAS in percent; the loader in block 6 divides by 100.
import os
import numpy as np
import pandas as pd
from scipy import stats

PPY_D, PPY_M = 252, 12                 # periods per year (MOP use 261 trading days; pin it in the spec)
D_SPR = {"HY": 4.0, "IG": 7.0}         # spread durations, illustrative
D_HY = D_SPR["HY"]


def excess_returns(spread_dec: pd.Series, dur: float) -> pd.Series:
    """r_t = s_{t-1} * (ACT/360 year fraction) - dur * (s_t - s_{t-1}); long risk is positive.
    Input: one series_id only, decimal spreads, sorted DatetimeIndex, no gaps."""
    s = spread_dec.astype(float)
    if not isinstance(s.index, pd.DatetimeIndex) or not s.index.is_monotonic_increasing:
        raise ValueError("need a sorted DatetimeIndex for ACT/360 accrual")
    if s.isna().any() or (s <= 0).any():
        raise ValueError("spreads must be positive decimals with no missing values")
    yf = s.index.to_series().diff().dt.days / 360.0
    r = s.shift(1) * yf - dur * s.diff()
    return r.iloc[1:]


def cdx_price_returns(price_pts: pd.Series, coupon_dec: float) -> pd.Series:
    """Price-quoted index (CDX HY): r = dP/100 + coupon * ACT/360. Never round-trip through spread."""
    p = price_pts.astype(float)
    yf = p.index.to_series().diff().dt.days / 360.0
    return (p.diff() / 100.0 + coupon_dec * yf).iloc[1:]


def roll_safe_returns(quotes: pd.DataFrame, dur: float) -> pd.Series:
    """quotes: columns [date, series_id, spread_dec]. The return from t-1 to t is computed inside the
    series that was on the run at t-1, so no return ever spans two series."""
    wide = quotes.pivot(index="date", columns="series_id", values="spread_dec").sort_index()
    held = wide.apply(lambda row: row.last_valid_index(), axis=1)
    idx, out = wide.index, []
    for t in range(1, len(idx)):
        k = held.iloc[t - 1]
        s0, s1 = wide.iloc[t - 1][k], wide.iloc[t][k]
        if np.isnan(s1):
            raise ValueError(f"series {k} has no quote on {idx[t].date()}; extend the overlap window")
        yf = (idx[t] - idx[t - 1]).days / 360.0
        out.append(s0 * yf - dur * (s1 - s0))
    return pd.Series(out, index=idx[1:])


# Guard 1 (carry): constant spreads earn exactly s * ACT/360.
dates = pd.bdate_range("2020-01-01", "2020-12-31")
r_flat = excess_returns(pd.Series(0.045, index=dates), D_HY)
assert abs(r_flat.sum() - 0.045 * (dates[-1] - dates[0]).days / 360.0) < 1e-10, "carry guard"

# Guard 2 (price-quoted carry): a CDX HY price pinned at 100 earns the 500 bp coupon, ACT/360.
r_par = cdx_price_returns(pd.Series(100.0, index=dates), 0.05)
assert abs(r_par.sum() - 0.05 * (dates[-1] - dates[0]).days / 360.0) < 1e-10, "price carry guard"

# Guard 3 (roll): a 10 bp roll-up between two flat series is not a loss.
q = pd.concat([
    pd.DataFrame({"date": pd.bdate_range("2025-01-02", "2025-03-31"), "series_id": 44, "spread_dec": 0.0350}),
    pd.DataFrame({"date": pd.bdate_range("2025-03-20", "2025-06-30"), "series_id": 45, "spread_dec": 0.0360}),
])
r_safe = roll_safe_returns(q, D_HY)
wide_q = q.pivot(index="date", columns="series_id", values="spread_dec").sort_index()
generic = wide_q.apply(lambda row: row[row.last_valid_index()], axis=1)   # vendor-style splice
r_naive = excess_returns(generic, D_HY)
assert abs((r_naive.sum() - r_safe.sum()) + D_HY * 0.0010) < 1e-12, "the splice shows a fake -D x 10 bp"
assert (r_safe > 0).all(), "flat spreads: every within-series return is pure carry"
print(f"block 1 ok: roll splice error = {r_naive.sum() - r_safe.sum():+.4%} of notional")
```


### Listing 10.2: Trend signals, sizing and P&L, with sign, turnover and Sheppard guards {#code-10-2}

```python
# credit_tsmom.py, block 2 of 6: signals, sizing, P&L; sign, turnover and Sheppard guards (Sections 10.2, 10.8)
def tsmom_sign(r: pd.Series, h: int) -> pd.Series:
    """sign of the trailing h-period summed excess return, known at the close of t."""
    return np.sign(r.rolling(h, min_periods=h).sum())


def ensemble_sign(r: pd.Series, hs) -> pd.Series:
    """mean of sign signals over lookbacks hs; NaN until the longest lookback is available."""
    return pd.concat([tsmom_sign(r, h) for h in hs], axis=1).mean(axis=1, skipna=False)


def crossover_signal(r: pd.Series, fast: int = 20, slow: int = 120) -> pd.Series:
    """tanh z-score of the gap between fast and slow EWMAs of the cumulative excess-return index."""
    level = r.cumsum()
    gap = level.ewm(span=fast, min_periods=fast).mean() - level.ewm(span=slow, min_periods=slow).mean()
    scale = gap.rolling(slow, min_periods=slow).std().replace(0.0, np.nan)
    return np.tanh(gap / scale)


def ewma_vol(r: pd.Series, com: float = 60.0, ppy: int = PPY_D, min_periods: int = 20) -> pd.Series:
    """annualized EWMA volatility, centre of mass `com` periods, zero-mean convention."""
    return np.sqrt((r ** 2).ewm(com=com, min_periods=min_periods).mean() * ppy)


def positions(sig: pd.Series, vol: pd.Series, target: float = 0.10,
              vol_floor: float = 0.005, lev_cap: float = 10.0) -> pd.Series:
    """w = target / max(vol, floor) * sig, capped at +/- lev_cap (notional per unit of capital)."""
    return (target / np.maximum(vol, vol_floor) * sig).clip(-lev_cap, lev_cap)


def strategy_pnl(w: pd.Series, r: pd.Series) -> pd.Series:
    """the weight known at t earns the return from t to t+1."""
    return (w.shift(1) * r).dropna()


def sharpe(x, ppy: int) -> float:
    x = pd.Series(np.asarray(x, dtype=float)).dropna()
    return float(x.mean() / x.std(ddof=1) * np.sqrt(ppy))


def max_drawdown(pnl) -> float:
    cum = np.cumsum(np.asarray(pnl, dtype=float))
    peak = np.maximum.accumulate(np.r_[0.0, cum])[1:]
    return float((cum - peak).min())


def turnover(w: pd.Series) -> float:
    return float(w.dropna().diff().abs().sum())


# Guard 4 (sign): 120 days of tightening at 1 bp/day, then 200 days of widening at 2 bp/day.
h = 60
path = np.r_[0.050 - 0.0001 * np.arange(120), 0.0381 + 0.0002 * np.arange(1, 201)]
s_path = pd.Series(path, index=pd.bdate_range("2021-01-04", periods=len(path)))
r_path = excess_returns(s_path, D_HY)
turn = 119                                          # position of the first widening return
assert (r_path.iloc[turn:] < 0).all(), "2 bp/day of widening must beat carry, Mondays included"
sig_path = tsmom_sign(r_path, h)
pnl_path = strategy_pnl(positions(sig_path, ewma_vol(r_path)), r_path)
assert (sig_path.iloc[h - 1:turn] == 1).all(), "long during the tightening"
assert (sig_path.iloc[turn + h - 1:] == -1).all(), "short within one lookback of the turn"
assert (pnl_path.loc[r_path.index[turn + h]:] > 0).all(), "a short earns money while spreads widen"

# Guard 5 (turnover identity): a unit sign strategy trades 2 units per flip.
rng = np.random.default_rng(10)
sig_n = tsmom_sign(pd.Series(rng.normal(0.0, 0.01, 5000)), 12).dropna()
assert set(np.unique(sig_n.values)) <= {-1.0, 1.0}
flips = int((sig_n.values[1:] != sig_n.values[:-1]).sum())
assert abs(turnover(sig_n) - 2 * flips) < 1e-9, "turnover = 2 x flips"

# Guard 6 (Sheppard, Section 10.8.1): the flip probability of a 12-period sign is arccos(11/12)/pi.
sg = tsmom_sign(pd.Series(np.random.default_rng(11).standard_normal(200_000)), 12).dropna().values
flip_rate = float((sg[1:] != sg[:-1]).mean())
assert abs(flip_rate - np.arccos(11 / 12) / np.pi) < 0.01, flip_rate
print(f"block 2 ok: flip rate {flip_rate:.4f} vs {np.arccos(11 / 12) / np.pi:.4f}; "
      f"turnover per year (monthly, h=12) = {2 * 12 * np.arccos(11 / 12) / np.pi:.2f}")
```


### Listing 10.3: No free lunch under a random walk: spread changes with persistence {#code-10-3}

```python
# credit_tsmom.py, block 3 of 6: no free lunch under a random walk, real money under persistence (Section 10.2)
def simulate_ar1_changes(n: int, phi: float, sd: float, seed: int, burn: int = 200) -> np.ndarray:
    """monthly spread changes with AR(1) persistence phi (phi = 0 is a random walk in spreads)."""
    e = np.random.default_rng(seed).normal(0.0, sd, n + burn)
    x = np.empty_like(e)
    x[0] = e[0]
    for t in range(1, len(e)):
        x[t] = phi * x[t - 1] + e[t]
    return x[burn:]


N_M = 6000                                   # 500 synthetic years, about 478 more than CDX has existed
sd_m = 0.25 * 0.045 / np.sqrt(PPY_M)         # 25% relative vol at a 450 bp level, per month
H_M = [1, 3, 6, 12]
results = {}
for label, phi, seed in [("random walk", 0.0, 1), ("phi = 0.25", 0.25, 2)]:
    r_sim = pd.Series(-D_HY * simulate_ar1_changes(N_M, phi, sd_m, seed))     # MTM-only returns
    results[label] = sharpe(strategy_pnl(ensemble_sign(r_sim, H_M), r_sim), PPY_M)
years = N_M / PPY_M
assert abs(results["random walk"]) < 3.5 / np.sqrt(years), results
assert results["phi = 0.25"] - results["random walk"] >= 0.3, results
print("block 3 ok:", {k: round(v, 2) for k, v in results.items()})
```


### Listing 10.4: Volatility scaling is DTS scaling: log-OU spreads and Ben Dor's law {#code-10-4}

```python
# credit_tsmom.py, block 4 of 6: volatility scaling is DTS scaling (Section 10.3)
def simulate_log_ou_spreads(n_days: int, s_bar: float = 0.045, kappa: float = 0.5, sigma: float = 0.25,
                            seed: int = 3, start: str = "1990-01-01") -> pd.Series:
    """daily spreads with log-OU dynamics, so sd(ds) is proportional to s (Ben Dor's law, beta = sigma)."""
    dt = 1.0 / PPY_D
    z = np.random.default_rng(seed).standard_normal(n_days)
    x = np.empty(n_days)
    x[0] = np.log(s_bar)
    for t in range(1, n_days):
        x[t] = x[t - 1] + kappa * (np.log(s_bar) - x[t - 1]) * dt + sigma * np.sqrt(dt) * z[t]
    return pd.Series(np.exp(x), index=pd.bdate_range(start, periods=n_days))


def beta_dts(spread: pd.Series, win: int = 63) -> float:
    """zero-intercept regression of non-overlapping realized spread-change vol on spread level."""
    vol = spread.diff().rolling(win).std() * np.sqrt(PPY_D)
    lvl = spread.rolling(win).mean()
    sel = np.arange(win, len(spread), win)
    v, l = vol.iloc[sel].values, lvl.iloc[sel].values
    return float((v * l).sum() / (l ** 2).sum())


s_d = simulate_log_ou_spreads(PPY_D * 40)
r_d = excess_returns(s_d, D_HY)
beta_hat = beta_dts(s_d)
assert abs(beta_hat / 0.25 - 1.0) < 0.20, beta_hat

s_now = s_d.reindex(r_d.index)              # spread known at the close of t
sig_d = tsmom_sign(r_d, 60)
vols = {"ewma": ewma_vol(r_d), "dts": beta_hat * D_HY * s_now}
vols["max"] = np.maximum(vols["ewma"], vols["dts"])
for name, vol in vols.items():
    realized = strategy_pnl(positions(sig_d, vol, target=0.10), r_d).std() * np.sqrt(PPY_D)
    print(f"block 4: {name:>4} sizing, realized vol {realized:.3f} (target 0.100)")
    if name in ("ewma", "dts"):
        assert abs(realized / 0.10 - 1.0) < 0.25, (name, realized)

# Constant-DTS identity: |w| * D * s = target / beta wherever the leverage cap does not bind.
w_dts = positions(sig_d, vols["dts"], target=0.10).dropna()
uncapped = w_dts.abs() < 10.0 - 1e-9
assert uncapped.mean() > 0.99, "leverage cap binding too often; check the floor and the spread units"
expo = w_dts[uncapped].abs() * D_HY * s_now.reindex(w_dts.index)[uncapped]
assert np.allclose(expo.values, 0.10 / beta_hat), "vol targeting in credit = constant DTS exposure"
print(f"block 4 ok: beta_DTS = {beta_hat:.3f}; constant DTS exposure = {0.10 / beta_hat:.3f}")
```


### Listing 10.5: Trend plus carry under the D3 model, on an expanding window {#code-10-5}

```python
# credit_tsmom.py, block 5 of 6: trend plus carry under D3, estimated on an expanding window (Section 10.4)
def simulate_d3(n: int, kappa: float = 0.03, phi: float = 0.25, s_bar: float = 0.045,
                beta: float = 0.25, floor: float = 0.0025, seed: int = 4) -> np.ndarray:
    """monthly D3: ds_{t+1} = kappa (s_bar - s_t) + phi ds_t + eps, sd(eps) = beta s_t sqrt(dt)."""
    rng, dt = np.random.default_rng(seed), 1.0 / PPY_M
    s = np.full(n, s_bar)
    for t in range(1, n - 1):
        eps = beta * s[t] * np.sqrt(dt) * rng.standard_normal()
        s[t + 1] = max(s[t] + kappa * (s_bar - s[t]) + phi * (s[t] - s[t - 1]) + eps, floor)
    return s


def d3_components(s: np.ndarray, dur: float, min_obs: int = 120) -> dict:
    """carry, value and trend forecasts of r_{t+1}; (a, b_s, phi) re-estimated using data up to t only."""
    n, dt = len(s), 1.0 / PPY_M
    ds = np.r_[np.nan, np.diff(s)]
    comp = {k: np.full(n, np.nan) for k in ("carry", "value", "trend", "kappa", "phi")}
    for t in range(min_obs, n - 1):
        k = np.arange(1, t)                               # regress ds[k+1] on [1, s[k], ds[k]], k+1 <= t
        X = np.column_stack([np.ones(len(k)), s[k], ds[k]])
        a, b_s, phi_hat = np.linalg.lstsq(X, ds[k + 1], rcond=None)[0]
        comp["carry"][t] = s[t] * dt
        comp["value"][t] = -dur * (a + b_s * s[t])        # = dur * kappa * (s_t - s_bar), no division by kappa
        comp["trend"][t] = -dur * phi_hat * ds[t]
        comp["kappa"][t], comp["phi"][t] = -b_s, phi_hat
    return comp


N_D3 = 1200
s_m = simulate_d3(N_D3)
dt_m = 1.0 / PPY_M
r_m = np.r_[np.nan, s_m[:-1] * dt_m - D_HY * np.diff(s_m)]       # r_m[t]: return from t-1 to t
c = d3_components(s_m, D_HY)
var_m = (D_HY * 0.25 * s_m) ** 2 * dt_m                            # DTS-law variance forecast
sleeves = {"carry+value": c["carry"] + c["value"], "trend": c["trend"],
           "blend": c["carry"] + c["value"] + c["trend"]}
pnl_m = {name: (f / var_m)[:-1] * r_m[1:] for name, f in sleeves.items()}   # mean-variance weights
assert np.allclose(sleeves["blend"], sleeves["carry+value"] + sleeves["trend"], equal_nan=True)
assert c["phi"][N_D3 - 2] > 0.10, "the expanding-window phi should find the persistence (true 0.25)"
ok = np.isfinite(pnl_m["trend"]) & np.isfinite(pnl_m["carry+value"])
rho_tc = float(np.corrcoef(pnl_m["trend"][ok], pnl_m["carry+value"][ok])[0, 1])
for name, p in pnl_m.items():
    pf = p[np.isfinite(p)]
    pf = pf / (pf.std() * np.sqrt(PPY_M)) * 0.10                  # scaled to 10% vol ex post, display only
    print(f"block 5: {name:>11} Sharpe {sharpe(pf, PPY_M):+.2f}, max DD at 10% vol {max_drawdown(pf):+.1%}")
print(f"block 5 ok: kappa_hat {c['kappa'][N_D3 - 2]:.3f} (true 0.03), phi_hat {c['phi'][N_D3 - 2]:.3f} "
      f"(true 0.25), corr(trend, carry+value) {rho_tc:+.2f}")
```


### Listing 10.6: Stale-mark lead-lag, whipsaw, convexity and the crisis table {#code-10-6}

```python
# credit_tsmom.py, block 6 of 6: stale-mark lead-lag, whipsaw, convexity, crisis table (Sections 10.5-10.7)
def ols_hac(y, X, lags: int = 4):
    """OLS coefficients, Newey-West (Bartlett) standard errors and t-statistics; X includes a constant."""
    y, X = np.asarray(y, dtype=float), np.asarray(X, dtype=float)
    XtX_inv = np.linalg.inv(X.T @ X)
    b = XtX_inv @ X.T @ y
    Xu = X * (y - X @ b)[:, None]
    S = Xu.T @ Xu
    for L in range(1, lags + 1):
        G = Xu[L:].T @ Xu[:-L]
        S += (1.0 - L / (lags + 1.0)) * (G + G.T)
    se = np.sqrt(np.diag(XtX_inv @ S @ XtX_inv))
    return b, se, b / se


def granger_f(y_next, own_lag, x_lag):
    """F-test that x_lag adds nothing to y_next = a + c * own_lag (+ b * x_lag) + e."""
    y = np.asarray(y_next, dtype=float)
    n = len(y)
    Xu = np.column_stack([np.ones(n), own_lag, x_lag])
    Xr = np.column_stack([np.ones(n), own_lag])
    rss = lambda X: float(np.sum((y - X @ np.linalg.lstsq(X, y, rcond=None)[0]) ** 2))
    F = (rss(Xr) - rss(Xu)) / (rss(Xu) / (n - Xu.shape[1]))
    return F, float(stats.f.sf(F, 1, n - Xu.shape[1]))


# (a) Stale marks manufacture an equity "lead" of about p(1-p) beta_ce (Section 10.5.3).
rng = np.random.default_rng(5)
n_w, p_print, beta_ce = 2000, 0.5, 0.2
r_eq = rng.normal(0.0, 0.025, n_w)                                # weekly equity returns
dP = beta_ce * r_eq + rng.normal(0.0, 0.003, n_w)                  # true credit: contemporaneous only
P = np.cumsum(dP)
printed = rng.random(n_w) < p_print
m = P.copy()
for t in range(1, n_w):
    if not printed[t]:
        m[t] = m[t - 1]                                          # no print this week: the mark goes stale
dm = np.r_[0.0, np.diff(m)]
ti = np.arange(1, n_w - 1)
_, _, t_mark = ols_hac(dm[ti + 1], np.column_stack([np.ones(len(ti)), dm[ti], r_eq[ti]]))
_, _, t_true = ols_hac(dP[ti + 1], np.column_stack([np.ones(len(ti)), dP[ti], r_eq[ti]]))
F_mark, p_mark = granger_f(dm[ti + 1], dm[ti], r_eq[ti])
assert t_mark[2] > 3.0, "stale marks should show a significant equity lead"
assert abs(t_true[2]) < 4.0, "true prices have no lead by construction"
print(f"block 6a: equity->mark t = {t_mark[2]:.1f} (Granger p = {p_mark:.1e}); equity->true t = {t_true[2]:.1f}")


# (b) Whipsaw arithmetic (Section 10.6.2): the follower's P&L on a stylized V is 2d(T - 4L)/T.
def v_capture(d: float, T: int, L: int) -> float:
    half = T // 2
    dp = np.r_[np.full(half, -d / half), np.full(half, d / half)]
    t = np.arange(2 * half)
    pos = np.where((t >= L) & (t < half + L), -1.0, 1.0)
    return float((pos * dp).sum())


for T, L in [(20, 3), (20, 6), (60, 10), (40, 12)]:
    assert np.isclose(v_capture(1.0, T, L), 2.0 * (T - 4 * L) / T), (T, L)

# (c) The convexity regression must find the smile in a payoff that is a smile by construction ...
x = rng.normal(0.0, 0.05, 400)
b_cx, _, t_cx = ols_hac(np.abs(x) + rng.normal(0.0, 0.01, 400),
                        np.column_stack([np.ones(400), x, x ** 2]), lags=2)
assert b_cx[2] > 0 and t_cx[2] > 3.0
# ... and then we ask the same question of the persistent-trend simulation, on non-overlapping quarters.
r_tr = pd.Series(-D_HY * simulate_ar1_changes(N_M, 0.25, sd_m, seed=2))
pnl_tr = strategy_pnl(ensemble_sign(r_tr, H_M), r_tr)
qtr = pd.DataFrame({"tf": pnl_tr, "mkt": r_tr.reindex(pnl_tr.index)}).groupby(np.arange(len(pnl_tr)) // 3).sum()
b_q, _, t_q = ols_hac(qtr["tf"], np.column_stack([np.ones(len(qtr)), qtr["mkt"], qtr["mkt"] ** 2]), lags=2)
print(f"block 6c: quarterly smile b2 = {b_q[2]:.2f} (t = {t_q[2]:.1f}); a positive b2 is the receipt for momentum")

# (d) Crisis-window table on real data, if the FRED CSV from the block 1 preamble is present.
CRISES = {"GFC": ("2007-06-01", "2009-06-30"), "COVID": ("2020-02-01", "2020-06-30"),
          "2022": ("2022-01-01", "2022-10-31"), "Tariffs 2025": ("2025-02-01", "2025-05-31")}


def crisis_table(pnl: pd.Series, bench: pd.Series) -> pd.DataFrame:
    rows = []
    for name, (a, b) in CRISES.items():
        p, bm = pnl.loc[a:b], bench.loc[a:b]
        if len(p) < 20:
            continue                                             # window not covered by the data
        rows.append({"window": name, "strategy": p.sum(), "long_risk": bm.sum(), "max_dd": max_drawdown(p)})
    return pd.DataFrame(rows)


def perf_summary(pnl: pd.Series, w: pd.Series, ppy: int) -> dict:
    yrs = len(pnl) / ppy
    return {"ann_ret": pnl.mean() * ppy, "ann_vol": pnl.std() * np.sqrt(ppy), "sharpe": sharpe(pnl, ppy),
            "max_dd": max_drawdown(pnl), "turnover_per_yr": turnover(w) / yrs}


fred = "BAMLH0A0HYM2.csv"
if os.path.exists(fred):
    raw = pd.read_csv(fred)
    oas = pd.to_numeric(raw.iloc[:, 1], errors="coerce") / 100.0      # FRED writes "." for missing
    hy = pd.Series(oas.values, index=pd.to_datetime(raw.iloc[:, 0])).dropna().sort_index()
    r_hy = excess_returns(hy, D_HY)
    sig_hy = 0.5 * ensemble_sign(r_hy, [21, 63, 126, 252]) + 0.5 * crossover_signal(r_hy)
    vol_hy = np.maximum(ewma_vol(r_hy), beta_dts(hy) * D_HY * hy.reindex(r_hy.index))
    w_hy = positions(sig_hy, vol_hy)
    pnl_hy = strategy_pnl(w_hy, r_hy)
    print(perf_summary(pnl_hy, w_hy, PPY_D))
    print(crisis_table(pnl_hy, r_hy))
else:
    print("block 6d: FRED CSV not found; crisis table skipped (see the block 1 preamble).")
print("all blocks ok")
```


## F.11: Chapter 11: Defensive Systematic High Yield {#code-11}

Listings from `11_ch11_defensive_systematic_high_yield.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 11.1: Capture ratios and asymmetric beta {#code-11-1}

```python
# Block 1: capture ratios and asymmetric beta (Section 11.2)
import numpy as np
import pandas as pd
from scipy import optimize, special, stats

RNG_SEED = 11


def capture_ratios(rp, rb, floor=1e-4):
    """Arithmetic upside/downside capture on benchmark-defined regimes."""
    rp = np.asarray(rp, dtype=float)
    rb = np.asarray(rb, dtype=float)
    if rp.shape != rb.shape or rp.ndim != 1:
        raise ValueError("rp and rb must be aligned 1-D arrays")
    up, dn = rb > 0, rb < 0
    if up.sum() < 3 or dn.sum() < 3:
        raise ValueError("need at least 3 up and 3 down benchmark months")
    mu_up, mu_dn = rb[up].mean(), rb[dn].mean()
    if mu_up < floor or abs(mu_dn) < floor:
        raise ValueError("benchmark regime mean too close to zero; capture undefined")
    return rp[up].mean() / mu_up, rp[dn].mean() / mu_dn


def asymmetric_beta(rp, rb):
    """OLS of rp on [1, max(rb,0), min(rb,0)]; good defense means beta_dn < beta_up."""
    rp = np.asarray(rp, dtype=float)
    rb = np.asarray(rb, dtype=float)
    X = np.column_stack([np.ones_like(rb), np.maximum(rb, 0.0), np.minimum(rb, 0.0)])
    coef, *_ = np.linalg.lstsq(X, rp, rcond=None)
    return {"alpha": coef[0], "beta_up": coef[1], "beta_dn": coef[2]}


rng = np.random.default_rng(RNG_SEED)
rb_demo = rng.normal(0.004, 0.022, 240)          # 20 years of monthly HY excess returns (synthetic)

# Sanity 1: a pure beta tilt has U == D == beta exactly.
U, D = capture_ratios(0.9 * rb_demo, rb_demo)
assert abs(U - 0.9) < 1e-12 and abs(D - 0.9) < 1e-12

# Sanity 2: positive alpha opens the gap U > D (the identity of Section 11.2.1).
U_a, D_a = capture_ratios(0.001 + 0.9 * rb_demo, rb_demo)
assert U_a > 0.9 > D_a

# Sanity 3: the identity U - D = alpha * (1/mu_up + 1/|mu_dn|) holds exactly with zero residual.
mu_up = rb_demo[rb_demo > 0].mean()
mu_dn = rb_demo[rb_demo < 0].mean()
assert abs((U_a - D_a) - 0.001 * (1 / mu_up + 1 / abs(mu_dn))) < 1e-12

# Sanity 4: the asymmetric regression sees through a beta tilt and recovers real convexity.
tilt = asymmetric_beta(0.9 * rb_demo, rb_demo)
assert abs(tilt["beta_up"] - 0.9) < 1e-10 and abs(tilt["beta_dn"] - 0.9) < 1e-10
convex_rp = (0.0005 + 1.0 * np.maximum(rb_demo, 0) + 0.8 * np.minimum(rb_demo, 0)
             + rng.normal(0.0, 0.002, rb_demo.size))
cvx = asymmetric_beta(convex_rp, rb_demo)
assert cvx["beta_dn"] < cvx["beta_up"] - 0.1
print(f"beta tilt: U={U:.4f} D={D:.4f} | convex: beta_up={cvx['beta_up']:.3f} "
      f"beta_dn={cvx['beta_dn']:.3f} alpha/yr={12 * cvx['alpha']:.4f}")
```


### Listing 11.2: Merton inversion, distance to default and the empirical PD map {#code-11-2}

```python
# Block 2: Merton inversion, distance-to-default, empirical PD map (Section 11.3)

def _merton_call(V, sigma_V, F, r, T):
    sq = sigma_V * np.sqrt(T)
    d1 = (np.log(V / F) + (r + 0.5 * sigma_V ** 2) * T) / sq
    d2 = d1 - sq
    E = V * stats.norm.cdf(d1) - F * np.exp(-r * T) * stats.norm.cdf(d2)
    return E, d1, d2


def merton_solve(E, sigma_E, F, r, T=1.0):
    """Recover (V, sigma_V) from observed (E, sigma_E) by nested bracketed root searches."""
    if min(E, sigma_E, F, T) <= 0:
        raise ValueError("E, sigma_E, F, T must be positive; route issuer to accounting-only PD")
    v_hi = E + 2.0 * F * max(1.0, np.exp(-r * T))

    def V_of(sV):
        return optimize.brentq(lambda V: _merton_call(V, sV, F, r, T)[0] - E,
                               E, v_hi, xtol=1e-12, rtol=1e-14, maxiter=500)

    def gap(sV):
        V = V_of(sV)
        return sV * V * stats.norm.cdf(_merton_call(V, sV, F, r, T)[1]) - sigma_E * E

    if gap(sigma_E) <= 0.0:          # no leverage effect left (F negligible)
        return V_of(sigma_E), sigma_E
    sV = optimize.brentq(gap, 1e-6, sigma_E, xtol=1e-14, rtol=1e-14, maxiter=500)
    return V_of(sV), sV


def distance_to_default(V, sigma_V, F, mu, T=1.0):
    return (np.log(V / F) + (mu - 0.5 * sigma_V ** 2) * T) / (sigma_V * np.sqrt(T))


def kmv_default_point(std, ltd):
    return std + 0.5 * ltd


def empirical_pd(dd, a=-0.718, b=0.9718, pd_floor=1e-4, pd_cap=0.35):
    """Illustrative monotone DD -> 12m PD map: PD(4) ~ 1%, PD(0.5) ~ 30%, capped at 35%."""
    return np.clip(np.exp(a - b * np.asarray(dd, dtype=float)), pd_floor, pd_cap)


# Sanity 1: round trip. Generate (E, sigma_E) from known (V, sigma_V), then recover them.
for V0, sV0, F0 in [(100.0, 0.30, 75.0), (100.0, 0.25, 95.0)]:
    E0, d1_0, _ = _merton_call(V0, sV0, F0, 0.04, 1.0)
    sE0 = stats.norm.cdf(d1_0) * sV0 * V0 / E0
    V_hat, sV_hat = merton_solve(E0, sE0, F0, 0.04, 1.0)
    assert abs(V_hat / V0 - 1) < 1e-6 and abs(sV_hat / sV0 - 1) < 1e-6
    assert sV_hat < sE0                       # leverage effect: asset vol below equity vol

# Sanity 2: the empirical map is monotone and the Gaussian map is the Kaz trap.
grid = np.linspace(-2.0, 8.0, 201)
assert np.all(np.diff(empirical_pd(grid)) <= 0.0)
assert abs(float(empirical_pd(4.0)) - 0.01) < 5e-4
assert stats.norm.cdf(-4.0) < 1e-4            # 3.2e-5: "three in a hundred thousand"

# A sponsor-levered B issuer (illustrative, $mm): E=2,000, sigma_E=55%, STD=600, LTD=3,000.
F_hy = kmv_default_point(600.0, 3000.0)
V_hy, sV_hy = merton_solve(2000.0, 0.55, F_hy, 0.04, 1.0)
dd_hy = distance_to_default(V_hy, sV_hy, F_hy, mu=0.06)
assert dd_hy > 0 and float(empirical_pd(dd_hy)) > stats.norm.cdf(-dd_hy)
print(f"V={V_hy:,.0f} sigma_V={sV_hy:.3f} DD={dd_hy:.2f} "
      f"PD_emp={float(empirical_pd(dd_hy)):.3%} vs N(-DD)={stats.norm.cdf(-dd_hy):.3%}")
```


### Listing 11.3: A synthetic HY panel, dynamic logit, clustered standard errors and purged issuer-grouped CV {#code-11-3}

```python
# Block 3: synthetic HY panel, dynamic logit, clustered SEs, purged issuer-grouped CV (Section 11.4)

def simulate_hy_universe(n_issuers=600, n_months=120, de_share=0.30, seed=RNG_SEED):
    """Issuer-month panel: persistent latent DD with a common factor (default clustering),
    a liquidity-runway covariate capped at 13 weeks, and a distressed-exchange flag."""
    g = np.random.default_rng(seed)
    mu_dd = g.uniform(0.5, 5.5, n_issuers)
    dd = mu_dd + g.normal(0.0, 0.5, n_issuers)
    runway = np.clip(g.normal(9.0, 3.0, n_issuers), 0.0, 13.0)
    alive = np.ones(n_issuers, dtype=bool)
    default_month = np.full(n_issuers, -1)
    DD = np.full((n_months, n_issuers), np.nan)
    RUN = np.full_like(DD, np.nan)
    EXR = np.full_like(DD, np.nan)
    for t in range(n_months):
        dd_new = (mu_dd + 0.92 * (dd - mu_dd) + g.normal(0.0, 0.20)
                  + g.normal(0.0, 0.35, n_issuers))
        exret = 0.08 * (dd_new - dd) + g.normal(0.0, 0.03, n_issuers)
        dd = dd_new
        runway = np.clip(runway + 0.6 * np.tanh(dd - 1.5) + g.normal(0.0, 0.7, n_issuers), 0.0, 13.0)
        DD[t, alive] = dd[alive] + g.normal(0.0, 0.25, alive.sum())
        RUN[t, alive] = runway[alive]
        EXR[t, alive] = exret[alive]
        hazard = special.expit(-3.4 - 1.0 * dd - 0.12 * runway)     # true monthly hazard
        d_now = alive & (g.random(n_issuers) < hazard)
        default_month[d_now] = t
        alive &= ~d_now
    t_idx, i_idx = np.nonzero(~np.isnan(DD))
    panel = pd.DataFrame({"issuer_id": i_idx, "month": t_idx, "DD": DD[t_idx, i_idx],
                          "runway": RUN[t_idx, i_idx], "exret": EXR[t_idx, i_idx]})
    dm = default_month[i_idx]
    panel["default_12m"] = ((dm >= t_idx) & (dm < t_idx + 12)).astype(int)
    is_de = g.random(n_issuers) < de_share
    panel["de_flag"] = ((panel["default_12m"].to_numpy() == 1) & is_de[i_idx]).astype(int)
    panel = panel[panel["month"] <= n_months - 12].reset_index(drop=True)   # censored labels out
    return panel, default_month


def lag_features(panel, cols, lag):
    out = panel.sort_values(["issuer_id", "month"]).copy()
    lagged_cols = [c + "_lag" for c in cols]
    for c, cl in zip(cols, lagged_cols):
        out[cl] = out.groupby("issuer_id")[c].shift(lag)
    return out.dropna(subset=lagged_cols).reset_index(drop=True)


def fit_logit(X, y, groups=None, max_iter=100):
    """Newton-Raphson logit with step halving; issuer-clustered sandwich SEs when groups given."""
    X1 = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
    y = np.asarray(y, dtype=float)
    ybar = np.clip(y.mean(), 1e-6, 1 - 1e-6)
    b = np.zeros(X1.shape[1])
    b[0] = np.log(ybar / (1 - ybar))

    def nll(beta):
        z = X1 @ beta
        return np.sum(np.logaddexp(0.0, z) - y * z)

    f = nll(b)
    for _ in range(max_iter):
        p = special.expit(X1 @ b)
        H = (X1 * (p * (1 - p))[:, None]).T @ X1
        step = np.linalg.solve(H + 1e-10 * np.eye(len(b)), X1.T @ (y - p))
        t = 1.0
        while nll(b + t * step) > f + 1e-12 and t > 1e-8:
            t *= 0.5
        b = b + t * step
        f = nll(b)
        if np.max(np.abs(t * step)) < 1e-9:
            break
    p = special.expit(X1 @ b)
    Hinv = np.linalg.inv((X1 * (p * (1 - p))[:, None]).T @ X1)
    if groups is None:
        cov = Hinv
    else:
        G = pd.DataFrame(X1 * (y - p)[:, None]).groupby(np.asarray(groups)).sum().to_numpy()
        cov = Hinv @ (G.T @ G) @ Hinv
    return b, np.sqrt(np.diag(cov))


def predict_logit(b, X):
    return special.expit(b[0] + np.asarray(X, dtype=float) @ b[1:])


def prior_shift(p, pi_sample, pi_pop):
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1 - 1e-12)
    shift = np.log(pi_pop * (1 - pi_sample) / (pi_sample * (1 - pi_pop)))
    return special.expit(special.logit(p) + shift)


def auc(score, default):
    """Mann-Whitney AUC: P(score of a defaulter > score of a survivor); ties count one half."""
    score = np.asarray(score, dtype=float)
    d = np.asarray(default).astype(bool)
    n1, n0 = int(d.sum()), int((~d).sum())
    if n1 == 0 or n0 == 0:
        return np.nan
    ranks = stats.rankdata(score)
    return (ranks[d].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def purged_group_cv(panel, n_splits=5, embargo=12, seed=RNG_SEED):
    """Issuer-disjoint folds; training rows within `embargo` months of the test block are purged."""
    g = np.random.default_rng(seed)
    issuers = g.permutation(panel["issuer_id"].unique())
    fold_of = np.empty(int(issuers.max()) + 1, dtype=int)
    for k, chunk in enumerate(np.array_split(issuers, n_splits)):
        fold_of[chunk] = k
    f = fold_of[panel["issuer_id"].to_numpy()]
    m = panel["month"].to_numpy()
    for k, block in enumerate(np.array_split(np.sort(panel["month"].unique()), n_splits)):
        lo, hi = block[0], block[-1]
        test = (f == k) & (m >= lo) & (m <= hi)
        train = (f != k) & ((m < lo - embargo) | (m > hi + embargo))
        yield np.flatnonzero(train), np.flatnonzero(test)


FEATURES = ["DD", "runway", "exret"]
XCOLS = [c + "_lag" for c in FEATURES]
panel, default_month = simulate_hy_universe()
lagged = lag_features(panel, FEATURES, lag=3)
X_all, y_all = lagged[XCOLS].to_numpy(), lagged["default_12m"].to_numpy()
assert (default_month >= 0).sum() >= 50                       # enough defaults to say anything

b_full, se_cl = fit_logit(X_all, y_all, groups=lagged["issuer_id"])
_, se_naive = fit_logit(X_all, y_all)
assert b_full[1] < 0 and b_full[2] < 0       # higher DD, longer runway -> lower PD
assert se_cl[1] > se_naive[1]                # overlapping 12m labels: clustering widens SEs

oos = []
for tr, te in purged_group_cv(lagged):
    if y_all[te].sum() == 0:
        print("fold skipped: no defaults in test block")
        continue
    b_cv, _ = fit_logit(X_all[tr], y_all[tr])
    oos.append(auc(predict_logit(b_cv, X_all[te]), y_all[te]))
oos_auc = float(np.mean(oos))
assert len(oos) >= 3 and oos_auc > 0.75

# Look-ahead warning: a feature that peeks at the label looks like genius.
g_leak = np.random.default_rng(RNG_SEED + 1)
X_leak = np.column_stack([X_all, y_all + g_leak.normal(0.0, 0.3, len(y_all))])
b_leak, _ = fit_logit(X_leak, y_all)
auc_leak = auc(predict_logit(b_leak, X_leak), y_all)
assert auc_leak > 0.97

# Label contamination: treating distressed exchanges as survival understates PD.
y_hard = ((y_all == 1) & (lagged["de_flag"].to_numpy() == 0)).astype(int)
b_hard, _ = fit_logit(X_all, y_hard)
assert predict_logit(b_hard, X_all).mean() < 0.9 * y_all.mean()

assert abs(float(prior_shift(0.5, 0.5, 0.03)) - 0.03) < 1e-12
print(f"defaults={(default_month >= 0).sum()} beta_DD={b_full[1]:.3f} "
      f"SE ratio clustered/naive={se_cl[1] / se_naive[1]:.2f} OOS AUC={oos_auc:.3f} "
      f"leaky AUC={auc_leak:.3f} (WARNING: look-ahead)")
```


### Listing 11.4: CAP curve, accuracy ratio, hit rate and the economics of exclusion {#code-11-4}

```python
# Block 4: CAP curve, accuracy ratio, hit rate, exclusion economics (Section 11.5)

def cap_curve(score, default):
    order = np.argsort(-np.asarray(score, dtype=float), kind="mergesort")
    d = np.asarray(default, dtype=float)[order]
    if d.sum() == 0:
        raise ValueError("no defaults: CAP undefined")
    x = np.concatenate([[0.0], np.arange(1, d.size + 1) / d.size])
    y = np.concatenate([[0.0], np.cumsum(d) / d.sum()])
    return x, y


def accuracy_ratio(score, default):
    x, y = cap_curve(score, default)
    area = np.sum(np.diff(x) * (y[1:] + y[:-1]) / 2.0)        # trapezoid rule
    f = float(np.mean(default))
    return (2.0 * area - 1.0) / (1.0 - f)


def hit_rate(score, default, q):
    x, y = cap_curve(score, default)
    return float(np.interp(q, x, y))


def exclusion_active_return(q, pi_X, pi_K, s_X, s_K, L):
    """q * [(pi_X - pi_K) * L - (s_X - s_K)], all decimals per year, P-measure."""
    return q * ((pi_X - pi_K) * L - (s_X - s_K))


# Sanity 1: AR = 2*AUC - 1 exactly for untied scores.
g4 = np.random.default_rng(RNG_SEED + 4)
dflt = (g4.random(5000) < 0.05).astype(int)
sc = g4.normal(0.0, 1.0, 5000) + 1.2 * dflt
assert abs(accuracy_ratio(sc, dflt) - (2 * auc(sc, dflt) - 1)) < 1e-10

# Sanity 2: a perfect ranking scores AR = 1; random scores average AR ~ 0 over 20 seeds.
assert abs(accuracy_ratio(dflt + 0.5 * g4.random(5000), dflt) - 1.0) < 1e-9
ar_rand = []
for s in range(20):
    gs = np.random.default_rng(1000 + s)
    ar_rand.append(accuracy_ratio(gs.random(5000), (gs.random(5000) < 0.05).astype(int)))
assert abs(np.mean(ar_rand)) < 0.05

# Sanity 3: the worked example of Section 11.5.2.
act_20 = exclusion_active_return(0.20, 0.77 * 0.03 / 0.20, 0.23 * 0.03 / 0.80, 0.0420, 0.0, 0.6)
act_40 = exclusion_active_return(0.40, 0.77 * 0.03 / 0.40, 0.23 * 0.03 / 0.60, 0.0300, 0.0, 0.6)
assert act_20 > 0 > act_40

# Apply to the Block 3 panel: in-sample PDs from the full model, one row per issuer-month.
pd_in = predict_logit(b_full, X_all)
print(f"panel AR={accuracy_ratio(pd_in, y_all):.3f} AUC={auc(pd_in, y_all):.3f} "
      f"HR(10/20/30%)={[round(hit_rate(pd_in, y_all, q), 2) for q in (0.1, 0.2, 0.3)]} "
      f"active 20%={act_20:.4%} active 40%={act_40:.4%}")
```


### Listing 11.5: The DTS-neutral defensive portfolio {#code-11-5}

```python
# Block 5: DTS-neutral defensive portfolio (Section 11.7)

def defensive_portfolio(pd_hat, spread, dur, bench_w, L=0.6, exclude_q=0.20,
                        issuer_cap=0.03, tilt=1.0):
    pd_hat, spread, dur, bench_w = (np.asarray(a, dtype=float) for a in (pd_hat, spread, dur, bench_w))
    dts = dur * spread
    dts_bench = float(bench_w @ dts)
    keep = pd_hat <= np.quantile(pd_hat, 1.0 - exclude_q)
    score = (spread - pd_hat * L) / dts                       # default-adjusted carry per unit DTS
    zk = (score[keep] - score[keep].mean()) / score[keep].std()
    w0 = bench_w[keep] * np.exp(tilt * np.clip(zk, -2.0, 2.0))
    w0 = w0 / w0.sum()
    dk = dts[keep]
    if not (dk.min() <= dts_bench <= dk.max()):
        raise ValueError("benchmark DTS unreachable long-only: refuse rather than lever")
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones_like(w)},
            {"type": "eq", "fun": lambda w: w @ dk / dts_bench - 1.0, "jac": lambda w: dk / dts_bench}]
    res = optimize.minimize(lambda w: 5e3 * np.sum((w - w0) ** 2), w0,
                            jac=lambda w: 1e4 * (w - w0), method="SLSQP",
                            bounds=[(0.0, issuer_cap)] * int(keep.sum()), constraints=cons,
                            options={"maxiter": 500, "ftol": 1e-14})
    w = np.zeros_like(bench_w)
    w[keep] = res.x
    return w, keep, w0, dts, dts_bench


FULL_GRID = False        # True: every issuer in every cross-section (SLSQP then takes several minutes)
N_DEMO = 100             # default grid: a systematic sample of this many issuers per cross-section

g5 = np.random.default_rng(RNG_SEED + 5)
n_iss = int(lagged["issuer_id"].max()) + 1
dur_by_issuer = g5.uniform(1.5, 6.5, n_iss)
size_by_issuer = g5.lognormal(0.0, 0.5, n_iss)
held_def, bench_def = 0.0, 0.0
for t0 in (24, 36, 48, 60, 72):
    cs = lagged[lagged["month"] == t0]
    if not FULL_GRID:
        cs = cs.iloc[:: max(1, len(cs) // N_DEMO)].iloc[:N_DEMO]      # every k-th issuer, by id
    iid = cs["issuer_id"].to_numpy()
    pd_t = predict_logit(b_full, cs[XCOLS].to_numpy())
    spr_t = 0.015 + 0.35 * empirical_pd(cs["DD"].to_numpy()) * np.exp(g5.normal(0.0, 0.2, len(cs)))
    bw = size_by_issuer[iid] / size_by_issuer[iid].sum()
    w, keep, w0, dts_t, dts_b = defensive_portfolio(pd_t, spr_t, dur_by_issuer[iid], bw)
    assert abs(w @ dts_t / dts_b - 1.0) < 0.01            # DTS-neutral within 1%
    assert abs(w.sum() - 1.0) < 1e-6 and w.min() > -1e-9 and np.all(w[~keep] == 0.0)
    assert (w0 @ dts_t[keep]) / dts_b < 0.95                # market-value tilt = dimmer switch
    y_t = cs["default_12m"].to_numpy()
    held_def += w @ y_t
    bench_def += bw @ y_t
assert held_def < bench_def                                  # fewer realized defaults held
print(f"avg 12m default exposure: held={held_def / 5:.3%} bench={bench_def / 5:.3%}; "
      f"last MV-tilt DTS ratio={(w0 @ dts_t[keep]) / dts_b:.2f}")
```


### Listing 11.6: The regime-aware DTS multiplier and capacity {#code-11-6}

```python
# Block 6: regime-aware DTS budget and capacity (Sections 11.8-11.9)

def model_spread(pd_hat, L=0.6, m=1.8, s0=0.005):
    return s0 + m * np.asarray(pd_hat, dtype=float) * L


def dts_multiplier(spread, s_hat, dts, w, z_ref, kappa=0.5, band=(0.9, 1.2), dts_max_ratio=np.inf):
    z = np.log(np.asarray(spread, dtype=float) / np.asarray(s_hat, dtype=float))
    z_bar = float(np.sum(w * dts * z) / np.sum(w * dts))
    mult = float(np.clip(1.0 + kappa * (z_bar - z_ref), band[0], band[1]))
    return min(mult, dts_max_ratio), z_bar                      # no-leverage guard


def alpha_net(C, alpha0, adv, horizon_days, kappa, turnover):
    return alpha0 - kappa * turnover * np.sqrt(C / (adv * horizon_days))


def capacity_closed_form(alpha0, alpha_min, adv, horizon_days, kappa, turnover):
    return adv * horizon_days * ((alpha0 - alpha_min) / (kappa * turnover)) ** 2


def capacity_numeric(alpha0, alpha_min, adv, horizon_days, kappa, turnover):
    f = lambda C: alpha_net(C, alpha0, adv, horizon_days, kappa, turnover) - alpha_min
    hi = adv * horizon_days
    while f(hi) > 0:
        hi *= 4.0
    return optimize.brentq(f, 0.0, hi, xtol=1e-6, rtol=1e-14, maxiter=500)


# Regime test on the last Block 5 cross-section.
pd_c = predict_logit(b_full, cs[XCOLS].to_numpy())
s_hat_c = model_spread(pd_c)
w_eq = np.full(len(cs), 1.0 / len(cs))
dts_c = dur_by_issuer[iid] * spr_t
_, z_ref = dts_multiplier(spr_t, s_hat_c, dts_c, w_eq, z_ref=0.0)
m_calm, _ = dts_multiplier(spr_t, s_hat_c, dts_c, w_eq, z_ref)
m_shock, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c, dts_c * 461 / 259, w_eq, z_ref)
m_fund, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c * 461 / 259, dts_c * 461 / 259, w_eq, z_ref)
m_guard, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c, dts_c, w_eq, z_ref, dts_max_ratio=1.05)
assert abs(m_calm - 1.0) < 1e-12 and abs(m_fund - 1.0) < 1e-12   # fundamentals: no add
assert m_shock > 1.0 and m_guard <= 1.05                          # overshoot: add, but never lever

# Capacity: a scalable core versus a CCC / fallen-angel satellite (all inputs illustrative).
core = dict(alpha0=0.010, alpha_min=0.0025, adv=14e9, horizon_days=20, kappa=0.03, turnover=0.6)
niche = dict(alpha0=0.030, alpha_min=0.0100, adv=1.5e9, horizon_days=20, kappa=0.05, turnover=2.0)
for spec in (core, niche):
    c_cf, c_num = capacity_closed_form(**spec), capacity_numeric(**spec)
    assert abs(c_num / c_cf - 1.0) < 1e-8
assert capacity_closed_form(**core) > 10 * capacity_closed_form(**niche)
print(f"DTS multiplier calm={m_calm:.2f} shock={m_shock:.2f} fundamental={m_fund:.2f} "
      f"guarded={m_guard:.2f}; capacity core=${capacity_closed_form(**core) / 1e9:.1f}bn "
      f"niche=${capacity_closed_form(**niche) / 1e9:.2f}bn")
```


## F.12: Chapter 12: Multi-Asset Credit Allocation {#code-12}

Listings from `12_ch12_multi_asset_credit_allocation.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 12.1: Sector inputs: expected loss, mark-to-market drag and forward return {#code-12-1}

```python
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20251119)   # Nuveen's as-of date; superstition is free

SECTORS = ["HY corp", "EM sov BB-B", "EM corp HY BB-B", "Lev loans", "CoCos", "Pref HY",
           "ABS other", "CMBS BBB", "CLO BBB-B", "MBS CRT", "MM direct lending"]
N, DL = len(SECTORS), 10
# Illustrative inputs (decimals per year; durations in years). Bounds are Nuveen Fig. 5.
TAB = dict(
    yld=np.array([.0697, .0750, .0720, .0800, .0680, .0700, .0600, .0850, .0950, .0780, .0975]),
    pd=np.array([.0425, .0300, .0350, .0400, .0150, .0180, .0100, .0350, .0380, .0230, .0500]),
    rec=np.array([.40, .40, .40, .52, .20, .30, .40, .30, .35, .35, .33]),
    dmod=np.array([3.2, 6.0, 3.8, .25, 4.5, 5.0, 2.5, 4.5, .25, .5, .25]),
    dspr=np.array([3.2, 6.0, 3.8, 4.0, 4.5, 5.0, 2.5, 4.5, 4.0, 3.5, 3.0]),
    spread=np.array([.030, .033, .034, .035, .030, .031, .015, .042, .055, .038, .060]),
    dspread_h=np.array([.0075, .003, .004, .005, .004, .004, .002, .006, .006, .004, .004]),
    tier=np.array(["ML", "ML", "LL", "LL", "ML", "ML", "LL", "LL", "LL", "LL", "IL"]),
    days=np.array([3, 3, 5, 10, 2, 4, 5, 10, 7, 5, 180], float),
    lcs_bp=np.array([60, 50, 80, 70, 60, 90, 40, 120, 100, 80, 300], float),
    w_min=np.array([.20, .02, .02, .05, .02, .02, 0, 0, 0, 0, 0]),
    w_max=np.array([.60, .15, .15, .25, .10, .10, .10, .10, .10, .10, .35]),
)
HORIZON, D_RATES_H, CASH = 5.0, 0.0050, 0.0368   # years; +50bp over horizon; cash from Fig. 6

def _decimal(name, x):
    if np.any(np.abs(np.asarray(x, float)) > 1.0):
        raise ValueError(f"{name} looks like a percent; pass decimals")

def expected_loss(pd, rec):
    _decimal("pd", pd)
    return np.asarray(pd) * (1.0 - np.asarray(rec))

def mtm_drag(duration, change_over_h, h):
    _decimal("change", change_over_h)
    return np.asarray(duration) * np.asarray(change_over_h) / h

def forward_return(yld, el, rates_mtm, spread_mtm):          # eq. (12.1), convexity dropped
    for nm, v in (("yld", yld), ("el", el), ("rates_mtm", rates_mtm), ("spread_mtm", spread_mtm)):
        _decimal(nm, v)
    return np.asarray(yld) - el - rates_mtm - spread_mtm

def breakeven_default(s, rec):
    return s / (1.0 - rec)

assert abs(forward_return(.0697, .0255, .0037, .0049) - .0356) < 1e-12   # Nuveen Fig. 3 reading
fig6 = np.array([[5.11, 5.50, .26], [5.25, 5.52, .28], [5.50, 5.60, .33],
                 [5.75, 5.76, .36], [6.00, 6.05, .38], [6.20, 6.29, .40]])
implied_cash = fig6[:, 0] - fig6[:, 2] * fig6[:, 1]                       # our inference, in %
assert np.all((implied_cash > 3.60) & (implied_cash < 3.75))
assert abs(breakeven_default(.1278, .35) - .1966) < 1e-3                  # Section 12.3 CCC
assert np.isclose(2.0 * 0.02, 4.0 * 0.01)                                 # Ben Dor p.50 DTS

MU = forward_return(TAB["yld"], expected_loss(TAB["pd"], TAB["rec"]),
                    mtm_drag(TAB["dmod"], D_RATES_H, HORIZON),
                    mtm_drag(TAB["dspr"], TAB["dspread_h"], HORIZON))
DTS = TAB["dspr"] * TAB["spread"]
print("implied cash (%):", implied_cash.round(3))
for s_, m_ in zip(SECTORS, MU):
    print(f"{s_:18s} forward {m_:6.2%}   excess {m_ - CASH:+6.2%}")
```


### Listing 12.2: GLM de-smoothing: fitting the MA(k) smoothing weights {#code-12-2}

```python
def acf(x, nlags):
    x = np.asarray(x, float) - np.mean(x)
    g0 = x @ x
    return np.array([x[k:] @ x[:-k] / g0 for k in range(1, nlags + 1)])

def _ma_rho(th, k):
    g = np.array([th[: len(th) - j] @ th[j:] for j in range(k + 1)])
    return g[1:] / g[0]

def _softmax(z):
    e = np.exp(z - z.max())
    return e / e.sum()

def fit_smoothing(r_obs, k=2):
    """GLM (2004) MA(k) weights by matching autocorrelations; theta >= 0, sum(theta) = 1."""
    rho = acf(r_obs, k)
    loss = lambda zz: np.sum((_ma_rho(_softmax(zz), k) - rho) ** 2)
    z0 = np.log(np.linspace(1.0, 0.3, k + 1))          # decreasing start: the invertible branch
    res = minimize(loss, z0, method="Nelder-Mead",
                   options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 20000})
    th = _softmax(res.x)
    return th, float(th @ th)

def desmooth(r_obs, theta):
    th = np.asarray(theta, float)
    if len(th) > 1 and np.any(np.abs(np.roots(th[::-1])) <= 1.0):
        raise ValueError("smoothing weights not invertible; refuse rather than guess")
    r = np.zeros(len(r_obs))
    for t in range(len(r_obs)):
        acc = r_obs[t] - sum(th[j] * r[t - j] for j in range(1, len(th)) if t - j >= 0)
        r[t] = acc / th[0]
    return r

def ar1_profile(phi, k=60):
    th = (1 - phi) * phi ** np.arange(k + 1)
    return th / th.sum()

T_DS, theta_true = 6000, np.array([0.5, 0.3, 0.2])
r_true = 0.006 + 0.02 * rng.standard_normal(T_DS)
r_obs = np.convolve(r_true, theta_true)[:T_DS]
th_hat, xi_hat = fit_smoothing(r_obs[10:], k=2)
sig_hat = r_obs[10:].std() / np.sqrt(xi_hat)
assert abs(xi_hat - 0.38) < 0.05, xi_hat
assert abs(sig_hat / r_true[10:].std() - 1.0) < 0.10
assert np.allclose(desmooth(r_obs, theta_true), r_true, atol=1e-10)
th_ar = ar1_profile(0.8)
assert abs(th_ar @ th_ar - (1 - 0.8) / (1 + 0.8)) < 1e-3                # xi = (1-phi)/(1+phi)
print("theta_hat", th_hat.round(3), " xi_hat", round(xi_hat, 3))
```


### Listing 12.3: The covariance an optimizer sees: DTS, smoothing, EWMA and Ledoit-Wolf shrinkage {#code-12-3}

```python
SIG_U = np.array([.35, .40, .40, .35, .45, .40, .30, .45, .45, .40, .35])  # annual vol of ds/s
B_LOAD = np.array([.90, .80, .85, .90, .80, .85, .70, .80, .85, .80, .90])
SIG_Y = 0.0080                                                         # annual vol of TSY dy

def dts_cov(dts, omega, dmod=None, sig_y=0.0):                         # eq. (12.3)
    S = np.outer(dts, dts) * omega
    return S if dmod is None else S + sig_y ** 2 * np.outer(dmod, dmod)

C1 = np.outer(B_LOAD, B_LOAD); np.fill_diagonal(C1, 1.0)
SIGMA = dts_cov(DTS, np.outer(SIG_U, SIG_U) * C1, TAB["dmod"], SIG_Y)

def smoothed_view(Sigma, i, theta):
    """Covariance an optimizer sees when sector i is reported with GLM smoothing theta."""
    th = np.asarray(theta, float); S = Sigma.copy()
    S[i, :] *= th[0]; S[:, i] *= th[0]; S[i, i] = Sigma[i, i] * (th @ th)
    return S

SIGMA_REP = smoothed_view(SIGMA, DL, ar1_profile(0.8))
print("DL vol: true %.2f%%, reported %.2f%%" % (100 * np.sqrt(SIGMA[DL, DL]),
                                               100 * np.sqrt(SIGMA_REP[DL, DL])))

P_TRUE = np.array([[0.95, 0.05], [0.20, 0.80]])
MU_F, SD_F, SD_E = np.array([-0.025, 0.10]), np.array([0.05, 0.12]), np.array([0.03, 0.06])
T_SIM = 3000
z = np.zeros(T_SIM, dtype=int)
for t in range(1, T_SIM):
    z[t] = int(rng.random() < P_TRUE[z[t - 1], 1])
f = MU_F[z] + SD_F[z] * rng.standard_normal(T_SIM)                 # common spread factor
U = f[:, None] * B_LOAD[None, :] + SD_E[z][:, None] * rng.standard_normal((T_SIM, N))
R = TAB["spread"][None, :] / 12.0 - DTS[None, :] * U               # monthly excess returns

def ewma_cov(U, lam=0.97, warmup=24):
    S = np.cov(U[:warmup].T, bias=True)
    for u in U[warmup:]:
        S = lam * S + (1 - lam) * np.outer(u, u)
    return S

def one_factor_target(S):
    w = np.full(S.shape[0], 1.0 / S.shape[0]); var_m = w @ S @ w
    beta = S @ w / var_m
    F = var_m * np.outer(beta, beta); np.fill_diagonal(F, np.diag(S))
    return F

def lw_delta(U):
    """Ledoit-Wolf (2004) intensity toward the one-factor target (diagonal-rho simplification)."""
    X = U - U.mean(0); T, n = X.shape; S = X.T @ X / T
    pi_mat = ((X[:, :, None] * X[:, None, :] - S) ** 2).mean(0)
    gam = ((one_factor_target(S) - S) ** 2).sum()
    return float(np.clip((pi_mat.sum() - np.trace(pi_mat)) / gam / T, 0.0, 1.0))

U_win = U[-300:]
S_ew, delta = ewma_cov(U_win), lw_delta(U_win)
OMEGA_HAT = 12.0 * (delta * one_factor_target(S_ew) + (1 - delta) * S_ew)   # annualized
SIGMA_HAT = dts_cov(DTS, OMEGA_HAT, TAB["dmod"], SIG_Y)
assert 0.0 <= delta <= 1.0
assert np.linalg.eigvalsh(SIGMA_HAT).min() >= -1e-10
assert np.isclose(np.sqrt(dts_cov(DTS, OMEGA_HAT)[0, 0]), DTS[0] * np.sqrt(OMEGA_HAT[0, 0]))
print("Ledoit-Wolf delta %.3f" % delta)
```


### Listing 12.4: A two-state regime model: HMM filter, EM fit and regime-conditional capital-market assumptions {#code-12-4}

```python
def mvn_logpdf(X, mu, S):
    L = np.linalg.cholesky(S)
    Z = np.linalg.solve(L, (X - mu).T)
    return -0.5 * (Z ** 2).sum(0) - np.log(np.diag(L)).sum() - 0.5 * X.shape[1] * np.log(2 * np.pi)

def forward_backward(logB, P, pi0):
    T, K = logB.shape
    m = logB.max(1, keepdims=True); B = np.exp(logB - m)            # underflow guard
    alpha, c, pred = np.zeros((T, K)), np.zeros(T), pi0.copy()
    for t in range(T):
        a = pred * B[t]; c[t] = a.sum(); alpha[t] = a / c[t]         # xi_{t|t}
        pred = alpha[t] @ P                                           # xi_{t+1|t} = P' xi_{t|t}
    beta = np.ones((T, K))
    for t in range(T - 2, -1, -1):
        beta[t] = P @ (B[t + 1] * beta[t + 1]) / c[t + 1]
    gamma = alpha * beta; gamma /= gamma.sum(1, keepdims=True)
    xi_sum = np.zeros((K, K))
    for t in range(T - 1):
        x = alpha[t][:, None] * P * (B[t + 1] * beta[t + 1])[None, :]
        xi_sum += x / x.sum()
    return alpha, gamma, xi_sum, float(np.log(c).sum() + m.sum())

def hmm2_em(R, n_iter=200, tol=1e-9, ridge=1e-10):
    T, n = R.shape; K = 2
    score = R.mean(1)
    stress = score <= np.quantile(score, 0.20)                      # init: worst 20% of months
    gamma = np.column_stack([~stress, stress]).astype(float)
    P, pi0, ll_old = np.array([[0.9, 0.1], [0.3, 0.7]]), np.array([0.5, 0.5]), -np.inf
    for it in range(n_iter):
        mu = np.array([gamma[:, k] @ R / gamma[:, k].sum() for k in range(K)])
        Sig = np.array([(gamma[:, k, None] * (R - mu[k])).T @ (R - mu[k]) / gamma[:, k].sum()
                        + ridge * np.eye(n) for k in range(K)])
        logB = np.column_stack([mvn_logpdf(R, mu[k], Sig[k]) for k in range(K)])
        alpha, gamma, xi_sum, ll = forward_backward(logB, P, pi0)
        P, pi0 = xi_sum / xi_sum.sum(1, keepdims=True), gamma[0]
        if ll - ll_old < tol * abs(ll):
            break
        ll_old = ll
    o = np.argsort(-mu.mean(1))                                      # label 0 = calm
    return dict(P=P[np.ix_(o, o)], mu=mu[o], Sig=Sig[o], filt=alpha[:, o],
                smooth=gamma[:, o], loglik=ll, iters=it + 1)

def stationary(P):
    K = P.shape[0]
    A = np.vstack([P.T - np.eye(K), np.ones(K)])
    return np.linalg.lstsq(A, np.r_[np.zeros(K), 1.0], rcond=None)[0]

def regime_cma(P, mu_k, Sig_k, xi_now, h):                          # eq. (12.2)
    p, probs = np.asarray(xi_now, float), np.zeros(len(xi_now))
    for _ in range(h):
        p = p @ P; probs += p / h
    mu = probs @ mu_k
    Sig = sum(probs[k] * (Sig_k[k] + np.outer(mu_k[k] - mu, mu_k[k] - mu)) for k in range(len(probs)))
    return mu, Sig, probs

fit = hmm2_em(R)
acc_filt = np.mean(fit["filt"].argmax(1) == z)
acc_smooth = np.mean(fit["smooth"].argmax(1) == z)
assert np.all(np.abs(np.diag(fit["P"]) - np.diag(P_TRUE)) < 0.05), fit["P"]
assert acc_filt > 0.85, acc_filt
print("P_hat", fit["P"].round(3), " durations (months)", (1 / (1 - np.diag(fit["P"]))).round(1))
print("state accuracy: filtered %.3f, smoothed %.3f (smoothed peeks)" % (acc_filt, acc_smooth))
mu_stress, Sig_stress, pr = regime_cma(fit["P"], fit["mu"], fit["Sig"], [0.0, 1.0], h=12)
assert np.isclose(pr.sum(), 1.0) and np.linalg.eigvalsh(Sig_stress).min() > -1e-12
_, _, pr_long = regime_cma(fit["P"], fit["mu"], fit["Sig"], [0.0, 1.0], h=600)
assert np.allclose(pr_long, stationary(fit["P"]), atol=0.02)
```


### Listing 12.5: Mean-variance with tiers, equal risk contribution and the frontier {#code-12-5}

```python
def feasible_start(lo, hi):
    lo, hi = np.asarray(lo, float), np.asarray(hi, float)
    if lo.sum() > 1 + 1e-12 or hi.sum() < 1 - 1e-12:
        raise ValueError("bounds cannot sum to one")
    return lo + (1.0 - lo.sum()) / (hi - lo).sum() * (hi - lo)

BUDGET = {"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones_like(w)}
OPTS = {"ftol": 1e-12, "maxiter": 2000}

def max_sharpe(mu, Sigma, lo, hi, cash=CASH):
    ex = mu - cash
    def f(w): return -(w @ ex) / np.sqrt(w @ Sigma @ w)
    def g(w):
        Sw = Sigma @ w; v = np.sqrt(w @ Sw)
        return -(ex / v - (w @ ex) * Sw / v ** 3)
    return minimize(f, feasible_start(lo, hi), jac=g, bounds=list(zip(lo, hi)),
                    constraints=[BUDGET], method="SLSQP", options=OPTS).x

def min_var(mu, Sigma, lo, hi, target=None):
    cons = [BUDGET] + ([] if target is None else
                       [{"type": "ineq", "fun": lambda w: w @ mu - target, "jac": lambda w: mu}])
    return minimize(lambda w: w @ Sigma @ w, feasible_start(lo, hi), jac=lambda w: 2 * Sigma @ w,
                    bounds=list(zip(lo, hi)), constraints=cons, method="SLSQP", options=OPTS).x

def max_return_under_bounds(mu, lo, hi):
    w, room = np.asarray(lo, float).copy(), 1.0 - np.sum(lo)
    for i in np.argsort(-mu):
        add = min(hi[i] - w[i], room); w[i] += add; room -= add
    return w

def frontier(mu, Sigma, lo, hi, n_pts=6):
    r_lo = min_var(mu, Sigma, lo, hi) @ mu
    r_hi = max_return_under_bounds(mu, lo, hi) @ mu
    targets = np.linspace(r_lo, r_lo + 0.95 * (r_hi - r_lo), n_pts)
    return [min_var(mu, Sigma, lo, hi, tg) for tg in targets], targets

def optimize_erc(Sigma, b=None, tol=1e-13, max_iter=100):
    n = Sigma.shape[0]
    b = np.full(n, 1.0 / n) if b is None else np.asarray(b, float) / np.sum(b)
    obj = lambda y: 0.5 * y @ Sigma @ y - b @ np.log(y)
    y = 1.0 / np.sqrt(np.diag(Sigma))
    for _ in range(max_iter):
        g = Sigma @ y - b / y
        if np.max(np.abs(g)) < tol:
            break
        step, t = np.linalg.solve(Sigma + np.diag(b / y ** 2), g), 1.0   # Newton, PD Hessian
        while t > 1e-12 and (np.any(y - t * step <= 0)
                             or obj(y - t * step) > obj(y) - 1e-4 * t * (g @ step)):
            t *= 0.5
        y = y - t * step
    return y / y.sum()

def risk_contrib(w, Sigma):
    Sw = Sigma @ w
    return w * Sw / (w @ Sw)

def beta_variance_share(sr_alpha, sr_beta):
    return 1.0 / (1.0 + (sr_alpha / sr_beta) ** 2)

def utility(w, mu, Sigma, gamma):
    return w @ mu - 0.5 * gamma * (w @ Sigma @ w)

def optimize_tiered(mu, Sigma, lo, hi, tiers, days, gamma=8.0, illiquid_cap=0.15,
                    liquid_min=0.35, tau_max=32.0, w_ref=None, tilt_budget=None, lcs=None):
    """Mean-variance with the tiers of eq. (12.4); optional l1 tilt budget and LCS costs."""
    n = len(mu); il = (tiers == "IL").astype(float); lq = np.isin(tiers, ["HL", "ML"]).astype(float)
    tilt = w_ref is not None; m = 2 * n if tilt else 0
    c2 = np.tile(0.5 * np.asarray(lcs, float), 2) if tilt else np.zeros(0)   # one-way cost
    pad = lambda v: np.concatenate([v, np.zeros(m)])
    f = lambda x: -utility(x[:n], mu, Sigma, gamma) + c2 @ x[n:]
    g = lambda x: np.concatenate([-(mu - gamma * Sigma @ x[:n]), c2])
    cons = [{"type": "eq", "fun": lambda x: x[:n].sum() - 1.0, "jac": lambda x: pad(np.ones(n))},
            {"type": "ineq", "fun": lambda x: illiquid_cap - il @ x[:n], "jac": lambda x: pad(-il)},
            {"type": "ineq", "fun": lambda x: lq @ x[:n] - liquid_min, "jac": lambda x: pad(lq)},
            {"type": "ineq", "fun": lambda x: tau_max - days @ x[:n], "jac": lambda x: pad(-days)}]
    if tilt:
        I = np.eye(n)
        cons += [{"type": "eq", "fun": lambda x: x[:n] - w_ref - x[n:2 * n] + x[2 * n:],
                  "jac": lambda x: np.hstack([I, -I, I])},
                 {"type": "ineq", "fun": lambda x: tilt_budget - x[n:].sum(),
                  "jac": lambda x: np.concatenate([np.zeros(n), -np.ones(2 * n)])}]
        x0 = np.concatenate([w_ref, np.zeros(2 * n)])
        bnds = list(zip(lo, hi)) + [(0.0, 1.0)] * (2 * n)
    else:
        x0, bnds = feasible_start(lo, np.where(il > 0, np.minimum(hi, illiquid_cap), hi)), list(zip(lo, hi))
    res = minimize(f, x0, jac=g, bounds=bnds, constraints=cons, method="SLSQP", options=OPTS)
    return res.x[:n], res

lo, hi = TAB["w_min"], TAB["w_max"]
# Unit tests: tangency with inactive bounds, ERC to 1e-8, Paleologo's beta share
mu3 = np.array([.05, .06, .07]); S3 = np.array([[.04, .01, .01], [.01, .06, .01], [.01, .01, .09]])
w_tan = np.linalg.solve(S3, mu3 - CASH); w_tan /= w_tan.sum()
w_num = max_sharpe(mu3, S3, np.full(3, -10.0), np.full(3, 10.0))
assert np.max(np.abs(w_num - w_tan) / np.abs(w_tan)) < 1e-4      # solver tolerance, not theorem
assert np.max(np.abs(risk_contrib(optimize_erc(SIGMA), SIGMA) - 1.0 / N)) < 1e-8
assert np.isclose(beta_variance_share(0.35, 0.35), 0.5)

# The flat frontier (six portfolios, as in Nuveen Fig. 6)
W_F, targets = frontier(MU, SIGMA, lo, hi)
vols = np.array([np.sqrt(w @ SIGMA @ w) for w in W_F]); rets = np.array([w @ MU for w in W_F])
assert np.all(np.diff(vols) > -1e-7) and np.all(rets >= targets - 1e-7)
for k, (r_, v_) in enumerate(zip(rets, vols), 1):
    print(f"portfolio {k}: return {r_:.2%}  vol {v_:.2%}  Sharpe {(r_ - CASH) / v_:.2f}")

# Kaz's allocation: reported (smoothed) risk vs desmoothed risk for direct lending
w_rep, w_tru = max_sharpe(MU, SIGMA_REP, lo, hi), max_sharpe(MU, SIGMA, lo, hi)
vol_claimed, vol_actual = np.sqrt(w_rep @ SIGMA_REP @ w_rep), np.sqrt(w_rep @ SIGMA @ w_rep)
assert vol_actual > vol_claimed                  # a theorem, not a seed: smoothing hides risk
print(f"DL weight: reported-risk {w_rep[DL]:.1%}, desmoothed {w_tru[DL]:.1%}; "
      f"the reported-risk book claims {vol_claimed:.2%} vol and carries {vol_actual:.2%}")

# Strategic allocation with liquidity tiers, plus shadow prices by finite difference
GAMMA = 8.0
tiers, days = TAB["tier"], TAB["days"]
w_saa, _ = optimize_tiered(MU, SIGMA, lo, hi, tiers, days, gamma=GAMMA)
assert abs(w_saa.sum() - 1) < 1e-8 and np.all(w_saa >= lo - 1e-9) and np.all(w_saa <= hi + 1e-9)
assert w_saa[tiers == "IL"].sum() <= 0.15 + 1e-8                 # never violates the 15% cap
assert w_saa @ days <= 32.0 + 1e-6 and w_saa[np.isin(tiers, ["HL", "ML"])].sum() >= 0.35 - 1e-8
u0 = utility(w_saa, MU, SIGMA, GAMMA)
w_cap, _ = optimize_tiered(MU, SIGMA, lo, hi, tiers, days, gamma=GAMMA, illiquid_cap=0.16)
lo_hy = lo.copy(); lo_hy[0] -= 0.01
w_hy, _ = optimize_tiered(MU, SIGMA, lo_hy, hi, tiers, days, gamma=GAMMA)
d_cap = utility(w_cap, MU, SIGMA, GAMMA) - u0
d_hy = utility(w_hy, MU, SIGMA, GAMMA) - u0
assert d_cap > -1e-8 and d_hy > -1e-8                            # relaxing cannot hurt
print(f"utility gain per 1% of NAV relaxed: illiquid cap {d_cap * 1e4:.2f} bp, "
      f"HY floor {d_hy * 1e4:.2f} bp")

# Tactical tilt: the filter says stress; 10% l1 budget, LCS costs, all tiers still binding
mu_stat = stationary(fit["P"]) @ fit["mu"]
overlay = 12.0 * (mu_stress - mu_stat)                          # annualized regime tilt
w_tac, _ = optimize_tiered(MU + overlay, SIGMA, lo, hi, tiers, days, gamma=GAMMA,
                           w_ref=w_saa, tilt_budget=0.10, lcs=TAB["lcs_bp"] / 1e4)
assert np.abs(w_tac - w_saa).sum() <= 0.10 + 1e-6
assert w_tac[tiers == "IL"].sum() <= 0.15 + 1e-8
print("tilt (pp):", dict(zip(SECTORS, (100 * (w_tac - w_saa)).round(1))))
```


## F.13: Chapter 13: Codifying Liability Management Transactions (LMTs) {#code-13}

Listings from `13_ch13_codifying_lmt_game_theory.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 13.1: Waterfall clearing with priority classes, and double-dip and pari-plus recoveries {#code-13-1}

```python
# lmt_engine.py, block (a): multi-obligor clearing with priority classes
import itertools
import numpy as np
from scipy import integrate, optimize, stats

rng = np.random.default_rng(13)

def waterfall_clearing(ents, claims, tol=1e-10, max_iter=10_000):
    """Eisenberg-Noe clearing: pay by rank, pro rata within rank, route intercompany
    receipts and subsidiary equity upward; iterate to a fixed point."""
    pay = {c["id"]: 0.0 for c in claims}
    res = {e: 0.0 for e in ents}
    for _ in range(max_iter):
        avail = {e: float(s["value"]) for e, s in ents.items()}
        for c in claims:
            if c["creditor"] != "ext":
                avail[c["creditor"]] += pay[c["id"]]
        for e, s in ents.items():
            if s["parent"] is not None:
                avail[s["parent"]] += res[e]
        new_pay, new_res = {}, {}
        for e in ents:
            left, mine = avail[e], [c for c in claims if c["debtor"] == e]
            for r in sorted({c["rank"] for c in mine}):
                cls = [c for c in mine if c["rank"] == r]
                owed = [max(c["face"] - sum(pay[k] for k in c.get("reduce_by", ())), 0.0) for c in cls]
                tot = sum(owed)
                frac = 1.0 if tot <= left else left / tot
                for c, o in zip(cls, owed):
                    new_pay[c["id"]] = frac * o
                left = max(left - frac * tot, 0.0)
            new_res[e] = left
        gap = max(max(abs(new_pay[k] - pay[k]) for k in pay), max(abs(new_res[e] - res[e]) for e in ents))
        pay, res = new_pay, new_res
        if gap < tol:
            return pay, sum(res[e] for e in ents if ents[e]["parent"] is None)
    raise RuntimeError("clearing did not converge")

def dd_recoveries(V, F1, F2, Vf=0.0, pari_plus=False):
    """Double-dip (SPV owned by OpCo); pari-plus adds a foreign-sub guarantee worth Vf."""
    ents = {"opco": {"value": V, "parent": None}, "spv": {"value": 0.0, "parent": "opco"},
            "fsub": {"value": Vf, "parent": "opco"}}
    g = ["fsub_guar"] if pari_plus else []
    cl = [dict(id="1L", creditor="ext", debtor="opco", face=F1, rank=1),
          dict(id="opco_guar", creditor="ext", debtor="opco", face=F2, rank=1, reduce_by=g),
          dict(id="interco", creditor="spv", debtor="opco", face=F2, rank=1),
          dict(id="spv_tl", creditor="ext", debtor="spv", face=F2, rank=1, reduce_by=g + ["opco_guar"])]
    if pari_plus:
        cl.append(dict(id="fsub_guar", creditor="ext", debtor="fsub", face=F2, rank=1))
    pay, eq = waterfall_clearing(ents, cl)
    new = sum(v for k, v in pay.items() if k in ("opco_guar", "spv_tl", "fsub_guar"))
    assert abs(pay["1L"] + new + eq - (V + Vf)) < 1e-8, "conservation"
    assert new <= F2 + 1e-9 and pay["1L"] <= F1 + 1e-9, "no claim paid above face"
    return pay["1L"] / F1, new / F2

F1, F2 = 1_000.0, 500.0
for V in (200.0, 600.0, 800.0, 999.0):                       # uncapped regime: closed form
    r1, rdd = dd_recoveries(V, F1, F2)
    assert abs(rdd - 2 * V / (F1 + 2 * F2)) < 1e-8 and abs(r1 - V / (F1 + 2 * F2)) < 1e-8
r1, rdd = dd_recoveries(1_200.0, F1, F2)                     # fixed-point regime: rho = (V - F2)/F1
assert abs(rdd - 1.0) < 1e-8 and abs(r1 - 0.7) < 1e-8
path = np.array([dd_recoveries(v, F1, F2) for v in np.linspace(0.0, 2_500.0, 101)])
assert np.all(np.diff(path, axis=0) >= -1e-9), "recoveries must be monotone in V"
assert np.allclose(dd_recoveries(600.0, F1, F2, 0.0, True), dd_recoveries(600.0, F1, F2))
assert dd_recoveries(600.0, F1, F2, 150.0, True)[0] < dd_recoveries(600.0, F1, F2, 150.0)[0]
```


### Listing 13.2: The uptier, the sponsor's knapsack, the co-op veto and Shapley carve-outs {#code-13-2}

```python
# block (b): uptier transfer, sponsor's knapsack, co-op veto, Shapley carve-outs
def uptier(V, F, N, x, p):
    """Per-dollar recoveries (R0, first-out, second-out, excluded), Section 13.3."""
    V = np.asarray(V, dtype=float)
    K1, exc = N + x * p * F, (1.0 - p) * F
    R0 = np.minimum(V, F) / F
    R_fo = np.minimum(V, N) / N if N > 0 else np.ones_like(V)
    R_so = np.minimum(np.maximum(V - N, 0.0), x * p * F) / (x * p * F) if p > 0 else np.ones_like(V)
    R_ex = np.minimum(np.maximum(V - K1, 0.0), exc) / exc if exc > 0 else np.full_like(V, np.nan)
    return R0, R_fo, R_so, R_ex

def priming_loss(V, F, N, x, p):
    R0, _, _, R_ex = uptier(V, F, N, x, p)
    return R0 - R_ex

F, N, p, x = 2_400.0, 200.0, 0.5, 875.0 / 1_200.0           # Serta, liens blended, $mm (approx.)
K1, K2 = N + x * p * F, N + x * p * F + (1 - p) * F
grid = np.linspace(1.0, 4_000.0, 4_000)
R0, R_fo, R_so, R_ex = uptier(grid, F, N, x, p)
assert np.allclose(N * R_fo + x * p * F * R_so + (1 - p) * F * R_ex, np.minimum(grid, K2))
assert np.allclose(priming_loss(grid[grid >= F + N], F, N, x, p), 0.0)
assert np.allclose(priming_loss(grid[grid <= K1], F, N, x, p), R0[grid <= K1])
assert np.allclose(uptier(grid, F, 0.0, 1.0, 1.0)[2], np.minimum(grid, F) / F)   # x=1, N=0, p=1: no transfer

mu, s = np.log(1_500.0), 0.45                               # illustrative P-law of V at resolution
dist = stats.lognorm(s=s, scale=np.exp(mu))
e_loss, _ = integrate.quad(lambda v: float(priming_loss(v, F, N, x, p)) * dist.pdf(v), 0.0, max(F, K2),
                           points=[q for q in (K1, K2, F) if q < max(F, K2)], limit=200)
Vmc = np.exp(mu + s * rng.standard_normal(400_000))
mc = priming_loss(Vmc, F, N, x, p)
assert abs(mc.mean() - e_loss) < 4 * mc.std() / np.sqrt(mc.size)
cf1 = np.exp(mu + s**2 / 2) * stats.norm.cdf((np.log(K1) - mu - s**2) / s) / F   # partial expectation
mc1 = Vmc / F * (Vmc < K1)
assert abs(mc1.mean() - cf1) < 4 * mc1.std() / np.sqrt(mc1.size)

def min_cost_coalition(w, c, theta, eps=0.01, coop=()):
    """Cheapest S, excluding co-op members (no separate deals), with sum(w[S]) >= theta + eps."""
    cand = [i for i in range(len(w)) if i not in set(coop)]
    if w[cand].sum() < theta + eps:
        return None                                         # the co-op blocks every coalition
    if len(cand) <= 12:
        feas = (list(S) for k in range(1, len(cand) + 1) for S in itertools.combinations(cand, k)
                if w[list(S)].sum() >= theta + eps)
        return min(feas, key=lambda S: float(c[S] @ w[S]))
    S = []
    for i in sorted(cand, key=lambda i: c[i]):             # greedy beyond 12 holders
        if w[S].sum() >= theta + eps:
            break
        S.append(i)
    return S

def shapley(w, quota):
    """Shapley value of the weighted game v(T) = 1[sum w > quota], by enumerating orders."""
    phi, orders = np.zeros(len(w)), list(itertools.permutations(range(len(w))))
    for order in orders:
        acc = 0.0
        for i in order:
            if acc <= quota < acc + w[i]:
                phi[i] += 1.0
                break
            acc += w[i]
    return phi / len(orders)

w = np.array([0.22, 0.18, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04])
c = np.array([0.02, 0.08, 0.03, 0.08, 0.15, 0.03, 0.08, 0.02, 0.08])   # funds cheap, CLOs dear, litigator dearest
S = min_cost_coalition(w, c, theta=0.5)
assert 4 not in S and w[S].sum() >= 0.51                   # the litigator is never invited
assert min_cost_coalition(w, c, theta=2 / 3, coop=(1, 3, 6)) is None   # 36% co-op > 1 - theta
assert np.allclose(shapley([0.25, 0.06, 0.03, 0.03], quota=1 / 3), [5 / 12, 5 / 12, 1 / 12, 1 / 12])
```


### Listing 13.3: The Bayesian Priming Risk Score and expected priming loss {#code-13-3}

```python
# block (c): Bayesian PRS on synthetic borrower-years, then expected priming loss
BETA_TRUE = np.array([-0.9, 0.8, -0.9, -0.8, 0.6])          # blocker, unsub cap, loan px, runway, sponsor
BETA_PRIOR = np.array([-0.5, 0.5, -0.5, -0.5, 0.5])         # "published" prior (illustrative)

def runway_months(cash, undrawn_rcf, monthly_burn, cap=120.0):
    return cap if monthly_burn <= 0 else min((cash + undrawn_rcf) / monthly_burn, cap)

def simulate(n):
    return np.column_stack([rng.binomial(1, 0.6, n), rng.beta(2, 18, n), np.clip(rng.normal(88, 8, n), 40, 101),
                            rng.gamma(3.0, 6.0, n), rng.binomial(1, 0.3, n)]).astype(float)

def sig(u):
    return 0.5 * (1.0 + np.tanh(0.5 * u))                   # overflow-safe logistic

def fit_map(Z, y, prior, tau, a=2.0, b=38.0, iters=100):
    """MAP logistic: N(prior, tau^2) on slopes, Beta(a, b) on sig(b0). tau=inf, a=b=0 is the MLE."""
    A = np.column_stack([np.ones(len(y)), Z])
    m = np.r_[0.0, prior]
    P = np.r_[0.0, np.full(Z.shape[1], 0.0 if np.isinf(tau) else tau ** -2.0)]
    def nlp(bt):
        eta = A @ bt
        return (np.logaddexp(0, eta).sum() - y @ eta + 0.5 * P @ (bt - m) ** 2
                + a * np.logaddexp(0, -bt[0]) + b * np.logaddexp(0, bt[0]))
    bt = np.r_[np.log(y.mean() / (1 - y.mean())), prior if tau < 1e-3 else np.zeros(Z.shape[1])]
    for _ in range(iters):
        pr, s0 = sig(A @ bt), sig(bt[0])
        g = A.T @ (pr - y) + P * (bt - m)
        g[0] += -a * (1 - s0) + b * s0
        H = A.T @ (A * (pr * (1 - pr))[:, None]) + np.diag(P)
        H[0, 0] += (a + b) * s0 * (1 - s0)
        step, t = np.linalg.solve(H, g), 1.0
        while nlp(bt - t * step) > nlp(bt) + 1e-12 and t > 1e-8:
            t *= 0.5                                         # step-halving guard
        bt = bt - t * step
        if np.max(np.abs(t * step)) < 1e-10:
            break
    return bt

n = 400
X = simulate(n)
mu_x, sd_x = X.mean(0), X.std(0)
Z = (X - mu_x) / sd_x
b0_true = optimize.brentq(lambda b0: sig(b0 + Z @ BETA_TRUE).mean() - 0.15, -10, 10)   # ~60 events
y = rng.binomial(1, sig(b0_true + Z @ BETA_TRUE)).astype(float)
assert 30 <= y.sum() <= 100

beta_hat = fit_map(Z, y, BETA_PRIOR, tau=1.0)
p_hat, s0 = sig(beta_hat[0] + Z @ beta_hat[1:]), sig(beta_hat[0])
assert abs(p_hat.mean() - y.mean() - (2.0 * (1 - s0) - 38.0 * s0) / n) < 1e-6   # intercept FOC
assert abs(p_hat.mean() - y.mean()) < 0.015                                    # base-rate prior is mild
mle = fit_map(Z, y, BETA_PRIOR, tau=np.inf, a=0.0, b=0.0)
assert np.allclose(fit_map(Z, y, BETA_PRIOR, tau=1e8, a=0.0, b=0.0), mle, atol=1e-4)   # tau -> inf
assert np.allclose(fit_map(Z, y, BETA_PRIOR, tau=1e-6)[1:], BETA_PRIOR, atol=1e-4)    # tau -> 0
boot = np.array([fit_map(Z[i], y[i], BETA_PRIOR, 1.0) for i in (rng.integers(0, n, n) for _ in range(200))])
lo, hi = np.percentile(boot, [5, 95], axis=0)
assert np.all((lo <= beta_hat) & (beta_hat <= hi))

def prs(x_raw, beta):
    zz = (np.atleast_2d(x_raw) - mu_x) / sd_x
    return sig(beta[0] + zz @ beta[1:])

x1, x0 = mu_x.copy(), mu_x.copy()
x1[0], x0[0] = 1.0, 0.0
assert prs(x1, beta_hat)[0] < prs(x0, beta_hat)[0]          # a Serta blocker lowers PRS
assert s0 * (1 - s0) * beta_hat[2] / sd_x[1] > 0            # dPRS/d(unsub capacity) > 0 at the mean
Zt = (simulate(n) - mu_x) / sd_x                            # seeded holdout
yt = rng.binomial(1, sig(b0_true + Zt @ BETA_TRUE)).astype(float)
assert np.mean((sig(beta_hat[0] + Zt @ beta_hat[1:]) - yt) ** 2) < np.mean((y.mean() - yt) ** 2)

def expected_priming_loss(prs_i, p_npr, p_excl, e_dr):
    """EPL in fraction of par: PRS x P(non-pro-rata | LMT) x P(excluded | NPR) x E[dR | excluded]."""
    assert all(0.0 <= v <= 1.0 for v in (prs_i, p_npr, p_excl, e_dr))
    return prs_i * p_npr * p_excl * e_dr

lark = np.array([0.0, 0.12, 78.0, runway_months(40.0, 30.0, 10.0), 1.0])   # Larkspur (illustrative)
prs_lark = float(prs(lark, beta_hat)[0])
epl = expected_priming_loss(prs_lark, 0.5, 1.0 - w[S].sum(), e_loss)      # Serta-shaped transfer
assert 0.0 <= epl <= e_loss
print(f"events={int(y.sum())} PRS={prs_lark:.3f} E[dR]={e_loss:.3f} EPL={100 * epl:.2f} pts")
```


## F.14: Chapter 14: The Default & Recovery Cycle in the LMT Era (TREND) {#code-14}

Listings from `14_ch14_default_and_recovery_cycle_lmt_era.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 14.1: LME-cycle parameters and the cohort simulator along a regime path {#code-14-1}

```python
# lme_cycle_engine.py -- Chapter 14 reference implementation (block 1 of 5: parameters and simulation)
import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy import integrate, optimize, special, stats

ETA_K12 = 2.0 / (-math.log(0.30)) ** (1.0 / 1.2)   # fact 3 of Sec. 14.3.2 with k = 1.2 -> ~1.713 years


@dataclass
class LMEParams:
    """All rates per year under P; recoveries as fractions of par. Index 0 = pre-LME regime, 1 = LME regime."""
    lam_H: np.ndarray = field(default_factory=lambda: np.array([0.030, 0.022]))  # hard-default hazard
    lam_D: np.ndarray = field(default_factory=lambda: np.array([0.008, 0.038]))  # distressed-exchange hazard
    lam_C: float = 0.05                                    # cure / refinanced-away hazard
    P: np.ndarray = field(default_factory=lambda: np.array([[0.90, 0.10],
                                                             [0.15, 0.85]]))  # annual regime transitions
    p_redefault: float = 0.25        # susceptible fraction after a DE (Moody's 2026: about 1 in 4)
    k: float = 1.2                   # Weibull shape among the susceptible (Sec. 14.3.2 table)
    eta: float = ETA_K12             # Weibull scale in years, so that F(2)/p = 0.70
    pi: float = 0.526                # P(in majority group): Serta first-lien class
    ab_in: tuple = (14.8, 5.2)       # value right after the DE, inside the group (mean 0.74)
    ab_out: tuple = (2.0, 6.0)       # value right after the DE, excluded (mean 0.25)
    ab_hard_noLME: tuple = (2.65, 2.35)    # recovery on a hard default with no prior LME (mean 0.53)
    ab_hard_postLME: tuple = (1.15, 3.85)  # recovery on a hard default after an LME (mean 0.23)
    T_max: float = 10.0
    censor_rate: float = 0.0         # independent random censoring of the first event, per year

    def __post_init__(self):
        self.lam_H = np.asarray(self.lam_H, dtype=float)
        self.lam_D = np.asarray(self.lam_D, dtype=float)
        self.P = np.asarray(self.P, dtype=float)
        assert self.lam_H.shape == (2,) and self.lam_D.shape == (2,)
        assert self.P.shape == (2, 2) and np.allclose(self.P.sum(axis=1), 1.0)
        assert 0.0 < self.p_redefault < 1.0 and self.k > 0.0 and self.eta > 0.0
        for ab in (self.ab_in, self.ab_out, self.ab_hard_noLME, self.ab_hard_postLME):
            assert min(ab) >= 1e-6, "Beta parameters must be positive"


def beta_mean(ab):
    a, b = ab
    return a / (a + b)


def beta_var(ab):
    a, b = ab
    return a * b / ((a + b) ** 2 * (a + b + 1.0))


def simulate_regime_path(n_years, P, s0, rng):
    s = np.empty(n_years, dtype=np.int8)
    s[0] = s0
    for j in range(1, n_years):
        s[j] = rng.choice(2, p=P[s[j - 1]])
    return s


def simulate_cohort(n, prm, seed, s0=1, regime_path=None):
    """Cohort of n issuers: Performing -> {1 hard, 2 DE, 3 cured}, then the post-DE cure-Weibull clock.

    The regime path is systematic (one path per cohort): every issuer sees the same regime each year.
    """
    rng = np.random.default_rng(seed)
    n_years = int(math.ceil(prm.T_max))
    if regime_path is None:
        s = simulate_regime_path(n_years, prm.P, s0, rng)
    else:
        s = np.asarray(regime_path, dtype=np.int8)
        assert s.shape == (n_years,)

    t1 = np.full(n, prm.T_max)                  # first-event time; T_max means administratively censored
    e1 = np.zeros(n, dtype=np.int8)
    g1 = np.full(n, s[-1], dtype=np.int8)
    alive = np.ones(n, dtype=bool)
    for j in range(n_years):                    # hazards are constant within each regime-year
        idx = np.flatnonzero(alive)
        if idx.size == 0:
            break
        lh, ld, lc = prm.lam_H[s[j]], prm.lam_D[s[j]], prm.lam_C
        lam = lh + ld + lc
        if lam <= 0.0:
            continue
        width = min(1.0, prm.T_max - j)
        wait = rng.exponential(1.0 / lam, size=idx.size)
        hit = wait < width
        who = idx[hit]
        t1[who] = j + wait[hit]
        u = rng.random(who.size) * lam          # which cause fired, proportional to its hazard
        e1[who] = np.where(u < lh, 1, np.where(u < lh + ld, 2, 3)).astype(np.int8)
        g1[who] = s[j]
        alive[who] = False

    if prm.censor_rate > 0.0:
        c = rng.exponential(1.0 / prm.censor_rate, size=n)
        cens = c < t1
        t1[cens] = c[cens]
        e1[cens] = 0

    rec1 = np.full(n, np.nan)
    in_maj = np.full(n, -1, dtype=np.int8)
    is_h = e1 == 1
    rec1[is_h] = rng.beta(*prm.ab_hard_noLME, size=int(is_h.sum()))
    de = np.flatnonzero(e1 == 2)
    member = rng.random(de.size) < prm.pi
    in_maj[de] = member.astype(np.int8)
    r_in = rng.beta(*prm.ab_in, size=de.size)
    r_out = rng.beta(*prm.ab_out, size=de.size)
    rec1[de] = np.where(member, r_in, r_out)

    susc = rng.random(de.size) < prm.p_redefault           # cured draws never hard-default
    u_draw = np.full(de.size, np.inf)
    u_draw[susc] = prm.eta * rng.weibull(prm.k, size=int(susc.sum()))
    follow = prm.T_max - t1[de]
    hit2 = u_draw <= follow
    u_obs = np.where(hit2, u_draw, follow)
    rec2 = np.full(de.size, np.nan)
    rec2[hit2] = rng.beta(*prm.ab_hard_postLME, size=int(hit2.sum()))
    t2 = t1[de] + u_obs
    g2 = s[np.minimum(t2.astype(int), n_years - 1)]

    first = pd.DataFrame({"issuer_id": np.arange(n, dtype=np.int64), "t_event": t1, "event": e1,
                          "time_since_de": np.nan, "regime": g1, "in_majority": in_maj, "recovery": rec1})
    post = pd.DataFrame({"issuer_id": de.astype(np.int64), "t_event": t2, "event": hit2.astype(np.int8),
                         "time_since_de": u_obs, "regime": g2, "in_majority": in_maj[de], "recovery": rec2})
    df = pd.concat([first, post], ignore_index=True)
    return df.sort_values("t_event", kind="stable").reset_index(drop=True)
```


### Listing 14.2: Competing-risks estimators, and the wrong one kept for the test {#code-14-2}

```python
# block 2 of 5: competing-risks estimators (first events only)
def _first_events(df):
    f = df[df["time_since_de"].isna()]
    return f["t_event"].to_numpy(dtype=float), f["event"].to_numpy(dtype=int)


def _risk_table(t, e, causes):
    order = np.argsort(t, kind="stable")
    t, e = t[order], e[order]
    times = np.unique(t[e > 0])                                   # distinct event times
    n_risk = (t.size - np.searchsorted(t, times, side="left")).astype(float)
    d = {}
    for k in causes:                                              # ties handled per distinct time
        tk = t[e == k]
        d[k] = (np.searchsorted(tk, times, side="right") - np.searchsorted(tk, times, side="left")).astype(float)
    return times, n_risk, d


def nelson_aalen_cause(df, cause, causes=(1, 2, 3)):
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    return times, np.cumsum(d[cause] / n_risk)


def aalen_johansen(df, causes=(1, 2, 3)):
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    d_all = sum(d[k] for k in causes)
    s_after = np.cumprod(1.0 - d_all / n_risk)
    s_before = np.concatenate(([1.0], s_after[:-1]))
    out = {"time": times, "S": s_after}
    for k, name in zip(causes, ("F_H", "F_D", "F_C")):
        out[name] = np.cumsum(s_before * d[k] / n_risk)
    return pd.DataFrame(out)


def km_naive_cif(df, cause, causes=(1, 2, 3)):
    """The WRONG estimator, kept for the test: 1 - KM with competing causes treated as censoring."""
    t, e = _first_events(df)
    times, n_risk, d = _risk_table(t, e, causes)
    return times, 1.0 - np.cumprod(1.0 - d[cause] / n_risk)


def step_at(times, values, t):
    i = np.searchsorted(times, t, side="right") - 1
    return float(np.where(i >= 0, values[np.maximum(i, 0)], 0.0))
```


### Listing 14.3: Re-default clock, expected loss, coalition mixture and the co-op game {#code-14-3}

```python
# block 3 of 5: re-default clock, expected loss, coalition mixture, co-op game
def _cure_nll(theta, u, delta):
    a = theta[0]
    b, c = np.clip(theta[1], -5.0, 5.0), np.clip(theta[2], -7.0, 7.0)   # log k, log eta (overflow guard)
    k, eta = math.exp(b), math.exp(c)
    log_p, log_1mp = -np.logaddexp(0.0, -a), -np.logaddexp(0.0, a)
    with np.errstate(over="ignore"):
        z = (u / eta) ** k
    log_f0 = b - c + (k - 1.0) * (np.log(u) - c) - z
    log_surv = np.logaddexp(log_1mp, log_p - z)                  # log[(1-p) + p S0(u)]
    ll = np.where(delta == 1, log_p + log_f0, log_surv)
    return -float(ll.sum())


def fit_cure_weibull(u, delta, seed=0, n_starts=4):
    u = np.maximum(np.asarray(u, dtype=float), 1e-8)
    delta = np.asarray(delta, dtype=int)
    rng = np.random.default_rng(seed)
    best = None
    for i in range(n_starts):
        x0 = np.array([special.logit(0.3), 0.0, 0.5]) + (rng.normal(0.0, 0.3, 3) if i else 0.0)
        res = optimize.minimize(_cure_nll, x0, args=(u, delta), method="Nelder-Mead",
                                options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000})
        if best is None or res.fun < best.fun:
            best = res
    a, b, c = best.x
    return float(special.expit(a)), math.exp(np.clip(b, -5, 5)), math.exp(np.clip(c, -7, 7)), -float(best.fun)


def expected_loss(prm, T, side="blend", regime=1):
    """Exact EL(T) of Sec. 14.3.3 in a single regime, by quadrature over the exchange date."""
    if T > prm.T_max:
        raise ValueError("horizon beyond T_max")
    lh, ld, lc = prm.lam_H[regime], prm.lam_D[regime], prm.lam_C
    lam = lh + ld + lc
    L_H = 1.0 - beta_mean(prm.ab_hard_noLME)
    L_post = 1.0 - beta_mean(prm.ab_hard_postLME)
    mu = {"in": beta_mean(prm.ab_in), "out": beta_mean(prm.ab_out)}
    mu["blend"] = prm.pi * mu["in"] + (1.0 - prm.pi) * mu["out"]
    L_D = 1.0 - mu[side]
    F_H = lh / lam * (1.0 - math.exp(-lam * T))

    def G(v):
        return prm.p_redefault * (1.0 - math.exp(-(max(v, 0.0) / prm.eta) ** prm.k))

    def integrand(x):
        return math.exp(-lam * x) * ld * (L_D + (1.0 - L_D) * L_post * G(T - x))

    de_part, _ = integrate.quad(integrand, 0.0, T)
    return F_H * L_H + de_part


def expected_loss_mc(df, T, side="blend"):
    first = df[df["time_since_de"].isna()]
    post = df[df["time_since_de"].notna()].set_index("issuer_id")
    n = len(first)
    h = first[(first["event"] == 1) & (first["t_event"] <= T)]
    loss = float((1.0 - h["recovery"]).sum()) / n
    de = first[(first["event"] == 2) & (first["t_event"] <= T)]
    de_side = de if side == "blend" else de[de["in_majority"] == (1 if side == "in" else 0)]
    if len(de_side) == 0:
        return loss
    p2 = post.loc[de_side["issuer_id"].to_numpy()]
    redef = (p2["event"].to_numpy() == 1) & (p2["t_event"].to_numpy() <= T)
    r_d = de_side["recovery"].to_numpy()
    r_post = np.nan_to_num(p2["recovery"].to_numpy(), nan=1.0)
    per_de = (1.0 - r_d) + r_d * (1.0 - r_post) * redef
    return loss + len(de) / n * float(per_de.mean())


def coalition_mixture_moments(pi, ab_in, ab_out):
    m_in, m_out = beta_mean(ab_in), beta_mean(ab_out)
    mean = pi * m_in + (1.0 - pi) * m_out
    within = pi * beta_var(ab_in) + (1.0 - pi) * beta_var(ab_out)
    between = pi * (1.0 - pi) * (m_in - m_out) ** 2
    return mean, within + between, between


def coop_break_prob(c, m=0.501, n=10, phi=0.10):
    """Sec. 14.5.1: P(at least d* of n equal co-op members defect), independent defection prob phi."""
    if 1.0 - c >= m:
        return 1.0                                             # co-op below the blocking line
    d_star = math.ceil(n * (m + c - 1.0) / c - 1e-12)
    return float(stats.binom.sf(d_star - 1, n, phi))
```


### Listing 14.4: A two-state binomial Markov-switching model of distressed-exchange counts {#code-14-4}

```python
# block 4 of 5: two-state binomial Markov-switching model on DE counts
def hamilton_filter(logf, P, xi0=None):
    """logf: (T, 2) log emission likelihoods; P: (2, 2) or (T, 2, 2) row-stochastic."""
    logf = np.asarray(logf, dtype=float)
    T_, K = logf.shape
    Pt = np.broadcast_to(P, (T_, K, K)) if np.ndim(P) == 2 else np.asarray(P)
    if xi0 is None:
        denom = 2.0 - Pt[0][0, 0] - Pt[0][1, 1]
        pi0 = (1.0 - Pt[0][1, 1]) / denom if denom > 1e-12 else 0.5
        xi0 = np.array([pi0, 1.0 - pi0])
    xi_pred = np.asarray(xi0, dtype=float)
    filt = np.empty((T_, K))
    ll = 0.0
    for t in range(T_):
        mx = logf[t].max()
        w = xi_pred * np.exp(logf[t] - mx)
        c = max(float(w.sum()), 1e-300)
        ll += math.log(c) + mx
        filt[t] = w / c
        xi_pred = Pt[t].T @ filt[t]
    return filt, ll


def binom_logf(k, n, shares):
    shares = np.clip(np.asarray(shares, dtype=float), 1e-9, 1.0 - 1e-9)
    return stats.binom.logpmf(np.asarray(k)[:, None], np.asarray(n)[:, None], shares[None, :])


def _ms2_unpack(theta):
    a, b, c0, c1 = theta
    s0 = special.expit(a)
    s1 = special.expit(a + math.exp(min(b, 5.0)))             # ordered: no label switching
    p00 = float(np.clip(special.expit(c0), 1e-6, 1 - 1e-6))
    p11 = float(np.clip(special.expit(c1), 1e-6, 1 - 1e-6))
    return np.array([s0, s1]), np.array([[p00, 1.0 - p00], [1.0 - p11, p11]])


def fit_ms2(k, n, seed=0, n_starts=6):
    rng = np.random.default_rng(seed)

    def nll(theta):
        shares, P = _ms2_unpack(theta)
        return -hamilton_filter(binom_logf(k, n, shares), P)[1]

    best = None
    for _ in range(n_starts):
        x0 = np.array([rng.normal(-1.0, 0.7), rng.normal(0.0, 0.5), rng.normal(2.0, 0.5), rng.normal(2.0, 0.5)])
        res = optimize.minimize(nll, x0, method="Nelder-Mead",
                                options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 4000})
        if best is None or res.fun < best.fun:
            best = res
    shares, P = _ms2_unpack(best.x)
    filt, ll = hamilton_filter(binom_logf(k, n, shares), P)
    return {"shares": shares, "P": P, "filtered": filt, "loglik": ll}


def simulate_de_share_series(n_years, shares, P, mean_defaults, seed, s0=0):
    rng = np.random.default_rng(seed)
    s = simulate_regime_path(n_years, np.asarray(P, dtype=float), s0, rng)
    n = rng.poisson(mean_defaults, size=n_years)
    k = rng.binomial(n, np.asarray(shares)[s])
    return s, k, n
```


### Listing 14.5: Sanity checks for the cycle engine {#code-14-5}

```python
# block 5 of 5: sanity checks (each prints PASS/FAIL and asserts)
def check(name, ok):
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
    assert ok, name


prm = LMEParams()
check("F(2)/p = 0.70 at the calibrated eta", abs((1 - math.exp(-(2 / prm.eta) ** prm.k)) - 0.70) < 1e-12)

one = LMEParams(P=np.eye(2))                                     # single-regime world for closed forms
path1 = np.ones(10, dtype=np.int8)
df1 = simulate_cohort(50_000, one, seed=14, regime_path=path1)
aj = aalen_johansen(df1)
resid = float((aj["S"] + aj["F_H"] + aj["F_D"] + aj["F_C"] - 1.0).abs().max())
check("S + F_H + F_D + F_C = 1 at every jump (1e-10)", resid < 1e-10)
lam1 = one.lam_H[1] + one.lam_D[1] + one.lam_C
for t in (1.0, 3.0, 5.0):
    for col, lk in (("F_H", one.lam_H[1]), ("F_D", one.lam_D[1])):
        truth = lk / lam1 * (1 - math.exp(-lam1 * t))
        est = step_at(aj["time"].to_numpy(), aj[col].to_numpy(), t)
        se = math.sqrt(truth * (1 - truth) / 50_000)
        check(f"Aalen-Johansen {col}({t:.0f}) within 4 SE of closed form", abs(est - truth) < 4 * se)

tk, naive = km_naive_cif(df1, cause=2)
check("Kaplan-Meier trap: 1 - KM_D(5) > F_D(5)",
      step_at(tk, naive, 5.0) > step_at(aj["time"].to_numpy(), aj["F_D"].to_numpy(), 5.0))

f1 = df1[df1["time_since_de"].isna()]
n_h, n_d = int((f1["event"] == 1).sum()), int((f1["event"] == 2).sum())
share_true = one.lam_D[1] / (one.lam_H[1] + one.lam_D[1])
share_se = math.sqrt(share_true * (1 - share_true) / (n_h + n_d))
check("DE share of first defaults -> lam_D/(lam_H+lam_D)", abs(n_d / (n_h + n_d) - share_true) < 4 * share_se)

rng = np.random.default_rng(7)
member = rng.random(400_000) < prm.pi
r = np.where(member, rng.beta(*prm.ab_in, 400_000), rng.beta(*prm.ab_out, 400_000))
mean_f, var_f, between_f = coalition_mixture_moments(prm.pi, prm.ab_in, prm.ab_out)
pm = member.mean()
between_s = pm * (1 - pm) * (r[member].mean() - r[~member].mean()) ** 2
check("mixture mean matches simulation", abs(r.mean() - mean_f) < 0.01)
check("mixture variance matches simulation", abs(r.var() - var_f) < 0.002)
check("between-group variance matches simulation", abs(between_s - between_f) < 0.002)
check("Serta between-group sd ~ 0.245",
      abs(math.sqrt(coalition_mixture_moments(0.526, (74, 26), (25, 75))[2]) - 0.245) < 0.001)

rng = np.random.default_rng(2026)
N = 20_000
susc = rng.random(N) < prm.p_redefault
u_true = np.where(susc, prm.eta * rng.weibull(prm.k, N), np.inf)
cens = rng.uniform(0.5, 10.0, N)
u_obs, d_obs = np.minimum(u_true, cens), (u_true <= cens).astype(int)
p_hat, k_hat, eta_hat, _ = fit_cure_weibull(u_obs, d_obs)
print(f"cure-Weibull fit: p={p_hat:.3f}, k={k_hat:.3f}, eta={eta_hat:.3f}")
check("cure fit: p within 0.03", abs(p_hat - prm.p_redefault) < 0.03)
check("cure fit: k within 0.15", abs(k_hat - prm.k) < 0.15)
check("cure fit: eta within 15%", abs(eta_hat / prm.eta - 1) < 0.15)
check("cure fit: F(2)/p ~ 0.70", abs((1 - math.exp(-(2 / eta_hat) ** k_hat)) - 0.70) < 0.03)
short = np.minimum(u_true, 14 / 12)                                # ROBO's 14 months of follow-up
lam_exp = (u_true <= 14 / 12).sum() / short.sum()
print(f"ROBO's exponential: hazard {lam_exp:.3f}/yr, mean {1 / lam_exp:.1f} yrs, "
      f"10y default prob {1 - math.exp(-10 * lam_exp):.0%} vs truth {prm.p_redefault:.0%}")
check("exponential on short follow-up overstates the 10y default prob", 1 - math.exp(-10 * lam_exp) > 0.5)

df_el = simulate_cohort(60_000, one, seed=99, regime_path=path1)
for side in ("in", "out", "blend"):
    ex, mc = expected_loss(one, 3.0, side), expected_loss_mc(df_el, 3.0, side)
    print(f"EL(3y) {side:>5}: exact {ex:.4f}  MC {mc:.4f}")
    check(f"EL exact vs MC ({side})", abs(ex - mc) < 0.005)
check("excluded holder's EL exceeds included holder's",
      expected_loss(one, 3.0, "out") > expected_loss(one, 3.0, "in"))

s_true, k_de, n_def = simulate_de_share_series(80, [0.30, 0.63], [[0.92, 0.08], [0.10, 0.90]], 90, seed=5)
fit = fit_ms2(k_de, n_def, seed=1)
filt = fit["filtered"]
check("filtered probabilities in [0, 1]", bool(((filt >= 0) & (filt <= 1)).all()))
check("filtered rows sum to 1", bool(np.allclose(filt.sum(axis=1), 1.0)))
agree = float(((filt[:, 1] > 0.5).astype(int) == s_true).mean())
print(f"MS2 shares {np.round(fit['shares'], 3)}, regime agreement {agree:.0%}")
check("filtered regime agrees with truth > 85% of years", agree > 0.85)

check("P vs Q: implied-hazard ratio 0.60/0.77 ~ 0.779", abs((0.06 / 0.77) / (0.06 / 0.60) - 0.779) < 0.001)
check("co-op c=0.70, n=10: break prob ~7.0%", abs(coop_break_prob(0.70) - 0.0702) < 0.0005)
check("co-op c=0.90, n=15: break prob < 0.1%", coop_break_prob(0.90, n=15) < 1e-3)
check("co-op below the blocking line is decorative", coop_break_prob(0.40) == 1.0)
check("Serta: 734 x 47.43% ~ 348 (USD mm)", abs(734 * 0.4743 - 348) < 1.0)
check("Serta: 484.88 - 895 x 0.25 = 261.13 (USD mm)", abs(484.88 - 895 * 0.25 - 261.13) < 1e-9)
```


## F.15: Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control {#code-15}

Listings from `15_ch15_event_driven_mna_and_coc.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 15.1: Bond math and the 101 change-of-control put {#code-15-1}

```python
# ---- Chapter 15 reference engine, block 1: bond math and the 101 CoC put ----
import warnings
import numpy as np
import pandas as pd
from scipy import optimize
from scipy.stats import norm
from scipy.interpolate import PchipInterpolator


def tsy_zero_curve(t):
    """Illustrative continuously compounded UST zero rate (decimal) at tenor t (years).
    A Nelson-Siegel shape chosen to look like 2025-26. NOT market data."""
    t = np.maximum(np.asarray(t, dtype=float), 1e-6)
    b0, b1, b2, lam = 0.0450, -0.0060, 0.0040, 1.8
    x = t / lam
    f = (1.0 - np.exp(-x)) / x
    return b0 + b1 * f + b2 * (f - np.exp(-x))


def bond_price(coupon, maturity_years, spread, curve=tsy_zero_curve, freq=2):
    """Price per 100 face. coupon in percent of par per year; spread decimal, scalar or (m,).
    Coupon dates are counted back from maturity. Keep maturity_years on the half-year grid
    so we value on a coupon date (clean = dirty). Returns shape (m,)."""
    s = np.atleast_1d(np.asarray(spread, dtype=float))
    n = int(np.ceil(maturity_years * freq - 1e-9))
    if n <= 0:
        return np.full(s.shape, 100.0)
    t = maturity_years - np.arange(n)[::-1] / freq                    # (n,), all > 0
    y = curve(t)                                                       # (n,)
    cf = np.full(n, coupon / freq)
    cf[-1] += 100.0
    disc = np.exp(-(y[None, :] + s[:, None]) * t[None, :])            # (m, n)
    return disc @ cf


def price_coc_put(deal_prob, trigger_prob_given_deal, post_spread_sampler, coupon,
                  maturity_years, curve=tsy_zero_curve, t_close=0.75, strike=101.0,
                  defeasance_prob=0.0, n_paths=200_000, seed=7):
    """Value at signing (points per 100 face) of a 101 change-of-control put."""
    if not 0.0 <= deal_prob <= 1.0:
        raise ValueError(f"deal_prob must be in [0,1], got {deal_prob}")
    zero = dict(value=0.0, stderr=0.0, moneyness_ratio=np.nan, mean_intrinsic=0.0)
    if maturity_years <= t_close:
        warnings.warn("bond matures before the expected close: put is worthless")
        return zero
    scalar_trig = not callable(trigger_prob_given_deal)
    scalar_def = not callable(defeasance_prob)
    if deal_prob == 0.0 or (scalar_trig and trigger_prob_given_deal == 0.0) \
            or (scalar_def and defeasance_prob == 1.0):
        return zero
    rng = np.random.default_rng(seed)
    s = np.clip(np.asarray(post_spread_sampler(rng, n_paths), dtype=float), 0.0, None)
    p_post = bond_price(coupon, maturity_years - t_close, s, curve)   # (n,)
    intrinsic = np.maximum(strike - p_post, 0.0)                       # (n,)
    p_trig = (np.full(n_paths, float(trigger_prob_given_deal)) if scalar_trig
              else np.clip(np.asarray(trigger_prob_given_deal(s), dtype=float), 0.0, 1.0))
    p_def = (np.full(n_paths, float(defeasance_prob)) if scalar_def
             else np.clip(np.asarray(defeasance_prob(intrinsic), dtype=float), 0.0, 1.0))
    disc = float(np.exp(-curve(t_close) * t_close))
    per_path = deal_prob * disc * p_trig * (1.0 - p_def) * intrinsic
    mean_int = float(intrinsic.mean())
    ratio = (float((p_trig * intrinsic).mean() / p_trig.mean() / mean_int)
             if mean_int > 0.0 and p_trig.mean() > 0.0 else np.nan)
    return dict(value=float(per_path.mean()),
                stderr=float(per_path.std(ddof=1) / np.sqrt(n_paths)),
                moneyness_ratio=ratio, mean_intrinsic=mean_int)


# --- sanity checks, block 1 ---
def const_sampler(s0):
    return lambda rng, n: np.full(n, s0)

# (1) a degenerate spread sampler reproduces the closed form pi_d * pi_trig * B * (K - P)^+
v = price_coc_put(0.85, 0.9, const_sampler(0.035), 1.85, 5.25, t_close=0.75)
p_star = bond_price(1.85, 4.5, 0.035)[0]
closed = 0.85 * 0.9 * float(np.exp(-tsy_zero_curve(0.75) * 0.75)) * max(101.0 - p_star, 0.0)
assert abs(v["value"] - closed) < 1e-10, (v, closed)

# (2) a high-coupon bond into a tight acquirer curve: the put is exactly worthless
v_otm = price_coc_put(0.9, 1.0, const_sampler(0.005), 6.875, 3.75, t_close=0.75)
assert bond_price(6.875, 3.0, 0.005)[0] > 101.0 and v_otm["value"] == 0.0

# (3) an LBO with a spread-dependent ratings leg: M > 1, and independence understates
lbo_spread = lambda rng, n: 0.035 * np.exp(0.35 * rng.standard_normal(n) - 0.5 * 0.35 ** 2)
ratings_leg = lambda s: 1.0 / (1.0 + np.exp(-(s - 0.025) / 0.004))   # both agencies cut
lbo = price_coc_put(0.85, ratings_leg, lbo_spread, 1.85, 5.25, t_close=0.75)
pbar = float(ratings_leg(lbo_spread(np.random.default_rng(7), 200_000)).mean())
lbo_indep = price_coc_put(0.85, pbar, lbo_spread, 1.85, 5.25, t_close=0.75)
assert lbo["moneyness_ratio"] > 1.0 and lbo["value"] > lbo_indep["value"]

# (4) a sponsor that defeases whenever the put is more than 5 points in the money
lbo_def = price_coc_put(0.85, ratings_leg, lbo_spread, 1.85, 5.25, t_close=0.75,
                        defeasance_prob=lambda intr: (intr > 5.0).astype(float))
assert lbo_def["value"] < lbo["value"]
print(f"1.85% LBO put: {lbo['value']:.2f} +/- {lbo['stderr']:.3f} pts, M = {lbo['moneyness_ratio']:.3f}; "
      f"independent: {lbo_indep['value']:.2f}; with defeasance: {lbo_def['value']:.2f}")
```


### Listing 15.2: Portability as a short digital on sponsor-chosen leverage {#code-15-2}

```python
# ---- block 2: portability as a short digital on sponsor-chosen leverage ----
def portability_put_survival(addback, lev_test=5.0, ebitda_sigma=0.25, ev_multiple=11.0,
                             max_equity_share=0.45, n_paths=100_000, seed=21):
    """Probability that a portable CoC put survives a sponsor who reads the test first.
    Reported EBITDA at close is lognormal with mean 1.0 (signing EBITDA = 1).
    Returns (survival_prob, mean EBITDA | put survives, mean EBITDA | deal ported)."""
    if addback < 0.0 or lev_test <= 0.0:
        raise ValueError("addback must be >= 0 and lev_test > 0")
    rng = np.random.default_rng(seed)
    ebitda = np.exp(ebitda_sigma * rng.standard_normal(n_paths) - 0.5 * ebitda_sigma ** 2)
    f_min = (1.0 - max_equity_share) * ev_multiple            # minimum debt, turns of signing EBITDA
    survives = f_min > lev_test * (1.0 + addback) * ebitda    # sponsor cannot pass the test
    bad = float(ebitda[survives].mean()) if survives.any() else np.nan
    good = float(ebitda[~survives].mean()) if (~survives).any() else np.nan
    return float(survives.mean()), bad, good


# --- sanity checks, block 2 ---
grid = [0.0, 0.1, 0.2, 0.3, 0.4]
surv = [portability_put_survival(a)[0] for a in grid]
assert all(x >= y for x, y in zip(surv, surv[1:]))            # more add-backs, fewer surviving puts
s20, bad20, good20 = portability_put_survival(0.20)
closed20 = norm.cdf((np.log(0.55 * 11.0 / (5.0 * 1.2)) + 0.5 * 0.25 ** 2) / 0.25)
assert abs(s20 - closed20) < 4.0 * np.sqrt(closed20 * (1.0 - closed20) / 100_000)
assert bad20 < good20                                          # surviving puts live in bad states
print("put survival by add-back ratio:", dict(zip(grid, np.round(surv, 3))))
```


### Listing 15.3: The special mandatory redemption gauge: Z-spread and implied break probability {#code-15-3}

```python
# ---- block 3: special mandatory redemption gauge ----
def z_spread(price, coupon, maturity_years, curve=tsy_zero_curve):
    """Constant spread (decimal) over the UST zero curve that reprices the bond."""
    f = lambda s: bond_price(coupon, maturity_years, s, curve)[0] - price
    return optimize.brentq(f, -0.05, 1.0, xtol=1e-12)


def curve_match_close_price(tranches, curve=tsy_zero_curve):
    """P_close for each SMR tranche from the issuer's non-SMR tranches (PCHIP in Z-spread)."""
    need = {"tranche_id", "coupon", "maturity", "price", "is_smr"}
    if need - set(tranches.columns):
        raise KeyError(f"missing columns: {need - set(tranches.columns)}")
    smr = tranches["is_smr"].astype(bool)
    base = tranches.loc[~smr].sort_values("maturity")
    mats = base["maturity"].to_numpy(dtype=float)
    if mats.size < 2 or np.any(np.diff(mats) <= 0):
        raise ValueError("need >= 2 non-SMR tranches with distinct maturities")
    z = np.array([z_spread(p, c, m, curve) for p, c, m in
                  zip(base["price"], base["coupon"], base["maturity"])])
    interp = PchipInterpolator(mats, z, extrapolate=False)
    out = tranches.loc[smr, ["tranche_id", "coupon", "maturity", "price"]].copy()
    m = out["maturity"].to_numpy(dtype=float)
    out["z_close"] = interp(np.clip(m, mats[0], mats[-1]))      # flat beyond the nodes
    out["extrapolated"] = (m < mats[0]) | (m > mats[-1])
    out["p_close"] = [bond_price(c, mm, zz, curve)[0]
                      for c, mm, zz in zip(out["coupon"], m, out["z_close"])]
    return out.reset_index(drop=True)


def smr_fail_leg(coupon, t_f, y_f, k=101.0, freq=2):
    """Value today of coupons paid on or before t_f plus (k + accrued) at t_f, at yield y_f."""
    if t_f <= 0.0:
        raise ValueError("t_f must be positive")
    n_cpn = int(np.floor(t_f * freq + 1e-9))
    pay = np.arange(1, n_cpn + 1) / freq
    accrued = coupon * (t_f - n_cpn / freq)
    return float(np.sum(coupon / freq * np.exp(-y_f * pay)) + (k + accrued) * np.exp(-y_f * t_f))


def smr_price(pi_f, p_close, g_f):
    if not 0.0 <= pi_f <= 1.0:
        raise ValueError("pi_f must be in [0,1]")
    return pi_f * g_f + (1.0 - pi_f) * p_close


def smr_implied_break_prob(p_obs, p_close, g_f, tol=1e-6):
    denom = p_close - g_f
    if abs(denom) < tol:
        raise ValueError("P_close ~ G_f: the SMR price carries no information about pi_f")
    raw = (p_close - p_obs) / denom
    return dict(pi_f=float(np.clip(raw, 0.0, 1.0)), raw=float(raw), clipped=not 0.0 <= raw <= 1.0)


def smr_duration(pi_f, g_f, d_fail, p_close, d_close):
    """Value-weighted probabilistic duration of an SMR tranche."""
    w = pi_f * g_f / smr_price(pi_f, p_close, g_f)
    return w * d_fail + (1.0 - w) * d_close


def spread_duration(coupon, maturity_years, s, curve=tsy_zero_curve, h=1e-4):
    up, dn = bond_price(coupon, maturity_years, [s + h, s - h], curve)
    return float((dn - up) / (2.0 * h * bond_price(coupon, maturity_years, s, curve)[0]))


# --- sanity checks, block 3 ---
g = smr_fail_leg(4.60, 0.25, 0.046)
assert abs(g - 102.15 * np.exp(-0.046 * 0.25)) < 1e-12              # the worked number
for pi in np.linspace(0.0, 1.0, 11):                                  # round trip
    assert abs(smr_implied_break_prob(smr_price(pi, 99.0, g), 99.0, g)["pi_f"] - pi) < 1e-10
assert smr_price(0.5, 103.0, g) < smr_price(0.2, 103.0, g)            # rates fell: holder short the digital
true_z = lambda m: 0.0060 + 0.0008 * m                                # a linear issuer curve
book = pd.DataFrame({"tranche_id": ["L26", "L28", "N34", "N54", "S27", "S31"],
                     "coupon": [3.50, 4.50, 5.00, 5.50, 4.60, 4.90],
                     "maturity": [1.5, 3.5, 9.5, 29.5, 2.5, 6.5],
                     "is_smr": [False, False, False, False, True, True]})
book["price"] = [bond_price(c, m, true_z(m))[0] for c, m in zip(book["coupon"], book["maturity"])]
fit = curve_match_close_price(book)
assert np.allclose(fit["z_close"], true_z(fit["maturity"].to_numpy()), atol=1e-9)   # PCHIP is exact on lines
assert not fit["extrapolated"].any()
obs = fit["p_close"].to_numpy() + np.array([0.30, 0.45])              # SMR tranches trade rich
gs = [smr_fail_leg(c, 0.25, tsy_zero_curve(0.25) + true_z(0.25)) for c in fit["coupon"]]
pis = [smr_implied_break_prob(o, pc, gg)["pi_f"] for o, pc, gg in zip(obs, fit["p_close"], gs)]
d_close = spread_duration(4.60, 2.5, true_z(2.5))
print("implied break probs:", np.round(pis, 3),
      "| SMR duration:", round(smr_duration(pis[0], gs[0], 0.25, fit["p_close"][0], d_close), 2))
```


### Listing 15.4: Deal clocks as competing-risks survival data {#code-15-4}

```python
# ---- block 4: deal clocks as competing-risks survival data, from scratch ----
COVARIATES = ["second_request", "horizontal", "log_value", "n_jurisdictions", "sponsor", "regime"]
BETA_TRUE = {1: np.array([-1.20, -0.30, -0.15, -0.10, 0.20, -0.40]),   # close
             2: np.array([0.60, 0.20, -0.10, 0.05, 0.30, 0.30]),       # abandon
             3: np.array([1.50, 1.00, 0.20, 0.00, -0.50, 0.80])}       # litigated block
WEIBULL = {1: (1.6, 0.55), 2: (1.1, 6.0), 3: (1.3, 12.0)}              # (shape, scale in years)


def synthetic_deal_cohort(n=600, seed=11):
    rng = np.random.default_rng(seed)
    X = pd.DataFrame({"second_request": rng.binomial(1, 0.15, n), "horizontal": rng.binomial(1, 0.40, n),
                      "log_value": rng.standard_normal(n), "n_jurisdictions": rng.poisson(2.0, n),
                      "sponsor": rng.binomial(1, 0.30, n), "regime": rng.binomial(1, 0.50, n)})
    xv = X[COVARIATES].to_numpy(dtype=float)
    latent = np.column_stack([b * (rng.exponential(size=n) / np.exp(xv @ BETA_TRUE[k])) ** (1.0 / a)
                              for k, (a, b) in WEIBULL.items()])           # inverse-CDF Weibull PH
    t_event, cause = latent.min(axis=1), latent.argmin(axis=1) + 1
    t_cens = rng.uniform(0.5, 4.0, n)                                      # independent data cutoff
    X["time"] = np.minimum(t_event, t_cens)
    X["cause"] = np.where(t_event <= t_cens, cause, 0)
    return X


def _risk_table(times, events):
    times, events = np.asarray(times, dtype=float), np.asarray(events, dtype=int)
    if times.ndim != 1 or times.shape != events.shape or np.any(times < 0):
        raise ValueError("times and events must be 1-d, same length, times >= 0")
    ut, d = np.unique(times[events == 1], return_counts=True)
    n_risk = times.size - np.searchsorted(np.sort(times), ut, side="left")
    return ut, n_risk, d


def kaplan_meier(times, events, z=1.96):
    ut, n, d = _risk_table(times, events)
    S = np.cumprod(1.0 - d / n)
    with np.errstate(divide="ignore", invalid="ignore"):
        gw = np.cumsum(np.where(n > d, d / (n * (n - d)), np.inf))       # Greenwood
        se = np.where(S > 0, S * np.sqrt(gw), 0.0)
    return pd.DataFrame({"t": ut, "n_risk": n, "d": d, "S": S, "se": se,
                         "lo": np.clip(S - z * se, 0, 1), "hi": np.clip(S + z * se, 0, 1)})


def nelson_aalen(times, events):
    ut, n, d = _risk_table(times, events)
    return pd.DataFrame({"t": ut, "H": np.cumsum(d / n), "var": np.cumsum(d / n ** 2)})


def aalen_johansen(times, cause, n_causes=3):
    times, cause = np.asarray(times, dtype=float), np.asarray(cause, dtype=int)
    ut, n, d = _risk_table(times, (cause > 0).astype(int))
    S = np.cumprod(1.0 - d / n)
    S_minus = np.concatenate(([1.0], S[:-1]))
    out = {"t": ut, "S": S}
    for k in range(1, n_causes + 1):
        tk, ck = np.unique(times[cause == k], return_counts=True)
        dk = np.zeros(ut.size)
        dk[np.searchsorted(ut, tk)] = ck
        out[f"F{k}"] = np.cumsum(S_minus * dk / n)
    return pd.DataFrame(out)


def cox_ph(times, event, X):
    t, e, X = (np.asarray(times, dtype=float), np.asarray(event, dtype=int), np.asarray(X, dtype=float))
    order = np.argsort(-t, kind="mergesort")
    t, e, X = t[order], e[order], X[order]
    last = np.searchsorted(-t, -t, side="right") - 1        # risk set of row i = rows 0..last[i]
    Xc, ev = X - X.mean(axis=0), e == 1                     # centring leaves beta unchanged
    if not ev.any():
        raise ValueError("no events")

    def parts(beta):
        eta = Xc @ beta
        w = np.exp(eta - eta.max())                         # log-sum-exp guard
        s0 = np.cumsum(w)[last]
        s1 = np.cumsum(w[:, None] * Xc, axis=0)[last]
        s2 = np.cumsum(w[:, None, None] * Xc[:, :, None] * Xc[:, None, :], axis=0)[last]
        xbar = s1[ev] / s0[ev, None]
        ll = np.sum(eta[ev] - eta.max() - np.log(s0[ev]))
        info = np.sum(s2[ev] / s0[ev, None, None] - xbar[:, :, None] * xbar[:, None, :], axis=0)
        return ll, np.sum(Xc[ev] - xbar, axis=0), info, xbar

    res = optimize.minimize(lambda b: (-parts(b)[0], -parts(b)[1]), np.zeros(X.shape[1]), jac=True,
                            hess=lambda b: parts(b)[2], method="trust-exact", options={"gtol": 1e-6})
    beta = res.x
    _, _, info, xbar = parts(beta)
    se = np.sqrt(np.diag(np.linalg.inv(info)))
    eta = X @ beta                                          # uncentred: baseline at x = 0
    s0 = np.cumsum(np.exp(eta - eta.max()))[last] * np.exp(eta.max())
    ut, d = np.unique(t[ev], return_counts=True)
    H0 = np.cumsum(d / s0[np.searchsorted(-t, -ut, side="left")])
    resid = Xc[ev] - xbar                                   # Schoenfeld residuals
    ph_corr = np.array([np.corrcoef(t[ev], resid[:, j])[0, 1] for j in range(X.shape[1])])
    return dict(beta=beta, se=se, baseline=np.column_stack([ut, H0]), ph_corr=ph_corr,
                converged=bool(res.success))


def bayes_deal_prob_path(pi0, milestones):
    """milestones: (t, q_deal, q_break) = P(milestone passes quietly | quiet so far, hypothesis)."""
    if not 0.0 < pi0 < 1.0:
        raise ValueError("pi0 must be in (0,1)")
    rows, pi = [(0.0, pi0)], pi0
    for t, q_d, q_b in milestones:
        if not (0.0 < q_d <= 1.0 and 0.0 < q_b <= 1.0):
            raise ValueError("quiet probabilities must be in (0,1]")
        pi = pi * q_d / (pi * q_d + (1.0 - pi) * q_b)
        rows.append((t, pi))
    return pd.DataFrame(rows, columns=["t", "pi_d"])


# --- sanity checks, block 4 ---
t_nc = np.random.default_rng(3).exponential(1.0, 50)                # no censoring: KM = 1 - ECDF
assert np.allclose(kaplan_meier(t_nc, np.ones(50, dtype=int))["S"], 1.0 - np.arange(1, 51) / 50)
cohort = synthetic_deal_cohort()
aj = aalen_johansen(cohort["time"], cohort["cause"])
assert np.allclose(aj[["F1", "F2", "F3"]].sum(axis=1), 1.0 - aj["S"], atol=1e-12)
km = kaplan_meier(cohort["time"], (cohort["cause"] > 0).astype(int))
assert np.allclose(km["S"].to_numpy(), aj["S"].to_numpy())
fit = cox_ph(cohort["time"], (cohort["cause"] == 1).astype(int), cohort[COVARIATES])
assert np.all(np.abs(fit["beta"] - BETA_TRUE[1]) < 4.0 * fit["se"]), (fit["beta"], fit["se"])
path = bayes_deal_prob_path(0.80, [(30 / 365, 0.97, 0.55), (0.15, 0.95, 0.70), (0.50, 0.99, 0.90)])
assert path["pi_d"].iloc[0] == 0.80 and path["pi_d"].is_monotonic_increasing
print("close-hazard beta:", np.round(fit["beta"], 2), "+/-", np.round(fit["se"], 2))
print("P(block by 2y):", round(float(np.interp(2.0, aj["t"], aj["F3"])), 3),
      "| PH-check corr:", np.round(fit["ph_corr"], 2), "| pi_d path:", np.round(path["pi_d"].to_numpy(), 3))
```


## F.16: Chapter 16: Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims {#code-16}

Listings from `16_ch16_post_reorg_equities_and_claims.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 16.1: The forced-seller overhang model, calibrated to fallen-angel aggregates {#code-16-1}

```python
import numpy as np
from dataclasses import dataclass
from typing import Optional
from scipy.stats import norm
from scipy.optimize import brentq

RNG = np.random.default_rng(16)   # chapter seed; every block below reuses it
TRADING_DAYS = 252


def trap(y, x):
    """Trapezoid rule (avoids numpy version differences in trapz/trapezoid)."""
    y, x = np.asarray(y, float), np.asarray(x, float)
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * np.diff(x)))


@dataclass
class ForcedSellerOverhang:
    """Overhang Q (USD mm at plan value), arbitrage capital M (USD mm), discount -kappa*Q/M.

    theta, rho, alpha are per year; s = t - t0 in years (s >= 0); physical measure P.
    alpha=None: the whole overhang lands at t0. Otherwise it is delivered at rate alpha.
    """
    Q0: float
    theta: float
    M0: float
    M_star: float
    rho: float
    kappa: float
    alpha: Optional[float] = None

    def __post_init__(self):
        if self.Q0 < 0 or self.kappa < 0 or self.rho < 0:
            raise ValueError("Q0, kappa, rho must be non-negative")
        if self.theta <= 0 or self.M0 <= 0 or self.M_star <= 0:
            raise ValueError("theta, M0, M_star must be positive")
        if self.alpha is not None and self.alpha <= 0:
            raise ValueError("alpha must be positive")

    def Q(self, s):
        s = np.asarray(s, float)
        if self.alpha is None:
            return self.Q0 * np.exp(-self.theta * s)
        a, th = self.alpha, self.theta
        if abs(th - a) < 1e-10:                       # limit theta -> alpha
            return self.Q0 * a * s * np.exp(-a * s)
        return self.Q0 * a / (th - a) * (np.exp(-a * s) - np.exp(-th * s))

    def Qdot(self, s):
        s = np.asarray(s, float)
        inflow = 0.0 if self.alpha is None else self.Q0 * self.alpha * np.exp(-self.alpha * s)
        return inflow - self.theta * self.Q(s)

    def M(self, s):
        s = np.asarray(s, float)
        return self.M_star + (self.M0 - self.M_star) * np.exp(-self.rho * s)

    def Mdot(self, s):
        return self.rho * (self.M_star - self.M(s))

    def discount(self, s):
        """E^P[p_s - v_s]: log-price discount (<= 0)."""
        return -self.kappa * self.Q(s) / self.M(s)

    def drift(self, s):
        """mu_s = d/ds E^P[p_s - v_s], per year."""
        Q, M = self.Q(s), self.M(s)
        return self.kappa * (-self.Qdot(s) / M + Q * self.Mdot(s) / M**2)

    def half_life(self):
        return np.log(2.0) / self.theta

    def peak_time(self):
        """Time of maximum overhang (= peak discount when capital is constant)."""
        if self.alpha is None:
            return 0.0
        a, th = self.alpha, self.theta
        if abs(th - a) < 1e-10:
            return 1.0 / th
        return np.log(th / a) / (th - a)


def theta_from_windows(w1, w2, window_years=0.5):
    """Single-exponential fit: w2 / w1 = exp(-theta * window)."""
    if not (w1 > w2 > 0):
        raise ValueError("need w1 > w2 > 0")
    return -np.log(w2 / w1) / window_years


def simulate_residual_panel(model, n_names=200, years=1.0, noise_daily=0.02, rng=RNG):
    """IDO-stripped log-price deviations p - v for n_names emergences: discount + iid noise."""
    s = np.arange(int(years * TRADING_DAYS) + 1) / TRADING_DAYS
    eps = rng.normal(0.0, noise_daily, size=(n_names, s.size))
    return s, model.discount(s)[None, :] + eps


def fit_theta_loglinear(s, panel, max_years=0.5, floor=0.005):
    """Fit log(-mean deviation) = log(A) - theta * s on the early, well-identified window."""
    mean_dev = panel.mean(axis=0)
    mask = (s <= max_years) & (-mean_dev > floor)
    slope, intercept = np.polyfit(s[mask], np.log(-mean_dev[mask]), 1)
    return -slope, np.exp(intercept)


def overhang_signal(Q_hat, M_hat, kappa_hat, theta_hat, executed_frac):
    """Expected excess drift (per year). Exactly zero once constrained holders are out."""
    Q_rem = np.clip(np.asarray(Q_hat, float) * (1.0 - np.asarray(executed_frac, float)), 0.0, None)
    return kappa_hat * theta_hat * Q_rem / np.maximum(np.asarray(M_hat, float), 1e-9)


# --- calibration to the fallen-angel aggregates (Dynkin p.158; illustrative) ---
theta_fa = theta_from_windows(5.75, 1.04)
A_fa = 5.75 / (1.0 - np.exp(-theta_fa * 0.5))
w3_pred = A_fa * np.exp(-theta_fa) * (1.0 - np.exp(-theta_fa * 0.5))
assert 3.3 < theta_fa < 3.5, theta_fa
assert 2.3 < 12 * np.log(2) / theta_fa < 2.5            # half-life in months
assert w3_pred < 0.86                                     # data need a slow component

# --- sanity checks on the model ---
s = np.linspace(0.0, 3.0, 3001)
ovh = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=60.0, M_star=60.0, rho=0.0, kappa=0.3)
assert abs(trap(ovh.drift(s), s) - (ovh.discount(3.0) - ovh.discount(0.0))) < 1e-4
assert abs(ovh.discount(ovh.half_life()) - 0.5 * ovh.discount(0.0)) < 1e-12
assert abs(-ovh.discount(0.0) - 0.15) < 1e-12              # kappa*Q0/M = 15% total

ovh_sched = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=60.0, M_star=60.0,
                                 rho=0.0, kappa=0.3, alpha=5.0)
grid = np.linspace(0.0, 2.0, 200001)
s_num = grid[np.argmin(ovh_sched.discount(grid))]
assert abs(s_num - ovh_sched.peak_time()) < 1e-4
assert 0.2 < ovh_sched.peak_time() < 0.3                   # about three months

ovh_slow = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=30.0, M_star=60.0, rho=1.0, kappa=0.3)
assert np.all(ovh_slow.drift(s) > ovh.drift(s))            # slow capital adds drift
assert abs(trap(ovh_slow.drift(s), s) - 0.3) < 1e-3        # total = kappa*Q0/M0

# --- panel fit recovers theta ---
s_d, panel = simulate_residual_panel(ovh)
theta_hat, A_hat = fit_theta_loglinear(s_d, panel)
assert abs(theta_hat / theta_fa - 1.0) < 0.10, theta_hat
assert abs(A_hat / 0.15 - 1.0) < 0.10, A_hat
assert overhang_signal(30.0, 60.0, 0.3, theta_hat, 1.0) == 0.0

print(f"theta={theta_fa:.2f}/yr  half-life={12*np.log(2)/theta_fa:.1f}m  "
      f"peak={12*ovh_sched.peak_time():.1f}m  panel theta_hat={theta_hat:.2f}")
```


### Listing 16.2: Rights offerings and backstops {#code-16-2}

```python
# --- Block 2: rights offerings and backstops (reuses RNG, norm, trap) ---

def _d1d2(S, K, T, sigma, r):
    vs = sigma * np.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / vs
    return d1, d1 - vs


def bs_call(S, K, T, sigma, r=0.0):
    S, K = np.asarray(S, float), np.asarray(K, float)
    if T <= 0 or sigma <= 0:
        return np.maximum(S - K * np.exp(-r * max(T, 0.0)), 0.0)
    d1, d2 = _d1d2(S, K, T, sigma, r)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def bs_put(S, K, T, sigma, r=0.0):
    S, K = np.asarray(S, float), np.asarray(K, float)
    if T <= 0 or sigma <= 0:
        return np.maximum(K * np.exp(-r * max(T, 0.0)) - S, 0.0)
    d1, d2 = _d1d2(S, K, T, sigma, r)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


@dataclass
class RightsOffering:
    """n0: plan shares before the offering, excluding fee shares (mm); m: rights shares (mm);
    K: subscription price per share. x: pre-money value per plan share at funding."""
    n0: float
    m: float
    K: float

    def __post_init__(self):
        if min(self.n0, self.m, self.K) <= 0:
            raise ValueError("n0, m, K must be positive")

    @property
    def dilution(self):
        return self.n0 / (self.n0 + self.m)

    @property
    def n_eff(self):
        return self.m * self.n0 / (self.n0 + self.m)

    def post_money(self, x):
        return (np.asarray(x, float) * self.n0 + self.m * self.K) / (self.n0 + self.m)

    def right_value_per_plan_share(self, x):
        return self.m / (self.n0 + self.m) * np.maximum(np.asarray(x, float) - self.K, 0.0)

    def backstop_payoff(self, x):
        """USD mm P&L of taking all unsubscribed shares under rational subscription."""
        return -self.n_eff * np.maximum(self.K - np.asarray(x, float), 0.0)

    def fair_fee(self, x0, sigma, T, r=0.0):
        """Fee (fraction of m*K, cash-equivalent) equal to the put the backstop sells."""
        return self.dilution * float(bs_put(x0, self.K, T, sigma, r)) / self.K


# Hertz share counts (8-K, 7 Jul 2021), in millions
HZ_RIGHTS_PART, HZ_UNSUB, HZ_FEE = 127.362114, 36.137887, 16.35
HZ_SPONSOR, HZ_OLD3PCT, HZ_TOTAL = 277.119438, 14.133075, 471.102514
hz_m = HZ_RIGHTS_PART + HZ_UNSUB
hz_n0 = HZ_SPONSOR + HZ_OLD3PCT
assert abs(hz_m * 10.0 - 1635.0) < 1e-3                       # $1.635bn at $10
assert abs(hz_m + hz_n0 + HZ_FEE - HZ_TOTAL) < 1e-6           # rows sum exactly
assert abs(HZ_FEE / hz_m - 0.10) < 1e-6                       # 10% fee in shares
hz = RightsOffering(n0=hz_n0, m=hz_m, K=10.0)
assert 0.63 < hz.dilution < 0.65

# identities
x_test = np.array([5.0, 10.0, 15.0])
assert np.allclose(hz.post_money(x_test) - 10.0, hz.dilution * (x_test - 10.0))
assert abs(bs_call(1.0, 0.75, 0.5, 0.7) - bs_put(1.0, 0.75, 0.5, 0.7) - 0.25) < 1e-12   # parity, r=0

# worked number: 25% discount, 70% vol, six months
gen = RightsOffering(n0=hz_n0, m=hz_m, K=0.75)
assert abs(float(bs_put(1.0, 0.75, 0.5, 0.7)) / 0.75 - 0.0979) < 0.002
f_star = gen.fair_fee(1.0, 0.70, 0.5)
assert 0.058 < f_star < 0.067, f_star

# Monte Carlo check of the short put (driftless lognormal under P)
sig, T = 0.70, 0.5
Z = RNG.standard_normal(400_000)
x_T = np.exp(-0.5 * sig**2 * T + sig * np.sqrt(T) * Z)
mc = gen.backstop_payoff(x_T).mean()
cf = -gen.n_eff * float(bs_put(1.0, 0.75, T, sig))
assert abs(mc / cf - 1.0) < 0.02, (mc, cf)

# fee table: fee and discount are substitutes
fee_table = {}
for disc in (0.0, 0.25, 0.50):
    for T_ in (0.25, 0.50):
        ro = RightsOffering(n0=hz_n0, m=hz_m, K=1.0 - disc)
        fee_table[(disc, T_)] = ro.fair_fee(1.0, 0.70, T_)
assert fee_table[(0.0, 0.5)] > fee_table[(0.25, 0.5)] > fee_table[(0.5, 0.5)]
assert 0.08 < fee_table[(0.0, 0.25)] < 0.10 and 0.115 < fee_table[(0.0, 0.5)] < 0.135

# Hertz, short window: even at the money the put is worth well under 10%
assert hz.fair_fee(10.0, 0.70, 0.10) < 0.07

# Hertz ex post at the $29 re-IPO price (USD mm)
fee_value = HZ_FEE * 29.0
unsub_gain = HZ_UNSUB * (29.0 - 10.0)
assert 1150 < fee_value + unsub_gain < 1170

for (disc, T_), f in sorted(fee_table.items()):
    print(f"discount {disc:4.0%}  T={T_:.2f}y  fair fee {f:6.2%}")
print(f"Hertz ex post: fee shares ${fee_value:,.0f}mm + unsubscribed gain ${unsub_gain:,.0f}mm")
```


### Listing 16.3: Warrants with dilution and jump-to-default: the Galai-Schneller fixed point {#code-16-3}

```python
# --- Block 3: warrants with dilution and jump-to-default (reuses bs_call, brentq) ---

def warrant_price(S, K, T, sigma, r, omega, lam=0.0, tol=1e-12, max_iter=1000):
    """Galai-Schneller fixed point W = C_BS(S + omega*W, K, T, sigma, r + lam) / (1 + omega).
    lam: jump-to-zero intensity; with a MARKET spot it enters through the rate, not a haircut."""
    if omega < 0 or lam < 0:
        raise ValueError("omega and lam must be non-negative")
    r_eff = r + lam
    W = float(bs_call(S, K, T, sigma, r_eff))
    for _ in range(max_iter):
        W_new = float(bs_call(S + omega * W, K, T, sigma, r_eff)) / (1.0 + omega)
        if abs(W_new - W) < tol:
            return W_new
        W = W_new
    raise RuntimeError("warrant fixed point did not converge")


def implied_vol_warrant(W_target, S, K, T, r, omega, lam=0.0, lo=0.01, hi=3.0):
    f = lambda sig: warrant_price(S, K, T, sig, r, omega, lam) - W_target
    if f(lo) * f(hi) > 0:
        raise ValueError("target warrant price not bracketed")
    return brentq(f, lo, hi, xtol=1e-10)


HZ_WARRANTS = 89.049029           # mm (8-K, 7 Jul 2021)
HZ_W_STRIKE, HZ_W_T = 13.80, 30.0
HZ_W_PLAN = 769.0 / HZ_WARRANTS   # USD per warrant (3d Cir. opinion, fn. 5)
R_30Y = 0.02                      # assumption, stated
omega_hz = HZ_WARRANTS / HZ_TOTAL
assert 8.6 < HZ_W_PLAN < 8.7 and 0.18 < omega_hz < 0.20

# fixed point actually solves its equation, and dilution never adds value
W_fp = warrant_price(10.0, HZ_W_STRIKE, HZ_W_T, 0.5, R_30Y, omega_hz)
rhs = float(bs_call(10.0 + omega_hz * W_fp, HZ_W_STRIKE, HZ_W_T, 0.5, R_30Y)) / (1 + omega_hz)
assert abs(W_fp - rhs) < 1e-10
assert W_fp <= float(bs_call(10.0, HZ_W_STRIKE, HZ_W_T, 0.5, R_30Y)) + 1e-12

# the plan's implied volatility at the honest spot ($10) and at the warrant basis ($13.80)
iv_undil = implied_vol_warrant(HZ_W_PLAN, 10.0, HZ_W_STRIKE, HZ_W_T, R_30Y, 0.0)
iv_dil = implied_vol_warrant(HZ_W_PLAN, 10.0, HZ_W_STRIKE, HZ_W_T, R_30Y, omega_hz)
iv_jump = implied_vol_warrant(HZ_W_PLAN, 10.0, HZ_W_STRIKE, HZ_W_T, R_30Y, omega_hz, lam=0.02)
iv_basis = implied_vol_warrant(HZ_W_PLAN, HZ_W_STRIKE, HZ_W_STRIKE, HZ_W_T, R_30Y, omega_hz)
assert 0.40 < iv_undil < 0.65 and iv_dil >= iv_undil - 1e-8     # ignoring dilution understates vol
assert iv_jump < iv_dil                                          # jump risk does part of vol's job
assert iv_basis < 0.35                                           # implausibly low for this equity

# Kaz's double-counted funeral: the correct jump price exceeds the no-jump price,
# which exceeds the haircut price
w_nojump = warrant_price(10.0, HZ_W_STRIKE, HZ_W_T, iv_dil, R_30Y, omega_hz)
w_jump = warrant_price(10.0, HZ_W_STRIKE, HZ_W_T, iv_dil, R_30Y, omega_hz, lam=0.02)
w_kaz = w_nojump * np.exp(-0.02 * HZ_W_T)
assert w_jump > w_nojump > w_kaz

# re-IPO arithmetic (8 Nov 2021, $29)
intrinsic_total = HZ_WARRANTS * (29.0 - HZ_W_STRIKE)
assert 1.7 < intrinsic_total / 769.0 < 1.8
OLD_SHARES = 156.0
package = 1.53 + HZ_OLD3PCT / OLD_SHARES * 29.0 + HZ_WARRANTS / OLD_SHARES * (29.0 - HZ_W_STRIKE)
assert 12.5 < package < 13.1

print(f"plan-implied vol: {iv_undil:.1%} (no dilution), {iv_dil:.1%} (dilution), "
      f"{iv_jump:.1%} (dilution + 2% jump), {iv_basis:.1%} at the $13.80 basis")
print(f"old-share package at $29: ${package:.2f}")
```


### Listing 16.4: Claims with a random denominator: expected recovery, timing and in-kind distributions {#code-16-4}

```python
# --- Block 4: claims with a random denominator (reuses RNG, norm) ---

def expected_recovery_lognormal(mu_Y, s_Y):
    """E[min(1, e^Y)], Y ~ N(mu_Y, s_Y^2)."""
    if s_Y <= 0:
        raise ValueError("s_Y must be positive")
    return float(norm.cdf(mu_Y / s_Y) + np.exp(mu_Y + 0.5 * s_Y**2) * norm.cdf(-mu_Y / s_Y - s_Y))


def expected_recovery_fixed_value(V, m_C, s):
    """Fixed distributable value V, lognormal pool with mean m_C and log-sd s."""
    return expected_recovery_lognormal(np.log(V / m_C) + 0.5 * s**2, s)


@dataclass
class ClaimSpec:
    kind: str                  # "GUC" or "503b9"
    p_allow: float             # probability the claim is allowed (with this priority)
    hazard_exit: float         # h, per year: effective date arrives at rate h
    r: float                   # discount rate, per year
    psi: float                 # illiquidity premium, per year
    mu_Y: float = 0.0          # GUC only: mean of ln(V/C)
    s_Y: float = 0.3           # GUC only: sd of ln(V/C)
    p_admin_insolvent: float = 0.0   # 503b9 only
    lgd_admin: float = 0.0           # 503b9 only


def timing_factor(c):
    return c.hazard_exit / (c.hazard_exit + c.r + c.psi)


def price_claim(c):
    """Price per dollar of face (no coupon: 11 U.S.C. 502(b)(2)); Hertz option omitted."""
    if c.kind == "GUC":
        return c.p_allow * timing_factor(c) * expected_recovery_lognormal(c.mu_Y, c.s_Y)
    if c.kind == "503b9":
        return c.p_allow * timing_factor(c) * (1.0 - c.p_admin_insolvent * c.lgd_admin)
    raise ValueError(f"unknown claim kind {c.kind!r}")


def in_kind_recovery(R_cash, price_at_petition, price_at_distribution):
    return R_cash * price_at_petition / price_at_distribution


# closed form vs Monte Carlo
mu_t, s_t = 0.10, 0.40
Y = RNG.normal(mu_t, s_t, 1_000_000)
assert abs(np.minimum(1.0, np.exp(Y)).mean() - expected_recovery_lognormal(mu_t, s_t)) < 0.002

# Jensen near par: covered on average, yet ~8 points lost
er_par = expected_recovery_fixed_value(1.0, 1.0, 0.30)
assert abs(er_par - 0.917) < 0.002
# ...and the other side of the kink: deep impairment, variance helps
er_deep = expected_recovery_fixed_value(0.30, 1.0, 0.30)
assert er_deep > 0.30
# limit s -> 0 recovers min(1, V/m_C)
assert abs(expected_recovery_fixed_value(0.8, 1.0, 1e-6) - 0.8) < 1e-4

# the pair: same timing factor, so the log spread decomposes exactly
guc = ClaimSpec("GUC", p_allow=0.95, hazard_exit=1.5, r=0.04, psi=0.08, mu_Y=np.log(0.9), s_Y=0.35)
b9 = ClaimSpec("503b9", p_allow=0.97, hazard_exit=1.5, r=0.04, psi=0.08,
               p_admin_insolvent=0.05, lgd_admin=0.5)
p_guc, p_b9 = price_claim(guc), price_claim(b9)
spread = np.log(p_b9) - np.log(p_guc)
decomp = (np.log(b9.p_allow / guc.p_allow) + np.log(1 - b9.p_admin_insolvent * b9.lgd_admin)
          - np.log(expected_recovery_lognormal(guc.mu_Y, guc.s_Y)))
assert abs(spread - decomp) < 1e-12
assert 0.0 < p_guc < p_b9 < 1.0
# near par, more pool uncertainty widens the spread (long 503b9 / short GUC is long s_Y)
guc_wide = ClaimSpec("GUC", 0.95, 1.5, 0.04, 0.08, mu_Y=np.log(0.9), s_Y=0.60)
assert np.log(p_b9) - np.log(price_claim(guc_wide)) > spread

# denomination risk: 120% in cash, ~20% in kind (illustrative prices)
assert abs(in_kind_recovery(1.20, 17_000.0, 100_000.0) - 0.204) < 1e-9

print(f"E[R] at par with s=0.30: {er_par:.3f}; deep (V/m=0.3): {er_deep:.3f}")
print(f"GUC {p_guc:.3f}  503(b)(9) {p_b9:.3f}  log spread {spread:.3f}")
```


### Listing 16.5: The post-reorg book: simulation, Kelly size, liquidity cap and markouts {#code-16-5}

```python
# --- Block 5: the post-reorg book (reuses RNG, ForcedSellerOverhang, ovh_sched, theta_fa) ---
P_JUMP = 0.05                        # illustrative jump-to-zero probability over 200 days
S_LOG = np.sqrt(2.0 * np.log(1.4))   # lognormal with median 0 and mean +40%


def simulate_post_reorg_returns(n, p_jump=P_JUMP, s_log=S_LOG, rng=RNG):
    X = rng.normal(0.0, s_log, n)
    R = np.exp(X) - 1.0
    R[rng.random(n) < p_jump] = -1.0
    return R


def kelly_fraction(R, grid=None):
    grid = np.linspace(0.0, 0.95, 191) if grid is None else grid
    growth = np.array([np.mean(np.log1p(f * R)) for f in grid])
    return float(grid[np.argmax(growth)]), growth


def position_cap(adv_usd, participation=0.10, exit_days=20):
    return participation * adv_usd * exit_days


def size_position(capital, f_kelly, adv_usd, kelly_mult=0.5, participation=0.10, exit_days=20):
    return min(kelly_mult * f_kelly * capital, position_cap(adv_usd, participation, exit_days))


R1 = simulate_post_reorg_returns(400_000)
assert abs(R1.mean() - ((1 - P_JUMP) * 1.4 - 1.0)) < 0.02      # mean about +33%
assert np.median(R1) < 0.0                                      # the typical name loses

N_NAMES, N_BOOKS = 20, 50_000
books = simulate_post_reorg_returns(N_NAMES * N_BOOKS).reshape(N_BOOKS, N_NAMES).mean(axis=1)
assert np.median(books) > 0.15                                  # diversification moves the median

f_kelly, growth = kelly_fraction(R1)
assert 0.05 < f_kelly < 0.5                                     # g'(1/2) = -2 p_J < 0

otc_size = size_position(500e6, f_kelly, adv_usd=2e5)
assert otc_size == position_cap(2e5) == 4e5                     # liquidity binds, not Kelly

# Ines's hand history: markouts for buying at the open vs at the trough (illustrative)
def markout(model, s_entry, s_exit):
    return float(model.discount(s_exit) - model.discount(s_entry))

s_pk = ovh_sched.peak_time()
assert markout(ovh_sched, 0.0, 1 / 12) < -0.04
assert markout(ovh_sched, 0.0, s_pk) < -0.06
assert markout(ovh_sched, s_pk, 1.0) > 0.05

print(f"single name: mean {R1.mean():.1%}, median {np.median(R1):.1%}; "
      f"20-name book median {np.median(books):.1%}; Kelly {f_kelly:.2f}")
print(f"OTC position at $200k ADV: ${otc_size:,.0f}; "
      f"markout open->trough {markout(ovh_sched, 0.0, s_pk):.1%}, trough->1y {markout(ovh_sched, s_pk, 1.0):.1%}")
```


## F.17: Chapter 17: Private Credit & the Public–Private Convergence {#code-17}

Listings from `17_ch17_private_credit_public_private_convergence.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 17.1: The mark as a filter: smoothed returns and the Dimson kernel {#code-17-1}

```python
# ---- Chapter 17 reference engine (mark_gap), block 1: the mark as a filter ----
import numpy as np
import pandas as pd


def simulate_smoothed(n, theta, beta=1.0, sigma_f=0.04, sigma_e=0.02, seed=17):
    """True quarterly excess return x_t = beta*F_t + e_t; reported x_obs_t = sum_k theta_k x_{t-k}.
    Returns (F, x_true, x_obs). The first K entries of x_obs are NaN (kernel not yet full)."""
    theta = np.asarray(theta, dtype=float)
    if theta.ndim != 1 or theta.size == 0 or np.any(theta < 0) or theta.sum() <= 0:
        raise ValueError("theta must be a non-empty vector of non-negative weights")
    theta = theta / theta.sum()                      # unit sum: marks eventually catch up
    K = theta.size - 1
    rng = np.random.default_rng(seed)
    F = rng.normal(0.0, sigma_f, n)
    x_true = beta * F + rng.normal(0.0, sigma_e, n)
    x_obs = np.full(n, np.nan)
    for t in range(K, n):
        x_obs[t] = float(np.dot(theta, x_true[t - K:t + 1][::-1]))   # theta_0 multiplies today
    return F, x_true, x_obs


def glm_moments(theta):
    """Closed-form GLM identities for a unit-sum kernel."""
    th = np.asarray(theta, dtype=float)
    th = th / th.sum()
    ss = float(np.dot(th, th))
    K = th.size - 1
    rho = np.array([np.dot(th[:-j], th[j:]) / ss for j in range(1, K + 1)])
    return {"var_ratio": ss, "rho": rho, "sharpe_inflation": 1.0 / np.sqrt(ss), "beta0_ratio": float(th[0])}


def autocorr(x, j):
    """Lag-j sample autocorrelation, ignoring NaNs at the start of the series."""
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    x = x - x.mean()
    return float(np.dot(x[j:], x[:-j]) / np.dot(x, x))


def dimson_beta(x_obs, F, K):
    """Regress reported returns on current and K lagged factor returns. Returns (b_0..b_K, sum b_k)."""
    x_obs = np.asarray(x_obs, dtype=float)
    F = np.asarray(F, dtype=float)
    T = x_obs.size
    if T - K < 10 * (K + 1):
        raise ValueError("too few observations for K lags")
    rows, y = [], []
    for t in range(K, T):
        if np.isnan(x_obs[t]):
            continue
        rows.append([1.0] + [F[t - k] for k in range(K + 1)])
        y.append(x_obs[t])
    X, y = np.asarray(rows), np.asarray(y)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[1:], float(coef[1:].sum())


def kernel_from_dimson(b):
    """theta_hat_k = b_k / sum(b), clipped to [0, 1] and renormalised. Returns (theta_hat, clip_bound)."""
    b = np.asarray(b, dtype=float)
    s = b.sum()
    if abs(s) < 1e-12:
        raise ValueError("aggregate beta is ~0: the kernel is not identified")
    th = b / s
    clipped = bool(np.any(th < 0.0) or np.any(th > 1.0))
    th = np.clip(th, 0.0, 1.0)
    return th / th.sum(), clipped


def unsmooth_ar1(x_obs, theta):
    """Geltner inversion x_hat_t = (x_obs_t - theta x_obs_{t-1}) / (1 - theta)."""
    if not 0.0 <= theta < 0.9:
        raise ValueError("theta outside [0, 0.9): noise amplification too large")
    x = np.asarray(x_obs, dtype=float)
    out = np.full_like(x, np.nan)
    out[1:] = (x[1:] - theta * x[:-1]) / (1.0 - theta)
    return out


# --- sanity checks, block 1 ---
theta = (0.5, 0.3, 0.2)
mom = glm_moments(theta)
assert abs(mom["var_ratio"] - 0.38) < 1e-12
assert np.allclose(mom["rho"], [0.21 / 0.38, 0.10 / 0.38])
assert abs(mom["sharpe_inflation"] - 1.0 / np.sqrt(0.38)) < 1e-12

F, x_true, x_obs = simulate_smoothed(20_000, theta)
var_ratio = np.nanvar(x_obs) / np.var(x_true)
assert abs(var_ratio - 0.38) < 0.02, var_ratio                      # variance deflation
assert abs(autocorr(x_obs, 1) - mom["rho"][0]) < 0.03                 # mechanical momentum, lag 1
assert abs(autocorr(x_obs, 2) - mom["rho"][1]) < 0.03                 # lag 2
b0, agg0 = dimson_beta(x_obs, F, 0)
bK, aggK = dimson_beta(x_obs, F, 2)
assert abs(agg0 - 0.5) < 0.05, agg0                                   # contemporaneous beta = theta_0 * beta
assert abs(aggK - 1.0) < 0.05, aggK                                   # Dimson sum recovers beta
theta_hat, clip_bound = kernel_from_dimson(bK)
assert np.allclose(theta_hat, theta, atol=0.05) and not clip_bound

# Geltner: exact inversion of AR(1) smoothing, then noise amplification (1 + th^2) / (1 - th)^2
th1 = 0.6
x_ar = np.empty_like(x_true)
x_ar[0] = (1.0 - th1) * x_true[0]
for t in range(1, x_true.size):
    x_ar[t] = (1.0 - th1) * x_true[t] + th1 * x_ar[t - 1]
assert np.allclose(unsmooth_ar1(x_ar, th1)[1:], x_true[1:])
eta = np.random.default_rng(171).normal(0.0, 0.001, x_ar.size)
amp = np.var(unsmooth_ar1(x_ar + eta, th1)[1:] - x_true[1:]) / 0.001 ** 2
amp_theory = (1.0 + th1 ** 2) / (1.0 - th1) ** 2                     # = 8.5
assert abs(amp / amp_theory - 1.0) < 0.05, amp
print("block 1 ok: var ratio %.3f, rho1 %.3f, Dimson sum %.3f, noise amp %.1f"
      % (var_ratio, autocorr(x_obs, 1), aggK, amp))
```


### Listing 17.2: Implied markdowns from BDC price to NAV, the non-accrual mark and stale-mark flags {#code-17-2}

```python
# ---- block 2: from listed prices and disclosures to implied marks ----
def implied_markdown(p_nav, lev, fee_drag=0.0):
    """m = ((1 - phi) - P/NAV) / (1 + ell), floored at 0. NaN for a non-traded vehicle."""
    if p_nav is None or np.isnan(p_nav):
        return np.nan
    if lev < 0 or not 0.0 <= fee_drag < 1.0:
        raise ValueError("leverage must be >= 0 and fee_drag in [0, 1)")
    return max(((1.0 - fee_drag) - p_nav) / (1.0 + lev), 0.0)


def implied_nonaccrual_mark(w_fv, w_cost, fv_over_cost=1.0):
    """Carrying value of the non-accrual bucket as a fraction of its cost (a mark, not a recovery)."""
    if w_cost <= 0:
        return np.nan
    return (w_fv / w_cost) * fv_over_cost


def cross_holder_dispersion(soi):
    """Per facility held by >= 2 vehicles: number of holders, mean, std and range of fv/par."""
    df = soi.assign(px=soi["fv"] / soi["par"])
    g = df.groupby("facility_id")["px"]
    out = pd.DataFrame({"n_holders": g.size(), "px_mean": g.mean(),
                        "px_std": g.std(ddof=0), "px_range": g.max() - g.min()})
    return out[out["n_holders"] >= 2]


def stale_mark_flag(px_by_quarter, n_unchanged=5, tol=1e-4):
    """True where a facility's mark has been unchanged (within tol) for n_unchanged consecutive quarters."""
    px = np.asarray(px_by_quarter, dtype=float)
    run, flags = 1, []
    for t in range(px.size):
        run = run + 1 if (t > 0 and abs(px[t] - px[t - 1]) <= tol) else 1
        flags.append(run >= n_unchanged)
    return np.array(flags)


obdc = pd.DataFrame({
    "qdate": pd.to_datetime(["2025-09-30", "2025-12-31", "2026-03-31", "2026-06-30"]),
    "nav_ps": [14.89, 14.81, 14.41, 14.26],
    "w_na_cost": [0.027, 0.023, 0.020, 0.028],
    "w_na_fv": [0.013, 0.011, 0.010, 0.008],
    "net_de": [1.22, 1.19, 1.13, 1.11],
}).set_index("qdate")
obdc["gap_pp"] = 100.0 * (obdc["w_na_cost"] - obdc["w_na_fv"])
obdc["na_mark"] = [implied_nonaccrual_mark(f, c, 0.98) for f, c in zip(obdc["w_na_fv"], obdc["w_na_cost"])]

# --- sanity checks, block 2 ---
assert abs(implied_markdown(0.86, 1.19, 0.05) - 0.0411) < 1e-3      # OBDC Q4 2025 buyback print
assert abs(implied_markdown(0.50, 1.10, 0.05) - 0.2143) < 1e-3      # a name near a 50% discount
assert implied_markdown(1.02, 1.0, 0.05) == 0.0                      # premium name: floor, not negative
assert np.isnan(implied_markdown(np.nan, 0.9))                       # non-traded: undefined, never 1.0
assert np.isnan(implied_nonaccrual_mark(0.0, 0.0))
assert abs(obdc["na_mark"].iloc[-1] - 0.28) < 0.005                  # ~28c on the bad bucket, Jun 2026
assert abs(obdc["gap_pp"].iloc[1] - 1.2) < 1e-9 and abs(obdc["gap_pp"].iloc[-1] - 2.0) < 1e-9

soi_toy = pd.DataFrame({                                             # illustrative holdings
    "facility_id": ["A", "A", "A", "B", "B", "C"],
    "bdc_id": ["X", "Y", "Z", "X", "Y", "Z"],
    "par": [10.0, 25.0, 5.0, 8.0, 12.0, 3.0],
    "fv": [9.8, 14.5, 4.6, 7.92, 11.88, 2.9],
})
disp = cross_holder_dispersion(soi_toy)
assert list(disp.index) == ["A", "B"]                                # C has a single holder
assert abs(disp.loc["A", "px_range"] - 0.40) < 1e-9                  # a 40-point same-loan gap
assert disp.loc["B", "px_range"] < 1e-9
assert stale_mark_flag([0.97, 0.97, 0.97, 0.97, 0.97, 0.95]).tolist() == [False] * 4 + [True, False]
print(obdc[["gap_pp", "na_mark"]].round(3))
```


### Listing 17.3: Private-credit to broadly syndicated loan migration as competing risks {#code-17-3}

```python
# ---- block 3: PC <-> BSL migration as competing risks ----
EXITS = ("to_bsl", "to_pc", "amend_extend", "default")


def cause_specific_hazards(base, psi, chi, omega, zeta, ds, V):
    """Annualised hazards kappa_ij = base_j * exp(psi_j*zeta + chi_j*ds + V_i @ omega_j).
    base, psi, chi: (J,); omega: (p, J); V: (n, p); zeta and ds are scalars. Returns (n, J)."""
    base, psi, chi = (np.asarray(a, dtype=float) for a in (base, psi, chi))
    V = np.atleast_2d(np.asarray(V, dtype=float))
    omega = np.asarray(omega, dtype=float)
    if np.any(base < 0):
        raise ValueError("baseline hazards must be non-negative")
    lin = zeta * psi + ds * chi + V @ omega
    return base * np.exp(np.clip(lin, -30.0, 30.0))          # clip guards exp overflow


def exit_probabilities(kappa, dt=0.25):
    """Constant competing hazards over dt years: P(exit via j) = kappa_j / K * (1 - exp(-K dt)).
    Returns (n, J + 1): exit probabilities by cause, then P(still outstanding)."""
    kappa = np.atleast_2d(np.asarray(kappa, dtype=float))
    if np.any(kappa < 0):
        raise ValueError("hazards must be non-negative")
    tot = kappa.sum(axis=1, keepdims=True)
    p_any = 1.0 - np.exp(-tot * dt)
    with np.errstate(invalid="ignore", divide="ignore"):
        share = np.where(tot > 0, kappa / tot, 0.0)
    return np.hstack([share * p_any, 1.0 - p_any])


def bsl_supply(face, kappa, dt=0.25, naive=False):
    """Expected face refinanced from private credit into the BSL market over the next dt years."""
    face = np.asarray(face, dtype=float)
    kappa = np.atleast_2d(np.asarray(kappa, dtype=float))
    if naive:                                                  # ignores competing exits: overstates
        return float(face @ (1.0 - np.exp(-kappa[:, 0] * dt)))
    return float(face @ exit_probabilities(kappa, dt)[:, 0])


# --- sanity checks, block 3 (all parameters illustrative) ---
rng3 = np.random.default_rng(2023)
n_loans = 400
V = np.column_stack([rng3.normal(0.0, 0.5, n_loans),                  # log size vs median borrower
                     (rng3.random(n_loans) < 0.21).astype(float)])     # software flag
face = 150.0 * np.exp(V[:, 0])                                         # $mm
base = np.array([0.12, 0.08, 0.06, 0.02])
psi = np.array([-0.8, 0.3, 0.4, 0.2])          # tight-LL regime (zeta = +1) slows takeouts into BSL
chi = np.array([0.5, -0.2, 0.0, 0.0])          # wider PC-minus-BSL spread (pp) pulls loans into BSL
omega = np.array([[0.6, -0.2, 0.0, 0.0],       # size: bigger borrowers can reach the BSL market
                  [-0.3, 0.1, 0.3, 0.4]])      # software: harder to syndicate, more A&E, more default
kap_loose = cause_specific_hazards(base, psi, chi, omega, zeta=-1.0, ds=1.0, V=V)
kap_tight = cause_specific_hazards(base, psi, chi, omega, zeta=+1.0, ds=1.0, V=V)
probs = exit_probabilities(kap_loose)
assert probs.shape == (n_loans, 5) and np.allclose(probs.sum(axis=1), 1.0)
assert abs(exit_probabilities([[0.2, 0.0, 0.0, 0.0]])[0, 0] - (1.0 - np.exp(-0.05))) < 1e-12
assert np.allclose(exit_probabilities([[0.0, 0.0, 0.0, 0.0]]), [[0.0, 0.0, 0.0, 0.0, 1.0]])
s_loose, s_tight = bsl_supply(face, kap_loose), bsl_supply(face, kap_tight)
assert s_tight < s_loose                                               # the regime turns the tap
assert bsl_supply(face, kap_loose, naive=True) >= s_loose              # ignoring competition overstates
print("expected PC->BSL supply next quarter ($mm, illustrative): loose %.0f, tight %.0f" % (s_loose, s_tight))
```


### Listing 17.4: The redemption game and the liquidity runway {#code-17-4}

```python
# ---- block 4: the redemption game and the liquidity runway ----
def redemption_fill(a, cap=0.05):
    """Pro-rata fill fraction f = min(1, cap / a)."""
    return 1.0 if a <= 0 else min(1.0, cap / a)


def stayer_value(nav, m, a, cap=0.05):
    """True value per remaining share after pro-rata redemptions paid at smoothed NAV."""
    paid = redemption_fill(a, cap) * a
    return nav * ((1.0 - m) - paid) / (1.0 - paid)


def queue_path(new_requests, cap=0.05):
    """New requests arrive as fractions of non-queued shares; unfilled requests stay queued.
    Shares start at 1. Returns one row per quarter."""
    S, backlog, rows = 1.0, 0.0, []
    for a_new in new_requests:
        if not 0.0 <= a_new <= 1.0:
            raise ValueError("request fractions must lie in [0, 1]")
        new = a_new * (S - backlog)
        demand = backlog + new
        paid = min(demand, cap * S)
        rows.append({"shares": S, "new": new, "demand": demand, "paid": paid,
                     "fill": paid / demand if demand > 0 else 1.0, "backlog_end": demand - paid})
        backlog = demand - paid
        S -= paid
    return pd.DataFrame(rows)


def runway_quarters(cash, undrawn, sleeve, haircut, nav, cap, unfunded, maturities, repayments=0.0):
    """Quarters of capped redemptions the vehicle can fund; all flows per quarter, as fractions of NAV."""
    if not 0.0 <= haircut <= 1.0:
        raise ValueError("haircut must lie in [0, 1]")
    outflow = cap * nav + unfunded + maturities - repayments
    return np.inf if outflow <= 0 else (cash + undrawn + sleeve * (1.0 - haircut)) / outflow


# --- sanity checks, block 4 ---
assert abs(redemption_fill(0.168) - 0.05 / 0.168) < 1e-12                 # ~30% fill at 16.8% requests
sv = stayer_value(1.0, 0.05, 0.168)
assert sv < 0.95 and abs(sv - 0.9474) < 1e-3                              # stayers lose vs N(1 - m)
assert abs(stayer_value(1.0, 0.0, 0.3) - 1.0) < 1e-12                     # honest marks: no transfer
paid = redemption_fill(0.168) * 0.168
assert abs((1.0 - paid) * (0.95 - sv) - paid * 0.05) < 1e-12              # stayers' loss = p * m
assert redemption_fill(0.168) * (1.0 - sv) > 0                            # requesting strictly dominates
path = queue_path([0.168, 0.10, 0.10, 0.10])
assert (path["paid"] <= 0.05 * path["shares"] + 1e-12).all()
assert abs(path["new"].sum() - path["paid"].sum() - path["backlog_end"].iloc[-1]) < 1e-12
assert path["fill"].is_monotonic_decreasing                               # fills fall with steady requests
T0 = runway_quarters(0.002, 0.10, 0.10, 0.10, 1.0, 0.05, 0.02, 0.0)
T1 = runway_quarters(0.002, 0.10, 0.10, 0.10, 1.0, 0.05, 0.02, 0.0, repayments=0.03)
assert abs(T0 - 2.743) < 0.01 and abs(T1 - 4.8) < 0.01                    # repayments buy two quarters
assert runway_quarters(0.0, 0.1, 0.0, 0.0, 1.0, 0.05, 0.0, 0.0, repayments=0.06) == np.inf
print(path.round(4))
print("runway (quarters): no repayments %.2f, with 3%%/qtr repayments %.2f" % (T0, T1))
```


### Listing 17.5: The mark-gap signal: what public factor returns already imply about the next marks {#code-17-5}

```python
# ---- block 5: what the public data already knows about the next marks ----
def pending_mark(theta, beta, F_recent):
    """Expected sum of all future reported returns already implied by public factor returns.
    F_recent = [F_t, F_{t-1}, ..., F_{t-K+1}] (newest first). Returns beta * sum_j Theta_{j+1} F_{t-j}."""
    th = np.asarray(theta, dtype=float)
    th = th / th.sum()
    K = th.size - 1
    tail = np.array([th[j + 1:].sum() for j in range(K)])           # Theta_{j+1} = sum_{k > j} theta_k
    F_recent = np.asarray(F_recent, dtype=float)
    if F_recent.size != K:
        raise ValueError("need exactly K recent factor returns, newest first")
    return float(beta * np.dot(tail, F_recent))


def mark_gap_signal(p_nav, lev, fee_drag, theta, beta, F_recent):
    """G = price-implied markdown minus the markdown the public data says is still coming."""
    m_hat = implied_markdown(p_nav, lev, fee_drag)
    return m_hat - max(-pending_mark(theta, beta, F_recent), 0.0)


# --- sanity checks, block 5 ---
th = np.array([0.5, 0.3, 0.2])
assert abs(pending_mark(th, 1.0, [-0.04, 0.0]) + 0.02) < 1e-12          # 2% of markdowns still to come
shock = np.zeros(8)
shock[3] = -0.04                                                         # one bad quarter at t = 3
reported = np.array([sum(th[k] * shock[t - k] for k in range(3) if t - k >= 0) for t in range(8)])
assert abs(reported[4:].sum() - pending_mark(th, 1.0, [shock[3], shock[2]])) < 1e-12
G = mark_gap_signal(0.86, 1.19, 0.05, th, 1.0, [-0.04, 0.0])
assert abs(G - (0.0411 - 0.02)) < 1e-3                                   # price discounts ~2% beyond catch-up
print("pending mark %.4f, mark-gap signal %.4f" % (pending_mark(th, 1.0, [-0.04, 0.0]), G))
print("mark_gap: all sanity checks passed")
```


## F.18: Chapter 18: OTC Credit Microstructure & the Market Maker's Equations {#code-18}

Listings from `18_ch18_otc_microstructure_and_avellaneda_stoikov.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 18.1: Roll (1984) effective spread, with a simulator that has order splitting {#code-18-1}

```python
import numpy as np
import pandas as pd
from scipy import stats, integrate, signal

RNG = np.random.default_rng(18)

def roll_spread(prices, min_obs=20):
    """Roll (1984) effective spread from consecutive trade prices (points per 100 par).
    Returns (spread_points, autocov). spread is NaN when autocov >= 0 (Roll undefined)."""
    p = np.asarray(prices, dtype=float)
    p = p[np.isfinite(p)]
    if p.size < min_obs + 2:
        return np.nan, np.nan
    dp = np.diff(p)
    c = np.cov(dp[1:], dp[:-1], ddof=1)[0, 1]
    if c >= 0.0:
        return np.nan, c          # momentum or splitting dominates: never take abs()
    return 2.0 * np.sqrt(-c), c

def simulate_roll(n, spread, sigma_mid, rho=0.0, phi_mid=0.0, rng=RNG):
    """p_t = m_t + (spread/2) I_t. I_t: symmetric +/-1 Markov chain with lag-1 autocorr rho.
    Mid increments: AR(1) with coefficient phi_mid (phi_mid > 0 mimics informed drift)."""
    stay = 0.5 * (1.0 + rho)
    flips = rng.random(n) >= stay
    flips[0] = False
    I = rng.choice([-1.0, 1.0]) * np.where(np.cumsum(flips) % 2 == 0, 1.0, -1.0)
    eps = rng.normal(0.0, sigma_mid, n)
    dm = signal.lfilter([1.0], [1.0, -phi_mid], eps)
    m = 90.0 + np.cumsum(dm)
    return m + 0.5 * spread * I

# Sanity 1: Roll recovers the spread when signs are i.i.d.
s_hat, _ = roll_spread(simulate_roll(200_000, spread=0.50, sigma_mid=0.05))
assert abs(s_hat - 0.50) < 0.02, s_hat
# Sanity 2: order splitting shrinks the estimate to S(1 - rho)
s_split, _ = roll_spread(simulate_roll(200_000, spread=0.50, sigma_mid=0.05, rho=0.6))
assert abs(s_split - 0.50 * 0.4) < 0.02, s_split
# Sanity 3: informed drift turns the covariance positive -> NaN, not a fake spread
s_mom, c_mom = roll_spread(simulate_roll(50_000, spread=0.10, sigma_mid=0.10, rho=0.6, phi_mid=0.4))
assert np.isnan(s_mom) and c_mom > 0, (s_mom, c_mom)
gamma_bpw = lambda prices: -roll_spread(prices)[1]   # Bao-Pan-Wang illiquidity, points^2
```


### Listing 18.2: The one-period Kyle (1985) equilibrium and its lambda estimator {#code-18-2}

```python
def kyle_equilibrium(sigma_v, sigma_u):
    """One-period Kyle (1985). Returns (lambda_K, beta).
    lambda_K is in points per unit of flow; beta in flow units per point."""
    if sigma_v <= 0 or sigma_u <= 0:
        raise ValueError("volatilities must be positive")
    return 0.5 * sigma_v / sigma_u, sigma_u / sigma_v

def estimate_kyle_lambda(markout, signed_flow):
    """OLS slope of markout (points) on signed flow, with intercept. Returns (slope, t_stat)."""
    yv = np.asarray(markout, float)
    xv = np.asarray(signed_flow, float)
    X = np.column_stack([np.ones_like(xv), xv])
    coef, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ coef
    s2 = resid @ resid / (len(yv) - 2)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    return coef[1], coef[1] / se

sig_v, sig_u, n_k, p0 = 2.0, 5.0, 100_000, 90.0     # value std (points), noise std (USD mm)
lam_K, beta_K = kyle_equilibrium(sig_v, sig_u)       # 0.2 points per USD mm
v_k = p0 + RNG.normal(0.0, sig_v, n_k)
u_k = RNG.normal(0.0, sig_u, n_k)
x_k = beta_K * (v_k - p0)
y_k = x_k + u_k
p_k = p0 + lam_K * y_k
slope_total, _ = estimate_kyle_lambda(v_k - p0, y_k)
slope_post, t_post = estimate_kyle_lambda(v_k - p_k, y_k)
assert abs(slope_total / lam_K - 1.0) < 0.03          # information content = lambda_K
assert abs(t_post) < 4.0                              # efficient pricing: no post-trade drift
assert abs(np.mean(x_k * (v_k - p_k)) / (0.5 * sig_v * sig_u) - 1.0) < 0.03
assert abs(np.var(v_k - p_k) / (0.5 * sig_v**2) - 1.0) < 0.03   # half the information revealed
```


### Listing 18.3: Avellaneda-Stoikov quotes: fear plus greed {#code-18-3}

```python
from scipy.optimize import minimize_scalar

def as_greed(gamma, k):
    """Per-side markup (1/gamma) ln(1 + gamma/k), in points. Tends to 1/k as gamma -> 0."""
    if k <= 0:
        raise ValueError("k must be positive (per point)")
    if gamma < 1e-12:
        return 1.0 / k
    return np.log1p(gamma / k) / gamma

def as_quotes(s, q, sigma, gamma, k, tau):
    """Avellaneda-Stoikov (2008) approximate quotes. s points; q lots; sigma points/sqrt(yr);
    gamma per point-lot; k per point; tau years. Returns prices and the fear/greed split."""
    if sigma < 0 or gamma < 0 or tau < 0:
        raise ValueError("sigma, gamma, tau must be non-negative")
    fear = gamma * sigma**2 * tau                     # full-spread inventory term, points
    g = as_greed(gamma, k)
    r_res = s - q * fear                              # (18.1)
    return {"r_res": r_res, "bid": r_res - 0.5 * fear - g, "ask": r_res + 0.5 * fear + g,
            "spread": fear + 2.0 * g, "fear": fear, "greed": 2.0 * g}

to_eighth = lambda px: np.round(np.asarray(px, float) * 8.0) / 8.0

tau_hold = 5.0 / 252.0
qa = as_quotes(s=91.25, q=3, sigma=8.0, gamma=0.005, k=3.0, tau=tau_hold)
assert abs(qa["bid"] - 90.8947) < 1e-3 and to_eighth(qa["bid"]) == 90.875     # Kaz's quote
assert abs(qa["spread"] - (qa["fear"] + qa["greed"])) < 1e-12                  # (18.4)
assert qa["greed"] / qa["spread"] > 0.9                                         # mostly greed
assert abs(as_greed(1e-9, 3.0) - 1.0 / 3.0) < 1e-9                              # gamma -> 0
assert as_quotes(91.25, 3, 8.0, 0.005, 3.0, 0.0)["r_res"] == 91.25             # t -> T

# General FOC (18.2), checked by brute force for the exponential intensity
A_, k_, g_, Delta = 50.0, 3.0, 0.005, 0.0222
obj = lambda d: -A_ * np.exp(-k_ * d) * (-np.expm1(-g_ * (d - Delta))) / g_
d_star = minimize_scalar(obj, bounds=(Delta, Delta + 5.0), method="bounded",
                         options={"xatol": 1e-10}).x
assert abs(d_star - (Delta + as_greed(g_, k_))) < 1e-6

# ROBO's unit error: spread vol in bp (200) fed as price vol in points
assert as_quotes(91.25, 3, 200.0, 0.005, 3.0, tau_hold)["bid"] < 78.0
```


### Listing 18.4: Jump-to-default reservation prices and the streaming inventory quotes {#code-18-4}

```python
def jtd_reservation(s, q, n, sigma, gamma, tau, lam_P, J, lam_Q=0.0):
    """Frozen-inventory reservation (bid, ask) for buying/selling a block of n lots.
    Mid: dS = lam_Q*J dt + sigma dW - J dN, N with P-intensity lam_P. Points, lots, consistent time."""
    if n < 1 or gamma < 0 or tau < 0:
        raise ValueError("need n >= 1, gamma >= 0, tau >= 0")
    def theta(qq):
        base = qq * (s + lam_Q * J * tau) - 0.5 * gamma * qq**2 * sigma**2 * tau
        if gamma < 1e-12:
            return base - lam_P * tau * qq * J
        return base - (lam_P * tau / gamma) * np.expm1(gamma * qq * J)
    return (theta(q + n) - theta(q)) / n, (theta(q) - theta(q - n)) / n

def jump_mgf_beta(u, s, a, b, scale=100.0):
    """E[exp(u J)] for J = s - scale*R, R ~ Beta(a, b), by adaptive quadrature."""
    f = lambda r: np.exp(u * (s - scale * r)) * stats.beta.pdf(r, a, b)
    return integrate.quad(f, 0.0, 1.0, limit=200)[0]

def glft_matrix(sigma, gamma, k, A, Q, lam=0.0, J=0.0, mu=0.0):
    """Symmetric tridiagonal M of (18.8) on q = -Q..Q. Consistent units (e.g. per day)."""
    if gamma <= 0 or k <= 0 or A <= 0 or Q < 1:
        raise ValueError("need gamma, k, A > 0 and Q >= 1")
    q = np.arange(-Q, Q + 1, dtype=float)
    eta = A * (1.0 + gamma / k) ** (-(1.0 + k / gamma))
    diag = 0.5 * k * gamma * sigma**2 * q**2 - k * mu * q
    if lam > 0.0:
        diag = diag + (k * lam / gamma) * np.expm1(gamma * q * J)
    M = np.diag(diag) - eta * (np.eye(q.size, k=1) + np.eye(q.size, k=-1))
    return q, M

def _quotes_from_logv(q, logv, gamma, k):
    g = as_greed(gamma, k)
    db, da = np.full(q.size, np.nan), np.full(q.size, np.nan)
    db[:-1] = (logv[:-1] - logv[1:]) / k + g          # no bid at q = +Q
    da[1:] = (logv[1:] - logv[:-1]) / k + g           # no ask at q = -Q
    return pd.DataFrame({"q": q.astype(int), "delta_bid": db, "delta_ask": da}).set_index("q")

def _safe_log(v):
    ok = v > 1e-12 * np.max(v)
    return np.where(ok, np.log(np.where(ok, v, 1.0)), np.nan)

def glft_quotes(sigma, gamma, k, A, tau, Q, lam=0.0, J=0.0, mu=0.0):
    q, M = glft_matrix(sigma, gamma, k, A, Q, lam, J, mu)
    w, P = np.linalg.eigh(M)
    v = P @ (np.exp(-(w - w.min()) * tau) * (P.T @ np.ones(q.size)))   # e^{-M tau} 1, rescaled
    return _quotes_from_logv(q, _safe_log(v), gamma, k)

def glft_stationary(sigma, gamma, k, A, Q, lam=0.0, J=0.0, mu=0.0):
    q, M = glft_matrix(sigma, gamma, k, A, Q, lam, J, mu)
    f0 = np.abs(np.linalg.eigh(M)[1][:, 0])          # Perron ground state
    return _quotes_from_logv(q, _safe_log(f0), gamma, k)

def glft_omega(sigma, gamma, k, A):
    """Closed-form stationary skew per lot, (18.6)."""
    return np.sqrt(sigma**2 * gamma / (2.0 * k * A) * (1.0 + gamma / k) ** (1.0 + k / gamma))

sig_d, gam, kk, A_d, Qmax = 8.0 / np.sqrt(252.0), 0.005, 3.0, 2.0, 20     # per trading day
g0 = as_greed(gam, kk)
short = glft_quotes(sig_d, gam, kk, A_d, tau=0.01, Q=Qmax)
for qq in range(-3, 4):                                                     # GLFT -> AS
    as_part = (qq + 0.5) * gam * sig_d**2 * 0.01
    assert abs((short.loc[qq, "delta_bid"] - g0) / as_part - 1.0) < 0.02
stat = glft_stationary(sig_d, gam, kk, A_d, Q=Qmax)
long_run = glft_quotes(sig_d, gam, kk, A_d, tau=3000.0, Q=Qmax)
assert np.allclose(long_run.loc[-5:5, "delta_bid"], stat.loc[-5:5, "delta_bid"], atol=1e-8)
omega = glft_omega(sig_d, gam, kk, A_d)
assert 0.9 < (stat.loc[0, "delta_bid"] - g0) / (0.5 * omega) < 1.15        # (18.6)
assert np.allclose(stat.loc[-5:5, "delta_bid"].values,
                   stat.loc[-5:5, "delta_ask"].values[::-1], atol=1e-9)    # symmetry
tau_eff_days = omega / (gam * sig_d**2)                                     # about 13 days
assert 10.0 < tau_eff_days < 17.0

lamP_d, lamQ_d, J_lmt = 0.005, 0.004, 20.0          # per day: 2.5% vs 2.0% per week of a 20-pt gap
jtd = glft_stationary(sig_d, gam, kk, A_d, Q=Qmax, lam=lamP_d, J=J_lmt, mu=lamQ_d * J_lmt)
assert jtd.loc[0, "delta_bid"] > stat.loc[0, "delta_bid"]          # less eager to buy
assert jtd.loc[0, "delta_ask"] < stat.loc[0, "delta_ask"]          # more eager to sell

rb_blk, _ = jtd_reservation(91.25, 3, 8, 8.0, 0.005, tau_hold, 0.025 / tau_hold, 20.0, 0.02 / tau_hold)
assert abs(rb_blk - 90.5716) < 1e-3                                 # used in Section 18.7
g_s = 1e-4                                                           # small-gamma expansion
rb1, _ = jtd_reservation(91.25, 3, 1, 8.0, g_s, tau_hold, 0.025 / tau_hold, 20.0)
assert abs(rb1 - (91.25 - 0.5 - 3.5 * g_s * (64.0 * tau_hold + 0.025 * 400.0))) < 1e-3
r_res = lambda qq: np.mean(jtd_reservation(91.25, qq, 1, 8.0, 0.005, tau_hold, 0.025 / tau_hold, 20.0))
assert (91.25 - r_res(5)) > (r_res(-5) - 91.25)                    # long fears more than short wants
M_quad = jump_mgf_beta(0.015, 91.25, 40.0, 60.0)
M_mc = np.mean(np.exp(0.015 * (91.25 - 100.0 * RNG.beta(40.0, 60.0, 400_000))))
assert abs(M_quad / M_mc - 1.0) < 2e-3
assert M_quad > np.exp(0.015 * (91.25 - 40.0))                      # Jensen: uncertainty costs
```


### Listing 18.5: The RFQ win curve, mark-up and the market maker's bid {#code-18-5}

```python
from scipy.optimize import minimize, brentq

def win_prob(x, b0, b1):
    """Logistic RFQ win probability; x = composite - bid (points); b1 > 0 per point."""
    return 1.0 / (1.0 + np.exp(-(b0 - b1 * np.asarray(x, float))))

def fit_win_curve(x, won):
    """MLE of (b0, b1) from an RFQ log of distances x (points) and outcomes won in {0, 1}."""
    x, won = np.asarray(x, float), np.asarray(won, float)
    nll = lambda b: np.sum(np.logaddexp(0.0, b[0] - b[1] * x) - won * (b[0] - b[1] * x))
    return minimize(nll, x0=np.array([0.0, 1.0]), method="BFGS").x

def markup(gn, b1, P):
    """(1/gn) ln(1 + gn / (b1 (1 - P))): equation (18.2) for a logistic curve and a block."""
    base = 1.0 / (b1 * (1.0 - P))
    return base if gn < 1e-12 else np.log1p(gn * base) / gn

def optimal_distance(d, nu, b0, b1, gn=0.0, iters=80):
    """Vectorized bisection for x = d - nu + markup(x); F(x) is increasing in x."""
    d, nu = np.broadcast_arrays(np.asarray(d, float), np.asarray(nu, float))
    lo, hi = d - nu, d - nu + 20.0 / b1
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        neg = mid - d + nu - markup(gn, b1, win_prob(mid, b0, b1)) < 0.0
        lo, hi = np.where(neg, mid, lo), np.where(neg, hi, mid)
    return 0.5 * (lo + hi)

def rfq_bid(s, q, n, sigma, gamma, tau, lam_P, lam_Q, J, a_tox, nu, b0, b1, tick=0.125):
    """Market maker's equation (18.9) for a client-sell RFQ of n lots; returns the five terms."""
    r_b, _ = jtd_reservation(s, q, n, sigma, gamma, tau, lam_P, J, lam_Q)
    view = (lam_P - lam_Q) * J * tau
    d = (s - r_b) + a_tox
    x = float(optimal_distance(d, nu, b0, b1, gamma * n))
    out = {"credit_view": view, "fear": (s - r_b) - view, "suspicion": a_tox,
           "greed": x - d + nu, "franchise": -nu, "bid": s - x, "p_win": float(win_prob(x, b0, b1))}
    out["bid_tick"] = float(np.round(out["bid"] / tick) * tick)
    return out

# Win-curve fit recovers known parameters
xs = RNG.uniform(-0.2, 1.5, 20_000)
b_hat = fit_win_curve(xs, RNG.random(xs.size) < win_prob(xs, 0.3, 4.0))
assert abs(b_hat[0] - 0.3) < 0.15 and abs(b_hat[1] - 4.0) < 0.2
# The cold open, solved
co = rfq_bid(91.25, 3, 8, 8.0, 0.005, tau_hold, 0.025 / tau_hold, 0.02 / tau_hold, 20.0,
             a_tox=0.15, nu=0.05, b0=0.0, b1=4.0)
terms = co["credit_view"] + co["fear"] + co["suspicion"] + co["greed"] + co["franchise"]
assert abs((91.25 - co["bid"]) - terms) < 1e-9
assert abs(co["bid"] - 90.219) < 0.005 and co["bid_tick"] == 90.25 and co["p_win"] < 0.03
# Raw vs quality-adjusted hit-ratio targeting (Niang 2026, in miniature)
tox = RNG.random(4_000) < 0.3
d_all = RNG.normal(0.35, 0.10, tox.size) + np.where(tox, 0.40, 0.05)
hit = lambda nu: win_prob(optimal_distance(d_all, nu, 0.0, 4.0), 0.0, 4.0).mean()
nu_raw = brentq(lambda nu: hit(nu) - 0.25, 0.0, 3.0)
x_raw = optimal_distance(d_all, nu_raw, 0.0, 4.0)
x_q = optimal_distance(d_all, np.where(tox, 0.0, nu_raw), 0.0, 4.0)
pw_raw, pw_q = win_prob(x_raw, 0.0, 4.0), win_prob(x_q, 0.0, 4.0)
pnl = lambda x, pw: np.sum(pw * (x - d_all))
assert abs(pw_raw.mean() - 0.25) < 1e-6 and np.allclose(pw_raw[~tox], pw_q[~tox])
assert pnl(x_q, pw_q) > pnl(x_raw, pw_raw)                          # stop subsidizing toxic flow
assert pw_q[tox].sum() / pw_q.sum() < pw_raw[tox].sum() / pw_raw.sum()
```


### Listing 18.6: A synthetic TRACE tape: cleaning and features {#code-18-6}

```python
CAP_MM = {"IG": 5.0, "HY": 1.0}            # dissemination caps, USD mm par (RN 25-17)

def make_synthetic_trace(n_trades=400, n_bad=20, rng=RNG):
    """Synthetic TRACE-like reports; bond ids are placeholders, not CUSIPs."""
    ids = np.array([f"BOND_{c}" for c in "ABCDEFGH"])
    tr = pd.DataFrame({"trade_id": np.arange(n_trades), "bond_id": rng.choice(ids, n_trades),
                       "minute": np.sort(rng.integers(0, 390, n_trades)),
                       "price": np.round(rng.normal(95.0, 3.0, n_trades), 3),
                       "qty_mm": np.round(np.exp(rng.normal(0.0, 1.2, n_trades)), 3),
                       "contra": rng.choice(["C", "D"], n_trades, p=[0.7, 0.3]),
                       "cust_buys": rng.random(n_trades) < 0.5,
                       "ats": rng.random(n_trades) < 0.15, "pt": rng.random(n_trades) < 0.10})
    tr["rating_class"] = tr.bond_id.map(dict(zip(ids, ["IG"] * 4 + ["HY"] * 4)))
    rows = []
    for t in tr.itertuples(index=False):
        sides = ["S", "B"] if t.contra == "D" else (["S"] if t.cust_buys else ["B"])
        rows += [{**t._asdict(), "side": sd, "status": "T", "orig_msg_seq": -1} for sd in sides]
    rep = pd.DataFrame(rows)
    rep["reported_qty"] = np.minimum(rep.qty_mm, rep.rating_class.map(CAP_MM))
    rep["msg_seq"] = np.arange(len(rep))
    pick = rng.choice(len(rep), 2 * n_bad, replace=False)
    m = len(rep)
    dup = rep.iloc[pick[:n_bad]].copy()
    dup["msg_seq"] = m + np.arange(n_bad)                                     # erroneous duplicates
    cxl = dup.assign(status="X", orig_msg_seq=dup.msg_seq.values, msg_seq=m + n_bad + np.arange(n_bad))
    fix = rep.iloc[pick[n_bad:]].copy()
    fix = fix.assign(status="C", orig_msg_seq=fix.msg_seq.values, msg_seq=m + 2 * n_bad + np.arange(n_bad))
    rep.loc[rep.index[pick[n_bad:]], "price"] += 1.0                          # originals mispriced
    return tr, pd.concat([rep, dup, cxl, fix], ignore_index=True)

def clean_trace(rep):
    """Apply cancels/corrections, keep the sell-side leg of interdealer trades, flag caps."""
    gone = set(rep.loc[rep.status.isin(["X", "C"]), "orig_msg_seq"])
    r = rep[(rep.status != "X") & ~rep.msg_seq.isin(gone)]
    r = r[~((r.contra == "D") & (r.side == "B"))]
    r = r.assign(capped=r.reported_qty >= r.rating_class.map(CAP_MM) - 1e-9)
    return r.sort_values(["bond_id", "minute", "msg_seq"]).reset_index(drop=True)

def trace_features(clean):
    cust = clean.contra == "C"
    c = clean.assign(cust_buy=np.where(cust & (clean.side == "S"), clean.reported_qty, 0.0),
                     cust_sell=np.where(cust & (clean.side == "B"), clean.reported_qty, 0.0))
    g = c.groupby("bond_id")
    tot = (g.cust_buy.sum() + g.cust_sell.sum()).replace(0.0, np.nan)
    return pd.DataFrame({"n_prints": g.size(), "cust_imbalance": (g.cust_buy.sum() - g.cust_sell.sum()) / tot,
                         "capped_share": g.capped.mean(), "pt_share": g.pt.mean(),
                         "ats_share": g.ats.mean(), "minutes_since_print": 390 - g.minute.max()})

true_tr, raw = make_synthetic_trace()
clean = clean_trace(raw)
assert len(clean) == len(true_tr) and clean.trade_id.is_unique          # one row per true trade
chk = clean.merge(true_tr[["trade_id", "price"]], on="trade_id", suffixes=("", "_true"))
assert np.allclose(chk.price, chk.price_true)                             # corrections applied
assert (clean.reported_qty <= clean.rating_class.map(CAP_MM) + 1e-12).all()
assert trace_features(clean).cust_imbalance.dropna().between(-1.0, 1.0).all()
```


### Listing 18.7: The expected maximum of n normals, and BWIC leakage {#code-18-7}

```python
def expected_max_std_normal(n):
    """e_n = E[max of n iid N(0,1)] by quadrature."""
    return integrate.quad(lambda z: z * n * stats.norm.pdf(z) * stats.norm.cdf(z) ** (n - 1), -12.0, 12.0)[0]

def bwic_leakage(list_mm, p_trade, phi, lam_K_per_100mm):
    """Pre-auction drift (points) and seller cost (USD mm) from order anticipation."""
    drift = lam_K_per_100mm * phi * p_trade * list_mm / 100.0
    return drift, drift * list_mm / 100.0

e_n = {n: expected_max_std_normal(n) for n in (3, 5, 8)}
assert abs(e_n[3] - 3.0 / (2.0 * np.sqrt(np.pi))) < 1e-6                 # closed form for n = 3
assert abs(e_n[8] - RNG.standard_normal((200_000, 8)).max(axis=1).mean()) < 0.01
assert e_n[8] > e_n[5] > e_n[3]                                           # curse grows with n
drift, cost = bwic_leakage(300.0, 0.9, 0.3, 0.5)
assert abs(drift - 0.405) < 1e-12 and abs(cost - 1.215) < 1e-12
```


## F.19: Chapter 19: Portfolio Trading & Basket Pricing Engines {#code-19}

Listings from `19_ch19_portfolio_trading_pricing_engines.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 19.1: The basket inquiry as a struct of arrays {#code-19-1}

```python
import time
import numpy as np
from dataclasses import dataclass, replace

RNG = np.random.default_rng(19)
N_SECTORS = 8

@dataclass
class Basket:
    """Struct-of-arrays PT inquiry. All arrays shape (N,). Units in comments."""
    ids: np.ndarray           # synthetic line ids (never real CUSIPs in examples)
    x: np.ndarray             # signed par notional, $; + = dealer buys (client sells)
    mid: np.ndarray           # composite mid, fraction of par (0.97 = 97.00)
    age: np.ndarray           # business days since a print anchored the composite
    print_frac: np.ndarray    # share of last 60 business days with a print, in (0, 1]
    lcs: np.ndarray           # round-trip LCS at standard size, fraction of price
    oasd: np.ndarray          # spread duration, years
    oas: np.ndarray           # OAS, decimal (0.045 = 450bp)
    sector: np.ndarray        # int sector code in [0, N_SECTORS)
    sig_idio: np.ndarray      # daily idiosyncratic price vol, fraction of par
    prs: np.ndarray           # Priming Risk Score in [0, 1] (Ch 13)
    days_to_call: np.ndarray  # business days to next lender call; np.inf if none
    ad_hoc: np.ndarray        # 1.0 if an ad hoc group / Rule 2019 statement is live

    def __post_init__(self):
        n = len(self.x)
        for name, arr in self.__dict__.items():
            if len(arr) != n:
                raise ValueError(f"{name}: length {len(arr)} != {n}")
        numeric = [self.x, self.mid, self.age, self.print_frac, self.lcs, self.oasd,
                   self.oas, self.sig_idio, self.prs, self.ad_hoc]
        if not all(np.all(np.isfinite(a)) for a in numeric):
            raise ValueError("non-finite numeric field")
        if np.any(self.x == 0):
            raise ValueError("zero-notional line")
        if np.any((self.mid <= 0) | (self.mid > 1.5)):
            raise ValueError("mid must be a fraction of par in (0, 1.5]: was 97.0 sent?")
        if np.any((self.print_frac <= 0) | (self.print_frac > 1)):
            raise ValueError("print_frac must lie in (0, 1]")
        if np.any(self.lcs < 0) or np.any((self.prs < 0) | (self.prs > 1)):
            raise ValueError("need lcs >= 0 and prs in [0, 1]")
        if np.any(self.sig_idio <= 0):
            raise ValueError("sig_idio must be positive")

    @property
    def n(self):
        return len(self.x)

    def mv(self):
        """Unsigned market value of each line, $."""
        return np.abs(self.x) * self.mid

    def drop(self, idx):
        keep = np.ones(self.n, dtype=bool)
        keep[np.asarray(idx, dtype=int)] = False
        return Basket(**{k: v[keep] for k, v in self.__dict__.items()})


def make_basket(n=150, total=212e6, seed=19):
    """Synthetic all-HY client-sell basket matching the cold open (illustrative)."""
    rng = np.random.default_rng(seed)
    size = rng.lognormal(mean=np.log(1.0e6), sigma=0.6, size=n)
    others = np.ones(n, dtype=bool)
    others[[41, 116]] = False
    size[41], size[116] = 18e6, 4e6                      # line 42 and line 117 (1-based)
    size[others] *= (total - 22e6) / size[others].sum()  # hit the $212mm ticket exactly
    mid = np.clip(rng.normal(0.97, 0.04, n), 0.70, 1.06)
    age = rng.exponential(1.5, n)
    pf = rng.uniform(0.15, 0.80, n)
    lcs = np.clip(rng.lognormal(np.log(0.010), 0.45, n), 0.003, 0.06)
    oasd = rng.uniform(2.5, 6.0, n)
    oas = rng.uniform(0.025, 0.060, n)
    sector = rng.integers(0, N_SECTORS, n)
    sig = 0.0025 * rng.uniform(0.6, 1.6, n)
    prs = rng.beta(1.0, 9.0, n)
    dtc = np.full(n, np.inf)
    adhoc = np.zeros(n)
    # line 42: big, stale, wide ("last printed eight weeks ago")
    age[41], pf[41], lcs[41], mid[41], sig[41] = 40.0, 0.05, 0.025, 0.95, 0.003
    # line 117: the name Theo recognizes; note its realized vol looks perfectly calm
    mid[116], oas[116], lcs[116], sig[116] = 0.82, 0.090, 0.012, 0.003
    prs[116], dtc[116], adhoc[116] = 0.85, 3.0, 1.0
    ids = np.array([f"L{i + 1:03d}" for i in range(n)])
    return Basket(ids, size, mid, age, pf, lcs, oasd, oas, sector, sig, prs, dtc, adhoc)


b0 = make_basket()
assert b0.n == 150 and abs(np.abs(b0.x).sum() - 212e6) < 1.0
assert np.all(b0.x > 0)                      # client sells everything: dealer buys
try:                                         # the points-vs-fraction guard fires
    replace(b0, mid=b0.mid * 100.0)
    raise AssertionError("guard failed")
except ValueError:
    pass

# Sanity (DER A): mean-variance CE is exact for CARA utility and Gaussian P&L
gam_t, mu_t, sd_t = 1e-6, 1.0e5, 3.0e5       # 1/$, $, $
W = RNG.normal(mu_t, sd_t, 400_000)
ce_mc = -np.log(np.mean(np.exp(-gam_t * W))) / gam_t
assert abs(ce_mc - (mu_t - 0.5 * gam_t * sd_t**2)) < 2_000.0
```


### Listing 19.2: Per-line handling cost with a size exponent and a liquidity multiplier {#code-19-2}

```python
X_STD = 4e6   # LCS standard size, $ par (Ben_Dor p.118: "$3 to $5 million")

def handling_cost(b, omega=0.5, eta=0.75, x_std=X_STD, m=1.0):
    """Eq. 19.3: one-way handling cost per line, $. m = liquidity regime multiplier (19.7)."""
    if not (0.0 < omega <= 1.0 and 0.5 <= eta <= 1.0 and m > 0):
        raise ValueError("omega in (0,1], eta in [0.5,1], m > 0")
    u = np.abs(b.x) / x_std
    return m * omega * 0.5 * b.lcs * b.mid * np.abs(b.x) * np.maximum(1.0, u) ** eta

c0 = handling_cost(b0)
assert np.all(c0 >= 0)
small = np.abs(b0.x) <= X_STD                     # at or below standard size: flat
assert np.allclose(c0[small], 0.25 * b0.lcs[small] * b0.mv()[small])
# line 42 ($18mm) pays (18/4)^0.75 ~ 3.1x the standard per-dollar rate
assert np.isclose(c0[41] / (0.25 * b0.lcs[41] * b0.mv()[41]), 4.5 ** 0.75)
# line 42 alone costs more to handle than the 25 cheapest lines combined
assert c0[41] > np.sort(c0)[:25].sum()
```


### Listing 19.3: Factor loadings, factor covariance and the minimum-variance hedge {#code-19-3}

```python
T_DAYS = 5.0          # unwind horizon, business days (Li 2022: ~5.3 extra days in inventory)
SIG_MKT_D = 0.015     # daily vol of the market relative-spread factor (illustrative)
SIG_SEC_D = 0.008     # daily vol of each sector relative-spread factor (illustrative)
HEDGE_HALF_SPREAD = np.array([1e-4, 0.5e-4])   # $ per $ notional: ETF, CDX (illustrative)

def loadings(b):
    """B (N, K): price change (fraction of par) per unit relative spread move.
    DTS model: dP = -P * D_spr * ds,  ds = s * g  =>  B = -P * DTS."""
    dts = b.oasd * b.oas
    B = np.zeros((b.n, 1 + N_SECTORS))
    B[:, 0] = -b.mid * dts
    B[np.arange(b.n), 1 + b.sector] = -b.mid * dts
    return B

def factor_cov(T=T_DAYS):
    """Omega_T (K, K): independent market and sector factors over the horizon."""
    return np.diag(np.r_[SIG_MKT_D**2, np.full(N_SECTORS, SIG_SEC_D**2)]) * T

def hedge_book(T=T_DAYS, basis_scale=1.0):
    """A (H, K) loadings per $ notional; U (H, H) basis covariance. Index DTS 0.16 / 0.14."""
    A = np.zeros((2, 1 + N_SECTORS))
    A[0, 0], A[1, 0] = -0.16, -0.14
    A[0, 1:], A[1, 1:] = -0.16 / N_SECTORS, -0.14 / N_SECTORS   # equal sector weights
    U = np.diag([0.0015**2, 0.0010**2]) * T * basis_scale**2
    return A, U

def joint_cov(b, d, T=T_DAYS, basis_scale=1.0, cond_max=1e8):
    """Sxx (N,N), Sxf (N,H), Sff (H,H); d = (N,) idiosyncratic variance over T."""
    B, Om = loadings(b), factor_cov(T)
    A, U = hedge_book(T, basis_scale)
    Sxx = B @ Om @ B.T + np.diag(d)
    Sxf = B @ Om @ A.T
    Sff = A @ Om @ A.T + U
    if np.linalg.cond(Sff) > cond_max:
        raise ValueError("hedges nearly collinear: drop one or model the basis")
    return Sxx, Sxf, Sff

def residual(Sxx, Sxf, Sff):
    """Eq. 19.4: Schur complement = optimally re-hedged covariance for any basket."""
    return Sxx - Sxf @ np.linalg.solve(Sff, Sxf.T)

def min_var_hedge(x, Sxf, Sff):
    """h* = Sff^{-1} Sfx x, $ notional per hedge (positive = sell risk)."""
    return np.linalg.solve(Sff, Sxf.T @ x)

d_naive = b0.sig_idio**2 * T_DAYS                    # no staleness yet (that is 19.5)
Sxx, Sxf, Sff = joint_cov(b0, d_naive)
Sres_naive = residual(Sxx, Sxf, Sff)
h0 = min_var_hedge(b0.x, Sxf, Sff)
v_unh = b0.x @ Sxx @ b0.x
v_res = b0.x @ Sres_naive @ b0.x
v_chk = v_unh - 2.0 * h0 @ (Sxf.T @ b0.x) + h0 @ Sff @ h0
assert np.isclose(v_res, v_chk, rtol=1e-8)          # Schur complement == hedged variance
assert v_res < 0.5 * v_unh                           # the hedge kills most of the lump
```


### Listing 19.4: Residual covariance for stale bonds: idiosyncratic variance and PSD projection {#code-19-4}

```python
def idio_var(b, T=T_DAYS, xi=0.5, kappa_stale=0.5, tau2=0.0):
    """Eq. 19.5: horizon idio variance + stale-composite error, sparse-print bias fix, ridge."""
    return b.sig_idio**2 * (T + kappa_stale * b.age) * b.print_frac ** (-xi) + tau2

def psd_project(S, rel_floor=1e-10):
    """Symmetrize, clip eigenvalues at rel_floor * max, symmetrize again."""
    S = 0.5 * (S + S.T)
    w, V = np.linalg.eigh(S)
    w = np.maximum(w, rel_floor * w.max())
    S = (V * w) @ V.T
    return 0.5 * (S + S.T)

def build_residual_cov(b, T=T_DAYS, basis_scale=1.0, cond_max=1e6, **kw):
    """Returns Sxx, Sxf, Sff and the PSD-projected, condition-guarded Sigma_res."""
    Sxx, Sxf, Sff = joint_cov(b, idio_var(b, T, **kw), T, basis_scale)
    Sres = psd_project(residual(Sxx, Sxf, Sff))
    if np.linalg.cond(Sres) > cond_max:
        raise ValueError("Sigma_res ill-conditioned: raise tau2 or evict lines")
    return Sxx, Sxf, Sff, Sres

Sxx, Sxf, Sff, Sres = build_residual_cov(b0)
assert np.all(np.linalg.eigvalsh(Sres) > 0)
assert Sres[41, 41] > 5.0 * Sres_naive[41, 41]       # staleness is variance, not a haircut
assert np.all(np.diag(Sres) >= idio_var(b0) * (1 - 1e-9))   # Sigma_res >= D in PSD order
# Kaz's matrix: 150 bonds x 14 observations -> rank <= 13, i.e. 137 "riskless" directions
R_kaz = RNG.normal(size=(14, 150))
assert np.linalg.matrix_rank(np.cov(R_kaz, rowvar=False)) <= 13
```


### Listing 19.5: Greedy eviction on exact removal savings {#code-19-5}

```python
def evict_greedy(b, Sres, as_vec, gamma=1e-6, omega=0.5, eta=0.75, m=1.0,
                 alpha=0.15, k_max=10, target=0.0045):
    """Greedy eviction on exact removal savings (eq. 19.7). Stops at cost/MV <= target,
    evicted MV > alpha * gross MV, or k_max lines. Returns (evicted indices, cost/MV path)."""
    mv = b.mv()
    c = handling_cost(b, omega, eta, m=m)
    x = b.x.astype(float).copy()
    alive = np.ones(b.n, dtype=bool)
    Sx = Sres @ x
    diag_s = np.diag(Sres)
    budget = alpha * mv.sum()

    def total():                       # x is zeroed for evicted lines
        return c[alive].sum() + as_vec[alive].sum() + 0.5 * gamma * x @ Sres @ x

    C = total()
    path, evicted = [C / mv[alive].sum()], []
    while len(evicted) < k_max and path[-1] > target:
        delta = c + as_vec + gamma * x * Sx - 0.5 * gamma * diag_s * x**2
        room = budget - mv[~alive].sum()
        ratio = np.where(alive & (mv <= room), delta / mv, -np.inf)
        j = int(np.argmax(ratio))
        if not np.isfinite(ratio[j]) or ratio[j] <= path[-1]:
            break
        Sx -= Sres[:, j] * x[j]        # O(N) update of the coupling term
        x[j] = 0.0
        alive[j] = False
        evicted.append(j)
        C_new = total()
        assert np.isclose(C - C_new, delta[j], rtol=1e-9, atol=1e-6)   # eq. 19.7 is exact
        C = C_new
        path.append(C / mv[alive].sum())
    return evicted, np.array(path)

# Without an adverse-selection model the engine evicts line 42 (index 41) and stops.
ev_noas, path_noas = evict_greedy(b0, Sres, np.zeros(b0.n))
assert ev_noas == [41]
assert np.all(np.diff(path_noas) < 0)
```


### Listing 19.6: The stress score and the stress covariance {#code-19-6}

```python
def regime(etf_disc_z=0.0, bidask_pct=0.5):
    """Stress score s in [0, 2] from ETF discount z-score (negative = discount) and bid-ask
    percentile in [0, 1]; one score drives m, gamma and basis together. At s = 2, m = 5.8,
    Ben Dor's 0.59% -> 3.40% IG LCS range (illustrative calibration)."""
    s = max(0.0, -etf_disc_z - 1.0) / 3.0 + max(0.0, bidask_pct - 0.8) / 0.2
    s = min(s, 2.0)
    return dict(s=s, m=1.0 + 2.4 * s, gamma_mult=1.0 + 1.5 * s, basis_mult=1.0 + 2.0 * s)

THETA_LIQ = 0.8   # price change per unit of m per unit of LCS (illustrative)

def stress_cov(b, Sres_calm, s):
    """Eq. 19.9: calm residual covariance plus a rank-one liquidity spike."""
    g = -THETA_LIQ * b.lcs * b.mid
    return Sres_calm + (0.25 * s) ** 2 * np.outer(g, g)

reg = regime(etf_disc_z=-2.5, bidask_pct=0.9)
assert np.isclose(reg["s"], 1.0) and np.isclose(regime(-10.0, 1.0)["m"], 5.8)
S_st = stress_cov(b0, Sres, reg["s"])
spike = S_st - Sres
assert np.linalg.matrix_rank(spike, tol=1e-8 * np.linalg.norm(spike, 2)) == 1
# the spike does not diversify: its share of basket variance dwarfs its share of line variance
share_basket = (b0.x @ spike @ b0.x) / (b0.x @ S_st @ b0.x)
share_lines = np.sum(b0.x**2 * np.diag(spike)) / np.sum(b0.x**2 * np.diag(S_st))
assert share_basket > 3.0 * share_lines
```


### Listing 19.7: The adverse-selection charge and markouts {#code-19-7}

```python
W_AS = dict(const=-5.0, prs=4.0, call_soon=1.5, ad_hoc=1.5, log_size=0.3)  # HY (illustrative)
J_FLOOR, J_LMT = 0.01, 0.15        # informed move, fraction of par (illustrative)

def as_charge(b, w=W_AS, j_floor=J_FLOOR, j_lmt=J_LMT):
    """Eq. 19.10: AS_i = MV_i * Pr(informed | z_i) * J_i, $. Returns (AS_i, Pr_i)."""
    call_soon = np.exp(-b.days_to_call / 5.0)        # 0 if no call (inf); -> 1 if imminent
    log_size = np.log(np.abs(b.x) / np.median(np.abs(b.x)))
    logit = (w["const"] + w["prs"] * b.prs + w["call_soon"] * call_soon
             + w["ad_hoc"] * b.ad_hoc + w["log_size"] * log_size)
    p = 1.0 / (1.0 + np.exp(-logit))
    return b.mv() * p * (j_floor + j_lmt * b.prs), p

as0, p0 = as_charge(b0)
assert p0[116] > 0.5 and np.median(p0) < 0.05
assert as0[116] > 0.5 * as0.sum()             # one line carries most of the basket's AS
ev_as, path_as = evict_greedy(b0, Sres, as0)
assert ev_as == [116, 41]                     # line 117 goes first now, then line 42

def markouts(x, p_trade, mid_path):
    """Hand history: per-line $ markout x_i * (mid_{t+tau} - p_i); mid_path is (N, 3),
    already net of factor and hedge P&L (IDO or it didn't happen)."""
    return x[:, None] * (mid_path - p_trade[:, None])

rng_mo = np.random.default_rng(117)
tau = np.array([1.0, 5.0, 20.0])
p_trade = b0.mid.copy()
mid_path = b0.mid[:, None] + rng_mo.normal(size=(b0.n, 3)) * b0.sig_idio[:, None] * np.sqrt(tau)
mid_path[116] = b0.mid[116] - np.array([0.01, 0.05, 0.14])   # the uptier lands (illustrative)
mo = markouts(b0.x, p_trade, mid_path)
assert int(np.argmin(mo[:, 2] / b0.mv())) == 116              # the face-down card, found
```


### Listing 19.8: The live pricing path: price_pt {#code-19-8}

```python
def price_pt(b, gamma=1e-6, omega=0.5, eta=0.75, etf_disc_z=0.0, bidask_pct=0.5,
             target=0.0045, alpha=0.15, k_max=10, evict=True):
    """Live path. Returns dealer cash for the kept basket (eq. 19.2; negative = dealer
    receives) and the four-term decomposition, all in $; cost_bp is on gross MV."""
    t0 = time.perf_counter()
    reg = regime(etf_disc_z, bidask_pct)
    gam, m = gamma * reg["gamma_mult"], reg["m"]
    _, Sxf, Sff, S = build_residual_cov(b, basis_scale=reg["basis_mult"])
    if reg["s"] > 0:
        S = stress_cov(b, S, reg["s"])
    as_vec, _ = as_charge(b)
    ev = []
    if evict:
        ev, _ = evict_greedy(b, S, as_vec, gamma=gam, omega=omega, eta=eta, m=m,
                             alpha=alpha, k_max=k_max, target=target)
    keep = np.setdiff1d(np.arange(b.n), ev)
    bk = b.drop(ev)
    h = min_var_hedge(bk.x, Sxf[keep], Sff)
    handling = handling_cost(bk, omega, eta, m=m).sum()
    risk = 0.5 * gam * bk.x @ S[np.ix_(keep, keep)] @ bk.x
    adv = as_vec[keep].sum()
    hedge_cost = np.abs(h) @ HEDGE_HALF_SPREAD
    cost = handling + risk + adv + hedge_cost
    gross = bk.mv().sum()
    return dict(cash=bk.x @ bk.mid - cost, cost=cost, cost_bp=1e4 * cost / gross,
                handling=handling, risk=risk, adv=adv, hedge_cost=hedge_cost, hedge=h,
                evicted=[str(b.ids[i]) for i in ev], hit_target=cost / gross <= target,
                regime=reg, ms=1e3 * (time.perf_counter() - t0))

fair = b0.x @ b0.mid
full = price_pt(b0, evict=False)
calm = price_pt(b0)
assert full["cash"] < fair                                   # a bid sits below fair value
assert np.isclose(full["cost"], full["handling"] + full["risk"] + full["adv"]
                  + full["hedge_cost"])
assert calm["evicted"] == ["L117", "L042"] and calm["hit_target"]
assert calm["cost_bp"] < full["cost_bp"]                     # the counter-proposal pays
stress = price_pt(b0, etf_disc_z=-2.5, bidask_pct=0.9, evict=False)
assert stress["cost"] > 2.0 * full["cost"]                   # same basket, one regime later
buy = price_pt(replace(b0, x=-b0.x), evict=False)           # client buys the same lines
assert np.isclose(buy["cost"], full["cost"], rtol=1e-9)      # costs are side-symmetric
assert np.isclose(buy["cash"], -fair - full["cost"])         # the ask sits above fair value
assert calm["ms"] < 1000.0                                   # the linear algebra is the easy second
```


## F.20: Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN) {#code-20}

Listings from `20_ch20_credit_etf_creation_redemption_arb.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 20.1: The ETF arbitrage monitor: static band, NAV catch-up, clearing premium and basket choice {#code-20-1}

```python
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20)

# ---- Block 1: a synthetic HY fund and the static band (20.4) ----
N = 120
n_units = rng.uniform(0.5, 1.5, N)             # face per share (arbitrary units)
mid = rng.uniform(85.0, 102.0, N)              # evaluated mid, points
c = rng.uniform(0.0015, 0.0060, N)             # half bid-offer, fraction of price
val = n_units * mid
M_tilde = val.sum()
c_bar = float((val * c).sum() / M_tilde)
NAV = float((n_units * mid * (1 - c)).sum())   # bid-side NAV
h = val / M_tilde                              # portfolio value weights
assert np.isclose(NAV, M_tilde * (1 - c_bar)) and NAV < M_tilde


def static_band(c_bar, c_create, c_redeem, f_c=1e-4, f_r=1e-4, k_c=5e-4, k_r=5e-4):
    """Eq. (20.4). All inputs and outputs are fractions of NAV."""
    pi_lo = (c_bar - c_redeem) - f_r - k_r
    pi_hi = (c_bar + c_create) + f_c + k_c
    return pi_lo, pi_hi


lo, hi = static_band(c_bar, c_bar, c_bar)
assert lo < 0 < hi
lo_mid, hi_mid = lo - c_bar, hi - c_bar        # the same band under a mid-price NAV
assert np.isclose(hi - lo, hi_mid - lo_mid)    # convention moves the center, not the width
assert np.isclose(0.5 * (lo + hi) - 0.5 * (lo_mid + hi_mid), c_bar)
P_edge = NAV * (1 + hi)                         # exact creation P&L at the upper edge
exact_edge = (P_edge - M_tilde * (1 + c_bar)) / NAV - 1e-4 - 5e-4
assert abs(exact_edge) < 1e-4                   # first-order error is -2 c_bar^2 / (1 - c_bar)

# ---- Block 2: staleness (20.2) and the NAV catch-up regression (20.3) ----
T = 4000
eta_true, sig_r, sig_ell = 0.35, 0.004, 0.0002
r = rng.normal(0.0, sig_r, T)
lnM = np.cumsum(r)
lnMt = np.empty(T)
lnMt[0] = lnM[0]
for t in range(1, T):
    lnMt[t] = lnMt[t - 1] + eta_true * (lnM[t] - lnMt[t - 1])
ell = rng.normal(0.0, sig_ell, T)
lnP = lnM + ell
lnNAV = lnMt + np.log(1 - c_bar)
p = lnP - lnNAV
s = lnM - lnMt
assert np.allclose(p, ell + s - np.log(1 - c_bar))       # identity (20.1)


def nav_catchup(lnNAV, p):
    """OLS of d ln NAV_t on p_{t-1}. Returns (slope, intercept); eq. (20.3)."""
    y = np.diff(lnNAV)
    X = np.column_stack([np.ones(len(y)), p[:-1]])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return float(beta[1]), float(beta[0])


eta_hat, a_hat = nav_catchup(lnNAV, p)
var_s = (1 - eta_true) ** 2 / (eta_true * (2 - eta_true)) * sig_r ** 2
atten = var_s / (var_s + sig_ell ** 2)
assert abs(eta_hat - eta_true * atten) < 0.03            # slope = eta x staleness share
assert abs(a_hat + eta_hat * (-np.log(1 - c_bar))) < 5e-4  # intercept = -eta x c_bar
assert abs(s[200:].var() / var_s - 1) < 0.15             # stationary variance formula

# ---- Block 3: the balance-sheet band (20.5) ----
def clearing_premium(F, kappa_r, gammas, sigma_b, T_h):
    """Premium at which J mean-variance APs absorb net ETF selling F (dollars)."""
    g = np.asarray(gammas, float)
    if np.any(g <= 0) or sigma_b <= 0 or T_h <= 0:
        raise ValueError("gammas, sigma_b and T_h must be positive")
    g_bar = 1.0 / np.sum(1.0 / g)
    psi = g_bar * sigma_b ** 2 * T_h
    return -kappa_r - psi * F, psi


def ap_redemptions(pi, kappa_r, gammas, sigma_b, T_h):
    """Aggregate dollar redemptions sum_j X Q_j^* at premium pi."""
    edge = max(-pi - kappa_r, 0.0)
    return edge / (sigma_b ** 2 * T_h) * np.sum(1.0 / np.asarray(gammas, float))


kappa_r, F = 6e-4, 2.0e9
calm = dict(gammas=[4.4e-7] * 28, sigma_b=0.02, T_h=2 / 252)
stress = dict(gammas=[8.8e-7] * 24, sigma_b=0.12, T_h=8 / 252)
pi_calm, psi_calm = clearing_premium(F, kappa_r, **calm)
pi_str, psi_str = clearing_premium(F, kappa_r, **stress)
assert np.isclose(ap_redemptions(pi_calm, kappa_r, **calm), F)    # market clears
assert np.isclose(ap_redemptions(pi_str, kappa_r, **stress), F)
assert np.isclose(psi_str / psi_calm, 2 * 36 * 4 * 28 / 24)        # corollaries (a)-(b)
assert abs(psi_calm * F - 1e-4) < 2e-6 and -0.05 < pi_str < -0.02  # 1 bp becomes about 3.4%

# ---- Block 4: the custom basket QP (20.6)-(20.7) ----
K = 40
hK = h[:K] / h[:K].sum()
cK = c[:K]
vol = rng.uniform(0.03, 0.10, K)
Sigma = np.outer(vol, vol) * (0.6 * np.ones((K, K)) + 0.4 * np.eye(K))
axe = np.zeros(K)
axe[rng.choice(K, 6, replace=False)] = 0.0030            # AP is axed in six bonds
k = cK - axe - 0.5 * cK                                  # c_i - a_i - l_i, with l_i = c_i / 2


def J_cost(w, h, k, Sigma, theta):
    d = w - h
    return float(k @ w + 0.5 * theta * d @ Sigma @ d)


def basket_closed_form(h, k, Sigma, theta):
    """Eq. (20.6), ignoring w >= 0. Returns (w*, mu*, D)."""
    one = np.ones(len(h))
    Si_k, Si_1 = np.linalg.solve(Sigma, k), np.linalg.solve(Sigma, one)
    mu = (one @ Si_k) / (one @ Si_1)
    dev = Si_k - mu * Si_1                                # Sigma^{-1}(k - mu 1)
    return h - dev / theta, float(mu), float((k - mu * one) @ dev)


def basket_qp(h, k, Sigma, theta, w_max=1.0):
    """Eq. (20.6) with 0 <= w <= w_max, solved by SLSQP."""
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones_like(w)}]
    scale = 1e4                                           # optimize in bp for SLSQP's tolerances
    res = minimize(lambda w: scale * J_cost(w, h, k, Sigma, theta), h.copy(),
                   jac=lambda w: scale * (k + theta * Sigma @ (w - h)),
                   bounds=[(0.0, w_max)] * len(h), constraints=cons,
                   method="SLSQP", options={"ftol": 1e-12, "maxiter": 500})
    if not res.success:
        raise RuntimeError(res.message)
    return res.x


theta = 50.0
w_cf, mu, D = basket_closed_form(hK, k, Sigma, theta)
assert np.isclose(w_cf.sum(), 1.0)
assert np.isclose(J_cost(hK, hK, k, Sigma, theta) - J_cost(w_cf, hK, k, Sigma, theta),
                  D / (2 * theta))                         # value of freedom, (20.7)
assert np.allclose(basket_closed_form(hK, k, Sigma, 1e9)[0], hK, atol=1e-6)  # theta -> inf
w_qp = basket_qp(hK, k, Sigma, theta)
assert w_qp.min() >= -1e-9 and np.isclose(w_qp.sum(), 1.0, atol=1e-8)
J_h, J_qp, J_cf = (J_cost(x, hK, k, Sigma, theta) for x in (hK, w_qp, w_cf))
assert J_cf <= J_qp + 1e-10 and J_qp <= J_h + 1e-10       # constraints can only cost
assert (w_qp[axe > 0] - hK[axe > 0]).mean() > 0           # axed bonds are overweighted
print(f"basket coverage {(w_qp > 1e-4).mean():.0%}; saving vs pro rata {1e4 * (J_h - J_qp):.2f} bp")

# ---- Block 5: the loan-ETF liquidity sleeve (20.8) ----
def sleeve_path(phi0, redemptions, lag_weeks):
    """phi_{t+1} = phi_t - R_t + R_{t-L}. Returns (path, first week exhausted or None)."""
    R = np.asarray(redemptions, float)
    phi = np.empty(len(R) + 1)
    phi[0] = phi0
    for t in range(len(R)):
        proceeds = R[t - lag_weeks] if t >= lag_weeks else 0.0
        phi[t + 1] = phi[t] - R[t] + proceeds
    bust = np.flatnonzero(phi <= 0)
    return phi, (int(bust[0]) if bust.size else None)


weekly = np.full(13, 0.092 / (31 / 7))          # 13 weeks at the March 2020 HY pace
phi, bust = sleeve_path(0.10, weekly, lag_weeks=3)
assert bust is None and np.isclose(phi.min(), 0.10 - 3 * weekly[0])
_, bust2 = sleeve_path(0.10, np.r_[0.045, 0.045, 0.045, np.zeros(10)], lag_weeks=3)
assert bust2 == 3                               # three heavy weeks before any proceeds land

# ---- Block 6: the monitor ROBO ships ----
def classify(p_t, c_bar, band, s_hat, u_t):
    """Regime label for a log premium p_t, per (20.1) and (20.4)."""
    lo, hi = band
    if lo <= p_t <= hi:
        return "inside_band"
    if abs(p_t - c_bar) <= u_t:
        return "measurement_noise"
    if abs(s_hat) >= 0.5 * abs(p_t - c_bar):
        return "late_nav"
    flow = p_t - c_bar - s_hat
    return "flow_dislocation_redeem" if flow < 0 else "flow_dislocation_create"


band = static_band(c_bar, c_bar, c_bar)
assert classify(c_bar + 1e-4, c_bar, band, 0.0, 0.001) == "inside_band"
assert classify(-0.004, c_bar, band, 0.0, 0.010) == "measurement_noise"
assert classify(-0.05, c_bar, band, -0.04, 0.005) == "late_nav"
assert classify(-0.05, c_bar, band, -0.005, 0.005) == "flow_dislocation_redeem"
```


## F.21: Chapter 21: Leveraged Loans, CLOs & Loan-Market Microstructure {#code-21}

Listings from `21_ch21_leveraged_loans_and_clo_microstructure.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 21.1: The CLO overcollateralization test and the cure trade {#code-21-1}

```python
# Chapter 21 reference implementation, block 1: the OC engine and the cure trade.
import numpy as np
import pandas as pd

RNG = np.random.default_rng(21)
CCC_LIMIT = 0.075   # CCC bucket as a fraction of non-defaulted collateral par
TOL = 1e-9
POOL_COLS = ["par", "price", "is_ccc", "is_default", "agency_rec", "is_discount", "purchase_px"]


def ccc_excess_haircut(par_ccc, px_ccc, limit_par):
    """Haircut (par minus market value) on the CCC excess, cheapest CCC loans first.

    par_ccc, px_ccc : 1-D arrays for the CCC loans only (price as a fraction of par).
    limit_par       : bucket size in par (ccc_limit * non-defaulted par).
    Returns (haircut, excess_par, marginal_price); marginal_price is NaN if no excess.
    """
    par_ccc = np.asarray(par_ccc, dtype=float)
    px_ccc = np.asarray(px_ccc, dtype=float)
    excess = max(0.0, float(par_ccc.sum()) - limit_par)
    if excess <= TOL:
        return 0.0, 0.0, float("nan")
    order = np.argsort(px_ccc, kind="stable")          # cheapest first
    haircut, remaining, p_marg = 0.0, excess, float("nan")
    for p, n in zip(px_ccc[order], par_ccc[order]):
        take = min(n, remaining)
        haircut += max(0.0, 1.0 - p) * take             # never a gain above par
        remaining -= take
        p_marg = float(p)
        if remaining <= TOL:
            break
    return haircut, excess, p_marg


def acpa(pool, cash=0.0, ccc_limit=CCC_LIMIT):
    """Adjusted collateral principal amount, equation (21.5)."""
    missing = set(POOL_COLS) - set(pool.columns)
    if missing:
        raise ValueError(f"pool missing columns: {sorted(missing)}")
    par = pool["par"].to_numpy(float)
    px = pool["price"].to_numpy(float)
    rec = pool["agency_rec"].to_numpy(float)
    p0 = pool["purchase_px"].to_numpy(float)
    dflt = pool["is_default"].to_numpy(bool)
    disc = pool["is_discount"].to_numpy(bool) & ~dflt
    ccc = pool["is_ccc"].to_numpy(bool) & ~dflt & ~disc
    if np.any(par < 0) or np.any(px <= 0) or np.any(px > 1.2):
        raise ValueError("par must be >= 0 and price a fraction of par in (0, 1.2]")
    h_def = float(np.sum(par[dflt] * (1.0 - np.minimum(px[dflt], rec[dflt]))))
    h_disc = float(np.sum(par[disc] * (1.0 - np.minimum(p0[disc], 1.0))))
    base = float(par[~dflt].sum())
    h_ccc, x_ccc, p_marg = ccc_excess_haircut(par[ccc], px[ccc], ccc_limit * base)
    value = float(par.sum()) + cash - h_def - h_disc - h_ccc
    share = float(par[ccc].sum()) / base if base > 0 else float("nan")
    return {"acpa": value, "h_def": h_def, "h_disc": h_disc, "h_ccc": h_ccc,
            "ccc_excess": x_ccc, "p_marg": p_marg, "ccc_share": share}


def oc_test(acpa_value, balances, triggers):
    """OC ratio and cushion (ratio minus trigger, decimals) per class, senior to junior."""
    cum = np.cumsum(np.asarray(balances, dtype=float))
    ratio = acpa_value / cum
    return ratio, ratio - np.asarray(triggers, dtype=float)


def make_pool(n_loans=250, par_each=2.0, n_ccc=21, n_default=2, n_disc=3, rng=RNG):
    """Synthetic 500mm pool (par in mm): CCC prices span 50-92 cents (illustrative)."""
    price = np.clip(rng.normal(0.985, 0.012, n_loans), 0.93, 1.005)
    is_ccc = np.zeros(n_loans, bool)
    is_default = np.zeros(n_loans, bool)
    is_disc = np.zeros(n_loans, bool)
    is_ccc[:n_ccc] = True
    price[:n_ccc] = np.linspace(0.50, 0.92, n_ccc)
    is_default[n_ccc:n_ccc + n_default] = True
    price[n_ccc:n_ccc + n_default] = 0.40
    d0 = n_ccc + n_default
    is_disc[d0:d0 + n_disc] = True
    price[d0:d0 + n_disc] = 0.86
    return pd.DataFrame({
        "par": np.full(n_loans, par_each), "price": price, "is_ccc": is_ccc,
        "is_default": is_default, "agency_rec": np.full(n_loans, 0.45),
        "is_discount": is_disc, "purchase_px": np.where(is_disc, 0.80, 1.0)})


def sell_and_rebuy_par(pool, idx):
    """Sell loan idx at its price and buy a performing loan at par with the proceeds."""
    row = pool.loc[idx]
    new = pd.DataFrame({"par": [row["par"] * row["price"]], "price": [1.0],
                        "is_ccc": [False], "is_default": [False], "agency_rec": [0.45],
                        "is_discount": [False], "purchase_px": [1.0]})
    return pd.concat([pool.drop(index=idx), new], ignore_index=True)


pool = make_pool()
BAL = np.array([365.0, 40.0, 30.0, 25.0])   # AAA/AA combined, A, BBB, BB (mm)
TRIG = np.array([1.22, 1.15, 1.08, 1.04])    # illustrative OC triggers
res = acpa(pool)
ratio, cushion = oc_test(res["acpa"], BAL, TRIG)

# Sanity 1: with every haircut off, ACPA is plain par (Schmid's textbook ratio).
clean = pool.assign(is_ccc=False, is_default=False, is_discount=False)
assert abs(acpa(clean)["acpa"] - pool["par"].sum()) < TOL

# Sanity 2: the bucket is over its limit; the marginal CCC is the third-cheapest here.
assert res["ccc_share"] > CCC_LIMIT and res["h_ccc"] > 0.0
assert abs(res["p_marg"] - pool.loc[pool.is_ccc, "price"].nsmallest(3).max()) < TOL

# Sanity 3: the cliff. Flat below the limit, (1 - p) on someone else's loan above it.
under = pool.copy()
under.loc[under.index[:5], "is_ccc"] = False             # CCC share about 6.5%
assert acpa(under)["h_ccc"] == 0.0
j = under.index[((~under.is_ccc) & (~under.is_default) & (~under.is_discount)).to_numpy()][-1]
under_dg = under.copy()
under_dg.loc[j, "is_ccc"] = True
assert acpa(under_dg)["h_ccc"] == 0.0                    # flat side of the cliff
over_dg = pool.copy()
over_dg.loc[j, "is_ccc"] = True                          # the bucket is already full
d_h = acpa(over_dg)["h_ccc"] - res["h_ccc"]
assert 0.0 < d_h <= 2.0 * (1.0 - 0.50) + TOL
print(f"downgrading a loan at {pool.loc[j, 'price']:.3f} cost {d_h:.3f}mm via other loans")

# Sanity 4: the cure-trade theorem, equation (21.6).
ccc_px = pool.loc[pool.is_ccc, "price"]
i_rich, i_cheap = ccc_px.idxmax(), ccc_px.idxmin()
n_i, p_i, p_m = pool.loc[i_rich, "par"], pool.loc[i_rich, "price"], res["p_marg"]
d_rich = acpa(sell_and_rebuy_par(pool, i_rich))["acpa"] - res["acpa"]
d_cheap = acpa(sell_and_rebuy_par(pool, i_cheap))["acpa"] - res["acpa"]
bound = n_i * ((p_i - p_m) - CCC_LIMIT * (1.0 - p_m) * (1.0 - p_i))
assert d_rich >= bound - TOL and d_rich > 0.0
p_c, n_c = pool.loc[i_cheap, "price"], pool.loc[i_cheap, "par"]
assert -CCC_LIMIT * (1.0 - p_c) * n_c - TOL <= d_cheap <= TOL
assert d_rich > d_cheap
print(f"junior OC {ratio[-1]:.4f} (cushion {cushion[-1]:+.4f}); "
      f"cure: sell richest CCC {d_rich:+.3f}mm, cheapest {d_cheap:+.3f}mm")
```


### Listing 21.2: The CLO Forced-Sale Pressure Index {#code-21-2}

```python
# Block 2: CLO Forced-Sale Pressure Index, calibrated to Elkamhi-Nozawa (2022) magnitudes.
P0, K0 = 0.1327, 0.04                 # 3-month sale probability at a 4% junior cushion
DP_PER_SD, SD_K = 0.0156, 0.0326      # +1.56pp per one-SD (3.26%) drop in cushion
B_FS = (DP_PER_SD / SD_K) / (P0 * (1.0 - P0))
A_FS = np.log(P0 / (1.0 - P0)) + B_FS * K0
D_FS = 10.0                           # illustrative loading on CCC excess / par


def sale_prob(jr_cushion, ccc_excess_frac):
    """P(a CLO sells a downgraded holding within 3 months); inputs are decimals."""
    z = (A_FS - B_FS * np.asarray(jr_cushion, float)
         + D_FS * np.maximum(0.0, np.asarray(ccc_excess_frac, float)))
    return 1.0 / (1.0 + np.exp(-z))


def fspi(holdings, outstanding, jr_cushion, ccc_excess_frac):
    """holdings (C, I): par of loan i held by CLO c; outstanding (I,).
    Returns (I,) expected fraction of each loan sold by constrained CLOs."""
    H = np.asarray(holdings, float)
    out = np.asarray(outstanding, float)
    if H.ndim != 2 or H.shape[1] != out.shape[0]:
        raise ValueError("holdings must be (C, I) with I == len(outstanding)")
    if np.any(H.sum(axis=0) > out + TOL):
        raise ValueError("CLOs cannot hold more than a loan's outstanding amount")
    return (sale_prob(jr_cushion, ccc_excess_frac) @ H) / out


assert abs(sale_prob(K0, 0.0) - P0) < 1e-12
slope = (sale_prob(K0 - 1e-6, 0.0) - sale_prob(K0 + 1e-6, 0.0)) / 2e-6
assert abs(slope * SD_K - DP_PER_SD) < 1e-4

n_clo, n_loan = 40, 60
outstanding = RNG.uniform(400.0, 1500.0, n_loan)                 # mm
share = RNG.dirichlet(np.ones(n_clo), size=n_loan).T * 0.65      # CLOs own 65% of each loan
holdings = share * outstanding                                    # (C, I)
cush = RNG.normal(0.038, 0.0326, n_clo)
exc = np.maximum(0.0, RNG.normal(0.0, 0.01, n_clo))
f_now = fspi(holdings, outstanding, cush, exc)
assert np.all((f_now >= 0.0) & (f_now <= 0.65 + TOL))
f_stress = fspi(holdings, outstanding, cush - 0.02, exc + 0.01)
assert np.all(f_stress > f_now)                                  # thinner cushions, more selling
print(f"FSPI median {np.median(f_now):.3f} -> stressed {np.median(f_stress):.3f}")
```


### Listing 21.3: The loan as a capped floater with a repricing hazard, and CLO equity gearing {#code-21-3}

```python
# Block 3: the loan as a capped floater with a repricing hazard; CLO equity gearing.
def annuity(T, rate):
    """a(T; rate) = integral_0^T exp(-rate u) du, stable as rate -> 0."""
    rate = np.asarray(rate, dtype=float)
    small = np.abs(rate * T) < 1e-8
    safe = np.where(small, 1.0, rate)
    return np.where(small, T - 0.5 * rate * T**2, (1.0 - np.exp(-safe * T)) / safe)


def loan_price(m, s, base, T=3.0, h=0.0):
    """Price per 100 of a floater paying base + m when the market requires s; eqs (21.2)/(21.7).
    h is the repricing hazard per year, active only while the call is in the money (m > s)."""
    m, s = np.asarray(m, dtype=float), np.asarray(s, dtype=float)
    h_eff = np.where(m > s, h, 0.0)
    return 100.0 * (1.0 + (m - s) * annuity(T, base + s + h_eff))


def spread_duration(m, s, base, h, side, ds=1e-6):
    """One-sided spread duration in years: side=+1 widening, side=-1 tightening."""
    p0 = loan_price(m, s, base, h=h)
    p1 = loan_price(m, s + side * ds, base, h=h)
    return float(-(p1 - p0) / (side * ds) / p0)


THETA = {"const": -3.0, "px_minus_par": 1.2, "softcall_expired": 1.5,
         "above_par_share": 4.0, "is_bb": 0.5}            # illustrative; fit on loan-months


def monthly_reprice_prob(px, softcall_expired, above_par_share, is_bb, theta=THETA):
    """Discrete-time hazard: P(reprice this month | features). px in points."""
    z = (theta["const"] + theta["px_minus_par"] * (np.asarray(px, float) - 100.0)
         + theta["softcall_expired"] * np.asarray(softcall_expired, float)
         + theta["above_par_share"] * (np.asarray(above_par_share, float) - 0.5)
         + theta["is_bb"] * np.asarray(is_bb, float))
    return 1.0 / (1.0 + np.exp(-z))


def annual_hazard(q_month):
    """Monthly event probability -> continuous annual hazard h."""
    q = np.clip(np.asarray(q_month, float), 0.0, 1.0 - 1e-12)
    return -12.0 * np.log1p(-q)


def expected_carry_loss(m, s, h, H=1.0):
    """Equation (21.8): annualized expected margin given up over horizon H (decimals)."""
    gap = np.maximum(np.asarray(m, float) - np.asarray(s, float), 0.0)
    hH = np.asarray(h, float) * H
    small = hH < 1e-8
    frac = np.where(small, 0.5 * hH, 1.0 - (1.0 - np.exp(-hH)) / np.where(small, 1.0, hH))
    return gap * frac


def clo_equity_yield(was, base, w, s, fees, el):
    """Equation (21.3): equity cash yield per year; w, s are liability weights and spreads."""
    w, s = np.asarray(w, float), np.asarray(s, float)
    w_e = 1.0 - w.sum()
    if w_e <= 0.0:
        raise ValueError("liabilities exceed collateral par")
    return base + (was - w @ s - fees - el) / w_e


B0 = 0.0365                                               # base rate (illustrative)
assert abs(float(loan_price(0.0325, 0.0325, B0)) - 100.0) < 1e-12
p_open, p_year, p_shut = (float(loan_price(0.035, 0.030, B0, h=hh)) for hh in (4.0, 1.0, 0.0))
assert 100.0 < p_open < p_year < 100.5 < p_shut           # the ceiling, eq. (21.7)
d_wide = spread_duration(0.03, 0.03, B0, h=4.0, side=+1)
d_tight = spread_duration(0.03, 0.03, B0, h=4.0, side=-1)
assert d_wide > 2.5 and d_tight < 0.3 and d_wide / d_tight > 8.0   # negative convexity

q_hot = monthly_reprice_prob(100.5, 1, 0.6, 0)
q_cold = monthly_reprice_prob(98.0, 0, 0.1, 0)
assert q_hot > 0.3 and q_cold < 0.01
loss = float(expected_carry_loss(0.035, 0.030, 4.0))
assert abs(loss - 0.005 * (1.0 - (1.0 - np.exp(-4.0)) / 4.0)) < 1e-12 and loss < 0.005
assert float(expected_carry_loss(0.030, 0.035, 4.0)) == 0.0

W_LIAB = np.array([0.62, 0.11, 0.08, 0.05, 0.05])         # AAA..BB, fraction of collateral
S_LIAB = np.array([0.0130, 0.0175, 0.0210, 0.0310, 0.0575])  # illustrative 2025 spreads
y_before = clo_equity_yield(0.0319, B0, W_LIAB, S_LIAB, 0.0045, 0.0075)
y_after = clo_equity_yield(0.0319 - 0.5 * 0.0045, B0, W_LIAB, S_LIAB, 0.0045, 0.0075)
assert abs((y_before - y_after) - 0.5 * 0.0045 / 0.09) < 1e-12   # 11x gearing
print(f"prices open/year/shut {p_open:.2f}/{p_year:.2f}/{p_shut:.2f}; "
      f"D_spr wide {d_wide:.2f} vs tight {d_tight:.2f}; equity yield {y_before:.2%}")
```


### Listing 21.4: The loan-fund liquidity queue and the ETF arbitrage band {#code-21-4}

```python
# Block 4: the loan-fund liquidity queue (21.9) and the ETF arbitrage band.
def window_var(sigma_eps, phi, ell):
    """Variance of the ell-day sum of stationary AR(1) flows with innovation sd sigma_eps."""
    if not -1.0 < phi < 1.0:
        raise ValueError("phi must lie in (-1, 1)")
    var_f = sigma_eps**2 / (1.0 - phi**2)
    k = np.arange(1, ell)
    return var_f * (ell + 2.0 * np.sum((ell - k) * phi**k))


def buffer_needed(mu, sigma_eps, phi, ell, z=2.326):
    """Cash buffer (fraction of NAV) covering one ell-day outflow window at one-sided z."""
    return ell * mu + z * np.sqrt(window_var(sigma_eps, phi, ell))


def simulate_flows(mu, sigma_eps, phi, n_days, n_paths, rng=RNG):
    """Seeded stationary AR(1) net-redemption paths, shape (n_paths, n_days)."""
    f = np.empty((n_paths, n_days))
    f[:, 0] = mu + rng.normal(0.0, sigma_eps / np.sqrt(1.0 - phi**2), n_paths)
    for t in range(1, n_days):
        f[:, t] = mu + phi * (f[:, t - 1] - mu) + rng.normal(0.0, sigma_eps, n_paths)
    return f


def rolling_window_sums(f, ell):
    """All ell-day window sums along axis 1."""
    c = np.concatenate([np.zeros((f.shape[0], 1)), np.cumsum(f, axis=1)], axis=1)
    return c[:, ell:] - c[:, :-ell]


def etf_discount_bound(ell, half_spread, sigma_ann, fund_rate=0.05, z=1.645):
    """Approximate discount (decimal) an AP needs before redeeming in kind."""
    return fund_rate * ell / 360.0 + min(half_spread, z * sigma_ann * np.sqrt(ell / 252.0))


MU, SIG, PHI = 0.0005, 0.004, 0.4        # illustrative daily net outflow, sd, persistence
b1, b7, b20 = (buffer_needed(MU, SIG, PHI, ell) for ell in (1, 7, 20))
assert b1 < b7 < b20
sd1, sd20 = np.sqrt(window_var(SIG, PHI, 1)), np.sqrt(window_var(SIG, PHI, 20))
assert np.sqrt(20.0) - 1e-9 <= sd20 / sd1 <= 20.0 + 1e-9     # between sqrt(l) and l scaling

flows = simulate_flows(MU, SIG, PHI, n_days=260, n_paths=2000)
w20 = rolling_window_sums(flows, 20)
assert w20.shape == (2000, 241)
q99 = float(np.quantile(w20, 0.99))
assert abs(q99 / b20 - 1.0) < 0.08                          # simulation agrees with (21.9)

band_loan = etf_discount_bound(20, 0.015, 0.15)
band_clo = etf_discount_bound(1, 0.005, 0.03)
assert band_loan > band_clo > 0.0
print(f"buffers l=1/7/20: {b1:.2%}/{b7:.2%}/{b20:.2%} (MC 99%: {q99:.2%}); "
      f"band loan {band_loan:.2%} vs AAA CLO {band_clo:.2%}")
```


### Listing 21.5: Stale marks: Geltner de-smoothing and Dimson betas {#code-21-5}

```python
# Block 5: stale marks. Geltner desmoothing and Dimson betas before any momentum test.
def smooth_marks(r_true, phi):
    """Observed (marked) returns: r_obs_t = (1 - phi) r_t + phi r_obs_{t-1}."""
    r_obs = np.empty_like(r_true)
    r_obs[0] = r_true[0]
    for t in range(1, len(r_true)):
        r_obs[t] = (1.0 - phi) * r_true[t] + phi * r_obs[t - 1]
    return r_obs


def lag1_autocorr(x):
    x = np.asarray(x, dtype=float) - np.mean(x)
    return float(np.dot(x[1:], x[:-1]) / np.dot(x, x))


def geltner_desmooth(r_obs, phi_hat):
    if not 0.0 <= phi_hat < 1.0:
        raise ValueError("phi_hat must lie in [0, 1)")
    out = np.empty_like(r_obs)
    out[0] = r_obs[0]
    out[1:] = (r_obs[1:] - phi_hat * r_obs[:-1]) / (1.0 - phi_hat)
    return out


def dimson_beta(r_obs, factor, n_lags):
    """Sum of OLS slopes on factor_t, ..., factor_{t-n_lags} (intercept included)."""
    T = len(r_obs)
    cols = [np.ones(T - n_lags)] + [factor[n_lags - k: T - k] for k in range(n_lags + 1)]
    coef, *_ = np.linalg.lstsq(np.column_stack(cols), r_obs[n_lags:], rcond=None)
    return float(coef[1:].sum())


T_W, BETA_L, PHI_M = 5000, 0.8, 0.5                      # weeks, true beta, smoothing
F_idx = RNG.normal(0.0, 0.02, T_W)                         # unsmoothed factor return
r_true = BETA_L * F_idx + RNG.normal(0.0, 0.01, T_W)
r_obs = smooth_marks(r_true, PHI_M)
phi_hat = lag1_autocorr(r_obs)
assert abs(phi_hat - PHI_M) < 0.05                         # eq. (21.10): autocorr = phi
assert np.std(r_obs) < 0.7 * np.std(r_true)                # marks understate volatility
r_hat = geltner_desmooth(r_obs, phi_hat)
assert abs(np.std(r_hat) / np.std(r_true) - 1.0) < 0.12
assert abs(lag1_autocorr(r_hat)) < 0.08                    # spurious momentum removed
naive, dimson = dimson_beta(r_obs, F_idx, 0), dimson_beta(r_obs, F_idx, 8)
assert naive < 0.6 * BETA_L and abs(dimson / BETA_L - 1.0) < 0.05
print(f"phi_hat {phi_hat:.3f}; beta naive {naive:.3f} vs Dimson {dimson:.3f} (true {BETA_L})")
```


## F.22: Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity {#code-22}

Listings from `22_ch22_market_structure_regulation_trends.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 22.1: Balance-sheet rent: binding Tier 1 capital and the breakeven holding period {#code-22-1}

```python
import numpy as np
import pandas as pd

BP = 1e4  # basis points per unit of notional


def capital_rate(kappa_rwa, risk_weight, kappa_lr):
    """Binding Tier 1 per $1 of gross inventory: max(kappa_rwa * RW, kappa_lr). Decimals, not percent."""
    k_rwa, rw, k_lr = (np.asarray(v, dtype=float) for v in (kappa_rwa, risk_weight, kappa_lr))
    if np.any((k_rwa < 0) | (k_rwa > 1)) or np.any((k_lr < 0) | (k_lr > 1)):
        raise ValueError("capital ratios must be decimals in [0, 1]; 5% is 0.05, not 5")
    if np.any(rw < 0):
        raise ValueError("risk_weight must be non-negative")
    return np.maximum(k_rwa * rw, k_lr)


def regulatory_carry_bp(kappa_rwa, risk_weight, kappa_lr, hurdle, holding_days):
    """Balance-sheet rent over the holding period, in bp of |notional| (eq. 22.1 times the hold).
    hurdle: excess annual return on Tier 1 over the funding rate. holding_days: calendar days, ACT/365."""
    hd = np.asarray(holding_days, dtype=float)
    h = np.asarray(hurdle, dtype=float)
    if np.any(hd <= 0):
        raise ValueError("holding_days must be positive")
    if np.any(h < 0):
        raise ValueError("hurdle must be non-negative")
    return BP * h * capital_rate(kappa_rwa, risk_weight, kappa_lr) * hd / 365.0


def breakeven_holding_days(bid_ask_bp, hurdle, kappa_lr, kappa_rwa=0.0, risk_weight=0.0):
    """Holding period (calendar days) at which rent equals the half bid-ask (eq. 22.4)."""
    if hurdle <= 0:
        raise ValueError("hurdle must be positive")
    c_bp_per_year = BP * hurdle * capital_rate(kappa_rwa, risk_weight, kappa_lr)
    if np.any(c_bp_per_year <= 0):
        raise ValueError("binding capital rate is zero: the breakeven is infinite")
    return 365.0 * (np.asarray(bid_ask_bp, dtype=float) / 2.0) / c_bp_per_year


def carry_table(positions, kappa_rwa, kappa_lr, hurdle):
    """positions: DataFrame [bond_id, notional ($, signed), rw, holding_days]. Adds carry_bp, carry_usd."""
    need = {"bond_id", "notional", "rw", "holding_days"}
    missing = need - set(positions.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    out = positions.copy()
    out["carry_bp"] = regulatory_carry_bp(kappa_rwa, out["rw"], kappa_lr, hurdle, out["holding_days"])
    out["carry_usd"] = out["notional"].abs() * out["carry_bp"] / BP   # shorts pay rent too
    return out


# Sanity checks: the numerics table of 22.1.1
ust = regulatory_carry_bp(0.105, 0.0, 0.05, 0.12, 7)         # Treasury: RW 0, leverage binds
bbb = regulatory_carry_bp(0.105, 1.0, 0.05, 0.12, 7)         # corporate: risk-based binds
ust_2026 = regulatory_carry_bp(0.105, 0.0, 0.0375, 0.12, 7)  # 3% + half of a 1.5% surcharge
assert abs(ust - 1.1507) < 1e-3 and abs(bbb - 2.4164) < 1e-3 and abs(ust_2026 - 0.8630) < 1e-3
assert abs(breakeven_holding_days(1.0, 0.12, 0.05) - 3.042) < 1e-2                  # 2y UST, 1bp wide
assert abs(breakeven_holding_days(1.0, 0.12, 0.0375) - 4.056) < 1e-2
assert abs(breakeven_holding_days(25.0, 0.12, 0.05, 0.105, 1.0) - 36.21) < 1e-1     # BBB, a quarter wide

book = pd.DataFrame({"bond_id": ["UST_2Y_OTR", "BBB_IND_2033", "BBB_IND_2033_SHORT"],
                     "notional": [1e8, 15e6, -15e6], "rw": [0.0, 1.0, 1.0], "holding_days": [7, 7, 7]})
tab = carry_table(book, kappa_rwa=0.105, kappa_lr=0.05, hurdle=0.12)
assert tab["carry_usd"].iloc[1] == tab["carry_usd"].iloc[2]      # |q|, not q
assert abs(tab["carry_usd"].iloc[0] - 11507.0) < 5.0              # $100mm of 2y, one week
try:
    regulatory_carry_bp(10.5, 1.0, 5.0, 0.12, 7)                   # percent instead of decimals
    raise AssertionError("percent inputs must be rejected")
except ValueError:
    pass
```


### Listing 22.2: The zero-profit block half-spread and the TRACE regime layer {#code-22-2}

```python
def block_half_spread(lam, Q, delay, unwind_time, gamma, sigma, inferred_size=None):
    """Zero-profit block half-spread, bp of price (eq. 22.6). lam: bp per $mm the market infers;
    Q: true block size, $mm; delay, unwind_time: minutes; sigma: bp per sqrt(minute); gamma: per bp*$mm.
    inferred_size: what the market believes Q is (defaults to Q; use the censored mean above the cap)."""
    if Q <= 0 or unwind_time <= 0 or min(delay, lam, gamma, sigma) < 0:
        raise ValueError("need Q > 0, unwind_time > 0, and non-negative delay, lam, gamma, sigma")
    q_hat = Q if inferred_size is None else inferred_size
    leak = max(0.0, 1.0 - delay / unwind_time)                 # positive-part guard
    return lam * q_hat * leak + gamma * sigma**2 * Q * unwind_time / 6.0


def pareto_alpha_from_imputed_mean(cap, imputed_mean):
    """Tail index from the mean size above the cap (eq. 22.7): alpha = m / (m - 1), m = mean / cap."""
    m = imputed_mean / cap
    if m <= 1.0:
        raise ValueError("imputed mean must exceed the cap")
    return m / (m - 1.0)


def censored_impact(lam, cap, alpha):
    """Impact of any capped print: lam * alpha / (alpha - 1) * cap."""
    if alpha <= 1.0:
        raise ValueError("alpha must exceed 1 for a finite conditional mean")
    return lam * alpha / (alpha - 1.0) * cap


REGIME_DATES = {                      # New York calendar dates; imported by every later chapter
    "sbsr_public": "2022-02-14",
    "pt_modifier_live": "2023-05-15",
    "t_plus_1": "2024-05-28",
    "alloc_reports_live": "2026-06-08",
    "affiliate_ind_voluntary": "2026-08-31",
    "affiliate_ind_mandatory": "2027-08-02",
}
DISSEMINATION_CAP_MM = {"IG": 5.0, "HY": 1.0}


def trace_regime_flags(trades):
    """Add one boolean column per regime, plus size_capped and dup_risk. Rejects naive timestamps."""
    need = {"trade_dt", "bond_id", "size_mm", "side", "price", "rating_bucket"}
    missing = need - set(trades.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    if not isinstance(trades["trade_dt"].dtype, pd.DatetimeTZDtype):
        raise ValueError("trade_dt must be timezone-aware (America/New_York)")
    if not trades["rating_bucket"].isin(list(DISSEMINATION_CAP_MM)).all():
        raise ValueError("rating_bucket must be 'IG' or 'HY'")
    out = trades.copy()
    ny_date = out["trade_dt"].dt.tz_convert("America/New_York").dt.tz_localize(None).dt.normalize()
    for flag, d in REGIME_DATES.items():
        out[flag] = ny_date >= pd.Timestamp(d)
    out["one_minute_rule"] = False    # approved by the SEC in 2024, never effective: FINRA Notice 25-17
    out["size_capped"] = out["size_mm"] >= out["rating_bucket"].map(DISSEMINATION_CAP_MM)
    out["dup_risk"] = ~out["affiliate_ind_mandatory"]    # affiliate duplicates not reliably flagged yet
    return out


# Sanity checks
lam, gam, sig = 0.5, 0.001, 2.5
s15 = block_half_spread(lam, 15.0, 15.0, 120.0, gam, sig)
s1 = block_half_spread(lam, 15.0, 1.0, 120.0, gam, sig)
s48h = block_half_spread(lam, 15.0, 48 * 60.0, 120.0, gam, sig)
assert abs(s15 - 8.4375) < 1e-9 and abs(s1 - 9.3125) < 1e-9          # worked example, 22.2.1
assert abs(s48h - gam * sig**2 * 15.0 * 120.0 / 6.0) < 1e-12          # delay >= unwind: inventory only
path = [block_half_spread(lam, 15.0, d, 120.0, gam, sig) for d in np.linspace(0.0, 240.0, 49)]
assert np.all(np.diff(path) <= 1e-12)                                  # non-increasing in the delay

alpha_ig = pareto_alpha_from_imputed_mean(5.0, 12.5)                   # Ben Dor p.364 imputed caps
alpha_hy = pareto_alpha_from_imputed_mean(1.0, 4.0)
assert abs(alpha_ig - 5.0 / 3.0) < 1e-12 and abs(alpha_hy - 4.0 / 3.0) < 1e-12
assert abs(censored_impact(lam, 5.0, alpha_ig) - lam * 12.5) < 1e-12
rng = np.random.default_rng(22)
capped_ig = 5.0 * (1.0 + rng.pareto(alpha_ig, 200_000))               # classical Pareto above $5mm
assert abs(np.median(capped_ig) - 5.0 * 2.0 ** (1.0 / alpha_ig)) < 0.05   # median ~ $7.6mm, mean $12.5mm

trades = pd.DataFrame({
    "trade_dt": pd.to_datetime(["2023-05-12 15:41", "2023-05-15 09:30", "2023-05-16 10:05"])
                  .tz_localize("America/New_York"),
    "bond_id": ["BBB_IND_2033", "B2_PKG_2029", "BBB_IND_2033"],
    "size_mm": [2.0, 1.0, 5.0], "side": ["S", "B", "S"], "price": [97.25, 91.10, 96.90],
    "rating_bucket": ["IG", "HY", "IG"],
})
flags = trace_regime_flags(trades)
flag_cols = list(REGIME_DATES) + ["one_minute_rule"]
assert [c for c in flag_cols if flags[c].iloc[0] != flags[c].iloc[-1]] == ["pt_modifier_live"]
assert flags["size_capped"].tolist() == [False, True, True] and flags["dup_risk"].all()
try:
    trace_regime_flags(trades.assign(trade_dt=trades["trade_dt"].dt.tz_localize(None)))
    raise AssertionError("naive timestamps must be rejected")
except ValueError:
    pass
```


### Listing 22.3: The settlement clock: initial margin scaling and the cost of fails {#code-22-3}

```python
from math import erf, exp, pi, sqrt


def margin_ratio(t_old, t_new, closeout_days):
    """IM_new / IM_old = sqrt((t_new + closeout) / (t_old + closeout)) for the volatility component (eq. 22.8)."""
    if min(t_old, t_new, closeout_days) < 0 or t_old + closeout_days <= 0:
        raise ValueError("day counts must be non-negative and the old horizon positive")
    return sqrt((t_new + closeout_days) / (t_old + closeout_days))


def fail_cost_annual(r_ref, floor=0.03):
    """(total annual cost of failing, fails charge) per $1 of proceeds (eq. 22.9); decimals."""
    charge = max(0.0, floor - r_ref)
    return r_ref + charge, charge


assert abs(margin_ratio(2, 1, 0) - 0.70711) < 1e-5 and abs(margin_ratio(2, 1, 1) - 0.81650) < 1e-5
dtcc = {"snapshot": 9.1 / 12.8, "three_month_avg": 9.8 / 12.8}        # NSCC clearing fund, $bn (approx.)
assert all(margin_ratio(2, 1, 0) <= v <= margin_ratio(2, 1, 1) for v in dtcc.values())
assert fail_cost_annual(0.0) == (0.03, 0.03) and fail_cost_annual(0.045) == (0.045, 0.0)
assert margin_ratio(2, 1, 0) != 0.5                                      # ROBO's linear answer
```


### Listing 22.4: The Treasury clearing mandate: netting factor, net benefit and capacity hinge {#code-22-4}

```python
def folded_normal_mean(m, s=1.0):
    """E|m + s Z| for standard normal Z (eq. 22.11)."""
    return s * sqrt(2.0 / pi) * exp(-m * m / (2.0 * s * s)) + m * erf(m / (s * sqrt(2.0)))


def netting_factor_mc(n_dealers, n_sims, seed, common_component=0.0, scale=1.0):
    if n_dealers < 2 or n_sims < 1000 or scale <= 0:
        raise ValueError("need n_dealers >= 2, n_sims >= 1000, scale > 0")
    rng = np.random.default_rng(seed)
    x = common_component + scale * rng.standard_normal((n_sims, n_dealers - 1))
    mc = np.abs(x.sum(axis=1)).mean() / np.abs(x).sum(axis=1).mean()
    m = abs(common_component)
    return {"mc": float(mc), "theory": 1.0 / sqrt(n_dealers - 1),
            "directional_floor": m / folded_normal_mean(m, scale)}


def implied_common_component(phi_target, scale=1.0, lo=1e-9, hi=50.0, tol=1e-12):
    """Directional component m at which the large-N floor equals phi_target (bisection; floor rises in m)."""
    if not 0.0 < phi_target < 1.0:
        raise ValueError("phi_target must lie in (0, 1)")
    f = lambda m: m / folded_normal_mean(m, scale) - phi_target
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if f(lo) * f(mid) <= 0 else (mid, hi)
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def mandate_net_benefit(gross, phi, kappa_lr, hurdle, im, funding_spread, default_fund_cost=0.0):
    """Left minus right side of eq. 22.12, per year, in the units of gross (e.g. $bn)."""
    if not 0.0 <= phi <= 1.0:
        raise ValueError("phi must lie in [0, 1]")
    return (1.0 - phi) * gross * kappa_lr * hurdle - (im * funding_spread + default_fund_cost)


def capacity_hinge(u_lo=0.4, u_hi=0.8, delta_sd=3.0, u_mid=0.6, level_sd=2.0):
    """Calibrate c and U* in eq. 22.13 from two statements in Duffie et al. (2023)."""
    c = delta_sd / (u_hi - u_lo)            # valid only if the kink lies below u_lo
    u_star = u_mid - level_sd / c
    if u_star > u_lo:
        raise ValueError("kink above u_lo: the two-point calibration is invalid")
    return c, u_star


nf = netting_factor_mc(25, 20_000, seed=7)
assert abs(nf["theory"] - 0.2041) < 1e-4 and abs(nf["mc"] / nf["theory"] - 1.0) < 0.02
nd = netting_factor_mc(25, 20_000, seed=7, common_component=1.0)
assert abs(nd["directional_floor"] - 0.857) < 1e-3 and abs(nd["mc"] - nd["directional_floor"]) < 0.01
m_implied = implied_common_component(1.0 - 1.14 / 2.48)                 # DTCC sponsored figures (approx.)
assert 0.4 < m_implied < 0.6
calm = mandate_net_benefit(100.0, 0.54, 0.05, 0.12, im=2.0, funding_spread=0.005, default_fund_cost=0.02)
one_way = mandate_net_benefit(100.0, 0.857, 0.05, 0.12, im=4.0, funding_spread=0.01, default_fund_cost=0.02)
assert calm > one_way                                                     # netting fades, IM rises
c_h, u_star = capacity_hinge()
assert abs(c_h - 7.5) < 1e-12 and abs(u_star - 1.0 / 3.0) < 1e-12
assert abs(c_h * max(0.96 - u_star, 0.0) - 4.70) < 0.01                  # 2020-03-12, excess over volatility
```


### Listing 22.5: A difference-in-differences event study with placebo dates {#code-22-5}

```python
def event_study_did(panel, event_date, window=(-60, 60), n_boot=500, seed=0,
                    treated_col="treated", y_col="y"):
    """Difference-in-differences around an effective date (eq. 22.17), cluster bootstrap by bond."""
    need = {"date", "bond_id", treated_col, y_col}
    missing = need - set(panel.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    t0 = np.datetime64(pd.Timestamp(event_date).date())
    rel = np.busday_count(t0, panel["date"].to_numpy().astype("datetime64[D]"))
    keep = (rel >= window[0]) & (rel <= window[1])
    df = panel.loc[keep, ["bond_id", treated_col, y_col]].copy()
    df["post"] = rel[keep] >= 0                                   # event day counts as post
    cell = df.groupby(["bond_id", treated_col, "post"])[y_col].mean().unstack("post")
    if False not in cell.columns or True not in cell.columns:
        raise ValueError("the window must contain pre and post observations")
    cell = cell.dropna()                                          # bonds seen on both sides only
    d = (cell[True] - cell[False]).to_numpy()
    tmask = cell.index.get_level_values(treated_col).to_numpy(dtype=bool)
    d_t, d_c = d[tmask], d[~tmask]
    if d_t.size < 2 or d_c.size < 2:
        raise ValueError("need at least two treated and two control bonds")
    rng = np.random.default_rng(seed)
    boots = np.array([rng.choice(d_t, d_t.size).mean() - rng.choice(d_c, d_c.size).mean()
                      for _ in range(n_boot)])
    table = pd.DataFrame({"pre": [cell[False][tmask].mean(), cell[False][~tmask].mean()],
                          "post": [cell[True][tmask].mean(), cell[True][~tmask].mean()]},
                         index=["treated", "control"])
    table["change"] = table["post"] - table["pre"]
    return {"table": table, "did": float(d_t.mean() - d_c.mean()), "se": float(boots.std(ddof=1)),
            "n_treated": int(d_t.size), "n_control": int(d_c.size)}


def placebo(panel, dates, **kwargs):
    """DiD estimate on each fake effective date; all should be near zero."""
    return pd.Series({pd.Timestamp(d): event_study_did(panel, d, **kwargs)["did"] for d in dates})


# Synthetic PT-modifier panel: +2bp on treated bonds from 2023-05-15, and a concurrent
# market-wide improvement of 3bp (the post-March-2023 healing) that a naive study would misread.
rng = np.random.default_rng(2023)
dates = pd.bdate_range("2022-10-03", "2023-09-29")
n_t = n_c = 40
ids = np.array([f"T{i:02d}" for i in range(n_t)] + [f"C{i:02d}" for i in range(n_c)])
is_t = np.r_[np.ones(n_t, dtype=bool), np.zeros(n_c, dtype=bool)]
post = np.asarray(dates >= pd.Timestamp("2023-05-15"))
fe = rng.normal(0.0, 20.0, ids.size)                                # bond-level cost, bp
market = np.cumsum(rng.normal(0.0, 0.05, dates.size)) - 3.0 * post  # market-wide cost, bp
y = (fe[None, :] + market[:, None] + rng.normal(0.0, 1.0, (dates.size, ids.size))
     + 2.0 * (post[:, None] & is_t[None, :]))
panel = pd.DataFrame({"date": np.repeat(dates.to_numpy(), ids.size), "bond_id": np.tile(ids, dates.size),
                      "treated": np.tile(is_t, dates.size), "y": y.ravel()})

res = event_study_did(panel, "2023-05-15", window=(-60, 60), n_boot=400, seed=1)
assert abs(res["did"] - 2.0) < max(4.0 * res["se"], 0.1) and res["se"] < 0.2
naive = res["table"].loc["treated", "change"]                       # before-after, no control group
assert naive < 0.0 < res["did"]                                     # naive says costs fell; they rose
plac = placebo(panel, ["2023-01-17", "2023-02-15"], window=(-40, 40), n_boot=200, seed=2)
assert (plac.abs() < 0.25).all()                                    # nothing happened on fake dates
```


## F.23: Chapter 23: Cross-Asset Convexity & the Volatility Surface {#code-23}

Listings from `23_ch23_cross_asset_convexity_and_vol_surface.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 23.1: Equity as a call on assets: Merton and CreditGrades {#code-23-1}

```python
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import brentq, fsolve, least_squares

RNG_SEED = 23

# ---------- Merton (1974): the identity behind the whole chapter ----------
def merton_equity(V, F, r, sigma_V, T):
    """Equity as a call on assets. Returns (E, d1, d2)."""
    srt = sigma_V * np.sqrt(T)
    d1 = np.clip((np.log(V / F) + (r + 0.5 * sigma_V**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    E = V * norm.cdf(d1) - F * np.exp(-r * T) * norm.cdf(d2)
    return E, d1, d2

def merton_equity_vol(V, F, r, sigma_V, T):
    """Eq. (23.1): sigma_E = sigma_V * V * N(d1) / E."""
    E, d1, _ = merton_equity(V, F, r, sigma_V, T)
    return sigma_V * V * norm.cdf(d1) / E

def merton_spread(V, F, r, sigma_V, T):
    """Eq. (23.2): model credit spread, decimal, continuously compounded."""
    _, d1, d2 = merton_equity(V, F, r, sigma_V, T)
    return -np.log(norm.cdf(d2) + V / (F * np.exp(-r * T)) * norm.cdf(-d1)) / T

def merton_solve_V_sigma(E, sigma_E, F, r, T):
    """Invert (E, sigma_E) -> (V, sigma_V); same contract as the Chapter 6 solver."""
    def eqs(x):
        V, sV = np.exp(x[0]), np.exp(x[1])          # log-parametrized: stays positive
        Em, d1, _ = merton_equity(V, F, r, sV, T)
        return [Em / E - 1.0, sV * V * norm.cdf(d1) / (sigma_E * E) - 1.0]
    V0 = E + F * np.exp(-r * T)
    x0 = [np.log(V0), np.log(sigma_E * E / V0)]
    sol, info, ier, msg = fsolve(eqs, x0, full_output=True, xtol=1e-12)
    if ier != 1:
        raise RuntimeError(f"Merton inversion failed: {msg}")
    return float(np.exp(sol[0])), float(np.exp(sol[1]))

# ---------- CreditGrades (Finger et al. 2002) in book notation ----------
# CG's lambda (barrier dispersion) -> nu ; CG's L-bar -> ell_bar ; CG's D -> F_ps.
def cg_asset_state(S0, sigma_E, F_ps, ell_bar=0.5):
    """Eq. (23.4): V0 = S0 + ell_bar*F_ps and sigma_V = sigma_E*S0/V0."""
    S0 = np.asarray(S0, dtype=float)
    if np.any(S0 <= 0) or np.any(np.asarray(sigma_E) <= 0):
        raise ValueError("S0 and sigma_E must be positive")
    if np.any(np.asarray(F_ps) <= 0):
        raise ValueError("F_ps must be positive: no debt, no CDS, no chapter")
    V0 = S0 + ell_bar * F_ps
    return V0, sigma_E * S0 / V0

def cg_survival(t, S0, sigma_E, F_ps, ell_bar=0.5, nu=0.3):
    """Eq. (23.3): CreditGrades survival curve; broadcasts over t and S0."""
    t = np.asarray(t, dtype=float)
    V0, sigma_V = cg_asset_state(S0, sigma_E, F_ps, ell_bar)
    log_d = np.log(V0 / (ell_bar * F_ps)) + nu**2
    Sig = np.maximum(np.sqrt(sigma_V**2 * t + nu**2), 1e-12)
    first = norm.cdf(-Sig / 2 + log_d / Sig)
    second = np.exp(log_d + norm.logcdf(-Sig / 2 - log_d / Sig))    # d * N(.), in logs
    return first - second

def cg_cds_spread(T, S0, sigma_E, F_ps, R=0.4, r=0.03, ell_bar=0.5, nu=0.3, dt=1/12):
    """Eq. (23.5) by direct integration of both legs; includes CG's time-zero mass.
    S0 may be a scalar (returns float) or a 1-D array (returns array)."""
    S0_arr = np.atleast_1d(np.asarray(S0, dtype=float))[:, None]
    n = max(int(round(T / dt)), 1)
    t = np.linspace(0.0, T, n + 1)[None, :]
    surv = cg_survival(t, S0_arr, sigma_E, F_ps, ell_bar, nu)
    h = np.diff(t, axis=1)
    rpv01 = np.sum(h * np.exp(-r * t[:, 1:]) * 0.5 * (surv[:, :-1] + surv[:, 1:]), axis=1)
    t_mid = 0.5 * (t[:, :-1] + t[:, 1:])
    prot = (1 - R) * ((1 - surv[:, 0])
                      + np.sum(np.exp(-r * t_mid) * (surv[:, :-1] - surv[:, 1:]), axis=1))
    s = prot / rpv01
    return float(s[0]) if np.ndim(S0) == 0 else s

def cg_implied_vol(spread_mkt, T, S0, F_ps, R=0.4, r=0.03, ell_bar=0.5, nu=0.3, lo=0.02, hi=5.0):
    """Invert a market CDS spread for (sigma_E, sigma_V); (nan, nan) outside the model's range."""
    f = lambda v: cg_cds_spread(T, S0, v, F_ps, R, r, ell_bar, nu) - spread_mkt
    if f(lo) > 0 or f(hi) < 0:
        return np.nan, np.nan            # below the low-vol floor, or beyond any vol
    sE = brentq(f, lo, hi, xtol=1e-12)
    return sE, sE * S0 / (S0 + ell_bar * F_ps)

def cg_survival_mc(t, S0, sigma_E, F_ps, ell_bar=0.5, nu=0.3,
                   n_paths=100_000, steps_per_year=252, seed=RNG_SEED):
    """Monte Carlo of the time-shifted Brownian motion that Eq. (23.3) is exact for,
    with a Brownian-bridge correction for barrier touches between grid dates."""
    rng = np.random.default_rng(seed)
    V0, sigma_V = cg_asset_state(S0, sigma_E, F_ps, ell_bar)
    V0, sigma_V = float(V0), float(sigma_V)
    xi = nu**2 / sigma_V**2                         # process 'started' at time -xi
    y = np.log(ell_bar * F_ps / V0) - nu**2         # barrier for X (negative)
    a, b = -0.5 * sigma_V**2, sigma_V
    horizon = t + xi
    n = int(np.ceil(horizon * steps_per_year))
    dt = horizon / n
    x = np.zeros(n_paths)
    alive = np.ones(n_paths, dtype=bool)
    for _ in range(n):
        x_new = x + a * dt + b * np.sqrt(dt) * rng.standard_normal(n_paths)
        gap0, gap1 = np.maximum(x - y, 0.0), np.maximum(x_new - y, 0.0)
        p_touch = np.exp(-2.0 * gap0 * gap1 / (b * b * dt))
        alive &= ~((x_new <= y) | (rng.random(n_paths) < p_touch))
        x = x_new
    p = alive.mean()
    return p, np.sqrt(p * (1 - p) / n_paths)

# ---------- sanity checks, block 1 ----------
# (a0) Merton round trip, and the leverage skew of Eq. (23.1)
V_true, sV_true, F_m, r_m, T1 = 100.0, 0.25, 70.0, 0.03, 1.0
E0, _, _ = merton_equity(V_true, F_m, r_m, sV_true, T1)
sE0 = merton_equity_vol(V_true, F_m, r_m, sV_true, T1)
V_hat, sV_hat = merton_solve_V_sigma(float(E0), float(sE0), F_m, r_m, T1)
assert abs(V_hat - V_true) < 1e-5 and abs(sV_hat - sV_true) < 1e-6
V_grid = np.array([75.0, 100.0, 150.0])
sig_E_grid = np.array([merton_equity_vol(v, F_m, r_m, sV_true, T1) for v in V_grid])
assert np.all(np.diff(sig_E_grid) < 0), "equity vol must fall as assets (and the stock) rise"
print("Merton sigma_E at V = 75, 100, 150:", np.round(sig_E_grid, 3))
print("Merton 1y spread at V = 100 (bp):", round(1e4 * float(merton_spread(V_true, F_m, r_m, sV_true, T1)), 1))

# (a) CG survival is non-increasing, and Eq. (23.3) matches Monte Carlo of its own process
S_ex, sE_ex, F_ex = 30.0, 0.40, 30.0
surv_curve = cg_survival(np.linspace(0.01, 10.0, 400), S_ex, sE_ex, F_ex)
assert np.all(np.diff(surv_curve) <= 1e-14)
p_cf = float(cg_survival(2.0, S_ex, sE_ex, F_ex))
p_mc, se_mc = cg_survival_mc(2.0, S_ex, sE_ex, F_ex)
assert abs(p_cf - p_mc) < 4 * se_mc, (p_cf, p_mc, se_mc)
print(f"CG 2y survival: closed form {p_cf:.5f}, MC {p_mc:.5f} +/- {se_mc:.5f}  PASS")
print("time-zero ghost 1 - S(0):  S0=30 ->", round(1 - float(cg_survival(0.0, 30.0, 0.4, 30.0)), 6),
      "  S0=5 ->", round(1 - float(cg_survival(0.0, 5.0, 0.4, 30.0)), 3))

# (b) leg integration vs. the average hazard (R = ell_bar, r = 0, a safer name)
T5 = 5.0
s_b = cg_cds_spread(T5, 50.0, 0.30, 30.0, R=0.5, r=0.0)
h_bar = -np.log(float(cg_survival(T5, 50.0, 0.30, 30.0))) / T5
assert abs(s_b / ((1 - 0.5) * h_bar) - 1) < 0.05

# (b2) the implied-vol inverter round-trips, and refuses quotes below the floor
s_mkt = cg_cds_spread(T5, 30.0, 0.45, 30.0)
sE_imp, sV_imp = cg_implied_vol(s_mkt, T5, 30.0, 30.0)
assert abs(sE_imp - 0.45) < 1e-6
assert np.isnan(cg_implied_vol(1e-6, T5, 30.0, 30.0)[0])
print(f"5y CG spread at sigma_E = 45%: {1e4 * s_mkt:.0f}bp; implied asset vol {sV_imp:.3f}  PASS")
```


### Listing 23.2: The jump-to-default put and the unit recovery claim from a put chain {#code-23-2}

```python
# ---------- block 2: Carr-Wu claims and the jump-to-default put ----------
def bs_put(S0, K, T, r, q, sigma):
    """Textbook Black-Scholes put (independent reference for the lam = 0 check)."""
    d1 = (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp(-q * T) * norm.cdf(-d1)

def jtd_put_price(S0, K, T, r, q, sigma, lam):
    """Eq. (23.8): European put when the stock diffuses at sigma and jumps to zero at rate lam (Q)."""
    K = np.asarray(K, dtype=float)
    srt = sigma * np.sqrt(T)
    d1 = np.clip((np.log(S0 / K) + (r - q + lam + 0.5 * sigma**2) * T) / srt, -40, 40)
    d2 = d1 - srt
    pays_K = -np.expm1(-lam * T) + np.exp(-lam * T) * norm.cdf(-d2)   # = 1 - e^{-lam T} N(d2), stably
    return K * np.exp(-r * T) * pays_K - S0 * np.exp(-q * T) * norm.cdf(-d1)

def bs_implied_vol_put(price, S0, K, T, r, q):
    return brentq(lambda v: float(bs_put(S0, K, T, r, q, v)) - price, 1e-4, 5.0, xtol=1e-12)

def make_put_chain(S0, strikes, T, r, q, sigma, lam, half_spread=0.0, american=False):
    mid = jtd_put_price(S0, strikes, T, r, q, sigma, lam)
    return pd.DataFrame({"T": T, "K": np.asarray(strikes, dtype=float), "cp": "P",
                         "bid": mid * (1 - half_spread), "ask": mid * (1 + half_spread),
                         "american": american})

def urc_from_puts(chain, T, A, B):
    """Eq. (23.6): unit recovery claim from a put spread struck inside the default corridor.
    Returns (U_bid, U_ask, convention)."""
    puts = chain[(chain["cp"] == "P") & np.isclose(chain["T"], T)].sort_values("K")
    if puts.empty:
        raise ValueError("no puts at this expiry")
    K = puts["K"].to_numpy()
    if not (0.0 <= A < B) or B > K.max() or (A > 0 and A < K.min()):
        raise ValueError("need 0 <= A < B inside the listed strikes; never extrapolate")
    bid = lambda k: float(np.interp(k, K, puts["bid"].to_numpy()))
    ask = lambda k: float(np.interp(k, K, puts["ask"].to_numpy()))
    if A == 0.0:
        U_bid, U_ask = bid(B) / B, ask(B) / B
    else:
        U_bid = (bid(B) - ask(A)) / (B - A)      # sell the spread: hit B's bid, lift A's offer
        U_ask = (ask(B) - bid(A)) / (B - A)
    convention = "at_default" if bool(puts["american"].all()) else "at_expiry"
    return U_bid, U_ask, convention

def urc_from_cds(spread, R, r, T, payment="at_default"):
    """Eq. (23.7): the same claim implied by a flat-hazard CDS (lam = s / (1 - R))."""
    lam = spread / (1.0 - R)
    if payment == "at_default":
        return lam / (r + lam) * (-np.expm1(-(r + lam) * T))
    if payment == "at_expiry":
        return np.exp(-r * T) * (-np.expm1(-lam * T))
    raise ValueError("payment must be 'at_default' or 'at_expiry'")

def jtd_fit(chain, S0, T, r, q, x0=(0.3, 0.02)):
    """Fit (sigma, lam) jointly on mid P(K)/K: low strikes pin lam, the money pins sigma."""
    puts = chain[(chain["cp"] == "P") & np.isclose(chain["T"], T)]
    K = puts["K"].to_numpy()
    mid = (0.5 * (puts["bid"] + puts["ask"])).to_numpy()
    resid = lambda x: jtd_put_price(S0, K, T, r, q, x[0], x[1]) / K - mid / K
    fit = least_squares(resid, x0, bounds=([1e-3, 0.0], [3.0, 3.0]),
                        xtol=1e-12, ftol=1e-12, gtol=1e-12)
    sig_hat, lam_hat = fit.x
    i_min = int(np.argmin(K))
    floor_ratio = ((mid[i_min] / K[i_min]) / (np.exp(-r * T) * -np.expm1(-lam_hat * T))
                   if lam_hat > 0 else np.inf)
    return {"sigma": float(sig_hat), "lam": float(lam_hat), "floor_ratio": float(floor_ratio)}

# ---------- sanity checks, block 2 ----------
S0p, Tp, rp, qp = 100.0, 1.0, 0.03, 0.0
lam_true, sig_true, R_cds = 0.05, 0.30, 0.40
# (c) lam = 0 is Black-Scholes; the deep-OTM floor is the hazard
assert abs(float(jtd_put_price(100.0, 90.0, 1.0, 0.03, 0.01, 0.3, 0.0))
           - float(bs_put(100.0, 90.0, 1.0, 0.03, 0.01, 0.3))) < 1e-10
K_low = 0.05 * S0p
floor = float(jtd_put_price(S0p, K_low, Tp, rp, qp, sig_true, lam_true)) / K_low
assert abs(floor / (np.exp(-rp * Tp) * -np.expm1(-lam_true * Tp)) - 1) < 0.01
# the skew: Black-Scholes implied vol of jump-to-default prices falls with strike
K_skew = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
iv = np.array([bs_implied_vol_put(float(jtd_put_price(S0p, k, Tp, rp, qp, sig_true, lam_true)),
                                  S0p, k, Tp, rp, qp) for k in K_skew])
assert np.all(np.diff(iv) < 0)
print("JTD implied vols by strike:", dict(zip(K_skew.tolist(), np.round(iv, 3).tolist())))
# (d) Carr-Wu on a synthetic European chain equals the CDS claim with matching payment timing
strikes = np.arange(10.0, 155.0, 5.0)
chain = make_put_chain(S0p, strikes, Tp, rp, qp, sig_true, lam_true)
U_bid, U_ask, conv = urc_from_puts(chain, Tp, 0.0, 0.2 * S0p)
U_cds = urc_from_cds(lam_true * (1 - R_cds), R_cds, rp, Tp, payment=conv)
assert conv == "at_expiry" and abs(0.5 * (U_bid + U_ask) - U_cds) < 5e-5
gap = urc_from_cds(lam_true * (1 - R_cds), R_cds, rp, Tp, "at_default") - U_cds
print(f"URC from puts {U_bid:.5f}, from CDS {U_cds:.5f}; American-minus-European {gap:.5f}  PASS")
# the fit recovers the hazard; a pure diffusion has no floor
chain2 = make_put_chain(S0p, strikes, Tp, rp, 0.01, 0.35, 0.08)
fit = jtd_fit(chain2, S0p, Tp, rp, 0.01)
assert abs(fit["lam"] - 0.08) < 1e-4 and abs(fit["sigma"] - 0.35) < 1e-4
assert abs(fit["floor_ratio"] - 1) < 0.01
assert float(bs_put(S0p, 10.0, Tp, rp, qp, 0.35)) / 10.0 < 1e-6
print(f"fitted lam {fit['lam']:.4f}, sigma {fit['sigma']:.4f}, floor ratio {fit['floor_ratio']:.4f}  PASS")
```


### Listing 23.3: Spread Greeks for CDS, bonds, Merton and CreditGrades {#code-23-3}

```python
# ---------- block 3: Greeks in spread terms ----------
def cds_rpv01(s, R=0.4, r=0.03, T=5.0):
    lam = np.asarray(s, dtype=float) / (1.0 - R)
    return -np.expm1(-(r + lam) * T) / (r + lam)

def cds_mtm_buyer(s, c, R=0.4, r=0.03, T=5.0):
    """MTM per unit notional of bought protection, running coupon c, market spread s."""
    return (s - c) * cds_rpv01(s, R, r, T)

def bond_price_flat(s, cpn=0.06, T=5.0, r=0.03, freq=2):
    t = np.arange(1, int(round(T * freq)) + 1) / freq
    cf = np.full(t.shape, cpn / freq)
    cf[-1] += 1.0
    return float(np.sum(cf * np.exp(-(r + s) * t)))

def spread_greeks(price_fn, s, bump_bp=1.0):
    """Eq. (23.9) by central differences: spread duration, convexity, CS01, DTS."""
    h = bump_bp * 1e-4
    p0, pu, pd = price_fn(s), price_fn(s + h), price_fn(s - h)
    D = -(pu - pd) / (2 * h * p0)
    C = (pu - 2 * p0 + pd) / (h * h * p0)
    return {"price": p0, "D_spr": D, "convexity": C, "cs01": D * p0 * 1e-4, "dts": D * s}

def merton_elasticity(V, F, r, sigma_V, T):
    """Eq. (23.10): % bond move per % equity move."""
    E, d1, _ = merton_equity(V, F, r, sigma_V, T)
    return float(norm.cdf(-d1) / norm.cdf(d1) * E / (V - E))

def cg_greeks(S0, sigma_E, F_ps, R=0.4, r=0.03, T=5.0, ell_bar=0.5, nu=0.3, notional=1e7):
    """Greeks of BOUGHT protection per `notional`, coupon struck at today's model spread."""
    s0 = cg_cds_spread(T, S0, sigma_E, F_ps, R, r, ell_bar, nu)
    def mtm(S, sE=sigma_E):
        s = cg_cds_spread(T, S, sE, F_ps, R, r, ell_bar, nu)
        return notional * float(cds_mtm_buyer(s, s0, R, r, T))
    h = 0.01 * S0
    m0, mu, md = mtm(S0), mtm(S0 + h), mtm(S0 - h)
    vega_E = 0.5 * (mtm(S0, sigma_E + 0.01) - mtm(S0, sigma_E - 0.01))   # per 1 vol pt of sigma_E
    V0 = S0 + ell_bar * F_ps
    return {"spread_bp": 1e4 * s0,
            "delta_shares": -(mu - md) / (2 * h),   # shares to BUY against bought protection
            "gamma": (mu - 2 * m0 + md) / h**2,     # stock-space convexity, $ per $^2
            "vega_equity": vega_E,
            "vega_asset": vega_E * V0 / S0}         # per 1 vol pt of sigma_V, via Eq. (23.4)

# ---------- sanity checks, block 3 ----------
s_hy = 0.035
g = spread_greeks(lambda s: bond_price_flat(s), s_hy)
ds = 0.005
actual = bond_price_flat(s_hy + ds) / g["price"] - 1
approx = -g["D_spr"] * ds + 0.5 * g["convexity"] * ds**2
assert abs(actual - approx) < 2e-5, "duration-convexity should explain a 50bp move"
hs = 1e-4
gam_cds = (float(cds_mtm_buyer(0.03 + hs, 0.03)) - 2 * float(cds_mtm_buyer(0.03, 0.03))
           + float(cds_mtm_buyer(0.03 - hs, 0.03))) / hs**2
assert gam_cds < 0, "bought protection is short spread convexity"
el = merton_elasticity(100.0, 70.0, 0.03, 0.25, 1.0)
assert 0 < el < 1
gk30, gk15 = cg_greeks(30.0, 0.40, 30.0), cg_greeks(15.0, 0.40, 30.0)
assert gk15["delta_shares"] > gk30["delta_shares"] > 0, "hedge ratio rises as the stock falls"
print(f"bond D_spr {g['D_spr']:.3f}, DTS {g['dts']:.3f}; CDS spread gamma {gam_cds:.2f}; "
      f"Merton elasticity {el:.4f}")
print(f"CG per $10mm: S=30 -> {gk30['spread_bp']:.0f}bp, {gk30['delta_shares']:,.0f} sh; "
      f"S=15 -> {gk15['spread_bp']:.0f}bp, {gk15['delta_shares']:,.0f} sh  PASS")
```


### Listing 23.4: Capital-structure arbitrage on a synthetic CreditGrades panel {#code-23-4}

```python
# ---------- block 4: Yu-style capital-structure arbitrage on a synthetic panel ----------
def simulate_cg_panel(n_issuers=20, n_days=500, T=5.0, R=0.4, r=0.03, seed=RNG_SEED):
    """GBM equity paths (no defaults) and CreditGrades model spreads with stock-space slopes."""
    rng = np.random.default_rng(seed)
    dt = 1 / 252
    frames = []
    for i in range(n_issuers):
        S0, sE, F_ps = rng.uniform(15, 60), rng.uniform(0.25, 0.60), rng.uniform(10, 60)
        steps = -0.5 * sE**2 * dt + sE * np.sqrt(dt) * rng.standard_normal(n_days - 1)
        S = S0 * np.exp(np.concatenate([[0.0], np.cumsum(steps)]))
        s_mod = cg_cds_spread(T, S, sE, F_ps, R, r)
        ds_dS = (cg_cds_spread(T, 1.01 * S, sE, F_ps, R, r)
                 - cg_cds_spread(T, 0.99 * S, sE, F_ps, R, r)) / (0.02 * S)
        frames.append(pd.DataFrame({"issuer": i, "day": np.arange(n_days), "S": S, "sigma_E": sE,
                                    "F_ps": F_ps, "s_model": s_mod, "ds_dS": ds_dS}))
    return pd.concat(frames, ignore_index=True)

def add_market_noise(panel, phi, sd_u=0.30, seed=RNG_SEED):
    """s_mkt = s_model * exp(u), u an AR(1) with persistence phi and stationary sd sd_u."""
    rng = np.random.default_rng(seed)
    u_all = []
    for _, g in panel.groupby("issuer", sort=True):
        eta = rng.standard_normal(len(g))
        u = np.empty(len(g))
        u[0] = sd_u * eta[0]
        for t in range(1, len(g)):
            u[t] = phi * u[t - 1] + sd_u * np.sqrt(1 - phi**2) * eta[t]
        u_all.append(u)
    out = panel.copy()
    out["s_mkt"] = out["s_model"] * np.exp(np.concatenate(u_all))
    return out

def capstruct_backtest(panel, alpha=0.5, eps=0.1, hold_max_days=180,
                       cost_bp_cds=5.0, cost_bp_eq=10.0, R=0.4, r=0.03, T=5.0):
    """Eq. (23.11) rules. pos = +1 sold protection (short stock hedge), -1 bought (long stock)."""
    n_days = int(panel["day"].max()) + 1
    pnl, carry, trades = np.zeros(n_days), np.zeros(n_days), []
    for iss, g in panel.groupby("issuer", sort=True):
        S, sm, smod = g["S"].to_numpy(), g["s_mkt"].to_numpy(), g["s_model"].to_numpy()
        dsdS_mkt = g["ds_dS"].to_numpy() * sm / smod          # market-spread slope in the stock
        z = sm / smod - 1.0
        pos, c, hedge, mtm_prev, t0, trade_pnl = 0, 0.0, 0.0, 0.0, 0, 0.0
        for t in range(n_days):
            exited = False
            if pos != 0:
                rpv = float(cds_rpv01(sm[t], R, r, T))
                mtm = pos * (c - sm[t]) * rpv
                step = (mtm - mtm_prev) + hedge * (S[t] - S[t - 1])
                mtm_prev = mtm
                carry[t] += pos * c / 252                          # reported, not in pnl
                closing = abs(z[t]) < eps or (t - t0) >= hold_max_days or t == n_days - 1
                if closing:
                    step -= cost_bp_cds * 1e-4 * rpv + abs(hedge) * S[t] * cost_bp_eq * 1e-4
                else:
                    new_hedge = pos * rpv * dsdS_mkt[t]
                    step -= abs(new_hedge - hedge) * S[t] * cost_bp_eq * 1e-4
                    hedge = new_hedge
                pnl[t] += step
                trade_pnl += step
                if closing:
                    trades.append({"issuer": iss, "entry": t0, "exit": t, "side": pos, "pnl": trade_pnl})
                    pos, hedge, exited = 0, 0.0, True
            if pos == 0 and not exited and abs(z[t]) > alpha and t < n_days - 1:
                pos = 1 if z[t] > 0 else -1
                rpv = float(cds_rpv01(sm[t], R, r, T))
                c, mtm_prev, t0 = sm[t], 0.0, t
                hedge = pos * rpv * dsdS_mkt[t]
                entry_cost = cost_bp_cds * 1e-4 * rpv + abs(hedge) * S[t] * cost_bp_eq * 1e-4
                pnl[t] -= entry_cost
                trade_pnl = -entry_cost
    daily = pd.Series(pnl, name="pnl")
    sd = float(daily.std())
    tr = pd.DataFrame(trades)
    return {"sharpe": float(np.sqrt(252) * daily.mean() / sd) if sd > 0 else 0.0,
            "n_trades": len(tr),
            "hit_rate": float((tr["pnl"] > 0).mean()) if len(tr) else float("nan"),
            "carry_total": float(carry.sum()), "daily": daily, "trades": tr}

# ---------- sanity checks, block 4 ----------
# (e) a delta-hedged protection seller is not JTD-hedged: at default the short stock covers little
jtd_gap = -(1 - 0.4) * 1e7 + gk30["delta_shares"] * 30.0
assert jtd_gap < -0.7 * (1 - 0.4) * 1e7
print(f"JTD on $10mm sold protection, delta-hedged at S=30: {jtd_gap:,.0f} USD")
# (f) the Kapadia-Pu lesson: convergence Sharpe falls as mispricings become persistent
panel = simulate_cg_panel()
bt = {}
for phi in (0.90, 0.98, 0.995):
    bt[phi] = capstruct_backtest(add_market_noise(panel, phi))
    print(f"phi={phi}: Sharpe {bt[phi]['sharpe']:.2f}, trades {bt[phi]['n_trades']}, "
          f"hit rate {bt[phi]['hit_rate']:.2f}, carry (excluded) {bt[phi]['carry_total']:.3f}")
assert bt[0.90]["sharpe"] > 0
assert bt[0.90]["sharpe"] > bt[0.995]["sharpe"], "persistence should erode convergence Sharpe"
```


### Listing 23.5: A bank-run liquidity default against a Merton PD {#code-23-5}

```python
# ---------- block 5: illustrative bank-run default vs. a Merton PD ----------
def bank_run_dd(cash, securities, haircut, max_monetize_per_day, uninsured, kappa, rho, equity_rets):
    """Liquidity default day under a run whose outflow rate rises with equity losses (kappa)
    and with cumulative outflows (rho, the panic feedback). All amounts in $bn; illustrative."""
    dep_u, liquid, sec = float(uninsured), float(cash), float(securities)
    path = []
    for day, ret in enumerate(equity_rets, start=1):
        rate = min(1.0, kappa * max(0.0, -ret) + rho * (1.0 - dep_u / uninsured))
        outflow = rate * dep_u
        raised = min(sec * (1.0 - haircut), max_monetize_per_day)
        sec -= raised / (1.0 - haircut)
        liquid += raised
        path.append({"day": day, "outflow": outflow, "liquidity": liquid})
        if outflow > liquid:
            return {"default_day": day, "path": pd.DataFrame(path)}
        liquid -= outflow
        dep_u -= outflow
    return {"default_day": None, "path": pd.DataFrame(path)}

run = bank_run_dd(cash=13.0, securities=115.0, haircut=0.10, max_monetize_per_day=30.0,
                  uninsured=165.0, kappa=0.42, rho=2.0, equity_rets=[-0.60, -0.30, -0.10])
_, _, d2_bank = merton_equity(212.0, 196.0, 0.03, 0.04, 1.0)
merton_pd_bank = float(norm.cdf(-d2_bank))
assert run["default_day"] == 2 and merton_pd_bank < 0.01
print(f"liquidity default on day {run['default_day']}; Merton 1y PD on the same bank {merton_pd_bank:.2%}")
print(run["path"].round(1).to_string(index=False))
```


## F.24: Chapter 24: Bond-to-CDS Basis & Deliverable Obligation Mechanics {#code-24}

Listings from `24_ch24_bond_cds_basis_and_deliverables.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 24.1: CDS legs, par spread, upfront and hazard bootstrap {#code-24-1}

```python
import numpy as np
import pandas as pd
from scipy.optimize import brentq

RNG = np.random.default_rng(24)
ACT360 = 365.0 / 360.0          # CDS premium accrues ACT/360: a year pays ~365/360 of the spread


def premium_schedule(T, freq=4):
    """Premium dates (years) and ACT/360 accrual fractions for a T-year CDS."""
    n = int(round(T * freq))
    if n < 1:
        raise ValueError("maturity shorter than one premium period")
    t = np.arange(1, n + 1, dtype=float) / freq
    alpha = np.full(n, ACT360 / freq)
    return t, alpha


def survival(t, lam):
    return np.exp(-lam * np.asarray(t, dtype=float))


def disc(t, r):
    """OIS discount factor B(t); not called D because D is reserved for duration."""
    return np.exp(-r * np.asarray(t, dtype=float))


def rpv01(lam, r, T, freq=4, accrued_on_default=True):
    """Risky annuity: Q-value of 1.0 (decimal) of running spread per year, paid quarterly."""
    t, a = premium_schedule(T, freq)
    S = survival(t, lam)
    S_prev = np.concatenate(([1.0], S[:-1]))
    value = np.sum(a * disc(t, r) * S)
    if accrued_on_default:                       # half a period of premium, on average
        value += np.sum(0.5 * a * disc(t - 0.5 / freq, r) * (S_prev - S))
    return float(value)


def protection_leg(lam, r, T, R):
    """(1-R) * int_0^T B(u) lam S(u) du, closed form for flat lam and r."""
    k = lam + r
    if abs(k) < 1e-12:
        return (1.0 - R) * lam * T
    return (1.0 - R) * lam / k * (1.0 - np.exp(-k * T))


def par_spread(lam, r, T, R):
    return protection_leg(lam, r, T, R) / rpv01(lam, r, T)


def hazard_from_spread(s, r, T, R):
    """Flat Q-hazard that reprices a quoted par spread s (decimal)."""
    return brentq(lambda x: par_spread(x, r, T, R) - s, 1e-10, 5.0)


def upfront(s_par, coupon, lam, r, T):
    """Fraction of notional the protection BUYER pays at trade (negative: buyer receives)."""
    return (s_par - coupon) * rpv01(lam, r, T)


# Sanity checks: the credit triangle, the bootstrap, and the upfront convention
r0, T0, R0, lam0 = 0.04, 5.0, 0.40, 0.05
s0 = par_spread(lam0, r0, T0, R0)
assert abs(s0 / (lam0 * (1.0 - R0) / ACT360) - 1.0) < 0.015    # s ~ lam(1-R), ACT/360-adjusted
assert abs(hazard_from_spread(s0, r0, T0, R0) - lam0) < 1e-9    # bootstrap round trip
assert abs(upfront(s0, s0, lam0, r0, T0)) < 1e-15               # par coupon: no upfront
pts_500 = 100.0 * upfront(s0, 0.05, lam0, r0, T0)
assert -9.0 < pts_500 < -7.5                                     # buyer RECEIVES about 8 points
assert rpv01(lam0, r0, T0, accrued_on_default=False) < rpv01(lam0, r0, T0)
```


### Listing 24.2: Bond-level basis: Z-spread, PECS and the jump-to-default hedge ratio {#code-24-2}

```python
def bond_cashflows(c, T, freq=2):
    """Coupon dates (years) and cash flows per 1.0 face; 30/360 semiannual coupons."""
    n = int(round(T * freq))
    t = np.arange(1, n + 1, dtype=float) / freq
    cf = np.full(n, c / freq)
    cf[-1] += 1.0
    return t, cf


def bond_price_hazard(c, T, lam, r, R, freq=2):
    """Q-price per 1.0 face: survival-weighted cash flows plus recovery of face R at default."""
    t, cf = bond_cashflows(c, T, freq)
    k = lam + r
    rec = R * lam * T if abs(k) < 1e-12 else R * lam / k * (1.0 - np.exp(-k * T))
    return float(np.sum(cf * np.exp(-k * t)) + rec)


def z_spread(price, c, T, r, freq=2):
    """Constant spread over the flat continuous OIS curve that reprices the bond."""
    t, cf = bond_cashflows(c, T, freq)
    return brentq(lambda z: np.sum(cf * np.exp(-(r + z) * t)) - price, -0.05, 3.0)


def pecs(price, c, T, r, R, freq=2):
    """Par-equivalent CDS spread: par CDS spread at the flat hazard that reprices the bond."""
    lo, hi = 1e-10, 5.0
    p_hi, p_lo = bond_price_hazard(c, T, hi, r, R, freq), bond_price_hazard(c, T, lo, r, R, freq)
    if not p_hi < price < p_lo:
        raise ValueError("price outside the model's range: is the bond below the assumed recovery?")
    lam_star = brentq(lambda x: bond_price_hazard(c, T, x, r, R, freq) - price, lo, hi)
    return par_spread(lam_star, r, T, R), lam_star


def jtd_hedge_ratio(full_price, R):
    """CDS notional per 1.0 bond face that is flat on an instantaneous default."""
    return (full_price - R) / (1.0 - R)


s_cds = par_spread(lam0, r0, T0, R0)
rows = []
for cpn in (0.04, 0.07, 0.10):                    # discount, near-par, premium bonds
    P = bond_price_hazard(cpn, T0, lam0, r0, R0)
    s_pe, _ = pecs(P, cpn, T0, r0, R0)
    z = z_spread(P, cpn, T0, r0)
    rows.append({"coupon": cpn, "price": 100.0 * P, "Z_bp": 1e4 * z, "PECS_bp": 1e4 * s_pe,
                 "basis_Z_bp": 1e4 * (s_cds - z), "basis_PECS_bp": 1e4 * (s_cds - s_pe)})
    assert abs(s_pe - s_cds) < 1e-9               # priced off the CDS hazard: PECS basis is zero
basis_table = pd.DataFrame(rows)
assert basis_table.Z_bp.iloc[0] < 1e4 * s_cds < basis_table.Z_bp.iloc[2]   # ...the Z basis is not
assert abs(jtd_hedge_ratio(0.88, 0.40) - 0.80) < 1e-12                     # Theo's sticky note
```


### Listing 24.3: A negative-basis package: carry on equity and the stress mark {#code-24-3}

```python
def basis_package_roe(basis_bp, repo_spread_bp, haircut):
    """Annual excess carry per unit of equity for a near-par negative-basis package."""
    if not 0.0 < haircut <= 1.0:
        raise ValueError("haircut must be in (0, 1]")
    carry_bp = -basis_bp - repo_spread_bp * (1.0 - haircut)
    return carry_bp / 1e4 / haircut


def basis_mtm_on_equity(d_basis_bp, spread_duration, haircut):
    """Mark-to-market on equity when the basis moves by d_basis_bp (package is long the basis)."""
    return d_basis_bp / 1e4 * spread_duration / haircut


assert abs(basis_package_roe(-100.0, 40.0, 0.15) - 0.044) < 1e-12     # calm
assert abs(basis_package_roe(-100.0, 40.0, 0.30) - 0.024) < 1e-12     # haircut doubles
assert abs(basis_mtm_on_equity(-150.0, 4.5, 0.15) + 0.45) < 1e-12     # basis -100 -> -250
assert basis_package_roe(-30.0, 40.0, 0.15) < 0.0                     # inside the band: pays to hold
```


### Listing 24.4: Cheapest-to-deliver under the two default regimes {#code-24-4}

```python
def price_at_yield(c, T, y, freq=2):
    """Price per 1.0 face at a semiannual-compounded yield y, on a coupon date."""
    t, cf = bond_cashflows(c, T, freq)
    return float(np.sum(cf / (1.0 + y / freq) ** (freq * t)))


def ctd(deliverables):
    """deliverables: dict name -> post-event price per 1.0 face. Returns (name, payout)."""
    if not deliverables:
        raise ValueError("empty deliverable set: the swap may be orphaned (Section 24.8)")
    name = min(deliverables, key=deliverables.get)
    return name, 1.0 - deliverables[name]


y_event = 0.11                                    # regime 2: no acceleration (illustrative)
no_accel = {"8% due in 1.5y": price_at_yield(0.08, 1.5, y_event),
            "5% due in 22y": price_at_yield(0.05, 22.0, y_event)}
assert abs(no_accel["8% due in 1.5y"] - 0.9595) < 2e-3
assert abs(no_accel["5% due in 22y"] - 0.5063) < 2e-3
name, pay = ctd(no_accel)
assert name == "5% due in 22y" and pay > 0.45     # half of par from a solvent issuer

R_claim = 0.30                                    # regime 1: bankruptcy, claims = par + accrued
accel = {"8% due in 1.5y": R_claim * (1.0 + 0.08 * 0.25),
         "5% due in 22y": R_claim * (1.0 + 0.05 * 0.25)}
_, pay_accel = ctd(accel)
ctd_option_accel = pay_accel - (1.0 - accel["8% due in 1.5y"])
assert 0.0 <= ctd_option_accel < 0.01             # under a point
```


### Listing 24.5: The two-stage auction: inside market, adjustment amounts and final price {#code-24-5}

```python
def round_half_up(x, inc=0.125):
    """Round to the auction increment with halves going UP (round() goes to even)."""
    return float(np.floor(x / inc + 0.5) * inc)


def inside_market(bids, offers, inc=0.125):
    """Stage 1: drop tradeable (touching/crossing) markets, average the best half."""
    b = np.sort(np.asarray(bids, dtype=float))[::-1]
    o = np.sort(np.asarray(offers, dtype=float))
    if b.size != o.size or b.size == 0:
        raise ValueError("need matched bid/offer pairs")
    k = 0
    while k < b.size and b[k] >= o[k]:
        k += 1
    if k == b.size:
        raise ValueError("every market is tradeable; no IMM")
    b_keep, o_keep = b[k:], o[k:]
    h = int(np.ceil(b_keep.size / 2.0))
    imm = round_half_up(np.mean(np.concatenate((b_keep[:h], o_keep[:h]))), inc)
    return imm, b[:k], o[:k]


def adjustment_amounts(tradeable_bids, tradeable_offers, imm, quotation_amount):
    """Dollar penalty for tradeable quotes on the wrong side of the IMM."""
    pb = np.maximum(np.asarray(tradeable_bids, dtype=float) - imm, 0.0) / 100.0 * quotation_amount
    po = np.maximum(imm - np.asarray(tradeable_offers, dtype=float), 0.0) / 100.0 * quotation_amount
    return pb, po


def final_price(imm, open_interest, limit_bids, limit_offers, cap=1.0):
    """Stage 2. open_interest > 0: net requests to BUY bonds, filled against offers from the
    lowest up; < 0: net requests to SELL, filled against bids from the highest down."""
    if open_interest == 0:
        return float(imm)
    selling = open_interest < 0
    if selling:
        book = sorted(limit_bids, key=lambda order: -order[0])
    else:
        book = sorted(limit_offers, key=lambda order: order[0])
    need, last = abs(open_interest), None
    for px, size in book:
        last = px
        need -= size
        if need <= 0:
            break
    if need > 0:                                   # book exhausted
        return 0.0 if selling else 100.0
    return float(min(last, imm + cap) if selling else max(last, imm - cap))


bids = [25.0, 25.25, 25.5, 25.75, 26.0, 26.0, 26.25, 28.0]      # 8 dealers (illustrative)
offers = [b + 2.0 for b in bids]                                 # 2 points wide; max is 3
imm, tb, to = inside_market(bids, offers)
assert imm == 26.875 and tb.size == 1                            # the 28.0 bid crossed 27.0
assert round(26.8125 / 0.125) * 0.125 == 26.75                   # ROBO's banker's rounding
pb, po = adjustment_amounts(tb, to, imm, 2_000_000)
assert abs(pb.sum() - 22_500.0) < 1e-6 and po.sum() == 0.0

QA = 2.0                                                         # $mm per stage-1 quote
lim_bids = [(b, QA) for b in bids] + [(26.5, 10.0), (25.0, 15.0), (23.0, 20.0), (20.0, 30.0)]
lim_offers = [(o, QA) for o in offers] + [(27.0, 5.0), (29.0, 10.0), (32.0, 20.0)]
assert final_price(imm, 0.0, lim_bids, lim_offers) == 26.875
assert final_price(imm, -50.0, lim_bids, lim_offers) == 23.0     # sellers walk the bids down
assert final_price(imm, -200.0, lim_bids, lim_offers) == 0.0     # bids exhausted
assert final_price(imm, -5.0, [(30.0, 10.0)] + lim_bids, lim_offers) == imm + 1.0   # cap binds
assert final_price(imm, 30.0, lim_bids, lim_offers) == 30.0      # buyers walk the offers up
fps = [final_price(imm, -oi, lim_bids, lim_offers) for oi in (5.0, 20.0, 50.0, 80.0, 120.0)]
assert all(a >= b for a, b in zip(fps, fps[1:]))                 # more selling, lower price
```


### Listing 24.6: An OU basis signal, net of costs {#code-24-6}

```python
def simulate_ou(n, dt, kappa, theta, sigma, b0, rng):
    """Exact OU discretization of the basis (bp)."""
    phi = np.exp(-kappa * dt)
    sd = sigma * np.sqrt((1.0 - phi ** 2) / (2.0 * kappa))
    eps = rng.standard_normal(n - 1)
    b = np.empty(n)
    b[0] = b0
    for i in range(1, n):
        b[i] = theta + (b[i - 1] - theta) * phi + sd * eps[i - 1]
    return b


def fit_ou(b, dt):
    """AR(1) regression -> (kappa, theta, sigma). Fails loudly if there is no reversion."""
    phi, a = np.polyfit(b[:-1], b[1:], 1)
    if not 0.0 < phi < 1.0:
        raise ValueError(f"AR(1) coefficient {phi:.4f}: no mean reversion to trade")
    kappa = -np.log(phi) / dt
    resid = b[1:] - (a + phi * b[:-1])
    sigma = np.std(resid, ddof=2) * np.sqrt(2.0 * kappa / (1.0 - phi ** 2))
    return kappa, a / (1.0 - phi), sigma


def basis_strategy(b, dt, theta, sd_stat, z_in, z_out, dur, repo_bp, cost_bp):
    """Long the negative-basis package when b < theta - z_in*sd; flat when b > theta - z_out*sd.
    Weekly P&L in bp of notional: duration MTM plus carry, minus one-way costs."""
    n = b.size
    x = np.zeros(n)
    for i in range(1, n):
        if x[i - 1] == 0.0 and b[i] < theta - z_in * sd_stat:
            x[i] = 1.0
        elif x[i - 1] == 1.0 and b[i] > theta - z_out * sd_stat:
            x[i] = 0.0
        else:
            x[i] = x[i - 1]
    gross = x[:-1] * (dur * np.diff(b) + (-b[:-1] - repo_bp) * dt)
    turnover = np.abs(np.diff(x, prepend=0.0))[:-1]
    net = gross - cost_bp * turnover
    return gross, net, int(np.sum(np.diff(x) > 0))


def sharpe(pnl, dt):
    return float(np.mean(pnl) / np.std(pnl, ddof=1) * np.sqrt(1.0 / dt))


dt_w, kap, th, sig = 1.0 / 52.0, 3.0, -40.0, 60.0          # per year, bp (illustrative)
b_sim = simulate_ou(5200, dt_w, kap, th, sig, th, RNG)
k_hat, th_hat, sig_hat = fit_ou(b_sim, dt_w)
assert abs(k_hat / kap - 1.0) < 0.35
assert abs(th_hat - th) < 10.0
assert abs(sig_hat / sig - 1.0) < 0.10
half_life_weeks = np.log(2.0) / k_hat * 52.0                # true value is about 12 weeks
sd_stat = sig_hat / np.sqrt(2.0 * k_hat)
gross, net, n_entries = basis_strategy(b_sim, dt_w, th_hat, sd_stat, 1.0, 0.0, 4.5, 30.0, 60.0)
assert n_entries > 20
assert sharpe(gross, dt_w) > sharpe(net, dt_w)              # costs are not optional
```


### Listing 24.7: The successor map and manufactured-event flags {#code-24-7}

```python
def successors(shares, original="REFERENCE ENTITY", original_survives=True):
    """Simplified successor thresholds: entity -> fraction of each CDS it inherits.
    shares: entity -> fraction of Relevant Obligations it succeeded to."""
    total = sum(shares.values())
    if total > 1.0 + 1e-12 or min(shares.values(), default=0.0) < 0.0:
        raise ValueError("shares must be non-negative and sum to at most 1")
    retained = 1.0 - total
    for e, x in shares.items():
        if x >= 0.75:
            return {e: 1.0}
    big = [e for e, x in shares.items() if x > 0.25]
    if big and retained <= 0.25:
        return {e: 1.0 / len(big) for e in big}
    if big:
        heirs = big + [original]
        return {e: 1.0 / len(heirs) for e in heirs}
    if original_survives or not shares:
        return {original: 1.0}
    return {max(shares, key=shares.get): 1.0}


def manufactured_event_flags(event):
    """Desk heuristic for the NTCE Credit Deterioration Requirement. Not a legal test."""
    flags = []
    ftp = event["type"] == "failure_to_pay"
    if ftp and event.get("payee_is_affiliate", False):
        flags.append("payment withheld from an affiliate")
    if ftp and event.get("liquidity_runway_weeks", 0) > 52:
        flags.append("ample liquidity: the 13-week model says they could pay")
    if event.get("financing_conditioned_on_default", False):
        flags.append("financing conditioned on the default")
    if event.get("new_long_low_coupon_deliverable", False):
        flags.append("fresh cheap deliverable created")
    return flags


assert successors({"SPINCO": 0.40}) == {"SPINCO": 0.5, "REFERENCE ENTITY": 0.5}   # Windstream shape
assert successors({"NEWCO": 0.80}) == {"NEWCO": 1.0}
assert successors({"A": 0.40, "B": 0.40}) == {"A": 0.5, "B": 0.5}
assert successors({"DROPCO": 0.25}) == {"REFERENCE ENTITY": 1.0}       # 25.0% is not "more than"
assert successors({"A": 0.20, "B": 0.15}, original_survives=False) == {"A": 1.0}
hov_like = {"type": "failure_to_pay", "payee_is_affiliate": True, "liquidity_runway_weeks": 80,
            "financing_conditioned_on_default": True, "new_long_low_coupon_deliverable": True}
assert len(manufactured_event_flags(hov_like)) == 4
assert manufactured_event_flags({"type": "failure_to_pay", "liquidity_runway_weeks": 6}) == []
```


## F.25: Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets {#code-25}

Listings from `25_ch25_nlp_pacer_and_covenant_scraping.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 25.1: The definition graph: parsing, strongly connected components and blast radius {#code-25-1}

```python
# Block 1: the definition graph ------------------------------------------------
import math
import re
from collections import defaultdict, deque
from dataclasses import dataclass

import numpy as np
import pandas as pd

rng = np.random.default_rng(2525)

# Synthetic text written for this book; not copied from any real agreement.
AGREEMENT = """
"Consolidated Net Income" means the net income of the Borrower and its Restricted Subsidiaries for such period.
"Run-Rate Cost Savings" means cost savings projected in good faith, not to exceed 25% of Consolidated EBITDA for such period (calculated after giving effect to such adjustments).
"Consolidated EBITDA" means Consolidated Net Income plus interest, taxes, depreciation and amortization, plus Run-Rate Cost Savings, in each case calculated on a Pro Forma Basis.
"Pro Forma Basis" means, with respect to any Specified Transaction, giving effect to such transaction as if it occurred on the first day of the Test Period, including for purposes of Consolidated EBITDA.
"Specified Transaction" means any acquisition, disposition or incurrence of Indebtedness.
"Indebtedness" means all obligations for borrowed money.
"Lien" means any mortgage, pledge or security interest.
"Lenders" means the lenders party hereto.
"Collateral" means all property subject to a Lien in favor of the Lenders.
"Consolidated First Lien Net Debt" means Indebtedness secured by a Lien on the Collateral on a pari passu basis, less unrestricted cash.
"First Lien Net Leverage Ratio" means the ratio of Consolidated First Lien Net Debt to Consolidated EBITDA.
"Subsidiary" means any entity controlled by the Borrower.
"Restricted Subsidiary" means any Subsidiary that is not an Unrestricted Subsidiary.
"Unrestricted Subsidiary" means any Subsidiary designated as such, provided that no Unrestricted Subsidiary may own Material Intellectual Property.
"Material Intellectual Property" means intellectual property material to the business of the Borrower and its Restricted Subsidiaries.
"Excluded Taxes" means taxes imposed on the Lenders.
"""

DEF_RE = re.compile(r'^"(?P<term>[^"]+)"\s+means[,\s]\s*(?P<body>.+)$', flags=re.M)


def parse_definitions(text):
    """Return {term: (body, char_offset)}; the offset is the citation anchor."""
    return {m.group("term"): (m.group("body"), m.start()) for m in DEF_RE.finditer(text)}


def term_pattern(term):
    """Case-sensitive, word-bounded pattern that also accepts the plural."""
    stem = re.escape(term[:-1]) + "(?:y|ies)" if term.endswith("y") else re.escape(term) + "s?"
    return re.compile(r"(?<![A-Za-z\-])" + stem + r"(?![A-Za-z])")


def find_references(body, terms):
    """Longest-match-first and span-consuming, so 'Lien' inside a longer term is not an edge."""
    taken = np.zeros(len(body), dtype=bool)
    found = set()
    for t in sorted(terms, key=len, reverse=True):
        for m in term_pattern(t).finditer(body):
            s, e = m.span()
            if not taken[s:e].any():
                taken[s:e] = True
                found.add(t)
    return found


def tarjan_scc(nodes, adj):
    """Tarjan's SCCs. Emission order is an evaluation order: dependencies come first."""
    index, low, on_stack, stack, comps = {}, {}, set(), [], []
    counter = [0]

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack.add(v)
        for w in sorted(adj[v]):
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop()
                on_stack.discard(w)
                comp.add(w)
                if w == v:
                    break
            comps.append(frozenset(comp))

    for v in sorted(nodes):
        if v not in index:
            strong(v)
    return comps


def blast_radius(v, adj):
    """Everything that (transitively) uses v: the set B(v) of Section 25.2.2."""
    rev = defaultdict(set)
    for u, vs in adj.items():
        for w in vs:
            rev[w].add(u)
    seen, queue = set(), deque([v])
    while queue:
        for u in rev[queue.popleft()]:
            if u not in seen:
                seen.add(u)
                queue.append(u)
    seen.discard(v)
    return seen


defs = parse_definitions(AGREEMENT)
TERMS = list(defs)
refs = {u: find_references(body, TERMS) for u, (body, _) in defs.items()}
self_refs = sorted(u for u in refs if u in refs[u])
edges = {u: vs - {u} for u, vs in refs.items()}

# The substring trap: a case-insensitive matcher invents the opposite edge.
naive_hits = [t for t in TERMS if t.lower() in "any unrestricted subsidiary"]
assert "Restricted Subsidiary" in naive_hits
assert find_references("any Unrestricted Subsidiary", TERMS) == {"Unrestricted Subsidiary"}
assert find_references("Restricted Subsidiaries of the Borrower", TERMS) == {"Restricted Subsidiary"}

comps = tarjan_scc(TERMS, edges)
comp_of = {v: i for i, c in enumerate(comps) for v in c}
cycles = sorted(sorted(c) for c in comps if len(c) > 1)
for u, vs in edges.items():                       # dependencies are evaluated first
    for v in vs:
        if comp_of[u] != comp_of[v]:
            assert comp_of[v] < comp_of[u]

idx = {t: i for i, t in enumerate(TERMS)}
A = np.zeros((len(TERMS), len(TERMS)), dtype=np.int64)
C = np.zeros((len(comps), len(comps)), dtype=np.int64)
for u, vs in edges.items():
    for v in vs:
        A[idx[u], idx[v]] = 1
        if comp_of[u] != comp_of[v]:
            C[comp_of[u], comp_of[v]] = 1
assert np.linalg.matrix_power(A, len(TERMS)).any()          # cycles: A is not nilpotent
assert not np.linalg.matrix_power(C, len(comps)).any()      # Lemma 25.1: condensation is a DAG

assert ["Consolidated EBITDA", "Pro Forma Basis", "Run-Rate Cost Savings"] in cycles
assert "First Lien Net Leverage Ratio" in blast_radius("Consolidated EBITDA", edges)
assert blast_radius("Excluded Taxes", edges) == set()
print("cycles:", cycles, "| self-references:", self_refs)
```


### Listing 25.2: Basket arithmetic: growers, ratio baskets, the add-back fixed point and the builder {#code-25-2}

```python
# Block 2: basket arithmetic (units: $mm) -------------------------------------
COVENANTS = """
Section 6.01(b)(xii). Indebtedness in an aggregate principal amount not to exceed the greater of $75,000,000 and 35% of Consolidated EBITDA.
Section 6.01(b)(xx). Indebtedness so long as, on a Pro Forma Basis, the First Lien Net Leverage Ratio does not exceed 4.50:1.00 (calculated without netting the cash proceeds of such Indebtedness).
"""
GROWER_RE = re.compile(r"greater of \$([\d,]+) and (\d+(?:\.\d+)?)% of Consolidated EBITDA")
RATIO_RE = re.compile(r"does not exceed (\d+\.\d+):1\.00")
CAP_RE = re.compile(r"not to exceed (\d+(?:\.\d+)?)% of Consolidated EBITDA")


@dataclass
class Grower:
    fixed_mm: float
    pct: float
    span: str

    def capacity(self, ebitda_mm):
        return max(self.fixed_mm, self.pct * ebitda_mm)


@dataclass
class RatioBasket:
    max_ratio: float
    scope_debt_mm: float
    nettable_cash_mm: float
    nets_proceeds: bool
    span: str

    def capacity(self, ebitda_mm):
        if ebitda_mm <= 0:
            return 0.0
        if self.nets_proceeds:                # Case 2 of 25.3.2: the perpetual-motion machine
            ok = (self.scope_debt_mm - self.nettable_cash_mm) / ebitda_mm <= self.max_ratio
            return math.inf if ok else 0.0
        return max(0.0, self.max_ratio * ebitda_mm - self.scope_debt_mm + self.nettable_cash_mm)


def parse_baskets(text, scope_debt_mm, nettable_cash_mm=0.0):
    out = []
    for line in text.strip().splitlines():
        g = GROWER_RE.search(line)
        if g:
            out.append(Grower(float(g.group(1).replace(",", "")) / 1e6, float(g.group(2)) / 100, line))
        r = RATIO_RE.search(line)
        if r:
            out.append(RatioBasket(float(r.group(1)), scope_debt_mm, nettable_cash_mm,
                                   nets_proceeds="without netting" not in line, span=line))
    return out


def addback_fixed_point(e0_mm, claimed_mm, cap, after_effect=True, tol=1e-10, max_iter=10_000):
    """Equation (25.1). 'After giving effect' turns the cap into a contraction fixed point."""
    if not after_effect:
        return min(claimed_mm, cap * e0_mm)
    if not 0.0 <= cap < 1.0:
        raise ValueError("cap >= 1: the cycle is not a contraction; send it to a human")
    a = 0.0
    for _ in range(max_iter):
        a_next = min(claimed_mm, cap * (e0_mm + a))
        if abs(a_next - a) < tol:
            return a_next
        a = a_next
    raise RuntimeError("add-back iteration did not converge")


def total_capacity(ebitda_mm, nodes):
    return sum(n.capacity(ebitda_mm) for n in nodes)


def builder_available(starter_mm, cni_quarters_mm, equity_mm=0.0, usage_mm=0.0):
    """Equation (25.2): 50% of cumulative CNI if positive, minus 100% of a deficit."""
    n = float(np.sum(cni_quarters_mm))
    return max(0.0, starter_mm + (0.5 * n if n >= 0 else n) + equity_mm - usage_mm)


rrcs_body = defs["Run-Rate Cost Savings"][0]
CAP = float(CAP_RE.search(rrcs_body).group(1)) / 100
AFTER = "after giving effect" in rrcs_body
E0, CLAIMED = 200.0, 80.0                                  # Halyard, illustrative
A_after = addback_fixed_point(E0, CLAIMED, CAP, after_effect=AFTER)
A_before = addback_fixed_point(E0, CLAIMED, CAP, after_effect=False)
assert CAP == 0.25 and AFTER
assert abs(A_after - CAP / (1 - CAP) * E0) < 1e-6         # 66.67, the closed form
assert abs(A_before - 50.0) < 1e-12

baskets = parse_baskets(COVENANTS, scope_debt_mm=900.0)
grower = next(b for b in baskets if isinstance(b, Grower))
ratio = next(b for b in baskets if isinstance(b, RatioBasket))
assert (grower.fixed_mm, grower.pct) == (75.0, 0.35)
assert ratio.max_ratio == 4.5 and not ratio.nets_proceeds

E_with = E0 + A_after
K_without, K_with = total_capacity(E0, baskets), total_capacity(E_with, baskets)
assert abs(K_without - 75.0) < 1e-9
assert abs(K_with - 393.333) < 1e-3
h = 1e-6
slope = (total_capacity(E_with + h, baskets) - total_capacity(E_with, baskets)) / h
assert abs(slope - 4.85) < 1e-4                            # dK/dE = m + p

leaky = RatioBasket(4.5, 900.0, 0.0, nets_proceeds=True, span="(synthetic: netting allowed)")
assert math.isinf(leaky.capacity(E_with))

assert builder_available(50.0, [30.0, -10.0]) == 60.0
assert builder_available(50.0, [10.0, -30.0]) == 30.0     # losses count double
assert builder_available(50.0, [-80.0]) == 0.0
print(f"capacity without add-backs ${K_without:.1f}mm, with ${K_with:.1f}mm, slope {slope:.2f}")
```


### Listing 25.3: Leakage capacity as max-flow (Edmonds-Karp) {#code-25-3}

```python
# Block 3: leakage capacity as max-flow (units: $mm) --------------------------
def max_flow_min_cut(arcs, s, t):
    """Edmonds-Karp. arcs: list of (u, v, basket, capacity). Returns (value, cut_arcs)."""
    cap = defaultdict(lambda: defaultdict(float))
    for u, v, _, c in arcs:
        cap[u][v] += c
        cap[v][u] += 0.0
    res = {u: dict(vs) for u, vs in cap.items()}
    value = 0.0
    while True:
        parent, queue = {s: None}, deque([s])
        while queue and t not in parent:
            u = queue.popleft()
            for v, c in res[u].items():
                if c > 1e-12 and v not in parent:
                    parent[v] = u
                    queue.append(v)
        if t not in parent:
            break
        path, v = [], t
        while parent[v] is not None:
            path.append((parent[v], v))
            v = parent[v]
        push = min(res[u][v] for u, v in path)
        if math.isinf(push):
            return math.inf, []                       # an uncapped route all the way out
        for u, v in path:
            res[u][v] -= push
            res[v][u] += push
        value += push
    reach, queue = {s}, deque([s])
    while queue:
        u = queue.popleft()
        for v, c in res[u].items():
            if c > 1e-12 and v not in reach:
                reach.add(v)
                queue.append(v)
    return value, [a for a in arcs if a[0] in reach and a[1] not in reach]


def jcrew_arcs(trapdoor_mm):
    return [("LoanParties", "NonGuarantorRS", "non-guarantor investments", 150.0),
            ("LoanParties", "NonGuarantorRS", "general investments", 100.0),
            ("NonGuarantorRS", "Unrestricted", "trapdoor", trapdoor_mm)]


phi_before, cut_before = max_flow_min_cut(jcrew_arcs(0.0), "LoanParties", "Unrestricted")
phi_after, cut_after = max_flow_min_cut(jcrew_arcs(math.inf), "LoanParties", "Unrestricted")
assert phi_before == 0.0 and [a[2] for a in cut_before] == ["trapdoor"]
assert phi_after == 250.0 and sum(a[3] for a in cut_after) == phi_after   # max-flow = min-cut
# A J.Crew blocker is commodity-specific: it zeroes IP arcs into the sink, not cash arcs.
# (Commodities share basket capacity, so phi_ip + phi_cash <= 250 jointly.)
phi_ip_blocked, _ = max_flow_min_cut(jcrew_arcs(0.0), "LoanParties", "Unrestricted")
phi_cash, _ = max_flow_min_cut(jcrew_arcs(math.inf), "LoanParties", "Unrestricted")
assert phi_ip_blocked == 0.0 and phi_cash == 250.0
```


### Listing 25.4: Why token diffs miss covenant edits {#code-25-4}

```python
# Block 4: why token diffs miss covenant edits (Section 25.5.1) ---------------
d, n_tok = 10_000, 150_000
x = np.bincount(rng.integers(0, d - 2, size=n_tok), minlength=d).astype(float)
x[d - 2], x[d - 1] = 1.0, 0.0              # token "4.50" appears once; "5.25" never
x_new = x.copy()
x_new[d - 2] -= 1.0
x_new[d - 1] += 1.0
cos = x @ x_new / (np.linalg.norm(x) * np.linalg.norm(x_new))
assert np.isclose(1 - cos, 1 / (x @ x), rtol=1e-6)
assert 1 - cos <= d / x.sum() ** 2                          # Cauchy-Schwarz bound
amended = RatioBasket(5.25, 900.0, 0.0, False, span="(synthetic amendment)")
delta_K = amended.capacity(E_with) - ratio.capacity(E_with)
assert abs(delta_K - 200.0) < 1e-6
print(f"1 - cos = {1 - cos:.2e}; capacity change = ${delta_K:,.1f}mm")
```


### Listing 25.5: Rate limits with a token bucket, and EDGAR hygiene {#code-25-5}

```python
# Block 5: rate limits (Lemma 25.2) and EDGAR hygiene -------------------------
class TokenBucket:
    """One global bucket. In production, share it across workers (lock or Redis)."""

    def __init__(self, rate, burst):
        self.rate, self.burst = float(rate), float(burst)
        self.tokens, self.t = float(burst), 0.0

    def try_acquire(self, now):
        self.tokens = min(self.burst, self.tokens + (now - self.t) * self.rate)
        self.t = now
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False


def max_in_window(times, h):
    times = np.sort(np.asarray(times))
    return int(np.max(np.searchsorted(times, times + h, side="right") - np.arange(len(times))))


attempts = np.sort(rng.uniform(0.0, 60.0, size=6_000))      # 100 requests/s of demand
naive_bucket, safe_bucket = TokenBucket(rate=10, burst=10), TokenBucket(rate=8, burst=2)
naive_ok = [t for t in attempts if naive_bucket.try_acquire(t)]
safe_ok = [t for t in attempts if safe_bucket.try_acquire(t)]
assert max_in_window(naive_ok, 1.0) <= 10 + 10 * 1.0           # the lemma's bound holds...
assert max_in_window(naive_ok, 1.0) > 10                        # ...and breaks 10 requests/s
assert max_in_window(safe_ok, 1.0) <= 10                        # b + rho*h0 <= L

USER_AGENT = "Example Desk Research desk-ops@example.com"     # the SEC asks for a real mailbox


def edgar_submissions_url(cik):
    return f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"


assert edgar_submissions_url("1234") == "https://data.sec.gov/submissions/CIK0000001234.json"
```


### Listing 25.6: A polite fetcher with backoff (a sketch, not run) {#code-25-6}

```python
# sketch: live ingest (not run here; needs network access, a real mailbox and a CourtListener token)
import time
import requests

bucket = TokenBucket(rate=8, burst=2)


def polite_get(url, headers, params=None, retries=5):
    for attempt in range(retries):
        while not bucket.try_acquire(time.monotonic()):
            time.sleep(0.01)
        r = requests.get(url, headers=headers, params=params, timeout=30)
        if r.status_code in (403, 429, 503):
            time.sleep(2 ** attempt)          # exponential backoff, then alert a human
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"gave up on {url}")


fts = polite_get("https://efts.sec.gov/LATEST/search-index", {"User-Agent": USER_AGENT},
                 {"q": '"unrestricted subsidiary"', "forms": "8-K", "dateRange": "custom",
                  "startdt": "2024-01-01", "enddt": "2026-10-17"})
dockets = polite_get("https://www.courtlistener.com/api/rest/v4/search/",
                     {"Authorization": "Token <YOUR_TOKEN>"},
                     {"type": "rd", "q": '"rule 2019" "verified statement"',
                      "docket_number": "23-90020", "court": "txsb"})
```


### Listing 25.7: Rule 2019 statements to a holdings panel, and the blocking test {#code-25-7}

```python
# Block 6: Rule 2019 statements -> holdings panel (synthetic holders; $mm face) --
lots = pd.DataFrame(
    [  # statement, filed, holder, face_mm, acquisition quarter
        (1, "2026-01-15", "Holder_A", 120.0, "2025Q3"),
        (1, "2026-01-15", "Holder_B", 80.0, "2025Q4"),
        (1, "2026-01-15", "Holder_C", 40.0, "2025Q4"),
        (2, "2026-03-02", "Holder_A", 120.0, "2025Q3"),
        (2, "2026-03-02", "Holder_A", 30.0, "2026Q1"),
        (2, "2026-03-02", "Holder_B", 80.0, "2025Q4"),
        (2, "2026-03-02", "Holder_C", 40.0, "2025Q4"),
        (2, "2026-03-02", "Holder_D", 60.0, "2026Q1"),
    ],
    columns=["stmt", "filed", "holder", "face_mm", "acq_q"],
)
CLASS_FACE_MM, ROUNDING_MM = 1_000.0, 1.0
QTR_PX = {"2025Q3": 88.0, "2025Q4": 71.0, "2026Q1": 58.0}   # synthetic quarterly average prices

wide = (lots.groupby(["stmt", "holder"], as_index=False)["face_mm"].sum()
        .pivot(index="holder", columns="stmt", values="face_mm").fillna(0.0))
theta = wide.sum() / CLASS_FACE_MM
flows = wide[2] - wide[1]
theta_err = (wide > 0).sum() * ROUNDING_MM / (2 * CLASS_FACE_MM)


def blocks(theta_g, turnout):
    """11 U.S.C. 1126(c) amount test: the group alone defeats acceptance if theta > turnout/3."""
    return theta_g > turnout / 3.0


lots["px"] = lots["acq_q"].map(QTR_PX)
last = lots[lots["stmt"] == 2]
basis = (last["face_mm"] * last["px"]).groupby(last["holder"]).sum() / last.groupby("holder")["face_mm"].sum()
hhi_lower = float(((wide[2] / CLASS_FACE_MM) ** 2).sum())   # a lower bound: non-filers are invisible

assert np.isclose(theta[1], 0.24) and np.isclose(theta[2], 0.33)
assert flows.to_dict() == {"Holder_A": 30.0, "Holder_B": 0.0, "Holder_C": 0.0, "Holder_D": 60.0}
assert blocks(theta[2], turnout=0.60) and not blocks(theta[2], turnout=1.00)
assert np.isclose(basis["Holder_A"], 82.0) and np.isclose(basis["Holder_D"], 58.0)
assert np.isclose(theta_err[2], 0.002)
assert 0.0 < hhi_lower < theta[2] ** 2
```


### Listing 25.8: The docket state machine and its transition intensities {#code-25-8}

```python
# Block 7: docket state machine, transition intensities (Section 25.7.2) ------
spells = pd.DataFrame(
    [  # case, state, days in state, next state (None = still there: censored)
        ("case1", "Organized", 31.0, "Contested"),    # case1 mimics the Hughes sequence
        ("case1", "Contested", 10.0, "Standstill"),
        ("case2", "Organized", 45.0, "Contested"),
        ("case2", "Contested", 60.0, None),
        ("case3", "Organized", 90.0, None),
    ],
    columns=["case", "state", "days", "next"],
)
T_a = spells.groupby("state")["days"].sum()
N_ab = spells.dropna(subset=["next"]).groupby(["state", "next"]).size()
q_hat = N_ab / T_a.reindex(N_ab.index.get_level_values(0)).to_numpy()
assert np.isclose(q_hat[("Organized", "Contested")], 2 / 166)   # censored days still count in T_a
assert np.isclose(q_hat[("Contested", "Standstill")], 1 / 70)
```


### Listing 25.9: Classifier error as an IC tax, and the citation contract {#code-25-9}

```python
# Block 8: classifier error as an IC tax (Equation 25.3), plus the citation contract --
n_obs, pi, a_sens, b_spec = 400_000, 0.05, 0.90, 0.95
x_true = (rng.random(n_obs) < pi).astype(float)
ret = x_true + rng.standard_normal(n_obs)                     # illustrative units
u = rng.random(n_obs)
x_hat = np.where(x_true == 1.0, u < a_sens, u < 1.0 - b_spec).astype(float)
J = a_sens + b_spec - 1.0
pi_hat = (1.0 - b_spec) + J * pi
ratio_pred = J * math.sqrt(pi * (1 - pi)) / math.sqrt(pi_hat * (1 - pi_hat))
ratio_sim = np.corrcoef(x_hat, ret)[0, 1] / np.corrcoef(x_true, ret)[0, 1]
ppv = a_sens * pi / pi_hat
assert abs(ratio_pred - 0.639) < 1e-3
assert abs(ratio_sim - ratio_pred) < 0.03
assert abs(ppv - 0.486) < 1e-3

for node in baskets:                                           # every number has a source span
    assert node.span in COVENANTS
assert "calculated after giving effect to such adjustments" in rrcs_body
print(f"IC retained: predicted {ratio_pred:.3f}, simulated {ratio_sim:.3f}; flag precision {ppv:.3f}")
```


## F.26: Chapter 26: AI Agents & LLMs on the Credit Desk {#code-26}

Listings from `26_ch26_ai_agents_and_llms_on_the_credit_desk.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 26.1: The document store and the deterministic basket calculators {#code-26-1}

```python
# llm_desk_harness.py, block 1 of 3: document store and deterministic calculators.
# Offline and seeded; numpy/scipy/pandas only; no network, no API calls.
import hashlib
import numpy as np
import pandas as pd
from scipy.special import comb
from scipy.stats import norm

SEED = 26
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]
PCTS = [0.15, 0.25, 0.30, 0.50, 1.00]


def make_agreement(doc_id="HALYARD-CA-AMD2"):
    """Synthetic agreement: Section 6.08(b)(i)-(xii), one clause per 1-based PDF page.
    Fixed amounts are distinct ($10mm..$65mm), so a span supports only its own clause."""
    pages, baskets = {}, {}
    for j, rn in enumerate(ROMAN):
        sec, fixed, pct = f"6.08(b)({rn})", (10 + 5 * j) * 1e6, PCTS[j % len(PCTS)]
        pages[j + 1] = (f"Section {sec}. Restricted Payments in an aggregate amount not to exceed "
                        f"the greater of ${fixed / 1e6:.0f}mm and {pct * 100:.0f}% of Consolidated EBITDA.")
        baskets[sec] = {"fixed": fixed, "pct_ebitda": pct, "page": j + 1}
    return {"doc_id": doc_id, "pages": pages, "baskets": baskets}


STORE = make_agreement()
SECTIONS = list(STORE["baskets"])


def basket_capacity(fixed, pct_ebitda, ebitda, used=0.0):
    """'Greater of fixed and pct x Consolidated EBITDA' in USD -> (capacity, remaining, over_used).
    EBITDA <= 0 contributes nothing; capacity is never negative."""
    if not np.all(np.isfinite([fixed, pct_ebitda, ebitda, used])):
        raise ValueError("non-finite input")
    if fixed < 0 or pct_ebitda < 0 or used < 0:
        raise ValueError("fixed, pct_ebitda and used must be >= 0")
    capacity = max(float(fixed), float(pct_ebitda) * max(float(ebitda), 0.0))
    return capacity, max(capacity - float(used), 0.0), bool(used > capacity)


def capacity_series(quarters, fixed, pct_ebitda):
    """Point-in-time: each quarter uses EBITDA as then reported, never the later restatement."""
    out = quarters.copy()
    res = [basket_capacity(fixed, pct_ebitda, e, u)
           for e, u in zip(out["ebitda_reported"], out["used"])]
    out["capacity"] = [r[0] for r in res]
    out["remaining"] = [r[1] for r in res]
    out["over_used"] = [r[2] for r in res]
    return out


QUARTERS = pd.DataFrame({      # Theo's 13-week model, reborn as a test fixture (illustrative)
    "quarter": ["2025Q4", "2026Q1", "2026Q2", "2026Q3"],
    "ebitda_reported": [210e6, 160e6, -35e6, 40e6],
    "ebitda_restated": [205e6, 150e6, -60e6, 40e6],
    "used": [0.0, 20e6, 20e6, 70e6],
})


def property_tests(n=10_000, seed=SEED):
    rng = np.random.default_rng(seed)
    for _ in range(n):
        fixed, pct = rng.uniform(0, 100e6), rng.uniform(0, 1.5)
        ebitda, used = rng.normal(50e6, 120e6), rng.uniform(0, 150e6)
        cap, rem, over = basket_capacity(fixed, pct, ebitda, used)
        assert cap >= fixed >= 0.0
        if ebitda <= 0:
            assert cap == fixed
        assert basket_capacity(fixed, pct, ebitda + abs(rng.normal(0, 10e6)), used)[0] >= cap
        assert rem == max(cap - used, 0.0) and over == (used > cap)
    return True


assert property_tests()
assert basket_capacity(40e6, 0.30, -1e9)[:2] == (40e6, 40e6)         # the ROBO trap
cs = capacity_series(QUARTERS, 50e6, 1.00)
assert cs.loc[cs["quarter"] == "2026Q2", "capacity"].item() == 50e6   # infuriatingly, right
assert cs.loc[cs["quarter"] == "2026Q3", "over_used"].item()         # used 70mm > capacity 50mm
assert STORE["pages"][7].count("$40mm") == 1 and 14 not in STORE["pages"]   # there is no (xiv)
```


### Listing 26.2: The stochastic reader, citation contract, calibration and abstention {#code-26-2}

```python
# Block 2 of 3: the stochastic reader, the citation contract, calibration, abstention.
def logistic(x):
    return 1.0 / (1.0 + np.exp(-x))


def make_questions(n, seed):
    """Question i asks for basket s_i; p_true is its difficulty, a property of the question."""
    rng = np.random.default_rng(seed)
    return pd.DataFrame({"question": rng.choice(SECTIONS, size=n),
                         "p_true": logistic(rng.normal(1.4, 0.9, n))})


class StochasticReader:
    """A model of the model. Right with prob p_true; a wrong read lands on another clause.
    Pointer: fabricated with prob fab_rate (V=0); a real page that does not support the claim
    with prob misrep_rate (V=1, S=0); otherwise the page the asserted values came from.
    Stated confidence = 1 - (1 - p)(1 - overconf); overconf = 0 is calibrated."""

    def __init__(self, overconf=0.0, fab_rate=0.0, misrep_rate=0.0, shuffle_conf=False, seed=SEED):
        assert fab_rate >= 0 and misrep_rate >= 0 and fab_rate + misrep_rate <= 1
        self.overconf, self.fab, self.misrep = overconf, fab_rate, misrep_rate
        self.shuffle, self.rng = shuffle_conf, np.random.default_rng(seed)

    def answer(self, store, qs):
        rng, pages, k = self.rng, store["pages"], len(SECTIONS)
        n, p, ql = len(qs), qs["p_true"].to_numpy(), qs["question"].tolist()
        q_idx = np.array([SECTIONS.index(s) for s in ql])
        correct = rng.random(n) < p
        u, offs, alt = rng.random(n), rng.integers(1, k, n), rng.integers(1, k, n)
        conf = 1.0 - (1.0 - p) * (1.0 - self.overconf)
        if self.shuffle:
            conf = rng.permutation(conf)                     # confidence with zero power
        rows = []
        for i in range(n):
            src = q_idx[i] if correct[i] else (q_idx[i] + offs[i]) % k
            b = store["baskets"][SECTIONS[src]]
            if u[i] < self.fab:
                page, start, end = k + 2, 0, 120             # the famous (xiv)
            else:
                honest = u[i] >= self.fab + self.misrep
                page = int(b["page"] if honest else (b["page"] - 1 + alt[i]) % k + 1)
                start, end = pages[page].find("the greater of"), len(pages[page])
            rows.append((ql[i], b["fixed"], b["pct_ebitda"], store["doc_id"],
                         int(page), int(start), int(end), float(conf[i])))
        return pd.DataFrame(rows, columns=["question", "fixed", "pct", "doc_id",
                                           "page", "start", "end", "conf"])


def support_test(span, fixed, pct):
    """Support test v1 (versioned): the span states both asserted parameters verbatim."""
    return f"greater of ${fixed / 1e6:.0f}mm and" in span and f"and {pct * 100:.0f}% of" in span


def verify_claims(claims, store):
    """Deterministic (A, V, S) for every claim; an unresolvable pointer is V = 0."""
    rows = []
    for c in claims.itertuples(index=False):
        text = store["pages"].get(c.page) if c.doc_id == store["doc_id"] else None
        V = int(text is not None and 0 <= c.start < c.end <= len(text))
        S = int(V == 1 and support_test(text[c.start:c.end], c.fixed, c.pct))
        t = store["baskets"][c.question]
        A = int(np.isclose(c.fixed, t["fixed"]) and np.isclose(c.pct, t["pct_ebitda"]))
        rows.append((A, V, S))
    out = claims.copy()
    out["A"], out["V"], out["S"] = (np.array(col) for col in zip(*rows))
    return out


def three_rates(v):
    return {"acc": v["A"].mean(), "valid": v["V"].mean(), "support": v["S"].mean(),
            "FH": (v["V"] * (1 - v["S"])).mean()}


def ece(conf, correct, bins=10):
    conf, correct = np.asarray(conf, float), np.asarray(correct, float)
    idx = np.minimum((conf * bins).astype(int), bins - 1)
    return float(sum((idx == b).mean() * abs(correct[idx == b].mean() - conf[idx == b].mean())
                     for b in range(bins) if (idx == b).any()))


def risk_coverage(conf, correct):
    order = np.argsort(-np.asarray(conf, float), kind="stable")
    err = 1.0 - np.asarray(correct, float)[order]
    k = np.arange(1, len(err) + 1)
    return k / len(err), np.cumsum(err) / k                  # (coverage, selective risk)


def aurc(conf, correct):
    return float(risk_coverage(conf, correct)[1].mean())


def abstain_threshold(c_fp, c_abs):
    """Answer iff calibrated confidence > p* = 1 - C_abs / C_FP."""
    if c_abs <= 0:
        return 1.0
    if c_fp <= c_abs:
        return 0.0
    return 1.0 - c_abs / c_fp


qs = make_questions(20_000, seed=SEED + 1)
cal = verify_claims(StochasticReader(seed=7).answer(STORE, qs), STORE)
over = verify_claims(StochasticReader(overconf=0.6, seed=7).answer(STORE, qs), STORE)
flat = verify_claims(StochasticReader(shuffle_conf=True, seed=7).answer(STORE, qs), STORE)
assert ece(cal["conf"], cal["A"]) < 0.02 < 0.10 < ece(over["conf"], over["A"])
assert np.isclose(aurc(cal["conf"], cal["A"]), aurc(over["conf"], over["A"]))  # same power...
assert aurc(cal["conf"], cal["A"]) < 0.8 * aurc(flat["conf"], flat["A"])      # ...and it is real
p_star = abstain_threshold(20.0, 1.0)
assert abs(p_star - 0.95) < 1e-12 and abstain_threshold(1.0, 2.0) == 0.0
answered = cal["conf"] > p_star
assert answered.any() and 1 - cal.loc[answered, "A"].mean() < 1 - cal["A"].mean()

noisy = verify_claims(StochasticReader(fab_rate=0.10, misrep_rate=0.20, seed=11).answer(STORE, qs), STORE)
rates = three_rates(noisy)
assert abs(rates["FH"] - 0.20) < 0.02 and abs(rates["valid"] - 0.90) < 0.02
assert (noisy["S"] <= noisy["V"]).all()                      # S = 1 implies V = 1
```


### Listing 26.3: Chains, verifiers, retries, pass^k, replay and research hurdles {#code-26-3}

```python
# Block 3 of 3: chains, verifiers, retries, pass^k, replay, research hurdles, cost frontier.
rng = np.random.default_rng(SEED)


def pass_hat_k(n, c, k):
    """Unbiased estimator of p**k (tau-bench pass^k) from c successes in n i.i.d. trials."""
    return float("nan") if k > n else comb(c, k) / comb(n, k)


def pass_at_k(n, c, k):
    return float("nan") if k > n else 1.0 - comb(n - c, k) / comb(n, k)


def verified_closed_form(p_types, weights, d, f, m):
    """Pr(right | accepted within m tries) and coverage, for a mixture of question types."""
    p, w = np.asarray(p_types, float), np.asarray(weights, float)
    a_r, a_w = p * (1 - f), (1 - p) * (1 - d)
    acc_m = 1.0 - (1.0 - a_r - a_w) ** m
    return float((w * a_r / (a_r + a_w) * acc_m).sum() / (w * acc_m).sum()), float((w * acc_m).sum())


def simulate_verified(p_types, weights, d, f, m, n_paths, rng):
    p_path = rng.choice(np.asarray(p_types, float), size=n_paths, p=np.asarray(weights, float))
    accepted, right = np.zeros(n_paths, bool), np.zeros(n_paths, bool)
    for _ in range(m):
        ok = rng.random(n_paths) < p_path
        reject = np.where(ok, rng.random(n_paths) < f, rng.random(n_paths) < d)
        new = ~accepted & ~reject
        right[new], accepted[new] = ok[new], True
    return float(right[accepted].mean()), float(accepted.mean())


def lost_in_the_middle(n=30_000, base=0.90, depth=0.35, seed=SEED):
    """Toy U-curve: hit probability dips when the evidence sits mid-context."""
    g = np.random.default_rng(seed)
    pos = g.random(n)
    hit = g.random(n) < base - depth * 4.0 * pos * (1.0 - pos)
    terc = np.minimum((pos * 3).astype(int), 2)
    return np.array([hit[terc == t].mean() for t in range(3)])


def frame_hash(df):
    return hashlib.sha256(df.to_csv(index=False, float_format="%.6f").encode()).hexdigest()


def log_record(prompt, model_id, params, output, ts):
    """An LLM output is a point-in-time datum keyed by what produced it. Store; never recompute."""
    key = hashlib.sha256(f"{prompt}|{model_id}|{sorted(params.items())}|{ts}".encode()).hexdigest()
    return {"key": key, "model_id": model_id, "params": dict(params), "output": output, "ts": ts}


def agreement_rate(a, b, cols=("fixed", "pct", "page")):
    return float((a[list(cols)].to_numpy() == b[list(cols)].to_numpy()).all(axis=1).mean())


EULER_GAMMA = 0.5772156649015329            # gamma_E, not the risk aversion gamma


def expected_max_sharpe(n_trials, sd_sharpe):
    """E[max of N zero-alpha Sharpe estimates] (Bailey & Lopez de Prado), units of sd_sharpe."""
    if n_trials < 2:
        return 0.0
    return float(sd_sharpe * ((1 - EULER_GAMMA) * norm.ppf(1 - 1 / n_trials)
                              + EULER_GAMMA * norm.ppf(1 - 1 / (n_trials * np.e))))


def admissible(dates, model_cutoff):
    """A feature generator trained through model_cutoff is clean only for dates after it."""
    return (pd.to_datetime(pd.Series(dates)) > pd.Timestamp(model_cutoff)).to_numpy()


CONFIGS = pd.DataFrame([    # illustrative accuracies; prices of the order of Oct 2026 list prices
    ("small-full-read", 230_000, 800, 0.50, 2.50, 1, 0.71),
    ("mid-retrieval", 12_000, 600, 2.00, 10.00, 1, 0.86),
    ("large-retrieval", 12_000, 900, 4.00, 20.00, 1, 0.89),
    ("mid+verifier", 12_000, 600, 2.00, 10.00, 2, 0.93),
], columns=["name", "tok_in", "tok_out", "usd_in_per_m", "usd_out_per_m", "calls", "accuracy"])


def cheapest_config(configs, a_star):
    c = configs.assign(usd_per_task=lambda x: x["calls"] * (x["tok_in"] * x["usd_in_per_m"]
                                                            + x["tok_out"] * x["usd_out_per_m"]) / 1e6)
    ok = c[c["accuracy"] >= a_star]
    return None if ok.empty else ok.sort_values("usd_per_task").iloc[0]


successes = (rng.random((2_000, 20)) < 0.7).sum(axis=1)
assert abs(np.mean([pass_hat_k(20, c, 5) for c in successes]) - 0.7 ** 5) < 0.02
assert pass_at_k(20, 14, 5) > 0.99 and np.isnan(pass_hat_k(3, 2, 5))   # pass@5 flatters
assert abs((rng.random((100_000, 10)) < 0.95).all(axis=1).mean() - 0.95 ** 10) < 0.01
post, _ = simulate_verified([0.9], [1.0], d=0.8, f=0.05, m=1, n_paths=200_000, rng=rng)
assert abs(post - 0.9 * 0.95 / (0.9 * 0.95 + 0.1 * 0.2)) < 0.01        # 0.977
mix = ([0.95, 0.40], [0.8, 0.2])
(cf1, cov1), (cf3, cov3) = (verified_closed_form(*mix, d=0.8, f=0.05, m=m) for m in (1, 3))
mc3, _ = simulate_verified(*mix, d=0.8, f=0.05, m=3, n_paths=200_000, rng=rng)
assert cf3 < cf1 and cov3 > cov1 and abs(mc3 - cf3) < 0.01   # retries buy coverage with accuracy
acc_pos = lost_in_the_middle()
assert acc_pos[1] < min(acc_pos[0], acc_pos[2])                  # the middle is skimmed

h = frame_hash(capacity_series(QUARTERS, 50e6, 1.00))
run_a, run_b, run_c = (StochasticReader(seed=s).answer(STORE, qs) for s in (101, 101, 202))
assert agreement_rate(run_a, run_b) == 1.0 > agreement_rate(run_a, run_c)
assert frame_hash(capacity_series(QUARTERS, 50e6, 1.00)) == h      # calculators ignore reader seeds
assert len(log_record("Fixed amount in 6.08(b)(vii)?", "reader-v1", {"T": 0.0},
                      "40000000", "2026-10-18T14:58:00Z")["key"]) == 64

assert 1.70 < expected_max_sharpe(2_000, 0.5) < 1.75 and 0.93 < expected_max_sharpe(20, 0.5) < 0.97
assert admissible(pd.date_range("2024-01-01", periods=36, freq="MS"), "2025-06-30").sum() == 18
assert cheapest_config(CONFIGS, 0.90)["name"] == "mid+verifier"
assert cheapest_config(CONFIGS, 0.85)["name"] == "mid-retrieval"
print("harness checks passed:", {k: round(float(v), 3) for k, v in rates.items()})
```


## F.27: Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs {#code-27}

Listings from `27_ch27_system_architecture_and_asics.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 27.1: Provenance-typed prices, clock checks and TRACE dedupe {#code-27-1}

```python
# ch27_desk_system.py, block 1 of 5: provenance-typed prices, clock checks, TRACE dedupe.
# Seeded; numpy/scipy/pandas only; the five blocks run in order in one interpreter.
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import math
import numpy as np
import pandas as pd
from scipy import stats

RNG = np.random.default_rng(27)


class PriceKind(str, Enum):
    TRADED = "traded"                  # a print: someone paid this
    FIRM_QUOTE = "firm_quote"          # executable at this size, now
    INDICATIVE_RUN = "indicative_run"  # dealer run: not firm (Man 2022 p.19)
    EVALUATED = "evaluated"            # matrix or evaluated vendor price (Bohn-Stein p.334)
    COMPOSITE = "composite"            # blended vendor composite


TRAINABLE = {PriceKind.TRADED, PriceKind.FIRM_QUOTE}   # allowed as labels, fills, cost targets


@dataclass(frozen=True)
class PriceRecord:
    instrument_key: str
    price: float
    price_type: str
    side: str
    size_mm: float
    kind: PriceKind
    source: str
    event_ns: int
    known_ns: int
    affiliate_flag: Optional[bool] = None


def latency_ms(rec: PriceRecord, clock_err_ms: float) -> float:
    """known_at - event_time in ms; a negative value beyond the clock-error bound is a clock fault."""
    lat = (rec.known_ns - rec.event_ns) / 1e6
    if lat < -clock_err_ms:
        raise ValueError(f"clock fault on {rec.instrument_key}: latency {lat:.3f} ms < -{clock_err_ms} ms")
    return lat


def training_labels(records):
    """Only traded prints and firm quotes may become labels or simulated fills."""
    return [r for r in records if r.kind in TRAINABLE]


def trace_regime(ts: pd.Timestamp) -> str:
    """Affiliate-indicator regime (voluntary 2026-08-31, mandatory 2027-08-02, per FINRA Notice 26-16)."""
    if ts < pd.Timestamp("2026-08-31"):
        return "no_flag"
    if ts < pd.Timestamp("2027-08-02"):
        return "flag_voluntary"
    return "flag_mandatory"


def dedupe_trace(prints: pd.DataFrame, window_s: float = 1.0) -> pd.DataFrame:
    """Mark (never delete) likely affiliate duplicates.
    Rule 1: affiliate_flag True -> duplicate leg.
    Rule 2 (no flag): same instrument, equal price and size, opposite sides, within window_s -> later leg."""
    df = prints.sort_values(["instrument_key", "event_time"]).reset_index(drop=True).copy()
    df["dup"] = df["affiliate_flag"].map(lambda v: v is True).astype(bool)
    df["dup_reason"] = np.where(df["dup"], "affiliate_flag", "")
    for _, g in df.groupby("instrument_key"):
        idx = g.index.to_list()
        for pos, a in enumerate(idx):
            if df.at[a, "dup"]:
                continue
            for b in idx[pos + 1:]:
                dt = (df.at[b, "event_time"] - df.at[a, "event_time"]).total_seconds()
                if dt > window_s:
                    break
                if (not df.at[b, "dup"] and df.at[b, "price"] == df.at[a, "price"]
                        and df.at[b, "size_mm"] == df.at[a, "size_mm"]
                        and df.at[b, "side"] != df.at[a, "side"]):
                    df.at[b, "dup"] = True
                    df.at[b, "dup_reason"] = "inferred_pair"
                    break
    df["regime"] = df["event_time"].map(trace_regime)
    return df


# Sanity 1: one inferred pair; size mismatch and a 5-second gap are not duplicates.
t0 = pd.Timestamp("2026-06-15 14:00:00")
ms = lambda k: pd.Timedelta(milliseconds=k)
prints = pd.DataFrame({
    "instrument_key": ["INS-000117"] * 5 + ["INS-000245"] * 2,
    "event_time": [t0, t0 + ms(300), t0 + ms(40_000), t0 + ms(40_200), t0 + ms(90_000), t0, t0 + ms(5_000)],
    "price": [97.25, 97.25, 97.10, 97.10, 97.00, 101.50, 101.50],
    "size_mm": [5.0, 5.0, 2.0, 1.0, 3.0, 1.0, 1.0],
    "side": ["S", "B", "S", "B", "S", "B", "S"],
    "affiliate_flag": [None] * 7,
})
deduped = dedupe_trace(prints)
assert int(deduped["dup"].sum()) == 1
assert deduped.loc[deduped["dup"], "dup_reason"].iloc[0] == "inferred_pair"
assert set(deduped["regime"]) == {"no_flag"}

# Sanity 2: provenance gate and clock-fault detection.
recs = [PriceRecord("INS-000117", 97.25, "PRICE", "B", 5.0, PriceKind.TRADED, "TRACE", 0, 2_000_000),
        PriceRecord("INS-000117", 97.40, "PRICE", "M", 0.0, PriceKind.COMPOSITE, "VENDOR_X", 0, 500_000),
        PriceRecord("INS-000117", 97.30, "PRICE", "B", 2.0, PriceKind.INDICATIVE_RUN, "RUN_PARSER", 0, 9_000_000)]
assert [r.kind for r in training_labels(recs)] == [PriceKind.TRADED]
assert abs(latency_ms(recs[0], clock_err_ms=0.001) - 2.0) < 1e-12
try:
    latency_ms(PriceRecord("INS-000117", 97.0, "PRICE", "B", 1.0, PriceKind.TRADED, "TRACE", 5_000_000, 0), 1.0)
    raise AssertionError("negative latency beyond the clock bound must raise")
except ValueError:
    pass
```


### Listing 27.2: The bitemporal security master {#code-27-2}

```python
# block 2 of 5: bitemporal security master; append-only on the knowledge axis.
OPEN = pd.Timestamp.max


class BitemporalMaster:
    COLS = ["instrument_key", "attr", "value", "valid_from", "valid_to", "known_from", "known_to"]

    def __init__(self):
        self.rows = []
        self._last_known = pd.Timestamp.min

    def assert_fact(self, key, attr, value, valid_from, valid_to=OPEN, known_at=None):
        """As of knowledge time known_at, attr of key had value over [valid_from, valid_to).
        Currently believed rows that overlap are closed (known_to = known_at) and their
        non-overlapping remainders re-inserted; nothing is edited or deleted."""
        kt, vf, vt = pd.Timestamp(known_at), pd.Timestamp(valid_from), pd.Timestamp(valid_to)
        if not vf < vt:
            raise ValueError("empty valid interval")
        if kt < self._last_known:
            raise ValueError("knowledge time must be non-decreasing (append-only axis)")
        self._last_known = kt
        new_rows = []
        for r in self.rows:
            if r["instrument_key"] != key or r["attr"] != attr or r["known_to"] != OPEN:
                continue
            if r["valid_to"] <= vf or r["valid_from"] >= vt:
                continue
            r["known_to"] = kt
            if r["valid_from"] < vf:
                new_rows.append(dict(r, valid_to=vf, known_from=kt, known_to=OPEN))
            if r["valid_to"] > vt:
                new_rows.append(dict(r, valid_from=vt, known_from=kt, known_to=OPEN))
        new_rows.append(dict(instrument_key=key, attr=attr, value=value, valid_from=vf,
                             valid_to=vt, known_from=kt, known_to=OPEN))
        self.rows.extend(new_rows)

    def as_of(self, key, attr, valid_t, known_t):
        tv, tk = pd.Timestamp(valid_t), pd.Timestamp(known_t)
        hits = [r["value"] for r in self.rows
                if r["instrument_key"] == key and r["attr"] == attr
                and r["valid_from"] <= tv < r["valid_to"] and r["known_from"] <= tk < r["known_to"]]
        if len(hits) > 1:
            raise RuntimeError(f"exclusion violated for {key}.{attr}")
        return hits[0] if hits else None

    def snapshot(self, known_t):
        tk = pd.Timestamp(known_t)
        live = [r for r in self.rows if r["known_from"] <= tk < r["known_to"]]
        # known_to is excluded: closing a row later changes its known_to, not what was visible at tk.
        df = pd.DataFrame(live, columns=self.COLS[:-1]).astype({"value": object})
        return df.sort_values(["instrument_key", "attr", "valid_from"]).reset_index(drop=True)

    def check_exclusion(self):
        def live(r):
            return r["known_from"] < r["known_to"]
        for i, a in enumerate(self.rows):
            for b in self.rows[i + 1:]:
                if (a["instrument_key"], a["attr"]) != (b["instrument_key"], b["attr"]):
                    continue
                if (live(a) and live(b) and a["valid_from"] < b["valid_to"] and b["valid_from"] < a["valid_to"]
                        and a["known_from"] < b["known_to"] and b["known_from"] < a["known_to"]):
                    return False
        return True


sm = BitemporalMaster()
ONBOARD = "2016-11-01"          # illustrative onboarding date for the 2016 facilities
CLOSE_KNOWN = "2020-06-22 18:00"  # illustrative: when the desk's event feed confirmed the closing
EFF = "2020-06-22"
sm.assert_fact("INS-SERTA-TL1-2016", "ranking", "first_lien_pari", ONBOARD, known_at=ONBOARD)
sm.assert_fact("INS-SERTA-TL2-2016", "ranking", "second_lien", ONBOARD, known_at=ONBOARD)
sm.assert_fact("INS-SERTA-FO-2020", "ranking", "super_priority_first_out", EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-SO-2020", "ranking", "super_priority_second_out", EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-TL1-2016", "ranking", "first_lien_behind_super_priority", EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-TL2-2016", "ranking", "second_lien_behind_super_priority", EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-FO-2020", "face_usd_mm_approx", 200.0, EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-SO-2020", "face_usd_mm_approx", 875.0, EFF, known_at=CLOSE_KNOWN)
sm.assert_fact("INS-SERTA-TL1-2016", "omp_litigation", "pending", EFF, known_at=CLOSE_KNOWN)

# The three Serta questions.
assert sm.as_of("INS-SERTA-TL1-2016", "ranking", "2020-06-23", "2030-01-01") == "first_lien_behind_super_priority"
assert sm.as_of("INS-SERTA-TL1-2016", "ranking", "2020-06-23", "2020-06-22 00:00") == "first_lien_pari"
assert sm.as_of("INS-SERTA-SO-2020", "ranking", "2020-06-23", "2020-06-22 00:00") is None
assert sm.as_of("INS-SERTA-TL1-2016", "ranking", "2019-06-01", "2030-01-01") == "first_lien_pari"

# The past is immutable: a later fact (Fifth Circuit, 2024-12-31) leaves the 2020 snapshot unchanged.
snap_2020 = sm.snapshot("2020-06-24")
sm.assert_fact("INS-SERTA-TL1-2016", "omp_litigation", "5th_cir_not_open_market_purchase",
               "2024-12-31", known_at="2025-01-02")
assert snap_2020.equals(sm.snapshot("2020-06-24"))
assert sm.as_of("INS-SERTA-TL1-2016", "omp_litigation", "2025-06-01", "2025-06-01") == "5th_cir_not_open_market_purchase"
assert sm.as_of("INS-SERTA-TL1-2016", "omp_litigation", "2023-06-01", "2025-06-01") == "pending"
assert sm.check_exclusion()
try:
    sm.assert_fact("INS-SERTA-TL1-2016", "ranking", "rewrite_history", "2016-11-01", known_at="2019-01-01")
    raise AssertionError("writing into the past of the knowledge axis must fail")
except ValueError:
    pass
```


### Listing 27.3: Latency as a queue: Pollaczek-Khinchine, the Lindley simulation and fan-out tails {#code-27-3}

```python
# block 3 of 5: latency as a queue. Pollaczek-Khinchine, Lindley simulation, fan-out tails.
def pk_mean_wait(rho, mean_s, cs2, ca2=1.0):
    """Kingman / Pollaczek-Khinchine mean queueing delay (exact for M/G/1, i.e. ca2 == 1)."""
    if not 0.0 <= rho < 1.0:
        raise ValueError("utilisation must be in [0, 1); at rho >= 1 there is no steady state")
    return rho / (1.0 - rho) * (ca2 + cs2) / 2.0 * mean_s


def wait_quantile_approx(rho, mean_wait, q):
    """t with P(Wq > t) = 1 - q under P(Wq > t) ~ rho * exp(-rho t / E[Wq])."""
    tail = 1.0 - q
    return 0.0 if tail >= rho else mean_wait / rho * math.log(rho / tail)


def simulate_mg1(n, rho, mean_s, cs2, rng):
    """Lindley recursion W_{k+1} = max(0, W_k + S_k - A_{k+1}), vectorised as X_k - min_{j<=k} X_j."""
    shape = 1.0 / cs2
    s = rng.gamma(shape, mean_s / shape, size=n)       # mean mean_s, squared CV cs2
    a = rng.exponential(mean_s / rho, size=n)           # Poisson arrivals at rate rho / mean_s
    x = np.concatenate([[0.0], np.cumsum(s[:-1] - a[1:])])
    w = x - np.minimum.accumulate(x)
    return w, s


def fanout_slow_prob(p_slow, n):
    return 1.0 - (1.0 - p_slow) ** n


MEAN_S, CS2, RHO = 40.0, 4.0, 0.7                       # ms; the cold-open pricing engine
ew = pk_mean_wait(RHO, MEAN_S, CS2)
assert abs(ew - 233.33) < 0.01
w, s = simulate_mg1(1_000_000, RHO, MEAN_S, CS2, RNG)
w, s = w[20_000:], s[20_000:]                           # burn-in
assert abs(w.mean() / ew - 1.0) < 0.10                  # simulation agrees with P-K
p99_wait_sim = float(np.quantile(w, 0.99))
p99_wait_approx = wait_quantile_approx(RHO, ew, 0.99)
assert 0.75 < p99_wait_approx / p99_wait_sim < 1.33     # exponential-tail approximation is serviceable
p99_sojourn = float(np.quantile(w + s, 0.99))
assert 1_000.0 < p99_sojourn < 2_400.0                  # "about a second and a half"
assert pk_mean_wait(0.9, MEAN_S, CS2) > 3.5 * ew        # load and danger arrive together

# Fan-out: Dean-Barroso's 63% at n = 100, and the 150-line PT at 78%.
assert abs(fanout_slow_prob(0.01, 100) - 0.634) < 0.001
assert abs(fanout_slow_prob(0.01, 150) - 0.779) < 0.001
slow = (RNG.random((20_000, 150)) < 0.01).any(axis=1).mean()
assert abs(slow - fanout_slow_prob(0.01, 150)) < 0.015
q_line = 0.99 ** (1 / 150)
assert 0.99993 < q_line < 0.99994                       # each line's p99.993
```


### Listing 27.4: Trigger tables for quote pulling: sensitivities and the joint and per-instrument rules {#code-27-4}

```python
# block 4 of 5: trigger tables. Sensitivities, joint vs per-instrument rules, fixed point, pick-off cost.
def beta_rate(dv01_bond, dv01_hedge, rate_beta):
    """Bond points per hedge point for a rate hedge: dollar-duration ratio times empirical rate beta."""
    return dv01_bond / dv01_hedge * rate_beta


def beta_credit(price, d_spr, dts_beta, etf_price, etf_d_spr):
    """Bond points per ETF point: dP = -P D dS_i, dS_i = dts_beta dS_HY, dH = -H D_H dS_HY."""
    return price * d_spr * dts_beta / (etf_price * etf_d_spr)


def allocate_tau(beta, sigma_h, theta):
    """Per-instrument thresholds in hedge units: theta_j = c |beta_j| sigma_j, sum theta_j = theta."""
    w = np.abs(beta) * sigma_h
    theta_j = theta * w / w.sum()
    return theta_j / np.abs(beta)


def joint_pull(beta, dH, theta, side):
    """side = +1 for a live bid, -1 for a live offer."""
    return side * float(beta @ dH) < -theta


def box_pull(tau, dH):
    return bool(np.any(np.abs(dH) > tau))


def bachelier_pickoff(h, sigma, dt):
    """E[(b - P_{t+dt})^+] with b = P_t - h; P diffuses with vol sigma in points per sqrt(second)."""
    sd = sigma * math.sqrt(dt)
    x = h / sd
    return sd * (stats.norm.pdf(x) - x * stats.norm.sf(x))


# The cold-open row (inputs illustrative).
beta = np.array([beta_rate(95 * 8.0 / 1e4, 0.065, 0.9),
                 beta_credit(95.0, 8.0, 130 / 325, 80.0, 3.0)])        # [TY, HYG]
H_HALF, MIN_MARGIN, GUARD = 0.19, 0.04, 0.01
THETA = H_HALF - MIN_MARGIN - GUARD
SIGMA_H = np.array([0.10, 0.08])                                       # stress-window hedge vols, points (illustrative)
tau = allocate_tau(beta, SIGMA_H, THETA)
move = np.array([-6 / 32, -0.14])                                      # TY -6/32, HYG -14 cents
assert abs(float(beta @ move) + 0.375) < 0.005                         # three-eighths
assert joint_pull(beta, move, THETA, side=+1) and box_pull(tau, move)  # both rules pull the bid

# Flight to quality: TY up, HYG down, fair value flat. The cheap rule panics; the joint rule does not.
offset = np.array([6 / 32, -0.15])
assert abs(float(beta @ offset)) < 0.02
assert box_pull(tau, offset) and not joint_pull(beta, offset, THETA, +1) and not joint_pull(beta, offset, THETA, -1)

# Safety theorem on 200,000 simulated moves (negatively correlated, fat-tailed via a scale mixture).
n = 200_000
cov = np.array([[1.0, -0.4], [-0.4, 1.0]]) * np.outer(SIGMA_H, SIGMA_H)
dH = RNG.multivariate_normal(np.zeros(2), cov, size=n) * np.sqrt(RNG.chisquare(4, size=(n, 1)) / 4) ** -1
TICK = np.array([1 / 64, 0.01])                                        # hedge price grids (illustrative)
ticks = np.round(dH / TICK).astype(np.int64)
dH = ticks * TICK                                                      # both rules see on-grid moves
fv = dH @ beta                                                         # linearised fair-value moves
jp = np.abs(fv) > THETA                                                # joint rule, either side
bp = (np.abs(dH) > tau).any(axis=1)                                    # per-instrument rule
assert not np.any(jp & ~bp)                                            # never misses a joint pull
false_pull_rate = float((bp & ~jp).mean())
assert bp.mean() >= jp.mean() and false_pull_rate > 0.0                # safety is paid for in false pulls

# Fixed point: beta in Q.16 bond points per tick; integer multiply-accumulate; error bound holds.
FRAC = 16
beta_q = np.round(beta * TICK * (1 << FRAC)).astype(np.int64)
theta_q = int(math.floor(THETA * (1 << FRAC)))
acc = ticks @ beta_q                                                   # int64, as on DSP slices
fixed_pull = (acc < -theta_q) | (acc > theta_q)
exact = ticks @ (beta * TICK)
bound = 2.0 ** (-FRAC - 1) * np.abs(ticks).sum(axis=1) + 2.0 ** -FRAC
mismatch = fixed_pull != jp
assert np.all(np.abs(np.abs(exact[mismatch]) - THETA) <= bound[mismatch])
max_ticks = float((2.0 / TICK).sum())                                  # moves up to 2 points per refresh;
assert 2.0 ** (-FRAC - 1) * max_ticks + 2.0 ** -FRAC < GUARD           # larger ones hit Tier-0 collars first

# Pick-off: closed form vs Monte Carlo at 15 minutes; zero at 1.5 s; the jump loss is the cold open.
SIGMA_S = 0.5 / math.sqrt(23_400)
z = RNG.standard_normal(2_000_000)
mc = np.maximum(-H_HALF - SIGMA_S * math.sqrt(900.0) * z, 0.0).mean()
assert abs(mc - bachelier_pickoff(H_HALF, SIGMA_S, 900.0)) < 5e-5
assert bachelier_pickoff(H_HALF, SIGMA_S, 1.5) < 1e-12
jump_loss_usd = max(abs(float(beta @ move)) - H_HALF, 0.0) * 3_000_000 / 100
assert 5_000 < jump_loss_usd < 6_000
```


### Listing 27.5: Kill switches: CUSUM run lengths against Siegmund, and a tiered switch {#code-27-5}

```python
# block 5 of 5: kill switches. CUSUM run lengths vs Siegmund; tiered switch with authority rules.
def siegmund_arl(drift, c):
    """ARL of G_k = max(0, G_{k-1} + X_k), X ~ N(drift, 1), alarm at G >= c."""
    b = c + 1.166
    if abs(drift) < 1e-12:
        return b * b
    return (math.exp(-2.0 * drift * b) + 2.0 * drift * b - 1.0) / (2.0 * drift ** 2)


def simulate_arl(drift, c, runs, rng, max_steps=200_000):
    g = np.zeros(runs)
    alarm_at = np.full(runs, -1)
    alive = np.ones(runs, dtype=bool)
    k = 0
    while alive.any() and k < max_steps:
        k += 1
        g[alive] = np.maximum(0.0, g[alive] + rng.normal(drift, 1.0, int(alive.sum())))
        hit = alive & (g >= c)
        alarm_at[hit] = k
        alive &= ~hit
    if alive.any():
        raise RuntimeError("raise max_steps")
    return float(alarm_at.mean())


DELTA, C = 1.0, 5.0
arl0, arl1 = siegmund_arl(-DELTA / 2, C), siegmund_arl(+DELTA / 2, C)
assert 930 < arl0 < 945 and 10.0 < arl1 < 10.6
assert abs(simulate_arl(-DELTA / 2, C, 2_000, RNG) / arl0 - 1.0) < 0.10
assert abs(simulate_arl(+DELTA / 2, C, 2_000, RNG) / arl1 - 1.0) < 0.10
assert siegmund_arl(-0.5, 6.0) > 2.5 * arl0 and siegmund_arl(0.5, 6.0) - arl1 < 2.5


class KillSwitch:
    """Any authorised tripper (human or monitor) trips instantly; a trip cancels all live orders.
    Re-arm needs two distinct authorised humans and a passing slow-path check."""

    def __init__(self, limits, can_trip, can_rearm):
        self.limits, self.can_trip, self.can_rearm = limits, set(can_trip), set(can_rearm)
        self.state, self.log, self.live, self.votes = "ARMED", [], {}, set()
        self.msg_times, self.last_heartbeat = [], 0.0

    def _trip(self, tier, reason, t):
        if self.state == "TRIPPED":
            return []
        self.state = "TRIPPED"
        self.log.append((t, tier, reason))
        cancelled = sorted(self.live)
        self.live.clear()
        self.votes.clear()
        return cancelled

    def pre_trade(self, order, t):
        """Tier 0 hard limits. There is deliberately no override parameter."""
        if self.state != "ARMED":
            return False, "switch_tripped"
        lim = self.limits
        self.msg_times = [x for x in self.msg_times if t - x < 1.0] + [t]
        if len(self.msg_times) > lim["max_msgs_per_s"]:
            self._trip(0, "message_rate", t)
            return False, "message_rate"
        if order["price_type"] == "PRICE" and not lim["price_floor"] <= order["price"] <= lim["price_cap"]:
            return False, "price_type_sanity"
        if abs(order["price"] - order["ref_price"]) > lim["collar_pts"]:
            return False, "price_collar"
        if order["qty_mm"] > lim["max_order_mm"]:
            return False, "max_order_value"
        if sum(o["qty_mm"] for o in self.live.values()) + order["qty_mm"] > lim["max_live_mm"]:
            return False, "max_live_notional"
        self.live[order["id"]] = order
        return True, "ok"

    def heartbeat(self, t):
        self.last_heartbeat = t

    def check_deadman(self, t):
        if t - self.last_heartbeat > self.limits["heartbeat_s"]:
            return self._trip(2, "heartbeat_lost", t)
        return []

    def trip(self, who, tier, reason, t):
        if who not in self.can_trip:
            raise PermissionError(who)
        return self._trip(tier, reason, t)

    def rearm(self, who, t, slow_path_ok):
        if who not in self.can_rearm:
            raise PermissionError(who)
        if self.state != "TRIPPED":
            return False
        self.votes.add(who)
        if len(self.votes) >= 2 and slow_path_ok:
            self.state = "ARMED"
            self.log.append((t, "rearm", tuple(sorted(self.votes))))
            self.votes.clear()
            return True
        return False


LIMITS = dict(max_msgs_per_s=50, price_floor=10.0, price_cap=200.0, collar_pts=2.0,
              max_order_mm=50.0, max_live_mm=150.0, heartbeat_s=2.0)
ks = KillSwitch(LIMITS, can_trip={"ines", "theo", "robo_monitor", "cusum_monitor"}, can_rearm={"ines", "theo"})
good = dict(id="o1", price_type="PRICE", price=95.10, ref_price=95.00, qty_mm=3.0)
assert ks.pre_trade(good, t=0.0) == (True, "ok")
fat_basket = dict(id="o2", price_type="PRICE", price=95.00, ref_price=95.00, qty_mm=444_000.0)
assert ks.pre_trade(fat_basket, t=0.1) == (False, "max_order_value")      # the whole basket, hard-blocked
spread_as_price = dict(id="o3", price_type="PRICE", price=105.0, ref_price=95.0, qty_mm=1.0)
assert ks.pre_trade(spread_as_price, t=0.2) == (False, "price_collar")     # 105 bp read as 105 points
try:
    ks.pre_trade(good, t=0.3, override=True)
    raise AssertionError("there is no pop-up to click through")
except TypeError:
    pass

ks.heartbeat(0.0)
assert ks.check_deadman(1.0) == []
assert ks.check_deadman(2.5) == ["o1"] and ks.state == "TRIPPED"          # dead man cancels everything
assert ks.pre_trade(good, t=2.6) == (False, "switch_tripped")
try:
    ks.rearm("robo_monitor", 3.0, slow_path_ok=True)
    raise AssertionError("machines may trip but never re-arm")
except PermissionError:
    pass
assert not ks.rearm("theo", 3.1, True) and not ks.rearm("theo", 3.2, True)  # one human is not two
assert not ks.rearm("ines", 3.3, slow_path_ok=False)                        # two humans, failing check
assert ks.rearm("ines", 3.4, slow_path_ok=True) and ks.state == "ARMED"
```


## F.28: Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha {#code-28}

Listings from `28_ch28_pm_playbook.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 28.1: Block 1: Effective breadth and the hit-rate law {#code-28-1}

```python
import numpy as np
import pandas as pd
from scipy import stats, optimize, integrate

RNG = np.random.default_rng(2028)
TRADING_DAYS = 252


def herfindahl_breadth(gmv_weights):
    """1/H on absolute GMV weights. Net positions to issuer level BEFORE calling."""
    w = np.abs(np.asarray(gmv_weights, dtype=float))
    total = w.sum()
    if total <= 0.0:
        raise ValueError("book has no gross exposure")
    w = w / total
    return 1.0 / np.sum(w ** 2)


def effective_breadth(weights, cov):
    """Eq. (28.4): (sum |w_i| sigma_i)^2 / (w' Sigma w), on the IDIOSYNCRATIC covariance."""
    w = np.asarray(weights, dtype=float)
    cov = np.asarray(cov, dtype=float)
    sig = np.sqrt(np.clip(np.diag(cov), 0.0, None))
    num = float(np.abs(w) @ sig) ** 2
    den = float(w @ cov @ w)
    if den <= 1e-18 * max(num, 1e-300):
        raise ValueError("near-zero book variance: hedged pairs? net to issuer first")
    return num / den


def issuer_block_cov(issuer_ids, sigma, rho_within, rho_across):
    """Residual covariance with one correlation inside an issuer and another across issuers."""
    ids = np.asarray(issuer_ids)
    same = ids[:, None] == ids[None, :]
    corr = np.where(same, rho_within, rho_across).astype(float)
    np.fill_diagonal(corr, 1.0)
    sig = np.asarray(sigma, dtype=float)
    return corr * np.outer(sig, sig)


def n_eff_equal_blocks(n_bonds, bonds_per_issuer, rho_within, rho_across):
    """Eq. (28.5), closed form for equal issuer blocks."""
    m = bonds_per_issuer
    return n_bonds / (1.0 + (m - 1) * rho_within + (n_bonds - m) * rho_across)


def ir_from_hit_rate(p, n_eff, periods=TRADING_DAYS, exact=False):
    """Eq. (28.3). exact=True keeps the sqrt(1-(2p-1)^2) term."""
    edge = 2.0 * p - 1.0
    ir = edge * np.sqrt(periods * n_eff)
    return ir / np.sqrt(1.0 - edge ** 2) if exact else ir


def hit_rate_se(p, n_eff, periods=TRADING_DAYS):
    """Eq. (28.6): standard error of one year's measured hit rate."""
    return np.sqrt(p * (1.0 - p) / (periods * n_eff))


# --- Theo's book: 300 bonds, 60 issuers x 5 bonds -------------------------------
issuers = np.repeat(np.arange(60), 5)
sig_bond = np.full(300, 0.051)                       # DTS 0.147 x sigma_rel 0.35 (illustrative)
cov_book = issuer_block_cov(issuers, sig_bond, rho_within=0.9, rho_across=0.01)
w_book = np.full(300, 1.0 / 300)

neff_num = effective_breadth(w_book, cov_book)
neff_cf = n_eff_equal_blocks(300, 5, 0.9, 0.01)
assert abs(neff_num - neff_cf) < 1e-8, (neff_num, neff_cf)
assert 39.0 < neff_cf < 40.5                          # "300 bonds, 60 issuers, 40 bets"
assert abs(herfindahl_breadth(w_book) - 300.0) < 1e-9 # 1/H ignores correlation entirely
assert abs(n_eff_equal_blocks(10**7, 5, 0.9, 0.01) - 100.0) < 0.01  # speed-of-light limit 1/rho_a

# Independent and perfectly correlated limits of (28.4)
assert abs(effective_breadth(np.full(50, 0.02), np.eye(50) * 0.04) - 50.0) < 1e-9
assert abs(effective_breadth(np.full(50, 0.02), np.full((50, 50), 0.04)) - 1.0) < 1e-9

# Paleologo's 0.33% standard error: about 90 effective names at p = 0.505
assert abs(hit_rate_se(0.505, 91) - 0.0033) < 1e-4
assert abs(hit_rate_se(0.505, 40) - 0.0050) < 2e-4   # a 40-bet credit PM: SE equals the edge

# Monte Carlo check of the hit-rate law: daily wins ~ Binomial(N, p), return = (2W - N)/N
p_hit, n_bets, n_days = 0.52, 40, TRADING_DAYS * 400
wins = RNG.binomial(n_bets, p_hit, size=n_days)
daily = (2.0 * wins - n_bets) / n_bets
ir_mc = daily.mean() / daily.std(ddof=1) * np.sqrt(TRADING_DAYS)
ir_exact = ir_from_hit_rate(p_hit, n_bets, exact=True)
assert abs(ir_mc - ir_exact) < 0.15, (ir_mc, ir_exact)          # MC SE ~ 0.05
assert abs(ir_exact / ir_from_hit_rate(p_hit, n_bets) - 1.0) < 1e-3
```


### Listing 28.2: Block 2: The horizon ladder {#code-28-2}

```python
# --- Block 2: the horizon ladder ------------------------------------------------
TIERS = pd.DataFrame(
    {"instruments": ["CDX/iTraxx, index futures, credit ETFs",
                     "liquid IG/HY cash, PT-eligible",
                     "stressed, LMT candidates, post-reorg"],
     "rt_cost": [0.0005, 0.006, 0.025]},          # round-trip cost, fraction of price (illustrative)
    index=pd.Index([0, 1, 2], name="tier"),
)

SIGNALS = pd.DataFrame(
    {"alpha0":       [0.05,    0.03,  0.02,   0.015, 0.012, 0.08],   # annual rate at inception (illustrative)
     "half_life_yr": [3 / 252, 1 / 12, 2 / 12, 0.75,  1.0,   0.5],
     "tiers":        [(0,),    (0, 1), (1,),   (1, 2), (1, 2), (2,)]},  # tiers able to express the signal
    index=pd.Index(["etf_premium", "index_trend", "momentum", "value", "carry", "lmt_event"],
                   name="signal"),
)


def break_even_half_life(rt_cost, alpha0):
    """Eq. (28.8): shortest half-life (years) that pays its own round-trip cost."""
    if alpha0 <= 0.0:
        return np.inf
    return np.log(2.0) * rt_cost / alpha0


def net_alpha(alpha0, half_life_yr, rt_cost):
    """Eq. (28.7): alpha0 - (ln 2 / h) * c_RT, annualized."""
    if half_life_yr <= 0.0:
        raise ValueError("half-life must be positive")
    return alpha0 - np.log(2.0) / half_life_yr * rt_cost


def horizon_ladder(signals, tiers):
    rows = []
    for name, sg in signals.iterrows():
        nets = {t: net_alpha(sg.alpha0, sg.half_life_yr, tiers.loc[t, "rt_cost"]) for t in sg.tiers}
        best = max(nets, key=nets.get)
        rows.append({"signal": name, "best_tier": best if nets[best] > 0 else None,
                     "net_alpha": nets[best], "tie_breaker_only": nets[best] <= 0,
                     **{f"net_t{t}": v for t, v in nets.items()}})
    return pd.DataFrame(rows).set_index("signal")


ladder = horizon_ladder(SIGNALS, TIERS)

assert ladder.loc["index_trend", "best_tier"] == 0               # trend lives in the index layer
assert ladder.loc["index_trend", "net_t1"] < 0 < ladder.loc["index_trend", "net_t0"]
assert ladder.loc["value", "best_tier"] == 1 and ladder.loc["value", "net_t2"] < 0
assert ladder.loc["lmt_event", "best_tier"] == 2 and ladder.loc["lmt_event", "net_alpha"] > 0.04
assert bool(ladder.loc["momentum", "tie_breaker_only"])          # cash momentum: tie-breaker only
assert break_even_half_life(0.0005, 0.03) * TRADING_DAYS < 5      # tier 0: under a week
assert 1.0 < break_even_half_life(0.006, 0.03) * 12 < 3.0         # tier 1: 1-3 months
```


### Listing 28.3: Block 3: Kelly with jumps {#code-28-3}

```python
# --- Block 3: Kelly with jump-to-default ----------------------------------------
def kelly_binary(p_surv, carry, loss):
    """Eq. (28.9): f* = p/L - q/c, floored at zero (long-only)."""
    q = 1.0 - p_surv
    return max(p_surv / loss - q / carry, 0.0)


def growth_binary(f, p_surv, carry, loss):
    if f * loss >= 1.0:
        return -np.inf
    return p_surv * np.log1p(f * carry) + (1.0 - p_surv) * np.log1p(-f * loss)


def growth_jump(f, carry, lam, loss, sigma=0.0):
    """Eq. (28.10): g(f) = f c - f^2 sigma^2 / 2 + lam ln(1 - f L). lam is P-measure."""
    diffusive = f * carry - 0.5 * f * f * sigma * sigma
    if lam <= 0.0:
        return diffusive
    if f * loss >= 1.0:
        return -np.inf
    return diffusive + lam * np.log1p(-f * loss)


def kelly_jump(carry, lam, loss, sigma=0.0):
    """Eqs. (28.11)-(28.12): the root of the FOC inside the ruin boundary 1/L."""
    edge = carry - lam * loss
    if edge <= 0.0:
        return 0.0
    if lam <= 0.0:                                     # no jump: Merton's mu / sigma^2
        return edge / sigma ** 2 if sigma > 0.0 else np.inf
    b = carry * loss + sigma ** 2
    disc = (carry * loss - sigma ** 2) ** 2 + 4.0 * sigma ** 2 * lam * loss ** 2
    return 2.0 * edge / (b + np.sqrt(disc))


def kelly_merton_approx(carry, lam, loss, sigma):
    """Diffusion approximation (comparison only): (c - lam L) / (sigma^2 + lam L^2)."""
    return max((carry - lam * loss) / (sigma ** 2 + lam * loss ** 2), 0.0)


def kelly_multiplier(rel_se_edge):
    """Eq. (28.13): optimal fraction of Kelly when the edge has relative s.e. s."""
    return 1.0 / (1.0 + rel_se_edge ** 2)


def growth_random_loss(f, carry, lam, a, b, loss_max, sigma=0.0):
    """g(f) with L = loss_max * Beta(a, b). Defined for f < 1 / loss_max."""
    if f * loss_max >= 1.0:
        return -np.inf
    dist = stats.beta(a, b)
    e_log, _ = integrate.quad(lambda u: np.log1p(-f * loss_max * u) * dist.pdf(u), 0.0, 1.0, limit=200)
    return f * carry - 0.5 * f * f * sigma * sigma + lam * e_log


def kelly_random_loss(carry, lam, a, b, loss_max, sigma=0.0):
    upper = (1.0 - 1e-6) / loss_max
    res = optimize.minimize_scalar(
        lambda f: -growth_random_loss(f, carry, lam, a, b, loss_max, sigma),
        bounds=(0.0, upper), method="bounded", options={"xatol": 1e-8})
    return float(res.x)


def kelly_cluster(n_names, carry, lam_idio, lam_common, loss):
    """Eq. (28.14): per-name fraction for n symmetric names with one common default jump."""
    def foc(f):
        return (carry - lam_idio * loss / (1.0 - f * loss)
                - lam_common * loss / (1.0 - n_names * f * loss))
    if foc(0.0) <= 0.0:
        return 0.0
    hi = (1.0 - 1e-12) / (n_names * loss)
    return optimize.brentq(foc, 0.0, hi, xtol=1e-14)


# Kaz's 93%: c = 4.5%, q = 3.1%, L = 0.6
f_kaz = kelly_binary(0.969, 0.045, 0.60)
assert abs(f_kaz - 0.926) < 1e-3
step = 1e-6
dg = (growth_binary(f_kaz + step, 0.969, 0.045, 0.6)
      - growth_binary(f_kaz - step, 0.969, 0.045, 0.6)) / (2 * step)
assert abs(dg) < 1e-6 and f_kaz < 1.0 / 0.6                   # FOC holds, inside the ruin boundary
q_star = 0.045 / (0.045 + 0.6)                                 # edge condition q < c / (c + L)
assert kelly_binary(1 - q_star + 1e-4, 0.045, 0.6) > 0.0
assert kelly_binary(1 - q_star - 1e-4, 0.045, 0.6) == 0.0

# Continuous time: closed form, FOC, and Merton's approximation crossing the ruin boundary
assert abs(kelly_jump(0.045, 0.031, 0.6) - (1 / 0.6 - 0.031 / 0.045)) < 1e-12
f_j = kelly_jump(0.045, 0.031, 0.6, sigma=0.05)
assert abs(0.045 - f_j * 0.05 ** 2 - 0.031 * 0.6 / (1 - f_j * 0.6)) < 1e-12
assert 0.93 < f_j < 0.95
f_m = kelly_merton_approx(0.045, 0.031, 0.6, 0.05)
assert f_m * 0.6 > 1.0 > f_j * 0.6                             # one default wipes out the Merton bettor
g_star = growth_jump(f_j, 0.045, 0.031, 0.6, 0.05)
assert g_star > growth_jump(0.9 * f_j, 0.045, 0.031, 0.6, 0.05)
assert g_star > growth_jump(1.1 * f_j, 0.045, 0.031, 0.6, 0.05)

# The Q-measure proof: under the credit triangle there is no edge
assert kelly_jump(0.045, 0.045 / 0.6, 0.6) < 1e-9

# Fractional Kelly: exact 75% at half Kelly for quadratic growth; Monte Carlo check of (28.13)
f_d = kelly_jump(0.03, 0.0, 0.6, sigma=0.10)                   # pure diffusion: mu / sigma^2 = 3
assert abs(f_d - 3.0) < 1e-12
assert abs(growth_jump(0.5 * f_d, 0.03, 0.0, 0.6, 0.10) / growth_jump(f_d, 0.03, 0.0, 0.6, 0.10) - 0.75) < 1e-12
eps = RNG.normal(0.0, 1.0, size=200_000)                       # relative s.e. of the edge = 100%
thetas = np.linspace(0.05, 1.5, 146)
ratio = [np.mean(2 * t * (1 + eps) - (t * (1 + eps)) ** 2) for t in thetas]
assert abs(thetas[int(np.argmax(ratio))] - kelly_multiplier(1.0)) < 0.03

# Random recovery: Jensen lowers f*, and the worst recovery sets the boundary
f_const = kelly_jump(0.045, 0.031, 0.6)
f_loose = kelly_random_loss(0.045, 0.031, 3.0, 2.0, 1.00)      # mean L = 0.6, docs allow L -> 1
f_tight = kelly_random_loss(0.045, 0.031, 8.0, 2.0, 0.75)      # mean L = 0.6, recovery floor 25%
assert f_loose < f_tight < f_const
assert f_loose < 1.0 and f_tight < 1.0 / 0.75

# Clusters: a common jump shrinks every name, and the cluster obeys sum f L < 1
f_alone = kelly_jump(0.084, 0.04 + 0.02, 0.55)
f_clu = kelly_cluster(5, 0.084, 0.04, 0.02, 0.55)
assert 0.0 < f_clu < f_alone and 5 * f_clu * 0.55 < 1.0
assert kelly_cluster(5, 0.084, 0.04, 0.03, 0.55) < f_clu

# The 2026 CCC case: the edge rose while Kelly fell
f_jan, f_oct = kelly_jump(0.084, 0.06, 0.55), kelly_jump(0.128, 0.10, 0.70)
assert (0.128 - 0.10 * 0.70) > (0.084 - 0.06 * 0.55) and f_oct < 0.6 * f_jan
```


### Listing 28.4: Block 4: LVaR, days-to-liquidate and runway {#code-28-4}

```python
# --- Block 4: LVaR, days-to-liquidate, FRTB scaling, runway ---------------------
STRESS_MULTIPLIERS = {"eur_ig_mar2026": 1.64, "ig_costs_mar2020": 3.0,
                      "ig_index_2007_08": 3.40 / 0.59, "ig_blocks_mar2020": 6.0}
FRTB_LH = np.array([10, 20, 40, 60, 120])                 # MAR33.12 liquidity horizons, days


def parametric_var(value, sigma_1d, z=2.33):
    """Bangia eq. (3): P [1 - exp(-z sigma)]."""
    return value * (1.0 - np.exp(-z * sigma_1d))


def bangia_col(value, spread_mean, spread_sd, a):
    """Bangia eq. (4): 0.5 P (S_bar + a sigma_S). Spreads are relative (fraction of mid)."""
    return 0.5 * value * (spread_mean + a * spread_sd)


def credit_col(mv, lcs_mean, adv, mult=1.0, eta=0.0):
    """Eq. (28.16): exogenous stress multiple times an endogenous size term. Longs AND shorts pay."""
    mv = np.abs(np.asarray(mv, dtype=float))
    adv = np.maximum(np.asarray(adv, dtype=float), 1.0)          # guard: no zero-ADV division
    return 0.5 * mult * np.asarray(lcs_mean) * mv * (1.0 + eta * np.sqrt(mv / adv))


def days_to_liquidate(position, adv, participation):
    """Eq. (28.17)."""
    if participation <= 0.0:
        raise ValueError("participation must be positive")
    return np.abs(position) / (participation * np.maximum(adv, 1.0))


def frtb_liquidity_es(es_by_bucket, horizons=FRTB_LH, base=10):
    """Eq. (28.18). es_by_bucket[j] = 10-day ES shocking factors with LH >= horizons[j]."""
    es = np.asarray(es_by_bucket, dtype=float)
    widths = np.diff(horizons)
    return float(np.sqrt(es[0] ** 2 + np.sum((es[1:] * np.sqrt(widths / base)) ** 2)))


def runway_weeks(cash, liquid_sleeve, weekly_burn, haircut=0.0):
    """Theo's 13-week model, pointed at the fund: (cash + haircut liquid sleeve) / burn."""
    if weekly_burn <= 0.0:
        return np.inf
    return (cash + (1.0 - haircut) * liquid_sleeve) / weekly_burn


# Paleologo's example: two days of volume at 4% participation takes 50 days
assert abs(days_to_liquidate(2.0, 1.0, 0.04) - 50.0) < 1e-12
# FRTB: all risk in HY corporate spread (LH 60) recovers sqrt(60 / 10)
assert abs(frtb_liquidity_es([1, 1, 1, 1, 0]) - np.sqrt(6.0)) < 1e-12
assert abs(frtb_liquidity_es([1, 0, 0, 0, 0]) - 1.0) < 1e-12
# Bangia's a-sigma form cannot reach the 2008 multiple with a calm-window sigma
implied_a = (3.40 - 0.59) / 0.15                              # sigma_S = 0.15 points (illustrative)
assert implied_a > 4.5 * 3
# The 5x problem on a $2bn gross IG book at 0.6% LCS
col_calm = credit_col([2e9], [0.006], [1e12])[0]
col_2008 = credit_col([2e9], [0.006], [1e12], mult=STRESS_MULTIPLIERS["ig_index_2007_08"])[0]
assert abs(col_calm - 6e6) < 1.0 and abs(col_2008 / col_calm - 3.40 / 0.59) < 1e-12
# Endogenous size term: cost per dollar rises with size
small = credit_col([5e6], [0.01], [5e6], eta=0.5)[0] / 5e6
large = credit_col([25e6], [0.01], [5e6], eta=0.5)[0] / 25e6
assert large > small
# Third Avenue, December 2015: about 2.7 weeks of runway, far inside 13
ta_runway = runway_weeks(cash=200e6, liquid_sleeve=0.0, weekly_burn=317e6 / (30 / 7))
assert 2.5 < ta_runway < 3.0 and ta_runway < 13.0
```


### Listing 28.5: Block 5: Stops, hitting probabilities and the mark-to-bid shock {#code-28-5}

```python
# --- Block 5: drawdown rules ----------------------------------------------------
def prob_hit(x, mu, sigma, horizon):
    """Eq. (28.19): P(min X_t <= -x by T) for X_t = mu t + sigma W_t."""
    s = sigma * np.sqrt(horizon)
    return (stats.norm.cdf((-x - mu * horizon) / s)
            + np.exp(-2.0 * mu * x / sigma ** 2) * stats.norm.cdf((-x + mu * horizon) / s))


def stop_for_lifetime_prob(prob, sharpe, sigma):
    """Eq. (28.20): x = sigma ln(1/P) / (2 SR)."""
    return sigma * np.log(1.0 / prob) / (2.0 * sharpe)


def mark_to_bid_shock(gross_leverage, lcs_mean, mult, already_at_bid=True):
    """Eq. (28.21): NAV drawdown from bid-ask widening alone, as a fraction of NAV."""
    widen = (mult - 1.0) if already_at_bid else mult
    return 0.5 * widen * lcs_mean * gross_leverage


def mc_prob_hit(x, mu, sigma, horizon, n_paths, n_steps, rng):
    """Brownian-bridge Monte Carlo of (28.19): exact for continuous monitoring."""
    dt = horizon / n_steps
    incr = mu * dt + sigma * np.sqrt(dt) * rng.standard_normal((n_paths, n_steps))
    path = np.concatenate([np.zeros((n_paths, 1)), np.cumsum(incr, axis=1)], axis=1)
    d = path + x                                           # distance above the barrier
    below = (d <= 0.0).any(axis=1)
    d0, d1 = np.maximum(d[:, :-1], 0.0), np.maximum(d[:, 1:], 0.0)
    survive = np.prod(1.0 - np.exp(-2.0 * d0 * d1 / (sigma ** 2 * dt)), axis=1)
    survive[below] = 0.0
    return 1.0 - survive.mean()


def simulate_two_threshold(sharpe, sigma, x, shocks):
    """Paleologo's rule: halve capital at loss x/2, liquidate at loss x (on initial capital).
    shocks: (n_paths, n_days) unit-variance Student-t(6) draws, reused across Sharpes."""
    n_paths, n_days = shocks.shape
    mu_d, sd_d = sharpe * sigma / n_days, sigma / np.sqrt(n_days)
    r = mu_d + sd_d * shocks
    cap, pnl = np.ones(n_paths), np.zeros(n_paths)
    for t in range(n_days):
        pnl += cap * r[:, t]
        cap = np.where(pnl <= -x, 0.0, np.where(pnl <= -x / 2.0, np.minimum(cap, 0.5), cap))
    free = r.sum(axis=1)
    price_of_safety = 1.0 - pnl.mean() / free.mean()       # share of expected P&L given up
    return {"mean_pnl": pnl.mean(), "p_out": float(np.mean(cap == 0.0)),
            "price_of_safety": price_of_safety}


# The reported 7.5% stop is what (28.20) gives a Sharpe-1, 6%-vol PM at ~8% lifetime odds
assert abs(stop_for_lifetime_prob(np.exp(-2.5), 1.0, 0.06) - 0.075) < 1e-12
p1 = prob_hit(0.075, 0.06, 0.06, 1.0)
assert 0.040 < p1 < 0.050
p1_mc = mc_prob_hit(0.075, 0.06, 0.06, 1.0, 10_000, 252, RNG)
assert abs(p1_mc - p1) < 0.01, (p1_mc, p1)

# Paleologo's ranking: the price of safety falls with the Sharpe ratio (t6 shocks, common draws)
t6 = stats.t.rvs(df=6, size=(20_000, TRADING_DAYS), random_state=RNG) / np.sqrt(6.0 / 4.0)
pos = [simulate_two_threshold(sr, 0.06, 0.075, t6)["price_of_safety"] for sr in (0.5, 1.0, 2.0)]
assert pos[0] > pos[1] > pos[2] >= 0.0, pos

# Theo's desk: G = 5, LCS 0.6%, the 2007-08 multiple -> through the 5% line on marks alone
shock = mark_to_bid_shock(5.0, 0.006, 3.40 / 0.59)
assert 0.05 < shock < 0.075
assert abs(mark_to_bid_shock(5.0, 0.006, 5.8) - 0.072) < 1e-12
```


### Listing 28.6: Block 6: The leverage band {#code-28-6}

```python
# --- Block 6: the leverage band -------------------------------------------------
def leverage_floor(n_eff, sigma, r_min, sharpe):
    """Eq. (28.2)."""
    return np.sqrt(n_eff) / sigma * r_min / sharpe


def leverage_ceiling(n_eff, sigma, dd_max, sharpe, kappa_z, col_fn=None):
    """Eq. (28.22): fixed point G = A (DD_max - COL(G)); COL(G) is a fraction of NAV, increasing."""
    if kappa_z <= sharpe:
        raise ValueError("kappa * z_p must exceed the Sharpe ratio")
    a = np.sqrt(n_eff) / (sigma * (kappa_z - sharpe))
    if col_fn is None:
        return a * dd_max
    h = lambda g: g - a * (dd_max - col_fn(g))
    hi = a * dd_max
    return hi if h(hi) <= 0.0 else optimize.brentq(h, 0.0, hi, xtol=1e-12)


def liquidity_speed_limit(dd_max, lcs_mean, mult):
    """Eq. (28.23), right-hand side: 2 DD / ((m - 1) LCS)."""
    return 2.0 * dd_max / ((mult - 1.0) * lcs_mean)


m08 = 5.8
c1 = 0.5 * (m08 - 1.0) * 0.008
lo = leverage_floor(40, 0.05, 0.05, 2.0)
hi_dry = leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0)
hi_wet = leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0, col_fn=lambda g: c1 * g)
a_band = np.sqrt(40) / (0.05 * 2.0)
assert abs(lo - 3.162) < 1e-3 and abs(hi_dry - 4.743) < 1e-3
assert abs(hi_wet - a_band * 0.075 / (1 + a_band * c1)) < 1e-9     # closed form (28.23)
assert hi_wet < lo < hi_dry                                        # liquidity closes the band
assert leverage_ceiling(10**8, 0.05, 0.075, 2.0, 4.0, lambda g: c1 * g) < liquidity_speed_limit(0.075, 0.008, m08)
assert abs(liquidity_speed_limit(0.075, 0.008, m08) - 0.075 / c1) < 1e-12
c1_half = 0.5 * (m08 - 1.0) * 0.004                                # halve LCS, accept a 4% hurdle
assert leverage_floor(40, 0.05, 0.04, 2.0) < leverage_ceiling(40, 0.05, 0.075, 2.0, 4.0, lambda g: c1_half * g)
```


### Listing 28.7: Block 7: The team production function {#code-28-7}

```python
# --- Block 7: the team production function --------------------------------------
def combined_ic(ics, corr):
    """Eq. (28.24): sqrt(ic' C^{-1} ic)."""
    ics = np.asarray(ics, dtype=float)
    return float(np.sqrt(ics @ np.linalg.solve(np.asarray(corr, dtype=float), ics)))


def optimal_coverage(n_c, e0=0.01, n_grid=None):
    """Eq. (28.25) by brute force: argmax of e(N) sqrt(N) with e(N) = e0 n_c / (N + n_c)."""
    n = np.arange(1, 20 * n_c + 1) if n_grid is None else n_grid
    ir = 2.0 * e0 * n_c / (n + n_c) * np.sqrt(TRADING_DAYS * n)
    return int(n[np.argmax(ir)])


for rho, target in ((0.6, 0.0559), (0.0, 0.0707), (-0.2, 0.0791)):
    two = np.sqrt((0.05 ** 2 * 2 - 2 * rho * 0.05 ** 2) / (1 - rho ** 2))
    assert abs(combined_ic([0.05, 0.05], [[1, rho], [rho, 1]]) - two) < 1e-12
    assert abs(two - target) < 1e-4
assert optimal_coverage(35) == 35
```


### Listing 28.8: The PM dashboard engine: pm_playbook_engine {#code-28-8}

```python
# --- Final block: pm_playbook_engine --------------------------------------------
def make_demo_book(rng, n_issuers=60, bonds_per=5, nav=4e8):
    iss = np.repeat(np.arange(n_issuers), bonds_per)
    n = iss.size
    tier = np.where(iss < 48, 1, 2)
    side = np.where(rng.random(n_issuers) < 0.8, 1.0, -1.0)[iss]        # same sign within issuer
    spread = np.where(tier == 1, rng.uniform(0.008, 0.045, n), rng.uniform(0.06, 0.14, n))
    return pd.DataFrame({
        "bond_id": [f"B{i:04d}" for i in range(n)], "issuer_id": iss, "sector": iss % 11,
        "tier": tier, "mv_usd": side * rng.uniform(4e6, 10e6, n),
        "spr_dur": rng.uniform(2.0, 6.0, n), "spread": spread, "sigma_rel": rng.uniform(0.25, 0.45, n),
        "lcs": np.where(tier == 1, 0.006, 0.025), "adv_usd": rng.uniform(2e6, 2e7, n),
        "lam_p": np.where(tier == 1, 0.5, 0.8) * spread / 0.6,              # P-hazard below Q (illustrative)
        "lgd_mean": np.where(tier == 1, 0.6, 0.7), "lgd_max": np.where(tier == 1, 0.8, 1.0),
    })


def pm_playbook_engine(book, desk):
    gross = float(book.mv_usd.abs().sum())
    g = gross / desk["nav_usd"]
    sig = (book.spr_dur * book.spread * book.sigma_rel).to_numpy()
    cov = issuer_block_cov(book.issuer_id.to_numpy(), sig, desk["rho_within"], desk["rho_across"])
    w = book.mv_usd.to_numpy() / gross
    n_eff = effective_breadth(w, cov)
    by_iss = book.groupby("issuer_id").mv_usd.sum()
    sigma_book = float(np.sqrt(w @ cov @ w) * np.sqrt(n_eff))           # per-bet vol consistent with N_eff
    lcs_bar = float(np.average(book.lcs, weights=book.mv_usd.abs()))
    c1 = 0.5 * (desk["mult"] - 1.0) * lcs_bar
    floor = leverage_floor(n_eff, sigma_book, desk["r_min"], desk["sharpe"])
    ceil = leverage_ceiling(n_eff, sigma_book, desk["dd_max"], desk["sharpe"], desk["kappa_z"],
                            col_fn=lambda x: c1 * x)
    iss = book.groupby("issuer_id").agg(carry=("spread", "mean"), lam=("lam_p", "mean"),
                                        lgd=("lgd_mean", "mean"), lgd_max=("lgd_max", "max"))
    theta = kelly_multiplier(desk["edge_rel_se"])
    kelly = np.array([theta * kelly_jump(r.carry, r.lam, r.lgd) for r in iss.itertuples()])
    kelly_cap = np.minimum(kelly, (1.0 - 1e-9) / iss.lgd_max.to_numpy())
    actual = by_iss.reindex(iss.index).abs().to_numpy() / desk["nav_usd"]
    dtl = days_to_liquidate(book.mv_usd.to_numpy(), book.adv_usd.to_numpy(), desk["participation"])
    col = credit_col(book.mv_usd, book.lcs, book.adv_usd, mult=desk["mult"], eta=desk["eta"]).sum()
    used = desk["realized_dd"] + mark_to_bid_shock(g, lcs_bar, desk["mult"])
    return pd.Series({
        "gross_leverage": g, "lev_floor": floor, "lev_ceiling": ceil,
        "lev_speed_limit": liquidity_speed_limit(desk["dd_max"], lcs_bar, desk["mult"]),
        "band_empty": floor > ceil, "lev_breach": g > ceil,
        "n_eff": n_eff, "issuer_herfindahl_n": herfindahl_breadth(by_iss.to_numpy()),
        "names_over_kelly_cap": int(np.sum(actual > kelly_cap)),
        "stressed_col_pct_nav": col / desk["nav_usd"],
        "pct_gross_over_20d": float(book.mv_usd.abs()[dtl > 20].sum() / gross),
        "dd_budget_used_pct_of_cut": used / desk["stop_half"],
        "runway_weeks": runway_weeks(desk["cash_usd"], desk["liquid_sleeve_usd"],
                                     desk["weekly_burn_usd"], haircut=0.1),
        "hit_rate_se_1y": hit_rate_se(0.51, n_eff),
    })


DESK = {"nav_usd": 4e8, "dd_max": 0.075, "kappa_z": 4.0, "sharpe": 0.7, "r_min": 0.05, "mult": 5.8,
        "eta": 0.5, "stop_half": 0.05, "realized_dd": 0.01, "cash_usd": 6e7, "liquid_sleeve_usd": 1.5e8,
        "weekly_burn_usd": 8e6, "participation": 0.10, "rho_within": 0.9, "rho_across": 0.01,
        "edge_rel_se": 1.0}
dash = pm_playbook_engine(make_demo_book(np.random.default_rng(28)), DESK)

assert 1.0 < dash.n_eff < dash.issuer_herfindahl_n <= 60.0 + 1e-9    # correlation shrinks breadth
assert dash.lev_ceiling < dash.lev_speed_limit
assert dash.lev_breach == (dash.gross_leverage > dash.lev_ceiling)
assert 0.0 <= dash.pct_gross_over_20d <= 1.0 and dash.stressed_col_pct_nav > 0.0
assert dash.runway_weeks > 13.0                                      # the desk survives the quarter
assert dash.dd_budget_used_pct_of_cut > DESK["realized_dd"] / DESK["stop_half"]   # marks count
print(dash.to_string())
```


## F.B: Appendix B: The Data & API Atlas {#code-b}

Listings from `91_appB_data_and_api_atlas.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing B.1: The tidy bond panel: security master, 30/360 bond math and a synthetic TRACE tape {#code-b-1}

```python
# Tidy bond panel from a synthetic TRACE-like tape. Bond ids are synthetic labels, NOT CUSIPs.
import numpy as np
import pandas as pd
from scipy.optimize import brentq

RNG = np.random.default_rng(20261017)
IG_CAP, HY_CAP = 5_000_000, 1_000_000          # dissemination caps (par $)
RATING_SCALE = {r: k + 1 for k, r in enumerate(
    "AAA AA+ AA AA- A+ A A- BBB+ BBB BBB- BB+ BB BB- B+ B B- CCC+ CCC CCC- CC C D".split())}
IG_MAX_NUM = RATING_SCALE["BBB-"]

# ---------------------------------------------------------------- 1. security master
secmaster = pd.DataFrame({
    "bond_id":        ["SYN-IG-A", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D"],
    "issuer_id":      ["ISS1", "ISS2", "ISS3", "ISS4"],
    "coupon":         [0.0450, 0.0525, 0.07875, 0.0950],
    "maturity":       pd.to_datetime(["2033-06-15", "2031-03-01", "2030-09-15", "2029-12-01"]),
    "offering_date":  pd.to_datetime(["2023-06-15", "2021-03-01", "2022-09-15", "2021-12-01"]),
    "offering_amt":   [1_500_000_000, 750_000_000, 600_000_000, 400_000_000],
    "security_level": ["SEN", "SEN", "SEN", "SUB"],
    "rule_144a":      [False, False, True, False],
    "freq":           [2, 2, 2, 2],
    "day_count":      ["30/360"] * 4,
})

# ------------------------------------------------- 2. point-in-time ratings history
# join on knowledge_ts (publication), never effective_ts
ratings = pd.DataFrame({
    "bond_id":      ["SYN-IG-A", "SYN-IG-B", "SYN-IG-B", "SYN-HY-C", "SYN-HY-D", "SYN-HY-D"],
    "effective_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-10", "2022-09-01",
                                    "2021-11-20", "2026-08-14"]),
    "knowledge_ts": pd.to_datetime(["2023-06-01", "2021-02-20", "2026-06-12", "2022-09-01",
                                    "2021-11-20", "2026-08-17"]),
    "rating":       ["A-", "BBB-", "BB+", "B", "CCC", "D"],
})
ratings["rating_num"] = ratings["rating"].map(RATING_SCALE).astype("int64")
DEFAULT_DATE = {"SYN-HY-D": pd.Timestamp("2026-08-14")}

# ------------------------------------------------------------- 3. bond math (30/360)
def d30360(d1, d2):
    """US 30/360 (bond basis) day count between two Timestamps."""
    D1 = min(d1.day, 30)
    D2 = d2.day
    if D2 == 31 and D1 >= 30:
        D2 = 30
    return 360 * (d2.year - d1.year) + 30 * (d2.month - d1.month) + (D2 - D1)

def coupon_dates(maturity, freq=2, start=None):
    months = 12 // freq
    out, d, k = [], maturity, 0
    while start is None or d > start - pd.DateOffset(months=months):
        out.append(d)
        k += 1
        d = maturity - pd.DateOffset(months=months * k)
        if start is None and k > 400:
            break
    return sorted(out)

def schedule(settle, maturity, freq=2):
    """(previous coupon date, list of future coupon dates) relative to settle."""
    dates = coupon_dates(maturity, freq, start=settle)
    future = [d for d in dates if d > settle]
    past = [d for d in dates if d <= settle]
    prev = past[-1] if past else future[0] - pd.DateOffset(months=12 // freq)
    return prev, future

def accrued(settle, maturity, coupon, freq=2):
    prev, _ = schedule(settle, maturity, freq)
    return 100.0 * coupon / freq * d30360(prev, settle) / (360.0 / freq)

def dirty_from_yield(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)          # fraction of period to next coupon
    k = np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    return float(np.sum(cf / (1.0 + y / freq) ** (w + k)))

def clean_from_yield(y, settle, maturity, coupon, freq=2):
    return dirty_from_yield(y, settle, maturity, coupon, freq) - accrued(settle, maturity, coupon, freq)

def yield_from_clean(p_clean, settle, maturity, coupon, freq=2):
    f = lambda y: clean_from_yield(y, settle, maturity, coupon, freq) - p_clean
    return brentq(f, -0.05, 5.0, xtol=1e-12)              # bracket: -5% to 500%

def mod_duration(y, settle, maturity, coupon, freq=2):
    prev, fut = schedule(settle, maturity, freq)
    w = d30360(settle, fut[0]) / (360.0 / freq)
    n = w + np.arange(len(fut))
    cf = np.full(len(fut), 100.0 * coupon / freq)
    cf[-1] += 100.0
    pv = cf / (1.0 + y / freq) ** n
    macaulay_years = np.sum((n / freq) * pv) / np.sum(pv)
    return float(macaulay_years / (1.0 + y / freq))

def tsy_curve(T, b0=0.042, b1=-0.005, b2=0.010, tau=2.0):
    """Synthetic Nelson-Siegel par curve (illustrative), bond-equivalent decimal."""
    T = np.maximum(np.asarray(T, dtype=float), 1e-6)
    x = T / tau
    return b0 + b1 * (1 - np.exp(-x)) / x + b2 * ((1 - np.exp(-x)) / x - np.exp(-x))

# ----------------------------------------------- 4. simulate "true" paths and a tape
bdays = pd.bdate_range("2026-03-02", "2026-09-30")
y0 = {"SYN-IG-A": 0.0480, "SYN-IG-B": 0.0590, "SYN-HY-C": 0.0760, "SYN-HY-D": 0.1350}
vol = {"SYN-IG-A": 0.0006, "SYN-IG-B": 0.0010, "SYN-HY-C": 0.0020, "SYN-HY-D": 0.0060}
lam = {"SYN-IG-A": 6.0, "SYN-IG-B": 4.0, "SYN-HY-C": 2.0, "SYN-HY-D": 1.5}
half_spread = {"SYN-IG-A": 0.10, "SYN-IG-B": 0.20, "SYN-HY-C": 0.40, "SYN-HY-D": 1.00}

rows, seq = [], 0
for _, b in secmaster.iterrows():
    y = y0[b.bond_id]
    for d in bdays:
        y += vol[b.bond_id] * RNG.standard_normal()
        if b.bond_id == "SYN-IG-B" and d >= pd.Timestamp("2026-06-10"):
            y += 0.0004                                   # fallen-angel drift
        settle = d + pd.offsets.BDay(1)                   # US corporates settle T+1
        defaulted = b.bond_id in DEFAULT_DATE and d >= DEFAULT_DATE[b.bond_id]
        if defaulted:
            true_px = 31.0 + 2.0 * RNG.standard_normal()  # trades flat near recovery
        else:
            true_px = clean_from_yield(max(y, 0.0), settle, b.maturity, b.coupon)
        for _ in range(RNG.poisson(lam[b.bond_id] * (2.0 if defaulted else 1.0))):
            side = RNG.choice(["B", "S", "D"], p=[0.4, 0.4, 0.2])   # cust buy/sell, dealer
            sgn = {"B": 1.0, "S": -1.0, "D": 0.0}[side]
            px = round(true_px + sgn * half_spread[b.bond_id] + 0.05 * RNG.standard_normal(), 3)
            median_qty = 1_000_000 if b.bond_id.startswith("SYN-IG") else 500_000
            qty = float(np.clip(np.round(RNG.lognormal(np.log(median_qty), 1.0), -3), 1_000, 25_000_000))
            exec_ts = d + pd.Timedelta(hours=9, minutes=30) + pd.Timedelta(seconds=int(RNG.integers(0, 6.5 * 3600)))
            seq += 1
            rows.append(dict(msg_seq=seq, orig_msg_seq=np.nan, trc_st="T", bond_id=b.bond_id,
                             exec_ts=exec_ts, report_ts=exec_ts + pd.Timedelta(seconds=int(RNG.integers(1, 900))),
                             price=px, qty_true=qty, side=side))
msgs = pd.DataFrame(rows)

# inject tape pathologies: cancels, corrections, a decimal shift, a bounce-back print
t_idx = msgs.index[msgs.trc_st == "T"]
cancel_targets = RNG.choice(t_idx, size=6, replace=False)
fix_targets = RNG.choice(np.setdiff1d(t_idx, cancel_targets), size=6, replace=False)
extra = []
for i in cancel_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="X")
    extra.append(r)
for i in fix_targets:
    r = msgs.loc[i].to_dict(); seq += 1
    r.update(msg_seq=seq, orig_msg_seq=msgs.at[i, "msg_seq"], trc_st="C", price=round(r["price"] + 0.25, 3))
    extra.append(r)
msgs = pd.concat([msgs, pd.DataFrame(extra)], ignore_index=True)
ig_a = msgs.index[(msgs.bond_id == "SYN-IG-A") & (msgs.trc_st == "T")]
msgs.loc[ig_a[100], "price"] *= 10.0                      # decimal-shift typo
msgs.loc[ig_a[200], "price"] += 7.0                       # bounce-back spike
msgs["orig_msg_seq"] = msgs["orig_msg_seq"].astype("Int64")

# ------------------------------- 5. point-in-time rating join (no look-ahead allowed)
def pit_rating(df, ts_col):
    left = df.sort_values(ts_col)
    right = ratings.sort_values("knowledge_ts")[["bond_id", "knowledge_ts", "rating", "rating_num"]]
    out = pd.merge_asof(left, right, left_on=ts_col, right_on="knowledge_ts", by="bond_id",
                        direction="backward", allow_exact_matches=True)
    assert (out["knowledge_ts"] <= out[ts_col]).all(), "look-ahead in rating join"
    return out

# --------------------------------------------- 6. clean the tape (Dick-Nielsen-lite)
def clean_tape(m):
    m = m.copy()
    cancelled = set(m.loc[m.trc_st == "X", "orig_msg_seq"].dropna().astype(int))
    corrected = set(m.loc[m.trc_st == "C", "orig_msg_seq"].dropna().astype(int))
    keep = (m.trc_st.isin(["T", "C"])) & ~m.msg_seq.isin(cancelled | corrected)
    t = m.loc[keep].copy()
    t = t.sort_values(["bond_id", "exec_ts"]).reset_index(drop=True)
    # decimal-shift and bounce-back screens against a rolling median of neighbours
    med = t.groupby("bond_id")["price"].transform(lambda s: s.rolling(11, center=True, min_periods=3).median())
    ratio = t["price"] / med
    t["flag_decimal"] = (ratio > 5) | (ratio < 0.2)
    prev_ = t.groupby("bond_id")["price"].shift(1)
    next_ = t.groupby("bond_id")["price"].shift(-1)
    jump_out = (t["price"] - prev_).abs()
    jump_back = (next_ - t["price"]).abs()
    t["flag_bounce"] = (jump_out > 3.0) & (jump_back > 3.0) & ((next_ - prev_).abs() < 1.0) & ~t["flag_decimal"]
    t = t.loc[~(t.flag_decimal | t.flag_bounce)].copy()
    # point-in-time rating -> dissemination cap the public tape would have shown
    t = pit_rating(t, "exec_ts")
    t["cap"] = np.where(t["rating_num"] <= IG_MAX_NUM, IG_CAP, HY_CAP)
    t["qty_dissem"] = np.minimum(t["qty_true"], t["cap"])
    t["qty_capped"] = t["qty_true"] > t["cap"]
    t["date"] = t["exec_ts"].dt.normalize()
    return t

trades = clean_tape(msgs)

# ------------------------------------------------ 7. bond-day panel on a full grid
def vwap(g, qty_col):
    return float(np.sum(g["price"] * g[qty_col]) / np.sum(g[qty_col]))

agg = (trades.groupby(["bond_id", "date"])
       .apply(lambda g: pd.Series({
           "px_vwap_true": vwap(g, "qty_true"),
           "px_vwap_dissem": vwap(g, "qty_dissem"),
           "px_last": g.sort_values("exec_ts")["price"].iloc[-1],
           "n_trades": len(g),
           "par_volume": g["qty_true"].sum(),
           "n_capped": int(g["qty_capped"].sum()),
           "cust_buy_par": g.loc[g.side == "B", "qty_true"].sum(),
           "cust_sell_par": g.loc[g.side == "S", "qty_true"].sum(),
       }), include_groups=False)
       .reset_index())

grid = pd.MultiIndex.from_product([secmaster.bond_id, bdays], names=["bond_id", "date"]).to_frame(index=False)
daily = grid.merge(agg, on=["bond_id", "date"], how="left").merge(secmaster, on="bond_id", how="left")
daily = daily.loc[daily["date"] < daily["maturity"]].copy()      # never drop defaulted bonds
daily = daily.sort_values(["bond_id", "date"]).reset_index(drop=True)
daily["traded"] = daily["n_trades"].fillna(0).astype("int64") > 0
daily["n_trades"] = daily["n_trades"].fillna(0).astype("int64")
daily["par_volume"] = daily["par_volume"].fillna(0.0)
daily["last_trade_date"] = daily["date"].where(daily["traded"])
daily["last_trade_date"] = daily.groupby("bond_id")["last_trade_date"].ffill()
daily["px_clean"] = daily.groupby("bond_id")["px_vwap_true"].ffill()          # carried price
daily["days_stale"] = [np.busday_count(l.date(), d.date()) if pd.notna(l) else np.nan
                       for l, d in zip(daily["last_trade_date"], daily["date"])]
daily["days_stale"] = daily["days_stale"].astype("float64")
daily["is_stale"] = daily["days_stale"] > 0
daily["status"] = np.where([b in DEFAULT_DATE and d >= DEFAULT_DATE[b] for b, d in zip(daily.bond_id, daily.date)],
                           "defaulted", "performing")
daily["trades_flat"] = daily["status"].eq("defaulted")
daily = pit_rating(daily, "date").sort_values(["bond_id", "date"]).reset_index(drop=True)

def analytics(r):
    if pd.isna(r.px_clean):
        return pd.Series({"accrued": np.nan, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    settle = r.date + pd.offsets.BDay(1)
    ai = 0.0 if r.trades_flat else accrued(settle, r.maturity, r.coupon)
    if r.trades_flat:                                   # yields are meaningless once flat
        return pd.Series({"accrued": ai, "ytm": np.nan, "dur_mod": np.nan, "tsy_yld": np.nan,
                          "spread": np.nan, "dts": np.nan})
    y = yield_from_clean(r.px_clean, settle, r.maturity, r.coupon)
    dmod = mod_duration(y, settle, r.maturity, r.coupon)
    T = (r.maturity - settle).days / 365.25
    ty = float(tsy_curve(T))
    s = y - ty
    return pd.Series({"accrued": ai, "ytm": y, "dur_mod": dmod, "tsy_yld": ty, "spread": s,
                      "dts": dmod * s * 1e4})          # DTS in years x bp
daily = pd.concat([daily, daily.apply(analytics, axis=1)], axis=1)

# ------------------------------------------- 8. monthly returns (stale-aware rule)
def monthly_returns(dp, max_stale_days=5):
    d = dp.copy()
    d["month_end"] = d["date"] + pd.offsets.BMonthEnd(0)
    me = d.loc[d["date"] == d["month_end"]].copy()
    ok = me["days_stale"] <= max_stale_days
    me["px_eom"] = np.where(ok, me["px_clean"], np.nan)
    me = me.sort_values(["bond_id", "month_end"])
    me["px_prev"] = me.groupby("bond_id")["px_eom"].shift(1)
    me["ai_prev"] = me.groupby("bond_id")["accrued"].shift(1)
    # coupon paid in (prev, this]: detected by an accrued-interest reset (approximation)
    me["cpn_paid"] = np.where((me["accrued"] < me["ai_prev"]) & ~me["trades_flat"],
                              100.0 * me["coupon"] / me["freq"], 0.0)
    me["ret_total"] = (me["px_eom"] + me["accrued"] + me["cpn_paid"]) / (me["px_prev"] + me["ai_prev"]) - 1.0
    return me[["bond_id", "month_end", "px_eom", "accrued", "cpn_paid", "ret_total",
               "days_stale", "rating", "status", "spread", "dur_mod", "dts"]].reset_index(drop=True)

monthly = monthly_returns(daily)

# --------------------------------------------------------- 9. schema + sanity checks
DAILY_SCHEMA = {"bond_id": "str", "date": "datetime", "px_clean": "float",
                "px_vwap_dissem": "float", "n_trades": "int", "par_volume": "float",
                "days_stale": "float", "is_stale": "bool", "rating": "str",
                "rating_num": "int", "status": "str", "accrued": "float",
                "ytm": "float", "dur_mod": "float", "spread": "float", "dts": "float"}
KIND_CHECK = {"str": pd.api.types.is_string_dtype, "datetime": pd.api.types.is_datetime64_any_dtype,
              "float": pd.api.types.is_float_dtype, "int": pd.api.types.is_integer_dtype,
              "bool": pd.api.types.is_bool_dtype}
for col, kind in DAILY_SCHEMA.items():
    assert col in daily.columns, f"missing column {col}"
    assert KIND_CHECK[kind](daily[col]), f"{col}: dtype {daily[col].dtype} is not {kind}"
assert not daily.duplicated(["bond_id", "date"]).any(), "panel key not unique"
assert (daily["date"] < daily["maturity"]).all()
assert "SYN-HY-D" in set(monthly.loc[monthly.status == "defaulted", "bond_id"]), "survivorship: defaulted bond dropped"
# no cancelled or corrected originals survive
dead = set(msgs.loc[msgs.trc_st.isin(["X", "C"]), "orig_msg_seq"].dropna().astype(int))
assert not trades["msg_seq"].isin(dead).any()
assert not trades["price"].gt(200).any(), "decimal-shift print survived"
# price-yield round trip and duration vs finite difference
s0, m0, c0 = pd.Timestamp("2026-04-15"), pd.Timestamp("2031-03-01"), 0.0525
y_rt = yield_from_clean(97.25, s0, m0, c0)
assert abs(clean_from_yield(y_rt, s0, m0, c0) - 97.25) < 1e-8
h = 1e-6
fd = -(dirty_from_yield(y_rt + h, s0, m0, c0) - dirty_from_yield(y_rt - h, s0, m0, c0)) / (2 * h) / dirty_from_yield(y_rt, s0, m0, c0)
assert abs(fd - mod_duration(y_rt, s0, m0, c0)) < 1e-6
# par bond on a coupon date prices at par
assert abs(clean_from_yield(0.0525, pd.Timestamp("2026-03-01"), m0, c0) - 100.0) < 1e-9
# fallen angel: the cap switches from $5mm to $1mm once the downgrade is KNOWN
fa = trades.loc[trades.bond_id == "SYN-IG-B"]
assert (fa.loc[fa.exec_ts < "2026-06-12", "cap"] == IG_CAP).all()
assert (fa.loc[fa.exec_ts >= "2026-06-13", "cap"] == HY_CAP).all()
# stale-price theorem check: EWMA smoothing shrinks variance by (1-theta)/(1+theta)
theta, n = 0.6, 400_000
r = RNG.standard_normal(n)
ro = np.empty(n); ro[0] = (1 - theta) * r[0]
for i in range(1, n):
    ro[i] = theta * ro[i - 1] + (1 - theta) * r[i]
var_ratio = ro[1000:].var() / r[1000:].var()
rho1 = np.corrcoef(ro[1001:], ro[1000:-1])[0, 1]
assert abs(var_ratio - (1 - theta) / (1 + theta)) < 0.01 and abs(rho1 - theta) < 0.01

print(f"messages={len(msgs)}, clean trades={len(trades)}, capped prints={int(trades.qty_capped.sum())}")
print(f"daily panel rows={len(daily)}, stale share={daily.is_stale.mean():.1%}")
print(f"var ratio={var_ratio:.4f} (theory {(1-theta)/(1+theta):.4f}), rho1={rho1:.4f}")
print(monthly.head(8).to_string(index=False, float_format=lambda v: f"{v:.4f}"))
```


## F.D: Appendix D: Plumbing: Settlement, Clearing, Margin, Financing and the ISDA Credit-Event Machine {#code-d}

Listings from `93_appD_market_plumbing_and_contract_mechanics.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing D.1: plumbing.py: settlement, financing, margin, CDS cash and credit-event mechanics, one function per rule {#code-d-1}

```python
# plumbing.py -- Appendix D reference implementation. Illustrative numbers; seeded.
from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np

# ------------------------------------------------------------ D.1 settlement
def accrued_30_360(coupon: float, days: int) -> float:
    """Accrued interest as a fraction of face (coupon an annual decimal, days on 30/360)."""
    if days < 0:
        raise ValueError("accrued days must be non-negative")
    return coupon * days / 360.0


def bond_settlement_cash(face: float, clean_pts: float, coupon: float, accrued_days: int) -> float:
    """Dirty invoice in dollars: clean price plus accrued to the SETTLEMENT date."""
    if face <= 0 or clean_pts <= 0:
        raise ValueError("face and clean price must be positive")
    return face * (clean_pts / 100.0 + accrued_30_360(coupon, accrued_days))


def gap_cost(cash: float, funding_rate: float, gap_days: int) -> float:
    """Cost of financing cash across a settlement gap, ACT/360."""
    if gap_days < 0:
        raise ValueError("gap_days must be non-negative")
    return cash * funding_rate * gap_days / 360.0


# ------------------------------------------------------------ D.2 clearing
def netting_ratio(n: int, rho: float) -> float:
    """Portfolio IM over the sum of standalone IMs: n equal long positions, correlation rho."""
    if n < 1 or not (-1.0 / max(n - 1, 1) <= rho <= 1.0):
        raise ValueError("need n >= 1 and a feasible equicorrelation")
    return math.sqrt((1.0 + (n - 1) * rho) / n)


# ------------------------------------------------------------ D.3 financing
def repo_open(market_value: float, haircut: float) -> tuple[float, float]:
    """Return (loan, equity) for a repo at the given haircut."""
    if not 0.0 <= haircut < 1.0:
        raise ValueError("haircut must lie in [0, 1)")
    loan = (1.0 - haircut) * market_value
    return loan, market_value - loan


def repo_margin_call(loan: float, collateral_value: float, new_haircut: float) -> float:
    """Cash the dealer demands after re-marking collateral and resetting the haircut."""
    if not 0.0 <= new_haircut < 1.0:
        raise ValueError("haircut must lie in [0, 1)")
    return max(0.0, loan - (1.0 - new_haircut) * collateral_value)


def forced_sale_fraction(h_old: float, h_new: float, price_drop: float) -> float:
    """Fraction of the position to sell when the haircut moves h_old -> h_new and price falls."""
    if not (0.0 < h_old < 1.0 and 0.0 < h_new < 1.0 and 0.0 <= price_drop < 1.0):
        raise ValueError("haircuts in (0, 1), price drop in [0, 1)")
    if price_drop >= h_old:
        return 1.0
    return max(0.0, 1.0 - (h_old - price_drop) / (h_new * (1.0 - price_drop)))


# ------------------------------------------------------------ D.4 CDS calendar
def cds_puf(par_spread: float, coupon: float, rpv01: float) -> float:
    """First-order points upfront as a fraction of notional (positive: buyer pays)."""
    return (par_spread - coupon) * rpv01


def cds_day_one_cash(notional: float, par_spread: float, coupon: float, rpv01: float,
                     accrued_days: int, factor: float = 1.0) -> float:
    """Cash from protection BUYER to SELLER at T+3; negative means the seller pays."""
    if accrued_days < 0 or not 0.0 < factor <= 1.0:
        raise ValueError("bad accrued days or index factor")
    return notional * factor * (cds_puf(par_spread, coupon, rpv01) - coupon * accrued_days / 360.0)


def cds_vm_to_buyer(notional: float, puf_old: float, puf_new: float, factor: float = 1.0) -> float:
    """Variation margin to the protection buyer when the upfront value moves."""
    return notional * factor * (puf_new - puf_old)


# ------------------------------------------------------------ D.5-D.6 events
BACKSTOP_DAYS = {"credit": 60, "succession": 90}


def backstop_date(question_date: date, kind: str) -> date:
    """Earliest event date a DC question can still catch (calendar days)."""
    return question_date - timedelta(days=BACKSTOP_DAYS[kind])


def ctd_payout(final_list_prices: list[float]) -> float:
    """Par minus the cheapest deliverable, per unit notional; empty list = stylized orphan."""
    if not final_list_prices:
        return 0.0
    cheapest = min(final_list_prices)
    if not 0.0 <= cheapest <= 100.0:
        raise ValueError("prices must be in points between 0 and 100")
    return 1.0 - cheapest / 100.0


# ------------------------------------------------------------ D.7 succession
def successor_split(weights: dict[str, float], original: str = "ORIGINAL",
                    original_survives: bool = True) -> dict[str, float]:
    """Simplified 2014 successor rules. weights: share of Relevant Obligations assumed."""
    total = sum(weights.values())
    if any(w < 0.0 for w in weights.values()) or total > 1.0 + 1e-12:
        raise ValueError("shares must be non-negative and sum to at most 1")
    retained = 1.0 - total
    sole = [e for e, w in weights.items() if w >= 0.75]
    if sole:
        return {sole[0]: 1.0}
    over = sorted(e for e, w in weights.items() if w > 0.25)
    if over:
        names = over if retained <= 0.25 else over + [original]
        return {e: 1.0 / len(names) for e in names}
    if original_survives or not weights:
        return {original: 1.0}
    largest = max(weights, key=weights.get)
    return {largest: 1.0}


# ------------------------------------------------------------ D.8 liquidity buffer
def liquidity_buffer(flows: list[tuple[int, int, float]]) -> float:
    """Worst cumulative shortfall of signed flows (day, intraday_order, cash; + is cash in)."""
    cum, worst = 0.0, 0.0
    for _, _, cash in sorted(flows, key=lambda f: (f[0], f[1])):
        cum += cash
        worst = min(worst, cum)
    return -worst


# ------------------------------------------------------------ the worked example
FACE = 10_000_000.0
cash_bond = bond_settlement_cash(FACE, 88.0, 0.06, 75)
loan, equity = repo_open(cash_bond, 0.15)
cds_cash0 = cds_day_one_cash(FACE, 0.0370, 0.05, 4.20, 30)
im0 = 0.06 * FACE
assert abs(cash_bond - 8_925_000.0) < 1e-6
assert abs(loan - 7_586_250.0) < 1e-6 and abs(equity - 1_338_750.0) < 1e-6
assert abs(cds_cash0 + 587_666.6667) < 1e-3          # the seller pays the buyer

collateral5 = bond_settlement_cash(FACE, 62.0, 0.06, 80)
call5 = repo_margin_call(loan, collateral5, 0.35)
vm6 = cds_vm_to_buyer(FACE, cds_puf(0.0370, 0.05, 4.20), cds_puf(0.15, 0.05, 3.20))
im_add5 = (0.15 - 0.06) * FACE
assert abs(call5 - 3_469_583.3333) < 1e-3
assert abs(vm6 - 3_746_000.0) < 1e-3
assert abs((-call5 + vm6 - im_add5) + 623_583.3333) < 1e-3    # net cash absorbed by the shock
assert abs((-FACE * 0.26 + vm6) - 1_146_000.0) < 1e-3         # ...on a day the P&L is positive

flows = [(1, 0, loan), (1, 1, -cash_bond), (1, 2, -im0), (3, 0, -cds_cash0),
         (5, 0, -call5), (5, 1, -im_add5), (6, 0, vm6)]
assert abs(liquidity_buffer(flows[:3]) - 1_938_750.0) < 1e-3  # what ROBO reported
assert abs(liquidity_buffer(flows) - 5_720_666.6667) < 1e-3   # what the trade needed

# D.1, D.2, D.3, D.5-D.7 checks against the text
assert abs(gap_cost(100_000_000.0, 0.05, 27) - 375_000.0) < 1e-6
assert abs(netting_ratio(100, 0.3) - 0.5541) < 1e-4
assert abs(forced_sale_fraction(0.10, 0.25, 0.0) - 0.60) < 1e-12
assert abs(forced_sale_fraction(0.10, 0.25, 0.05) - 0.789474) < 1e-6
assert forced_sale_fraction(0.10, 0.25, 0.12) == 1.0
assert backstop_date(date(2026, 11, 23), "credit") == date(2026, 9, 24)
assert backstop_date(date(2026, 11, 23), "succession") == date(2026, 8, 25)
assert abs(ctd_payout([62.0, 50.0]) * FACE - 5_000_000.0) < 1e-6
assert ctd_payout([]) == 0.0
assert successor_split({"A": 0.8}) == {"A": 1.0}
assert successor_split({"A": 0.6, "B": 0.3}) == {"A": 0.5, "B": 0.5}
assert successor_split({"A": 0.3}) == {"A": 0.5, "ORIGINAL": 0.5}
assert successor_split({"A": 0.25}) == {"ORIGINAL": 1.0}               # 25.0% does nothing
assert successor_split({"A": 0.251}) == {"A": 0.5, "ORIGINAL": 0.5}    # 25.1% halves the swap


# ------------------------------------------------------------ seeded stress of the shock day
def simulate_shock_buffer(seed: int = 20261018, n_paths: int = 20_000,
                          buffer: float = 2_000_000.0) -> dict[str, float]:
    """Distribution of the Day-5 intraday cash need (repo call + IM add-on, VM not yet in)."""
    rng = np.random.default_rng(seed)
    drop_pts = 40.0 * rng.beta(2.0, 5.0, n_paths)              # bond price drop, points
    p_stress = 0.25 + 0.5 * drop_pts / 40.0                    # bigger drops, likelier stress
    stress = rng.random(n_paths) < p_stress
    new_haircut = np.where(stress, 0.35, 0.15)
    new_im_rate = np.where(stress, 0.15, 0.08)
    collateral = FACE * ((88.0 - drop_pts) / 100.0 + accrued_30_360(0.06, 80))
    call = np.maximum(0.0, loan - (1.0 - new_haircut) * collateral)
    im_add = np.maximum(0.0, new_im_rate - 0.06) * FACE
    vm = FACE * 1.44 * drop_pts / 100.0                        # CDS points per bond point, from D.8
    intraday = call + im_add
    return {
        "p_exceeds_buffer": float(np.mean(intraday > buffer)),
        "median_intraday": float(np.median(intraday)),
        "q99_intraday": float(np.quantile(intraday, 0.99)),
        "mean_net_after_vm": float(np.mean(intraday - vm)),
    }


stats = simulate_shock_buffer()
assert 0.0 <= stats["p_exceeds_buffer"] <= 1.0
assert stats["q99_intraday"] >= stats["median_intraday"] >= 0.0
```


## F.E: Appendix E: The Laws of the Desk {#code-e}

Listings from `94_appE_laws_of_the_desk.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing E.1: laws_of_the_desk.py: the Laws of the Desk as data, a Debrief linter and one checker per law {#code-e-1}

```python
"""laws_of_the_desk.py: the Laws of the Desk as data, a Debrief linter, and one checker per law.

numpy plus the standard library only. Seed 94.
Units: prices in points per 100 par unless a name ends in _frac; spreads, rates
and hazards are decimals per year; time is in years; DTS is decimal-years.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass, replace
from pathlib import Path
from statistics import NormalDist

import numpy as np

RNG = np.random.default_rng(94)
EULER_GAMMA = 0.5772156649015329  # gamma_E in Law 12; gamma stays risk aversion


# ---------------------------------------------------------------- the registry
@dataclass(frozen=True)
class Law:
    number: int
    name: str
    family: str
    statement: str
    equation: str
    earned_in: tuple
    bites_in: tuple
    patterns: tuple


LAWS = (
    Law(1, "IDO or it didn't happen", "Ruler",
        "Strip carry, Treasuries and DTS-scaled credit beta before you call anything alpha.",
        r"\epsilon_{i,t} = r^{ex}_{i,t} - s_i\Delta t - \sum_k \beta_{i,k}F_{k,t}",
        ("8.1", "8.8", "3.3.3"), ("10.6.3", "11.7.2", "18.7", "19.8", "22.8.1"),
        (r"\bIDO\b", r"\bstrip\b.*\b(beta|carry)\b", r"beta wearing", r"\bnot alpha\b")),
    Law(2, "Bonds are not bets; issuers are", "Ruler",
        "Effective breadth counts issuers, not CUSIPs.",
        r"BR_{eff} = N/(1+(m-1)\rho)",
        ("4.3", "7.6", "28.2"), ("7.7", "9.7", "11.6", "28.8"),
        (r"\bissuers?\b", r"\bhats?\b", r"\bbreadth\b", r"\bCUSIPs?\b")),
    Law(3, "DTS is the unit of credit beta", "Ruler",
        "Spread volatility scales with spread; size, hedge and vol-target in DTS.",
        r"\beta_i = DTS_i/DTS_m",
        ("8.4", "9.2"), ("1.4", "7.4", "9.5", "10.3", "12.5", "19.4", "28.7"),
        (r"\bDTS\b", r"risk scales with spread")),
    Law(4, "Say which measure you are in", "Ruler",
        "Prices live in Q, forecasts in P; the gap is the premium.",
        r"s - \lambda^P L \approx (\lambda^Q - \lambda^P) L",
        ("6.3", "6.8"), ("1.5", "3.1", "4.4", "12.2", "13.8", "14.1", "15.4", "18.6", "28.4"),
        (r"\\mathbb\{[PQ]\}", r"\bmeasures?\b", r"agency default rate", r"risk premium")),
    Law(5, "A bid is a posterior, and winning is information", "Table",
        "Condition on who is selling and on having won.",
        r"b = E^P[V | sell] = m - \pi\sigma_V",
        ("3.2", "1.3", "18.3"), ("1.9", "2.3.2", "3.3", "18.7", "18.9", "19.8"),
        (r"posterior", r"winner'?s curse", r"winning is information", r"adverse selection",
         r"hit ratios?", r"who is on the call", r"anchored dealers")),
    Law(6, "Charge the jump once", "Table",
        "Price the jump-to-default in one place only.",
        r"-(\lambda^P - \lambda^Q) J \tau;\ \lambda^P J^2 \tau",
        ("5.1", "5.3", "18.6"), ("10.9", "11.1", "16.4", "23.4", "24.3.1", "28.4"),
        (r"\bjumps?\b", r"funeral", r"\bJTD\b", r"short put")),
    Law(7, "Default is a menu, and recovery is a U", "Table",
        "Two default rates, two recovery humps; 40% is a convention.",
        r"\lambda = \lambda_H + \lambda_D;\ f_R = w f_{in} + (1-w) f_{out}",
        ("5.5", "5.6", "14.1", "14.4"), ("6.8", "12.2", "13.3", "16.5", "24.2"),
        (r"\brecover(y|ies)\b", r"distressed exchange", r"default rate", r"\b40%", r"parole",
         r"\bauction\b")),
    Law(8, "Every clause is a payoff function", "Table",
        "Read the document as a program before you model it as a distribution.",
        r"\Delta_j(V) = W^{post}_j(V) - W^{pre}_j(V)",
        ("13.2", "13.3", "15.1", "21.4", "25.3"), ("6.5", "13.6", "16.3", "16.5", "24.8", "27.3"),
        (r"\bclauses?\b", r"payoff", r"credit agreement", r"indenture", r"\bdocuments?\b",
         r"\bbaskets?\b", r"covenant", r"option book", r"one word")),
    Law(9, "A mark is a moving average of the truth", "Tape",
        "Stale marks shrink betas, fake lead-lag and flatter Sharpe ratios.",
        r"\sigma_o = \sigma\sqrt{\sum_k\theta_k^2};\ \beta^o_0 = \theta_0\beta",
        ("8.5", "17.2", "12.5"), ("7.1", "10.5", "19.5", "20.2", "21.7", "28.6"),
        (r"\bmarks?\b", r"\bstale", r"desmooth|unsmooth", r"dimson|sum the lags", r"smooth")),
    Law(10, "Costs decide, and capacity is a square", "Tape",
        "Turnover beyond alpha/2c is charity; liquidity tiers bind first.",
        r"T_{max} = \alpha/(2\bar c);\ \alpha(A^*) = g/3",
        ("2.9", "4.7", "4.8", "11.9", "28.3"), ("9.4", "9.8", "10.8", "12.7", "24.7", "28.5"),
        (r"\bcosts?\b", r"capacity", r"turnover", r"liquidity tiers?", r"\brake\b", r"break-even")),
    Law(11, "Label every number", "Tape",
        "Gross or net, simulated or live, P or Q, denominator, knowledge time, source.",
        r"x = (v, u, M, g, l, num/den, t^{known}, src)",
        ("4.5", "27.2", "27.3"), ("2.6", "7.9", "14.1", "25.3", "26.4"),
        (r"label every", r"gross or net", r"denominator", r"known_at|knowledge[_ ]t",
         r"\bunits?\b", r"price_kind", r"timestamps?", r"\bclocks?\b")),
    Law(12, "Count your trials", "Tape",
        "Deflate every Sharpe ratio by the number of things you tried.",
        r"E[\max_k \widehat{SR}_k] \approx \sqrt{V} z_K",
        ("7.8", "7.9", "26.7"), ("4.5", "7.12", "9.9"),
        (r"\btrials?\b", r"deflat", r"\bDSR\b|\bPBO\b", r"replicat", r"\bzoo\b", r"folded hands")),
    Law(13, "The label is the model", "Clock",
        "Label the trade you would make; cumulative incidence, not 1 - KM.",
        r"F_k(t) \le 1 - \widehat{KM}_k(t)",
        ("7.4", "11.4", "11.5", "14.2"), ("7.5", "14.3", "15.5"),
        (r"label is the model", r"label the trade", r"triple barrier", r"cumulative incidence",
         r"kaplan", r"exclusion rate", r"competing risks?")),
    Law(14, "Censoring is the signal", "Clock",
        "Truncated samples: model the truncation before the data.",
        r"L = \prod f(Q_i) \prod [1 - F(\bar q)]",
        ("2.2", "18.8", "22.2"), ("3.2", "5.7", "7.9", "14.2", "17.3"),
        (r"censor", r"5MM\+|1MM\+", r"truncat", r"survivor", r"pareto")),
    Law(15, "Forced selling is a supply schedule", "Clock",
        "Forced sellers sell on rules you can read in advance.",
        r"dQ = -\theta Q dt;\ p = v - \kappa Q/M",
        ("16.2", "21.4", "1.8"), ("11.6", "20.3", "20.5", "21.7", "24.6"),
        (r"forced sell", r"supply", r"overhang", r"\bcure\b", r"\bFSPI\b", r"redemption")),
    Law(16, "The court is a random variable with timestamps", "Clock",
        "Rulings are regime switches; the plan value is negotiated.",
        r"logit \theta_w(t) = \alpha_w + \sum_r J_{r,w} 1\{t \ge t_r\}",
        ("14.6", "13.9", "16.1"), ("3.7", "13.8", "25.6", "27.3"),
        (r"\bcourts?\b", r"rulings?", r"\bdocket", r"plan value", r"negotiat", r"serta|mitel",
         r"regime switch")),
)

LAW_BY_NUMBER = {law.number: law for law in LAWS}
COMPILED = {law.number: [re.compile(p, re.IGNORECASE) for p in law.patterns] for law in LAWS}
PROBATION = {
    "silence is data": re.compile(r"\bsilen(ce|t)\b", re.IGNORECASE),
    "hedge less than naive": re.compile(r"hedge less", re.IGNORECASE),
    "regimes size the tilt": re.compile(r"regimes? size", re.IGNORECASE),
}

assert len(LAWS) == 16 and sorted(LAW_BY_NUMBER) == list(range(1, 17))


# ---------------------------------------------------------------- the linter
DEBRIEF_HEAD = re.compile(r"^##\s+\S+\s+Desk Debrief\b")
STOP = re.compile(r"^(##\s|###\s|\*\*The Spec|\*\*Exercises)")
BULLET = re.compile(r"^(?:[-*]|\d+\.)\s+(.*)")
TAG_BLOCK = re.compile(r"\[L\d+(?:\s*,\s*L?\d+)*\]")


def chapter_id(path):
    """'01_ch01_x.md' -> '1'; '04_ch04b_x.md' -> '4-B'; '91_appB_x.md' -> 'B'."""
    name = Path(path).name
    m = re.match(r"\d+_ch(\d+)(b?)_", name)
    if m:
        return f"{int(m.group(1))}{'-B' if m.group(2) else ''}"
    m = re.match(r"\d+_app([A-Z])_", name)
    if m:
        return m.group(1)
    return Path(path).stem


def iter_debrief_bullets(path):
    """Yield (line_no, text) for every bullet inside a Desk Debrief section."""
    inside = False
    with Path(path).open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            if DEBRIEF_HEAD.match(line):
                inside = True
                continue
            if inside and STOP.match(line):
                inside = False
                continue
            if inside:
                m = BULLET.match(line)
                if m:
                    yield line_no, m.group(1).strip()


def explicit_tags(text):
    found = set()
    for block in TAG_BLOCK.findall(text):
        found.update(int(x) for x in re.findall(r"\d+", block))
    return sorted(found)


def suggest_tags(text):
    return [n for n, pats in COMPILED.items() if any(p.search(text) for p in pats)]


def lint_book(book_dir):
    """Read every Desk Debrief in book_dir (never writes). One row per bullet."""
    rows = []
    for path in sorted(Path(book_dir).glob("*.md")):
        if path.name.startswith("94_appE"):
            continue
        for line_no, text in iter_debrief_bullets(path):
            tags = explicit_tags(text)
            unknown = [n for n in tags if n not in LAW_BY_NUMBER]
            if unknown:
                raise ValueError(f"{path.name}:{line_no}: unknown law tag(s) {unknown}")
            rows.append({
                "file": path.name,
                "chapter": chapter_id(path),
                "line": line_no,
                "explicit": tags,
                "suggested": suggest_tags(text),
                "probation": [k for k, p in PROBATION.items() if p.search(text)],
                "untagged": not tags,
                "text": text[:120],
            })
    return rows


def coverage(rows, explicit_only=False):
    """Law number -> set of chapter ids whose Debriefs carry it."""
    cov = {law.number: set() for law in LAWS}
    for row in rows:
        tags = row["explicit"] if explicit_only else (row["explicit"] or row["suggested"])
        for n in tags:
            cov[n].add(row["chapter"])
    return cov


def admission_failures(cov, min_debriefs=3):
    return [n for n, chapters in cov.items() if len(chapters) < min_debriefs]


def format_tags(numbers):
    return "[" + ", ".join(f"L{n}" for n in sorted(set(numbers))) + "]"


# ---------------------------------------------------------------- Law 11 as a type
_MEASURES = ("P", "Q", "none")
_COSTS = ("gross", "net", "n/a")
_PROVENANCE_RANK = {"live": 0, "model": 1, "simulated": 2}
_MUST_MATCH = ("unit", "measure", "costs", "denominator")


@dataclass(frozen=True)
class LabeledNumber:
    value: float
    unit: str
    measure: str = "none"
    costs: str = "n/a"
    provenance: str = "live"
    denominator: str = "n/a"
    known_at: str = ""
    source: str = "illustrative"

    def __post_init__(self):
        if not math.isfinite(float(self.value)):
            raise ValueError(f"Law 11: non-finite value {self.value!r}")
        if not self.unit:
            raise ValueError("Law 11: a number needs a unit")
        if self.measure not in _MEASURES:
            raise ValueError(f"Law 11: measure must be one of {_MEASURES}")
        if self.costs not in _COSTS:
            raise ValueError(f"Law 11: costs must be one of {_COSTS}")
        if self.provenance not in _PROVENANCE_RANK:
            raise ValueError(f"Law 11: provenance must be one of {tuple(_PROVENANCE_RANK)}")
        if not self.source:
            raise ValueError("Law 11: cite a source or write 'illustrative'")

    def _check(self, other):
        if not isinstance(other, LabeledNumber):
            raise TypeError("Law 11: cannot combine a labeled number with a bare one")
        diffs = [k for k in _MUST_MATCH if getattr(self, k) != getattr(other, k)]
        if diffs:
            detail = ", ".join(f"{k} ({getattr(self, k)!r} vs {getattr(other, k)!r})" for k in diffs)
            raise ValueError("Law 11: label mismatch on " + detail)

    def _combine(self, other, value):
        prov = max(self.provenance, other.provenance, key=_PROVENANCE_RANK.get)
        src = self.source if self.source == other.source else f"{self.source}; {other.source}"
        return replace(self, value=value, provenance=prov,
                       known_at=max(self.known_at, other.known_at), source=src)

    def __add__(self, other):
        self._check(other)
        return self._combine(other, self.value + other.value)

    def __sub__(self, other):
        self._check(other)
        return self._combine(other, self.value - other.value)

    def scaled(self, k, unit=None):
        return replace(self, value=self.value * float(k), unit=unit or self.unit)


# ---------------------------------------------------------------- one checker per law
def ido_residual(r_total, r_tsy, spread, dt, dts, loadings, factor_rel):
    """Law 1. Arrays (T,N) except loadings (N,K) and factor_rel (T,K). Returns epsilon (T,N)."""
    r_total, r_tsy, spread, dts = (np.asarray(a, dtype=float) for a in (r_total, r_tsy, spread, dts))
    loadings, factor_rel = np.asarray(loadings, dtype=float), np.asarray(factor_rel, dtype=float)
    shape = r_total.shape
    if r_tsy.shape != shape or spread.shape != shape or dts.shape != shape:
        raise ValueError("Law 1: r_total, r_tsy, spread and dts must share shape (T, N)")
    if loadings.shape[0] != shape[1] or factor_rel.shape != (shape[0], loadings.shape[1]):
        raise ValueError("Law 1: loadings must be (N, K) and factor_rel (T, K)")
    systematic = -dts * (factor_rel @ loadings.T)
    return (r_total - r_tsy) - spread * dt - systematic


def effective_breadth(n_bonds, n_issuers, rho_within, rho_across=0.0):
    """Law 2, equations (4.1) and (28.5)."""
    if n_issuers <= 0 or n_bonds < n_issuers:
        raise ValueError("Law 2: need at least one bond per issuer")
    if not (0.0 <= rho_across <= rho_within <= 1.0):
        raise ValueError("Law 2: need 0 <= rho_across <= rho_within <= 1")
    m = n_bonds / n_issuers
    return n_bonds / (1.0 + (m - 1.0) * rho_within + (n_bonds - m) * rho_across)


def dts_beta(dts_i, dts_m):
    """Law 3."""
    if dts_m <= 0:
        raise ValueError("Law 3: market DTS must be positive")
    return dts_i / dts_m


def credit_premium(spread, lgd_q, lambda_p, lgd_p=None):
    """Law 4. Credit triangle in Q, expected loss in P, premium = s - lambda_P * L_P."""
    if not (0.0 < lgd_q <= 1.0):
        raise ValueError("Law 4: lgd_q must be in (0, 1]")
    lgd_p = lgd_q if lgd_p is None else lgd_p
    lambda_q = spread / lgd_q
    return {"lambda_q": lambda_q, "premium": spread - lambda_p * lgd_p,
            "q_over_p": lambda_q / lambda_p if lambda_p > 0 else math.inf}


def gm_bid(mid, sigma_v, pi):
    """Law 5, equation (3.1)."""
    if not (0.0 <= pi <= 1.0) or sigma_v < 0:
        raise ValueError("Law 5: need 0 <= pi <= 1 and sigma_v >= 0")
    return mid - pi * sigma_v


def effective_dealers(n, phi):
    """Law 5, the anchored-dealer count of section 2.3.2."""
    if n < 1 or not (0.0 < phi <= 1.0):
        raise ValueError("Law 5: need n >= 1 and 0 < phi <= 1")
    return n / (1.0 + (n - 1.0) * phi)


def jump_terms(lambda_p, lambda_q, jump, horizon):
    """Law 6. Returns (credit-view drift term, jump standard deviation), in the units of jump."""
    credit_view = -(lambda_p - lambda_q) * jump * horizon
    jump_sd = math.sqrt(max(lambda_p, 0.0) * jump ** 2 * horizon)
    return credit_view, jump_sd


def mixture_variance(q, var_x, var_y, jump):
    """Law 6, section 5.1: within-world terms plus q(1-q)J^2."""
    if not (0.0 <= q <= 1.0):
        raise ValueError("Law 6: q must be a probability")
    return (1.0 - q) * var_x + q * var_y + q * (1.0 - q) * jump ** 2


def jtd_hedge_ratio(price_frac, r_bond, r_auction=None):
    """Laws 6-8. CDS notional per unit of bond face: (P - R_bond) / (1 - R_auction)."""
    r_auction = r_bond if r_auction is None else r_auction
    if not (0.0 <= r_auction < 1.0):
        raise ValueError("Law 7: auction recovery must be in [0, 1)")
    return (price_frac - r_bond) / (1.0 - r_auction)


def recovery_mixture(w_in, mu_in, mu_out, sd_in=0.0, sd_out=0.0):
    """Law 7, section 14.4. Returns (mean, total sd, sd from membership alone)."""
    if not (0.0 <= w_in <= 1.0):
        raise ValueError("Law 7: w_in must be a probability")
    mean = w_in * mu_in + (1.0 - w_in) * mu_out
    between = w_in * (1.0 - w_in) * (mu_in - mu_out) ** 2
    within = w_in * sd_in ** 2 + (1.0 - w_in) * sd_out ** 2
    return mean, math.sqrt(within + between), math.sqrt(between)


def ar1_theta(phi, k_max=240):
    """Law 9. Smoothing weights (1 - phi) phi^k, renormalised after truncation."""
    if not (0.0 <= phi < 1.0):
        raise ValueError("Law 9: need 0 <= phi < 1")
    theta = (1.0 - phi) * phi ** np.arange(k_max + 1)
    return theta / theta.sum()


def smoothing_stats(theta):
    """Law 9. Volatility ratio, contemporaneous-beta ratio and Sharpe inflation."""
    theta = np.asarray(theta, dtype=float)
    if np.any(theta < 0) or abs(theta.sum() - 1.0) > 1e-9:
        raise ValueError("Law 9: weights must be non-negative and sum to one")
    s2 = float(np.sum(theta ** 2))
    return {"vol_ratio": math.sqrt(s2), "beta0_ratio": float(theta[0]),
            "sharpe_inflation": 1.0 / math.sqrt(s2)}


def breakeven_turnover(alpha_gross, cbar):
    """Law 10, equation (4.6)."""
    if cbar <= 0:
        raise ValueError("Law 10: cost must be positive")
    return alpha_gross / (2.0 * cbar)


def capacity_star(liquidity, g, turnover, eta):
    """Law 10, equation (4.2). Returns (A*, the AUM at which net alpha is zero)."""
    if min(liquidity, g, turnover, eta) <= 0:
        raise ValueError("Law 10: inputs must be positive")
    a_star = liquidity * g ** 2 / (18.0 * turnover ** 3 * eta ** 2)
    return a_star, 2.25 * a_star


def net_alpha(aum, liquidity, g, turnover, eta):
    """Law 10, section 4.8: g minus square-root impact."""
    return g - 2.0 * turnover * eta * math.sqrt(2.0 * turnover * aum / liquidity)


def expected_max_sharpe(k_trials, var_sr):
    """Law 12, section 7.8 (Bailey and Lopez de Prado)."""
    if k_trials < 2:
        raise ValueError("Law 12: with one trial there is nothing to deflate; need K >= 2")
    if var_sr < 0:
        raise ValueError("Law 12: variance must be non-negative")
    nd = NormalDist()
    z = ((1.0 - EULER_GAMMA) * nd.inv_cdf(1.0 - 1.0 / k_trials)
         + EULER_GAMMA * nd.inv_cdf(1.0 - 1.0 / (k_trials * math.e)))
    return math.sqrt(var_sr) * z


def cif_constant_hazards(h_k, h_other, t):
    """Law 13. Cumulative incidence vs the naive 1 - KM that censors the other cause."""
    total = h_k + h_other
    cif = 0.0 if total == 0 else h_k / total * (1.0 - math.exp(-total * t))
    naive = 1.0 - math.exp(-h_k * t)
    return cif, naive


def pareto_mean_excess(alpha, cap):
    """Law 14. Mean size of a print disseminated as 'cap+' under a Pareto tail."""
    if alpha <= 1.0:
        raise ValueError("Law 14: the mean above the cap exists only for alpha > 1")
    return alpha / (alpha - 1.0) * cap


def half_life(theta):
    """Law 15."""
    if theta <= 0:
        raise ValueError("Law 15: execution rate must be positive")
    return math.log(2.0) / theta


def overhang_peak(theta, alpha):
    """Law 15, section 16.2.2: time of peak overhang after the event."""
    if theta <= 0 or alpha <= 0:
        raise ValueError("Law 15: rates must be positive")
    if math.isclose(theta, alpha, rel_tol=1e-12):
        return 1.0 / theta
    return math.log(theta / alpha) / (theta - alpha)


def ruling_probability(alpha_w, jumps, t):
    """Law 16, section 14.6.1. jumps: iterable of (t_r, J_rw) in years and log-odds."""
    x = alpha_w + sum(j for t_r, j in jumps if t >= t_r)
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    ex = math.exp(x)
    return ex / (1.0 + ex)


# ---------------------------------------------------------------- the section E.6 audit
def audit_halvorsen():
    """Reproduce the illustrative numbers of section E.6."""
    mid, face_mm, d_spr, z = 88.0, 15.0, 3.9, 0.048
    dts_bond, dts_index = d_spr * z, 3.2 * 0.031
    beta = dts_beta(dts_bond, dts_index)
    prem = credit_premium(spread=0.037, lgd_q=0.60, lambda_p=0.030)
    shade = mid - gm_bid(mid, sigma_v=4.0, pi=0.10)
    credit_view, jump_sd = jump_terms(0.030, prem["lambda_q"], jump=48.0, horizon=5 / 252)
    r_mean, _, _ = recovery_mixture(0.30, 0.65, 0.20)
    hedge_bankruptcy = jtd_hedge_ratio(mid / 100, r_mean)
    hedge_no_accel = (mid - 70.0) / 100 / (1.0 - 0.52)
    reversal_month = 0.070 * (1.0 - math.exp(-3.42 / 12))
    bid = mid - shade - 0.25 - 0.10
    quote = LabeledNumber(mid, "points", measure="Q", provenance="model",
                          known_at="2026-10-16T14:55", source="composite (illustrative)")
    return {
        "L3 beta": beta,
        "L3 index-equivalent MV ($mm)": beta * face_mm * mid / 100,
        "L4 lambda_Q": prem["lambda_q"],
        "L4 premium (decimal/yr)": prem["premium"],
        "L5 shade (points)": shade,
        "L6 credit view (points)": credit_view,
        "L6 jump sd (points)": jump_sd,
        "L7 E[R]": r_mean,
        "L7 JTD hedge, bankruptcy": hedge_bankruptcy,
        "L8 JTD hedge, no acceleration": hedge_no_accel,
        "L10 reversal in a month": reversal_month,
        "L14 mean HY block ($mm)": pareto_mean_excess(4 / 3, 1.0),
        "L15 half-life (months)": 12 * half_life(3.42),
        "bid (points)": bid,
        "label": f"{quote.value:.2f} {quote.unit}, measure {quote.measure}, known {quote.known_at}",
    }


# ---------------------------------------------------------------- demos
def demo_law12(k_trials=100, months=120):
    """Best of K null strategies vs the expected maximum (expect about 0.8 for K=100, 10 years)."""
    rets = RNG.normal(0.0, 0.02, size=(k_trials, months))
    sr = rets.mean(axis=1) / rets.std(axis=1, ddof=1) * math.sqrt(12)
    return float(sr.max()), expected_max_sharpe(k_trials, var_sr=12.0 / months)


def demo_law9(phi=0.8, months=600, beta=1.0, lags=12):
    """AR(1) smoothing: vol ratio about 1/3; contemporaneous beta about (1 - phi) beta; lag sum near beta."""
    f = RNG.normal(0.0, 0.03, size=months)
    r = beta * f + RNG.normal(0.0, 0.01, size=months)
    obs = np.empty(months)
    obs[0] = r[0]
    for t in range(1, months):
        obs[t] = (1.0 - phi) * r[t] + phi * obs[t - 1]
    x = np.column_stack([f[lags - k: months - k] for k in range(lags + 1)])
    y = obs[lags:]
    coef, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(y)), x]), y, rcond=None)
    return {
        "vol_ratio_sim": float(obs[lags:].std() / r[lags:].std()),
        "vol_ratio_theory": smoothing_stats(ar1_theta(phi))["vol_ratio"],
        "beta0_sim": float(coef[1]),
        "beta_lag_sum_sim": float(coef[1:].sum()),  # theory: 1 - phi**(lags + 1), about 0.945
    }


if __name__ == "__main__":
    best, theory = demo_law12()
    print(f"Law 12: best of 100 null Sharpes {best:.2f}; expected max {theory:.2f}")
    print("Law 9:", {k: round(v, 3) for k, v in demo_law9().items()})
    print("Law 2: 47 CUSIPs, one issuer, rho 0.9 ->", round(effective_breadth(47, 1, 0.9), 2), "bets")
    for key, value in audit_halvorsen().items():
        print(f"  {key}: {value if isinstance(value, str) else round(value, 4)}")
    book = Path("book_src")
    if book.is_dir():
        rows = lint_book(book)
        cov = coverage(rows)
        print(f"Linter: {len(rows)} Debrief bullets, {sum(r['untagged'] for r in rows)} without explicit tags")
        print("Laws below three Debriefs:", admission_failures(cov) or "none")
```


## F.4-B: Chapter 4-B: Bond Math for the Desk: Price, Yield, Duration, Convexity, Spread Measures and the Callable Bond {#code-4b}

Listings from `04_ch04b_bond_math_for_the_desk.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 4-B.1: bondmath.py: cash flows, curve, solver, price and yield {#code-4b-1}

```python
# bondmath.py (Chapter 4-B): one list of cash flows, one curve, one solver.
# Units: prices per 100 face (dirty unless a name says otherwise); rates, spreads and hazards
# as annual decimals; times in years. Every number in Chapter 4-B is reproduced at the bottom.
import math
from datetime import date

import numpy as np


def year_frac(d1, d2, basis="30/360"):
    """Year fraction from d1 to d2. '30/360' is the US bond basis, 31st rule included."""
    if basis == "30/360":
        a1 = min(d1.day, 30)
        a2 = 30 if (d2.day == 31 and a1 == 30) else d2.day
        return (360 * (d2.year - d1.year) + 30 * (d2.month - d1.month) + (a2 - a1)) / 360.0
    days = (d2 - d1).days
    if basis == "ACT/360":
        return days / 360.0
    if basis == "ACT/365F":
        return days / 365.0
    raise ValueError(f"unknown day count {basis!r}")


def accrued(coupon, last_coupon, settle, basis="30/360"):
    """Accrued interest per 100 face, counted to the settlement date, not the trade date."""
    return 100.0 * coupon * year_frac(last_coupon, settle, basis)


def cashflows(c, n, f=2, w=1.0):
    """Times (years) and flows per 100 face: n coupons left, w of the current period to run."""
    t = (np.arange(n, dtype=float) + w) / f
    cf = np.full(n, 100.0 * c / f)
    cf[-1] += 100.0
    return t, cf


def workout_flows(c, k, redemption, f=2):
    """Flows to a call date or maturity after k coupons, redeemed at `redemption` per 100."""
    t, cf = cashflows(c, k, f)
    cf[-1] += redemption - 100.0
    return t, cf


def price(y, c, n, f=2, w=1.0):
    """Street dirty price at periodic yield y (Sec. 4B.2)."""
    t, cf = cashflows(c, n, f, w)
    return float(np.sum(cf * (1.0 + y / f) ** (-f * t)))


def solve(fn, target, lo, hi, tol=1e-12):
    """Bisection for a monotone fn(x) = target on [lo, hi]; refuses an unbracketed target."""
    f_lo, f_hi = fn(lo) - target, fn(hi) - target
    if f_lo * f_hi > 0:
        raise ValueError("target not bracketed: check units, dirty vs clean, or recovery")
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        f_mid = fn(mid) - target
        if (f_mid > 0) == (f_lo > 0):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def ytm(p_dirty, c, n, f=2, w=1.0):
    """Yield to maturity; unique because price is strictly decreasing in yield."""
    return solve(lambda y: price(y, c, n, f, w), p_dirty, -0.05, 5.0)


def ytw(p_dirty, c, n, schedule, f=2):
    """(yield, coupon number, redemption) to worst over every coupon date of every call window
    and maturity. schedule: [(first callable coupon number, call price), ...] in date order."""
    workouts = [(n, 100.0)]
    for j, (k0, K) in enumerate(schedule):
        k1 = schedule[j + 1][0] if j + 1 < len(schedule) else n
        workouts += [(k, K) for k in range(k0, k1)]

    def y_to(k, K):
        t, cf = workout_flows(c, k, K, f)
        return solve(lambda y: float(np.sum(cf * (1.0 + y / f) ** (-f * t))), p_dirty, -0.05, 5.0)

    return min((y_to(k, K), k, K) for k, K in workouts)


def risk_at_yield(y, c, n, f=2, w=1.0):
    """Price, Macaulay and modified duration, modified convexity, from analytic derivatives."""
    t, cf = cashflows(c, n, f, w)
    v, e = 1.0 + y / f, f * t
    pv = cf * v ** (-e)
    p = float(pv.sum())
    d_mac = float(np.sum(pv * t)) / p
    c_mod = float(np.sum(pv * e * (e + 1.0))) / (p * f * f * v * v)
    return {"price": p, "D_mac": d_mac, "D_mod": d_mac / v, "C_mod": c_mod}


def dv01(d_mod, p_dirty, face):
    """Dollars gained per 1bp fall in yield (positive for a long position)."""
    return d_mod * p_dirty * face * 1e-6


def effective(pricer, h=1e-4):
    """(D_eff, C_eff) of pricer(h), the full price after a parallel shift h; central differences."""
    p0, p_up, p_dn = pricer(0.0), pricer(h), pricer(-h)
    return (p_dn - p_up) / (2.0 * h * p0), (p_up + p_dn - 2.0 * p0) / (h * h * p0)


def flat_curve(r, f=2):
    """Discount function of a flat curve quoted at periodic rate r (par = zero = r)."""
    return lambda t: (1.0 + r / f) ** (-f * np.asarray(t, dtype=float))


def curve_from_par(par, f=2):
    """Bootstrap d(t_n), t_n = n/f, from par yields on that grid; linear in zero rates."""
    par = np.asarray(par, dtype=float)
    d = np.empty(len(par))
    for n, cn in enumerate(par):
        d[n] = (1.0 - cn / f * d[:n].sum()) / (1.0 + cn / f)
    nodes = np.arange(1, len(par) + 1) / f
    z = -np.log(d) / nodes
    return lambda t: np.exp(-np.interp(t, nodes, z) * np.asarray(t, dtype=float))


def z_spread(p_dirty, t, cf, disc):
    """Constant continuous shift over the zero curve that reprices the flows."""
    base = cf * disc(t)
    return solve(lambda z: float(np.sum(base * np.exp(-z * t))), p_dirty, -0.05, 3.0)


def key_rate_durations(t, cf, disc, z, keys):
    """KRDs from tent bumps of the zero curve at `keys`; the tents sum to one everywhere."""
    pv = cf * disc(t) * np.exp(-z * t)
    eye = np.eye(len(keys))
    return np.array([np.sum(t * pv * np.interp(t, keys, eye[j])) for j in range(len(keys))]) / pv.sum()


def asw_par(p_dirty, t, cf, disc, f=2):
    """Par-par asset-swap spread over the swap curve `disc` (full coupon periods)."""
    d = disc(t)
    return (float(np.sum(cf * d)) - p_dirty) / (100.0 * float(np.sum(d)) / f)


def discount_margin(p_dirty, margin, base, life, f=4):
    """Margin over a flat-forward base rate that reprices a floater paying base + margin."""
    k = np.arange(1, int(round(life * f)) + 1, dtype=float)

    def pv(dm):
        v = (1.0 + (base + dm) / f) ** (-k)
        return float(100.0 * (base + margin) / f * v.sum() + 100.0 * v[-1])

    return solve(pv, p_dirty, -0.05, 3.0)


def hazard_price(lam, t, cf, r, R):
    """Q-price per 100: survival-weighted flows plus recovery of face R at default (flat, cc)."""
    k, T = lam + r, float(t[-1])
    rec = 100.0 * R * lam * T if abs(k) < 1e-12 else 100.0 * R * lam / k * (1.0 - math.exp(-k * T))
    return float(np.sum(cf * np.exp(-k * t))) + rec


def pecs(p_dirty, t, cf, r, R=0.40):
    """Par-equivalent CDS spread (ACT/360 premium, paid continuously) and the flat hazard."""
    lo, hi = 1e-10, 10.0
    if not hazard_price(hi, t, cf, r, R) < p_dirty < hazard_price(lo, t, cf, r, R):
        raise ValueError("no hazard reprices this price: is the bond at or below recovery?")
    lam = solve(lambda x: hazard_price(x, t, cf, r, R), p_dirty, lo, hi)
    k, T = lam + r, float(t[-1])
    protection = (1.0 - R) * lam / k * (1.0 - math.exp(-k * T))
    rpv01 = (365.0 / 360.0) * (1.0 - math.exp(-k * T)) / k
    return protection / rpv01, lam


def toy_tree(s, call=101.0):
    """Sec. 4B.7 hand lattice: 3-year 9% annual bond, simple rates, p = 1/2, call ex-coupon."""
    tree = [[0.04], [0.05, 0.03], [0.06, 0.04, 0.02]]
    V = [109.0 / (1.0 + r + s) for r in tree[2]]
    for i in (1, 0):
        V = [min(v, call) for v in V] if call else V
        V = [0.5 * (V[j] + V[j + 1] + 18.0) / (1.0 + tree[i][j] + s) for j in range(i + 1)]
    return V[0]


def ho_lee(disc, T, steps, sigma):
    """Ho-Lee tree fitted to disc(t) with Arrow-Debreu prices, no root-finding (Sec. 4B.7)."""
    dt, Q, rates = T / steps, np.array([1.0]), []
    for i in range(steps):
        x = sigma * math.sqrt(dt) * (2.0 * np.arange(i + 1) - i)
        theta = -math.log(float(disc((i + 1) * dt)) / float(np.sum(Q * np.exp(-x * dt)))) / dt
        rates.append(theta + x)
        g = Q * np.exp(-rates[-1] * dt)
        Q = 0.5 * (np.append(g, 0.0) + np.append(0.0, g))
    return dt, rates


def on_grid(t, cf, dt, steps):
    """Flows by lattice step; refuses any flow that is not on a step date."""
    a = np.zeros(steps + 1)
    for ti, ci in zip(t, cf):
        k = int(round(ti / dt))
        if abs(k * dt - ti) > 1e-9:
            raise ValueError("cash flow off the grid: choose steps so every coupon date is a node")
        a[k] += ci
    return a


def lattice_price(flows, dt, rates, s, calls=None, mw=None):
    """Backward induction at spread s. calls: {step: strike}; the issuer pays the coupon plus
    min(continuation, strike). With mw the strike is max(100, W), W = remaining flows at r + mw."""
    calls = calls or {}
    V = np.full(len(rates) + 1, flows[-1])
    W = V.copy()
    for i in range(len(rates) - 1, -1, -1):
        V = np.exp(-(rates[i] + s) * dt) * 0.5 * (V[:-1] + V[1:])
        if mw is not None:
            W = np.exp(-(rates[i] + mw) * dt) * 0.5 * (W[:-1] + W[1:])
        if i in calls:
            V = np.minimum(V, np.maximum(100.0, W) if mw is not None else calls[i])
        V = V + flows[i]
        if mw is not None:
            W = W + flows[i]
    return float(V[0])


def oas(p_dirty, flows, dt, rates, calls=None, mw=None):
    """The spread at which the lattice, with every option exercised, reprices the dirty price."""
    return solve(lambda s: lattice_price(flows, dt, rates, s, calls, mw), p_dirty, -0.05, 3.0)


def explain(p0, d_mod, c_mod, dy_rates, ds, p1):
    """P&L explain per 100 face: rates, spread, convexity, and the residual nobody likes."""
    rates, spread = -d_mod * dy_rates * p0, -d_mod * ds * p0
    convexity = 0.5 * c_mod * (dy_rates + ds) ** 2 * p0
    return {"rates": rates, "spread": spread, "convexity": convexity,
            "residual": p1 - p0 - rates - spread - convexity}


def fallen_angel_row(y, y_tsy, c=0.045, n=20, f=2, R=0.40, face=10e6):
    """Table 4B.1: every measure of the stylized note from one flat Treasury curve."""
    t, cf = cashflows(c, n, f)
    disc, rk = flat_curve(y_tsy, f), risk_at_yield(y, c, n, f)
    p, g = rk["price"], y - y_tsy
    a = asw_par(p, t, cf, disc, f)
    s_pe, _ = pecs(p, t, cf, f * math.log(1.0 + y_tsy / f), R)
    return {"price": p, "G": 1e4 * g, "Z": 1e4 * z_spread(p, t, cf, disc), "ASW_par": 1e4 * a,
            "ASW_mm": 1e4 * a * 100.0 / p, "PECS": 1e4 * s_pe, "D_mod": rk["D_mod"],
            "C_mod": rk["C_mod"], "DV01": dv01(rk["D_mod"], p, face), "DTS": rk["D_mod"] * 1e4 * g}


# ---- every identity in the chapter, asserted ----
assert abs(accrued(0.045, date(2020, 2, 15), date(2020, 3, 25)) - 0.50) < 1e-12
assert abs(year_frac(date(2020, 1, 30), date(2020, 3, 31)) - 60 / 360) < 1e-12      # the 31st rule
assert abs(price(0.045, 0.045, 20) - 100.0) < 1e-10                                 # par: c = y
assert abs(ytm(price(0.09, 0.045, 20), 0.045, 20) - 0.09) < 1e-10
feb = risk_at_yield(0.035, 0.045, 20)
fd_d, fd_c = effective(lambda h: price(0.035 + h, 0.045, 20))
assert abs(fd_d - feb["D_mod"]) < 1e-5 and abs(fd_c - feb["C_mod"]) < 1e-3
assert abs(feb["D_mod"] - 8.106) < 0.005 and abs(feb["C_mod"] - 78.0) < 0.1
grid = np.arange(1, 21) / 2
assert np.allclose(curve_from_par([0.03] * 20)(grid), flat_curve(0.03)(grid), rtol=0, atol=1e-12)
assert abs(discount_margin(100.0, 0.0375, 0.04, 3.0) - 0.0375) < 1e-10              # floater at par
assert abs(toy_tree(0.05) - 99.67) < 0.01 and abs(toy_tree(0.05, None) - 100.03) < 0.01
y_w, k_w, K_w = ytw(103.0, 0.0925, 10, [(4, 104.625), (6, 102.3125), (8, 100.0)])
assert k_w == 8 and K_w == 100.0 and abs(y_w - 0.0835) < 0.0005                    # the par call

# Table 4B.1 and the 23 March column
dates = {"2020-02-20": (0.035, 0.0152), "2020-03-23": (0.09, 0.0076), "2020-06-30": (0.055, 0.0066)}
table = {d: fallen_angel_row(*yy) for d, yy in dates.items()}
for d, row in table.items():
    print(d, "  ".join(f"{k} {v:,.2f}" for k, v in row.items()))
mar = table["2020-03-23"]
assert abs(mar["G"] - 824) < 0.01 and abs(mar["Z"] - 804.5) < 0.5 and abs(mar["ASW_par"] - 678.5) < 1
assert abs(mar["ASW_mm"] - 959) < 1 and abs(mar["PECS"] - 945) < 2
assert abs(table["2020-02-20"]["DV01"] - 8785) < 2 and abs(mar["DV01"] - 5236) < 2

# The P&L explain and the hedge with the wrong sign (Sec. 4B.8)
print({k: round(v, 1) for k, v in explain(feb["price"], feb["D_mod"], feb["C_mod"],
                                           0.0076 - 0.0152, 0.0824 - 0.0198, mar["price"]).items()})
ust = risk_at_yield(0.0152, 0.0152, 20)
print("hedge ratio", round(feb["D_mod"] * feb["price"] / (ust["D_mod"] * 100.0), 3),
      "hedge P&L", round(-9.5e6 * (price(0.0076, 0.0152, 20) - 100.0) / 100.0))

# Key rates sum to effective duration; the bullet's OAS is its Z; the make-whole never binds
t_fa, cf_fa = cashflows(0.045, 20)
disc_mar, z_mar = flat_curve(0.0076), mar["Z"] / 1e4
krd = key_rate_durations(t_fa, cf_fa, disc_mar, z_mar, [2.0, 5.0, 10.0, 30.0])
d_eff, _ = effective(lambda h: float(np.sum(cf_fa * disc_mar(t_fa) * np.exp(-(z_mar + h) * t_fa))))
assert abs(krd.sum() - d_eff) < 1e-4 and abs(d_eff - risk_at_yield(0.09, 0.045, 20)["D_mac"]) < 1e-4
mw_calls = {k: None for k in range(2, 40, 2)}
for d, (y_b, y_t) in dates.items():                                  # the OAS row of Table 4B.1
    dt_fa, rates_fa = ho_lee(flat_curve(y_t), 10.0, 40, 0.01)
    flows_fa = on_grid(t_fa, cf_fa, dt_fa, 40)
    oas_d = oas(table[d]["price"], flows_fa, dt_fa, rates_fa, mw_calls, mw=0.005)
    assert abs(oas_d - table[d]["Z"] / 1e4) < 1e-9
assert abs(lattice_price(flows_fa, dt_fa, rates_fa, z_mar, mw_calls, 0.005)
           - lattice_price(flows_fa, dt_fa, rates_fa, z_mar)) < 1e-12
try:
    pecs(39.0, t_fa, cf_fa, 0.0076)
    raise AssertionError("a bond below its recovery must have no PECS")
except ValueError:
    pass

# Brambleworth on a lattice: zero-vol OAS is the spread to worst; curve shift = spread shift; OAS < Z
disc_b = flat_curve(0.03)
t_b, cf_b = cashflows(0.0925, 10)
calls_b = {4: 104.625, 5: 104.625, 6: 102.3125, 7: 102.3125, 8: 100.0, 9: 100.0}
stw = min(z_spread(103.0, *workout_flows(0.0925, k, K), disc_b) for k, K in [*calls_b.items(), (10, 100.0)])
dt_b, rates_0 = ho_lee(disc_b, 5.0, 10, 0.0)
flows_b = on_grid(t_b, cf_b, dt_b, 10)
assert abs(oas(103.0, flows_b, dt_b, rates_0, calls_b) - stw) < 1e-9
_, rates_b = ho_lee(disc_b, 5.0, 10, 0.01)
_, rates_h = ho_lee(lambda t: disc_b(t) * np.exp(-1e-3 * np.asarray(t, dtype=float)), 5.0, 10, 0.01)
s_b = oas(103.0, flows_b, dt_b, rates_b, calls_b)
assert abs(lattice_price(flows_b, dt_b, rates_h, s_b, calls_b)
           - lattice_price(flows_b, dt_b, rates_b, s_b + 1e-3, calls_b)) < 1e-9
assert s_b < z_spread(103.0, t_b, cf_b, disc_b)
_, rates_b2 = ho_lee(disc_b, 5.0, 10, 0.02)
print("Brambleworth OAS (bp) at 100bp and 200bp vol:", round(1e4 * s_b),
      round(1e4 * oas(103.0, flows_b, dt_b, rates_b2, calls_b)))
print("Larkspur DM (bp) at 97 and 84:", [round(1e4 * discount_margin(p, 0.0375, 0.04, 3.0)) for p in (97.0, 84.0)])
```


## F.12-B: Chapter 12-B: The Restructuring Process as a State Machine: Documents, Liens, Intercreditor Agreements, Out-of-Court and Chapter 11 {#code-12b}

Listings from `12_ch12b_the_restructuring_process_as_a_state_machine.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 12-B.1: restructuring_state_machine.py: the restructuring process as a state machine {#code-12b-1}

```python
"""restructuring_state_machine.py (Chapter 12-B).

Four layers, kept apart: a timed automaton whose guards are probabilities (12B.4),
contract arithmetic (12B.1-12B.6), statutory clocks (12B.5) and the pricing
resolvent (12B.7). Claims and values in $mm, intensities per year, rates as annual
decimals, recoveries as fractions of allowed claim. Every generator G is a P object.
"""
from __future__ import annotations

import datetime as dt
import math
from dataclasses import dataclass, field
from typing import Callable

import numpy as np

Guard = Callable[[dict, dict], float]  # (document state, clocks) -> P(guard holds)


# ---------------------------------------------------------------- legal layer
@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    event: str
    guard: Guard = lambda doc, clk: 1.0
    resets: tuple[str, ...] = ()
    forced: bool = False  # fires when an invariant of `src` is about to fail


@dataclass
class Machine:
    edges: list[Edge]
    invariants: dict[str, dict[str, float]] = field(default_factory=dict)
    state: str = "Performing"
    clocks: dict[str, float] = field(default_factory=dict)
    t: float = 0.0  # days elapsed
    log: list[tuple[float, str, str, str, float]] = field(default_factory=list)

    def legal_edges(self, doc: dict) -> list[tuple[Edge, float]]:
        """Every edge out of the current state with a positive guard. Never picks one."""
        out = []
        for e in self.edges:
            if e.src != self.state:
                continue
            p = float(e.guard(doc, self.clocks))
            if not 0.0 <= p <= 1.0:
                raise ValueError(f"guard on {e.event!r} returned {p}")
            if p > 0.0:
                out.append((e, p))
        return out

    def fire(self, event: str, doc: dict) -> str:
        """Take a legal edge. The log keeps the guard's value so a later ruling can revalue it."""
        for e, p in self.legal_edges(doc):
            if e.event == event:
                for c in e.resets:
                    self.clocks[c] = 0.0
                self.log.append((self.t, self.state, e.dst, event, p))
                self.state = e.dst
                return self.state
        raise ValueError(f"{event!r} is not a legal edge from {self.state!r}")

    def advance(self, days: float, doc: dict) -> str:
        """Run every clock; when an invariant binds, fire the forced edge at the deadline."""
        while days > 0:
            inv = self.invariants.get(self.state, {})
            for c in inv:
                self.clocks.setdefault(c, 0.0)
            slack = min((cap - self.clocks[c] for c, cap in inv.items()), default=math.inf)
            step = min(days, max(slack, 0.0))
            for c in self.clocks:
                self.clocks[c] += step
            self.t += step
            days -= step
            if days > 0:
                forced = [e for e, _ in self.legal_edges(doc) if e.forced]
                if not forced:
                    raise RuntimeError(f"invariant fails in {self.state!r} and no edge is forced")
                self.fire(forced[0].event, doc)
        return self.state


# ------------------------------------------------------------- contract layer
def effective_threshold(implementations: list[list[float]]) -> float:
    """12B.1: min over implementations of the max threshold among the rights each touches."""
    return min(max(thetas) for thetas in implementations)


def blocking_stake(theta: float, turnout: float = 1.0) -> float:
    """12B.3: a no-voter blocks an amount test of `theta` (share of the amount voting) with
    any share above this, when everyone else turns out at `turnout` and votes yes."""
    t = turnout
    return (1 - theta) * t / (1 - (1 - theta) * (1 - t))


@dataclass
class Silo:
    value: float
    tiers: list[list[str]]  # lien order; classes within one tier share pro rata


def _pro_rata(amount: float, owed: dict[str, float]) -> dict[str, float]:
    total = sum(owed.values())
    if total <= 0.0:
        return {k: 0.0 for k in owed}
    paid = min(amount, total)
    return {k: paid * v / total for k, v in owed.items()}


def silo_waterfall(claims: dict[str, float], silos: list[Silo], unencumbered: float,
                   admin: float = 0.0, subordination=()) -> dict[str, float]:
    """12B.2 in four steps: silos, deficiencies, the pool, turnover. `subordination` is a
    list of (junior, [beneficiaries]) and runs in the order given."""
    got = dict.fromkeys(claims, 0.0)
    for s in silos:
        left = s.value
        for tier in s.tiers:
            paid = _pro_rata(left, {k: claims[k] - got[k] for k in tier})
            for k, x in paid.items():
                got[k] += x
            left = max(left - sum(paid.values()), 0.0)
        unencumbered += left  # equity in the collateral belongs to the estate
    dist = _pro_rata(max(unencumbered - admin, 0.0), {k: claims[k] - got[k] for k in claims})
    for junior, seniors in subordination:
        moved = _pro_rata(dist[junior], {b: claims[b] - got[b] - dist[b] for b in seniors})
        dist[junior] -= sum(moved.values())
        for b, x in moved.items():
            dist[b] += x
    return {k: (got[k] + dist[k]) / claims[k] for k in claims}


def call_spread_recoveries(V: float, claims: list[float]) -> list[float]:
    """12B.6: C_j R_j = (V - K_{j-1})^+ - (V - K_j)^+, classes in priority order."""
    out, K = [], 0.0
    for c in claims:
        out.append((max(V - K, 0.0) - max(V - K - c, 0.0)) / c)
        K += c
    return out


def fulcrum(V: float, claims: list[float]) -> int | None:
    """min{j : K_j > V}. At V == K_j class j is whole and the fulcrum is j + 1, at zero
    recovery. None means every class is whole and old equity is in the money."""
    K = 0.0
    for j, c in enumerate(claims):
        K += c
        if K > V:
            return j
    return None


def fulcrum_deltas(V_samples, claims: list[float]):
    """pi_j = P(class j is the fulcrum) over draws of V (say which measure drew them), and
    the expected value delta pi_j / C_j per $mm of V."""
    V = np.asarray(V_samples, float)
    K = np.concatenate([[0.0], np.cumsum(claims)])
    pi = np.array([np.mean((K[j] <= V) & (V < K[j + 1])) for j in range(len(claims))])
    return pi, pi / np.asarray(claims, float)


def rollup_transfer(W: float, F: float, M: float, kappa: float) -> float:
    """12B.5: recovery lost by class members outside the DIP group, R - R'."""
    rolled = kappa * M
    if rolled > min(W, F):
        raise ValueError("roll-up exceeds the value the class receives")
    return 0.0 if W >= F else rolled * (F - W) / (F * (F - rolled))


def cramdown_price(c: float, y: float, n: int) -> float:
    """12B.6: takeback paper per unit of allowed secured claim, 1 - (y - c) a_n(y)."""
    a = n if y == 0 else (1 - (1 + y) ** -n) / y
    return 1 - (y - c) * a


# ---------------------------------------------------------------- clock layer
def _add_months(d: dt.date, months: int) -> dt.date:
    y, m = divmod(d.month - 1 + months, 12)
    for day in (d.day, 30, 29, 28):
        try:
            return dt.date(d.year + y, m + 1, day)
        except ValueError:
            pass
    raise ValueError(d)


def statutory_clocks(petition: dt.date) -> dict[str, dt.date]:
    """12B.5 clock table from a voluntary petition (the order for relief). Court-set clocks
    (challenge period, general bar date, DIP milestones) are case inputs, not statute."""
    day = lambda n: petition + dt.timedelta(days=n)
    return {
        "interim_relief_window_ends": day(21),                  # Rule 6003
        "exclusive_filing_ends": day(120),                      # 1121(b)
        "exclusive_solicitation_ends": day(180),                # 1121(c)(3)
        "exclusive_filing_cap": _add_months(petition, 18),      # 1121(d)(2)
        "exclusive_solicitation_cap": _add_months(petition, 20),
        "lease_decision_with_extension": day(210),              # 365(d)(4)
        "governmental_bar_date": day(180),                      # 502(b)(9)
        "avoidance_limitations": _add_months(petition, 24),     # 546(a)
        "preference_lookback_start": day(-90),                  # 547(b)(4)
        "insider_lookback_start": _add_months(petition, -12),
        "goods_503b9_lookback_start": day(-20),                 # 503(b)(9)
    }


def transfer_trace(claim_kind: str, proof_filed: bool) -> str:
    """12B.8, Rule 3001(e): what a claim transfer leaves on the docket."""
    if claim_kind == "public_bond":
        return "none: settles through DTC"
    if proof_filed:
        return "evidence of transfer; the transferor has 21 days to object"
    return "only the transferee or an indenture trustee may file the proof"


# ---------------------------------------------------------- probability layer
def resolvent(G, transient: list[int], absorbing: list[int], r: float = 0.0):
    """12B.7: U = (rI - G_TT)^-1 G_TA, W = (rI - G_TT)^-1 U, m = (-G_TT)^-1 1.
    Rows are transient states, columns absorbing ones. Linear solves, no inverse."""
    G = np.asarray(G, float)
    if (G - np.diag(np.diag(G)) < 0).any() or not np.allclose(G.sum(axis=1), 0.0):
        raise ValueError("not a generator: off-diagonals must be >= 0 and rows sum to 0")
    GTT = G[np.ix_(transient, transient)]
    A = r * np.eye(len(transient)) - GTT
    U = np.linalg.solve(A, G[np.ix_(transient, absorbing)])
    W = np.linalg.solve(A, U)
    m = np.linalg.solve(-GTT, np.ones(len(transient)))  # singular: a case that cannot end
    return U, W, m


# ------------------------------------------------------------------ self-test
def _self_test() -> str:
    def close(a, b, tol=1e-3):
        assert abs(a - b) < tol, (a, b)

    # Moyer's Dead Co.: assets 75, all unsecured; the sub is subordinated to the bank only
    r = silo_waterfall({"bank": 50, "trade": 50, "sub": 100}, [], 75.0,
                       subordination=[("sub", ["bank"])])
    close(r["bank"], 1.0); close(r["trade"], 0.375); close(r["sub"], 0.0625)
    # 12B.2: lien subordination, then payment subordination as well
    claims, silo = {"1L": 100, "2L": 100, "U": 100}, [Silo(80.0, [["1L"], ["2L"]])]
    r = silo_waterfall(claims, silo, 60.0)
    close(r["1L"], 0.8545); close(r["2L"], 0.2727); close(r["U"], 0.2727)
    r = silo_waterfall(claims, silo, 60.0, subordination=[("2L", ["1L"])])
    close(r["1L"], 1.0); close(r["2L"], 0.1273); close(r["U"], 0.2727)
    # thresholds, the fulcrum boundary, roll-up, cramdown
    close(blocking_stake(2 / 3, 0.7), 0.2593)
    close(effective_threshold([[0.5, 1.0], [0.5, 2 / 3]]), 2 / 3)
    assert fulcrum(100.0, [100.0, 50.0]) == 1
    assert call_spread_recoveries(100.0, [100.0, 50.0]) == [1.0, 0.0]
    pi, delta = fulcrum_deltas([50, 120, 140, 200], [100.0, 50.0])
    close(pi[0], 0.25); close(pi[1], 0.5); close(delta[1], 0.01)
    close(rollup_transfer(910, 1400, 150, 1.0), 0.042)
    close(cramdown_price(0.085, 0.11, 7), 0.882)
    # the Halvorsen clock (12B.9): Petition, Contested, Solicitation | Effective, Sale
    G = [[-4.0, 1.0, 3.0, 0.0, 0.0],
         [0.0, -2.5, 2.0, 0.0, 0.5],
         [0.0, 0.0, -6.0, 6.0, 0.0],
         [0.0] * 5, [0.0] * 5]
    U, W, m = resolvent(G, [0, 1, 2], [3, 4], r=0.05)
    close(U[0, 0], 0.927); close(U[0, 1], 0.048); close(W[0, 0], 0.457); close(m[0], 0.508)
    # out of court: a Serta blocker closes the uptier; the grace invariant forces the EoD
    edges = [
        Edge("Stressed", "Grace", "missed_coupon", resets=("grace",)),
        Edge("Grace", "EoD", "grace_expires", forced=True),
        Edge("Grace", "Petition", "file"),
        Edge("Stressed", "Post-LMT", "uptier",
             guard=lambda doc, clk: 0.0 if doc["subordination_sacred"] else 1.0),
        Edge("Stressed", "Post-LMT", "exchange", guard=lambda doc, clk: doc["p_min_tender"]),
    ]
    doc = {"subordination_sacred": True, "p_min_tender": 0.35}
    mach = Machine(edges, invariants={"Grace": {"grace": 30.0}}, state="Stressed")
    assert {e.event for e, _ in mach.legal_edges(doc)} == {"missed_coupon", "exchange"}
    try:
        mach.fire("uptier", doc)
        raise AssertionError("a sacred right was amended by a majority")
    except ValueError:
        pass
    mach.fire("missed_coupon", doc)
    assert mach.advance(28, doc) == "Grace"
    assert mach.advance(5, doc) == "EoD" and mach.log[-1][0] == 30.0
    # clocks and transfers
    c = statutory_clocks(dt.date(2026, 3, 31))
    assert c["exclusive_filing_ends"] == dt.date(2026, 7, 29)
    assert c["exclusive_filing_cap"] == dt.date(2027, 9, 30)
    assert transfer_trace("public_bond", True).startswith("none")
    return "restructuring_state_machine: all checks passed"


if __name__ == "__main__":
    print(_self_test())
```


## F.3-B: Chapter 3-B: Your First Year on the Desk: The Day, the Week, the Quarter, and the Twelve Mistakes Ex-Bankers Make {#code-3b}

Listings from `03_ch03b_your_first_year_on_the_desk.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 3-B.1: desk_calendar.py: venue calendars, versioned contract clocks and event features {#code-3b-1}

```python
# desk_calendar.py (Chapter 3-B): venue calendars, versioned contract clocks, event features, Edge Ledger.
# Dates are datetime.date. Windows and countdowns are business days on the named venue calendar.
# Holiday sets are illustrative 2026 subsets; load the published SIFMA and NYSE tables in production.
import math
import random
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

random.seed(2026)  # only the synthetic ledger in the tests uses randomness

HOLIDAYS = {
    # SIFMA recommends full closes on Columbus Day and Veterans Day while the NYSE is open (App D).
    "SIFMA": {date(2026, 9, 7), date(2026, 10, 12), date(2026, 11, 11),
              date(2026, 11, 26), date(2026, 12, 25)},
    "NYSE": {date(2026, 4, 3), date(2026, 9, 7), date(2026, 11, 26), date(2026, 12, 25)},
}
SETTLEMENT = {  # class -> (calendar, business-day offset); loan offsets are targets, not cash dates (App D)
    "corp_bond": ("SIFMA", 1), "etf": ("NYSE", 1), "par_loan": ("SIFMA", 7), "distressed_loan": ("SIFMA", 20),
}
CONTRACT_KINDS = {"coupon", "record", "grace_end", "notice_cure_end", "consent_deadline", "early_tender",
                  "call", "maturity", "rsa_milestone", "nda_outside", "claim_transfer_objection"}


def is_business_day(d, cal):
    return d.weekday() < 5 and d not in HOLIDAYS[cal]


def roll_forward(d, cal):
    """Following convention: the first business day on or after d."""
    while not is_business_day(d, cal):
        d += timedelta(days=1)
    return d


def add_business_days(d, n, cal):
    step, k = (1 if n >= 0 else -1), 0
    while k < abs(n):
        d += timedelta(days=step)
        if is_business_day(d, cal):
            k += 1
    return d


def business_days_between(a, b, cal):
    """Business days in (a, b]; negative when b is before a."""
    if b < a:
        return -business_days_between(b, a, cal)
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        n += int(is_business_day(d, cal))
    return n


def settle_date(trade_date, instrument_class):
    cal, k = SETTLEMENT[instrument_class]
    return add_business_days(trade_date, k, cal)


def grace_end(missed_payment_date, days=30, basis="calendar", cal="SIFMA"):
    """Last day of a grace period, raw and rolled forward. Which one applies is in the indenture."""
    if basis == "business":
        end = add_business_days(missed_payment_date, days, cal)
        return end, end
    end = missed_payment_date + timedelta(days=days)
    return end, roll_forward(end, cal)


def index_roll_dates(year, cal="SIFMA"):
    """CDX/iTraxx roll on 20 March and 20 September, moved to the next business day (proxy calendar)."""
    return [roll_forward(date(year, 3, 20), cal), roll_forward(date(year, 9, 20), cal)]


@dataclass(frozen=True)
class ContractEvent:
    event_id: str      # one logical event across all its versions, e.g. 'HALV-consent'
    instrument: str    # surrogate key, never a CUSIP: an exchange changes CUSIPs, not instruments
    kind: str
    event_date: date
    known_at: date     # when the desk learned this version of the date
    source: str        # 'indenture', '8-K', 'docket', 'vendor', 'desk'


def as_of(events, t):
    """Bitemporal read: the latest version of each logical event known on or before t."""
    best = {}
    for e in events:
        if e.known_at <= t and (e.event_id not in best or e.known_at > best[e.event_id].known_at):
            best[e.event_id] = e
    return list(best.values())


CROSSWALK = {}  # cusip -> instrument surrogate key


def instrument_of(cusip):
    return CROSSWALK[cusip]


def features(events, instrument, t, cal="SIFMA", window=10):
    live = [e for e in as_of(events, t) if e.instrument == instrument and e.event_date >= t]
    contract = [business_days_between(t, e.event_date, cal) for e in live if e.kind in CONTRACT_KINDS]
    nda = [business_days_between(t, e.event_date, cal) for e in live if e.kind == "nda_outside"]
    since_roll = [business_days_between(r, t, cal) for r in index_roll_dates(t.year, cal)]
    return {
        "days_to_next_contract_event": min(contract) if contract else None,
        "in_contract_window": int(bool(contract) and min(contract) <= window),
        "in_cleansing_window": int(bool(nda) and min(nda) <= window),  # scheduling input only (3B.5)
        "in_roll_week": int(any(0 <= g < 5 for g in since_roll)),
    }


@dataclass
class LedgerEntry:
    view_id: str
    logged_at: date
    instrument: str
    direction: int          # +1 long credit risk, -1 short credit risk ("bought protection" is -1)
    prob: float             # stated probability that the view is right at the horizon
    horizon_bd: int
    size_and_hedge: str
    kill_condition: str
    decay_class: str        # 'days', 'weeks', 'months', 'never'
    ido_markout_bp: dict = field(default_factory=dict)  # {1: x, 5: y, 20: z}, beta stripped, filled later
    outcome: Optional[int] = None                        # 1 right, 0 wrong, None while open


def hit_rate_se(outcomes):
    n = len(outcomes)
    p = sum(outcomes) / n
    return p, math.sqrt(p * (1 - p) / n)


def brier(probs, outcomes):
    return sum((q - y) ** 2 for q, y in zip(probs, outcomes)) / len(probs)


if __name__ == "__main__":
    # 1. Columbus Day: a T+1 bond trade on Friday 9 Oct 2026 settles Tuesday; a T+1 ETF trade settles Monday.
    assert settle_date(date(2026, 10, 9), "corp_bond") == date(2026, 10, 13)
    assert settle_date(date(2026, 10, 9), "etf") == date(2026, 10, 12)

    # 2. Halvorsen 6s: an $18mm coupon (600 x 6% / 2) missed on Friday 13 Nov 2026 (illustrative date).
    assert abs(600 * 0.06 / 2 - 18.0) < 1e-12
    end, rolled = grace_end(date(2026, 11, 13))
    assert end == date(2026, 12, 13) and end.weekday() == 6 and rolled == date(2026, 12, 14)
    assert date(2026, 11, 13) + timedelta(days=28) == date(2026, 12, 11)  # day 28: RSA and petition (12B.9)

    # 3. The A/B exchange: two CUSIPs, one instrument. A consent deadline extended three times.
    CROSSWALK.update({"HALV144A0": "HALV-7.25-2029", "HALVREG00": "HALV-7.25-2029"})
    assert instrument_of("HALV144A0") == instrument_of("HALVREG00")
    versions = [(date(2026, 10, 15), date(2026, 10, 1)), (date(2026, 10, 22), date(2026, 10, 14)),
                (date(2026, 10, 29), date(2026, 10, 21)), (date(2026, 11, 5), date(2026, 10, 28))]
    ev = [ContractEvent("HALV-consent", "HALV-7.25-2029", "consent_deadline", d, k, "8-K") for d, k in versions]
    f13 = features(ev, instrument_of("HALV144A0"), date(2026, 10, 13))
    f20 = features(ev, instrument_of("HALVREG00"), date(2026, 10, 20))
    assert f13["days_to_next_contract_event"] == 2  # sees 15 Oct, not the 5 Nov it could not yet know
    assert f20["days_to_next_contract_event"] == 2 and f20["in_contract_window"] == 1

    # 4. The roll: 20 September 2026 is a Sunday, so the roll week starts Monday 21 September.
    assert index_roll_dates(2026)[1] == date(2026, 9, 21)
    assert features([], "ANY", date(2026, 9, 25))["in_roll_week"] == 1
    assert features([], "ANY", date(2026, 9, 28))["in_roll_week"] == 0

    # 5. Measurement (3B.7): 22 of 40 is 55% with SE near 7.9 points; ten 70% calls, six right, score 0.25.
    p40, se40 = hit_rate_se([1] * 22 + [0] * 18)
    assert abs(p40 - 0.55) < 1e-12 and abs(se40 - 0.0787) < 1e-3
    outcomes = [1] * 6 + [0] * 4
    random.shuffle(outcomes)  # order does not matter to the score
    assert abs(brier([0.7] * 10, outcomes) - 0.25) < 1e-12
    assert abs(brier([0.6] * 10, outcomes) - 0.24) < 1e-12

    # 6. A seeded synthetic year of 400 views at a true 55%: the standard error is about 2.5 points.
    year = [int(random.random() < 0.55) for _ in range(400)]
    p400, se400 = hit_rate_se(year)
    assert abs(se400 - 0.0249) < 0.003
    entry = LedgerEntry("TM-0001", date(2026, 10, 20), "BRAM-9.25-SSN", -1, 0.6, 20,
                        "$5mm, DTS-hedged in CDX HY", "refinancing launched at or above par", "days")
    assert entry.outcome is None and entry.ido_markout_bp == {}
    print(f"40 views: {p40:.3f} +/- {se40:.3f}; 400 views: {p400:.3f} +/- {se400:.3f}")
```


## F.8-B: Chapter 8-B: The Risk Model You Run Every Morning: Factors, Idiosyncratic Variance, Jump-to-Default, Stress and the Limit Sheet {#code-8b}

Listings from `08_ch08b_the_risk_model_and_the_limit_sheet.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 8-B.1: risk_model.py: the morning risk model for a credit book {#code-8b-1}

```python
"""risk_model.py (Chapter 8-B): the morning risk model for a credit book.

Gaussian layer: EWMA factor covariance with shrinkage, DTS-scaled spread loadings,
idiosyncratic variance by rating x price bucket, and a sub-80 equity regime with
hysteresis. Jump layer: issuer-level JTD with Beta recoveries under P, simulated
separately and never folded into the Gaussian variance. Then VaR/ES on the mixture,
stress, Kupiec and Christoffersen backtests, and the limit sheet.
Units: $mm for P&L and notionals, decimals for prices (fraction of par), spreads,
yields and probabilities; DTS in years x decimal spread; time in years.
"""
import numpy as np
from scipy.special import xlogy
from scipy.stats import beta as beta_dist, chi2

RNG = np.random.default_rng(20261018)
SNAP = ("15:00", "America/New_York")
COND_ALARM = 1e6


class RiskModelError(Exception):
    """Raised instead of guessing."""


def check_snaps(snaps):
    """snaps: dict input name -> (wall clock, time zone). All must equal SNAP."""
    bad = {k: v for k, v in snaps.items() if tuple(v) != SNAP}
    if bad:
        raise RiskModelError(f"snap mismatch: {bad}")


def price_bucket(price, in_equity_regime=False, enter=0.80, leave=0.85):
    """Price bucket with hysteresis: enter the equity regime below 80, leave above 85."""
    if price < enter or (in_equity_regime and price < leave):
        return "lt80"
    if price < 0.90:
        return "80-90"
    if price < 0.95:
        return "90-95"
    return "ge95"


def build_loadings(positions, factor_names, cell_sens, cell_est, equity_beta):
    """n x K loadings per $ of market value. Spread loadings are -DTS x b_{g,k};
    rate loadings are -KRD; estimated loadings (liquidity, residual, basis) fall back
    own -> issuer sibling (rescaled by DTS) -> cell (per unit DTS) -> refuse."""
    idx = {f: j for j, f in enumerate(factor_names)}
    B = np.zeros((len(positions), len(factor_names)))
    siblings = {}
    for p in positions:
        if p.get("est"):
            siblings.setdefault(p["issuer"], p)
    for i, p in enumerate(positions):
        if p["bucket"] == "lt80":                      # equity regime (Section 8B.4)
            if p["id"] not in equity_beta:
                raise RiskModelError(f"{p['id']}: below 80 with no equity loading")
            B[i, idx["EQ"]] = equity_beta[p["id"]]     # recovery route: H -> 0 on rates
            continue
        for tenor, krd in p["krd"].items():
            B[i, idx["KR" + tenor]] = -krd
        if p["cell"] not in cell_sens:
            raise RiskModelError(f"{p['id']}: no sensitivity for cell {p['cell']}")
        for f, b in cell_sens[p["cell"]].items():
            B[i, idx[f]] = -p["dts"] * b
        est = p.get("est")
        if not est and p["issuer"] in siblings:
            ref = siblings[p["issuer"]]
            est = {f: v * p["dts"] / ref["dts"] for f, v in ref["est"].items()}
        if not est and p["cell"] in cell_est:
            est = {f: v * p["dts"] for f, v in cell_est[p["cell"]].items()}
        if not est:
            raise RiskModelError(f"{p['id']}: no loading and no fallback")
        for f, v in est.items():
            B[i, idx[f]] = v
    return B


def ewma_cov(X, halflife=60):
    """EWMA covariance (zero mean) of a T x K panel of factor returns, oldest first."""
    lam = 0.5 ** (1.0 / halflife)
    w = lam ** np.arange(X.shape[0] - 1, -1, -1)
    w = w / w.sum()
    return (X * w[:, None]).T @ X


def factor_cov(X, halflife=60, delta=0.25):
    """Shrink the EWMA covariance toward a constant-correlation target with weight
    delta (estimated by creditstats.py's Ledoit-Wolf in production), then check it."""
    S = ewma_cov(X, halflife)
    sd = np.sqrt(np.diag(S))
    C = S / np.outer(sd, sd)
    K = len(sd)
    rbar = (C.sum() - K) / (K * (K - 1))
    T = rbar * np.outer(sd, sd)
    np.fill_diagonal(T, sd ** 2)
    S = (1.0 - delta) * S + delta * T
    cond = np.linalg.cond(S)
    if cond > COND_ALARM:
        raise RiskModelError(f"factor covariance condition number {cond:.2e}")
    return S


def idio_var(positions, bucket_vol_pts):
    """Diagonal Omega in return units: (daily idio vol in points / 100 / price)^2."""
    v = []
    for p in positions:
        key = (p["rating"], p["bucket"])
        if key not in bucket_vol_pts:
            raise RiskModelError(f"{p['id']}: no idiosyncratic bucket {key}")
        v.append((bucket_vol_pts[key] / 100.0 / p["price"]) ** 2)
    return np.diag(v)


def gaussian_risk(w, B, SigF, Omega):
    """Volatility of P&L with its factor and idiosyncratic variances (w in $mm MV)."""
    x = B.T @ w
    fac, idi = float(x @ SigF @ x), float(w @ Omega @ w)
    return np.sqrt(fac + idi), fac, idi


def jtd_overlay(instruments):
    """Issuer -> list of legs (const, slope, (a, b)) with JTD = sum(const + slope * R).
    Long bond or loan: N(P - R); short bond: -N(P - R); bought CDS: -N(1 - R)."""
    legs = {}
    for ins in instruments:
        N, P = ins["notional"], ins.get("price", 1.0)
        kind = ins["kind"]
        if kind in ("bond", "loan"):
            c, s = N * P, -N
        elif kind == "bond_short":
            c, s = -N * P, N
        elif kind == "cds_bought":
            c, s = -N, N
        else:
            raise RiskModelError(f"unknown instrument kind {kind}")
        legs.setdefault(ins["issuer"], []).append((c, s, ins["rec"]))
    return legs


def mean_jtd(legs):
    return {i: sum(c + s * a / (a + b) for c, s, (a, b) in L) for i, L in legs.items()}


def simulate_losses(gauss, legs, lam_P, h, n_paths=200_000, rng=RNG):
    """Losses (positive = loss) over h years. gauss is a Gaussian-layer volatility
    for the horizon, or an array of historical Gaussian-layer losses to resample.
    Defaults are independent across issuers under P; recoveries within an issuer
    are comonotone (one uniform per issuer through each leg's Beta)."""
    if np.ndim(gauss) == 0:
        L = rng.standard_normal(n_paths) * float(gauss)
    else:
        L = rng.choice(np.asarray(gauss, dtype=float), size=n_paths, replace=True)
    for issuer, issuer_legs in legs.items():
        p = 1.0 - np.exp(-lam_P[issuer] * h)
        hit = rng.random(n_paths) < p
        k = int(hit.sum())
        if k == 0:
            continue
        U = rng.random(k)
        jtd = np.zeros(k)
        for c, s, (a, b) in issuer_legs:
            jtd += c + s * beta_dist.ppf(U, a, b)
        L[hit] += jtd
    return L


def historical_gaussian(w, B, X, Omega, h_days, rng=RNG):
    """Gaussian layer by historical simulation: overlapping h-day sums of past factor
    returns on today's exposures, plus normal idiosyncratic draws. Losses positive."""
    x = B.T @ w
    n = X.shape[0] - h_days + 1
    blocks = np.array([X[t:t + h_days].sum(axis=0) for t in range(n)])
    idio_sd = np.sqrt(float(w @ Omega @ w) * h_days)
    return -(blocks @ x + rng.standard_normal(n) * idio_sd)


def var_es(L, alpha=0.99):
    """VaR, ES and the Monte Carlo standard error of ES (Section 7-B.8)."""
    q = float(np.quantile(L, alpha))
    tail = L[L >= q]
    return q, float(tail.mean()), float(tail.std(ddof=1) / np.sqrt(len(tail)))


def stress(w, B, factor_names, scenario, legs):
    """Two columns, never pre-added: factor loss and jump loss (mean recoveries)."""
    shock = np.zeros(len(factor_names))
    for f, v in scenario["shocks"].items():
        shock[factor_names.index(f)] = v
    gauss_loss = -float((B.T @ w) @ shock)
    mj = mean_jtd(legs)
    jump_loss = sum(mj[i] for i in scenario.get("defaults", []) if i in mj)
    return {"gaussian": gauss_loss, "jump": jump_loss}


def kupiec_pof(x, n, p=0.01):
    """Kupiec (1995) proportion-of-failures LR and its chi-squared(1) p-value."""
    lr = -2.0 * (xlogy(n - x, 1 - p) + xlogy(x, p)
                 - xlogy(n - x, 1 - x / n) - xlogy(x, x / n))
    return float(lr), float(chi2.sf(lr, 1))


def christoffersen_ind(hits):
    """Christoffersen (1998) independence LR on a 0/1 exception sequence."""
    h = np.asarray(hits, dtype=int)
    a, b = h[:-1], h[1:]
    n00 = int(np.sum((a == 0) & (b == 0)))
    n01 = int(np.sum((a == 0) & (b == 1)))
    n10 = int(np.sum((a == 1) & (b == 0)))
    n11 = int(np.sum((a == 1) & (b == 1)))
    pi = (n01 + n11) / (n00 + n01 + n10 + n11)
    p01 = n01 / (n00 + n01) if n00 + n01 else 0.0
    p11 = n11 / (n10 + n11) if n10 + n11 else 0.0
    l0 = xlogy(n00 + n10, 1 - pi) + xlogy(n01 + n11, pi)
    l1 = (xlogy(n00, 1 - p01) + xlogy(n01, p01)
          + xlogy(n10, 1 - p11) + xlogy(n11, p11))
    lr = -2.0 * (l0 - l1)
    return float(lr), float(chi2.sf(lr, 1)), (n00, n01, n10, n11)


def limit_sheet(exposures, limits):
    """limits: line -> (soft, hard) on magnitudes. Hard breaches sort first."""
    rows = []
    for line, (soft, hard) in limits.items():
        if line not in exposures:
            raise RiskModelError(f"limit line {line} has no exposure")
        v = exposures[line]
        status = "HARD" if abs(v) > hard else ("SOFT" if abs(v) > soft else "ok")
        rows.append((line, v, soft, hard, status))
    rank = {"HARD": 0, "SOFT": 1, "ok": 2}
    return sorted(rows, key=lambda r: rank[r[4]])


# ---- Self-checks: the chapter's numbers -------------------------------------------
# 8B.1: two bonds, $60k and $80k daily vol, rho = 0.6 -> about $125.5k.
cov = np.array([[60.0 ** 2, 0.6 * 60 * 80], [0.6 * 60 * 80, 80.0 ** 2]])
sig, _, _ = gaussian_risk(np.ones(2), np.eye(2), cov, np.zeros((2, 2)))
assert abs(sig - 125.54) < 0.01

# 8B.4: hysteresis keeps a bond at 82 in the equity regime once it is there.
assert price_bucket(0.82, in_equity_regime=True) == "lt80"
assert price_bucket(0.82, in_equity_regime=False) == "80-90"

# 8B.5: Halvorsen JTD at 78 with mean recovery 15%; Brambleworth net JTD.
halv = jtd_overlay([{"issuer": "HALV", "kind": "bond", "notional": 12.0,
                     "price": 0.78, "rec": (0.6, 3.4)}])
assert abs(mean_jtd(halv)["HALV"] - 7.56) < 1e-9
bramble = jtd_overlay([
    {"issuer": "BRAM", "kind": "bond", "notional": 8.0, "price": 0.95, "rec": (0.87, 1.30)},
    {"issuer": "BRAM", "kind": "loan", "notional": 5.0, "price": 0.98, "rec": (0.93, 0.40)},
    {"issuer": "BRAM", "kind": "cds_bought", "notional": 6.0, "rec": (0.87, 1.30)},
])
assert abs(mean_jtd(bramble)["BRAM"] - 2.20) < 0.01

# 8B.6: one concentrated jump. Ten-day VaR is far above sqrt(10) x one-day VaR.
jump = {"J": [(20.0, 0.0, (1.0, 1.0))]}          # fixed $20mm JTD (slope zero)
lam = {"J": -np.log(1 - 0.0015) * 252}           # 0.15% a day under P
v1, e1, se1 = var_es(simulate_losses(1.0, jump, lam, 1 / 252, 400_000))
v10, e10, se10 = var_es(simulate_losses(np.sqrt(10), jump, lam, 10 / 252, 400_000))
assert v10 > 2.0 * np.sqrt(10) * v1 and e10 > np.sqrt(10) * e1 * 1.1

# 8B.8: seven exceptions in 250 days, in clusters of 3, 2, 1, 1.
lr, pval = kupiec_pof(7, 250, 0.01)
assert abs(lr - 5.497) < 0.01 and pval < 0.05
hits = np.zeros(250, dtype=int)
hits[[50, 51, 52, 57, 58, 120, 200]] = 1
lri, _, counts = christoffersen_ind(hits)
assert counts == (238, 4, 4, 3) and abs(lri - 13.49) < 0.01

# 8B.10 and the guards: collinear factors and mismatched snaps both refuse.
rng = np.random.default_rng(7)
z = rng.standard_normal((500, 1))
try:
    factor_cov(np.hstack([z, z * (1 + 1e-9)]), delta=0.0)
    raise AssertionError("condition-number alarm did not fire")
except RiskModelError:
    pass
try:
    check_snaps({"bonds": SNAP, "cdx": ("16:00", "America/New_York")})
    raise AssertionError("snap guard did not fire")
except RiskModelError:
    pass

# 8B.9: the cold open's three breaches.
sheet = limit_sheet({"JTD_HALV": 7.56, "DTS_B_IND": 1.61, "ES_1D": 2.7},
                    {"JTD_HALV": (7.0, 9.0), "DTS_B_IND": (1.2, 1.5), "ES_1D": (2.5, 3.0)})
assert [r[4] for r in sheet] == ["HARD", "SOFT", "SOFT"]
print("risk_model.py: all chapter checks pass")
```


## F.8-C: Chapter 8-C: The Morning Explain: P&L Attribution That Foots, From One Bond to the Book to the Signal {#code-8c}

Listings from `08_ch08c_the_morning_explain_pnl_attribution.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 8-C.1: pnl_explain.py: the morning explain, with named lines per position and hedge {#code-8c-1}

```python
# pnl_explain.py (Chapter 8-C): the morning explain. Named lines per position and hedge leg,
# the foot against official P&L with a tolerance, signal attribution with issuer netting and a
# stated cross-term rule, flags for stale marks and cash with no trade, and a dispute file.
# Money in dollars; yields and spreads in bp; accrual day counts named. In production the
# sensitivities come from risk_model.py (Chapter 8-B) and issuer IDO returns from ido_engine
# (Section 8.9); here they are arguments, so the module runs alone. Test numbers are illustrative.
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import comb, factorial

import numpy as np

PROVENANCE = ("traded", "composite", "evaluated", "model")
SOURCES = {"custodian", "model", "risk_model", "issuer_curve", "clearing", "exchange",
           "treasury", "blotter", "market", "product_control"}
PLUG_NAMES = {"other", "plug", "adjustment", "misc", "market"}


@dataclass(frozen=True)
class Line:
    name: str
    value: float            # dollars
    source: str             # one of SOURCES
    evidence: str = ""      # required when source == "product_control"


def accrual(face, coupon, days, basis=360.0, defaulted=False):
    """Coupon accrual in dollars: a contractual fact. Zero once the bond trades flat."""
    return 0.0 if defaulted else face * coupon * days / basis


def pull_to_par_linear(face, price, years_to_maturity, days, basis=360.0):
    """First-order pull-to-par in dollars; Chapter 4-B gives the constant-yield version."""
    return face / 100.0 * (100.0 - price) / years_to_maturity * days / basis


def bond_lines(face, coupon, price0, price1, days, theta, dv01_kr, dy_kr, cs01, beta,
               ds_factor, ds_issuer, convexity, defaulted=False):
    """Lines for one bond and its residual u. theta in price points per year; dv01_kr in $ per bp
    gained when each key rate falls; dy_kr, ds_factor, ds_issuer in bp. ds_issuer comes from the
    issuer's fitted curve, never from this bond's own mark."""
    pred = float(np.asarray(beta, float) @ np.asarray(ds_factor, float))
    dy_tot = float(np.mean(dy_kr)) + ds_issuer
    lines = [
        Line("accrual", accrual(face, coupon, days, defaulted=defaulted), "custodian"),
        Line("pull_to_par", face / 100.0 * theta * days / 360.0, "model"),
        Line("rates", -float(np.dot(dv01_kr, dy_kr)), "risk_model"),
        Line("spread_factor", -cs01 * pred, "risk_model"),
        Line("idiosyncratic", -cs01 * (ds_issuer - pred), "issuer_curve"),
        Line("convexity", 0.5 * face * price0 / 100.0 * convexity * (dy_tot / 1e4) ** 2, "model"),
    ]
    official = face / 100.0 * (price1 - price0) + lines[0].value
    return lines, official, official - sum(l.value for l in lines)


def cdx_protection_lines(notional, coupon_bp, factor_dprice, official_dprice, days,
                         mark_asof, today):
    """Long protection on an index (short risk). Prices in points; coupon on ACT/360.
    Stale signature: no official price change on a day the factor moved, from an old mark."""
    coupon = Line("cdx_coupon", -notional * coupon_bp / 1e4 * days / 360.0, "clearing")
    price = Line("cdx_price_factor", -notional * factor_dprice / 100.0, "risk_model")
    official = -notional * official_dprice / 100.0 + coupon.value
    u = official - coupon.value - price.value
    stale = official_dprice == 0.0 and factor_dprice != 0.0 and mark_asof < today
    return [coupon, price], official, u, stale


def series_basis_line(notional_long_risk, p_new_at_roll, p_old_at_roll):
    """Roll day: the change of instrument, from the roll quote, so a generic ticker's jump is named."""
    return Line("series_basis", notional_long_risk * (p_new_at_roll - p_old_at_roll) / 100.0,
                "blotter")


def day_one(side, composite_at_trade, fill, face):
    """Markout at horizon zero against the composite at the trade's minute; side +1 buy, -1 sell."""
    return Line("day_one", side * (composite_at_trade - fill) * face / 100.0, "blotter")


def fx_lines(face_local, p0, p1, x0, x1):
    """Local move at yesterday's rate, translation on yesterday's value, and the cross-term."""
    move = face_local * (p1 - p0) / 100.0
    return [Line("fx_local", move * x0, "risk_model"),
            Line("fx_translation", face_local * p0 / 100.0 * (x1 - x0), "market"),
            Line("fx_cross", move * (x1 - x0), "model")]


def phantom(dv01_bond, dy_at_hedge_snap, dy_at_bond_snap):
    """Fake P&L of a DV01-matched pair marked at two times (Section 3B.1); bp in, dollars out."""
    return -dv01_bond * (dy_at_bond_snap - dy_at_hedge_snap)


def tolerance(nav, es_1d, bp_of_nav=1.0, frac_of_es=0.05):
    return min(bp_of_nav * 1e-4 * nav, frac_of_es * es_1d)


def foot(official, lines, nav, es_1d):
    """official = sum(lines) + U. Refuses plugs; flags breaches and suspiciously perfect zeros."""
    for l in lines:
        if l.name.strip().lower() in PLUG_NAMES or l.source not in SOURCES:
            raise ValueError(f"line '{l.name}' is a plug: the unexplained is not adjustable")
        if l.source == "product_control" and not l.evidence:
            raise ValueError(f"product-control line '{l.name}' needs evidence")
    U = official - sum(l.value for l in lines)
    tol = tolerance(nav, es_1d)
    return {"U": U, "tol": tol, "breach": abs(U) > tol, "suspicious_zero": abs(U) < 0.005}


def true_up_line(face, composite, evaluated):
    return Line("mark_change_evaluated_vs_composite", (evaluated - composite) * face / 100.0,
                "product_control", evidence="month-end evaluated price file")


def dispute_file(position, face, composite, evaluated, evidence):
    if not evidence:
        raise ValueError("a dispute without evidence is an opinion")
    return {"position": position, "composite": composite, "evaluated": evaluated,
            "line": true_up_line(face, composite, evaluated).value, "evidence": list(evidence)}


def classify_cash(events, expected):
    """Cash that matches no coupon, settlement, margin call or fee is flagged, never booked."""
    return [{"position": pid, "amount": amt, "flag": "cash_no_trade"} for pid, amt in events
            if not any(abs(amt - e) < 0.01 for e in expected.get(pid, []))]


def corporate_action(old_carrying, new_allocations):
    """An exchange books the new instruments at the old carrying value: zero P&L."""
    if abs(sum(new_allocations.values()) - old_carrying) > 0.01:
        raise ValueError("exchange allocations must sum to the old carrying value")
    return Line("corporate_action", 0.0, "custodian")


def sleeve_ido_pnl(sleeves, ido_by_issuer):
    """Linear, issuer-netted IDO P&L per signal: {signal: {issuer: DTS-weighted $}}."""
    return {s: sum(x * ido_by_issuer[j] for j, x in pos.items()) for s, pos in sleeves.items()}


def shapley(signals, v):
    """Shapley split of v: frozenset of signals -> P&L of the book rebuilt from them."""
    n, phi = len(signals), {}
    for s in signals:
        others = [t for t in signals if t != s]
        phi[s] = sum(factorial(k) * factorial(n - k - 1) / factorial(n)
                     * (v[frozenset(S) | {s}] - v[frozenset(S)])
                     for k in range(n) for S in combinations(others, k))
    return phi


def sequential(order, v):
    out, S = {}, frozenset()
    for s in order:
        out[s] = v[S | {s}] - v[S]
        S = S | {s}
    return out


def binomial_tail(n, k, p):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


# Tests: the chapter's numbers.
assert abs(accrual(10e6, 0.06, 1) - 1666.67) < 0.01 and accrual(10e6, 0.06, 1, defaulted=True) == 0.0
assert abs(pull_to_par_linear(10e6, 88.0, 5.0, 1) - 666.67) < 0.01
assert abs(accrual(130e6, 0.07, 3) - 75_800) < 50
lines, off, u = bond_lines(10e6, 0.06, 88.0, 87.47, 1, 1.909, [1200, 2400], [1.0, 1.0], 3600,
                           [1.3], [10.0], 14.0, 20.0)
assert abs(sum(l.value for l in lines) + u - off) < 1e-6 and abs(u) < 500
cdx, off_c, u_c, stale = cdx_protection_lines(40e6, 500, -0.275, 0.0, 3, "2026-09-18", "2026-09-21")
assert abs(cdx[1].value - 110_000) < 1e-6 and abs(u_c + cdx[1].value) < 1e-6 and stale
assert abs(series_basis_line(-40e6, 104.1, 104.8).value - 280_000) < 1e-6
assert abs(day_one(+1, 97.32, 97.25, 5e6).value - 3_500) < 1e-6
assert abs(sum(l.value for l in fx_lines(10e6, 95.0, 95.5, 1.08, 1.075)) - 6_250) < 1e-6
assert abs(phantom(5_000, 0.0, -4.0) - 20_000) < 1e-9
monday = [Line("accrual", 75_800, "custodian"), Line("pull_to_par", 12_400, "model"),
          Line("rates_bonds", -52_000, "risk_model"), Line("rates_futures", 40_000, "exchange"),
          Line("spread_factor", -338_000, "risk_model"), Line("cdx_price_factor", 110_000, "risk_model"),
          Line("cdx_coupon", -16_700, "clearing"), Line("idiosyncratic", -96_300, "issuer_curve"),
          Line("convexity", 300, "model"), Line("financing", -15_000, "treasury"),
          Line("fees", -4_000, "blotter"), Line("day_one", 3_500, "blotter")]
assert abs(sum(l.value for l in monday) + 280_000) < 1e-6
first = foot(-399_000, monday, nav=100e6, es_1d=1.5e6)
assert first["breach"] and abs(first["U"] + 119_000) < 1e-6 and abs(first["tol"] - 10_000) < 1e-6
fixed = foot(-399_000, monday + [Line("mark_correction_cdx_old_series", -110_000, "product_control",
                                      evidence="dealer quotes 09:40; stale-signature flag")], 100e6, 1.5e6)
assert not fixed["breach"] and abs(fixed["U"] + 9_000) < 1e-6
try:
    foot(-399_000, monday + [Line("Other", -119_000, "model")], 100e6, 1.5e6)
    raise AssertionError("the plug was accepted")
except ValueError:
    pass
d = dispute_file("Corriveau 9.5% 2030", 8e6, 84.50, 81.50, ["TRACE 21 Oct 84.25 x 2mm", "runs 30 Oct"])
assert abs(d["line"] + 240_000) < 1e-6
assert classify_cash([("REVLON_2016_TL", 10e6)], {"REVLON_2016_TL": [150_000.0]})[0]["flag"] == "cash_no_trade"
assert corporate_action(6.0e6, {"takeback_notes": 2.5e6, "new_equity": 3.5e6}).value == 0.0
pnl = sleeve_ido_pnl({"value": {"HALV": 10e6}, "momentum": {"HALV": -6e6}}, {"HALV": -0.02})
assert abs(sum(pnl.values()) - 4e6 * -0.02) < 1e-6
v = {frozenset(): 0.0, frozenset({"mom"}): 3.0, frozenset({"val"}): 2.0, frozenset({"mom", "val"}): 2.4}
phi = shapley(["mom", "val"], v)
assert abs(phi["mom"] - 1.7) < 1e-9 and abs(phi["val"] - 0.7) < 1e-9
assert abs(sequential(["mom", "val"], v)["val"] + 0.6) < 1e-9
assert 3.0e-5 < binomial_tail(12, 7, 6 / 63) < 4.2e-5

# A seeded synthetic quarter for the ledger (Section 8C.9): noise inside tolerance, spikes on six days.
rng = np.random.default_rng(8)
U_q = rng.normal(0.0, 3_000.0, 63)
special = [0, 20, 21, 22, 41, 62]                      # roll week and three month-ends, by index
U_q[special] += -40_000.0
breach = np.abs(U_q) > 10_000.0
assert breach[special].all() and breach.sum() - breach[special].sum() <= 2
```


## F.12-C: Chapter 12-C: Plan Value Is a Negotiated Random Variable: Valuation Fights, the DIP, Roll-Ups, Exit Financing and the Fulcrum Under Uncertainty {#code-12c}

Listings from `12_ch12c_plan_valuation_dip_and_exit_as_derivatives.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 12-C.1: plan_value_engine.py: plan value, the DIP and exit as derivatives {#code-12c-1}

```python
"""plan_value_engine.py (Chapter 12-C).

Plan value as a random variable: a lognormal mixture over confirmed value, a silo
waterfall per draw, fulcrum probabilities and recovery distributions by class, the
section 1129 flags, the DIP package, the take-back transfer and the NOL line.
Money in $mm, rates as annual decimals, recoveries as fractions of allowed claim.
Every distribution here is a P object: a forecast of a judge, not a price (Law 4).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from lmt_engine import waterfall_clearing                 # Chapter 13, Listing 13.1
from restructuring_state_machine import (                 # Chapter 12-B
    Silo, silo_waterfall, rollup_transfer, cramdown_price)

rng = np.random.default_rng(1229)


@dataclass
class PlanCase:
    classes: dict[str, float]                  # allowed claim by class, after any roll-up
    silos: list[tuple[float, float, list[list[str]]]]  # (fixed value, share of remainder, lien tiers)
    fixed_carve: float                         # value carved out before shares (e.g. ABL collateral)
    pool_classes: list[str]                    # classes sharing the unsecured pool
    admin: float                               # administrative and priority claims, paid first in cash
    gift: tuple[str, str, float] | None = None # (from class, to pool, amount): a top-up the senior
                                               # funds, net of collateral surplus it already lets through
    floors: dict[str, float | None] = field(default_factory=dict)  # best-interests floors


def _class_recoveries(V: float, case: PlanCase) -> dict[str, float]:
    """One waterfall at plan value V: silos, cash wall, pool, settlement gift."""
    rem = max(V - case.fixed_carve, 0.0)
    got = dict.fromkeys(case.classes, 0.0)
    unencumbered, surplus = 0.0, 0.0
    src = case.gift[0] if case.gift is not None else None
    for fixed, share, tiers in case.silos:
        left = fixed + share * rem
        if not tiers:                          # an unencumbered silo
            unencumbered += left
            continue
        for tier in tiers:
            owed = {k: case.classes[k] - got[k] for k in tier}
            tot = sum(owed.values())
            paid = min(left, tot)
            for k, o in owed.items():
                got[k] += paid * o / tot if tot > 0 else 0.0
            left -= paid
        unencumbered += max(left, 0.0)         # equity in collateral returns to the estate
        if src is not None and any(src in t for t in tiers):
            surplus += max(left, 0.0)          # value the gift's source is already releasing
    if case.gift is not None:                  # settlement: senior tops up the pool
        amt = case.gift[2]
        moved = min(max(amt - surplus, 0.0), got[src])   # no gift once the senior is whole
        got[src] -= moved
        unencumbered += moved
    pool = max(unencumbered - case.admin, 0.0) # section 1129(a)(9): admin is paid first
    owed = {k: case.classes[k] - got[k] for k in case.pool_classes}
    tot = sum(owed.values())
    for k, o in owed.items():
        got[k] += min(pool, tot) * o / tot if tot > 0 else 0.0
    return {k: got[k] / case.classes[k] for k in case.classes}


def draw_plan_values(medians, sigmas, weights, n=200_000, rng=rng) -> np.ndarray:
    """Lognormal mixture: the judge picks expert i with probability weights[i]."""
    w = np.asarray(weights, float)
    if np.any(w < 0) or abs(w.sum() - 1.0) > 1e-9:
        raise ValueError("expert weights must be non-negative and sum to one")
    pick = rng.choice(len(w), size=n, p=w)
    mu = np.log(np.asarray(medians, float))[pick]
    sd = np.asarray(sigmas, float)[pick]
    return np.maximum(np.exp(mu + sd * rng.standard_normal(n)), 0.0)  # guard for swapped-in normals


def recovery_paths(V: np.ndarray, case: PlanCase) -> dict[str, np.ndarray]:
    out = {k: np.empty(len(V)) for k in case.classes}
    for i, v in enumerate(V):
        for k, r in _class_recoveries(float(v), case).items():
            out[k][i] = r
    return out


def fulcrum_probabilities(paths: dict[str, np.ndarray], order: list[str]) -> dict[str, float]:
    """Fulcrum = most senior class in `order` not paid in full (strict: whole means R >= 1)."""
    n = len(next(iter(paths.values())))
    first_short = np.full(n, len(order))       # len(order) means old equity is the fulcrum
    for j in reversed(range(len(order))):
        first_short = np.where(paths[order[j]] < 1.0 - 1e-12, j, first_short)
    probs = {c: float(np.mean(first_short == j)) for j, c in enumerate(order)}
    probs["old_equity"] = float(np.mean(first_short == len(order)))
    return probs


def recovery_distribution(paths, floors) -> dict[str, dict]:
    rep = {}
    for k, r in paths.items():
        f = floors.get(k)
        rep[k] = dict(mean=float(r.mean()), median=float(np.median(r)),
                      p5=float(np.percentile(r, 5)), p95=float(np.percentile(r, 95)),
                      below_floor=None if f is None else float(np.mean(r < f - 1e-12)))
    return rep


def best_interests_flags(rep) -> dict[str, bool | None]:
    """True = no path breaches; None = floor not supplied. Never pass on a missing floor."""
    return {k: (None if d["below_floor"] is None else d["below_floor"] == 0.0) for k, d in rep.items()}


def cash_wall_flag(V: np.ndarray, case: PlanCase, exit_cash: float | None) -> float | None:
    """Fraction of paths where unencumbered value plus exit cash misses the admin claims."""
    if exit_cash is None:
        return None
    rem = np.maximum(V - case.fixed_carve, 0.0)
    unenc = sum(fixed + share * rem for fixed, share, tiers in case.silos if not tiers)
    return float(np.mean(unenc + exit_cash < case.admin))


def feasibility_proxy(fcf_downside: list[float] | None, exit_debt_service: float) -> bool | None:
    if not fcf_downside:
        return None
    return min(fcf_downside) >= exit_debt_service


def dip_package_value(M, kappa, W, F, base, margin, upfront, exit_fee, tenor, group_share_after):
    """Coupon, fees and the roll-up for the lender group (section 12C.4). Raises if W < kappa*M."""
    if kappa * M > W:
        raise ValueError("roll-up exceeds value the class receives: transfer comes from outside")
    coupon = (base + margin) * M * tenor
    fees = (upfront + exit_fee) * M
    gross = kappa * M * (1.0 - min(W / F, 1.0))            # rolled claims promoted to par
    loss_pts = rollup_transfer(W, F, M, kappa)              # 12-B closed form, per remaining claim
    remaining = F - kappa * M
    assert abs(gross - loss_pts * remaining) < 1e-6, "roll-up must conserve value"
    net = gross - loss_pts * group_share_after               # the group pays part of its own bill
    return dict(coupon=coupon, fees=fees, rollup_gross=gross, rollup_net=net,
                all_in_annual=(coupon + fees) / (M * tenor))


def takeback_note_transfer(face, coupon, market_yield, years):
    exact = face * (1.0 - cramdown_price(coupon, market_yield, years))
    a = (1 - (1 + market_yield) ** -years) / market_yield
    dur_mod = sum(t * (coupon if t < years else 1 + coupon) / (1 + market_yield) ** t
                  for t in range(1, years + 1)) / ((1 + market_yield) * (1 - (market_yield - coupon) * a))
    first_order = face * dur_mod * (market_yield - coupon)
    return dict(exact=exact, first_order=first_order)


def nol_value(nol, cod, rate_lt, equity, chi, income, r, branch="l6", years=40, cap=0.8):
    """Attribute reduction first (section 108(b)), then the section 382 branch."""
    left = max(nol - cod, 0.0)
    limit = {"none": np.inf, "l6": rate_lt * equity, "l5": np.inf}[branch]
    pv = 0.0
    for t in range(1, years + 1):
        use = min(limit, left, cap * income)
        pv += chi * use / (1 + r) ** t
        left -= use
        if left <= 0:
            break
    return pv


def halvorsen_case() -> PlanCase:
    """Section 12B.9 after the roll-up and the day-71 settlement."""
    cls = {"ABL": 150.0, "DIP": 300.0, "1L": 1250.0, "UNS": 1020.0}
    silos = [(250.0, 0.0, [["ABL"], ["1L"]]),             # ABL collateral, fixed at 250
             (0.0, 32 / 35, [["DIP"], ["1L"]]),           # term collateral, primed by the DIP
             (0.0, 3 / 35, [])]                           # unencumbered
    return PlanCase(classes=cls, silos=silos, fixed_carve=250.0, pool_classes=["UNS"],
                    admin=75.0, gift=("1L", "pool", 20.0),
                    floors={"ABL": 1.0, "DIP": 1.0, "1L": 0.216, "UNS": 0.0})


def _self_test() -> str:
    case = halvorsen_case()
    r = _class_recoveries(1300.0, case)
    assert abs(r["1L"] - 0.592) < 1e-3 and abs(r["UNS"] - 35 / 1020) < 1e-3, r
    no_gift = PlanCase(**{**case.__dict__, "gift": None})
    assert abs(_class_recoveries(1300.0, no_gift)["1L"] - 0.608) < 1e-3     # 12-B before settlement
    # agreement with 12-B's silo_waterfall when nothing is waived or gifted
    simple = PlanCase(classes={"A": 100.0, "B": 200.0}, silos=[(0.0, 1.0, [["A"]]), (0.0, 0.0, [])],
                      fixed_carve=0.0, pool_classes=["A", "B"], admin=0.0)
    ref = silo_waterfall({"A": 100.0, "B": 200.0}, [Silo(value=150.0, tiers=[["A"]])], 0.0)
    mine = _class_recoveries(150.0, simple)
    assert all(abs(mine[k] - ref[k]) < 1e-9 for k in ref), (mine, ref)
    # agreement with Chapter 13's waterfall_clearing on a one-entity, two-rank stack
    pay, _ = waterfall_clearing({"co": {"value": 150.0, "parent": None}},
                                [dict(id="A", creditor="ext", debtor="co", face=100.0, rank=1),
                                 dict(id="B", creditor="ext", debtor="co", face=200.0, rank=2)])
    assert abs(pay["A"] / 100 - mine["A"]) < 1e-9 and abs(pay["B"] / 200 - 0.25) < 1e-9
    # roll-up conservation and the 4.2-point transfer
    pkg = dip_package_value(150, 1.0, 910, 1400, 0.035, 0.08, 0.03, 0.02, 0.5, 662)
    assert abs(pkg["rollup_gross"] - 52.5) < 1e-6 and abs(pkg["rollup_net"] - 24.696) < 0.01
    tb = takeback_note_transfer(350.0, 0.08, 0.10, 5)
    assert abs(tb["exact"] - 26.54) < 0.05
    # the mixture: fulcrum probabilities near 0.83 / 0.17 by Monte Carlo
    V = draw_plan_values([1300, 1900], [0.10, 0.12], [0.7, 0.3], n=100_000)
    paths = recovery_paths(V, case)
    pf = fulcrum_probabilities(paths, ["ABL", "DIP", "1L", "UNS"])
    assert abs(pf["1L"] - 0.828) < 0.01 and abs(pf["UNS"] - 0.172) < 0.01, pf
    flags = best_interests_flags(recovery_distribution(paths, {**case.floors, "UNS": None}))
    assert flags["UNS"] is None, "a missing floor must not pass"
    assert nol_value(600, 1495, 0.035, 390, 0.21, 87, 0.10) == 0.0      # attribute reduction first
    return "plan_value_engine: all checks passed"


if __name__ == "__main__":
    print(_self_test())
```


## F.1-B: Chapter 1-B: A Week in Five Quant Shops {#code-1b}

Listings from `01_ch01b_a_week_in_five_quant_shops.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 1-B.1: The week log: an immutable event row and the bitemporal read {#code-1b-1}

```python
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Iterable, Optional


class Shop(Enum):
    MARKET_MAKER = "market_maker"
    POD = "pod"
    SYSTEMATIC_AM = "systematic_am"
    BANK_DESK = "bank_desk"
    DISTRESSED = "distressed"


class ClockType(Enum):
    REGULATION = "regulation"      # a rule sets the clock (e.g. FINRA 6730, 5310; SEC 15c3-5)
    SOURCED_PRACTICE = "sourced"   # a cited public account describes the routine
    COMPOSITE = "composite"        # invented for the story, labelled as such


@dataclass(frozen=True)
class WeekEvent:
    event_id: str                        # logical id; a correction is a new row, same id
    shop: Shop
    task_class: str                      # "reconciliation", "model_review", "restricted_list", ...
    clock_type: ClockType
    occurred_at: datetime                # when it happened (or is scheduled to happen)
    known_at: datetime                   # when the shop learned this version
    source: Optional[str] = None         # citation; required unless COMPOSITE
    instrument_id: Optional[str] = None  # surrogate key, never a CUSIP (see Chapter 3-B)
    ends_at: Optional[datetime] = None   # interval end; None means open ("next 8-K")
    ticket_opened: Optional[date] = None

    def __post_init__(self) -> None:
        if self.clock_type is not ClockType.COMPOSITE and not self.source:
            raise ValueError(f"{self.event_id}: a non-composite event needs a source")
        if self.ends_at is not None and self.ends_at < self.occurred_at:
            raise ValueError(f"{self.event_id}: interval ends before it starts")

    def ticket_age_days(self, on: date) -> Optional[int]:
        return None if self.ticket_opened is None else (on - self.ticket_opened).days


def as_known(events: Iterable[WeekEvent], event_id: str, at: datetime) -> Optional[WeekEvent]:
    """Latest version of event_id that the shop knew at time `at` (bitemporal read).
    Ties on known_at are broken by list order; production feeds carry a sequence number."""
    best = None
    for e in events:
        if e.event_id == event_id and e.known_at <= at:
            if best is None or e.known_at >= best.known_at:
                best = e
    return best


def to_calendar_row(e: WeekEvent) -> dict:
    """Row shape for Chapter 3-B's desk_calendar.py (event id, date, known-at date, source)."""
    return {
        "event_id": e.event_id,
        "instrument_id": e.instrument_id,
        "event_date": e.occurred_at.date(),
        "known_at": e.known_at.date(),
        "source": e.source or "composite",
    }
```


## F.4-C: Chapter 4-C: Other Seats at the Table: One Bond, Seven Owners {#code-4c}

Listings from `04_ch04c_other_seats_at_the_table.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 4-C.1: The seat state vector: one holder of one instrument, described by its leash {#code-4c-1}

```python
import math
from dataclasses import dataclass
from datetime import date
from typing import Iterable, Optional


@dataclass(frozen=True)
class SeatState:
    """One holder (a vehicle, not a firm) of one instrument, described by its leash."""
    vehicle_id: str               # e.g. one CLO, one BDC, one insurer account
    seat_type: str                # "clo", "insurer", "bdc", "systematic", "dealer", "pod", "opportunistic"
    instrument_id: str
    face: float                   # vehicle's face holding in the instrument, $
    as_of: date                   # date of the source record (trustee report, filing, tender notice)
    next_check: Optional[date]    # next date the binding rule is tested
    rule: str                     # "ccc_bucket", "jr_oc", "rbc", "redemption_cap", "risk_budget", ...
    slack: float                  # distance to the threshold, decimal; <= 0 means binding


def tightness(s: SeatState, scale: float = 0.02) -> float:
    """1.0 at or past the threshold, decaying exponentially with slack."""
    return 1.0 if s.slack <= 0 else math.exp(-s.slack / scale)


def forced_pressure(states: Iterable[SeatState], outstanding_face: float,
                    rated_ccc: bool, today: date,
                    max_age_days: int = 45, horizon_days: int = 30) -> float:
    """Share of the issue held by CLO vehicles near a binding test inside the horizon."""
    if outstanding_face <= 0 or not rated_ccc:
        return 0.0
    total = 0.0
    for s in states:
        if s.seat_type != "clo" or s.next_check is None:
            continue
        if (today - s.as_of).days > max_age_days:
            continue                                  # stale record: holder may have sold
        days_to_check = (s.next_check - today).days
        if not 0 <= days_to_check <= horizon_days:
            continue
        total += (s.face / outstanding_face) * tightness(s)
    return min(total, 1.0)
```


## F.8-D: Chapter 8-D: The Pair Book: Long One Credit, Short Another {#code-8d}

Listings from `08_ch08d_the_pair_book_long_one_credit_short_another.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 8-D.1: pair_book.py: rulers, jumps, the stop, the borrow and the ledger row for one pair {#code-8d-1}

```python
"""pair_book.py (Chapter 8-D): rulers, jumps, the stop, the borrow and the ledger row for one pair."""
from dataclasses import dataclass
import numpy as np

try:  # the book's one copy of the DTS arithmetic (Chapter 8, section 8.9)
    from ido_engine import dts, dts_pair_hedge
except ImportError:
    def dts(D_spr, oas):
        if np.any(np.asarray(oas, dtype=float) <= 0.0):
            raise ValueError("non-positive spread: DTS undefined")
        return np.asarray(D_spr, dtype=float) * np.asarray(oas, dtype=float)

    def dts_pair_hedge(dts_long, dts_short):
        return float(dts_long / dts_short)

LIQUID_CDS = {"GM", "F"}  # illustrative stand-in for the ~100 regularly traded US names
LOG = []


@dataclass
class Leg:
    name: str
    instrument: str        # 'bond' or 'cds' (index, etf, future, equity: same fields)
    mv: float              # $mm market value; for a CDS, notional
    price: float           # per 100 (a CDS leg uses 100)
    spread: float          # decimal: Z-spread for a bond, par spread for a CDS
    spr_dur: float         # years
    recovery: float        # fraction of par
    reference: str = ""    # CDS reference entity


@dataclass
class ShortCost:
    lender: object = None          # None: nobody lends it
    fee: float = 0.0               # decimal a year on short market value
    inventory: float = 0.0         # lender's lendable market value, $mm
    share_limit: float = 0.20      # the pod's cap on its share of that inventory
    expected_recall: float = 0.0   # $mm the weather says is coming back
    financing: float = 0.0         # decimal a year on the long, net of rebate
    half_spread_bp: float = 0.0    # per leg, per trade
    hold_years: float = 0.25
    coupon: float = 0.0            # CDS standard coupon, decimal
    upfront_pts: float = 0.0       # CDS upfront paid by the protection buyer, points


def ratio(L, S, ruler, beta_L=None, beta_S=None, load_L=None, load_S=None, f_vol=None):
    """Dollars of short per dollar of long, and the ruler actually used."""
    if L.price < 70 or S.price < 70:
        LOG.append(f"{L.name}/{S.name}: a leg trades on price; ruler set to market value")
        return 1.0, "market_value"
    h_dts = dts_pair_hedge(dts(L.spr_dur, L.spread), dts(S.spr_dur, S.spread))
    if ruler == "dv01":
        return L.spr_dur / S.spr_dur, ruler
    if ruler == "dts":
        return h_dts, ruler
    if ruler in ("beta", "beta_adj"):
        if ruler == "beta_adj":  # Ben Dor's adjusted beta, (1 + beta) / 2
            beta_L, beta_S = (1 + beta_L) / 2, (1 + beta_S) / 2
        if abs(beta_S) < 0.1:
            LOG.append(f"{S.name}: trailing beta {beta_S:.2f} near zero; shrunk to DTS")
            return h_dts, "dts"
        return (beta_L / beta_S) * L.spr_dur / S.spr_dur, ruler
    if ruler == "factor":  # least factor variance; equals DTS with one relative-spread factor
        bL, bS, v = (np.asarray(x, dtype=float) for x in (load_L, load_S, f_vol))
        return float(np.sum(bL * bS * v**2) / np.sum(bS**2 * v**2)), ruler
    raise ValueError(f"unknown ruler {ruler}")


def pnl(L, S, h, ds_L_bp, ds_S_bp):
    """$mm P&L of the long L.mv and the short h * L.mv for spread moves in bp."""
    return -L.spr_dur * ds_L_bp * 1e-4 * L.mv + S.spr_dur * ds_S_bp * 1e-4 * h * L.mv


def scenarios(L, S, h, rel=0.10, parallel=10.0, idio_L=-15.0, idio_S=10.0):
    sL, sS = L.spread * 1e4, S.spread * 1e4
    return {"market_relative": pnl(L, S, h, rel * sL, rel * sS),
            "parallel": pnl(L, S, h, parallel, parallel),
            "idio_long": pnl(L, S, h, idio_L, 0.0),
            "idio_short": pnl(L, S, h, 0.0, idio_S)}


def jump_table(L, S, h, capital):
    """Loss at default per leg ($mm), expected jump under Q, worst case / capital."""
    loss_L = L.mv / (L.price / 100) * (L.price / 100 - L.recovery)
    face_S = h * L.mv / (S.price / 100)
    gain_S = face_S * (S.price / 100 - S.recovery) if S.instrument == "bond" else face_S * (1 - S.recovery)
    lam_L, lam_S = L.spread / (1 - L.recovery), S.spread / (1 - S.recovery)  # Q intensities
    return {"long_defaults": -loss_L, "short_defaults": gain_S,
            "expected_Q": lam_S * gain_S - lam_L * loss_L, "worst_share": loss_L / capital}


def max_long(L, S, h, budget, cost):
    """Largest long ($mm MV) allowed by the stop and by the borrow; the smaller binds."""
    if S.instrument == "bond" and cost.lender is None:
        return {"status": "declined", "reason": "no lender: no short leg"}
    stop = budget / ((L.price / 100 - L.recovery) / (L.price / 100))
    borrow = np.inf
    if S.instrument == "bond":
        borrow = (cost.share_limit * cost.inventory - cost.expected_recall) / h
    elif S.reference not in LIQUID_CDS:
        LOG.append(f"{S.reference}: CDS outside the liquid set; basis unquoted")
    size = min(stop, borrow)
    return {"status": "ok", "stop": stop, "borrow": borrow, "size": size,
            "binds": "stop" if stop <= borrow else "borrow"}


def carry_friction(L, S, h, cost):
    """$mm a year: spread carry, then the friction lines (both legs, in and out)."""
    short = h * L.mv
    if S.instrument == "cds":
        short_cost, fee = (cost.coupon + cost.upfront_pts / 100 / S.spr_dur) * short, 0.0
    else:
        short_cost, fee = S.spread * short, cost.fee * short
    trading = 2 * cost.half_spread_bp * 1e-4 * (L.mv + short) / cost.hold_years
    return {"carry": L.spread * L.mv - short_cost, "fee": -fee,
            "financing": -cost.financing * L.mv, "trading": -trading}


def capture(idio, leak, friction):
    return (idio + leak + friction) / idio


def ledger_row(pid, thesis, L, S, h, ruler, cost, kappa=None, leaked=""):
    short_leg = (f"{S.name}, {cost.lender}, fee {cost.fee * 1e4:.0f} bp" if S.instrument == "bond"
                 else f"{S.reference} CDS, {S.spread * 1e4:.0f} bp par on {cost.coupon * 1e4:.0f} bp coupon")
    return {"id": pid, "thesis": thesis, "long": L.name, "short": short_leg,
            "ruler": ruler, "ratio": round(h, 2), "capture": kappa, "leaked": leaked}


# ---- Self-checks: the chapter's numbers --------------------------------------------
F = Leg("Ford Credit", "bond", 40.0, 95.0, 0.0180, 4.5, 0.40)
G = Leg("GM Financial", "bond", 60.0, 98.0, 0.0120, 4.5, 0.40)
assert np.isclose(ratio(F, G, "dv01")[0], 1.00) and np.isclose(ratio(F, G, "dts")[0], 1.50)
assert np.isclose(ratio(F, G, "beta", 1.5, 0.7)[0], 2.142857, atol=1e-6)
assert ratio(F, G, "beta", 1.5, 0.05)[1] == "dts"                                  # shrunk, logged
sc = scenarios(F, G, 2.142857)
assert np.isclose(scenarios(F, G, 1.0)["market_relative"], -0.108) and np.isclose(sc["parallel"], 0.2057, atol=1e-3)
jt = jump_table(F, G, 1.5, 400.0)
assert np.isclose(jt["long_defaults"], -23.158, atol=1e-3) and np.isclose(jt["short_defaults"], 35.510, atol=1e-3)
assert np.isclose(jt["expected_Q"], 0.0155, atol=1e-4)                                # about +$15k a year
F_now = Leg("Ford Credit", "bond", 40.0, 95.0, 0.0180, 4.5, 0.40)
sz = max_long(F_now, G, 1.5, 13.0, ShortCost("agent lender", 0.0070, 300.0, 0.20, 20.0))
assert np.isclose(sz["stop"], 22.45, atol=0.01) and np.isclose(sz["borrow"], 26.67, atol=0.01)
assert sz["binds"] == "stop"
assert max_long(F_now, G, 1.5, 13.0, ShortCost(None))["status"] == "declined"
assert ratio(Leg("Ford Credit", "bond", 25.0, 60.0, 0.20, 3.0, 0.40), G, "dts")[1] == "market_value"
cds = Leg("GM 5y", "cds", 0.0, 100.0, 0.0110, 4.5, 0.40, reference="GM")
h_cds = ratio(Leg("Ford Credit", "bond", 22.5, 95.0, 0.0180, 4.5, 0.40), cds, "dts")[0]
assert np.isclose(22.5 * h_cds, 36.82, atol=0.01)                                      # §8D.7
assert np.isclose(capture(0.162, -0.0578, -0.0458), 0.3605, atol=1e-3)                 # §8D.6
print("pair_book.py: all chapter checks pass")
```


## F.2-B: Chapter 2-B: Transaction Cost Analysis for Credit: Arrival, Cover, Shortfall and the Dealer Scorecard {#code-2b}

Listings from `02_ch02b_transaction_cost_analysis_for_credit.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 2-B.1: tca.py: transaction cost analysis for an RFQ market {#code-2b-1}

```python
"""tca.py (Chapter 2-B): transaction cost analysis for an RFQ market.

Every function reads the desk's RFQ log, one row per child order, through the order
state machine of Section 27.4.2. Units: face in $mm, prices per 100 of face, costs in
dollars unless a name ends in _bp (basis points of price). side = +1 when we buy and
-1 when we sell; a positive cost is bad for us. Demo numbers are illustrative.
"""
from dataclasses import dataclass
from typing import Callable, Optional, Sequence
import math

import numpy as np

TERMINAL = ("FILLED", "EXPIRED", "EXPIRED_PARTIAL", "DONE_AWAY", "REJECTED", "CANCELLED")


@dataclass
class Order:
    order_id: str
    side: int                          # +1 we buy, -1 we sell
    target: float                      # face the optimiser asked for, $mm
    filled: float                      # face executed, $mm
    terminal: str                      # one of TERMINAL
    m_new: Optional[float]             # composite mid at NEW: the arrival benchmark
    m_routed: Optional[float] = None   # composite mid at ROUTED
    m_quoted: Optional[float] = None   # composite mid at QUOTED (None if nobody quoted)
    fill_px: Optional[float] = None    # size-weighted fill price
    cover: Optional[float] = None      # second-best response, if two or more quoted
    m_end: Optional[float] = None      # mid when the remainder is retried or abandoned
    beta_end: float = 0.0              # market part of (m_end - m_new), points
    parent_id: Optional[str] = None    # the legs of one pair share a parent
    protocol: str = "rfq"              # rfq, a2a, pt, voice, session
    regime: str = "calm"               # label in force at NEW (Section 2B.5)

    def __post_init__(self):
        if self.terminal not in TERMINAL:
            raise ValueError(f"{self.order_id}: unknown terminal state {self.terminal}")
        if self.filled > self.target + 1e-9:
            raise ValueError(f"{self.order_id}: filled more than the target")


def _usd(face_mm: float, points: float) -> float:
    """Dollars from face in $mm and a price difference in points per 100."""
    return face_mm * 1e6 * points / 100.0


def benchmarks_bp(o: Order, print_px: Optional[float] = None) -> dict:
    """One fill scored against every benchmark the log supplies, bp of price, + = cost."""
    if o.fill_px is None:
        return {}
    refs = {"arrival": o.m_new, "rfq_time": o.m_routed, "cover": o.cover,
            "next_print": print_px}
    return {k: o.side * (o.fill_px - b) / b * 1e4 for k, b in refs.items() if b is not None}


def shortfall(o: Order) -> dict:
    """Perold's shortfall for one child order, split along the log's stamps (dollars)."""
    flags = []
    m0 = o.m_new
    if m0 is None:                                   # no composite at the decision
        m0 = o.m_routed
        flags.append("no_arrival_mid")
    if m0 is None:
        return {"total": float("nan"), "flags": flags + ["unscorable"]}
    m_r = o.m_routed if o.m_routed is not None else m0
    m_q = o.m_quoted if o.m_quoted is not None else m_r
    out = dict.fromkeys(("delay", "drift", "half_spread", "opp_beta", "opp_idio"), 0.0)
    if o.filled > 0:
        if o.fill_px is None:
            raise ValueError(f"{o.order_id}: filled size but no fill price")
        out["delay"] = o.side * _usd(o.filled, m_r - m0)
        out["drift"] = o.side * _usd(o.filled, m_q - m_r)
        out["half_spread"] = o.side * _usd(o.filled, o.fill_px - m_q)
        if o.protocol == "pt":
            flags.append("basket_price_allocated")
    rest = o.target - o.filled
    if rest > 1e-9:
        if o.m_end is None:
            flags.append("unfilled_unmarked")        # flagged, never silently zero
        else:
            out["opp_beta"] = o.side * _usd(rest, o.beta_end)
            out["opp_idio"] = o.side * _usd(rest, (o.m_end - m0) - o.beta_end)
    out["total"] = sum(out.values())
    out["flags"] = flags
    return out


def event_study(sent, placebo) -> dict:
    """Leakage as sent-minus-placebo drift. Rows are orders, columns minutes after
    ROUTED; values are bp of price signed so that + means the price moved against us."""
    sent, placebo = np.asarray(sent, float), np.asarray(placebo, float)
    mu_s, mu_p = np.nanmean(sent, axis=0), np.nanmean(placebo, axis=0)
    n_s = np.sum(~np.isnan(sent), axis=0)
    n_p = np.sum(~np.isnan(placebo), axis=0)
    se = np.sqrt(np.nanvar(sent, axis=0, ddof=1) / n_s
                 + np.nanvar(placebo, axis=0, ddof=1) / n_p)
    leak = mu_s - mu_p
    return {"sent": mu_s, "placebo": mu_p, "leak": leak, "se": se, "t": leak / se}


def scorecard(dealer, regime, quoted, won, quote_mo, k: float = 20.0,
              stress_weight: float = 0.4) -> dict:
    """Per dealer: response and hit rates shrunk toward the panel with a prior worth k
    inquiries, the mean counterfactual markout of every quote shown (not only wins;
    bp, + = good for us), and the same on stress days. stress_weight is a judgment."""
    dealer, regime = np.asarray(dealer), np.asarray(regime)
    quoted, won = np.asarray(quoted, bool), np.asarray(won, bool)
    quote_mo = np.asarray(quote_mo, float)
    p_resp = quoted.mean()
    p_hit = won[quoted].mean() if quoted.any() else 0.0
    rows = {}
    for d in np.unique(dealer):
        row = {}
        for label, mask in (("all", dealer == d),
                            ("stress", (dealer == d) & (regime == "stress"))):
            n, q, h = int(mask.sum()), int((mask & quoted).sum()), int((mask & won).sum())
            row[label] = {
                "n": n,
                "resp": (q + k * p_resp) / (n + k),
                "hit": (h + k * p_hit) / (q + k),
                "quote_mo": float(np.nanmean(quote_mo[mask & quoted])) if q else float("nan"),
            }
        row["tier_score"] = ((1 - stress_weight) * row["all"]["resp"]
                             + stress_weight * row["stress"]["resp"])
        rows[str(d)] = row
    return rows


def sqrt_prior(c0_bp: float, eta_bp: float, adv_mm: float, mult: float = 1.0) -> Callable:
    """Section 4.8's square-root law as a stated prior: mult * (c0 + eta * sqrt(size/ADV))."""
    return lambda size_mm: mult * (c0_bp + eta_bp * math.sqrt(size_mm / adv_mm))


def cost_curve(size, cost_bp, edges: Sequence[float], min_count: int = 30,
               prior: Optional[Callable] = None) -> list:
    """Mean cost per size bucket with its count; a thin bucket reports the prior, flagged."""
    size, cost_bp = np.asarray(size, float), np.asarray(cost_bp, float)
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (size >= lo) & (size < hi)
        n = int(m.sum())
        est = float(cost_bp[m].mean()) if n else float("nan")
        mid = 1.5 * lo if math.isinf(hi) else (math.sqrt(lo * hi) if lo > 0 else hi / 2.0)
        use_prior = n < min_count and prior is not None
        out.append({"bucket": (lo, hi), "n": n, "estimate": est,
                    "used": prior(mid) if use_prior else est, "prior_used": use_prior})
    return out


def participation(desk_vol, trace_vol, dates: Sequence[str],
                  breaks: Sequence[str] = ("2026-08-31", "2027-08-02")) -> dict:
    """Desk volume over TRACE volume in the same bonds and window, with a 0/1 dummy per
    known break in the denominator (ISO date strings compare correctly as text)."""
    desk, trace = np.asarray(desk_vol, float), np.asarray(trace_vol, float)
    ratio = np.divide(desk, trace, out=np.full(desk.shape, np.nan), where=trace > 0)
    dummies = {b: np.array([d >= b for d in dates], dtype=int) for b in breaks}
    return {"ratio": ratio, "breaks": dummies}


def we_are_the_market(part, mo_trend, resp_trend, part_max: float = 0.20) -> np.ndarray:
    """Fires only when all three agree: participation above part_max (on the dummied
    series), residualised markouts trending against us, response counts falling."""
    part = np.asarray(part, float)
    return (part > part_max) & (np.asarray(mo_trend) < 0) & (np.asarray(resp_trend) < 0)


def legging_sd(dts: float, minutes: float, sigma_day_rel: float = 0.022,
               day_minutes: float = 390.0, rho_bridge: float = 0.0) -> float:
    """Dollar s.d. of an open DTS exposure held for `minutes`. DTS is in $ per 1% relative
    spread move; sigma_day_rel is the daily s.d. of relative spread changes (decimal).
    A bridge hedge with correlation rho leaves sqrt(1 - rho^2) of the risk."""
    sd_pct = 100.0 * sigma_day_rel * math.sqrt(minutes / day_minutes)
    return abs(dts) * sd_pct * math.sqrt(max(0.0, 1.0 - rho_bridge ** 2))


def pair_line(leg_costs: Sequence[float], dts_open: float, rel_move_pct: float,
              minutes_open: float, standing_per_day: float = 0.0, days: float = 0.0) -> dict:
    """Two-leg cost under one parent arrival: the legs' own shortfalls, the legging term
    (signed DTS left open, + = net long credit, times the relative spread move in %, so a
    widening costs a long), and the short leg's standing cost over the holding days."""
    legs = float(sum(leg_costs))
    legging = dts_open * rel_move_pct
    standing = standing_per_day * days
    return {"legs": legs, "legging": legging, "standing": standing,
            "total": legs + legging + standing,
            "legging_sd": legging_sd(dts_open, minutes_open)}


if __name__ == "__main__":
    fill = Order("2B1-demo", +1, 2.0, 2.0, "FILLED", m_new=98.38, m_routed=98.40,
                 m_quoted=98.40, fill_px=98.42, cover=98.45)
    print({k: round(v, 1) for k, v in benchmarks_bp(fill, print_px=98.47).items()})
    # arrival 4.1, rfq_time 2.0, cover -3.0, next_print -5.1

    nine = Order("2B2-unfilled", +1, 40.5, 0.0, "EXPIRED", m_new=100.00,
                 m_end=100.28, beta_end=0.11)
    sf = shortfall(nine)
    print(round(sf["opp_beta"]), round(sf["opp_idio"]), round(sf["total"]))
    # 44550 68850 113400

    trim = pair_line([14_000.0, 1_937.5], dts_open=-17_700.0, rel_move_pct=-0.25,
                     minutes_open=12.0)
    print({k: round(v) for k, v in trim.items()})
    # legs 15938, legging 4425, standing 0, total 20362, legging_sd about 6,830
```


## F.4-D: Chapter 4-D: Getting the Seat: Interviews for Market-Making and Systematic Credit, From Probability Puzzles to the Thirty-Minute Credit Pitch, and the Portfolio That Proves It {#code-4d}

Listings from `04_ch04d_getting_the_seat.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 4-D.1: interview_drills.py: seeded drills for Chapter 4-D {#code-4d-1}

```python
"""interview_drills.py: seeded drills for Chapter 4-D (illustrative numbers).

Each drill returns (question, answer, check); check(x) is True when x is within
the drill's tolerance of the answer. Home sections are in the docstrings.
"""
import math
import random


def _check(answer, tol):
    return lambda x: x is not None and abs(x - answer) <= tol


def measure_drill(rng):
    """§4D.2: two-point bond, risk-neutral default probability, with a rate."""
    hi, lo = 100.0, rng.choice([20.0, 30.0, 40.0, 50.0])
    price = rng.choice([80.0, 85.0, 88.0, 92.0])
    r = rng.choice([0.0, 0.02, 0.04])
    q_d = (hi - price * math.exp(r)) / (hi - lo)  # undiscounted mean under Q
    text = (f"Pays {hi:.0f} or {lo:.0f} in one year; price {price:.0f}; "
            f"rate {r:.0%} continuous. Q-default probability?")
    return text, q_d, _check(q_d, 0.005)


def gm_drill(rng):
    """§4D.3 and §3.2: value after n sells from new sellers, two-point prior."""
    hi, lo = 100.0, rng.choice([30.0, 40.0, 60.0])
    pi = rng.choice([0.1, 0.2, 0.3])
    n = rng.randint(1, 4)
    p_sell_bad, p_sell_good = pi + (1 - pi) / 2, (1 - pi) / 2
    odds = (p_sell_bad / p_sell_good) ** n       # prior odds 1: fifty-fifty
    post_bad = odds / (1 + odds)
    value = post_bad * lo + (1 - post_bad) * hi
    text = (f"Worth {hi:.0f} or {lo:.0f}, fifty-fifty; {pi:.0%} of sellers "
            f"informed. Value after {n} sells from new sellers?")
    return text, value, _check(value, 0.25)


def kelly_drill(rng):
    """§4D.5 and §28.4: discrete Kelly for a bond; None means no edge, no bet."""
    c = rng.choice([0.03, 0.045, 0.06])
    q_d = rng.choice([0.01, 0.031, 0.05, 0.08])
    loss = rng.choice([0.4, 0.6, 0.8, 1.0])
    f = (1 - q_d) / loss - q_d / c
    text = (f"Carry {c:.1%}, PD {q_d:.1%}, LGD {loss:.0%}. "
            f"Full-Kelly fraction of NAV (None if no edge)?")
    if f <= 0:
        return text, None, lambda x: x is None
    return text, f, _check(f, 0.01)


def stop_drill(rng):
    """§4D.5 and §8D.5: largest long that one default cannot push past a line."""
    capital = rng.choice([100.0, 200.0, 400.0])               # $mm
    line = rng.choice([0.025, 0.05, 0.075])
    price, recovery = rng.choice([(98.0, 40.0), (90.0, 30.0), (75.0, 25.0)])
    size = capital * line / ((price - recovery) / 100.0)
    text = (f"Capital ${capital:.0f}mm; one default may cost {line:.1%}. "
            f"Bond at {price:.0f}, recovery {recovery:.0f}. Largest long, $mm?")
    return text, size, _check(size, 0.1)


def ruler_drill(rng):
    """§4D.6 and §8D.3: short size under the duration, DTS or beta ruler."""
    long_mv = rng.choice([20.0, 40.0, 60.0])
    s_a, d_a = rng.choice([(380, 4.2), (300, 5.0), (450, 3.8)])
    s_b, d_b = rng.choice([(520, 4.6), (600, 4.0), (410, 5.2)])
    beta = rng.choice([0.5, 0.6, 0.8])
    ruler = rng.choice(["duration", "dts", "beta"])
    short = {"duration": long_mv * d_a / d_b,
             "dts": long_mv * d_a * s_a / (d_b * s_b),
             "beta": long_mv * d_a * beta / d_b}[ruler]
    text = (f"Long ${long_mv:.0f}mm of A ({s_a}bp, spread duration {d_a}); "
            f"short B ({s_b}bp, {d_b}); beta {beta}. Short by {ruler}, $mm?")
    return text, short, _check(short, 0.1)


def dv01_drill(rng):
    """§4D.7 and §4B.5: DV01 per $10mm = D_mod x dirty price x face x 1e-6."""
    d_mod = rng.choice([3.9, 4.2, 6.5, 8.11])
    price = rng.choice([92.39, 100.0, 108.38])
    dv01 = d_mod * price * 10_000_000 * 1e-6
    text = f"Modified duration {d_mod}, dirty price {price}. DV01 per $10mm?"
    return text, dv01, _check(dv01, 0.05 * dv01)              # mental-math band


DRILLS = [measure_drill, gm_drill, kelly_drill, stop_drill, ruler_drill,
          dv01_drill]


def session(seed, k=6):
    """A reproducible set of k drills: same seed, same questions."""
    rng = random.Random(seed)
    return [rng.choice(DRILLS)(rng) for _ in range(k)]


if __name__ == "__main__":
    # The chapter's anchors, recomputed from the drill formulas.
    assert abs((100 - 85) / 60 - 0.25) < 1e-12                    # §4D.2
    assert abs((100 - 85 * math.exp(0.04)) / 60 - 0.192) < 1e-3   # §4D.2, 4%
    assert abs(0.6 * 40 + 0.4 * 100 - 64.0) < 1e-12               # §4D.3
    assert abs(0.969 / 0.6 - 0.031 / 0.045 - 0.926) < 1e-3        # §4D.5
    assert abs(15 / 0.58 - 25.86) < 0.01                          # §4D.5 stop
    assert abs(40 * 4.2 * 380 / (4.6 * 520) - 26.69) < 0.01       # §4D.6 DTS
    assert abs(8.11 * 108.38 * 10 - 8789.6) < 1.0   # §4D.7 (4-B prints $8,785)
    for text, answer, check in session(seed=2026):
        print(text)
        assert check(answer)
```


## F.9-B: Chapter 9-B: The Bond Data Problem and the Replication Crisis {#code-9b}

Listings from `09_ch09b_the_bond_data_problem_and_the_replication_crisis.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 9-B.1: replication_harness.py: look-ahead gates and the replication of a bond signal {#code-9b-1}

```python
# replication_harness.py -- Listing 9B.1 (Chapter 9-B)
# Two gates for a candidate bond signal: (1) the signal price is never the entry
# price; (2) every screen is ex ante. Reports premium, CAPM-B alpha (Newey-West t,
# floor(T**0.25) lags), gap share, a look-ahead diagnostic and a non-standard-error
# band across screening paths. A pandas mirror of the PyBondLab 0.3.0 workflow.
import numpy as np
import pandas as pd


def newey_west_t(y, x=None):
    """OLS of y on [1, x]; returns (coefficients, Newey-West t-stats)."""
    y = np.asarray(y, float)
    X = np.ones((len(y), 1)) if x is None else np.column_stack([np.ones(len(y)), np.asarray(x, float)])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    u = y - X @ beta
    lags = int(np.floor(len(y) ** 0.25))
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for l in range(1, lags + 1):
        G = Xu[l:].T @ Xu[:-l]
        S += (1.0 - l / (lags + 1.0)) * (G + G.T)
    XtX_inv = np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(XtX_inv @ S @ XtX_inv))
    return beta, beta / se


def check_gap(panel, sig_date, base_date):
    """Gate 1: refuse any bond-month that sorts and earns on the same price."""
    bad = (panel[sig_date] >= panel[base_date]).mean()
    if bad > 0:
        raise ValueError(f"{bad:.1%} of bond-months use the signal price as the entry price")


def exante_screen(panel, ret_cap=None, tail="both", px_range=None):
    """Gate 2: drop bond-months using only formation-date information:
    the return already earned in month t (ret_lag) and the formation price (prc)."""
    keep = pd.Series(True, index=panel.index)
    if ret_cap is not None:
        if tail in ("left", "both"):
            keep &= ~(panel["ret_lag"] < -ret_cap)
        if tail in ("right", "both"):
            keep &= ~(panel["ret_lag"] > ret_cap)
    if px_range is not None:
        keep &= panel["prc"].between(*px_range)
    return panel[keep]


def expost_winsorize(panel, ret, q=0.005):
    """Look-ahead DIAGNOSTIC only: clip the holding-month return at full-sample
    percentiles, to measure how much a result leans on the future."""
    lo, hi = panel[ret].quantile([q, 1 - q])
    out = panel.copy()
    out[ret] = out[ret].clip(lo, hi)
    return out


def long_short(panel, sig, ret, n=10, within_firm=False, weight="EW"):
    """Monthly top-minus-bottom return. Single sort: top bucket minus bottom bucket.
    Within firm: each issuer's top-ranked bond minus its bottom-ranked bond, averaged."""
    out = {}
    for d, g in panel.dropna(subset=[sig, ret]).groupby("date"):
        if within_firm:
            g = g[g.groupby("firm")[sig].transform("nunique") >= 2]
            if g.empty:
                continue
            top = g.loc[g.groupby("firm")[sig].idxmax()]
            bot = g.loc[g.groupby("firm")[sig].idxmin()]
            w = np.ones(len(top)) if weight == "EW" else top["VW"].to_numpy() + bot["VW"].to_numpy()
            out[d] = np.average(top[ret].to_numpy() - bot[ret].to_numpy(), weights=w)
        else:
            if len(g) < 5 * n:
                continue
            bucket = pd.qcut(g[sig].rank(method="first"), n, labels=False)

            def leg(x):
                w = np.ones(len(x)) if weight == "EW" else x["VW"].to_numpy()
                return np.average(x[ret].to_numpy(), weights=w)

            out[d] = leg(g[bucket == n - 1]) - leg(g[bucket == 0])
    return pd.Series(out).sort_index()


def harness(panel, mktb_end, mktb_bgn, n=10, within_firm=False, weight="EW",
            caps=tuple(np.round(np.arange(0.20, 0.951, 0.05), 2))):
    panel = panel.reset_index(drop=True)
    check_gap(panel, "sig_gap_px_date", "end_base_date")   # signal gap version
    check_gap(panel, "sig_px_date", "bgn_base_date")       # return gap version
    versions = {"reference (contaminated)": ("signal", "ret_end", mktb_end),
                "signal gap": ("signal_gap", "ret_end", mktb_end),
                "return gap": ("signal", "ret_bgn", mktb_bgn)}
    report = {}
    for name, (sig, ret, mkt) in versions.items():
        ls = long_short(panel, sig, ret, n, within_firm, weight)
        m = mkt.reindex(ls.index)
        ok = m.notna().to_numpy()
        (_,), (t_mu,) = newey_west_t(ls.to_numpy()[ok])
        (a, _), (t_a, _) = newey_west_t(ls.to_numpy()[ok], m.to_numpy()[ok])
        report[name] = {"premium": ls.mean(), "t_premium": t_mu, "alpha": a, "t_alpha": t_a,
                        "months": int(ok.sum()), "bond_months": int(panel[[sig, ret]].dropna().shape[0])}
    ref, gap = report["reference (contaminated)"]["premium"], report["return gap"]["premium"]
    report["gap_share"] = 1.0 - gap / ref if ref != 0 else np.nan
    wz = long_short(expost_winsorize(panel, "ret_bgn"), "signal", "ret_bgn", n, within_firm, weight)
    report["lookahead_diagnostic"] = wz.mean() - gap
    prem = [long_short(exante_screen(panel, c, tail), "signal", "ret_bgn", n, within_firm, w).mean()
            for c in caps for tail in ("left", "right", "both") for w in ("EW", "VW")]
    q25, q75 = np.nanpercentile(prem, [25, 75])
    report["nse"] = {"paths": len(prem), "iqr": q75 - q25, "median": float(np.nanmedian(prem))}
    return report


if __name__ == "__main__":
    # Synthetic check of section 9B.4: true returns i.i.d. (no reversal at all),
    # month-end marks carry 0.5% noise; month-begin and gap prices are fresh draws.
    rng = np.random.default_rng(7)
    months = pd.period_range("2005-01", periods=120, freq="M").to_timestamp(how="end").normalize()
    nb, sd = 600, 0.005
    true = np.cumsum(rng.normal(0.004, 0.02, (len(months) + 2, nb)), axis=0)
    ne, nb_, ng = (rng.normal(0, sd, true.shape) for _ in range(3))
    rows = []
    for k, d in enumerate(months, start=1):
        p_end_prev, p_end, p_end_next = true[k - 1] + ne[k - 1], true[k] + ne[k], true[k + 1] + ne[k + 1]
        p_gap, p_bgn = true[k] + ng[k], true[k] + nb_[k]
        ret_lag = p_end - p_end_prev
        rows.append(pd.DataFrame({
            "date": d, "ID": np.arange(nb), "firm": np.arange(nb) // 3,
            "signal": -ret_lag, "signal_gap": -(p_gap - p_end_prev),
            "ret_end": p_end_next - p_end, "ret_bgn": p_end_next - p_bgn, "ret_lag": ret_lag,
            "prc": 100 * np.exp(p_end - true[0]), "VW": 1.0 + rng.random(nb), "RATING_NUM": 15,
            "sig_px_date": d, "sig_gap_px_date": d - pd.Timedelta(days=3),
            "end_base_date": d, "bgn_base_date": d + pd.Timedelta(days=1)}))
    panel = pd.concat(rows, ignore_index=True)
    mkt_end, mkt_bgn = panel.groupby("date")["ret_end"].mean(), panel.groupby("date")["ret_bgn"].mean()
    rep = harness(panel, mkt_end, mkt_bgn, caps=(0.20, 0.50, 0.95))
    for key, val in rep.items():
        print(key, val)
    assert rep["reference (contaminated)"]["premium"] > 0.002      # about 2 x 1.75 x 0.24 x 0.5%
    assert abs(rep["return gap"]["premium"]) < 0.0015               # nothing left with the gap
```


## F.10-B: Chapter 10-B: Credit Index Futures and Index Microstructure {#code-10b}

Listings from `10_ch10b_credit_index_futures_and_index_microstructure.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 10-B.1: index_micro.py: four small measurements of the index market {#code-10b-1}

```python
"""index_micro.py (Chapter 10-B): four small measurements of the index market.

turnover / roll_window_share  volume against open interest, and the expiry calendar
tff_net / spliced_change      CFTC positioning by category, with a reclassification flag
intrinsic / skew              duration-weighted intrinsic spread and the quote's distance from it
series_basis_line             the roll-day explain line (Section 8C.2)

Units: volume and OI in contracts or $mm (consistently); spreads in bp; risky
durations in years; index prices per 100; notionals in $mm. Demo numbers are the
chapter's illustrative ones except where a comment cites a source.
"""
import numpy as np
import pandas as pd


def turnover(adv, oi):
    """ADV / OI and the implied average holding period in trading days."""
    adv = pd.Series(adv, dtype=float)
    oi = pd.Series(oi, dtype=float)
    ratio = adv / oi.where(oi > 0)              # NaN, not inf, when OI is zero
    return pd.DataFrame({"turnover": ratio, "hold_days": 1.0 / ratio})


def roll_window_share(daily, expiries, window=5):
    """Share of each quarter's volume traded in the last `window` trading days
    (days with a row in the file) before each expiry.

    daily: DataFrame with 'date' and 'volume' for ONE product, any number of
    rows per date (Cboe's file has one per contract month); they are summed.
    """
    d = daily.assign(date=pd.to_datetime(daily["date"]))
    d = d.groupby("date")["volume"].sum().sort_index()
    rows, start = [], d.index.min()
    for exp in sorted(pd.to_datetime(list(expiries))):
        q = d[(d.index >= start) & (d.index < exp)]
        start = exp
        if q.empty:
            continue
        w, tot = q.iloc[-window:].sum(), q.sum()
        rows.append({"expiry": exp, "window_vol": w, "quarter_vol": tot,
                     "share": w / tot if tot > 0 else np.nan})
    cols = ["expiry", "window_vol", "quarter_vol", "share"]
    return pd.DataFrame(rows, columns=cols).set_index("expiry")


# Traders in Financial Futures column names as published; check them against the
# dataset's metadata (publicreporting.cftc.gov, dataset gpe5-46if) on first use.
TFF_FIELDS = {
    "date": "report_date_as_yyyy_mm_dd",
    "code": "cftc_contract_market_code",
    "oi": "open_interest_all",
    "dealer_long": "dealer_positions_long_all",
    "dealer_short": "dealer_positions_short_all",
    "am_long": "asset_mgr_positions_long",
    "am_short": "asset_mgr_positions_short",
    "lev_long": "lev_money_positions_long",
    "lev_short": "lev_money_positions_short",
}


def tff_net(rows, code, fields=TFF_FIELDS, jump=0.25, oi_tol=0.05):
    """Weekly net (long - short) by category for one contract code, with a flag
    for probable reclassifications: one category's net moves by more than `jump`
    x last week's OI, another moves the opposite way by more than half that, and
    OI changes by less than `oi_tol`."""
    df = pd.DataFrame(rows)
    df = df[df[fields["code"]].astype(str) == str(code)].copy()
    df["date"] = pd.to_datetime(df[fields["date"]])
    for k in ("oi", "dealer_long", "dealer_short", "am_long", "am_short",
              "lev_long", "lev_short"):
        df[k] = pd.to_numeric(df[fields[k]], errors="coerce")
    df = df.sort_values("date").set_index("date")
    net = pd.DataFrame({
        "dealer": df["dealer_long"] - df["dealer_short"],
        "asset_mgr": df["am_long"] - df["am_short"],
        "lev_funds": df["lev_long"] - df["lev_short"],
    })
    rel = net.diff().div(df["oi"].shift(1), axis=0)
    up, dn = rel.max(axis=1), rel.min(axis=1)
    big = (up > jump) | (dn < -jump)
    opposite = (up > jump / 2) & (dn < -jump / 2)
    flat_oi = df["oi"].pct_change().abs() < oi_tol
    out = net.assign(oi=df["oi"], am_short_share=df["am_short"] / df["oi"])
    out["reclass_flag"] = (big & opposite & flat_oi).fillna(False)
    return out


def spliced_change(series, flag):
    """Week-on-week change with flagged weeks set to NaN: splice, do not difference."""
    ch = series.diff()
    ch[flag.astype(bool)] = np.nan
    return ch


def intrinsic(spreads_bp, durations, weights=None):
    """Duration-weighted intrinsic spread, bp. Drop defaulted names first."""
    s = np.asarray(spreads_bp, dtype=float)
    dur = np.asarray(durations, dtype=float)
    w = np.ones_like(s) if weights is None else np.asarray(weights, dtype=float)
    if not np.all(np.isfinite(s)) or np.any(dur <= 0):
        raise ValueError("each constituent needs a finite spread and a positive duration")
    return float(np.sum(w * dur * s) / np.sum(w * dur))


def skew(index_bp, spreads_bp, durations, weights=None):
    """Quoted index spread minus intrinsic, bp (negative: index tighter than its names).
    Quotes and constituents must share one snapshot time."""
    return index_bp - intrinsic(spreads_bp, durations, weights)


def series_basis_line(p_new, p_old, notional_mm, long_risk=True):
    """Roll-day line for a price-quoted index, $mm: (P_new - P_old) x N / 100,
    N positive for long risk. A change of instrument, not P&L (Section 8C.2)."""
    sign = 1.0 if long_risk else -1.0
    return sign * (p_new - p_old) * notional_mm / 100.0


if __name__ == "__main__":
    # Section 10B.3 (The DESK, exchange data): ADV and OI in $m.
    adv = pd.Series({("CME", "2026-02"): 522, ("CME", "2026-08"): 253,
                     ("Cboe", "2026-02"): 435, ("Cboe", "2026-08"): 407})
    oi = pd.Series({("CME", "2026-02"): 689, ("CME", "2026-08"): 1610,
                    ("Cboe", "2026-02"): 1990, ("Cboe", "2026-08"): 2170})
    print(turnover(adv, oi).round(2))            # CME 0.76 then 0.16; Cboe 0.22, 0.19
    # Section 10B.6 toy index: intrinsic 147.7 bp; skew -4.7 bp at a quote of 143.
    sp, du = [60, 80, 100, 150, 400], [4.6, 4.5, 4.4, 4.2, 3.6]
    assert abs(intrinsic(sp, du) - 147.70) < 0.01
    print(round(skew(143.0, sp, du), 1))
    # Exercise 5: $13mm long risk, old series 106.10, new 105.20 -> -0.117, named, not P&L.
    print(round(series_basis_line(105.20, 106.10, 13.0), 3))
```


## F.13-B: Chapter 13-B: The Autopsy Room: LMT Docket Diaries {#code-13b}

Listings from `13_ch13b_the_autopsy_room_lmt_docket_diaries.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 13-B.1: docket_diary.py: labelled docket entries to rulings, case paths and transitions {#code-13b-1}

```python
"""docket_diary.py (Chapter 13-B): labelled docket entries -> rulings, case paths,
transition counts, and token log-odds that jump on ruling dates.

Direction: +1 favours excluded or non-consenting holders, -1 the majority or debtor,
0 mixed, None for entries that are not rulings (including settlements).
Jumps are elicited priors on the excluded side's log-odds (illustrative), not estimates.
"""
from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from datetime import date

STATES = ("announced", "challenged", "mtd_denied", "trial", "ruled_pos", "ruled_neg",
          "reversed", "settled", "in_court", "emerged", "coop_close")
ABSORBING = {"coop_close", "emerged"}


@dataclass(frozen=True)
class Entry:
    case: str
    forum: str
    kind: str                          # "ruling", "filing", "scheduling", "settlement", ...
    decided_at: date | None = None
    entered_at: date | None = None
    first_public_at: date | None = None
    direction: int | None = None       # +1, -1, 0, or None
    tokens: tuple[str, ...] = ()
    state_after: str | None = None     # map state this entry moves the case into
    jump: float = 0.0                  # elicited log-odds jump for the excluded side

    def event_date(self) -> date | None:
        """First date the market could know: public, else decided, else entered."""
        return self.first_public_at or self.decided_at or self.entered_at


def rulings(entries):
    """Entries that decide something, in event-date order; scheduling orders excluded."""
    out = [e for e in entries
           if e.kind == "ruling" and e.direction in (-1, 0, 1) and e.event_date()]
    for e in out:
        if e.jump * e.direction < 0:
            raise ValueError(f"{e.case}: jump {e.jump} has the wrong sign for {e.direction}")
    return sorted(out, key=lambda e: e.event_date())


def case_paths(entries):
    """Ordered list of map states per case, from entries that carry state_after."""
    paths: dict[str, list[str]] = {}
    dated = [e for e in entries if e.state_after and e.event_date()]
    for e in sorted(dated, key=lambda e: e.event_date()):
        if e.state_after not in STATES:
            raise ValueError(f"unknown state {e.state_after!r} in {e.case}")
        path = paths.setdefault(e.case, ["announced"])
        if path[-1] != e.state_after:
            path.append(e.state_after)
    return paths


def transition_counts(paths):
    """One-step moves i -> j across cases; nothing may leave an absorbing state."""
    counts = Counter()
    for case, path in paths.items():
        for i, j in zip(path, path[1:]):
            if i in ABSORBING:
                raise ValueError(f"{case}: move out of absorbing state {i}")
            counts[(i, j)] += 1
    return counts


def row_probabilities(counts, state):
    """Empirical one-step probabilities out of one state; None if never left."""
    row = {j: n for (i, j), n in counts.items() if i == state}
    total = sum(row.values())
    return {j: n / total for j, n in row.items()} if total else None


def token_logodds(alpha, token, entries, as_of):
    """Excluded side's log-odds for a wording token on as_of: baseline plus the jumps
    of rulings that read the token and were public on or before as_of."""
    return alpha + sum(e.jump for e in rulings(entries)
                       if token in e.tokens and e.event_date() <= as_of)


def prob(logit):
    return 1.0 / (1.0 + math.exp(-logit))


if __name__ == "__main__":
    serta = [
        Entry("Serta", "Bankr. S.D. Tex.", "ruling", decided_at=date(2023, 3, 28),
              direction=-1, tokens=("open_market_purchase",), jump=-0.5),
        Entry("Serta", "5th Cir.", "ruling", decided_at=date(2024, 12, 31),
              direction=+1, tokens=("open_market_purchase",), jump=+1.0),
        Entry("Serta", "Bankr. S.D. Tex.", "scheduling", entered_at=date(2023, 4, 3)),
    ]
    for d in (date(2023, 1, 1), date(2023, 6, 1), date(2025, 1, 2)):
        x = token_logodds(0.0, "open_market_purchase", serta, d)
        print(d, round(prob(x), 2))    # 0.5, then 0.38, then 0.62
```


## F.17-B: Chapter 17-B: Marking the Unmarked: Private Credit LMEs {#code-17b}

Listings from `17_ch17b_marking_the_unmarked_private_credit_lmes.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 17-B.1: The redemption queue, de-duplicated and nowcast {#code-17b-1}

```python
# pc_queue.py: the redemption queue, de-duplicated and nowcast (Chapter 17-B, §17B.3)
import numpy as np
from scipy import optimize, stats


def paid_share(a, f):
    """Share of shares outstanding repurchased this cycle, p = a * f (decimals)."""
    if not (0.0 <= a <= 1.0 and 0.0 <= f <= 1.0):
        raise ValueError("requests a and fill f must be decimals in [0, 1]")
    return a * f


def split_requests(a_prev, f_prev, a_now, xi=1.0, subs=0.0):
    """Split this cycle's requests into the returning line and new joiners.

    a_prev, f_prev: last cycle's requests and fill (fill as a share of REQUESTS),
                    both as fractions of last cycle's shares.
    a_now: this cycle's requests, as a fraction of this cycle's shares.
    xi: share of last cycle's unfilled requests that come back (1.0 = all of them).
    subs: shares issued between the two offers, as a fraction of last cycle's shares.

    Returns a dict:
      returning  b_t, the resubmitted line, as a fraction of this cycle's shares;
      new_share  a_t - b_t, new requests as a fraction of all shares;
      joiners    (a_t - b_t) / (1 - b_t), Chapter 17's a^new;
      resub      b_t / a_t, the resubmission share a fund letter would report.
    With xi = 1 and subs = 0, joiners is a lower bound and resub an upper bound."""
    if not (0.0 <= xi <= 1.0) or subs < 0.0:
        raise ValueError("xi must be in [0, 1] and subs >= 0")
    p = paid_share(a_prev, f_prev)
    b = xi * (a_prev - p) / (1.0 - p + subs)
    b = min(b, a_now)  # the floor: more returning than requested means xi is too high here
    joiners = (a_now - b) / (1.0 - b) if b < 1.0 else np.nan
    resub = b / a_now if a_now > 0 else np.nan
    return {"returning": b, "new_share": a_now - b, "joiners": joiners, "resub": resub}


def nowcast_requests(a_now, f_now, joiners_lo, joiners_hi, xi=1.0, subs=0.0):
    """Next cycle's requests: the returning line (arithmetic) plus a range of joiners (belief).
    Returns (returning, low, high) as fractions of next cycle's shares."""
    p = paid_share(a_now, f_now)
    b = xi * (a_now - p) / (1.0 - p + subs)
    lo = b + joiners_lo * (1.0 - b)
    hi = b + joiners_hi * (1.0 - b)
    return b, min(lo, 1.0), min(hi, 1.0)


def prorata_quarters(fill, target=0.5):
    """Quarters for a holder who tenders everything every cycle to get `target` of the shares
    out at a constant pro rata fill: the smallest n with 1 - (1 - fill)**n >= target."""
    if not (0.0 < fill <= 1.0) or not (0.0 < target < 1.0):
        raise ValueError("fill must be in (0, 1] and target in (0, 1)")
    if fill == 1.0:
        return 1
    return int(np.ceil(np.log(1.0 - target) / np.log(1.0 - fill)))


def littles_wait(backlog, throughput):
    """Average wait, in quarters, in a first-come-first-served line: W = L / throughput."""
    return np.inf if throughput <= 0 else backlog / throughput


def fit_censored_lognormal(y, censored, x):
    """Maximum likelihood for log(y) = mu0 + mu1 * x + sigma * eps, eps ~ N(0, 1).

    Rows with censored=True are lower bounds (the filing says only that the cap bound)
    and contribute log P(Y >= y), the survival term of Law 14, instead of a density."""
    y = np.asarray(y, float)
    x = np.asarray(x, float)
    c = np.asarray(censored, bool)
    if y.shape != x.shape or y.shape != c.shape:
        raise ValueError("y, censored and x must have the same length")
    if np.any(y <= 0):
        raise ValueError("y must be positive: drop or floor zero rows before fitting")
    ly = np.log(y)

    def nll(theta):
        mu0, mu1, log_s = theta
        z = (ly - mu0 - mu1 * x) / np.exp(log_s)
        ll_obs = stats.norm.logpdf(z[~c]) - log_s - ly[~c]
        ll_cen = stats.norm.logsf(z[c])
        return -(ll_obs.sum() + ll_cen.sum())

    x0 = np.array([ly.mean(), 0.0, np.log(ly.std() + 1e-3)])
    res = optimize.minimize(nll, x0, method="Nelder-Mead",
                            options={"xatol": 1e-6, "fatol": 1e-7, "maxiter": 20000})
    mu0, mu1, log_s = res.x
    return {"mu0": float(mu0), "mu1": float(mu1), "sigma": float(np.exp(log_s)),
            "n": int(y.size), "n_censored": int(c.sum()), "converged": bool(res.success)}


# --- sanity checks: the chapter's numbers (computed; xi = 1, no subscriptions) ---
otic = split_requests(0.404, 0.144, 0.381)
assert abs(otic["new_share"] - 0.0138) < 5e-4 and abs(otic["joiners"] - 0.022) < 1e-3
assert abs(split_requests(0.188, 0.266, 0.168)["joiners"] - 0.027) < 1e-3     # OCIC, Q3
assert abs(split_requests(0.110, 0.452, 0.168)["joiners"] - 0.112) < 1e-3     # ADS, Q2
assert 0.58 < split_requests(0.116, 0.430, 0.114)["resub"] < 0.64             # NHPIF: "nearly two thirds"
assert split_requests(0.20, 0.25, 0.04)["new_share"] == 0.0                     # the floor binds
assert prorata_quarters(0.131, 0.5) == 5 and prorata_quarters(0.131, 0.9) == 17
assert abs(littles_wait(0.35, 0.05) - 7.0) < 1e-12
_, lo, hi = nowcast_requests(0.168, 0.298, 0.05, 0.112)                          # ADS, pending Q3
assert abs(lo - 0.168) < 2e-3 and abs(hi - 0.222) < 2e-3

# --- the censored fit recovers known parameters; the naive fit shrinks them ---
rng = np.random.default_rng(1702)
n = 2000
x = rng.normal(0.0, 1.0, n)
y_true = np.exp(np.log(0.04) + 0.3 * x + 0.5 * rng.normal(0.0, 1.0, n))
cap = 0.08
cens = y_true > cap
y_obs = np.where(cens, cap, y_true)
fit = fit_censored_lognormal(y_obs, cens, x)
naive = fit_censored_lognormal(y_obs, np.zeros(n, bool), x)
assert fit["converged"] and abs(fit["mu1"] - 0.3) < 0.05 and abs(fit["sigma"] - 0.5) < 0.05
assert naive["mu1"] < fit["mu1"] and naive["sigma"] < fit["sigma"]
print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in fit.items()})
```


### Listing 17-B.2: The private-credit LME detector: marks, states, features and a hazard watchlist {#code-17b-2}

```python
# pc_lme_detector.py: a dated watchlist of private-credit LMEs from public filings (Chapter 17-B, §17B.4)
import numpy as np
import pandas as pd

STATES = ["performing", "pik_by_amendment", "non_accrual", "restructured", "re_cut"]
SOI_COLS = ["bdc_id", "qdate", "facility_id", "borrower", "par", "fv", "pik_flag", "industry"]  # §17.8
EXTRA_COLS = ["adviser_id", "nonaccrual_flag"]          # added here: who values it; the holder's own flag
FEATURES = ["disp_level", "shortfall", "sponsor_hit", "dropdown", "pik_cliff", "pik_amend",
            "software", "pending", "holder_joiners", "in_state_1", "in_state_2", "in_state_3"]


def cluster_marks(soi):
    """One par-weighted mark per facility, quarter and valuation process (adviser)."""
    missing = sorted(set(SOI_COLS + EXTRA_COLS) - set(soi.columns))
    if missing:
        raise KeyError(f"soi is missing columns: {missing}")
    g = (soi.groupby(["facility_id", "qdate", "adviser_id"], as_index=False)
            .agg(par=("par", "sum"), fv=("fv", "sum"),
                 na=("nonaccrual_flag", "max"), pik=("pik_flag", "max")))
    g["mark"] = g["fv"] / g["par"]
    return g


def assign_state(f):
    """Most advanced state any public beat supports, carried forward; a second reset is a re-cut.
    0 performing, 1 PIK by amendment, 2 non-accrual at any valuer, 3 restructured, 4 re-cut."""
    f = f.sort_values(["facility_id", "qdate"]).reset_index(drop=True)
    raw = np.zeros(len(f), dtype=int)
    raw = np.where(f["pik_amend"], 1, raw)
    raw = np.where(f["na_share"] > 0, 2, raw)
    raw = np.where(f["restructured"], 3, raw)
    f["state"] = pd.Series(raw, index=f.index).groupby(f["facility_id"]).cummax()
    n_reset = f["restructured"].astype(int).groupby(f["facility_id"]).cumsum()
    f.loc[n_reset >= 2, "state"] = 4
    last_reset = f["qdate"].where(f["restructured"]).groupby(f["facility_id"]).ffill()
    f["q_since_reset"] = ((f["qdate"] - last_reset).dt.days / 91.3).round()   # §14.3's clock
    return f


def facility_features(soi, events=None, window=4):
    """Facility-quarter features. events: facility_id, qdate (the date the fact became PUBLIC),
    sponsor_equity (float or NaN), dropdown (bool), restructured (bool)."""
    cm = cluster_marks(soi)
    f = (cm.groupby(["facility_id", "qdate"])
           .agg(n_valuers=("mark", "size"), mark_min=("mark", "min"), mark_max=("mark", "max"),
                fv=("fv", "sum"), par=("par", "sum"), na_share=("na", "mean"), pik_now=("pik", "max"))
           .reset_index().sort_values(["facility_id", "qdate"]).reset_index(drop=True))
    f["mark_pw"] = f["fv"] / f["par"]
    f["dispersion"] = np.where(f["n_valuers"] >= 2, f["mark_max"] - f["mark_min"], np.nan)
    f["disp_level"] = (f.groupby("facility_id")["dispersion"]
                         .transform(lambda s: s.rolling(window, min_periods=1).max()))
    prev_pik = f.groupby("facility_id")["pik_now"].shift(1)
    f["pik_amend"] = f["pik_now"].astype(bool) & (prev_pik == False)   # noqa: E712, PIK appears
    f["pik_cliff"] = ~f["pik_now"].astype(bool) & (prev_pik == True)   # noqa: E712, PIK lapses
    sw = soi.groupby("facility_id")["industry"].first().eq("software")
    f["software"] = f["facility_id"].map(sw).astype(float)
    if events is not None:
        f = f.merge(events, on=["facility_id", "qdate"], how="left")
    for col, default in [("sponsor_equity", np.nan), ("dropdown", False), ("restructured", False)]:
        if col not in f.columns:
            f[col] = default
    f["dropdown"] = f["dropdown"].fillna(False).astype(bool)
    f["restructured"] = f["restructured"].fillna(False).astype(bool)
    prev_eq = f.groupby("facility_id")["sponsor_equity"].ffill().groupby(f["facility_id"]).shift(1)
    f["sponsor_hit"] = (f["sponsor_equity"] <= 0) | (f["sponsor_equity"] <= 0.5 * prev_eq)
    return assign_state(f)


def design(f):
    """Feature matrix; optional inputs (pending = Pi of §17.8.3, holder_joiners = a^new) enter as 0."""
    X = pd.DataFrame(index=f.index)
    X["disp_level"] = f["disp_level"].fillna(0.0)
    X["shortfall"] = (1.0 - f["mark_min"]).clip(lower=0.0)
    for c in ["sponsor_hit", "dropdown", "pik_cliff", "pik_amend", "software"]:
        X[c] = f[c].astype(float) if c in f.columns else 0.0
    X["pending"] = (-f["pending"]).clip(lower=0.0).fillna(0.0) if "pending" in f.columns else 0.0
    X["holder_joiners"] = f["holder_joiners"].fillna(0.0) if "holder_joiners" in f.columns else 0.0
    for k in (1, 2, 3):
        X[f"in_state_{k}"] = (f["state"] == k).astype(float)
    return X[FEATURES]


def advance_label(f):
    """1.0 if the facility sits on a later square next quarter; the mask is False on the last quarter."""
    nxt = f.groupby("facility_id")["state"].shift(-1)
    return (nxt > f["state"]).astype(float), nxt.notna()


def fit_hazard(X, y, ridge=1.0, iters=100):
    """Ridge logistic regression by Newton steps on standardized columns (the ridge is the prior)."""
    Xv = X.to_numpy(float)
    yv = np.asarray(y, float)
    mu, sd = Xv.mean(axis=0), Xv.std(axis=0)
    sd = np.where(sd > 0, sd, 1.0)
    Z = np.column_stack([np.ones(len(Xv)), (Xv - mu) / sd])
    w = np.zeros(Z.shape[1])
    P = ridge * np.eye(Z.shape[1])
    P[0, 0] = 0.0
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-np.clip(Z @ w, -30, 30)))
        grad = Z.T @ (yv - p) - P @ w
        H = (Z * (p * (1.0 - p))[:, None]).T @ Z + P
        step = np.linalg.solve(H, grad)
        w = w + step
        if np.max(np.abs(step)) < 1e-9:
            break
    return {"w": w, "mu": mu, "sd": sd, "cols": list(X.columns)}


def score(model, X):
    Z = (X[model["cols"]].to_numpy(float) - model["mu"]) / model["sd"]
    eta = model["w"][0] + Z @ model["w"][1:]
    return 1.0 / (1.0 + np.exp(-np.clip(eta, -30, 30)))


def watchlist(f, model, asof, top=25):
    """The dated list: facilities ranked by score, each with its beat (largest contribution).
    A ranking, not a probability. Print n_valuers beside every row."""
    cur = f[f["qdate"] == pd.Timestamp(asof)].copy()
    if cur.empty:
        return cur
    X = design(cur)
    contrib = ((X[model["cols"]].to_numpy(float) - model["mu"]) / model["sd"]) * model["w"][1:]
    cur["score"] = score(model, X)
    cur["beat"] = np.array(model["cols"])[contrib.argmax(axis=1)]
    cur["asof"] = pd.Timestamp(asof)
    cols = ["asof", "facility_id", "state", "score", "beat", "disp_level", "mark_min", "n_valuers"]
    return cur.sort_values("score", ascending=False)[cols].head(top).reset_index(drop=True)


# --- check 1: Medallia, 30 June 2026 (marks from the seven 10-Qs; par set to 100 each, illustrative) ---
med = pd.DataFrame({
    "bdc_id": ["BCRED", "BXSL", "HLEND", "ADS", "FSK", "ONEX", "MONROE"],
    "adviser_id": ["BX", "BX", "HPS", "APOLLO", "FSKKR", "ONEX", "MONROE"],
    "fv": [49.5, 49.5, 49.2, 40.7, 50.1, 39.0, 41.3],
    "nonaccrual_flag": [True, True, False, False, False, False, False],  # only the flags parsed here
})
med = med.assign(qdate=pd.Timestamp("2026-06-30"), facility_id="MEDALLIA_TL", borrower="Medallia",
                 par=100.0, pik_flag=False, industry="software")
fm = facility_features(med)
assert fm["n_valuers"].iloc[0] == 6                         # two Blackstone rows, one opinion
assert abs(fm["dispersion"].iloc[0] - 0.111) < 1e-9 and fm["state"].iloc[0] == 2

# --- check 2: the five squares and the re-default clock on a toy facility ---
toy = pd.DataFrame({
    "facility_id": "X",
    "qdate": pd.to_datetime(["2023-12-31", "2024-03-31", "2024-06-30", "2024-09-30",
                             "2025-06-30", "2025-12-31", "2026-03-31"]),
    "pik_amend": [False, True, False, False, False, False, False],
    "na_share": [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0],
    "restructured": [False, False, False, True, False, False, True],
})
st = assign_state(toy)
assert st["state"].tolist() == [0, 1, 2, 3, 3, 3, 4]
assert st["q_since_reset"].tolist()[4:6] == [3.0, 5.0]
assert advance_label(st)[0].tolist()[:3] == [1.0, 1.0, 1.0]

# --- check 3: a seeded panel; a Pluralsight-shaped row outranks a Zayo-shaped one ---
rng = np.random.default_rng(1717)
n = 4000
sim = pd.DataFrame({
    "disp_level": rng.gamma(2.0, 0.02, n),
    "mark_min": np.clip(1.0 - rng.gamma(2.0, 0.03, n), 0.3, 1.0),
    "sponsor_hit": rng.random(n) < 0.03, "dropdown": rng.random(n) < 0.01,
    "pik_cliff": rng.random(n) < 0.02, "pik_amend": rng.random(n) < 0.05,
    "software": (rng.random(n) < 0.2).astype(float), "state": 0,
})
eta = (-4.0 + 25.0 * sim["disp_level"] + 5.0 * (1.0 - sim["mark_min"]) + 3.0 * sim["sponsor_hit"]
       + 2.0 * sim["dropdown"] + 1.5 * sim["pik_cliff"])
y = rng.random(n) < 1.0 / (1.0 + np.exp(-eta))
model = fit_hazard(design(sim), y)
w = dict(zip(model["cols"], model["w"][1:]))
assert w["disp_level"] > 0 and w["sponsor_hit"] > 0
probe = pd.DataFrame({"disp_level": [0.136, 0.01], "mark_min": [0.834, 0.95],
                      "sponsor_hit": [True, False], "dropdown": [False, False],
                      "pik_cliff": [False, False], "pik_amend": [False, False],
                      "software": [1.0, 0.0], "state": [0, 0]})
s = score(model, design(probe))
assert s[0] > 5 * s[1]
wl = watchlist(fm, model, "2026-06-30")
assert len(wl) == 1 and wl.loc[0, "beat"] in FEATURES
print(wl)
```


## F.18-B: Chapter 18-B: The RFQ Response Engine {#code-18b}

Listings from `18_ch18b_the_rfq_response_engine.md`, in the order they appear in the chapter. Blocks within a chapter are written to run cumulatively in one interpreter.


### Listing 18-B.1: rfq_engine.py: the RFQ response engine in six small pieces {#code-18b-1}

```python
"""rfq_engine.py (Chapter 18-B): the RFQ response engine in six small pieces.

Units: quote distances x in points from the composite, positive when worse for the client;
sizes z and inventory q in $mm; rates in RFQs per day. Win curve as in Section 18.7:
P(x) = 1 / (1 + exp(-(b0 - b1 x))). Every parameter in the demos is illustrative.
"""
import math
import numpy as np


def win_prob(x, b0, b1):
    return 1.0 / (1.0 + np.exp(-(b0 - b1 * np.asarray(x, dtype=float))))


def lambert_w0(z, tol=1e-14):
    """Principal branch of Lambert W on z >= 0, by Halley's iteration."""
    if z < 0:
        raise ValueError("only z >= 0 is needed here")
    w = math.log1p(z)
    for _ in range(60):
        ew = math.exp(w)
        g = w * ew - z
        step = g / (ew * (w + 1.0) - (w + 2.0) * g / (2.0 * w + 2.0))
        w -= step
        if abs(step) < tol * (1.0 + abs(w)):
            break
    return w


def quote_from_p(p, b0, b1):
    """Optimal distance for total effective cost p: x* = p + (1 + W0(exp(b0 - b1 p - 1))) / b1."""
    return p + (1.0 + lambert_w0(math.exp(b0 - b1 * p - 1.0))) / b1


def h_second(p, rate, b0, b1, eps=1e-4):
    """H''(p) by central difference of H'(p) = -rate * P(x*(p)) (envelope theorem)."""
    hp = lambda u: -rate * float(win_prob(quote_from_p(u, b0, b1), b0, b1))
    return (hp(p + eps) - hp(p - eps)) / (2.0 * eps)


def effective_dealers(n, phi):
    """Section 2.3.2 and Listing E.1: n / (1 + (n - 1) phi)."""
    if n < 1 or not 0.0 <= phi <= 1.0:
        raise ValueError("need n >= 1 and 0 <= phi <= 1")
    return n / (1.0 + (n - 1.0) * phi)


# ---------------------------------------------------------------- 1. who answers, together
def fit_response_corr(answers, asked, grid=None):
    """Beta-binomial fit: answers[i] of asked[i] invited dealers responded to RFQ i. The answer
    rate is held at its pooled value; phi_ans = 1/(a+b+1) is chosen by likelihood on a grid."""
    k, n = np.asarray(answers, dtype=int), np.asarray(asked, dtype=int)
    if k.shape != n.shape or k.size == 0 or np.any(k < 0) or np.any(k > n):
        raise ValueError("need 0 <= answers <= asked, same shape, non-empty")
    p = k.sum() / n.sum()
    if not 0.0 < p < 1.0:
        raise ValueError("all or none answered: the correlation is not identified")
    pairs, counts = np.unique(np.stack([k, n], axis=1), axis=0, return_counts=True)
    best_ll, best_rho = -math.inf, None
    for rho in (np.linspace(0.005, 0.6, 120) if grid is None else grid):
        s = 1.0 / rho - 1.0
        a, b = p * s, (1.0 - p) * s
        ll = sum(c * (math.lgamma(kk + a) + math.lgamma(nn - kk + b) - math.lgamma(nn + s)
                      + math.lgamma(s) - math.lgamma(a) - math.lgamma(b))
                 for (kk, nn), c in zip(pairs, counts))
        if ll > best_ll:
            best_ll, best_rho = ll, float(rho)
    return {"p": float(p), "phi_ans": best_rho,
            "n_eff_invitees": effective_dealers(float(np.median(n)), best_rho)}


# ---------------------------------------------------------------- 2. the whole log, not the blotter
DONE, COVERED, TRADED_AWAY, NOT_TRADED = "done", "covered", "traded_away", "not_traded"


def _trap(y, x):
    return float(np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2.0)


def cover_loglik(theta, records, p_ans, res_scale, m=200):
    """Log-likelihood of every outcome when each of n rivals answers with probability p_ans at a
    distance ~ Exponential(mean theta) and the client accepts any quote within an
    Exponential(mean res_scale) reservation distance. records: dicts with outcome, n (rivals),
    y (our distance) and, on DONE, cover (best rival distance, or None if no rival answered)."""
    S = lambda x: 1.0 - p_ans * (1.0 - np.exp(-x / theta))      # rival above x, or silent
    f = lambda x: np.exp(-x / theta) / theta
    G = lambda x: np.exp(-x / res_scale)                        # client accepts distance x
    groups = {}
    for r in records:
        groups.setdefault((r["n"], r["y"]), []).append(r)
    ll = 0.0
    for (n, y), rows in groups.items():
        xs = np.linspace(0.0, y, m + 1)
        best = n * p_ans * f(xs) * S(xs) ** (n - 1)             # density of the best rival below y
        p_cov = n * _trap(p_ans * f(xs) * G(xs), xs) * S(y) ** (n - 1)
        probs = {COVERED: p_cov, TRADED_AWAY: _trap(best * G(xs), xs) - p_cov,
                 NOT_TRADED: S(y) ** n * (1.0 - G(y)) + _trap(best * (1.0 - G(xs)), xs)}
        for r in rows:
            if r["outcome"] in probs:
                if probs[r["outcome"]] <= 0.0:
                    return -math.inf
                ll += math.log(probs[r["outcome"]])
            elif r["cover"] is None:                            # DONE and nobody else answered
                ll += n * math.log(1.0 - p_ans) - y / res_scale if p_ans < 1.0 else -math.inf
            else:                                               # DONE with the cover revealed
                c = r["cover"]
                ll += (math.log(n * p_ans / theta) - c / theta
                       + (n - 1) * math.log(S(c)) - y / res_scale)
    return ll


def fit_rival_scale(records, p_ans, res_scale, grid=None):
    grid = np.linspace(0.3, 3.0, 136) if grid is None else np.asarray(grid)
    return float(grid[int(np.argmax([cover_loglik(t, records, p_ans, res_scale) for t in grid]))])


def simulate_log(m, theta, p_ans, res_scale, rng, ns=(2, 4), ys=(0.3, 0.5, 0.7)):
    """A synthetic RFQ log, plus the best rival quote on every row, which no desk ever sees."""
    recs, truth = [], []
    for _ in range(m):
        n, y = int(rng.choice(ns)), float(rng.choice(ys))
        rivals = rng.exponential(theta, size=n)[rng.random(n) < p_ans]
        best = float(rivals.min()) if rivals.size else math.inf
        reserve = rng.exponential(res_scale)
        if y < best:
            out = DONE if reserve >= y else NOT_TRADED
        elif reserve >= best:
            out = COVERED if int(np.sum(rivals < y)) == 1 else TRADED_AWAY
        else:
            out = NOT_TRADED
        cover = best if out == DONE and math.isfinite(best) else None
        recs.append({"outcome": out, "n": n, "y": y, "cover": cover})
        truth.append(best)
    return recs, np.array(truth)


# ---------------------------------------------------------------- 3. the target is a price
def curvature(tiers, sigma2, phi_sigma):
    """Stationary one-bond Riccati: A = sqrt(phi_sigma * sigma2 / K), with K the sum over tiers
    and both sides of z * H''(0). Points of reservation-price move per $mm of inventory."""
    k = 2.0 * sum(t["z"] * h_second(0.0, t["rate"], t["b0"], t["b1"]) for t in tiers)
    if k <= 0 or sigma2 <= 0 or phi_sigma <= 0:
        raise ValueError("need positive liquidity, variance and risk aversion")
    return math.sqrt(phi_sigma * sigma2 / k)


def tier_hit_ratio(tier, a_curv, q, shift):
    """Two-sided win probability at inventory q, with costs A(+-q + z/2) lowered by shift."""
    hits = [float(win_prob(quote_from_p(a_curv * (s * q + tier["z"] / 2.0) - shift,
                                        tier["b0"], tier["b1"]), tier["b0"], tier["b1"]))
            for s in (1.0, -1.0)]
    return 0.5 * sum(hits)


def tier_dual(tiers, target, r_star, sigma2, phi_sigma, q=0.0, hi=5.0):
    """Price of a hard hit-ratio target for one tier at inventory q: the smallest shift >= 0
    that reaches r_star, and zero when the target is slack. Returns (A, shift)."""
    a_curv = curvature(tiers, sigma2, phi_sigma)
    tier = next(t for t in tiers if t["name"] == target)
    ratio = lambda s: tier_hit_ratio(tier, a_curv, q, s)
    if ratio(0.0) >= r_star:
        return a_curv, 0.0
    if ratio(hi) < r_star:
        raise ValueError("target unreachable inside the search band")
    lo = 0.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if ratio(mid) < r_star else (lo, mid)
    return a_curv, hi


# ---------------------------------------------------------------- 4. three terms to five
def quote_decompose(tier, side, a_curv, q, alpha=0.0, nu=0.0, eta=5.0, targeted=False):
    """Niang's five terms for one RFQ, priced cumulatively so that they add up to the quote.
    side 'bid' (client sells to us) or 'offer'; alpha > 0 means the desk thinks the bond is cheap."""
    if side not in ("bid", "offer"):
        raise ValueError("side is 'bid' or 'offer'")
    sgn = 1.0 if side == "bid" else -1.0
    inv = a_curv * (sgn * q + tier["z"] / 2.0)
    view = -sgn * alpha
    sub = math.exp(-eta * tier["chi"]) * nu if targeted else 0.0
    steps = [0.0, inv, inv + view, inv + view + tier["chi"], inv + view + tier["chi"] - sub]
    xs = [quote_from_p(p, tier["b0"], tier["b1"]) for p in steps]
    names = ("riskless", "inventory", "credit_alpha", "toxicity", "subsidy")
    out = {"riskless": xs[0]}
    out.update({names[i]: xs[i] - xs[i - 1] for i in range(1, 5)})
    out["quote"], out["win_prob"] = xs[4], float(win_prob(xs[4], tier["b0"], tier["b1"]))
    return out


# ---------------------------------------------------------------- 5. the stress switch
def stress_switch(observed, expected, sd, enter=2.0, leave=1.0, persist=2):
    """Switch on the residual of response counts against their expected level for that tier and
    hour: on after `persist` z-scores below -enter, off after `persist` above -leave."""
    obs, exp_, s = (np.asarray(v, dtype=float) for v in (observed, expected, sd))
    if np.any(s <= 0):
        raise ValueError("sd must be positive")
    z = (obs - exp_) / s
    state, run, out = False, 0, []
    for zi in z:
        crossing = (zi < -enter) if not state else (zi > -leave)
        run = run + 1 if crossing else 0
        if run >= persist:
            state, run = not state, 0
        out.append(state)
    return out, z


# ---------------------------------------------------------------- 6. the quoting game
def play(book, account, r_star, mode, eta=5.0, hi=3.0):
    """Tiers named in `account` share a size-weighted hit-ratio target. 'raw' charges each the
    account-average toxicity and pays all the same nu; 'residual' charges each its own chi and
    pays exp(-eta chi) * nu against a quality-weighted ratio. Expected values only."""
    acct = [t for t in book if t["name"] in account]
    if mode == "raw":
        chi_bar = sum(t["rate"] * t["chi"] for t in acct) / sum(t["rate"] for t in acct)
        cost, wts = (lambda t, nu: chi_bar - nu), [1.0] * len(acct)
    elif mode == "residual":
        cost = lambda t, nu: t["chi"] - math.exp(-eta * t["chi"]) * nu
        wts = [math.exp(-eta * t["chi"]) for t in acct]
    else:
        raise ValueError("mode is 'raw' or 'residual'")
    hit = lambda t, p: float(win_prob(quote_from_p(p, t["b0"], t["b1"]), t["b0"], t["b1"]))
    ratio = lambda nu: (sum(w * t["rate"] * t["z"] * hit(t, cost(t, nu)) for t, w in zip(acct, wts))
                        / sum(w * t["rate"] * t["z"] for t, w in zip(acct, wts)))
    nu = 0.0
    if ratio(0.0) < r_star:
        if ratio(hi) < r_star:
            raise ValueError("target unreachable inside the search band")
        lo = 0.0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if ratio(mid) < r_star else (lo, mid)
        nu = hi
    out = {"nu": nu}
    for t in book:
        p = cost(t, nu) if t in acct else t["chi"]
        x = quote_from_p(p, t["b0"], t["b1"])
        h = float(win_prob(x, t["b0"], t["b1"]))
        out[t["name"]] = {"hit": h, "pnl": t["rate"] * t["z"] * h * (x - t["chi"])}
    return out


BOOK = [
    {"name": "index",     "rate": 40.0, "z": 1.0, "b0": 0.0, "b1": 4.0, "chi": 0.00},
    {"name": "asset_mgr", "rate": 30.0, "z": 1.0, "b0": 0.0, "b1": 4.0, "chi": 0.05},
    {"name": "event_pod", "rate": 10.0, "z": 2.0, "b0": 1.5, "b1": 4.0, "chi": 0.80},
]

if __name__ == "__main__":
    rng = np.random.default_rng(18)
    # 1. dealers answer together: Beta(1, 3) appetite, mean 0.25, phi_ans = 1/(1+3+1) = 0.2
    answers = rng.binomial(27, rng.beta(1.0, 3.0, size=3000))
    fit = fit_response_corr(answers, np.full(3000, 27))
    assert abs(fit["phi_ans"] - 0.20) < 0.06 and 3.0 < fit["n_eff_invitees"] < 7.0
    assert np.mean(answers == 0) > 50 * (1.0 - fit["p"]) ** 27
    # 2. the whole log recovers the rivals; the wins alone flatter them
    log, best_rival = simulate_log(6000, 1.0, 0.5, 1.5, rng)
    assert abs(fit_rival_scale(log, 0.5, 1.5) - 1.0) < 0.15
    covers = [r["cover"] for r in log if r["cover"] is not None]
    assert np.mean(covers) > 1.3 * np.mean(best_rival[np.isfinite(best_rival)])
    # 3. a steeper bowl makes the target dearer; background flow makes it cheaper
    a1, nu1 = tier_dual(BOOK, "asset_mgr", 0.25, sigma2=0.25, phi_sigma=1.0)
    a2, nu2 = tier_dual(BOOK, "asset_mgr", 0.25, sigma2=1.00, phi_sigma=1.0)
    _, nu3 = tier_dual(BOOK[1:], "asset_mgr", 0.25, sigma2=1.00, phi_sigma=1.0)
    assert a2 > a1 and nu2 > nu1 and nu3 > nu2
    # 4. five terms that add up, with the subsidy only where it is paid
    parts = ("riskless", "inventory", "credit_alpha", "toxicity", "subsidy")
    for t in BOOK:
        d = quote_decompose(t, "bid", a1, q=5.0, nu=nu1, targeted=(t["name"] == "asset_mgr"))
        assert abs(sum(d[k] for k in parts) - d["quote"]) < 1e-9
        assert (d["subsidy"] < 0) == (t["name"] == "asset_mgr")
    # 5. the afternoon is not a stress event
    expected = np.array([12.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0])
    calm, _ = stress_switch(expected, expected, np.ones(8))
    assert any(e < 7 for e in expected) and not any(calm)
    stressed = expected.copy()
    stressed[2:6] /= 2.0
    on, _ = stress_switch(stressed, expected, np.ones(8))
    assert on[3] and on[5] and not on[7]
    # 6. the game: raw targeting buys the toxic tier; residual targeting keeps the money
    acct = ("asset_mgr", "event_pod")
    total = lambda g: sum(g[t["name"]]["pnl"] for t in BOOK)
    for r_star in (0.15, 0.20, 0.25):
        raw, res = play(BOOK, acct, r_star, "raw"), play(BOOK, acct, r_star, "residual")
        assert total(res) > total(raw) and raw["event_pod"]["pnl"] < 0
    assert raw["event_pod"]["hit"] > 4 * res["event_pod"]["hit"]
    assert res["asset_mgr"]["hit"] > raw["asset_mgr"]["hit"]
    print("rfq_engine: all checks pass")
```


<!-- STATUS: COMPLETE -->
