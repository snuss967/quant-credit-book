# Chapter 4-B: Bond Math for the Desk: Price, Yield, Duration, Convexity, Spread Measures and the Callable Bond

> *"The OAS represents the increase in the spot curve that is necessary for the model price to equal the traded price."* (Veronesi_Fixed_Income_Securities p.467)

## Cold Open: Six Columns Called "Spread"

*Tuesday 6 October 2026, 6:55 p.m., Theo Marsh's third week. A replay, run by Ines's rule of cutting a real episode off at a date and trading it blind (§1.8.2). The dates and Treasury yields are real; the bond is a stylized composite, its prices and spreads are illustrative, and every word the desk says is invented.*

The folder was called `FA_2020_cut0323`, and Ines had stuck the rules to Theo's monitor on a yellow Post-it, in the handwriting that once filled in tournament scorecards: *Cut it at 23 March. Trade it blind. Nobody looks at April.* Inside was a backtest with one job: replay the Chapter 1 fallen angel through March 2020 and ask whether a desk that absorbed the index sellers would have been paid for it (§1.8.2). Kaz had loaded the history up to the cut. Neither of them had a memory to cheat with. Kaz had spent that March in a university library finishing a thesis on stochastic filtering; Theo had spent it ten weeks into PJT, building thirteen-week cash forecasts for clients who were drawing every revolver they had. Mags and Ines had both been on dealer desks that month, which was why the Post-it said *blind* and why the two of them had been asked to keep quiet.

Theo opened the vendor file the way he used to open a data room. At PJT the first click was the same on every deal: the credit agreement, Article I, Definitions, because a number in a deal is worth exactly what the paragraph defining it says. "Consolidated EBITDA" had run to four pages and eleven add-backs in his last deal, and he could still recite the fight over each one. He looked for the vendor file's Article I. There was a tab called `data`; a tab called `meta`, which listed forty-one columns in alphabetical order, every one of type `float64`; and a README of two lines: *Spreads in bp. See methodology.* The methodology was a link to a PDF dated 2017. He bookmarked it and did not open it, a decision that would cost the desk forty minutes the next morning (§4B.8).

Six of the forty-one columns had "spread" in the name. On 23 March 2020 they read, left to right: `g_spd 824`, `z_spd 804`, `asw_par 679`, `asw_mm 959`, `oas 804`, `cds_equiv 945`. (The bond is a stylized ten-year 4.50% note of a BBB− auto issuer, held at constant maturity; the Treasury yields are real, the bond's yields are illustrative, and every number in this chapter is reproduced by the code in §4B.9.)

"Which one is the spread?" Theo asked.

"All of them," said Kaz. "Same bond, six coats."

"They differ by 280 basis points. In my old job, 280 basis points was a covenant reset and two weeks of lawyers."

Mags, from the next desk, without looking up: "When I started there was one spread. It was whatever the man on the phone said, minus whatever he thought you knew."

Ines came over with her coffee and read the row the way she reads a hand history. "Wrong question. Ask which one is the pot. Which of these numbers did money actually move on that day, and which ones are just the way somebody chose to count?"

ROBO had been asked the week before to "add the spread to the feature set." It had added all six, and reported, accurately, that they were highly correlated. Its note ran to one line, *pairwise correlation 0.97 to 0.99, 2010–2020; recommend retaining one*, and did not say which one, because nobody had asked and ROBO does not guess.

Theo scrolled to the duration column: 8.11 on 20 February, 7.40 on 23 March. "The bond got *less* risky? It lost thirty-eight points."

"Per basis point," said Kaz. "Per basis point it got less risky. There were just a lot more basis points."

The replay had dealt them a position along with the data: \$10mm of the note, bought in February, and \$9.5mm of ten-year Treasuries sold short against it, a hedge somebody had sized from that same duration column (§4B.5). The Treasury had rallied hard into the cut. So on the screen in front of Theo the bond was losing money and the hedge that was supposed to protect it was losing money too, in the same red, on adjacent lines.

"So which one do I load?" Theo asked. "And what does the risk report say tonight?"

"Z," said Kaz. "It's the only one built from a curve. G is a subtraction, the asset swaps are a package with a swap stapled to it, and the CDS one is an opinion about recovery."

Mags had been asked to keep quiet and had taken it as an instruction about volume. "Load the price."

"Price isn't a spread."

"No," said Mags. "That's what I like about it."

Ines did not take a side. She took an index card from the stack she keeps by the coffee machine, wrote on it, and put it face down on Theo's keyboard. He turned it over.

> *Write three things: which column you would load into the model, what the risk line should have read on 23 March, and whether you would have kept the Treasury hedge.*

"Due when?"

"Six-thirty tomorrow. Before Kaz rebuilds the columns." She picked up her coffee. "If you write it after, you'll write whatever Kaz built."

**By the end of this chapter you will be able to** build every number on that row, and every number behind it, from one list of cash flows and one curve: price and accrued, yield, the five durations, the three things "convexity" means, DV01, CS01 and DTS, the eight spreads, OAS on a calibrated lattice, and the make-whole. You will also be able to say which of them are the pot and which are counting conventions, and to ship `bondmath.py`, which Chapters 5, 8, 9, 10, 12, 15 and 19 import; the capabilities come back as the Finder table at the top of the Desk Debrief (§4B.10).

> **Prerequisites.** Calculus to second order (Taylor's theorem), continuous discounting $e^{-rt}$, and what a coupon is. Nothing else. The hazard-rate bond price in §4B.6 borrows one formula from §6.6.3 and says so; the lattice in §4B.7 is self-contained. A reader who already prices callables on a calibrated tree can skip to the case in §4B.8 and the code in §4B.9. Later chapters cite this one as §4B.N. The free evening before this chapter is Andrew Lo's MIT OpenCourseWare 15.401, "Lectures 4–6: Fixed-Income Securities" and "Recitation 2a" (Fall 2008), which derive spot rates, yield and Macaulay duration in MBA language and leave this chapter to do the credit desk's version (the lectures are linked in the Resource Graph; the recitation sits on the same course page).

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

> **Math, Gently.** *A bond is a stack of post-dated cheques.* Picture the note as twenty cheques in an envelope, each with a date and an amount on it: nineteen for \$2.25 and one for \$102.25. Nobody will hand you \$2.25 today for a cheque dated 2030, because money held now can earn something in the meantime. The *discount factor* $d(t)$ is the price today of a \$1 cheque dated $t$ years out, and it is below one for that reason; with continuous compounding at rate $z$ it is $d(t) = e^{-zt}$. A tiny number to redo in the margin: a \$100 cheque due in two years at 5% is worth $100e^{-0.05 \times 2} = 100e^{-0.10} = 90.48$ today, since $e^{-0.1} \approx 1 - 0.1 + 0.005 = 0.905$. The bond's price is each cheque's amount times its own discount factor, added up: twenty small multiplications and one sum. Every number in this chapter, from yield to OAS, turns out to be a different way of choosing those twenty discount factors. The formula opens §4B.2, once the calendar has had its say.

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

*Quant-Shop Life, a fictional composite: the operations desk of a systematic asset manager, the first break report of a month.* Agnieszka had been a reconciler for eleven weeks, long enough to stop reading the break report and start diffing it. It had one line: \$1,250 on \$10mm of a 4.50% note paying on 31 March and 30 September, bought for settlement on 31 October. She laid the firm's accrued and the custodian's side by side, field by field, and the only difference was a day: the custodian counted thirty from 30 September to 31 October, the firm's library thirty-one. The library had been written by a contractor and tested on the fifteenth of every month. The fix was four characters. The meeting about why nobody had caught it took an hour and left the sentence the desk still says before any pricing function goes live: "Accrued to settlement, thirty-first to thirtieth."

> **Ways This Blows Up.** A 30/360 function that forgets the "31st" rule is wrong by one day on every trade that starts or ends on the 31st. On \$10mm of a 4.50% bond one day of accrued is \$1,250. ROBO will not notice. The client's back office will, on the first trade of the month, and will send you a break for each one.

*Used in:* §15.2 (the change-of-control put at 101 plus accrued), §21.1 (ACT/360 loan interest), §24.2–§24.3 (CDS premium accrual and `bond_cashflows`), §24.5 (accrued at default and the deliverable), App A §A.4–§A.5, App D (settlement cycles).

## 4B.2 The Price–Yield Function

Desk framing. A yield is a price written in a different font. It is the single discount rate that, applied to every cash flow on the list, reproduces the dirty price. Its virtue is that it lets you compare a 4.50% ten-year with a 7.25% six-year in one number. Its vice is that the number contains two assumptions nobody says aloud: every coupon is paid, and every coupon is reinvested at the same yield. For an investment-grade bond those are close enough. For a bond at 60 they are fiction, and the yield is a promise, not a forecast.

### The street formula

> **Math, Gently.** *The one dial.* Take the envelope of cheques from §4B.1 and suppose that, instead of twenty discount factors, you are allowed one dial: a single rate applied to every cheque. Turn it up and every cheque is worth less, so the stack is worth less; turn it down and the stack is worth more. Somewhere on the dial the stack is worth exactly what the bond traded at, and that setting is the yield. Nobody observes a yield. A trader observes a price, and a solver turns the dial until the stack matches, the way you hunt for the right shower temperature: too hot, too cold, closer. Tiny number: a one-year 5% annual-pay bond trades at 99, so the stack is a single cheque for \$105, and the dial that makes it worth 99 solves $105/(1+y) = 99$, so $y = 105/99 - 1 = 6.06\%$. That 6.06% was on no screen until a division put it there. With twenty cheques no division does it, only the dial, and the dial is the formula next.

With $w$ the fraction of the current period still to run (on the bond's own day count), the street price–yield function with periodic compounding at frequency $f$ is

$$
P^{\text{dirty}}(y) = \sum_{k=1}^{N} \frac{\text{CF}_k}{\left(1 + y/f\right)^{k - 1 + w}} .
$$

On a coupon date $w = 1$ and the exponent is simply $k$. Summed in closed form (the derivation is just below), the formula hides the identity that every bond trader carries in their head without knowing it is an identity:

$$
P(y) - 100 = 100\,(c - y)\,a_N(y), \qquad a_N(y) = \frac{1 - (1 + y/f)^{-N}}{y} .
$$

A bond's premium is the present value of the coupon it overpays, and its discount is the present value of the coupon it underpays. The factor $a_N(y)$ is an annuity in years: the present value of receiving one unit a year, paid $f$ times a year, for the bond's remaining life. At par, $c = y$ and $P = 100$. That is the definition of a par yield, and it is the first unit test in §4B.9.

#### The Full Derivation

Write $v = (1 + y/f)^{-1}$ and $i = y/f$. On a coupon date the coupons form a geometric series, $\sum_{k=1}^{N} v^k = v\,(1 - v^N)/(1 - v) = (1 - v^N)/i$, so

$$
P(y) = \frac{100\,c}{y}\left[1 - \left(1 + \frac{y}{f}\right)^{-N}\right] + 100\left(1 + \frac{y}{f}\right)^{-N}.
$$

Subtract 100 from both sides, write $100 = 100\,(y/y)\left[1 - (1+y/f)^{-N}\right] + 100\,(1+y/f)^{-N}$, and the premium identity above falls out.

The properties of $P(y)$ come from differentiating term by term. Every cash flow is positive and every exponent $e_k = k - 1 + w$ is positive, so

$$
\frac{dP}{dy} = -\frac{1}{f}\sum_{k} e_k\,\text{CF}_k\left(1 + \frac{y}{f}\right)^{-e_k - 1} < 0, \qquad
\frac{d^2P}{dy^2} = \frac{1}{f^2}\sum_{k} e_k(e_k+1)\,\text{CF}_k\left(1 + \frac{y}{f}\right)^{-e_k - 2} > 0 .
$$

Price is strictly decreasing and strictly convex in yield. Two consequences follow. The yield is *unique*: a strictly monotone function crosses any price level once, so a bracketing solver cannot find the wrong root and cannot fail if the price lies between $P(\infty) = 0$ and $P(y_{\min})$; the shower has one right temperature. And the boundary cases are clean enough to make good tests: as $y \to 0$, $P \to 100\,(1 + cN/f)$, the undiscounted sum of the list; as $y \to \infty$, $P \to 0$. For a zero-coupon bond, $P = 100\,(1+y/f)^{-fT}$ and every result below collapses to something you can do in your head.

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

> **Math, Gently.** *Duration is a slope.* Plot the bond's price against its yield and you get a hill that falls away to the right: the higher the dial of §4B.2, the lower the price. Stand on the hill at today's yield and ask how steep it is where you are standing. That steepness, measured as the fraction of price lost per unit of yield, is modified duration. A walker's version: if the path drops 8 metres for every 100 metres forward, a one-metre step costs 8 centimetres. Tiny number: on 20 February the note had $D^{\text{mod}} = 8.11$ and a price of 108.38, so one basis point (0.0001) of yield moves the price by $8.11 \times 0.0001 \times 108.38 = 0.088$ points, about \$8,785 on \$10mm. The steepness changes as you walk, because the hill is curved, and the curve is §4B.4's subject. The derivative behind the slope is next.

From §4B.2, $dP/dy = -\frac{1}{f(1+y/f)}\sum_k e_k\,\text{CF}_k\,(1+y/f)^{-e_k}$. Divide by $-P$:

$$
D^{\text{mod}} \equiv -\frac{1}{P}\frac{dP}{dy} = \frac{D^{\text{Mac}}}{1 + y/f} .
$$

Under continuous compounding the denominator disappears and $D^{\text{mod}} = D^{\text{Mac}}$ exactly, which is one more reason the book's formulas use it. The par-bond case has a closed form worth memorizing. Differentiate the premium identity $P - 100 = 100(c - y)\,a_N(y)$:

$$
\frac{dP}{dy} = -100\,a_N(y) + 100\,(c - y)\,a_N'(y) \quad\Longrightarrow\quad D^{\text{mod}}_{\text{par}} = a_N(y) = \frac{1 - (1+y/f)^{-N}}{y}.
$$

The modified duration of a par bond *is* its annuity factor. That is why the DV01 of a par swap is its annuity times a basis point, and why the CDS risky annuity of §6.8 (RPV01) is the credit market's duration: it is the same object with survival probabilities inside the discount factors.

The fallen angel at constant ten-year maturity, 4.50% coupon: at a 3.50% yield (20 February 2020) $D^{\text{Mac}} = 8.25$ and $D^{\text{mod}} = 8.11$; at 9.00% (23 March) $7.74$ and $7.40$; at 5.50% (30 June) $8.07$ and $7.86$. The balance point moved earlier by half a year in one month because the market discounted the principal harder, not because anything in the indenture changed. Figure 4-B.1 shows the two beams.

![Figure 4-B.1: The note's twenty cash flows weighted by present value: the final payment carries two-thirds of the value at a 3.50% yield and 60% at 9.00%, so the balance point (the Macaulay duration) slides from 8.25 to 7.74 years. Illustrative: the stylized 4.50% ten-year note of Table 4B.1, computed by Listing 4-B.1.](assets/figures/ch04b_duration_balance_point.png)

### Effective: reprice, don't differentiate

When cash flows depend on rates (a call, a floater's reset, a prepayment), the yield formula is the wrong function to differentiate. Bump the *curve*, reprice the *instrument* with all its options, and difference:

$$
D^{\text{eff}} = \frac{P(z - h) - P(z + h)}{2\,h\,P(z)}, \qquad C^{\text{eff}} = \frac{P(z + h) + P(z - h) - 2P(z)}{h^2\,P(z)},
$$

where $z \pm h$ is the zero curve shifted in parallel by $\pm h$ and every option is re-evaluated at the shifted curve with the spread held fixed. For a bullet on a flat curve, $D^{\text{eff}}$ equals the continuous-compounding $D^{\text{mod}}$ to $O(h^2)$. For a callable it is the only duration that is not a lie (§4B.7).

### Spread duration, and the two routes to zero

$D^{\text{spr}} = -\frac{1}{P}\,\partial P/\partial s$ for whichever spread $s$ the desk uses (Z, OAS, or a hazard-based spread). For a fixed-rate bullet priced at $\sum_k \text{CF}_k e^{-(z(t_k)+Z)t_k}$, the curve and the spread enter only through $z + Z$, so a parallel curve bump and a Z bump are the same bump and $D^{\text{spr}} = D^{\text{eff}}$. Three instruments break the equality, and the desk met all three on the same whiteboard.

Later that Tuesday, with the replay's two red lines still on the screen, Kaz went to the whiteboard to show Theo where spread duration and rate duration part company, and drew three bonds. Theo, without being asked, wrote a clause beside each one.

The first was a floater. "The coupon is the curve plus a fixed margin," Kaz said, "so when the curve moves, the next coupon moves with it. The rate risk lives only until the next reset. The margin is locked for the whole life." Rate duration is the time to the next reset; spread duration is roughly the remaining life (built in §21.1). Theo wrote *Interest Period; Applicable Margin* beside it: the reset clause, which in a leveraged loan is three definitions and a benchmark-replacement section that nobody read until LIBOR died.

The second was a callable. Kaz drew a small tree and stopped. "Here the spread duration is OAS duration, $-\frac1P\,\partial P/\partial\,\text{OAS}$ on the lattice, the `oasd` field of §19.2. Whether it equals the effective duration depends on the rate model, which is a problem for later." Theo wrote *Article III, Redemption*: the section that hands the issuer the option, with its schedule of call prices and, at the bottom, the make-whole (§4B.7).

The third was a bond at 40. Kaz wrote the recovery-of-face price from §4B.2 and let the default intensity run off to infinity. "Under recovery of face, as $\lambda \to \infty$ the survival leg vanishes and the price tends to $100R\,\lambda/(\lambda + r)$. Differentiate in $r$ and you get $-100R\,\lambda/(\lambda + r)^2$, which goes to zero. The rate duration dies, because the recovery is paid at default whatever the maturity says."

"Acceleration," said Theo, and wrote it: *Section 6.02, Acceleration*, the number it carried in most of the indentures he had marked up. "On an Event of Default the whole principal is due now. The maturity date stops being a date and becomes a suggestion."

Kaz looked back at the screen. "A modified duration computed from the 31% yield of §4B.2's bond at 40 still says about 3.3."

"Because the yield formula believes the coupon schedule," said Theo. "The indenture has a section that says it might not happen."

That is the first of the two routes to zero duration in §8.3. The second, the negative correlation between rates and spreads, is the empirical duration of §8.2, which this chapter does not rebuild; the replay's hedge was already demonstrating it on the second red line, and §4B.8 grades it. The first route has a date on it, too, and the desk's next replay was built around that date.

#### Long Scene: The Book That Had a Duration and a Bank That Did Not

*A replay, run on Thursday 8 October 2026 at 5:10 p.m. and cut off at the close of Thursday 9 March 2023. The filings, dates and balance-sheet figures come from SVB Financial Group's 2022 Form 10-K and its March 2023 8-Ks, the Federal Reserve's April 2023 review of the bank's supervision, and the market data named in the text. The desk's marks for the note, its hedge and every line of dialogue are invented (illustrative).*

*The folder.* Ines had warned them on Tuesday that the fallen angel would not be the week's only replay, and on Thursday she came back with a thinner folder. It held the 2022 Form 10-K of SVB Financial Group, filed on Friday 24 February 2023, and the 8-K from the evening of Wednesday 8 March. "This isn't your fourth-weekend folder," she told Theo. "That one comes with a bid, and you get all of it then (§3.4). Tonight I'm lending you a ruler. Cut at the close of Thursday the ninth. Kaz plays, you play. Mags remembers, and keeps it to herself."

"I remember everything about that week," said Mags. "That's the trouble with me in a replay."

Kaz opened the 10-K and did something Theo had not seen a quant do with a filing: went straight to the fair-value footnote and read backwards from it. The held-to-maturity securities, carried at an amortized cost of \$91.3bn, had a fair value of \$76.2bn. With the available-for-sale book added, the unrealized losses came to \$17.7bn, against common equity of \$12.4bn: 143%. Deposits were \$173.1bn, down \$16.1bn in a year. Advances from the Federal Home Loan Bank stood at \$15.0bn, where a year earlier there had been none.

"This isn't a credit problem," said Kaz. "It's a duration problem with a credit problem attached." Kaz drew two boxes on the whiteboard. The left one said ASSETS: bonds bought when yields were at the floor, paying fixed coupons for years. The right one said DEPOSITS. "The left side has a duration measured in years. What's the duration of the right side? How long does it take to wire money out of a bank?"

"An afternoon," said Theo. "Less, if your venture investor sends an email."

"Then it's a bank that bought long duration with short money. The loss on the left is §4B.3's slope times how far rates moved. Nothing is wrong with the bonds. Every one of them is going to pay in full, on time."

"If they're held to maturity," said Theo.

"If the *bank* is held to maturity," said Kaz. "That's the only assumption in the accounting, and it's an assumption about the duration of the liabilities."

Kaz could not read the duration of the bank's portfolio off the page, and said so. The fair-value table gives a loss, not a slope, and backing a slope out of a loss needs the yields the book was bought at, which the 10-K does not lay out in one place. The loss was enough: about a sixth of the held-to-maturity book's cost had gone at market prices, and the equity that was supposed to absorb it was smaller than the hole. Five days after the bank failed, Dan Davies told the same story at greater length on the *Odd Lots* episode in this chapter's Resource Graph (14 March 2023), as a bank reaching for yield in long-dated Treasuries when rates were at the floor. Kaz had got there from one table. The depositors' side of the story, an uninsured share that the Federal Reserve's review later put at 94%, was a number the replay's rules kept out of the room.

*The note.* The holding company owed seven series of senior notes, \$3.3bn in all, one class, from the 3.50% due January 2025 to the 4.570% fixed-to-floating due April 2033. Ines's sheet carried a desk mark for one of them: the 1.800% notes due February 2031, at 75 on Wednesday's close (illustrative). Theo did what he had learned on Tuesday: dirty price, yield, slope. At 75 the yield was 5.77%, the modified duration 7.11 and the DV01 \$5,340 per \$10mm. "If we owned ten million, we'd short about \$8.9mm of seven-year Treasuries against it," he said, sizing DV01 against DV01 the way §4B.5 does. "And then we'd own the spread."

"And then you'd own the spread," said Kaz. "Spread duration is the same 7.1. It's a bullet; the curve and the spread sit in the same exponent."

Then the 8-K. After the close on 8 March the company announced that it had sold the available-for-sale book, \$23.97bn of it at amortized cost for \$21.45bn of proceeds, a loss of 10.5%, and that it would raise \$2.25bn of capital. The same evening Silvergate said it would wind itself down.

"They've sold the part of the book they were allowed to sell, at what it was worth," said Kaz. "The loss had been there all along. Now it's on the income statement."

"And they're raising equity to fill the hole," said Theo, "which tells every depositor how big the hole is." In six years of first-day declarations he had not once seen a company announce a capital raise and a loss in the same paragraph and have the paragraph calm anybody down.

*Thursday 9 March: the card.* Ines put Thursday's close into the replay. The stock had finished at \$106.04, down 60.4% from \$267.83 the day before. The desk's mark for the 2031s was 62 (illustrative). Theo reran the slope: yield 8.48%, modified duration 6.94, DV01 \$4,310 per \$10mm.

"Lower DV01," he said. "Per basis point it got less risky."

"That joke was funnier on Tuesday," said Kaz.

Theo checked the day's loss against the slope anyway, out of the habit of a man who used to tie every model back to the cash. The yield had risen 271 basis points. Wednesday's slope said that would cost $7.11 \times 0.0271 \times 75.1 \approx 14.5$ points; the mark had fallen 13. "The duration overstated the loss by a point and a half."

"Because the hill is curved," said Kaz. "Walk far enough and the slope you started with is wrong. That point and a half has a name, and it's the next section."

Ines dealt the card.

> *Write three things: the note's DV01, its spread duration, and which of the two you would bet on tomorrow.*

Kaz wrote fast: *DV01 \$4,310 per \$10mm. Spread duration 6.9. Bet on rates: if this spreads to other banks the curve rallies, so keep the Treasury short and size it to the DV01. It is the one line on this sheet I can price.*

Mags had been asked to keep quiet and wrote a card anyway, one line long: *A bank bond at 60 has no duration. It has a lawyer.*

Theo wrote the two numbers and stopped at the third line. Under it he wrote a question instead of an answer: *What does the holdco own?* It was the first question of his old job. A holding company owns the stock of its subsidiaries and whatever cash it keeps upstairs, and when the subsidiary is a bank, the cash upstairs has a way of being a deposit downstairs. Ines read the card and handed it back without a word on the third line. "Fourth weekend," she said.

(Your own card goes here, before Friday.)

*Friday 10 March: the grading.* Ines put up the morning. Trading in the stock was halted before the open. The thirty-day implied volatility, which had spent the year near the bottom of a 52-week range of 39 to 280, was quoted at 167 before the bell. By midday the California regulator had closed Silicon Valley Bank and appointed the FDIC as receiver, and the closing order put Thursday's withdrawals at more than \$40bn. The default mechanics, and why no structural model on any desk had seen it coming, are §6.4.4's case; Ines did not replay them. She asked for one thing. "Mark the note."

Nobody could, and that was the first lesson. There was no single-name CDS to read a curve from, and the notes traded by appointment; press reports in the days that followed put them in the 30s and 40s. Kaz asked for a number anyway, so Ines gave the desk's: 40 (illustrative).

Then she graded the cards against it.

Kaz's DV01 had been right on Thursday and meant nothing on Friday. At 40 the yield formula of §4B.2 still reported a modified duration of 6.5, because it still believed that sixteen coupons were coming. The bond's real rate duration came from the distressed route of §4B.3. Under recovery of face, with a large default intensity, the price is close to $100R\,\lambda/(\lambda+r)$, and its rate duration is $-\frac1P\,\partial P/\partial r = 1/(\lambda + r)$: the expected wait for the recovery payment, in years. At an intensity of 5 a year, a default expected within weeks, that is about 0.2. The Treasury short sized on Wednesday was hedging a rate duration that no longer existed, which made it a second position rather than a hedge. What a Treasury short did to a credit book on that Friday and the Monday after is Chapter 8's scene (§8, Case Study B), and it is not a kind one.

Spread duration did no better. It measures what a small change in the spread does to the price, and Friday's change was not small; it was a jump, and a jump is priced by what is lost when it happens, the price minus whatever the claim recovers, not by a derivative. When Kaz asked the §4B.6 code for a par-CDS-equivalent spread at 40 with $R = 40\%$, it returned an error instead of a number: no hazard rate can make a bond worth less than its recovery, so at or below recovery the solver has nothing to find.

"So the only number left," said Theo.

"Is the price," said Mags, "and a claim. I wrote *lawyer*."

The grades went on the whiteboard under Kaz's two boxes. Mags's card was the answer in eleven words. Kaz's card had both numbers right and the bet wrong, because the thing it bet on had left the bond. Theo's third line was not an answer, and it was the right question: what the claim was worth is the subject of his fourth-weekend drill (§3.4), where he bids the notes from the parent-company balance sheet. The claim's last chapter was written three and a half years later: in late August 2026, after a twelve-day bench trial, a federal court in California held that the liquidating trust that pays the senior noteholders could not recover the holding company's \$1.71bn deposit claim against the FDIC.

A reader whose card bet on either duration has made Kaz's mistake, which is a good mistake to make in a replay. Both durations describe a bond that is going to keep paying its list. On Thursday night that was still the bond on the screen. On Friday morning the list was gone, and with it every number that had been computed from the list.

Kaz added one line under the two boxes before wiping the board: *The book had a duration. The bank did not.* Mags read it twice, which on this desk counts as applause.

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

> **Math, Gently.** *Two trucks with the same centre of mass.* Load one truck with a single pallet in the middle of its bed, and another with two half-pallets, one over the front axle and one over the back. Both balance at the same point, the beam of §4B.3 again, so both have the same duration. But swing them round a corner and the second one fights you, because weight far from the centre resists turning. That extra resistance, over and above what the balance point alone would predict, is the extra convexity. A tiny number: a single \$100 cheque due in ten years has $D = 10$ and $C = 10^2 = 100$. Split the same present value into two equal halves due at 2 and 18 years and the balance point is still $\tfrac12(2 + 18) = 10$, but the convexity is $\tfrac12(2^2 + 18^2) = \tfrac12(4 + 324) = 164$. The extra 64 is the spread of the load, $\tfrac12(8^2 + 8^2)$. Cash flows spread out bend the price curve more than cash flows bunched together, and a zero, with all its weight on one date, bends by exactly its duration squared and not a hair more. The identity is next.

Work in continuous compounding, where the algebra is cleanest. With $P(y) = \sum_k \text{CF}_k e^{-y t_k}$ and weights $w_k = \text{CF}_k e^{-y t_k}/P$,

$$
D = \sum_k w_k\,t_k, \qquad C \equiv \frac{1}{P}\frac{d^2 P}{dy^2} = \sum_k w_k\,t_k^2 = D^2 + \sum_k w_k\,(t_k - D)^2 .
$$

Convexity is duration squared plus the *dispersion* of the payment dates. A zero has no dispersion and $C = T^2$. A barbell (a 2-year and a 20-year) has the same duration as a 10-year bullet and far more dispersion, so more convexity.

#### The Full Derivation

The last equality is the variance decomposition $\mathbb{E}[t^2] = \mathbb{E}[t]^2 + \mathrm{Var}(t)$ under the PV weights, which a physicist would recognize as the parallel-axis theorem of the trucks. Differentiating $D$ itself gives a companion identity. Since $dw_k/dy = -t_k w_k - w_k P'/P = -w_k\,(t_k - D)$, we have $dD/dy = -\sum_k w_k\,t_k\,(t_k - D) = -(C - D^2)$, that is,

$$
\frac{dD}{dy} = D^2 - C = -\sum_k w_k\,(t_k - D)^2 \le 0,
$$

so duration falls as yields rise at a rate equal to the dispersion, and a zero's duration does not move at all. With periodic compounding the exact counterpart, from the second derivative in §4B.2, is $C^{\text{mod}} = \frac{1}{P f^2 (1+y/f)^2}\sum_k e_k(e_k+1)\,\text{CF}_k(1+y/f)^{-e_k}$.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.158:* "The interviewer would then say 'Ah! I caught you! You see, the duration of the zero coupon bond is independent of interest rates, therefore the convexity of the zero coupon bond is zero'. Unfortunately, the interviewer was plainly wrong, as the discussion in this section demonstrates."
>
> **Annotation.** The identity $dD/dy = D^2 - C$ diagnoses the interviewer exactly. For a zero, $dD/dy = 0$ because the dispersion is zero, and the interviewer read "duration does not change" as "no curvature." But $C = T^2 = 400$ for a 20-year zero, and the price–yield curve bends; what vanishes is the *difference* between curvature and duration squared. For a credit desk the interviewer's error has a modern form: a risk report that carries only $D^{\text{spr}}$ and recomputes it daily looks as if it "captures" convexity because the duration moves. It captures the dispersion term only, and only after the move. The second-order P&L of a large spread move must come from $C^{\text{spr}}$ or from repricing.

### How big is the second term?

The Taylor expansion is $\Delta P/P \approx -D^{\text{mod}}\,\Delta y + \tfrac12 C^{\text{mod}}(\Delta y)^2$. The fallen angel on 20 February 2020 had $D^{\text{mod}} = 8.11$ and $C^{\text{mod}} = 78.0$ at a price of 108.38. Its yield then rose 550bp to 23 March. Duration alone predicts a loss of $8.11 \times 0.055 \times 108.38 = 48.3$ points. The convexity term gives back $\tfrac12 \times 78.0 \times 0.055^2 \times 108.38 = 12.8$, for a predicted $-35.5$. The bond actually lost 37.6. Convexity was worth thirteen points and overshot by two, because at 550bp the third-order term is not small. The expansion is good enough for risk reports and attribution; stress tests and P&L reprice. Figure 4-B.2 draws the two approximations against the true curve.

![Figure 4-B.2: Price against yield for the fallen angel, with the duration-only and duration-plus-convexity approximations built at the 3.50% yield of 20 February: at 9.00% duration alone is 10.7 points too low, and adding convexity overshoots by 2.1 because the third-order term is not small after a 550bp move. Illustrative: the stylized 4.50% ten-year note, computed by Listing 4-B.1.](assets/figures/ch04b_price_yield_taylor.png)

### Convexity is paid for

> **Math, Gently.** *Jensen's coin, and the tax Itô will collect.* **Part one.** Take a ten-year zero priced at a 5% continuous yield: $100e^{-0.5} = 60.65$. Now flip a coin. Heads, the yield goes to 6% and the price to $100e^{-0.6} = 54.88$; tails, it goes to 4% and the price to $100e^{-0.4} = 67.03$. The *average yield* is still 5%, but the *average price* is $\tfrac12(54.88 + 67.03) = 60.96$, which beats 60.65 by 0.31, or 0.5% of the price. The curve bends upward, so the tails gain more than the heads lose, and the holder of a curved payoff profits from the wobble itself. The size of the gift is half the convexity times the variance: here $C = T^2 = 100$ and the move is $\pm 1\%$, so $\tfrac12 \times 100 \times 0.01^2 = 0.5\%$, the same number the coin gave. Mathematicians call the inequality Jensen's; traders call it being long convexity. **Part two.** The same half-sigma-squared turns up whenever a curved payoff rides a noisy variable, which in this book is constantly. Chapter 6 calls it Itô's term and derives it from $(dW_t)^2 = dt$ (§6.1.2; §5.2.3 has the picture). Here it is a coin, and the paragraph after this box sends the bill.

Under either measure (a volatility is the same under $\mathbb{P}$ and $\mathbb{Q}$), the expected instantaneous return from convexity is $\tfrac12 C\,\sigma_y^2$ per year if yields have volatility $\sigma_y$ (in decimal per root-year). For the fallen angel at $\sigma_y = 100$bp a year that is $\tfrac12 \times 78 \times 0.0001 = 39$bp a year. Long-convexity positions look like free money, and are not: the market charges for convexity through a lower yield, so the barbell yields less than the bullet of the same duration. Veronesi's statement of the trade-off (Veronesi_Fixed_Income_Securities p.162) is that "the gain in value from higher convexity is offset by a lower gain due to the passage of time." Convexity is the one free lunch in fixed income that arrives with a bill, and the bill is called theta. Chapter 6-B derives the same bill for options, where it is the theta–gamma relation.

### The three meanings

The word appears more than fifty times in this book, in three senses that share a name and a sign convention and nothing else.

| Meaning | Object | Variable | Who pays for it, and how | Built or used in |
| :--- | :--- | :--- | :--- | :--- |
| 1. Price–yield curvature | $C = \frac1P\,\partial^2 P/\partial y^2$ (or $\partial s^2$) of a bond | yield or spread | the holder, through a lower yield | this section; §5.2.2, §8.3, §23.5 |
| 2. Option gamma | $\Gamma = \partial^2 V/\partial S^2$ of an option | the underlying | the long side, through time decay $\Theta$ | Chapter 6-B; §23.5 |
| 3. Payoff-shape convexity | curvature of $\mathbb{E}[\text{strategy return} \mid \text{market return}]$ over a horizon | the market's horizon return | the strategy, through whipsaw losses in reversals | §10.6.1 |

Meaning 1 is meaning 2 with the yield as the underlying: a bullet is long gamma in its own yield, a callable near its call price is short it (§4B.7), and a CDS protection buyer is short spread convexity (§23.5). Meaning 3 is not a derivative of any price function. It is a property of a dynamic strategy's conditional expected return, and "trend is a straddle" (§10.6.1) is an analogy to meaning 2 that holds because a trend rule approximately replicates one. When someone says "convexity," ask: *with respect to what, over what horizon, and who is short it?* The collision joins App A §A.3.

"So when the trend people say convexity," Theo asked, "they mean the shape of a *strategy*, not of a bond?"

"Of a strategy that behaves as if it owned a straddle," said Kaz. "Nobody sends it a theta bill. It pays in whipsaws."

Spread convexity, finally, is meaning 1 with $s$ in place of $y$. For a bullet priced off $z + Z$ it equals the curve convexity. The spread-return expansion of §5.2, $X \approx s\,h + \text{roll} - D^{\text{spr}}\Delta s + \tfrac12 C^{\text{spr}}(\Delta s)^2$, now has every term built; its $C^{\text{spr}}$ turns negative for the callable high-yield bonds that dominate the index, which is the convexity tax of §5.9.

*Used in:* §5.2 and §5.9 (spread convexity and the third moment), §6.2 and Chapter 6-B (gamma), §8.3 (the discount-bond asymmetry), §10.6.1 (trend as a straddle), §21.5 (the loan's negative convexity under repricing), §23.5 (spread Greeks), App A §A.3 and §A.7.

## 4B.5 The Risk Report: DV01, CS01, DTS and the Hedge Ratio

Desk framing. A risk report turns derivatives into dollars, because a PM cannot add a modified duration to a key-rate duration to a CDS risky annuity, and can add dollars.

**DV01** is the dollar change in value for a one-basis-point *fall* in yield (positive for a long bond):

$$
\text{DV01} = -\frac{\partial P^{\text{dirty}}}{\partial y}\times 10^{-4} \times \frac{\text{Face}}{100} = D^{\text{mod}} \times P^{\text{dirty}} \times \text{Face} \times 10^{-6}.
$$

Per \$1mm of face, DV01 in dollars is simply $D^{\text{mod}} \times P^{\text{dirty}}$. The dirty price is the right one; App A's shortcut with the quoted price is close unless accrued is large. **CS01** is the same with $D^{\text{spr}}$ and a spread bump. For a fixed bullet the two coincide; for a loan CS01 dwarfs DV01; for a CDS, CS01 is the risky annuity times notional times a basis point (§6.8, §24.2). Signs follow App A §A.8: long credit is long CS01, and the rate term in a return is $-D\,\Delta y$.

> **Math, Gently.** *Percent, not basis points.* A stock at \$10 that moves a dollar has had a big day; a stock at \$100 that moves a dollar has had a quiet one. Same dollar, not the same event, and no equity desk would add the two moves as if they were. Spreads behave the same way. Ten basis points on a bond trading at 100bp over is a 10% move in its spread; ten basis points on a bond at 800bp is 1.25%. If spreads tend to move by similar *percentages*, which is roughly what the data say (§8.4), the first bond's ten basis points carry eight times the news of the second's, and a report that counts basis points has filed a shout and a whisper under the same heading. DTS counts in percent: multiply the spread duration by the spread, and a basis-point ruler becomes a percent ruler. The algebra takes two lines, next.

**DTS** rescales CS01 by the spread level. With $s$ in basis points, $\text{DTS} = D^{\text{spr}}\,s$, and if spreads move *proportionally*, $\Delta s = s\,x$ with relative change $x$, then

$$
\frac{\Delta P}{P} \approx -D^{\text{spr}}\,s\,x \times 10^{-4} = -\text{DTS} \times x \times 10^{-4}.
$$

When relative spread changes have similar volatility across bonds, which is the empirical finding behind §8.4, DTS is the unit of credit risk and CS01 is not (Law 3).

What the two reports said about the fallen angel in March 2020, one that it had become safer and the other that it had become almost four times riskier, is Figure 4-B.3; the replay of §4B.8 reads both reports aloud on the day it mattered.

![Figure 4-B.3: The same note in two risk units: DV01 (equal to CS01 for a bullet) fell 40% from 20 February to 23 March while DTS rose 3.8 times, because spreads were widening in percent rather than in basis points. Illustrative: the stylized 4.50% ten-year note per \$10mm face; DTS is modified duration times the G-spread in basis points (Table 4B.1, Listing 4-B.1).](assets/figures/ch04b_dv01_vs_dts.png)

**The hedge ratio.** To neutralize rate risk with an instrument $H$, hold $-\text{DV01}_{\text{bond}}/\text{DV01}_{H}$ of it per unit of bond. A par ten-year Treasury has $D^{\text{mod}} = a_{20}(y)$ by §4B.3, so its DV01 per \$1mm is $100\,a_{20}(y)$ dollars: \$924 at the 1.52% ten-year yield of 20 February 2020 and \$961 at 0.76% on 23 March (FRED, DGS10). The bond's DV01 per \$1mm was \$878 and then \$524. The hedge ratio went from 0.95 to 0.545: \$9.50mm of Treasuries per \$10mm of bonds in February, \$5.45mm a month later. A static hedge set in February was 74% too large in March by its own analytic measure, before anyone asked §8.2 what the empirical hedge ratio of a bond at 824bp is (smaller still, and possibly negative).

That division neutralizes rates with a Treasury. Swap the Treasury for a second credit and the same division becomes the central decision of a relative-value pod, the seat that is long one credit and short another so that only the view on the gap between them is left. Which duration goes on top of the fraction stops being a detail.

> **The Pair.** *Pair Book PB-03, before it opens: the arithmetic. Two generic issuers, A and B; every number is illustrative. When Dov Adler's pod at Vantress Capital Management (a fictional composite) opens PB-03 in Chapter 8 (§8.4), the names are Ford Motor Credit and GM Financial and the sizes are its own; the full comparison of rulers is §8D.3's.* **Thesis.** A's spread is too wide against B's for reasons particular to A, and it will tighten. **Legs.** Long \$40.0m of A at 380bp, spread duration 4.2; short B at 520bp, spread duration 4.6, borrowed. Both are treated as near par, so each leg's P&L is spread change times spread duration times notional. The short has three defensible sizes. Equal basis-point risk, DV01 against DV01 ($40 \times 4.2/4.6$), says \$36.5m. Equal DTS ($40 \times 4.2 \times 380/(4.6 \times 520)$) says \$26.7m. An empirical beta of 0.60 says \$21.9m. **What the hedge removes.** That depends on the ruler. If both spreads widen by the same 10% (A +38bp, B +52bp), the DTS pair loses nothing, the DV01 pair makes \$0.24m and the beta pair loses \$0.11m. **What idio remains.** If A alone tightens 15bp, every version makes \$0.25m: the thesis pays the same whichever ruler sized the short. If B alone widens 20bp, the pair makes \$0.34m, \$0.25m or \$0.20m, because the short leg's size *is* the ruler. **What leaks.** A parallel 50bp widening of both costs nothing under DV01, \$0.23m under DTS and \$0.34m under beta; no ruler is flat in every state. **What it costs to carry and to short.** Long A earns \$1.52m a year of spread; short \$26.7m of B pays away \$1.39m; at an assumed 75bp borrow fee the DTS pair runs at about −\$0.07m a year, roughly −17bp on the long, before a single basis point of convergence.

Theo had worked the three sizes on a pad, and Ines read the pad the way she reads a hand. "Fifteen basis points of thesis is a quarter of a million. Pick the wrong ruler on the wrong day and the market takes a quarter of a million back. The alpha is the size of the hedge-ratio error." She handed the pad back. "That's every pair you'll ever see. Know which ruler you used, and which day it's wrong on."

> **Ways This Blows Up.** Finite-difference risk is only as good as the price under it. A price produced by a yield solver with a tolerance of $10^{-6}$ and bumped by one basis point gives a DV01 with about 1% noise, and a convexity that is pure noise. Use the analytic derivatives of §4B.2 for bullets, solve to $10^{-12}$ when you must solve, use a 10bp bump for second differences on a lattice, and check that the key rates sum to the parallel number before the report goes out.

*Used in:* §1.3 (the inventory term in the bid equation), §8.4 and §9.2 (DTS as beta), §8.6 (the hedge matrix in DV01 terms), §10.3 (volatility scaling is DTS scaling), §12.5 (DTS-structured covariance), §19.2–§19.4 (basket risk and the lump hedge), §24.4 (basis carry per DV01), App A §A.5 and §A.8.

## 4B.6 One Curve, Eight Spreads

Desk framing. Every spread is the answer to one question, *how much more than the reference curve does this bond pay?*, asked with a different reference curve, a different idea of "pay," and a different compounding. With the curve built once, the eight answers are short.

### The curve

A zero curve is a function $z(t)$ with discount factors $d(t) = e^{-z(t)\,t}$. Markets quote *par* yields, so the curve is bootstrapped.

> **Math, Gently.** *Bootstrapping is peeling.* The market will not tell you the price of a single \$1 cheque due in two years; it tells you the yields of whole bonds, which are bundles of cheques. So you peel them, shortest first. A one-year par bond at 4% (annual coupon) is one cheque of \$104 priced at \$100, so a \$1 one-year cheque is worth $d(1) = 100/104 = 0.9615$. The two-year par bond at 5% is a \$5 cheque in one year and a \$105 cheque in two. You already know what the first cheque is worth, $5 \times 0.9615 = 4.81$, so peel it off: the remaining $100 - 4.81 = 95.19$ is the value of the \$105 cheque, and $d(2) = (1 - 0.05 \times 0.9615)/1.05 = 0.9066$. In continuous compounding that is a two-year zero rate of $z(2) = -\ln(0.9066)/2 = 4.90\%$. Each new bond adds exactly one unknown, and each earlier peel has already removed the rest. The general rule is the next display.

On a grid $t_n = n/f$ with par yields $c_n$ (interpolated from quoted tenors), a par bond maturing at $t_n$ prices to one, $\sum_{k \le n} (c_n/f)\,d(t_k) + d(t_n) = 1$, which solves forward:

$$
d(t_n) = \frac{1 - (c_n/f)\sum_{k<n} d(t_k)}{1 + c_n/f}, \qquad z(t_n) = -\frac{\ln d(t_n)}{t_n}.
$$

The desk keeps two curves and always names which: Treasury (for G, Z and excess returns) and SOFR swaps (for I, asset swaps and anything a funded investor hedges).

### The eight

*Wednesday 7 October, 6:30 a.m.* Theo had put his card face down under Ines's coffee cup at 6:25 (it is graded in §4B.8). Kaz was already at the whiteboard with the vendor's six column names down the left-hand side and two more added in a different colour, rebuilding each one from the note's list and a single Treasury curve. Theo, who had spent the previous evening failing to find a definitions tab, decided to become one. For each column he asked the question it answered, and wrote Kaz's answer next to it.

**G-spread.** "What does it pay over the government?" The answer is one subtraction: $G = y - y^{\text{TSY}}_{\text{par}}(T)$, the bond's yield minus the Treasury par yield interpolated at its maturity. That is its appeal and its flaw: it compares a 4.50% coupon's yield with a different-coupon par bond's yield and ignores the curve's shape between today and $T$.

**I-spread.** "Same question, a different government?" Nearly: the same subtraction against the par swap rate $y^{\text{SOFR}}_{\text{par}}(T)$. The difference $I - G$ is minus the swap spread at $T$; it is a fact about the curves, not the bond.

**Z-spread.** "If I lifted the whole Treasury curve by one number until the bond priced, what's the number?" That is Z, the constant added to every zero rate that reprices the bond:

$$
P^{\text{dirty}} = \sum_k \text{CF}_k\, e^{-(z(t_k) + Z)\,t_k}.
$$

Linearize around the yield: $y^{\text{cc}} - Z \approx \sum_k \omega_k\,z(t_k)$ with duration weights $\omega_k \propto t_k\,\text{CF}_k e^{-y^{\text{cc}} t_k}$. The yield is the Z-spread plus a duration-weighted average zero rate. So $Z - G$ is (to first order) the par Treasury's weighted average zero minus the bond's. On an upward-sloping curve a high-coupon, high-yield bond puts its weight earlier than the low-coupon Treasury, its average zero is lower, and $Z > G$. Invert the curve, as it was for most of mid-2022 to mid-2024, and the sign flips. On a flat curve, Z in the bond's own compounding equals G exactly, and Z in continuous compounding differs only by the compounding.

**Asset-swap spread (par-par).** "What does a funded buyer earn over SOFR, once the rate risk is swapped away?" Kaz did not answer that one from memory, and reached for the cleanest definition on the shelf, Schmid's.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "Basically, an asset swap is a synthetic structure that allows an investor to buy a fixed rate bond and then hedge out the interest rate risk by swapping the fixed payments to floating. The investor keeps the credit exposure to the fixed rate bond."
>
> **Annotation.** The package has a price, and the price is the spread. In the par-par version the investor pays 100 for a bond worth $P$ and swaps its coupons for SOFR plus $A$. Setting the package's value to zero gives the formula below, and makes visible what the definition leaves out: when $P$ is far from par, the investor has also made (or received) an upfront payment of $100 - P$ to the swap counterparty. That loan carries counterparty and funding risk, which is why ASW and Z diverge for discount bonds and why the March 2020 basis trades of §24.4 cared which one they used.

With $P^{\text{sw}}$ the bond's value on the swap curve and $\mathcal{A}$ the annuity on its coupon dates (both defined just below), the package is worth zero at

$$
A^{\text{par}} = \frac{P^{\text{sw}} - P^{\text{dirty}}}{100\,\mathcal{A}}, \qquad A^{\text{mkt}} = A^{\text{par}}\,\frac{100}{P^{\text{dirty}}} .
$$

The market-value variant puts the floating leg on the dirty price instead of par. For a bond at 70 the two differ by a factor of 1.4. "So the par version," said Theo, "is the market-value version plus a loan to the swap dealer that nobody mentions." Kaz wrote *loan* on the board, then *of $100 - P$*, and underlined it.

#### The Full Derivation: valuing the package

Value the package per 100 at inception. The investor pays 100 and receives the bond ($P$). The swap's floating leg is worth $100\,(1 - d(T)) + 100\,A\,\mathcal{A}$ on the swap curve, where $\mathcal{A} = \sum_k \alpha_k d(t_k)$ is the annuity on the bond's coupon dates; the fixed leg paid away is $100\,c\,\mathcal{A}$. Let $P^{\text{sw}} = \sum_k \text{CF}_k d(t_k)$ be the bond's value on the swap curve. Then $P - 100 + 100 - 100\,d(T) + 100A\mathcal{A} - 100c\mathcal{A} = P - P^{\text{sw}} + 100\,A\,\mathcal{A} = 0$, which is the first formula above; the second scales the floating leg to $P$ instead of 100.

#### The rest of the eight

**Discount margin.** "What does a loan pay over its base rate, if the base rate stays where it is today?" For a floater or loan paying $b + m$ (base rate plus contractual margin), DM is the spread over the base rate that reprices it, under the convention that the base rate stays at today's level. On a reset date, a floater paying $b + m$ and discounted at $b + m$ is worth par by backward induction (each period's coupon is exactly the period's discount), so $\text{DM} = m$ at a price of 100, and to first order

$$
\text{DM} \approx m + \frac{100 - P}{100\,a(T)},
$$

with $a(T)$ the annuity at $b + \text{DM}$: the loan form of the premium identity, and (21.2) of §21.1 solved for $s$. The Larkspur Foam 2029 first-lien term loan of Chapter 13 pays SOFR + 375bp. At 97, with a flat 4.00% base rate and the common three-year-life convention *(illustrative)*, its DM is about 490bp. At the 84 mark of the morning of the headline it is about 1,040bp, at which point the desk stops quoting DM and starts quoting recovery. State whether the floor is priced: a floor is an option the lender owns, and the flat-forward convention values it at intrinsic only.

> **View From Another Seat.** *The CLO manager.* To a CLO manager the Larkspur loan at 97 is not a 490bp discount margin. It is 375bp of contractual margin, which is what the vehicle's weighted-average-spread test counts, plus three points of par the vehicle builds by buying below 100, which is what its overcollateralization tests count. DM is the number for choosing between two loans, not for passing the tests. The SOFR floor is an option the vehicle owns, and the flat-forward convention values it at intrinsic, which with the base rate well above any floor is nothing. At 84 the question changes. The manager is no longer asking what the spread is. It is asking whether a downgrade will put the loan into the CCC bucket, whose excess above the indenture's limit (commonly 7.5% of the portfolio) is carried at market value instead of par in the overcollateralization test, and what the loan does to the portfolio's weighted-average rating factor. A loan can be cheap on DM and expensive to own inside a structure. Section 21.1 prices the loan; §21.4 runs the tests.

**Yield-to-worst.** "What is the least I earn if the issuer does whatever hurts me most?" The lowest yield over maturity and every call date, each at its call price: §4B.7, because it needs a call schedule.

**OAS.** "And what is left once somebody has priced the issuer's option?" The spread over the curve that reprices the bond *after* valuing its options on a rate model: §4B.7, because it needs a lattice.

**Par CDS equivalent (PECS).** "What would the CDS have to be?" Kaz's answer needed one word Theo had not met yet. A hazard rate $\lambda$ is a default intensity, the per-year chance of the jump to default for a bond that has survived so far, so that it survives a year with probability $e^{-\lambda}$, about $1 - \lambda$ when $\lambda$ is small; Chapter 6 builds it properly. Find the flat hazard $\lambda$ that reprices the bond with recovery of face $R$ (the formula of §4B.2, from §6.6.3), then read the par CDS spread off the same $(\lambda, R)$ with the legs of §6.8 and §24.2:

$$
P^{\text{dirty}} = \sum_k \text{CF}_k d(t_k)e^{-\lambda t_k} + 100R\!\int_0^{T}\!\lambda e^{-\lambda u}d(u)\,du, \qquad s^{\text{PECS}} = \frac{(1-R)\int_0^T \lambda e^{-\lambda u}d(u)\,du}{\text{RPV01}(\lambda)} \approx \lambda(1 - R).
$$

PECS is the bond spread that a CDS basis should use (App A §A.5), and it exceeds Z for a discount bond for a reason worth one line: Z is a loss rate per unit of *price*, a CDS spread is a loss rate per unit of *par*, and a bond at 70 with recovery 40 loses 30 of its 70 at default, not 60 of 100. Schmid makes the same point from the hedge's side.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "A default swap is a par product: it does not completely hedge the loss on an asset that is currently trading away from par. If the asset is trading at a discount, a default swap overhedges the credit risk and vice-versa."
>
> **Annotation.** Two consequences on a 2026 desk. For *valuation*, compare a discount bond with CDS only through PECS, or the convention masquerades as a basis. For *hedging*, the jump-to-default-neutral notional is $(P - R)/(1 - R)$ per unit of face (derived in §24.3), so \$10mm of the fallen angel at 70.73 with $R = 40\%$ needs about \$5.1mm of protection, not \$10mm. The departure from Schmid: $R$ is itself random and is now a property of the transaction (§5.5, §5.6), so PECS has a recovery delta that the desk must report next to it (Law 7).

By half past seven the whiteboard was the definitions tab the vendor file had lacked, and Theo photographed it before anyone could wipe it. Kaz turned it into a table.

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

Theo had spent six years on the other side of these redemptions, and he had an objection. "None of the issuers I worked for called a bond because rates fell. They called to get out of a covenant, or to refinance ahead of a sale, or because a buyer wanted the debt gone at closing. The rate saving was the last bullet on the slide."

"Then your issuers had a reason to call that isn't on anybody's tree," said Ines. "Put them on a range anyway. Just remember the range was drawn by someone who hasn't met them."

"Everything you listed ends up in the OAS," said Kaz, "as residual. The tree prices the rate reason. Whatever is left over gets called a spread."

"So an OAS is half a rate model and half my old job."

"That," said Kaz, "is the most honest definition of a residual I've heard on this floor." Veronesi says the same thing in a textbook's voice in the extraction below the lattice.

### A lattice small enough to do by hand

Take a three-year annual-pay 9% bond, callable at 101 (ex-coupon) at years one and two, on a binomial short-rate tree with risk-neutral probability $\tfrac12$ and spread $s$ added to every node's rate. To keep the hand arithmetic honest, discount with simple annual rates, $1/(1 + r + s)$, on a tree that is not fitted to any curve: $r = 4\%$ today; 5% or 3% at year one; 6%, 4% or 2% at year two. Work backward at $s = 5\%$.

At year two each node has one payment left, 109: values $109/1.11 = 98.20$, $109/1.09 = 100.00$ and $109/1.07 = 101.87$, which the issuer calls at 101.00. At year one, the up node is worth $\tfrac12(98.20 + 9) + \tfrac12(100.00 + 9)$ discounted at 10%, or 98.27, and is not called; the down node is worth $\tfrac12(109) + \tfrac12(110)$ at 8%, or 101.39, and is called at 101.00. Today: $\tfrac12(107.27) + \tfrac12(110.00)$ at 9% gives **99.67**. The same tree with no call gives 100.03. The call is worth 0.36 points.

Now invert. If the market price is 99.67, the OAS is 500bp *by construction*: it is the $s$ at which the callable tree matches the price. The Z-spread is the $s$ at which the *non-callable* tree matches the same price, about 514bp. The call costs the holder 14bp a year, and $\text{OAS} = Z - (\text{option cost in bp})$, which is App A's "$\text{OAS} \le Z$ for callables" with the gap computed instead of asserted.

### The production lattice

> **Math, Gently.** *What "risk-neutral" means, on one branch.* The ½ on every branch of these trees is nobody's forecast. Here is why. Take a one-step tree: the one-year rate is 4% today and will be 6% or 2% next year, and the market prices a \$100 cheque due in two years at 92.49. At year one that cheque is worth $100/1.06 = 94.34$ if rates went up and $100/1.02 = 98.04$ if they went down. Weight the branches ½ and ½, discount at today's 4%, and you get $\tfrac12(94.34 + 98.04)/1.04 = 92.49$, the market's price. Weight them 70/30 because you are sure rates are going up and you get $(0.7 \times 94.34 + 0.3 \times 98.04)/1.04 = 91.78$, and your tree now disagrees by 0.71 with a bond anyone can buy. A tree that misprices the bonds you would hedge with misprices every option built from them, and the gap is a free lunch for whoever trades against the tree. So the probabilities are chosen to make the tree agree with the curve, and an option priced on it is priced by the cost of building it out of bonds, whatever anyone believes about rates. That is all "risk-neutral" ($\mathbb{Q}$) means: the probabilities that make prices consistent, not the ones that describe the world ($\mathbb{P}$). The production tree does the same fitting the other way round, holding the ½ fixed and moving the rates, next.

Replace the toy with Ho–Lee: short rates $r_{i,j} = \theta_i + \sigma\sqrt{\Delta t}\,(2j - i)$ at step $i$, node $j = 0, \dots, i$, with normal volatility $\sigma$ (decimal per root-year) and continuous discounting $e^{-(r_{i,j} + s)\Delta t}$. The drifts $\theta_i$ are fitted, one step at a time, so that the tree reprices every zero-coupon bond on today's curve; the fitting needs no root-finding and is the derivation just below. Price backward from maturity: at each node the continuation value is $e^{-(r_{i,j}+s)\Delta t}\,\tfrac12(V_{i+1,j} + V_{i+1,j+1})$; on an exercise date the issuer replaces it with $\min(\text{continuation}, K(t_i))$; then add the coupon paid at $t_i$. The OAS is the root in $s$ of $V_{0,0}(s) = P^{\text{dirty}}$, unique because $V_{0,0}$ is decreasing in $s$.

#### The Full Derivation: fitting the tree

With Arrow–Debreu prices $Q_{i,j}$ (the value today of \$1 paid at node $(i,j)$, starting from $Q_{0,0} = 1$) and $x_{i,j} = \sigma\sqrt{\Delta t}(2j-i)$, the step-$i$ drift is set so that the tree's price of a zero maturing at step $i+1$ equals the curve's:

$$
\sum_j Q_{i,j}\,e^{-(\theta_i + x_{i,j})\Delta t} = d\big((i+1)\Delta t\big) \;\Longrightarrow\; \theta_i = -\frac{1}{\Delta t}\ln\frac{d\big((i+1)\Delta t\big)}{\sum_j Q_{i,j}\,e^{-x_{i,j}\Delta t}},
$$

then propagate $Q_{i+1,k} = \tfrac12 Q_{i,k}e^{-r_{i,k}\Delta t} + \tfrac12 Q_{i,k-1}e^{-r_{i,k-1}\Delta t}$. Each step's $\theta_i$ is a closed form in quantities already known, so no root-finding is needed: the tree is peeled forward exactly as the curve was bootstrapped in §4B.6.

#### The four asserts

Kaz wrote four identities as asserts before the lattice was allowed to price anything real, on the theory that a tree you cannot test is a tree you cannot trust. Each is one of the tests in §4B.9:

1. **No option, no adjustment.** Without a call, the value of a cash flow at $t_n$ is $e^{-s t_n}\sum_j Q_{n,j} = e^{-s t_n}d(t_n)$, so the OAS of a bullet equals its continuous Z-spread exactly.
2. **Zero volatility is yield-to-worst.** As $\sigma \to 0$ the path is deterministic, backward induction picks the issuer's best date, and the OAS equals the spread to worst. YTW is the zero-volatility OAS written as a yield.
3. **Curve shift equals spread shift (in Ho–Lee, with fixed strikes).** A parallel shift $h$ of the zero curve shifts every $\theta_i$ by exactly $h$ (substitute $d(t)e^{-ht}$ above and induct), so it is the same perturbation as $s \to s + h$, and $D^{\text{eff}} = D^{\text{OAS}}$. In a lognormal tree (Black–Derman–Toy, Black–Karasinski) the identity fails, and the desk stores both numbers (the `oasd` of §19.2 is the second).
4. **Volatility lowers OAS.** With any exercise and $\sigma > 0$ the callable is worth less than the bullet at the same spread, so $\text{OAS} < Z$, and more volatility makes the gap wider.

The first one failed at 1:10 on Wednesday morning. A plain bullet, no call anywhere, came back from the lattice with an OAS three basis points wider than its continuous Z-spread: three basis points of option cost, with the wrong sign, on a bond that had no option. Kaz spent half an hour suspecting the Arrow–Debreu propagation, which was innocent. The culprit was a convention. The tree charged the spread one step at a time as a simple discount, $1/(1 + s\,\Delta t)$, while the Z-spread solver used $e^{-s t}$, and the two differ by about $\tfrac12 s^2 \Delta t$ a year: at 804bp on a monthly grid, $\tfrac12 \times 0.0804^2/12 \approx 2.7$bp. Same compounding gap as the cold open's G and Z, one level down, inside a loop. The fix was one line. The assert stayed, and it is the reason the OAS row of Table 4B.1 can be read as Z and not merely compared with it.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.467:* "It is also important to realize that the size of the OAS depends on the model used to compute it: It is possible that different term structure models may generate different OAS, in the same way they generate different values of options even when using the same inputs."
>
> **Annotation.** OAS is a residual, not an observation, and on a credit desk the residual contains three things Veronesi's Treasury callable does not: default risk (the lattice is a riskless tree with a spread on top), liquidity, and whatever the model gets wrong about the issuer's call behaviour (issuers call for covenant relief and M&A, not only for rates). So an OAS series is model output, and a backtest on it has a model inside it (Law 11). When Chapters 8–12 regress on OAS, they are using the index provider's model; when this desk computes OAS, it states $\sigma$ and the tree.

### Negative convexity

Near the call price the issuer's option binds and the callable's price flattens toward the strike as rates fall; Veronesi's Treasury callable shows the same thing, where "the bond price has to converge to the call price ($100) as interest rates decline" (Veronesi_Fixed_Income_Securities p.464). Effective convexity turns negative there, and far from the call, where the option is worthless, the two curves merge and convexity is positive again.

```text
Sketch 4B.1 (schematic, not a numbered figure). Price against the level of rates (or spreads) at fixed OAS.

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

That flattening is what a call costs when its strike is a fixed price on a schedule. A make-whole call is struck somewhere else entirely, at a price that moves with the curve, and the difference decides whether the option is worth anything at all.

### The make-whole

A make-whole call lets the issuer redeem at $K^{\text{MW}} = \max\!\big(100,\ \text{PV of remaining flows at the Treasury curve} + m_w\big)$, with a make-whole spread $m_w$ such as 50bp. On the lattice, compute $W_{i,j}$, the remaining flows valued at $r + m_w$ by a parallel backward induction, and set $K^{\text{MW}}_{i,j} = \max(100, W_{i,j})$.

*Proposition.* If $s \ge m_w$, the make-whole is never exercised. *Proof.* At every node the callable's continuation value is at most the non-callable value at spread $s$, which is at most the non-callable value at spread $m_w$ (positive cash flows, higher discount), which is $W_{i,j} \le K^{\text{MW}}_{i,j}$. So $\min(\text{continuation}, K^{\text{MW}}) = \text{continuation}$ everywhere. $\square$

A make-whole is a call struck at the issuer's own credit spread equal to $m_w$, so it is out of the money for every issuer that trades wider than T+50, which is every high-yield issuer and every fallen angel. It is worth nothing to price and a great deal in three places: a merger refinancing (entry 3 of the table in §15.1), a covenant defeasance, and a bankruptcy claim, where whether the make-whole is allowed was the Hertz fight (§16.6).

> **Trend Watch: The reference curve moved under every spread, 2018–2026.** *What changed:* the New York Fed began publishing SOFR on 3 April 2018; CME and LCH switched discounting of cleared US dollar swaps to SOFR in October 2020; the ARRC recommended CME Term SOFR on 29 July 2021, and it became the base rate of new leveraged loans; the USD LIBOR panel ended after 30 June 2023; US corporate settlement moved from T+2 to T+1 on 28 May 2024. The Treasury curve did its own work: the ten-year constant-maturity yield was 1.52% on 20 February 2020, 0.76% on 23 March and 0.66% on 30 June (FRED, DGS10), and the 2s10s curve was inverted for most of July 2022 to August 2024 (approx.; FRED, T10Y2Y), which flipped the sign of $Z - G$ for high-coupon bonds. *What it means for the desk:* an I-spread, ASW or DM series that spans 2019–2024 changes its reference curve in the middle; that is a structural break made of convention, and a factor or trend signal (Chapters 9, 10) will read it as a market move unless the panel is rebuilt on one curve. Accrued interest shrank by one business day on every trade in May 2024, and DM's "flat forward" assumption now runs on term SOFR, not three-month LIBOR.

*Used in:* §5.2.2 (the price cap and negative convexity), §5.9 (the convexity tax), §12.2 (YTW as the yield input), §15.1 (make-whole and call economics in mergers), §16.6 (the Hertz make-whole), §19.2 (`oasd`, `oas`), §21.5 (the loan's call as a repricing hazard), App A §A.5.

## 4B.8 Case Study: The Fallen Angel, Repriced in Every Measure

#### Long Scene: One Month, Six Rulers, One Pot

*The cold open's replay, continued on Wednesday 7 October 2026 from 7:40 a.m. The tape is real, cut at 23 March 2020 and released one date at a time as Ines chose; the Treasury yields, the ratings, the Federal Reserve's announcements, the Ford deal and the market-wide figures are sourced in the text. The bond is the cold open's stylized composite, and the desk's position, its P&L and every line of dialogue are invented (illustrative).*

#### Beat 1: The First Hour Is Reconciliation

*Quant-Shop Life, a fictional composite: the first hour of a systematic credit desk.* Kaz had either not gone home, or gone home and come back in the same sweater, which on this desk amounts to the same thing. Since the whiteboard session of §4B.6 the two of them had rebuilt all six columns from one object: the note's twenty coupons, priced against a Treasury curve held flat at each date's ten-year par yield (FRED, DGS10). The flat curve is a deliberate stylization. It sets the shape term in $Z - G$ of §4B.6 to zero, so any gap left between two columns has to be a convention. (Exercise 2 puts the real curve back.)

The first hour went where first hours on a quant desk go, which is reconciliation. Kaz's Z-spread for 23 March sat three basis points from the vendor's. Three basis points is nothing on a bond at 804 and everything to a test suite, because a model that cannot reproduce the vendor's number cannot tell you which of the two numbers is wrong. Theo opened the methodology PDF he had bookmarked on Tuesday night, sixty-two pages with a cover in a font nobody uses any more. Forty minutes later the reasons were on the whiteboard: the vendor fits a smoothed Treasury curve and values the bond for settlement two days later, with accrued. Both choices are defensible, both are on page 41 of a methodology PDF nobody on the desk had opened since 2017, and neither is visible in a column called `z_spd`. Theo wrote them on a sticky note, *curve: smoothed; settle: T+2; accrued: yes*, and stuck it to the bezel under Ines's Post-it. It was, he pointed out, the definitions tab.

Then Kaz checked the thing every replay checks before anything else: that the vendor's number for 23 March 2020 was the number the vendor had actually published on 23 March 2020, and not a later restatement wearing an old date. Vendors do restate, and a backtest run on restated history has a time machine in it. Market makers describe the cure in public; on Jane Street's *Signals and Threads* (episode 29, 2 September 2026) an engineer explains the firm saving its market data together with the time it was received, so that a vendor's later correction cannot quietly rewrite what the desk knew. Ines's desk has done the same with every vendor file since before Kaz arrived. The archived file from the morning of 24 March 2020 said 804. Nobody cheered, because this is not a cheering kind of task. Kaz ticked a box and moved on.

Mags had watched the whiteboard fill. "My first year, I'd have called the salesman and he'd have said 'call it eight hundred.' Same answer, and nobody lost a night's sleep." She paused. "Mind you, he was lying about something else."

#### Beat 2: The Table, and the Rows That Are Only Rulers

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

Start with the gaps that would exist on a day when nothing happened. G and Z differ by 2.5bp in February, 19.5bp in March and 7.3bp in June, and on a flat curve all of it is compounding, which grows with the square of the level. The two asset swaps differ by exactly $100/P$: 0.92 at the premium, 1.41 at the trough. PECS sits *below* Z in February and *above* it in March, because a CDS spread is a loss rate per unit of par, Z one per unit of price, and the bond crossed par on the way down (§4B.6). The OAS row equals Z on all three dates, and not by rounding: the make-whole is struck at T+50, the bond never traded tighter than 196bp, and by the proposition of §4B.7 a make-whole is never exercised while the spread exceeds the make-whole spread. The vendor's `oas` column was Z with a more expensive name.

Mags, who regards any number with "adjusted" in its name as a number somebody wanted to be different, was briefly delighted. "The one time an adjustment was honest, it was zero."

"Make whole *whom*?" asked Kaz, who was reading an indenture for the first time and had reached the redemption section. "Is it an insurance term?"

"The bondholder," said Theo. "It's the only clause in the indenture that apologizes in advance."

> **Math, Gently.** *Six rulers, one length.* G, Z, the two asset swaps and PECS are rulers with different units and zero points. On any one day they rank bonds almost identically, which is why ROBO found them "highly correlated." Their *changes* and *ratios* are another matter. Warm a room from 10°C to 20°C and Celsius says the temperature doubled; Fahrenheit says 50°F to 68°F, up 36%. Nothing got twice as hot. In Table 4B.1 the same bond's spread multiplied by 3.3 on the par asset-swap ruler and by 5.1 on the PECS ruler, in the same month. For compounding the conversion is one line of Taylor: $\ln(1+x) \approx x - x^2/2$, so $y^{\text{cc}} = f\ln(1 + y/f) \approx y - y^2/(2f)$, and at $y = 9\%$ with $f = 2$ the gap is $0.09^2/4 \approx 20$bp. The full version is in §4B.2.

Every ruler agrees that something enormous happened between 20 February and 23 March: the note's spread rose by roughly six percentage points (market-wide, about 250bp for investment grade and 550bp for high yield, by the count in New York Fed Staff Report 986). They disagree about *how* enormous. G rose 626bp, Z 609, the par-par asset swap 471, the market-value asset swap 768, PECS 759: a 300bp disagreement about the change, which is the left-hand side of every regression in Part III and the input to every trend signal in Chapter 10. In relative terms, which is how DTS (Law 3) measures, the multiplier runs from 3.3 to 5.1, so the same bond's measured volatility depends, by half, on which column was loaded. Figure 4-B.4 shows the five rulers on all three dates.

![Figure 4-B.4: On 23 March the rulers for one bond sit about 280bp apart (left), and from 20 February the spread widened by 3.3 times on the par-par asset swap but 5.1 times on PECS (right). Illustrative: the stylized 4.50% ten-year note of Table 4B.1 on a flat Treasury curve (FRED DGS10); the OAS equals Z on all three dates.](assets/figures/ch04b_five_rulers.png)

#### Beat 3: 23 March, the Card, and the Rows That Moved

Ines released nothing new. "It's 23 March," she said. "The Fed has said it will buy investment-grade bonds and hasn't bought one. S&P still has Ford at investment grade. Theo's card is under my coffee. Kaz, Mags, here's yours, in the replay's terms." She dealt two cards.

> *You hold \$10mm of the note and \$9.5mm of ten-years short. Write three things: what you do with the hedge, what you do with the position, and which number you report to the PM.*

Kaz wrote: *Hedge: re-size to the analytic ratio, 0.545; buy back \$4.05mm. Position: hold. Report: CS01, \$5,236 a basis point.* "It's what the durations say," Kaz said. "Both of them."

Mags wrote three words and then said the rest aloud. *Off. More. Price.* "At 824 a ten-year Treasury isn't a hedge for this bond. It's a second opinion about a different bond. The only question at 824 is fallen angel or falling knife, and that depends on who's selling."

"Then ask it," said Ines, who does not write cards in her own replays. "Who's on the other side of the index exit at the end of the month?" She did not answer it. Chapter 1 had (§1.8.2): a rulebook seller, an index fund obliged to sell a bond the day it stops being investment grade and knows nothing about Ford, which is the best kind of seller to buy from if you can carry the bond until the rule-followers are done.

Theo turned his own card over. He had written it at 6:25, before the whiteboard and before page 41: *1. Z, with its definition attached. 2. Not CS01: it says the bond got safer. Something that counts in percent. 3. Keep the hedge, but find out why it lost money.* Underneath, in different ink, he had answered the line his card had not asked: *Position: hold. Article III.* Kaz, who had read Article III for the first time an hour earlier, nodded. "The make-whole. Struck at T+50, so at 824 it's worthless, by the proposition. Nobody can call the upside away."

"That's why I hold," said Theo.

Ines graded the cards against the P&L, the one row on which money moved. The note lost 37.65 points. Split it as §4B.4 did, around February's $D^{\text{mod}} = 8.11$, $C^{\text{mod}} = 78.0$ and $P = 108.38$: the 76bp Treasury rally contributed $+6.7$ points; 626bp of spread widening contributed $-55.0$; convexity on the 550bp total yield move gave back $+12.8$; and the residual, mostly the third-order term, was $-2.1$. An explain without its residual line claims a precision it does not have. Figure 4-B.5 lays the four lines out as a waterfall.

![Figure 4-B.5: The note's 37.65-point loss from 20 February to 23 March, explained from February's duration and convexity: a 6.7-point gain from the Treasury rally is swamped by a 55.0-point loss from spread widening, convexity gives back 12.8, and 2.1 points are left as residual. Illustrative: the stylized 4.50% ten-year note, with the explain function of Listing 4-B.1 and the real DGS10 moves of Table 4B.1.](assets/figures/ch04b_pnl_explain_waterfall.png)

Then the hedge. In February the analytic ratio of §4B.5 said to short \$9.5mm of the ten-year against \$10mm of the note. The ten-year rallied 7.3 points, so the hedge *lost* about \$0.69mm while the note lost \$3.76mm. It did exactly what it was sized to do, against a rate move with the opposite sign from the one that mattered.

ROBO had been right on Tuesday: the six spreads were highly correlated with each other. Nobody had asked it about the correlation that cost money, the one between the Treasury yield and the spread, and in March 2020 that one was sharply negative.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.191:* "If this correlation is negative, the empirical duration would be lower than the analytical one and may even end up being negative."
>
> **Annotation.** March 2020 is that sentence with numbers in it. Treasury yields fell while the note's spread rose eight times as far, so $\rho_{y,s}$ was sharply negative and the analytic hedge pointed the wrong way. Ben Dor's Table 7.1 (p.192, 1998–2009 data) puts the Ba bucket's empirical hedge ratio at maximum spreads at −0.26: the right hedge at 824bp was a small *long*, or nothing. The modern departure: the correlation is a regime, not a constant. In 2022 it flipped, and "no hedge" lost on rates and spreads together (§8.7). The desk reports $D^{\text{mod}}$ and hedges with the rolling empirical duration of §8.2, and shows both.

So the hedge line of every card could be graded. Kaz's re-size to 0.545 was right by the analytic measure of §4B.5, under which the February hedge was 74% too large, and wrong by Ben Dor's, under which the right hedge at 824 was a small long or nothing. Mags's *off* was right. Theo's *keep the hedge* was wrong, and his *find out why it lost money* was the right question, the one §8.2 spends a chapter on.

"Before anybody tapes *no hedge* to a monitor," Mags said, "in March rates fell because everyone was frightened, and spreads rose for the same reason. In 2022 rates rose because of inflation, and spreads rose anyway. Same hedge, opposite answer. Chapter 8 has the bill" (§8.7).

The number for the PM was graded against the two risk reports for the same position. Per \$10mm, DV01 (equal to CS01 for a bullet) had fallen from \$8,785 on 20 February to \$5,236 on 23 March, down 40%; DTS, using $D^{\text{mod}}$ and the 198bp and 824bp G-spreads, had gone from 1,605 to 6,100, up 3.8 times. The CS01 report said the position had become safer. The DTS report said it had become almost four times riskier. Both were arithmetically right, and only one described a market in which spreads were moving in percent, which is what the cold open's "per basis point it got less risky" was missing (Figure 4-B.3). Kaz's card reported the first. Theo's line 2 described the second without knowing its name. Mags's *price* was right for a different reason: at 70.73 the note sat on the boundary below which every spread stops being worth quoting, and the table at the end of this section says so in its last row.

The position line was graded by the tape, which the next beat runs to June: *hold* and *more* both made money, and *more* made more. Theo's line 1 got the one grade nobody argued with: the definition attached to Z had been worth forty minutes of the morning, and the column without it would have carried an unexplained gap into every backtest the desk ran on it.

The reader's card, from the cold open, is graded the same way. A card that kept the hedge because the duration column said so made the February trade twice. A card that took the hedge off because Treasuries always rally in a panic won in 2020 and lost in 2022, for the same reason. A card that said *price* for the column, *DTS* for the risk line and *it depends on why rates are moving* for the hedge would have come back from Ines with nothing written on it, which on this desk is full marks.

#### Beat 4: Rows That Became Prices Again

Ford was an extreme of a pattern, not an exception to it. Downgrades out of investment grade in the first months of 2020 exceeded the total for the whole of the 2008–09 crisis, by the count in a New York Fed post (Liberty Street Economics, 16 February 2022), and across 1,188 fallen-angel bonds the median OAS over BBB went from 56bp a year before the downgrade to 278bp in the downgrade month (QML Solutions, "Fallen Angels Part 2: Forced Selling and Recovery," 17 December 2025). The stylized note's 824 was the far tail of that distribution, on the worst day of the worst month.

The rest is the tape, which a backtest cannot see unless somebody writes it down. The Federal Reserve announced its corporate credit facilities on 23 March, the table's middle column, before buying a single bond. S&P cut Ford to BB+ on 25 March; Moody's had rated it Ba1 since September 2019, so with two high-yield ratings Ford's bonds left the investment-grade index at the month-end rebalance (§1.8.2). On 9 April the Fed extended its facilities to issuers that had been investment grade on 22 March, which covered Ford. And on 17 April Ford came to the high-yield market itself.

Ines released April one date at a time. At 9 April Kaz redrew the absorber line on Chapter 1's graph and moved it across the boundary into high yield. At 17 April she put a single headline on the screen and said nothing, and Theo read it twice. "That's the first number this month that came with its definition attached," he said. "Par, a coupon, a size. No curve."

> **View From Another Seat.** *The issuer.* On 17 April 2020 Ford priced \$8bn of unsecured notes in three tranches: \$3.5bn of three-year notes at 8.50%, \$3.5bn of five-year at 9% and \$1bn of ten-year at 9.625%, the ten-year after being marketed at around 11% (Bloomberg, via BNN Bloomberg, 17 April 2020). From the treasurer's seat, none of the six columns exists. A bond sold at par has $c = y$ (§4B.2), so the coupon *is* the yield, and the yield is ten years' cost of capital, more than double the old 4.50% coupon. For the desk it was the cleanest spread observation of the month: no curve, no compounding convention, no recovery assumption, and \$8bn changed hands at it. The move from talk to print, about 140bp on the ten-year, measured demand in the one unit nobody argues with.

By 30 June the stylized note was back at 92.39 and 484bp over, and the rulers had drawn back together, as they do when price returns toward par: the compounding gap fell with the level, $100/P$ fell toward one, and PECS and Z converged because price and par did.

> **View From Another Seat.** *The life insurer and the bank desk.* A life insurer holding the note at amortized cost saw none of 23 March in its statutory income. Its number was the rating: the move from an NAIC 2 to an NAIC 3 designation multiplied the capital held against the position, and its "spread" was book yield over the liability's crediting rate. It sold, if it sold, over quarters, into the June column (§1.8.2). A bank's credit-trading desk writes its limits in CS01, and the CS01 report showed 40% less risk on 23 March than in February, freeing limit on the day bid–offer was widest, though the balance sheet the limit rations had not grown (§22.5). CS01 said "room to add," DTS said "four times the risk," and both were arithmetically correct.

### When to reach for which number

Before the desk broke for lunch, Kaz turned the morning into one more table, a row per question, because the question chooses the ruler and not the other way round.

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

At 7:40 on Wednesday the function Kaz needed first was the one that would not reconcile: `z_spread` with a settlement date. The vendor valued the note for settlement two days after the trade, with accrued (§4B.8); Kaz's overnight version valued it on the trade date and had no argument through which a settlement date could even be passed. The three basis points were not an arithmetic bug. They were a question the function's signature had no way to ask, and the rest of this section follows from taking that seriously.

**The Spec You Hand the Robot.** *What ROBO built from the vague version* ("add a spread function to the bond library"): `spread(bid, ask) = ask - bid`, with a docstring, a unit test and full coverage. It was correct.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.68:* "The word spread is perhaps the most overloaded (and sometimes abused) word in finance."
>
> **Annotation.** ROBO picked a correct dictionary entry, and the wrong one. The cure is not a better guess but a signature that cannot be called without the missing facts: which curve, which compounding, which price (dirty, per 100), which unit comes back. This module implements eight meanings and computes none of them from a clean price.

*What the module is for, at this point in the story.* The cold open showed what happens when every consumer of a spread computes its own: six columns, 280bp apart. So `bondmath.py` is less a pricing library than a single source of arithmetic. Chapters 5, 8, 9, 10, 12, 15 and 19 import it, so that when two chapters disagree, they disagree about the market and not about compounding.

*Why it is built this way.* The chapter reduces to two objects and one verb. The objects are a list of (time, cash flow) pairs (§4B.1) and a discount function $d(t)$ (§4B.6). The verb is *reprice*: a yield, a Z-spread, an OAS, a hazard rate and a discount margin are each the single constant that, inserted in the right place, makes the list equal the dirty price. So there is one pricing kernel per model (yield, curve, hazard, lattice) and one solver for all of them: bisection, on purpose. Every kernel is strictly monotone in its constant (§4B.2), so a bracketed bisection cannot find the wrong root or diverge, and when the price is impossible it fails loudly, which is the failure you want.

> **Math, Gently.** *An implied number is a question asked backwards.* Pricing runs forward: give me a yield and I will give you a price. Every spread on the desk runs backward: here is the price, so what yield, spread or hazard would have produced it? Bisection plays twenty questions. Take a bracket that surely contains the answer, say yields from −5% to 500%, and price the midpoint. If that price is above the market's, the yield is too low, so keep the upper half; otherwise keep the lower. Each guess halves the bracket, so 43 guesses shrink 5.05 below $10^{-12}$ and the 9.00% of 23 March comes back to twelve decimals. It works because price only falls as yield rises, and a one-way function crosses a given price once. The proof is in §4B.2.

*Inputs and outputs.* Prices per 100 face, dirty unless a name says otherwise; rates, spreads and hazards as annual decimals (basis points only for display); times in years. A curve is any function `disc(t)` returning discount factors, flat (`flat_curve`) or bootstrapped (`curve_from_par`). Results are floats or dicts with named fields. The lattice runs on a grid: `ho_lee` builds the tree, `on_grid` places the flows, `lattice_price` runs §4B.7's backward induction.

*Where it belongs.* It is built for research, for the risk report's analytics, and for checking a vendor; it found Kaz's three basis points. It is not a production library: no holiday calendars, no odd coupons beyond $w$, a CDS premium leg paid continuously on ACT/360 (within a basis point or two of §24.2's quarterly model), and a Ho–Lee tree whose normal rates go negative at the bottom nodes. A lognormal desk will disagree with this OAS by a few basis points, and each will be right about its own model (Veronesi p.467, §4B.7).

*Where it refuses, and why.* The function `pecs` on a bond at or below its assumed recovery has no solution, since no hazard can make a bond worth less than its recovery; it raises, as it did on the SVB holdco note at 40 in §4B.3's replay, and the right response is to quote price and recovery, not to lower $R$ until the solver is happy. A clean price passed as dirty gives a smooth, plausible yield that is off by the accrued; the solver cannot know, so the argument is named `p_dirty`. And the lattice refuses a cash flow off its step dates, because rounding a coupon to the nearest node moves it by up to half a step and the OAS absorbs the error silently.

*Tests.* Every identity in the chapter is an assertion at the bottom of the listing, from the 0.50 of accrued and the 31st rule to the lattice identities of §4B.7 and the make-whole proposition, and so is the 23 March column of Table 4B.1.

*The full python listing is [Listing 4-B.1 in Appendix F](#code-4b-1).*

*Used in:* §5.2 and §5.9 (durations and convexities in the spread-return expansion), §6-B.8 (Halvorsen's Z-spread), §8.1–§8.4 (excess returns, empirical duration, DTS), §9.2 and §10.3 (DTS as beta and as the volatility scaler), §12.2–§12.3 (carry and spread per unit of risk), §15.1 (call and make-whole economics), §19.2 (`oas`, `oasd`), §21.1 (`discount_margin`), §24.2–§24.3 (`hazard_price`, `pecs`), App F.

## 4B.10 Desk Debrief

**Finder.** One row per tool: where its equation lives, the picture that explains it, the scene that shows when it works or breaks, and the function in `bondmath.py` (Listing 4-B.1) that computes it.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code |
| :-- | :-- | :-- | :-- | :-- |
| Price, accrued, yield | Street formula and premium identity, §4B.1–§4B.2 | Post-dated cheques (§4B.1); the one dial (§4B.2) | Agnieszka's thirty-first (§4B.1): accrued to settlement, thirty-first to thirtieth | `accrued`, `cashflows`, `price`, `ytm` |
| Duration: Macaulay, modified, effective, spread, key-rate | $D^{\text{mod}} = D^{\text{Mac}}/(1+y/f)$ and $D^{\text{eff}}$, §4B.3 | The beam and the hill's slope (§4B.3) | Kaz's three bonds and the SVB replay (§4B.3): near recovery the rate duration is $1/(\lambda + r)$, whatever the yield formula says | `risk_at_yield`, `effective`, `key_rate_durations` |
| Convexity, in three meanings | $C = D^2 + $ dispersion; $dD/dy = D^2 - C$, §4B.4 | Two trucks; Jensen's coin (§4B.4) | The point and a half on 9 March 2023 (§4B.3) and the 12.8 points of 2020 (§4B.4, §4B.8); Theo's question about the trend sense (§4B.4) | `risk_at_yield`, `explain` |
| DV01, CS01, DTS | DV01 and the DTS expansion, §4B.5 | Percent, not basis points (§4B.5) | The number for the PM on 23 March (§4B.8, Beat 3): CS01 said safer, DTS said four times riskier | `dv01`, `fallen_angel_row` |
| Hedge ratio, Treasury and pair | $-\text{DV01}_{\text{bond}}/\text{DV01}_H$, §4B.5 | The Pair, PB-03 before it opens (§4B.5) | The hedge line of the 23 March cards (§4B.8, Beat 3): analytic 0.545 against Ben Dor's −0.26; Ines's "the alpha is the size of the hedge-ratio error" | `dv01`, `effective` (empirical ratio: §8.2) |
| The curve and the eight spreads | Bootstrap; Z, ASW, DM and PECS, §4B.6 | Bootstrapping is peeling (§4B.6); six rulers, one length (§4B.8) | Kaz's whiteboard (§4B.6) and the reconciliation (§4B.8, Beat 1): attach the definition; the CLO seat reads DM differently (§4B.6) | `curve_from_par`, `z_spread`, `asw_par`, `discount_margin`, `pecs` |
| YTW, OAS, the lattice and the make-whole | Ho–Lee fit, backward induction, the four identities and the proposition, §4B.7 | What "risk-neutral" means (§4B.7) | Theo's objection (§4B.7): issuers call for covenants and M&A; the 1:10 a.m. assert; *Article III* on the card (§4B.8, Beat 3) | `ytw`, `ho_lee`, `on_grid`, `lattice_price`, `oas` |
| Implied numbers and the solver | Bracketed bisection, §4B.9 | An implied number is a question asked backwards (§4B.9) | PECS at 40 in the SVB replay (§4B.3): the solver's refusal is the signal | `solve`, `pecs` |

- **A bond is a list, and a yield is a price in another font.** Every spread is the one constant that makes the list reprice against some curve. Name the curve, the compounding and the dirty price, or the number means nothing. (Law 11)
- **Duration answers two questions that share a number by coincidence.** For a callable, a floater or a bond at 60, reprice; in a crisis, hedge with §8.2's empirical duration, because the analytic one can have the wrong sign. (Law 1)
- **"Convexity" is three words.** Ask with respect to what, over what horizon, and who is short it. The bill for it is called theta.
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
5. *(ROBO's momentum signal.)* Theo asks for "twelve-month spread momentum on high yield, 2019–2025, using the spread column." Name three ways the output can measure conventions instead of markets. *Solution.* I-spread or ASW switching from LIBOR to SOFR in 2023 (one curve); G across the 2022–24 inversion (Z or OAS); YTW jumping when the workout date changes (OAS at a stated $\sigma$; Law 11).

### Deep-Dive Resource Graph

- **Podcasts.** *Wolf Street Report*, "Nothing's Fixed: What's Behind the Corporate Debt Bailout" (Wolf Richter, 6 May 2020), with transcript, https://wolfstreet.com/2020/05/06/nothings-fixed-whats-behind-the-corporate-debt-bailout/ : a skeptic's account of the March 2020 seizure and the Fed's facilities; read it next to McCauley below.
- **"ReSolve Riffs with Harley Bassman, the Convexity Maven"** (*ReSolve Riffs*, host Adam Butler, 19 January 2021). Convexity explained by the creator of the MOVE index, including how simple the calculus is; the audio companion to §4B.4, and the place to start. https://resolve-gestalt-university.captivate.fm/episode/resolve-riffs-with-harley-bassman-the-convexity-maven
- **"Bond Market Mastery: Harley Bassman on Mortgages, the Fed Rates and Convexity"** (*Tradeweb Off The Desk*, host Bhas Nalabothula, 23 September 2024). Mortgage-backed securities, why convexity matters and the rise of the MOVE index, from a dealer-platform podcast; the nearest public bridge from §4B.4 to the callable-bond lattice of §4B.7. https://offthedesk.podbean.com/e/bond-market-mastery-harley-bassman-on-the-move-index-fed-rates-and-convexity
- **"At the Money: Managing Bond Duration"** (*Masters in Business*, Barry Ritholtz with Karen Veraa of BlackRock iShares, 11 September 2024). A short, plain-language statement of the yield-versus-duration trade-off; hear what a retail-facing explanation leaves out before §4B.3 adds spread, effective and key-rate duration. https://omny.fm/shows/masters-in-business/at-the-money-managing-bond-duration
- **"Dan Davies On What Brought Down Silicon Valley Bank"** (*Odd Lots*, Dan Davies, 14 March 2023). A bank "reached for yield buying long-dated Treasuries" at ultra-low rates: duration mismatch as a failure story, and a hook for the §4B.3 risk-report discussion. https://omny.fm/shows/odd-lots/dan-davies-on-what-brought-down-silicon-valley-ban
- **"Lectures 4-6: Fixed-Income Securities"** (Andrew W. Lo, MIT OpenCourseWare 15.401 Finance Theory I, Fall 2008). The free MBA-level derivation of spot and forward rates, yield to maturity, and Macaulay and modified duration; the clean prerequisite for §4B.1-4B.3. https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/resources/mit15_401f08_lec04/
- **"DTS (Duration Times Spread)," summary of Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen and Penninga** (*CFA Digest*, August 2007). A short, free summary of the paper that defines DTS as market weight × spread duration × spread; the source for the DTS line of the §4B.5 risk report. https://rpc.cfainstitute.org/-/media/documents/article/cfa-digest/2007/dig-v37-n3-4779-pdf.pdf
- **Practitioner Writing.** BNN Bloomberg, "Ford taps junk market for cash after virus spurs \$2 billion loss" (17 April 2020), https://www.bnnbloomberg.ca/ford-taps-junk-market-for-cash-after-virus-spurs-2-billion-loss-1.1422986 (the deal in §4B.8). Robert McCauley, "The Fed in the Corporate Bond Market in 2020" (Boston University Global Development Policy Center, 7 August 2020), https://bu.edu/gdp/2020/08/07/the-fed-in-the-corporate-bond-market-in-2020 , which argues the announcement did the work before the purchases. Congressional Research Service, *COVID-19 and Corporate Debt Market Stress* (Insight IN11275), https://www.everycrsreport.com/reports/IN11275.html . Veronesi, *Fixed Income Securities* (2010), Chapters 2–4 and 12.
- **Academic Papers.** Macaulay (1938), *Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856*, NBER; Ho and Lee (1986), *Term Structure Movements and Pricing Interest Rate Contingent Claims*, Journal of Finance 41(5); Black, Derman and Toy (1990), *A One-Factor Model of Interest Rates and Its Application to Treasury Bond Options*, Financial Analysts Journal 46(1); Ho (1992), *Key Rate Durations: Measures of Interest Rate Risks*, Journal of Fixed Income 2(2); Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen and Penninga (2007), *DTS (Duration Times Spread)*, Journal of Portfolio Management 33(2); Ambastha, Ben Dor, Dynkin, Hyman and Konstantinovsky (2010), *Empirical Duration of Corporate Bonds and Credit Market Segmentation*, Journal of Fixed Income 20(1); Haddad, Moreira and Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response*, Review of Financial Studies 34(11); O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, Journal of Financial Economics 142(1); Federal Reserve Bank of New York Staff Report 986, on the corporate credit facilities, https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr986.pdf
- **Data & Code.** `bondmath.py` (§4B.9, App F); FRED DGS10, https://fred.stlouisfed.org/series/DGS10 , and T10Y2Y, https://fred.stlouisfed.org/series/T10Y2Y ; New York Fed SOFR, https://www.newyorkfed.org/markets/reference-rates/sofr ; QuantLib, https://www.quantlib.org (the production library to check this module against, and the reverse); ISDA CDS Standard Model, https://www.cdsmodel.com

*Used in:* every chapter that quotes a duration, a DV01 or a spread; the Debrief bullets feed App E (Laws 1, 3, 7, 11, 13) and App A §A.3 (the convexity and duration collisions).

<!-- STATUS: COMPLETE -->

