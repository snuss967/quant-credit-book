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

