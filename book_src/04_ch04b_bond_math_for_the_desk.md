# Chapter 4-B: Bond Math for the Desk: Price, Yield, Duration, Convexity, Spread Measures and the Callable Bond

> *"The OAS represents the increase in the spot curve that is necessary for the model price to equal the traded price."* (Veronesi_Fixed_Income_Securities p.467)

## Cold Open: Six Columns Called "Spread"

*Tuesday, 6:55 p.m.* The backtest had one job: replay the Chapter 1 fallen angel through March 2020 and ask whether a desk that absorbed the index sellers would have been paid for it (§1.8.2). Kaz had loaded the history. Theo opened the file and found six columns with "spread" in the name.

On 23 March 2020 they read, left to right: `g_spd 824`, `z_spd 804`, `asw_par 679`, `asw_mm 959`, `oas 804`, `cds_equiv 945`. (The bond is a stylized ten-year 4.50% note of a BBB− auto issuer, held at constant maturity; the Treasury yields are real, the bond's yields are illustrative, and every number in this chapter is reproduced by the code in §4B.9.)

"Which one is the spread?" Theo asked.

"All of them," said Kaz. "Same bond, six coats."

"They differ by 280 basis points. In my old job, 280 basis points was a covenant reset and two weeks of lawyers."

Mags, from the next desk, without looking up: "In 1994 there was one spread. It was whatever the man on the phone said, minus whatever he thought you knew."

Ines came over with her coffee and read the row the way she reads a hand history. "Wrong question. Ask which one is the pot. Which of these numbers did money actually move on that day, and which ones are just the way somebody chose to count?"

ROBO had been asked the week before to "add the spread to the feature set." It had added all six, and reported, accurately, that they were highly correlated.

Theo scrolled to the duration column: 8.11 on 20 February, 7.40 on 23 March. "The bond got *less* risky? It lost thirty-eight points."

"Per basis point," said Kaz. "Per basis point it got less risky. There were just a lot more basis points."

That exchange is this chapter. Every later chapter quotes a duration, a convexity, a DV01 or one of the six spreads, and none of them stops to build the thing. This chapter builds all of them once, from one price and one curve, and then reprices the fallen angel in every measure to sort the numbers that moved from the numbers that were conventions.

**By the end of this chapter you will be able to** write down the price–yield function of a fixed-rate bond from its indenture; compute clean and dirty prices and accrued interest on the right day count; derive Macaulay, modified, effective, spread and key-rate duration and know which one a hedge needs; separate the three things "convexity" means on this desk; produce DV01, CS01 and DTS and size a Treasury hedge; compute G, I, Z, asset-swap, discount-margin and par-CDS-equivalent spreads from one curve; price a callable bond on a calibrated lattice so that OAS, yield-to-worst and the make-whole are computed rather than named; and ship `bondmath.py`, which Chapters 5, 8, 9, 10, 12, 15 and 19 import.

> **Prerequisites.** Calculus to second order (Taylor's theorem), continuous discounting $e^{-rt}$, and what a coupon is. Nothing else. The hazard-rate bond price in §4B.6 borrows one formula from §6.6.3 and says so; the lattice in §4B.7 is self-contained. A reader who already prices callables on a calibrated tree can skip to the case in §4B.8 and the code in §4B.9. Later chapters cite this one as §4B.N.

**Notation added in this chapter.** $c$ is the annual coupon rate (decimal), $f$ the number of coupons per year, $N$ the number of remaining coupons, $w \in (0,1]$ the fraction of the current coupon period still to run, and $\text{AI}$ accrued interest per 100 of face. The discount factor is $d(t)$, in lower case so it cannot be confused with duration $D$; the continuously compounded zero rate is $z(t)$, also lower case, because upper-case $Z$ is the Z-spread. Convexities carry the same decorations as durations: $C^{\text{mod}}$ (to yield), $C^{\text{spr}}$ (to spread), $C^{\text{eff}}$ (to a curve shift, by repricing). The issuer's call value in §5.2.2 keeps $C^{\text{call}}$ and the call price keeps $K_{\text{call}}$, so no convexity is ever undecorated. $A$ is an asset-swap spread and $\text{DM}$ a discount margin. These join App A §A.3.

## 4B.1 A Bond Is a List: Cash Flows, Day Counts, Clean and Dirty

The RSSG reader already knows the most important fact in this chapter, because it is in Section 2 of every indenture: *interest will be payable semi-annually in arrears on February 15 and August 15 of each year, and will be computed on the basis of a 360-day year comprised of twelve 30-day months.* That sentence is a payment schedule and a day count. Everything else is arithmetic on a list.

"But what does the indenture say?" is, for once, the quant's question too.

### The list

A fixed-rate bullet with face 100, annual coupon rate $c$ and $f$ coupons a year pays $N$ remaining cash flows at dates $t_1 < t_2 < \dots < t_N$:

$$
\text{CF}_k = \frac{100\,c}{f}\quad (k < N), \qquad \text{CF}_N = \frac{100\,c}{f} + 100 .
$$

A US corporate has $f = 2$. Each coupon is the same size whatever the calendar says, because 30/360 makes every half-year exactly 180 days. That is the whole point of the convention: it was designed so that a clerk with a pencil could compute a coupon, and it survives because a court can still check one.

### Day counts

A day count converts two dates into a year fraction. Let $d_1 = (Y_1, M_1, D_1)$ and $d_2 = (Y_2, M_2, D_2)$. The four the book uses:

$$
\tau_{30/360}(d_1,d_2) = \frac{360\,(Y_2 - Y_1) + 30\,(M_2 - M_1) + (D_2' - D_1')}{360},
$$

with $D_1' = \min(D_1, 30)$ and $D_2' = 30$ if $D_2 = 31$ and $D_1' = 30$, else $D_2' = D_2$ (the "bond basis"; the SIFMA variant adds end-of-February rules that matter for about one trade in a thousand and for every audit). Then $\tau_{\text{ACT}/360} = (\text{days})/360$ for loans, CDS and repo, $\tau_{\text{ACT}/365\text{F}} = (\text{days})/365$ for curve time in this chapter's code, and ACT/ACT (ICMA) for Treasuries, where the accrued fraction is actual days elapsed over actual days in the coupon period. App A §A.4 maps instruments to bases.

### Clean, dirty, accrued

The buyer of a bond between coupon dates pays the seller for the coupon the seller has earned and will not receive. That payment is accrued interest. Under 30/360, with $t_{\text{prev}}$ the last coupon date and $t_{\text{set}}$ settlement,

$$
\text{AI} = 100\,c\,\tau_{30/360}(t_{\text{prev}}, t_{\text{set}}), \qquad P^{\text{dirty}} = P^{\text{clean}} + \text{AI}.
$$

Bonds are quoted clean and settle dirty (App A §A.5). Worked example: the fallen angel's dated twin, a 4.50% note due 15 February 2030, traded on 23 March 2020 and settled T+2 on 25 March 2020 (US corporates moved to T+1 on 28 May 2024). From 15 February to 25 March is $30 \cdot 1 + (25 - 15) = 40$ days of 30/360, so $\text{AI} = 100 \times 0.045 \times 40/360 = 0.50$. A buyer of \$10mm at 70.73 clean wires \$7,073,000 of price plus \$50,000 of accrued. Accrued counts to the *settlement* date, which is why the T+1 move changed the accrued on every trade in the market by one day's coupon without changing a single price.

Why quote clean? Because the dirty price is a sawtooth. It rises linearly by $100c/f$ over each period and drops by the coupon on the payment date. Quote dirty and every bond in the index would crash twice a year on a published schedule, and somebody would build a factor on it. (It happens: a return computed from dirty prices without adding back the coupon shows exactly that crash, and Chapter 9-B's return-construction rules exist partly to catch it.) Bonds in default trade *flat*: no accrued is added, and whatever claim to unpaid interest the holder has is inside the price (App A §A.5).

> **Ways This Blows Up.** A 30/360 function that forgets the "31st" rule is wrong by one day on every trade that starts or ends on the 31st. On \$10mm of a 4.50% bond one day of accrued is \$1,250. ROBO will not notice. The client's back office will, on the first trade of the month, and will send you a break for each one.

*Used in:* §15.2 (the change-of-control put at 101 plus accrued), §21.1 (ACT/360 loan interest), §24.2–§24.3 (CDS premium accrual and `bond_cashflows`), §24.5 (accrued at default and the deliverable), App A §A.4–§A.5, App D (settlement cycles).

## 4B.2 The Price–Yield Function

Desk framing. A yield is a price written in a different font. It is the single discount rate that, applied to every cash flow on the list, reproduces the dirty price. Its virtue is that it lets you compare a 4.50% ten-year with a 7.25% six-year in one number. Its vice is that the number contains two assumptions nobody says aloud: every coupon is paid, and every coupon is reinvested at the same yield. For an investment-grade bond those are close enough. For a bond at 60 they are fiction, and the yield is a promise, not a forecast.

### The street formula

With $w$ the fraction of the current period still to run (on the bond's own day count), the street price–yield function with periodic compounding at frequency $f$ is

$$
P^{\text{dirty}}(y) = \sum_{k=1}^{N} \frac{\text{CF}_k}{\left(1 + y/f\right)^{k - 1 + w}} .
$$

On a coupon date $w = 1$ and the exponent is simply $k$. Write $v = (1 + y/f)^{-1}$ and $i = y/f$. The coupons form a geometric series, $\sum_{k=1}^{N} v^k = v\,(1 - v^N)/(1 - v) = (1 - v^N)/i$, so

$$
P(y) = \frac{100\,c}{y}\left[1 - \left(1 + \frac{y}{f}\right)^{-N}\right] + 100\left(1 + \frac{y}{f}\right)^{-N}.
$$

Rearranging gives the identity that every bond trader carries in their head without knowing it is an identity:

$$
P(y) - 100 = 100\,(c - y)\,a_N(y), \qquad a_N(y) = \frac{1 - (1 + y/f)^{-N}}{y} .
$$

A bond's premium is the present value of the coupon it overpays, and its discount is the present value of the coupon it underpays. The factor $a_N(y)$ is an annuity in years: the present value of receiving one unit a year, paid $f$ times a year, for the bond's remaining life. At par, $c = y$ and $P = 100$. That is the definition of a par yield, and it is the first unit test in §4B.9.

### Properties, with proofs

Differentiate term by term. Every cash flow is positive and every exponent $e_k = k - 1 + w$ is positive, so

$$
\frac{dP}{dy} = -\frac{1}{f}\sum_{k} e_k\,\text{CF}_k\left(1 + \frac{y}{f}\right)^{-e_k - 1} < 0, \qquad
\frac{d^2P}{dy^2} = \frac{1}{f^2}\sum_{k} e_k(e_k+1)\,\text{CF}_k\left(1 + \frac{y}{f}\right)^{-e_k - 2} > 0 .
$$

Price is strictly decreasing and strictly convex in yield. Two consequences follow. First, the yield is *unique*: a strictly monotone function crosses any price level once, so a bracketing solver cannot find the wrong root and cannot fail if the price lies between $P(\infty) = 0$ and $P(y_{\min})$. Second, the boundary cases are clean and make good tests: as $y \to 0$, $P \to 100\,(1 + cN/f)$, the undiscounted sum of the list; as $y \to \infty$, $P \to 0$. For a zero-coupon bond, $P = 100\,(1+y/f)^{-fT}$ and every result below should collapse to something you can do in your head.

### Continuous compounding, and the first convention

The book's formulas use continuous compounding unless they say otherwise (App A §A.5). Write $y^{\text{cc}}$ for the continuously compounded yield. Then

$$
P(y^{\text{cc}}) = \sum_k \text{CF}_k\, e^{-y^{\text{cc}} t_k}, \qquad y^{\text{cc}} = f \ln\!\left(1 + \frac{y}{f}\right).
$$

The two yields describe the same price. They are not the same number, and the gap grows with the level: at a 3.50% semi-annual yield, $y^{\text{cc}} = 3.47\%$; at 9.00%, $y^{\text{cc}} = 8.80\%$. Twenty basis points of "spread" at the trough of March 2020 are a choice of compounding, which is why two of the six columns in the cold open differ by almost exactly that. Label every number (Law 11).

### What a yield is not

Yield to maturity is not an expected return. It assumes the list is paid in full. Under the risk-neutral measure $\mathbb{Q}$, with a default intensity $\lambda$ and recovery of face $R$, the price is a survival-weighted list plus a recovery leg (built in §6.6.3, used in §4B.6):

$$
P = \sum_k \text{CF}_k\, d(t_k)\, S(t_k) + 100\,R\int_0^{t_N} \lambda(u)\,S(u)\,d(u)\,du, \qquad S(t) = \mathbb{Q}(\tau > t).
$$

The yield is the rate that makes the *first* term alone match the price with $S \equiv 1$. A five-year 7% bond at 40 has a yield above 31%. Nobody expects to earn 31%; the market expects to be paid $R$ at some point and is pricing the timing. Mags's version: "Below seventy it isn't a yield. It's a ransom note with a coupon schedule." That is the reason bonds switch from spread quotes to price quotes in distress (App A §A.5), and the reason Chapter 5 treats price, spread and return as three different distributions (§5.2).

Theo's thirteen-week cash flow model, it turns out, was a bond all along: a dated list of cash flows with an internal rate of return he never computed because nobody in a restructuring wants to know the IRR of a company that is running out of money. Add one row of discount factors and the USB stick becomes a pricing engine.

> **Desk Myth vs. Desk Reality.** *Myth:* "The bond yields 9%, so it returns 9% if nothing happens." *Reality:* It returns 9% if nothing happens *and* rates and spreads are unchanged at every coupon date *and* each coupon is reinvested at 9%. If spreads move, the return over a horizon is carry plus $-D\,\Delta y + \tfrac12 C\,(\Delta y)^2$, which is the next two sections; if the issuer defaults, the return is $R$ divided by what you paid.

*Used in:* §5.2.2 (price as a bounded interval), §6.6 (the survival-weighted price), §8.1 (the return decomposition), §12.2 (yield as the carry term), §24.3 and §24.5 (`bond_cashflows`, `price_at_yield`), App A §A.5.

## 4B.3 Duration: Macaulay, Modified, Effective, Spread and Key-Rate

Desk framing. "Duration" answers two questions that share a number only because of a coincidence in calculus. One is *when, on average, do I get my money back?* The other is *how much do I lose per basis point?* A risk manager needs the second, a liability matcher needs the first, and a callable bond, a floater and a distressed bond each break the coincidence in a different way. So the book keeps five durations and never lets one stand in for another.

### Macaulay: the balance point

Define the present-value weights at yield $y$,

$$
w_k = \frac{\text{CF}_k\,(1 + y/f)^{-e_k}}{P^{\text{dirty}}}, \qquad \sum_k w_k = 1, \qquad D^{\text{Mac}} = \sum_k w_k\,\frac{e_k}{f}\ \text{(years)}.
$$

$D^{\text{Mac}}$ is the PV-weighted average time to payment. Put each cash flow's present value on a beam at its date; the Macaulay duration is where the beam balances. A zero-coupon bond has all its weight at one date, so $D^{\text{Mac}} = T$. A coupon bond's balance point sits before its maturity, and moves earlier as the yield rises, because distant weights are discounted harder.

"So the duration is the fulcrum," said Kaz.

"The fulcrum," said Mags, "is the security that gets the equity."

"Then it's the point where the claims balance." Kaz considered this. "Same physics."

Theo opened his mouth to object and found that he could not. The fulcrum security is the tranche where enterprise value runs out; the Macaulay duration is the date where present value balances. Both are centres of mass. Kaz's legal vocabulary remains a liability, but this once it was hedged.

### Modified: the derivative

From §4B.2, $dP/dy = -\frac{1}{f(1+y/f)}\sum_k e_k\,\text{CF}_k\,(1+y/f)^{-e_k}$. Divide by $-P$:

$$
D^{\text{mod}} \equiv -\frac{1}{P}\frac{dP}{dy} = \frac{D^{\text{Mac}}}{1 + y/f} .
$$

Under continuous compounding the denominator disappears and $D^{\text{mod}} = D^{\text{Mac}}$ exactly, which is one more reason the book's formulas use it. The par-bond case has a closed form worth memorizing. Differentiate the premium identity $P - 100 = 100(c - y)\,a_N(y)$:

$$
\frac{dP}{dy} = -100\,a_N(y) + 100\,(c - y)\,a_N'(y) \quad\Longrightarrow\quad D^{\text{mod}}_{\text{par}} = a_N(y) = \frac{1 - (1+y/f)^{-N}}{y}.
$$

The modified duration of a par bond *is* its annuity factor. That is why the DV01 of a par swap is its annuity times a basis point, and why the CDS risky annuity of §6.8 (RPV01) is the credit market's duration: it is the same object with survival probabilities inside the discount factors.

The fallen angel at constant ten-year maturity, 4.50% coupon: at a 3.50% yield (20 February 2020) $D^{\text{Mac}} = 8.25$ and $D^{\text{mod}} = 8.11$; at 9.00% (23 March) $7.74$ and $7.40$; at 5.50% (30 June) $8.07$ and $7.86$. The balance point moved earlier by half a year in one month because the market discounted the principal harder, not because anything in the indenture changed.

### Effective: reprice, don't differentiate

When cash flows depend on rates (a call, a floater's reset, a prepayment), the yield formula is the wrong function to differentiate. Bump the *curve*, reprice the *instrument* with all its options, and difference:

$$
D^{\text{eff}} = \frac{P(z - h) - P(z + h)}{2\,h\,P(z)}, \qquad C^{\text{eff}} = \frac{P(z + h) + P(z - h) - 2P(z)}{h^2\,P(z)},
$$

where $z \pm h$ is the zero curve shifted in parallel by $\pm h$ and every option is re-evaluated at the shifted curve with the spread held fixed. For a bullet on a flat curve, $D^{\text{eff}}$ equals the continuous-compounding $D^{\text{mod}}$ to $O(h^2)$. For a callable it is the only duration that is not a lie (§4B.7).

### Spread duration, and the two routes to zero

$D^{\text{spr}} = -\frac{1}{P}\,\partial P/\partial s$ for whichever spread $s$ the desk uses (Z, OAS, or a hazard-based spread). For a fixed-rate bullet priced at $\sum_k \text{CF}_k e^{-(z(t_k)+Z)t_k}$, the curve and the spread enter only through $z + Z$, so a parallel curve bump and a Z bump are the same bump and $D^{\text{spr}} = D^{\text{eff}}$. Three instruments break the equality:

- **Floaters and loans.** The coupon resets with the curve, so rate duration is the time to the next reset and spread duration is roughly the remaining life (built in §21.1).
- **Callables.** OAS duration, the `oasd` field of §19.2, is $-\frac1P\,\partial P/\partial\,\text{OAS}$ on the lattice; whether it equals $D^{\text{eff}}$ depends on the rate model (§4B.7).
- **Distressed bonds.** Under recovery of face, as $\lambda \to \infty$ the survival leg vanishes and the price tends to $100R\,\lambda/(\lambda + r)$, whose derivative in $r$ is $-100R\,\lambda/(\lambda + r)^2 \to 0$. The bond's rate duration goes to zero because the recovery is paid at default whatever the maturity. A modified duration computed from the 31% yield of §4B.2's bond at 40 still says about 3.3. This is the first of the two routes to zero duration in §8.3; the second, the negative rate–spread correlation, is the empirical duration of §8.2, which this chapter does not rebuild.

### Key-rate durations

A parallel bump hedges a parallel move. Curves twist. Key-rate durations (Ho 1992) split the parallel duration across tenors. Let the zero curve be linear between key tenors $T_1 < \dots < T_J$ and flat outside. Bumping node $j$ alone by $h$ shifts the curve by $h\,\phi_j(t)$, where $\phi_j$ is a tent: one at $T_j$, falling linearly to zero at the neighbouring nodes (and flat beyond the end nodes). Under continuous compounding,

$$
\text{KRD}_j = -\frac{1}{P}\frac{\partial P}{\partial z_j} = \frac{1}{P}\sum_k t_k\,\text{CF}_k\,d(t_k)\,\phi_j(t_k), \qquad \sum_{j=1}^{J}\phi_j(t) = 1 \ \ \forall t \ \Longrightarrow\ \sum_j \text{KRD}_j = D^{\text{eff}} .
$$

The tents are a partition of unity, so the key rates add up to the parallel duration, and the sum is a unit test. KRDs are what "duration-matched Treasury return" means when an index computes excess returns (§8.1; Man's KRD-matched convention in §9.8), and what a desk hedges with 5-year and 10-year futures instead of one.

> **Ways This Blows Up.** Replace linear interpolation with a cubic spline and the tents stop being local: a bump at the 5-year node moves the 30-year zero. The KRDs still sum to the parallel duration, so the unit test passes, but a 10-year bond acquires a nonzero 2-year key rate and the hedger finds itself short 2-year notes for no economic reason. Use local interpolation for risk, or bump par rates and re-bootstrap, and say which.

*Used in:* §5.2 (the spread-return expansion), §8.1 (KRD-matched excess returns), §8.2 (analytical versus empirical duration), §8.3 (the two routes to zero), §9.8 (benchmark-matched KRDs), §19.2 (`oasd`), §21.1 (the loan's two durations), §23.5 (spread Greeks), App A §A.5.

## 4B.4 Convexity, and the Three Things the Word Means

### The curvature

Work in continuous compounding, where the algebra is cleanest. With $P(y) = \sum_k \text{CF}_k e^{-y t_k}$ and weights $w_k = \text{CF}_k e^{-y t_k}/P$,

$$
D = \sum_k w_k\,t_k, \qquad C \equiv \frac{1}{P}\frac{d^2 P}{dy^2} = \sum_k w_k\,t_k^2 = D^2 + \sum_k w_k\,(t_k - D)^2 .
$$

The last equality is the variance decomposition $\mathbb{E}[t^2] = \mathbb{E}[t]^2 + \mathrm{Var}(t)$ under the PV weights. Convexity is duration squared plus the *dispersion* of the payment dates. A zero has no dispersion and $C = T^2$. A barbell (a 2-year and a 20-year) has the same duration as a 10-year bullet and far more dispersion, so more convexity. Differentiating $D$ itself gives the companion identity

$$
\frac{dD}{dy} = D^2 - C = -\sum_k w_k\,(t_k - D)^2 \le 0,
$$

so duration falls as yields rise at a rate equal to the dispersion, and a zero's duration does not move at all. With periodic compounding the exact counterpart, from the second derivative in §4B.2, is $C^{\text{mod}} = \frac{1}{P f^2 (1+y/f)^2}\sum_k e_k(e_k+1)\,\text{CF}_k(1+y/f)^{-e_k}$.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.158:* "The interviewer would then say 'Ah! I caught you! You see, the duration of the zero coupon bond is independent of interest rates, therefore the convexity of the zero coupon bond is zero'. Unfortunately, the interviewer was plainly wrong, as the discussion in this section demonstrates."
>
> **Annotation.** The identity $dD/dy = D^2 - C$ diagnoses the interviewer exactly. For a zero, $dD/dy = 0$ because the dispersion is zero, and the interviewer read "duration does not change" as "no curvature." But $C = T^2 = 400$ for a 20-year zero, and the price–yield curve bends; what vanishes is the *difference* between curvature and duration squared. For a credit desk the interviewer's error has a modern form: a risk report that carries only $D^{\text{spr}}$ and recomputes it daily looks as if it "captures" convexity because the duration moves. It captures the dispersion term only, and only after the move. The second-order P&L of a large spread move must come from $C^{\text{spr}}$ or from repricing.

### How big is the second term?

The Taylor expansion is $\Delta P/P \approx -D^{\text{mod}}\,\Delta y + \tfrac12 C^{\text{mod}}(\Delta y)^2$. The fallen angel on 20 February 2020 had $D^{\text{mod}} = 8.11$ and $C^{\text{mod}} = 78.0$ at a price of 108.38. Its yield then rose 550bp to 23 March. Duration alone predicts a loss of $8.11 \times 0.055 \times 108.38 = 48.3$ points. The convexity term gives back $\tfrac12 \times 78.0 \times 0.055^2 \times 108.38 = 12.8$, for a predicted $-35.5$. The bond actually lost 37.6. Convexity was worth thirteen points and overshot by two, because at 550bp the third-order term is not small. Use the expansion for risk reports and attribution. For stress and P&L, reprice.

### Convexity is paid for

Under either measure (a volatility is the same under $\mathbb{P}$ and $\mathbb{Q}$), the expected instantaneous return from convexity is $\tfrac12 C\,\sigma_y^2$ per year if yields have volatility $\sigma_y$ (in decimal per root-year). For the fallen angel at $\sigma_y = 100$bp a year that is $\tfrac12 \times 78 \times 0.0001 = 39$bp a year. Long-convexity positions look like free money, and are not: the market charges for convexity through a lower yield, so the barbell yields less than the bullet of the same duration. Veronesi's statement of the trade-off (Veronesi_Fixed_Income_Securities p.162) is that "the gain in value from higher convexity is offset by a lower gain due to the passage of time." Convexity is the one free lunch in fixed income that arrives with a bill, and the bill is called theta. Chapter 6-B derives the same bill for options, where it is the theta–gamma relation.

### The three meanings

The word appears more than fifty times in this book, in three senses that share a name and a sign convention and nothing else.

| Meaning | Object | Variable | Who pays for it, and how | Built or used in |
| :--- | :--- | :--- | :--- | :--- |
| 1. Price–yield curvature | $C = \frac1P\,\partial^2 P/\partial y^2$ (or $\partial s^2$) of a bond | yield or spread | the holder, through a lower yield | this section; §5.2.2, §8.3, §23.5 |
| 2. Option gamma | $\Gamma = \partial^2 V/\partial S^2$ of an option | the underlying | the long side, through time decay $\Theta$ | Chapter 6-B; §23.5 |
| 3. Payoff-shape convexity | curvature of $\mathbb{E}[\text{strategy return} \mid \text{market return}]$ over a horizon | the market's horizon return | the strategy, through whipsaw losses in reversals | §10.6.1 |

Meaning 1 is meaning 2 with the yield as the underlying: a bullet is long gamma in its own yield, a callable near its call price is short it (§4B.7), and a CDS protection buyer is short spread convexity (§23.5). Meaning 3 is not a derivative of any price function. It is a property of a dynamic strategy's conditional expected return, and "trend is a straddle" (§10.6.1) is an analogy to meaning 2 that holds because a trend rule approximately replicates one. When someone says "convexity," ask: *with respect to what, over what horizon, and who is short it?* The collision joins App A §A.3.

Spread convexity, finally, is meaning 1 with $s$ in place of $y$. For a bullet priced off $z + Z$ it equals the curve convexity. The spread-return expansion of §5.2, $X \approx s\,h + \text{roll} - D^{\text{spr}}\Delta s + \tfrac12 C^{\text{spr}}(\Delta s)^2$, now has every term built; its $C^{\text{spr}}$ turns negative for the callable high-yield bonds that dominate the index, which is the convexity tax of §5.9.

*Used in:* §5.2 and §5.9 (spread convexity and the third moment), §6.2 and Chapter 6-B (gamma), §8.3 (the discount-bond asymmetry), §10.6.1 (trend as a straddle), §21.5 (the loan's negative convexity under repricing), §23.5 (spread Greeks), App A §A.3 and §A.7.

## 4B.5 The Risk Report: DV01, CS01, DTS and the Hedge Ratio

Desk framing. A risk report turns derivatives into dollars, because a PM cannot add a modified duration to a key-rate duration to a CDS risky annuity, and can add dollars.

**DV01** is the dollar change in value for a one-basis-point *fall* in yield (positive for a long bond):

$$
\text{DV01} = -\frac{\partial P^{\text{dirty}}}{\partial y}\times 10^{-4} \times \frac{\text{Face}}{100} = D^{\text{mod}} \times P^{\text{dirty}} \times \text{Face} \times 10^{-6}.
$$

Per \$1mm of face, DV01 in dollars is simply $D^{\text{mod}} \times P^{\text{dirty}}$. Use the dirty price; App A's shortcut with the quoted price is close unless accrued is large. **CS01** is the same with $D^{\text{spr}}$ and a spread bump. For a fixed bullet the two coincide; for a loan CS01 dwarfs DV01; for a CDS, CS01 is the risky annuity times notional times a basis point (§6.8, §24.2). Signs follow App A §A.8: long credit is long CS01, and the rate term in a return is $-D\,\Delta y$.

**DTS** rescales CS01 by the spread level. With $s$ in basis points, $\text{DTS} = D^{\text{spr}}\,s$, and if spreads move *proportionally*, $\Delta s = s\,x$ with relative change $x$, then

$$
\frac{\Delta P}{P} \approx -D^{\text{spr}}\,s\,x \times 10^{-4} = -\text{DTS} \times x \times 10^{-4}.
$$

When relative spread changes have similar volatility across bonds, which is the empirical finding behind §8.4, DTS is the unit of credit risk and CS01 is not (Law 3).

The fallen angel makes the difference vivid. Per \$10mm face, DV01 (equal to CS01 here) was \$8,785 on 20 February and \$5,236 on 23 March: down 40%. DTS, using $D^{\text{mod}}$ and the 198bp and 824bp G-spreads, went from 1,605 to 6,100: up 3.8 times. The CS01 report said the position had become safer. The DTS report said it had become almost four times riskier. Both were arithmetically right. Only one described a market in which spreads were moving in percent, which is what the cold open's "per basis point it got less risky" was missing.

**The hedge ratio.** To neutralize rate risk with an instrument $H$, hold $-\text{DV01}_{\text{bond}}/\text{DV01}_{H}$ of it per unit of bond. A par ten-year Treasury has $D^{\text{mod}} = a_{20}(y)$ by §4B.3, so its DV01 per \$1mm is $100\,a_{20}(y)$ dollars: \$924 at the 1.52% ten-year yield of 20 February 2020 and \$961 at 0.76% on 23 March (FRED, DGS10). The bond's DV01 per \$1mm was \$878 and then \$524. The hedge ratio went from 0.95 to 0.545: \$9.50mm of Treasuries per \$10mm of bonds in February, \$5.45mm a month later. A static hedge set in February was 74% too large in March by its own analytic measure, before anyone asked §8.2 what the empirical hedge ratio of a bond at 824bp is (smaller still, and possibly negative).

> **Ways This Blows Up.** Finite-difference risk is only as good as the price under it. A price produced by a yield solver with a tolerance of $10^{-6}$ and bumped by one basis point gives a DV01 with about 1% noise, and a convexity that is pure noise. Use the analytic derivatives of §4B.2 for bullets, solve to $10^{-12}$ when you must solve, use a 10bp bump for second differences on a lattice, and check that the key rates sum to the parallel number before the report goes out.

*Used in:* §1.3 (the inventory term in the bid equation), §8.4 and §9.2 (DTS as beta), §8.6 (the hedge matrix in DV01 terms), §10.3 (volatility scaling is DTS scaling), §12.5 (DTS-structured covariance), §19.2–§19.4 (basket risk and the lump hedge), §24.4 (basis carry per DV01), App A §A.5 and §A.8.

## 4B.6 One Curve, Eight Spreads

Desk framing. Every spread is the answer to one question, *how much more than the reference curve does this bond pay?*, asked with a different reference curve, a different idea of "pay," and a different compounding. Build the curve once and the eight answers are short.

### The curve

A zero curve is a function $z(t)$ with discount factors $d(t) = e^{-z(t)\,t}$. Markets quote *par* yields, so the curve is bootstrapped. On a grid $t_n = n/f$ with par yields $c_n$ (interpolated from quoted tenors), a par bond maturing at $t_n$ prices to one, $\sum_{k \le n} (c_n/f)\,d(t_k) + d(t_n) = 1$, which solves forward:

$$
d(t_n) = \frac{1 - (c_n/f)\sum_{k<n} d(t_k)}{1 + c_n/f}, \qquad z(t_n) = -\frac{\ln d(t_n)}{t_n}.
$$

The desk keeps two curves and always names which: Treasury (for G, Z and excess returns) and SOFR swaps (for I, asset swaps and anything a funded investor hedges).

### The eight

**G-spread.** $G = y - y^{\text{TSY}}_{\text{par}}(T)$, the bond's yield minus the Treasury par yield interpolated at its maturity. One subtraction, which is its appeal and its flaw: it compares a 4.50% coupon's yield with a different-coupon par bond's yield and ignores the curve's shape between today and $T$.

**I-spread.** The same subtraction against the par swap rate $y^{\text{SOFR}}_{\text{par}}(T)$. The difference $I - G$ is minus the swap spread at $T$; it is a fact about the curves, not the bond.

**Z-spread.** The constant $Z$ added to every zero rate that reprices the bond:

$$
P^{\text{dirty}} = \sum_k \text{CF}_k\, e^{-(z(t_k) + Z)\,t_k}.
$$

Linearize around the yield: $y^{\text{cc}} - Z \approx \sum_k \omega_k\,z(t_k)$ with duration weights $\omega_k \propto t_k\,\text{CF}_k e^{-y^{\text{cc}} t_k}$. The yield is the Z-spread plus a duration-weighted average zero rate. So $Z - G$ is (to first order) the par Treasury's weighted average zero minus the bond's. On an upward-sloping curve a high-coupon, high-yield bond puts its weight earlier than the low-coupon Treasury, its average zero is lower, and $Z > G$. Invert the curve, as it was for most of mid-2022 to mid-2024, and the sign flips. On a flat curve, Z in the bond's own compounding equals G exactly, and Z in continuous compounding differs only by the compounding.

**Asset-swap spread (par-par).** Schmid's definition is the cleanest on the shelf.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "Basically, an asset swap is a synthetic structure that allows an investor to buy a fixed rate bond and then hedge out the interest rate risk by swapping the fixed payments to floating. The investor keeps the credit exposure to the fixed rate bond."
>
> **Annotation.** The package has a price, and the price is the spread. In the par-par version the investor pays 100 for a bond worth $P$ and swaps its coupons for SOFR plus $A$. Setting the package's value to zero gives the formula below, and makes visible what the definition leaves out: when $P$ is far from par, the investor has also made (or received) an upfront payment of $100 - P$ to the swap counterparty. That loan carries counterparty and funding risk, which is why ASW and Z diverge for discount bonds and why the March 2020 basis trades of §24.4 cared which one they used.

Value the package per 100 at inception. The investor pays 100 and receives the bond ($P$). The swap's floating leg is worth $100\,(1 - d(T)) + 100\,A\,\mathcal{A}$ on the swap curve, where $\mathcal{A} = \sum_k \alpha_k d(t_k)$ is the annuity on the bond's coupon dates; the fixed leg paid away is $100\,c\,\mathcal{A}$. Let $P^{\text{sw}} = \sum_k \text{CF}_k d(t_k)$ be the bond's value on the swap curve. Then $P - 100 + 100 - 100\,d(T) + 100A\mathcal{A} - 100c\mathcal{A} = P - P^{\text{sw}} + 100\,A\,\mathcal{A} = 0$, so

$$
A^{\text{par}} = \frac{P^{\text{sw}} - P^{\text{dirty}}}{100\,\mathcal{A}}, \qquad A^{\text{mkt}} = A^{\text{par}}\,\frac{100}{P^{\text{dirty}}} .
$$

The market-value variant puts the floating leg on the dirty price instead of par. For a bond at 70 the two differ by a factor of 1.4.

**Discount margin.** For a floater or loan paying $b + m$ (base rate plus contractual margin), DM is the spread over the base rate that reprices it, under the convention that the base rate stays at today's level. On a reset date, a floater paying $b + m$ and discounted at $b + m$ is worth par by backward induction (each period's coupon is exactly the period's discount), so $\text{DM} = m$ at a price of 100, and to first order

$$
\text{DM} \approx m + \frac{100 - P}{100\,a(T)},
$$

with $a(T)$ the annuity at $b + \text{DM}$: the loan form of the premium identity, and (21.2) of §21.1 solved for $s$. The Larkspur Foam 2029 first-lien term loan of Chapter 13 pays SOFR + 375bp. At 97, with a flat 4.00% base rate and the common three-year-life convention *(illustrative)*, its DM is about 490bp. At the 84 mark of the morning of the headline it is about 1,040bp, at which point the desk stops quoting DM and starts quoting recovery. State whether the floor is priced: a floor is an option the lender owns, and the flat-forward convention values it at intrinsic only.

**Yield-to-worst.** The lowest yield over maturity and every call date, each at its call price: §4B.7, because it needs a call schedule.

**OAS.** The spread over the curve that reprices the bond *after* valuing its options on a rate model: §4B.7, because it needs a lattice.

**Par CDS equivalent (PECS).** Find the flat hazard $\lambda$ that reprices the bond with recovery of face $R$ (the formula of §4B.2, from §6.6.3), then read the par CDS spread off the same $(\lambda, R)$ with the legs of §6.8 and §24.2:

$$
P^{\text{dirty}} = \sum_k \text{CF}_k d(t_k)e^{-\lambda t_k} + 100R\!\int_0^{T}\!\lambda e^{-\lambda u}d(u)\,du, \qquad s^{\text{PECS}} = \frac{(1-R)\int_0^T \lambda e^{-\lambda u}d(u)\,du}{\text{RPV01}(\lambda)} \approx \lambda(1 - R).
$$

PECS is the bond spread that a CDS basis should use (App A §A.5), and it exceeds Z for a discount bond for a reason worth one line: Z is a loss rate per unit of *price*, a CDS spread is a loss rate per unit of *par*, and a bond at 70 with recovery 40 loses 30 of its 70 at default, not 60 of 100. Schmid makes the same point from the hedge's side.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "A default swap is a par product: it does not completely hedge the loss on an asset that is currently trading away from par. If the asset is trading at a discount, a default swap overhedges the credit risk and vice-versa."
>
> **Annotation.** Two consequences on a 2026 desk. For *valuation*, compare a discount bond with CDS only through PECS, or the convention masquerades as a basis. For *hedging*, the jump-to-default-neutral notional is $(P - R)/(1 - R)$ per unit of face (derived in §24.3), so \$10mm of the fallen angel at 70.73 with $R = 40\%$ needs about \$5.1mm of protection, not \$10mm. The departure from Schmid: $R$ is itself random and is now a property of the transaction (§5.5, §5.6), so PECS has a recovery delta that the desk must report next to it (Law 7).

| Spread | Reference | Solves for | State with it |
| :--- | :--- | :--- | :--- |
| G | Treasury par yield at $T$ | a subtraction | interpolation, on-the-run or fitted |
| I | swap par rate at $T$ | a subtraction | SOFR or LIBOR (pre-2023 data) |
| Z | Treasury or swap zero curve | constant shift that reprices | curve, compounding |
| ASW par / market | swap curve | package value zero | par or market value |
| DM | base rate, flat forward | constant margin that reprices | floor, assumed life |
| YTW | none (a yield) | minimum yield over workout dates | call schedule |
| OAS | zero curve plus rate model | shift that reprices the option-adjusted price | model, volatility |
| PECS | zero curve plus hazard | par CDS spread at the implied hazard | recovery $R$ |

*Used in:* §1.3 and §1.8.2 (spread in the bid equation and the fallen-angel case), §6.8 (the credit triangle), §8.4 and §9.2 (OAS as the DTS input), §12.3 (spread per unit of what), §19.2 (`oas`), §21.1 (DM), §24.2–§24.3 (Z, PECS and the basis), App A §A.5.

## 4B.7 The Callable Bond: Yield-to-Worst, a Lattice, OAS and the Make-Whole

Desk framing. Most high-yield bonds can be redeemed by the issuer at a schedule of prices after a non-call period. The issuer exercises when refinancing is cheaper, which is exactly when the bond has done well. The holder is short a call, so the bond's upside is sold in advance (§5.2.2). There are two ways to price what was sold: assume the worst and skip the model (yield-to-worst), or model rates and average over paths (OAS).

### Yield-to-worst

Brambleworth Packaging's 9.25% senior secured notes (Chapter 3's B3 credit, before the lender call) have five years to run, are non-call for two, then callable at 104.625, at 102.3125 from year three and at par from year four *(terms illustrative; a standard half-coupon, quarter-coupon, par schedule)*. At a price of 103, with semi-annual compounding:

| Workout | Redemption | Yield |
| :--- | ---: | ---: |
| first call, year 2 | 104.625 | 9.71% |
| second call, year 3 | 102.3125 | 8.78% |
| par call, year 4 | 100 | **8.35%** |
| maturity, year 5 | 100 | 8.50% |

The yield-to-worst is 8.35%, to the par call. Within a window, if the call price exceeds the market price the latest date in the window is worst, and if it is below, the earliest; so only the window boundaries need checking, though the code checks every coupon date anyway. YTW is the yield you get if the issuer plays perfectly against you *and* the future has no uncertainty.

> **Poker Table.** "Yield-to-worst," says Ines, "is putting the other player on the nuts every hand. It's a fine way to never lose more than you expected, and a terrible way to price, because he doesn't have the nuts every hand. Sometimes rates go up and the call is worthless. OAS is playing against his whole range." Her hand history: on bonds bought at YTW and later called, the markout at the call date is the difference between the YTW you were quoted and the OAS you were really earning. On bonds where rates rose instead, the call expired and you were paid the full coupon. Price the range.

### A lattice small enough to do by hand

Take a three-year annual-pay 9% bond, callable at 101 (ex-coupon) at years one and two, on a binomial short-rate tree with risk-neutral probability $\tfrac12$ and spread $s$ added to every node's rate. To keep the hand arithmetic honest, discount with simple annual rates, $1/(1 + r + s)$, on a tree that is not fitted to any curve: $r = 4\%$ today; 5% or 3% at year one; 6%, 4% or 2% at year two. Work backward at $s = 5\%$.

At year two each node has one payment left, 109: values $109/1.11 = 98.20$, $109/1.09 = 100.00$ and $109/1.07 = 101.87$, which the issuer calls at 101.00. At year one, the up node is worth $\tfrac12(98.20 + 9) + \tfrac12(100.00 + 9)$ discounted at 10%, or 98.27, and is not called; the down node is worth $\tfrac12(109) + \tfrac12(110)$ at 8%, or 101.39, and is called at 101.00. Today: $\tfrac12(107.27) + \tfrac12(110.00)$ at 9% gives **99.67**. The same tree with no call gives 100.03. The call is worth 0.36 points.

Now invert. If the market price is 99.67, the OAS is 500bp *by construction*: it is the $s$ at which the callable tree matches the price. The Z-spread is the $s$ at which the *non-callable* tree matches the same price, about 514bp. The call costs the holder 14bp a year, and $\text{OAS} = Z - (\text{option cost in bp})$, which is App A's "$\text{OAS} \le Z$ for callables" with the gap computed instead of asserted.

### The production lattice

Replace the toy with Ho–Lee: short rates $r_{i,j} = \theta_i + \sigma\sqrt{\Delta t}\,(2j - i)$ at step $i$, node $j = 0, \dots, i$, with normal volatility $\sigma$ (decimal per root-year) and continuous discounting $e^{-(r_{i,j} + s)\Delta t}$. Fit $\theta_i$ so that the tree reprices every zero-coupon bond. With Arrow–Debreu prices $Q_{i,j}$ (the value today of \$1 paid at node $(i,j)$, starting from $Q_{0,0} = 1$) and $x_{i,j} = \sigma\sqrt{\Delta t}(2j-i)$,

$$
\sum_j Q_{i,j}\,e^{-(\theta_i + x_{i,j})\Delta t} = d\big((i+1)\Delta t\big) \;\Longrightarrow\; \theta_i = -\frac{1}{\Delta t}\ln\frac{d\big((i+1)\Delta t\big)}{\sum_j Q_{i,j}\,e^{-x_{i,j}\Delta t}},
$$

then propagate $Q_{i+1,k} = \tfrac12 Q_{i,k}e^{-r_{i,k}\Delta t} + \tfrac12 Q_{i,k-1}e^{-r_{i,k-1}\Delta t}$. No root-finding is needed. Price backward from maturity: at each node the continuation value is $e^{-(r_{i,j}+s)\Delta t}\,\tfrac12(V_{i+1,j} + V_{i+1,j+1})$; on an exercise date the issuer replaces it with $\min(\text{continuation}, K(t_i))$; then add the coupon paid at $t_i$. The OAS is the root in $s$ of $V_{0,0}(s) = P^{\text{dirty}}$, unique because $V_{0,0}$ is decreasing in $s$.

Four identities make this lattice testable, and each is an assertion in §4B.9:

1. **No option, no adjustment.** Without a call, the value of a cash flow at $t_n$ is $e^{-s t_n}\sum_j Q_{n,j} = e^{-s t_n}d(t_n)$, so the OAS of a bullet equals its continuous Z-spread exactly.
2. **Zero volatility is yield-to-worst.** As $\sigma \to 0$ the path is deterministic, backward induction picks the issuer's best date, and the OAS equals the spread to worst. YTW is the zero-volatility OAS written as a yield.
3. **Curve shift equals spread shift (in Ho–Lee, with fixed strikes).** A parallel shift $h$ of the zero curve shifts every $\theta_i$ by exactly $h$ (substitute $d(t)e^{-ht}$ above and induct), so it is the same perturbation as $s \to s + h$, and $D^{\text{eff}} = D^{\text{OAS}}$. In a lognormal tree (Black–Derman–Toy, Black–Karasinski) the identity fails, and the desk stores both numbers (the `oasd` of §19.2 is the second).
4. **Volatility lowers OAS.** With any exercise and $\sigma > 0$ the callable is worth less than the bullet at the same spread, so $\text{OAS} < Z$, and more volatility makes the gap wider.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.467:* "It is also important to realize that the size of the OAS depends on the model used to compute it: It is possible that different term structure models may generate different OAS, in the same way they generate different values of options even when using the same inputs."
>
> **Annotation.** OAS is a residual, not an observation, and on a credit desk the residual contains three things Veronesi's Treasury callable does not: default risk (the lattice is a riskless tree with a spread on top), liquidity, and whatever the model gets wrong about the issuer's call behaviour (issuers call for covenant relief and M&A, not only for rates). So an OAS series is model output, and a backtest on it has a model inside it (Law 11). When Chapters 8–12 regress on OAS, they are using the index provider's model; when this desk computes OAS, it states $\sigma$ and the tree.

### Negative convexity

Near the call price the issuer's option binds and the callable's price flattens toward the strike as rates fall; Veronesi's Treasury callable shows the same thing, where "the bond price has to converge to the call price ($100) as interest rates decline" (Veronesi_Fixed_Income_Securities p.464). Effective convexity turns negative there, and far from the call, where the option is worthless, the two curves merge and convexity is positive again.

```text
Figure 4B.1 (schematic). Price against the level of rates (or spreads) at fixed OAS.

 price
   | .                                          .  straight bond: convex everywhere
   |   .                                        o  callable: same cash flows, short a call
   |     .
   | o o o o.o o                                <- pinned near the call price at low rates:
   |            o.                                 concave here, C_eff < 0
   |              o.
   |                o .
   |                   o .
   |                      o o . .               <- far from the call the option is worthless:
   |                             o o o . . .       the curves merge and convexity returns
   +---------------------------------------------- rate level / spread
```

### The make-whole

A make-whole call lets the issuer redeem at $K^{\text{MW}} = \max\!\big(100,\ \text{PV of remaining flows at the Treasury curve} + m_w\big)$, with a make-whole spread $m_w$ such as 50bp. On the lattice, compute $W_{i,j}$, the remaining flows valued at $r + m_w$ by a parallel backward induction, and set $K^{\text{MW}}_{i,j} = \max(100, W_{i,j})$.

*Proposition.* If $s \ge m_w$, the make-whole is never exercised. *Proof.* At every node the callable's continuation value is at most the non-callable value at spread $s$, which is at most the non-callable value at spread $m_w$ (positive cash flows, higher discount), which is $W_{i,j} \le K^{\text{MW}}_{i,j}$. So $\min(\text{continuation}, K^{\text{MW}}) = \text{continuation}$ everywhere. $\square$

A make-whole is a call struck at the issuer's own credit spread equal to $m_w$, so it is out of the money for every issuer that trades wider than T+50, which is every high-yield issuer and every fallen angel. It is worth nothing to price and a great deal in three places: a merger refinancing (entry 3 of the table in §15.1), a covenant defeasance, and a bankruptcy claim, where whether the make-whole is allowed was the Hertz fight (§16.6).

> **Trend Watch: The reference curve moved under every spread, 2018–2026.** *What changed:* the New York Fed began publishing SOFR on 3 April 2018; CME and LCH switched discounting of cleared US dollar swaps to SOFR in October 2020; the ARRC recommended CME Term SOFR on 29 July 2021, and it became the base rate of new leveraged loans; the USD LIBOR panel ended after 30 June 2023; US corporate settlement moved from T+2 to T+1 on 28 May 2024. The Treasury curve did its own work: the ten-year constant-maturity yield was 1.52% on 20 February 2020, 0.76% on 23 March and 0.66% on 30 June (FRED, DGS10), and the 2s10s curve was inverted for most of July 2022 to August 2024 (approx.; FRED, T10Y2Y), which flipped the sign of $Z - G$ for high-coupon bonds. *What it means for the desk:* an I-spread, ASW or DM series that spans 2019–2024 changes its reference curve in the middle; that is a structural break made of convention, and a factor or trend signal (Chapters 9, 10) will read it as a market move unless the panel is rebuilt on one curve. Accrued interest shrank by one business day on every trade in May 2024, and DM's "flat forward" assumption now runs on term SOFR, not three-month LIBOR.

*Used in:* §5.2.2 (the price cap and negative convexity), §5.9 (the convexity tax), §12.2 (YTW as the yield input), §15.1 (make-whole and call economics in mergers), §16.6 (the Hertz make-whole), §19.2 (`oasd`, `oas`), §21.5 (the loan's call as a repricing hazard), App A §A.5.

## 4B.8 Case Study: The Fallen Angel, Repriced in Every Measure

*Wednesday, 7:40 a.m.* Kaz had either not gone home, or gone home and come back in the same sweater, which on this desk amounts to the same thing. Overnight they had rebuilt all six columns from one object: the note's twenty coupons, priced against a Treasury curve held flat at each date's ten-year par yield (FRED, DGS10). The flat curve is a deliberate stylization. It sets the shape term in $Z - G$ of §4B.6 to zero, so any gap left between two columns has to be a convention. (Exercise 2 puts the real curve back.)

The first hour went where first hours on a quant desk go, which is reconciliation. Kaz's Z-spread for 23 March sat three basis points from the vendor's. Forty minutes later the reasons were on the whiteboard: the vendor fits a smoothed Treasury curve and values the bond for settlement two days later, with accrued. Both choices are defensible, both are on page 41 of a methodology PDF nobody had opened since 2017, and neither is visible in a column called `z_spd`. Mags watched the whiteboard fill. "In 1994 I'd have called the salesman and he'd have said 'call it eight hundred.' Same answer, and nobody lost a night's sleep." She paused. "Mind you, he was lying about something else."

Then Kaz put up the table.

*Table 4B.1. The Chapter 1 fallen angel (stylized ten-year 4.50% note, semi-annual, on a coupon date, so dirty equals clean) on three dates, every measure computed from one flat curve. Treasury yields are real; the bond's yields are illustrative; §4B.9 reproduces every entry. Spreads in basis points.*

| | 20 Feb 2020 | 23 Mar 2020 | 30 Jun 2020 |
| :--- | ---: | ---: | ---: |
| Ten-year Treasury (DGS10) | 1.52% | 0.76% | 0.66% |
| Bond yield | 3.50% | 9.00% | 5.50% |
| Price | 108.38 | 70.73 | 92.39 |
| G-spread | 198 | 824 | 484 |
| Z-spread (continuous) | 196 | 804 | 477 |
| OAS (Ho–Lee, $\sigma$ = 100bp, make-whole at T+50) | 196 | 804 | 477 |
| Asset swap, par-par | 207 | 679 | 463 |
| Asset swap, market value | 191 | 959 | 501 |
| PECS ($R = 40\%$) | 186 | 945 | 482 |
| $D^{\text{mod}}$ | 8.11 | 7.40 | 7.86 |
| DV01 per \$10mm | \$8,785 | \$5,236 | \$7,258 |
| DTS ($D^{\text{mod}} \times G$) | 1,605 | 6,100 | 3,802 |

The I-spread equals G here, because the stylized swap curve is the Treasury curve.

"Now," said Ines, "which rows are the pot?"

### Rows that are only rulers

Start with the gaps that would exist on a day when nothing happened. G and Z differ by 2.5bp in February, 19.5bp in March and 7.3bp in June, and on a flat curve all of it is compounding, which grows with the square of the level. The two asset swaps differ by exactly $100/P$: 0.92 at the premium, 1.41 at the trough. PECS sits *below* Z in February and *above* it in March, because a CDS spread is a loss rate per unit of par, Z one per unit of price, and the bond crossed par on the way down (§4B.6). The OAS row equals Z on all three dates, and not by rounding: the make-whole is struck at T+50, the bond never traded tighter than 196bp, and by the proposition of §4B.7 a make-whole is never exercised while the spread exceeds the make-whole spread. The vendor's `oas` column was Z with a more expensive name.

Mags, who regards any number with "adjusted" in its name as a number somebody wanted to be different, was briefly delighted. "The one time an adjustment was honest, it was zero."

"Make whole *whom*?" asked Kaz, who was reading an indenture for the first time and had reached the redemption section. "Is it an insurance term?"

"The bondholder," said Theo. "It's the only clause in the indenture that apologizes in advance."

> **Math, Gently.** *Six rulers, one length.* G, Z, the two asset swaps and PECS are rulers with different units and zero points. On any one day they rank bonds almost identically, which is why ROBO found them "highly correlated." Their *changes* and *ratios* are another matter. Warm a room from 10°C to 20°C and Celsius says the temperature doubled; Fahrenheit says 50°F to 68°F, up 36%. Nothing got twice as hot. In Table 4B.1 the same bond's spread multiplied by 3.3 on the par asset-swap ruler and by 5.1 on the PECS ruler, in the same month. For compounding the conversion is one line of Taylor: $\ln(1+x) \approx x - x^2/2$, so $y^{\text{cc}} = f\ln(1 + y/f) \approx y - y^2/(2f)$, and at $y = 9\%$ with $f = 2$ the gap is $0.09^2/4 \approx 20$bp. The full version is in §4B.2.

### Rows that moved

Every ruler agrees that something enormous happened between 20 February and 23 March: the note's spread rose by roughly six percentage points (market-wide, about 250bp for investment grade and 550bp for high yield, by the count in New York Fed Staff Report 986). They disagree about *how* enormous. G rose 626bp, Z 609, the par-par asset swap 471, the market-value asset swap 768, PECS 759: a 300bp disagreement about the change, which is the left-hand side of every regression in Part III and the input to every trend signal in Chapter 10. In relative terms, which is how DTS (Law 3) measures, the multiplier runs from 3.3 to 5.1, so the same bond's measured volatility depends, by half, on which column was loaded.

Then the P&L, the one row on which money moved. The note lost 37.65 points. Split it as §4B.4 did, around February's $D^{\text{mod}} = 8.11$, $C^{\text{mod}} = 78.0$ and $P = 108.38$: the 76bp Treasury rally contributed $+6.7$ points; 626bp of spread widening contributed $-55.0$; convexity on the 550bp total yield move gave back $+12.8$; and the residual, mostly the third-order term, was $-2.1$. An explain without its residual line claims a precision it does not have.

Then the hedge. In February the analytic ratio of §4B.5 said to short \$9.5mm of the ten-year against \$10mm of the note. The ten-year rallied 7.3 points, so the hedge *lost* about \$0.69mm while the note lost \$3.76mm. It did exactly what it was sized to do, against a rate move with the opposite sign from the one that mattered.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.191:* "If this correlation is negative, the empirical duration would be lower than the analytical one and may even end up being negative."
>
> **Annotation.** March 2020 is that sentence with numbers in it. Treasury yields fell while the note's spread rose eight times as far, so $\rho_{y,s}$ was sharply negative and the analytic hedge pointed the wrong way. Ben Dor's Table 7.1 (p.192, 1998–2009 data) puts the Ba bucket's empirical hedge ratio at maximum spreads at −0.26: the right hedge at 824bp was a small *long*, or nothing. The modern departure: the correlation is a regime, not a constant. In 2022 it flipped, and "no hedge" lost on rates and spreads together (§8.7). The desk reports $D^{\text{mod}}$ and hedges with the rolling empirical duration of §8.2, and shows both.

### Rows that became prices again

The rest is the tape, which a backtest cannot see unless somebody writes it down. The Federal Reserve announced its corporate credit facilities on 23 March, the table's middle column, before buying a single bond. S&P cut Ford to BB+ on 25 March; Moody's had rated it Ba1 since September 2019, so with two high-yield ratings Ford's bonds left the investment-grade index at the month-end rebalance (§1.8.2). On 9 April the Fed extended its facilities to issuers that had been investment grade on 22 March, which covered Ford. And on 17 April Ford came to the high-yield market itself.

> **View From Another Seat.** *The issuer.* On 17 April 2020 Ford priced \$8bn of unsecured notes in three tranches: \$3.5bn of three-year notes at 8.50%, \$3.5bn of five-year at 9% and \$1bn of ten-year at 9.625%, the ten-year after being marketed at around 11% (Bloomberg, via BNN Bloomberg, 17 April 2020). From the treasurer's seat, none of the six columns exists. A bond sold at par has $c = y$ (§4B.2), so the coupon *is* the yield, and the yield is ten years' cost of capital, more than double the old 4.50% coupon. For the desk it was the cleanest spread observation of the month: no curve, no compounding convention, no recovery assumption, and \$8bn changed hands at it. The move from talk to print, about 140bp on the ten-year, measured demand in the one unit nobody argues with.

By 30 June the stylized note was back at 92.39 and 484bp over, and the rulers had drawn back together, as they do when price returns toward par: the compounding gap fell with the level, $100/P$ fell toward one, and PECS and Z converged because price and par did.

> **View From Another Seat.** *The life insurer and the bank desk.* A life insurer holding the note at amortized cost saw none of 23 March in its statutory income. Its number was the rating: the move from an NAIC 2 to an NAIC 3 designation multiplied the capital held against the position, and its "spread" was book yield over the liability's crediting rate. It sold, if it sold, over quarters, into the June column (§1.8.2). A bank's credit-trading desk writes its limits in CS01, and the CS01 report showed 40% less risk on 23 March than in February, freeing limit on the day bid–offer was widest, though the balance sheet the limit rations had not grown (§22.5). CS01 said "room to add," DTS said "four times the risk," and both were arithmetically correct.

### When to reach for which number

The habit that separates a seasoned desk from a fast one is to start from the question and let the question choose the ruler.

| The question you are actually asking | The number | Where it breaks |
| :--- | :--- | :--- |
| Is this bond cheap against its own CDS? | PECS, with $R$ stated | at or below recovery there is no solution; $R$ is random (§5.5) |
| What does a funded investor earn over SOFR after swapping? | asset swap: par-par if the package is bought at 100, market value if at $P$ | far from par, par-par hides a loan of $100 - P$ to the swap dealer |
| Which of two callables is cheaper? | OAS at a stated $\sigma$ and tree | issuers call for covenants and M&A, not only for rates (§4B.7) |
| How many Treasuries do I short? | DV01 from $D^{\text{eff}}$, then the empirical ratio of §8.2 | high yield in a crisis, where the analytic hedge can have the wrong sign |
| How much credit risk is this? | DTS | near default, where price and recovery dominate (§8.3) |
| What feeds a factor or trend signal? | one spread, on one curve, for the whole sample | a reference-curve switch (LIBOR to SOFR, 2023); G across the 2022–24 inversion |
| What is it worth below 70? | price, and a recovery | every spread on this list |

Ines read the table twice and tapped the last row. "That's the pot. Everything above it is how people choose to count their chips."

*Used in:* §1.8.2 (Ford and the fallen-angel wave), §5.2 (price, spread and return as three distributions), §8.2 and §8.7 (the hedge with the wrong sign), §8.4 and §10.3 (DTS and volatility scaling), §12.3 (spread per unit of what), §19.7.2 (March 2020 in portfolio trading), §22.5 (dealer capital), §24.3–§24.4 (PECS and the basis), App A §A.5.

## 4B.9 Specification for AI Implementation: `bondmath.py`

**The Spec You Hand the Robot.** *What ROBO built from the vague version* ("add a spread function to the bond library"): `spread(bid, ask) = ask - bid`, with a docstring, a unit test and full coverage. It was correct.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.68:* "The word spread is perhaps the most overloaded (and sometimes abused) word in finance."
>
> **Annotation.** ROBO picked a correct dictionary entry, and the wrong one. The cure is not a better guess but a signature that cannot be called without the missing facts: which curve, which compounding, which price (dirty, per 100), which unit comes back. This module implements eight meanings and computes none of them from a clean price.

*What the module is for, at this point in the story.* The cold open showed what happens when every consumer of a spread computes its own: six columns, 280bp apart. So `bondmath.py` is less a pricing library than a single source of arithmetic. Chapters 5, 8, 9, 10, 12, 15 and 19 import it, so that when two chapters disagree, they disagree about the market and not about compounding.

*Why it is built this way.* The chapter reduces to two objects and one verb. The objects are a list of (time, cash flow) pairs (§4B.1) and a discount function $d(t)$ (§4B.6). The verb is *reprice*: a yield, a Z-spread, an OAS, a hazard rate and a discount margin are each the single constant that, inserted in the right place, makes the list equal the dirty price. So there is one pricing kernel per model (yield, curve, hazard, lattice) and one solver for all of them: bisection, on purpose. Every kernel is strictly monotone in its constant (§4B.2), so a bracketed bisection cannot find the wrong root or diverge, and when the price is impossible it fails loudly, which is the failure you want.

> **Math, Gently.** *An implied number is a question asked backwards.* Pricing runs forward: give me a yield and I will give you a price. Every spread on the desk runs backward: here is the price, so what yield, spread or hazard would have produced it? Bisection plays twenty questions. Take a bracket that surely contains the answer, say yields from −5% to 500%, and price the midpoint. If that price is above the market's, the yield is too low, so keep the upper half; otherwise keep the lower. Each guess halves the bracket, so 43 guesses shrink 5.05 below $10^{-12}$ and the 9.00% of 23 March comes back to twelve decimals. It works because price only falls as yield rises, and a one-way function crosses a given price once. The proof is in §4B.2.

*Inputs and outputs.* Prices per 100 face, dirty unless a name says otherwise; rates, spreads and hazards as annual decimals (basis points only for display); times in years. A curve is any function `disc(t)` returning discount factors, flat (`flat_curve`) or bootstrapped (`curve_from_par`). Results are floats or dicts with named fields. The lattice runs on a grid: `ho_lee` builds the tree, `on_grid` places the flows, `lattice_price` runs §4B.7's backward induction.

*When to use it, and when not.* Use it for research, for the risk report's analytics, and to check a vendor; it found Kaz's three basis points. It is not a production library: no holiday calendars, no odd coupons beyond $w$, a CDS premium leg paid continuously on ACT/360 (within a basis point or two of §24.2's quarterly model), and a Ho–Lee tree whose normal rates go negative at the bottom nodes. A lognormal desk will disagree with this OAS by a few basis points, and each will be right about its own model (Veronesi p.467, §4B.7).

*The edge cases that bite.* First, `pecs` on a bond at or below its assumed recovery has no solution, since no hazard can make a bond worth less than its recovery. The function raises, and the right response is to quote price and recovery, not to lower $R$ until the solver is happy. Second, a clean price passed as dirty gives a smooth, plausible yield that is off by the accrued; the solver cannot know, so the argument is named `p_dirty`. Third, the lattice refuses a cash flow off its step dates, because rounding a coupon to the nearest node moves it by up to half a step and the OAS absorbs the error silently.

*Tests.* Every identity in the chapter is an assertion at the bottom of the listing, from the 0.50 of accrued and the 31st rule to the lattice identities of §4B.7 and the make-whole proposition, and so is the 23 March column of Table 4B.1.

<!-- EXPLAINED -->
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
dt_fa, rates_fa = ho_lee(disc_mar, 10.0, 40, 0.01)
flows_fa = on_grid(t_fa, cf_fa, dt_fa, 40)
mw_calls = {k: None for k in range(2, 40, 2)}
assert abs(oas(mar["price"], flows_fa, dt_fa, rates_fa, mw_calls, mw=0.005) - z_mar) < 1e-9
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

*Used in:* §5.2 and §5.9 (durations and convexities in the spread-return expansion), §6-B.8 (Halvorsen's Z-spread), §8.1–§8.4 (excess returns, empirical duration, DTS), §9.2 and §10.3 (DTS as beta and as the volatility scaler), §12.2–§12.3 (carry and spread per unit of risk), §15.1 (call and make-whole economics), §19.2 (`oas`, `oasd`), §21.1 (`discount_margin`), §24.2–§24.3 (`hazard_price`, `pecs`), App F.

## 4B.10 Desk Debrief

- **A bond is a list, and a yield is a price in another font.** Every spread is the one constant that makes the list reprice against some curve. Name the curve, the compounding and the dirty price, or the number means nothing. (Law 11)
- **Duration answers two questions that share a number by coincidence.** For a callable, a floater or a bond at 60, reprice; in a crisis, hedge with §8.2's empirical duration, because the analytic one can have the wrong sign. (Law 1)
- **"Convexity" is three words.** Ask with respect to what, over what horizon, and who is short it. The market charges for it in yield, and the bill is called theta.
- **Per basis point the fallen angel got safer; per percent it got four times riskier.** Size, limit and scale in DTS; keep CS01 for the hedge. (Law 3)
- **On a flat curve, every gap between spreads is a convention**: compounding ($\approx y^2/2f$), $100/P$, par versus price. Those conventions moved the measured spread change by 300bp in one month. (Law 11)
- **OAS is model output.** State $\sigma$ and the tree. For a bond trading wider than its make-whole spread, OAS equals Z and the adjustment is zero. (Law 13)
- **Below about 70, stop quoting spreads.** Quote price and recovery, and treat the solver's refusal as the signal. (Law 7)

**The Spec You Hand the Robot.** "Implement `bondmath.py` per §4B.9: 30/360 (31st rule), ACT/360, ACT/365F and accrued to settlement; price, YTM and YTW over every call-window coupon date; analytic and effective duration and convexity, tent key rates; DV01, DTS; flat and bootstrapped curves; G, Z, both asset swaps, DM, PECS; a Ho–Lee tree fitted by Arrow–Debreu prices with fixed-strike and make-whole calls, and OAS. One bracketed bisection that raises when unbracketed. Prices per 100 dirty, decimals, years. Tests: every identity in §4B.9 and Table 4B.1's 23 March column."

### Exercises

1. *(Rulers.)* With $y^{\text{cc}} \approx y - y^2/(2f) + y^3/(3f^2)$, reproduce the G − Z gaps of Table 4B.1 on an envelope, Treasury correction included. At what bond yield is half a point of "spread" made of compounding? *Solution.* At 9%: $20.25 - 0.61 = 19.6$bp, less 0.1bp for the Treasury, so 19.5. The gap reaches 50bp at about 14.5%.
2. *(The real curve.)* Bootstrap the 23 March 2020 Treasury par curve from FRED (DGS1, DGS2, DGS5, DGS7, DGS10, DGS30) with `curve_from_par` and recompute Z. Does the shape term raise or lower it? *Solution.* By §4B.6, $Z - G$ is the par Treasury's duration-weighted zero minus the note's. The note's weight sits earlier (Macaulay 7.74 years against about 9.6), so where the curve slopes up between seven and ten years the shape term is positive and offsets part of the 19.5bp compounding gap; its size must come from that day's data.
3. *(The hedge.)* Recompute the February-to-March P&L of \$10mm of the note with no hedge, with the analytic hedge, and with Ben Dor's Ba ratio at maximum spreads (−0.26 times the analytic notional). *Solution.* −\$3.76mm; −\$4.46mm; and (long \$2.5mm of Treasuries) about −\$3.58mm. The empirical hedge wins here and loses in 2022 (§8.7), so use a rolling estimate with a stated window, not a constant from a table.
4. *(Kaz reads the redemption section.)* Show with `lattice_price` that the T+50 make-whole is worthless on all three dates of Table 4B.1, and find where it starts to bind. Why does an RSSG banker still read the clause? *Solution.* By the proposition of §4B.7 it cannot bind while $s \ge m_w$; with the bond worth well above par at $r + m_w$, it binds once the spread falls below about 50bp, which is high-grade territory. The clause still matters in a merger refinancing (§15.1), a defeasance and a bankruptcy claim (Hertz, §16.6), where it is a claim amount, not an option.
5. *(ROBO's momentum signal.)* Theo asks for "twelve-month spread momentum on high yield, 2019–2025, using the spread column." Name three ways the output can measure conventions instead of markets. *Solution.* I-spread or ASW switching from LIBOR to SOFR in 2023 (rebuild on one curve); G across the 2022–24 inversion (use Z or OAS); YTW jumping when a bond's workout date changes (use OAS at a stated $\sigma$, labeled, Law 11).

### Deep-Dive Resource Graph

- **Podcasts.** *Wolf Street Report*, "Nothing's Fixed: What's Behind the Corporate Debt Bailout" (Wolf Richter, 6 May 2020), with transcript, https://wolfstreet.com/2020/05/06/nothings-fixed-whats-behind-the-corporate-debt-bailout/ : a skeptic's account of the March 2020 seizure and the Fed's facilities; read it next to McCauley below.
- **Practitioner Writing.** BNN Bloomberg, "Ford taps junk market for cash after virus spurs \$2 billion loss" (17 April 2020), https://www.bnnbloomberg.ca/ford-taps-junk-market-for-cash-after-virus-spurs-2-billion-loss-1.1422986 (the deal in §4B.8). Robert McCauley, "The Fed in the Corporate Bond Market in 2020" (Boston University Global Development Policy Center, 7 August 2020), https://bu.edu/gdp/2020/08/07/the-fed-in-the-corporate-bond-market-in-2020 , which argues the announcement did the work before the purchases. Congressional Research Service, *COVID-19 and Corporate Debt Market Stress* (Insight IN11275), https://www.everycrsreport.com/reports/IN11275.html . Veronesi, *Fixed Income Securities* (2010), Chapters 2–4 and 12.
- **Academic Papers.** Macaulay (1938), *Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856*, NBER; Ho and Lee (1986), *Term Structure Movements and Pricing Interest Rate Contingent Claims*, Journal of Finance 41(5); Black, Derman and Toy (1990), *A One-Factor Model of Interest Rates and Its Application to Treasury Bond Options*, Financial Analysts Journal 46(1); Ho (1992), *Key Rate Durations: Measures of Interest Rate Risks*, Journal of Fixed Income 2(2); Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen and Penninga (2007), *DTS (Duration Times Spread)*, Journal of Portfolio Management 33(2); Ambastha, Ben Dor, Dynkin, Hyman and Konstantinovsky (2010), *Empirical Duration of Corporate Bonds and Credit Market Segmentation*, Journal of Fixed Income 20(1); Haddad, Moreira and Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response*, Review of Financial Studies 34(11); O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, Journal of Financial Economics 142(1); Federal Reserve Bank of New York Staff Report 986, on the corporate credit facilities, https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr986.pdf
- **Data & Code.** `bondmath.py` (§4B.9, App F); FRED DGS10, https://fred.stlouisfed.org/series/DGS10 , and T10Y2Y, https://fred.stlouisfed.org/series/T10Y2Y ; New York Fed SOFR, https://www.newyorkfed.org/markets/reference-rates/sofr ; QuantLib, https://www.quantlib.org (the production library to check this module against, and the reverse); ISDA CDS Standard Model, https://www.cdsmodel.com

*Used in:* every chapter that quotes a duration, a DV01 or a spread; the Debrief bullets feed App E (Laws 1, 3, 7, 11, 13) and App A §A.3 (the convexity and duration collisions).

