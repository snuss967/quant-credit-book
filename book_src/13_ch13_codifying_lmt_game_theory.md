# Chapter 13: Codifying Liability Management Transactions (LMTs)

*Tuesday, 7:41 a.m. Three days after the lender call. The desk smells like cold coffee and somebody else's leverage.*

The headline lands at 7:40: **LARKSPUR FOAM LENDERS SAID TO TAP COUNSEL AS SPONSOR EXPLORES "LIABILITY MANAGEMENT."** (Larkspur Foam Holdings is fictional. Every clause in its credit agreement is borrowed from a real one.) At 7:41 a client asks for a bid on \$15mm of the Larkspur 2029 first-lien term loan. It was marked 84 last night. The client "would look at 78."

Theo Marsh already has the credit agreement open. Old habits. "Section 2.18 is pro rata sharing. Section 9.02(b) makes it a sacred right. But 9.05(g) carves out purchases by the borrower, and the question is whether it says *open market* purchase or just *purchase*—"

"I assumed a Serta blocker was a mattress protector," says Kaz Lind, reading over his shoulder.

"It is," says Mags Dunleavy, not looking up. "It protects the mattress company's lenders from the mattress company."

Kaz considers this. "So the lenders are the mattress."

"The excluded ones are what gets slept on."

Ines Okafor turns her chair a quarter turn, which is how she signals that a hand has started. "Theo. What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is fifteen million face, call it a twelve-million-dollar check at 78. The odds depend on whether the sponsor can get a bare majority to sign up to a non-pro-rata deal. And the person who knows more than me is—" He stops. "Either this seller was invited into the group and is selling before they get wall-crossed, which is unlikely, or they *weren't* invited, and they know exactly what that means."

"Or," says Ines, "they're a CLO that just read the same headline you did and has a CCC bucket to manage. Three sellers. Three different hands. Same price."

From somewhere offstage comes the sound of a Rule 2019 statement being drafted. The Ad Hoc Group, represented by counsel, speaks in unison: *"We neither confirm nor deny that we exist. We hold 51.3% of the first lien."*

Mags finally looks up. "Back in my day we did this with exit consents on bonds and called it an exchange offer. The innovation was doing it to the bank group. The bank group used to be the one holding the knife."

Theo stares at three hundred pages of credit agreement and one rumor. **The question this chapter answers: how do you turn a document and a rumor into a number you can quote against?**

By the end of this chapter you will be able to: write every LMT (uptier, drop-down, double-dip, pari-plus, amend-extend-and-exchange) as the difference between two waterfalls on the same enterprise value; convert the five clause families that enable priming into state variables with units; price an excluded lender's position as a short digital put on $V$ struck where document capacity says; solve the $n$-lender threshold game and the sponsor's procurement auction, and see why a cooperation agreement turns both into bilateral bargaining; build a multi-obligor clearing engine that handles guarantees, intercompany loans, and circularity without creating or destroying a dollar; and specify the Priming Risk Score, a Bayesian hazard model that a coding agent can build from about a hundred events without overfitting itself into the sun.

## 13.1 The LMT Zoo, Seen From the Desk

A liability management transaction is an out-of-court change to the capital structure, executed under the existing documents, that re-allocates recovery among claims that were drafted to be equal. That last clause is the whole thing. A pro rata amend-and-extend that treats every lender identically is liability management in the polite sense. The trades that make careers and lawsuits are the ones in which some holders of the same tranche end up senior to other holders of that tranche, or in which collateral that was everybody's becomes somebody's.

From the desk, every species in the zoo has the same skeleton. There is an enterprise value $V$ at some resolution date (a refinancing, a sale, a Chapter 11 plan). There is a document state $\mathcal{D}$, which encodes who has a claim against which entity, at what priority, secured by what. And there is a waterfall operator $\mathcal{W}_{\mathcal{D}}$ that maps $V$ into a vector of recoveries per dollar of face, one entry per claim:

$$
\mathbf{R} = \mathcal{W}_{\mathcal{D}}(V), \qquad R_j \in [0, 1].
$$

An LMT is a move $\mathcal{D} \to \mathcal{D}'$. The economic content of the move, for claim $j$, is the **transfer function**

$$
\Delta_j(V) = \big[\mathcal{W}_{\mathcal{D}'}(V)\big]_j - \big[\mathcal{W}_{\mathcal{D}}(V)\big]_j .
$$

Two facts make this useful. First, $\Delta_j$ is a function of $V$, so it is a derivative on enterprise value and can be priced like one: integrate it against a distribution of $V$ and you have the expected transfer. Second, waterfalls conserve value. If the face amounts under the two document states are $\mathbf{F}$ and $\mathbf{F}'$, then

$$
\mathbf{F}'^{\top}\mathcal{W}_{\mathcal{D}'}(V) = \min\!\big(V,\ \mathbf{1}^{\top}\mathbf{F}'\big), \qquad \mathbf{F}^{\top}\mathcal{W}_{\mathcal{D}}(V) = \min\!\big(V,\ \mathbf{1}^{\top}\mathbf{F}\big),
$$

so in any state where $V$ is below both totals, the dollar transfers sum to exactly zero. An LMT does not create recovery in the states that matter. It moves recovery. (It may change $V$ itself, by buying liquidity runway or by burning fees, and we will keep that effect separate and explicit; see §13.3.)

That is the sentence to say out loud on your first day: *an LMT is a zero-sum transfer among creditors in low states, wrapped in a liquidity story about high states.* The liquidity story is sometimes true. The transfer is always true.

| Species | What moves | Who loses | Enabling clause (the trapdoor) | Canonical cases |
| :--- | :--- | :--- | :--- | :--- |
| Non-pro-rata uptier | Participating lenders exchange into new super-priority debt, primed above non-participants of the same tranche | Excluded lenders of the same class | Majority-vote amendment of lien/payment subordination; buyback exception ("open market purchase" or "purchase") to pro rata sharing | Serta Simmons (2020), Mitel (2022), Wesco/Incora (2022) |
| Drop-down | Collateral (often IP) moves to an unrestricted or non-guarantor subsidiary, which borrows against it | Every lender whose collateral package shrank | Investment baskets, RP builder, unrestricted-subsidiary designation, permissive lien/guarantee release | J.Crew (2016–17), PetSmart/Chewy (2018) |
| Double-dip | New lender gets a guarantee claim *and* a claim via an intercompany loan against the same obligor group | Existing pari passu lenders, diluted by a claim that counts twice | Debt and lien baskets that permit pari guarantees and intercompany loans | Trinseo (2023) |
| Pari-plus | Double-dip plus a structurally senior guarantee from non-guarantor (often foreign) subsidiaries | Existing lenders, who lose the non-guarantor value to the new money | Same baskets plus foreign-sub guarantee capacity | Sabre (2023) |
| Amend-extend-and-exchange | Majority extends into a separate class, then amends away the old class's protections, then refinances its own class | Lenders left in the old class | Majority amendments and class-voting mechanics | Post-Serta structures "deployed throughout 2025" (Wachtell, Feb 2026) |
| Exit-consent bond exchange | Tendering holders consent to strip covenants on the old notes and receive new notes from a better-positioned issuer | Non-tendering holders | Majority-amendable covenants; TIA §316(b) protects only payment terms | Lions Gate/Starz (2024 exchange; 2026 ruling) |
| Deal away | Borrower raises third-party money, often with a short par call, around an organized lender group | Organized lenders, if the threat works | Same baskets, used as a threat point | Optimum, Altice International, Liberty Puerto Rico, KIK (per Wachtell, Feb 2026) |

The first column is how the press names these deals. The fourth column is how you will name them, because the fourth column is the thing your model reads.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.228:* "Exchange offers are “coercive” when they compel cooperation by exposing nonparticipants to the risk of being made worse off."
>
> **Annotation.** Moyer's definition was written for the bond exchange offers of the 1990s and 2000s, and it travels unchanged into the LMT era with one twist that changes the game theory completely. In Moyer's world, coercion is *uniform*: every holder is offered the same exchange, and the threat to non-participants (stripped covenants, structural subordination) is the stick that solves the holdout problem. Everyone can take the carrot. In a non-pro-rata uptier, coercion is *selective*. The carrot is offered only to an invitation list, and the stick lands on everyone else, including holders who would have happily taken the carrot. That one change turns a coordination problem (will enough of us accept?) into a coalition-formation problem (who gets to be in the coalition that does the coercing?). Section 13.4 solves the second problem. The desk's practical departure from Moyer is this: in the 1990s you modeled your *participation decision*. In 2026 you model your *invitation probability*, because for most holders, most of the time, the decision is made for them.

> **Desk Myth vs. Desk Reality.** *Myth:* "LMEs avoid bankruptcy; that's the point." *Reality:* Roe and Rotaru hand-collected 89 coercive non-pro-rata LMEs and found that fewer than half avoided both bankruptcy and re-default within a year, and "within two years, only 22% avoided both"; among firms with at least two years of post-LME history, 56% had already filed, and those that filed spent two to three times longer in bankruptcy than non-LME prepacks (Harvard Law School Bankruptcy Roundtable, Feb 24, 2026; SSRN abstract 6103369). Moody's found about 46% of 2023 distressed exchanges had already re-defaulted, most in under a year (reported by Bloomberg Law, Apr 23, 2025). Proponents cite an S&P figure that 63% of LME users avoid Chapter 11 (quoted in Antill, Jiang and Wang, HLS Roundtable, June 30, 2026; secondhand). The two camps differ in their samples, horizons, and default definitions. Whichever number you believe, the LMT is not the terminal state of the credit. It is a jump to a new state with a new, usually higher, hazard. Model it that way (§13.8).

## 13.2 Legal Prose to State Space

You have spent years reading credit agreements as text. The model needs them as numbers. The translation has five clause families, and each one maps to a small set of features with units. The goal is not to replace a lawyer. It is to make the lawyer's reading *comparable across 1,500 borrowers*, so that the desk can rank them.

**Family 1: Pro rata sharing and sacred rights.** The pro rata sharing clause (Serta's was §2.18) says every lender in a tranche shares payments ratably. The amendment section (Serta's §9.02(b)) lists the "sacred rights" that need the consent of each affected lender rather than a majority. The question for an uptier is whether *subordination* of the loans, or of the liens, is on that list. If it is, a majority cannot prime the minority. That is the blocker. Features: `sacred_rights_scope` $\in$ {`payments_only`, `payments_plus_liens`, `payments_plus_subordination`}, and `has_serta_blocker` $\in \{0,1\}$, which is 1 when lien or payment subordination requires each affected lender's consent.

**Family 2: Voting thresholds.** The required-lender fraction $\theta$ is the share of the class that can amend everything not on the sacred list. In syndicated loans $\theta$ is usually a simple majority. Many indentures require two-thirds for lien releases (that was the threshold the Wesco participants needed). Sacred rights are $\theta = 1$ for the affected lender. Feature: `theta_required` $\in (0, 1]$, measured *for the specific action the deal requires*, not for the agreement in general. One agreement has several $\theta$'s, and the trapdoor is usually the lowest one that can be reached.

**Family 3: Buyback exceptions to pro rata.** Most agreements let the borrower buy back its own loans without offering the same deal to everyone, through Dutch auctions open to all lenders or through open market purchases. This exception is how a non-pro-rata exchange slips past the pro rata clause. Feature: `buyback_exception` $\in$ {`none`, `dutch_only`, `open_market`, `purchase`}. On December 31, 2024, two appellate courts decided on the same day that the difference between the third and fourth values is worth the entire priming loss. The Fifth Circuit held in *Serta* that "an open market purchase is a purchase of corporate debt that occurs on the secondary market for syndicated loans," so a privately negotiated exchange did not qualify. New York's First Department held in *Mitel* that an undefined "purchases" exception, with no "open market" qualifier, was unambiguous and was satisfied by an exchange paid in new loans (as summarized by Paul, Weiss, Jan 10, 2025). Same kind of deal, same day, one word, opposite results. "Open market purchase" really is the most expensive three words in finance, and the word "open" accounts for most of the bill.

**Family 4: Investments, restricted payments, and unrestricted subsidiaries.** This is drop-down territory. The question is how many dollars of value can legally leave the collateral group. The capacity is a sum of baskets:

$$
C^{\text{unsub}} = B^{\text{gen}} + B^{\text{builder}} + B^{\text{ratio}}\,\mathbf{1}[\text{ratio test passes}] + B^{\text{unsub}} + B^{\text{other}},
$$

where $B^{\text{gen}}$ is the general investment basket (often a "greater of" dollar amount and percentage of EBITDA or total assets), $B^{\text{builder}}$ is the builder basket (the "Available Amount" or "Cumulative Credit"), $B^{\text{ratio}}$ is the unlimited capacity that opens if a leverage test is met, $B^{\text{unsub}}$ is a dedicated basket for investments in unrestricted subsidiaries, and $B^{\text{other}}$ covers the capacity that hides in "Permitted Investments" clauses that can be stacked (the J.Crew trapdoor was precisely a stack: an investment in a non-guarantor restricted subsidiary, then onward from that subsidiary to an unrestricted one). Features: `unsub_capacity_pct_ev` $= C^{\text{unsub}}/\text{EV}$ and `rp_builder_pct_ev` $= B^{\text{builder}}/\text{EV}$, both dimensionless. Divide by enterprise value, not by face, because the question is what fraction of the *pie* can walk out the door.

The builder basket is a running account, and Moyer lays out the classic bond-indenture version line by line.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.173:* "50% of all net income earned 100% of proceeds from the sale of common or preferred stock 100% of the proceeds from the issuance of any junior debt securities Less: 100% of all net losses 100% of all amounts distributed as"
>
> **Annotation.** (The extraction preserves the page's line breaks as spaces; the original is a formatted list in which each item is a line of the builder computation.) This is the accounting identity behind $B^{\text{builder}}$: a starter amount, plus half of cumulative consolidated net income, plus equity proceeds and certain junior debt proceeds, less net losses and less every restricted payment and unrestricted-subsidiary investment already made. Code it as a state variable that evolves quarterly: $B^{\text{builder}}_{t+1} = B^{\text{builder}}_t + 0.5\,\text{CNI}_t^{+} - \text{CNI}_t^{-} + \text{EqProc}_t - \text{RP}_t - \text{Inv}^{\text{unsub}}_t$, floored at zero. Two modern departures matter. First, leveraged-loan agreements written after about 2015 often build from Consolidated EBITDA minus a multiple of fixed charges, or from a "greater of" starter that grows with EBITDA, so the builder can *grow while the company deteriorates* if EBITDA add-backs are generous (Mags is right to distrust anything called "adjusted"). Second, the builder is only one of several stackable baskets; the drop-down cases were won or lost on whether baskets could be used *sequentially through intermediate subsidiaries*. The feature you want is not "the builder" but the maximum dollar amount that can reach an unrestricted subsidiary by any legal path through the entity graph, which is a max-flow problem on the definitions (the parser in Chapter 25 builds that graph).

**Family 5: Lien and guarantee release, and the IP blockers.** Can a guarantor be released when it stops being wholly owned (the PetSmart/Chewy move)? Can material intellectual property be transferred out of the collateral group (the J.Crew move)? Can liens be released by a majority? Features: `jcrew_blocker`, `chewy_blocker`, `envision_blocker` (the last named for a 2022 drop-down whose details we treat as illustrative), each in $\{0, 1\}$, plus `lien_release_theta`. Also flag `non_pro_rata_extension_allowed`, which captures the amend-and-extend mechanics that the 2025 "amend-extend-and-exchange" structures exploited.

Kaz, who has followed this so far, raises a hand. "I have a question about the blocker."

"Go ahead."

"Is it a beta blocker? Because the deal seems to raise everyone's heart rate."

"It is a *J.Crew* blocker," says Theo. "It blocks the IP from leaving."

"So it's a beta blocker for the brand." Kaz writes this down. Nobody corrects it, because it is not entirely wrong: a blocker caps the downside jump, which is exactly what a beta blocker does to a pulse.

### 13.2.1 The feature vector

Collect the document features $x^{\text{doc}}_i$ and add three groups the document cannot tell you.

- **Market state** $x^{\text{mkt}}_i(t)$: loan price `loan_px` (points), months to maturity, the liquidity cost score `lcs` (Ben Dor's measure, Chapter 8), three-month equity momentum or, for sponsor-owned names with no public equity, the price momentum of the loan itself.
- **Liquidity state** $x^{\text{liq}}_i(t)$: `runway_months`, defined as unrestricted cash plus undrawn committed revolver, divided by forecast monthly cash burn. This is Theo's 13-week cash flow model, reborn for the third time in this book as a covariate. When `runway_months` falls below about nine and `loan_px` below about 80, the company is in the region where a sponsor *must* do something, and the only question is whether the something is pro rata.
- **Holder and sponsor state** $x^{\text{hold}}_i(t)$: `sponsor_repeat_lme` (has this sponsor done a non-pro-rata deal before?), `holder_hhi` (Herfindahl concentration of the class from CLO holdings data and Rule 2019 statements), `coop_reported` (a cooperation agreement has been reported), and `forum_ny_vs_tx` (which court is likely to hear the fight).

The full state is $x_i(t) = \big(x^{\text{doc}}_i, x^{\text{mkt}}_i(t), x^{\text{liq}}_i(t), x^{\text{hold}}_i(t)\big)$. The document block is nearly static (it changes when the agreement is amended, which is itself an event). The other blocks move daily. Section 13.8 turns $x_i(t)$ into a hazard. Sections 13.3 to 13.7 compute what the hazard is a hazard *of*.

| Feature | Type | Units | Typical source | Expected sign on PRS |
| :--- | :--- | :--- | :--- | :--- |
| `has_serta_blocker` | binary | — | Credit agreement §9.02(b) | − |
| `buyback_exception` | categorical (4) | — | §9.05(g) or equivalent | `purchase` > `open_market` > `dutch_only` > `none` |
| `theta_required` | continuous | fraction of class | Amendment section | − (higher bar, harder deal) |
| `unsub_capacity_pct_ev` | continuous | fraction of EV | Negative covenants + definitions graph | + |
| `rp_builder_pct_ev` | continuous | fraction of EV | Builder definition | + |
| `jcrew_blocker`, `chewy_blocker` | binary | — | Asset-sale and guarantor-release clauses | − |
| `loan_px` | continuous | points | Vendor marks, TRACE for bonds | − |
| `runway_months` | continuous | months | 10-Q cash, revolver, burn model | − |
| `sponsor_repeat_lme` | binary | — | Hand-collected deal history | + |
| `holder_hhi` | continuous | 0–1 | CLO filings, Rule 2019 | + (easier to assemble a majority) |
| `coop_reported` | binary | — | Press, docket | − on non-pro-rata, + on *some* LMT |
| `forum_ny_vs_tx` | binary | — | Governing law, venue history | Time-varying; see §13.9 |

The last column is a prior, not a result. Section 13.8 is where the data gets a vote.

## 13.3 The Uptier as a Recovery Transfer

Start with the cleanest species and price it exactly. One secured class, face $F$, everyone pari passu. Before the deal, each lender recovers

$$
R_0(V) = \frac{\min(V, F)}{F}.
$$

The uptier has three moving parts. New money $N$ comes in as a first-out tranche. A fraction $p$ of the existing face (the participants) is exchanged into a second-out tranche at exchange ratio $x$ (new face per dollar of old face; $x < 1$ means the participants take a haircut in face to jump the line). The remaining $(1-p)F$ (the excluded lenders) stays in the old tranche, now third in line. Write $K_1 = N + xpF$ for the total face senior to the excluded lenders and $K_2 = K_1 + (1-p)F$ for the total face of the new structure. Then

$$
R^{\text{FO}}(V) = \frac{\min(V, N)}{N}, \qquad
R^{\text{SO}}(V) = \frac{\min\!\big((V - N)^+,\ xpF\big)}{xpF}, \qquad
R^{\text{excl}}(V) = \frac{\min\!\big((V - K_1)^+,\ (1-p)F\big)}{(1-p)F}.
$$

**Conservation check.** Multiply each recovery by its face and add: $N R^{\text{FO}} + xpF\,R^{\text{SO}} + (1-p)F\,R^{\text{excl}} = \min(V, K_2)$. Total face fell from $F$ to $K_2 - N = F - (1-x)pF$, which is the "deleveraging" in the press release. It is real, and it is paid for entirely by the participants, in exactly those states where nobody needed it.

**The excluded lender's transfer.** The priming loss is $\Delta R^{\text{excl}}(V) = R_0(V) - R^{\text{excl}}(V)$. It is piecewise linear with three regions:

$$
\Delta R^{\text{excl}}(V) =
\begin{cases}
\dfrac{V}{F}, & V \le K_1, \\[2ex]
\dfrac{V}{F} - \dfrac{V - K_1}{(1-p)F}, & K_1 < V < K_2, \\[2ex]
R_0(V) - 1, & V \ge K_2 .
\end{cases}
$$

In the first region the excluded lender loses everything it would have recovered. In the middle region the loss shrinks linearly, at slope $\frac{1}{F} - \frac{1}{(1-p)F} < 0$. In the third region the loss is *non-positive*: if $K_2 \le V < F$, the excluded lender is paid in full while it would have recovered only $V/F$ before. It gains, because the participants gave up face. (The gain is small and lives in a narrow band of states; when $V \ge F$ both recoveries are 1 and the transfer is zero.)

Now look at the shape. The excluded lender used to own a linear slice of the firm, $\min(V,F)/F$. It now owns a call spread on $V$ between strikes $K_1$ and $K_2$. When the excluded minority is small, $(1-p)F$ is small, the spread is steep, and the call spread is approximately a *digital call* struck at $K_1$. So the priming loss is approximately

$$
\Delta R^{\text{excl}}(V) \approx R_0(V)\,\mathbf{1}[V < K_1].
$$

**The excluded lender is short a soft digital put on enterprise value, struck at the face that now sits ahead of it, with notional equal to its old recovery.** It wrote that put on the day the uptier closed. Nobody asked it to.

The participants, meanwhile, bought the same put. Per original dollar, a participant's position changed by $x R^{\text{SO}}(V) - R_0(V)$ (ignoring the new-money economics, which are usually priced generously). In low states this is large and positive. In high states it is $x - 1 < 0$: the participant paid for its put with $(1-x)$ points of face. A participant in an uptier is a lender who bought downside protection and paid the premium in principal. The excluded lender is the counterparty who wrote that protection for free.

**The expected transfer, in closed form.** Suppose $V$ is lognormal under $\mathbb{P}$ at the resolution horizon: $\ln V \sim \mathcal{N}(\mu, s^2)$. The dominant term of the expected loss is the partial expectation below the strike, which has the same form as the put leg of Black–Scholes:

$$
\mathbb{E}^{\mathbb{P}}\!\big[V\,\mathbf{1}[V < K]\big] = e^{\mu + s^2/2}\,\Phi\!\left(\frac{\ln K - \mu - s^2}{s}\right).
$$

So for $K_1 \le F$, the first region contributes $\frac{1}{F}e^{\mu + s^2/2}\Phi\big((\ln K_1 - \mu - s^2)/s\big)$ to $\mathbb{E}^{\mathbb{P}}[\Delta R^{\text{excl}}]$. The middle and upper regions add the correction terms. The code in §13.8 computes all three exactly by quadrature and checks the first against this closed form by Monte Carlo. This is the uptier's version of checking a simulated Merton spread against the formula: if your simulated transfer and your partial expectation disagree, your waterfall has a bug.

**Where value enters.** New money is not free value. If the $N$ dollars buy runway that survives to resolution, the post-deal enterprise value is $V + \kappa N$, with $\kappa \in [0, 1]$ the fraction of new money still in the firm at resolution, and every formula above should be evaluated at $V + \kappa N$ in the post-deal world. For a company burning cash, $\kappa$ is close to zero by the time anyone files. Roe and Rotaru's evidence that leverage did not fall and ratings stayed flat after LMEs is evidence that, on average, $\kappa$ is small.

### 13.3.1 Case Study: Serta Simmons (2016–2026), in the Formula

The Fifth Circuit's opinion supplies the parameters. In 2016 Serta Simmons Bedding refinanced with "\$1.95 billion in first-lien syndicated loans and \$450 million in second-lien syndicated loans." In June 2020, "The Prevailing Lenders provided SSB with \$200 million in new financing in exchange for \$200 million in first-out, super-priority debt. The Prevailing Lenders also traded in \$1.2 billion of their first-lien and second-lien loans for approximately \$875 million in second-out, super-priority debt." They "held a bare majority of the outstanding first-line debt" (sic; the opinion means first-lien), and the loans "were trading far below par."

Map it, treating the two liens as one blended class for the moment (an approximation we flag; the 2L lenders were already junior, so the blended class overstates the 1L excluded lenders' pre-deal recovery in low states):

- $N = 200$, $F = 2{,}400$ (all figures \$mm), $pF = 1{,}200$, so $p = 0.5$.
- $x = 875/1{,}200 \approx 0.729$, a face haircut of about 27 points for the participants.
- $K_1 = 200 + 875 = 1{,}075$. $K_2 = 1{,}075 + 1{,}200 = 2{,}275$.

So after June 2020, the excluded lenders recovered nothing unless enterprise value exceeded about \$1.075bn. In a state where $V = \$1.075$bn, their pre-deal blended recovery would have been $1{,}075/2{,}400 \approx 44.8$ cents. The transfer in that state is the entire 44.8 points.

Six years later a court put a number on it. On remand, the bankruptcy court for the Southern District of Texas issued a memorandum opinion on July 7, 2026, finding certain participating lenders liable for breach of the pro rata sharing provision and awarding \$261.13mm plus prejudgment interest. As summarized by Mayer Brown (July 2026): damages were measured as of the breach date, June 22, 2020; the benefit taken was the face value (\$734mm) of the first-lien second-out debt the participants received; the excluded lenders' ratable share was \$348mm (\$895mm / \$1.887bn × \$734mm); the excluded loans were valued at their 25-cent closing-date market price; the "but-for" world was worth \$484.88mm and the actual outcome \$223.75mm (that is, \$895mm × 0.25); and the difference, \$261.13mm, carries mandatory 9% New York prejudgment interest from June 22, 2020. At simple interest for about six years, that adds roughly 54%, or about \$142mm (our arithmetic, illustrative).

Notice which measure the court used. It did not compute $\mathbb{E}^{\mathbb{P}}[\Delta R]$ over a distribution of enterprise values. It used a market price on the closing date, which is a $\mathbb{Q}$-flavored number with the risk premium baked in. For the desk this is useful twice over. It gives a hard calibration point for the expected damages term in the litigation outside option (§13.4), and it tells you that if you are long excluded paper with a live claim, the claim's value is anchored to *where the loan traded the day the deal closed*, not to where it ends up. A claim measured at the trough is a put that a court can exercise for you, years later, with 9% interest.

The other remedy matters too. Serta's plan gave the participants an indemnity for their litigation exposure. The Fifth Circuit held that this violated the equal-treatment rule of Bankruptcy Code §1123(a)(4) because "the unequal treatment in this case implicates both opportunity and result," and chose "to excise the offending indemnity." In a footnote it disposed of the argument that offering everyone the same *opportunity* is enough, with a hypothetical worth memorizing: a plan that gives every class member "a note promising payment of \$5 million in one year if the member is headquartered in Louisiana." Equal opportunity, in the sense that anyone may move to Louisiana. In the language of this section, the indemnity was the participants' hedge against the litigation leg of their put. The court cancelled the hedge and left them with the exposure.

> **Trend Watch.** *The strike moved, and so did the volume.* **Documents:** Buccola and Nini's study of 600+ leveraged loan agreements (2016–2022) found that "prior to 2020, only 40% of loans restricted uptiers, often inadvertently," while "by mid-2022, 85% of new loans explicitly blocked uptiers, with 70% requiring unanimous lender consent for subordination" (HLS Roundtable, Apr 8, 2025; *Journal of Legal Studies* 53:489, 2024). **Aggressiveness:** Octus counted 11 non-pro-rata uptiers from March 2022 to July 2024; Wesco, Mitel and Robertshaw moved 100% of value away from non-ad-hoc creditors, while the six most recent moved an average of 18% (Apex 38%, Valcour 12%, EyeCare 13%, GoTo 13%) (Octus, July 16, 2024). **Counts:** LMEs hit a high-water mark of 38 in 2024 and fell to 24 in 2025, but still accounted for about two-thirds of default activity by issuer count in 2025 and exceeded both payment defaults and bankruptcies on a rolling 12-month basis in every month of 2025 (Wachtell Lipton, *Liability Management 2026: For Better or Worse*, Feb 3, 2026). In H1 2026, 25 LMEs closed, against 24 in H1 2025, and "the coercive uptier structures that defined 2025 have all but vanished," replaced by equity handovers and consensual amend-and-extends (9fin, Aug 28, 2026). **What it means for the desk:** in the formula above, blockers drive the probability of a non-pro-rata deal down, and later deals have higher $K_1$ relative to $F$ (smaller transfers). A PRS model trained on 2020–2022 events will overstate both the probability and the severity of a 2026 uptier, unless vintage enters as a covariate. The transfer did not disappear. It migrated to structures (drop-downs, double-dips, amend-extend-and-exchange) whose clauses the 2020-vintage blockers do not cover.

## 13.4 Game Theory I: Threshold Games and the Sponsor's Auction

The waterfall tells you what the transfer is. The game tells you who ends up on which side of it.

**The threshold game.** A class has lenders $i = 1, \dots, n$ with holdings $w_i$, $\sum_i w_i = 1$. An amendment passes if a coalition $S$ with $\sum_{i \in S} w_i > \theta$ consents. Let $u^{\text{in}}$ be the per-dollar value of being inside a winning coalition, $u^0$ the value of the status quo, and $u^{\text{out}}$ the value of being primed, with $u^{\text{in}} > u^0 > u^{\text{out}}$. (From §13.3: $u^{\text{in}} - u^0 = \mathbb{E}[x R^{\text{SO}} - R_0]$ plus new-money economics, and $u^0 - u^{\text{out}} = \mathbb{E}[\Delta R^{\text{excl}}]$.)

Take an invited lender $i$ and collapse everyone else into "the rest of the class." There are three relevant situations: the rest can win without $i$, the rest can win only with $i$ (lender $i$ is *pivotal*), or no deal is possible. The payoff to $i$ is:

| | Rest wins without $i$ | $i$ is pivotal | No deal possible |
| :--- | :--- | :--- | :--- |
| $i$ **Joins** | $u^{\text{in}}$ | $u^{\text{in}}$ | $u^0$ |
| $i$ **Holds out** | $u^{\text{out}}$ | $u^0$ | $u^0$ |

*Join* weakly dominates *Hold out* in every column. That is the prisoner's dilemma Moyer describes for exchange offers, with one sharpening: in a selective deal, the bottom-left cell is $u^{\text{out}}$, the primed outcome, which is strictly worse than the status quo. Holding out does not preserve your position. It hands your recovery to the people who did not hold out.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.85:* "those not participating in the exchange may be better off than those that do, but if too many hold out, all will be worse off. This is the general game theory problem known as the “prisoner’s dilemma.”"
>
> **Annotation.** Moyer's holdout problem runs the opposite way from the uptier's. In a uniform exchange offer, the *holdout* is the free rider: it keeps its old claim at full face while the participants deleverage the company and make the old claim safer. The game's danger is that everyone free-rides and the deal fails. The issuer's response, in Moyer's era, was to make holding out costly (covenant stripping, structural subordination), which is the coercive exchange of §13.1. The non-pro-rata uptier takes that logic to its limit: it makes holding out *maximally* costly and then removes the option to participate from most holders. The payoff matrix above is the result. The 2026 desk departs from Moyer's framing in what it measures. Moyer asks: what participation rate makes the deal work? The desk asks: given the holder register, what is the probability *this* holder is in the minimal winning coalition? That second question is a combinatorial optimization, and it is the sponsor's.

**The sponsor's problem is a knapsack.** The sponsor (acting through the borrower) does not want every lender. It wants the cheapest set of lenders that clears the threshold. Let $c_i$ be the per-dollar concession needed to bring lender $i$ in: the exchange ratio, the new-money economics, the fees. Then

$$
\min_{S \subseteq \{1,\dots,n\}} \sum_{i \in S} c_i w_i \quad \text{subject to} \quad \sum_{i \in S} w_i \ge \theta + \varepsilon .
$$

This is a 0–1 knapsack in its minimization form. It is NP-hard in general and trivial at the sizes that matter: a loan class with a few dozen meaningful holders, of which the top dozen hold most of it, can be brute-forced in milliseconds. The slack $\varepsilon$ is not decorative. It covers holdings that change hands between signing and closing, disputed votes, and the holders who simply do not respond.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.87:* "the “conscious” participation rate must make up for certain “innocent” holdouts."
>
> **Annotation.** In a public bond exchange the innocent holdouts are retail holders who never read the notice. In a loan uptier they are the lenders the sponsor never called. The sponsor's coalition must clear $\theta$ with a margin $\varepsilon$, and the knapsack solution is what determines who is "innocent." The modern twist is that innocence is now a choice made by the counterparty, not by the holder.

The cost vector $c_i$ is where your institutional knowledge goes, and it predicts who gets excluded. A distressed fund that can write a new-money ticket is cheap to include: it *brings* value to the coalition. A CLO is expensive. It faces concentration limits, CCC buckets and collateral-quality tests, and its documents often restrict what new instruments it can hold, so including it means designing around its constraints. A lender that has sued this sponsor before is expensive in a different way. The knapsack therefore excludes the fragmented, the constrained, and the litigious, which is roughly who the Serta and Mitel excluded lenders were: in *Serta* the appellants included CLO managers and Citadel; the Fifth Circuit noted that after the bankruptcy, the remainder of the super-priority debt was "probably held by entities like Citadel that did not participate."

**The auction between groups.** The richer version has two organized groups, $A$ and $B$, each able to reach $\theta$ by recruiting unaffiliated holders. Each proposes a package to the sponsor. The Fifth Circuit's opinion records that the eventual Excluded Lenders "had made an alternative recapitalization proposal involving a similar kind of debt swap" themselves. The losers of the Serta auction were not bystanders. They were the losing bidders.

That fact changes the auction's economics. In an ordinary auction a losing bidder gets zero. Here a losing bidder gets primed. Let $T^{\text{win}}$ be the winning group's gain from the transfer and $T^{\text{lose}}$ the losing group's loss from being primed, and let $b$ be the concession the winner pays the sponsor (better terms for the company, more new money, a bigger haircut). Group $B$ is willing to outbid $A$ as long as winning at bid $b$ beats losing:

$$
T^{\text{win}} - b \;\ge\; -T^{\text{lose}} + \pi^{\text{lit}}
\quad\Longleftrightarrow\quad
b \;\le\; T^{\text{win}} + T^{\text{lose}} - \pi^{\text{lit}} .
$$

With symmetric groups, Bertrand competition drives the winning bid to that bound. The sponsor extracts not only the winner's gain but also the loser's *fear*, less the loser's expected litigation recovery $\pi^{\text{lit}}$. This is the auction-with-externalities logic of Jehiel, Moldovanu and Stacchetti, *How (Not) to Sell Nuclear Weapons* (American Economic Review, 1996): when losing hurts, bidders pay to avoid it, and the seller can capture more than the item is worth to the winner. In LMT terms, equity captures the transfer by auctioning the right not to be its victim.

**The litigation outside option.** The term that disciplines the auction is

$$
\pi^{\text{lit}} = q \cdot \mathbb{E}[\text{damages} \mid \text{win}] - \text{cost},
$$

where $q$ is the probability a court finds the deal impermissible. $q$ depends on the clause and the forum, and since December 31, 2024, the dependence is sharp: high for an `open_market` exception litigated in the Fifth Circuit after *Serta*, low for a `purchase` exception in New York after *Mitel*. The damages term now has an anchor: \$261.13mm plus 9% interest on roughly \$895mm of excluded holdings in *Serta*. A higher $\pi^{\text{lit}}$ lowers the sponsor's take and, through the inequality, makes groups less willing to bid. That is the channel through which a court ruling moves the frequency of deals, not just their legality.

**Levers the sponsor pulls.** Buccola and Kahan (*Getting to Yes*, HLS Roundtable, Mar 25, 2025; SSRN abstract 5014946) catalog the sources of coercion in these deals. In the language of the matrix, every lever does one of three things. It lowers $u^{\text{out}}$ (how deeply non-participants are primed), it raises $u^{\text{in}} - u^0$ (how rich the participants' deal is), or it lowers the effective $\theta$. The third is the most aggressive. In Wesco/Incora (2022), per Mayer Brown's account of the record, the participating group held more than two-thirds of the 2024 notes but *not* of the 2026 notes before the transaction began; the steps amended the indentures and issued additional secured notes to clear the threshold, the participants put in \$250mm of new money for new secured notes, and the liens securing the old notes were then released. Issue yourself enough notes to become two-thirds, then vote as two-thirds. Section 13.9 follows what the courts made of that.

**Why prices drift before announcements.** One more refinement explains a pattern every loan trader has seen. Lenders do not observe $V$ exactly. Each gets a noisy signal $s_i = V + \sigma \epsilon_i$. In the global-games framework of Morris and Shin (*Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks*, American Economic Review, 1998), a coordination game with noisy private signals has a unique threshold equilibrium: each player joins the coalition if and only if its signal falls below a cutoff $s^*$, so the coalition forms if and only if $V$ is below some $V^*$. The cutoff is common knowledge in equilibrium, which means *the act of organizing is itself a signal that the organizers' estimates of $V$ are low*. Loan prices drift down as groups organize, before anything is announced. For the desk, an organizing signal (counsel hired, a Rule 2019 statement, a co-op reported) is a downward update on $V$ and an upward update on the PRS at the same time.

> **Poker Table.** "The sponsor isn't a player," Ines says. "The sponsor is the dealer, and the dealer chooses who sees the flop. Every lender at the table thinks they're playing the other lenders. They're playing for a seat." She taps the screen. "So when that client offers the Larkspur loan at 78, I don't ask what the loan is worth. I ask which seat the seller has. A seller who got a seat doesn't sell at 78; they're wall-crossed or they're about to be paid. A seller who knows they don't have a seat sells at whatever clears, because they've seen the flop from the outside and it's ugly. A seller who doesn't know either way is the only one I want to trade with, and I can't tell them apart from the second one." Her hand history, replayed through markouts: suppose the desk had bought the \$15mm at 78, the uptier closed three weeks later, and the excluded tranche marked at 52 *(illustrative)*. The markout is $-26$ points, or $-\$3.9$mm, on one ticket. Across many such hands the average markout on "client sells after an organizing headline" is the market's estimate of $\Pr(\text{excluded}) \cdot \mathbb{E}[\Delta R^{\text{excl}}]$, which is exactly what §13.8 tries to forecast before the headline.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.86:* "as in poker, which is analogous because the “multiple-hand” format of the game is similar to the series of transactions in the distressed marketplace, to be effective one must have a credible “bluff.”"
>
> **Annotation.** Moyer's point is about repeated play: an investor who never holds out cannot threaten to, so investors sometimes act against their immediate interest to keep the threat credible for future deals. The LMT era made this literal. A small set of sponsors and a small set of distressed funds meet across many capital structures, and a sponsor's history of non-pro-rata deals is a public record of its type. That is why `sponsor_repeat_lme` is a feature and why it carries a positive sign. Lenders have repeated-game reputations too, and the cooperation agreement (§13.5) is the institution they built to make their threats credible collectively when no single lender's bluff is large enough to matter.

## 13.5 Game Theory II: Cooperation Agreements as Commitment Devices

By Thursday the Larkspur lenders who have not been called have found each other, the way excluded lenders always do: by comparing notes on who has not been called. By Friday they have counsel, a financial advisor, and a forty-page document with a sunset clause. The Ad Hoc Group, represented by counsel, announces in unison that it has "organized." (Cooperation agreements signed in this book so far: 2.)

Mags reads it twice. "In 1991 this was a steering committee and a handshake. Now it's a transfer restriction with a joinder." She puts it down. "It's better. Don't repeat that."

**What the document does to the game.** A cooperation agreement is a set of lenders $C$, with combined holdings $s_C = \sum_{i \in C} w_i$, who promise not to negotiate separately, require any buyer of their loans to sign on, and agree on a sunset date. The number that matters is $s_C$ against $1 - \theta$. If $s_C > 1 - \theta$, any coalition $S$ that avoids the co-op satisfies

$$
\sum_{i \in S} w_i \;\le\; 1 - s_C \;<\; \theta ,
$$

so it cannot pass the amendment. Every winning coalition must contain a co-op member, and the no-separate-deal covenant turns "contains a member" into "contains the co-op." The sponsor's knapsack from §13.4 has no feasible solution that leaves the group out. The $n$-lender game, with its invitation list and its prisoner's dilemma, collapses into bargaining between two players: the sponsor and $C$.

> **Poker Table.** "A co-op," says Ines, "is the players agreeing not to play heads-up against the house. One at a time, every one of them can be dealt out. Together they're a blocking stack, and the dealer has to deal with the stack." Her hand history: the Larkspur loan, bid 78 before the co-op headline, trades at 81 the morning after *(illustrative)*. The three points are the market repricing $\Pr(\text{excluded})$, not $V$.

**Nash bargaining.** Let $\Pi$ be the joint surplus from a deal (avoided Chapter 11 costs, runway, the equity's option value from an extension), $d_C$ the co-op's disagreement payoff (its litigation value or its Chapter 11 recovery), and $d_{\text{sp}}$ the sponsor's (a third-party "deal away," or Chapter 11). The generalized Nash solution maximizes $(\Pi_C - d_C)^{\eta}(\Pi_{\text{sp}} - d_{\text{sp}})^{1-\eta}$ subject to $\Pi_C + \Pi_{\text{sp}} = \Pi$, where $\eta \in (0,1)$ is the co-op's bargaining weight. Take logs and differentiate in $\Pi_C$:

$$
\frac{\eta}{\Pi_C - d_C} = \frac{1-\eta}{\Pi - \Pi_C - d_{\text{sp}}}
\quad\Longrightarrow\quad
\Pi_C = d_C + \eta\,\big(\Pi - d_C - d_{\text{sp}}\big),
$$

with the symmetric split at $\eta = \tfrac12$. Two boundary conditions matter. A deal exists only if $\Pi \ge d_C + d_{\text{sp}}$; otherwise each side's outside option beats the deal, and that is when you see deals away and free-fall filings. Inside the deal region, the comparative static is linear and brutal:

$$
\frac{\partial \Pi_C}{\partial d_{\text{sp}}} = -\eta .
$$

Every dollar of credible outside financing the sponsor can line up costs the co-op $\eta$ dollars at the table. This is why deals away came back in 2025, often with six-month par calls (Wachtell, Feb 2026). The par call makes the threat cheap: if the co-op folds later, the sponsor refinances the outside money at par after six months, so the cost of *executing* the threat is roughly six months of excess spread plus fees, while $d_{\text{sp}}$ rises by the full value of the alternative. The co-op's counter is to be the cheapest financing in the room. Miller (SSRN abstract 5549919) finds that "by operating collectively, incumbent lenders outbid third-party financing offers."

**Carve-out premiums are Shapley values.** Inside the co-op, members bargain with each other, and small holders have more power than their size suggests. Treat the co-op's blocking power as a weighted majority game in which a subset $T \subseteq C$ blocks if $\sum_{i \in T} w_i > 1 - \theta$. The Shapley value of member $i$ is the probability, over random joining orders, that $i$ is the member who turns a non-blocking subset into a blocking one:

$$
\phi_i = \sum_{T \subseteq C \setminus \{i\}} \frac{|T|!\,(|C| - |T| - 1)!}{|C|!}\,\big(v(T \cup \{i\}) - v(T)\big), \qquad v(T) = \mathbf{1}\Big[\textstyle\sum_{j \in T} w_j > 1 - \theta\Big].
$$

Take a lien release with $\theta = \tfrac23$, so blocking needs more than a third, and a co-op of four: A holds 25%, B 6%, C and D 3% each, 37% in all. The blocking subsets are $\{A,B,C\}$ and $\{A,B,D\}$ (34% each) and all four; $\{A,C,D\}$ reaches only 31%. A and B sit in every blocking subset, so both hold vetoes. Counting orderings gives $\phi = (\tfrac{5}{12}, \tfrac{5}{12}, \tfrac{1}{12}, \tfrac{1}{12})$. B holds a quarter of A's position and an equal share of the blocking power. When B asks for a carve-out premium (a larger new-money allocation, a bigger backstop fee), it is asking to be paid its Shapley value instead of its pro rata share, and the arithmetic is on its side. A steering committee's carve-out premium is a Shapley value with a law firm attached. The code in §13.8 checks these four numbers.

**Three flavours, one failure mode.** Co-ops come *open* (any holder of the class may join), *closed* (membership fixed at signing), or *tiered* (anyone may join; early signers get the premium). A closed co-op that clears $\theta$ on its own is no longer a defense against a non-pro-rata deal. It *is* one, waiting for a term sheet; Miller (2025) calls the pattern "inclusive, but unequal." This is why `coop_reported` carries the split sign in the §13.2.1 table: it lowers the probability of a deal that excludes the co-op and raises the probability of *some* LMT, because a co-op that can block can also deliver.

**The antitrust attack is an attack on the commitment device.** Wachtell reports that "antitrust challenges in connection with cooperation agreements (Optimum and Selecta) are in their early days." In the model, a successful challenge voids the no-separate-deal covenant, $s_C$ becomes a sum of individual holdings that can each be bid away, and the game reverts to the §13.4 auction. Issuers have found a contractual route to the same place: Seaton (SSRN abstract 5247506) reports that Warner Bros. Discovery's 2025 bonds pioneered an "anti-cartel" provision, and that issuers' equity falls on co-op news. The second fact is the Nash solution showing up in a stock price: a co-op raises $d_C$, and the sponsor's share falls by $1 - \eta$ per dollar of it.

> **Trend Watch.** *From auctions to bargaining, 2024–2026.* **Structures:** within a month of the Fifth Circuit's *Serta* ruling the market had a replacement, "amend-extend-and-exchange," which was "deployed throughout 2025"; deals away returned (Optimum/Altice USA, Altice International, Liberty Puerto Rico, KIK), often with six-month par calls (Wachtell Lipton, Feb 3, 2026). **Mix:** 25 LMEs closed in H1 2026 against 24 in H1 2025, but "the coercive uptier structures that defined 2025 have all but vanished," with equity handovers and consensual amend-and-extends dominating (9fin, Aug 28, 2026). **Hazard:** the Federal Reserve's *Financial Stability Report* of Nov 7, 2025 said the volume-weighted leveraged-loan default rate "stayed well below its historical median" while defaults including distressed exchanges "continued to be elevated relative to history"; the May 8, 2026 report repeated the point and added that in private credit "the elevated usage of payment-in-kind (PIK) provisions indicates some borrowers may face repayment difficulties." **Supply:** "\$580 billion of loans and \$625 billion of high-yield bonds mature between 2027 and 2029" (Wachtell). **What it means for the desk:** the modal 2026 game is the bilateral one of this section, not the auction of §13.4. Model `coop_reported` and deal-away capacity explicitly, let $\Pr(\text{non-pro-rata} \mid \text{LMT})$ fall with vintage, and keep the re-default hazard from the Desk Myth box: a maturity wall met by consensual extensions is a wall of candidates for a second LMT.

## 13.6 Drop-Downs: Collateral Leakage Arithmetic

An uptier reorders the claims and leaves the assets where they are. A drop-down leaves the claims where they are and moves the assets. Same transfer, different mechanism, and a different payoff shape.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.244:* "if the existing bank debt has a lien on substantially all the assets, there may be little or nothing to offer."
>
> **Annotation.** Moyer is describing the constraint on a classic coercive exchange: the issuer wants to offer bondholders secured paper, but the banks already hold the collateral. The drop-down is the modern answer to his problem. If nothing is unencumbered, *manufacture* unencumbered collateral by moving assets out of the restricted group through the investment and unrestricted-subsidiary baskets, then grant liens on them. Moyer's next item suggests offering "a structurally senior security"; the drop-down does both at once, because debt issued by the unrestricted subsidiary is structurally senior to the parent's lenders on the assets that moved. Where the desk departs: Moyer treats the absence of free collateral as a constraint. The 2026 desk treats it as a quantity, $C^{\text{unsub}}$, that a parser can measure and a model can rank.

**The arithmetic.** Let the collateral group be worth $V$ before the deal. The borrower moves assets worth $T$ to an unrestricted subsidiary, with $T \le C^{\text{unsub}}$ as declared at the time of the investment. (Agreements often let the borrower value the investment itself, in good faith, which makes $C^{\text{unsub}}$ a cap on the *declared* value of $T$, not its economic value. Read the valuation clause before you trust the cap.) The subsidiary borrows $D_u$ against the assets, structurally senior on them, and a fraction $\phi$ of the proceeds comes back into the collateral group as cash or debt paydown. The restricted group keeps the subsidiary's equity, worth $(T - D_u)^+$ at resolution. The existing lenders now recover

$$
R^{\text{post}}(V) = \frac{\min\!\big(V - T + \phi D_u + (T - D_u)^+,\; F\big)}{F}.
$$

Sanity checks: $T = 0$ returns $R_0(V) = \min(V,F)/F$. With $\phi = 1$ and $D_u = T$ the lenders keep every dollar but swap an asset for cash, and cash is the first thing a distressed company spends (the $\kappa$ of §13.3 again). The J.Crew trapdoor is the opposite corner, $\phi \to 0$ and $D_u \to T$: the asset leaves, is levered to the hilt, and the proceeds pay a different class. Then

$$
\Delta R(V) = R_0(V) - R^{\text{post}}(V) = \frac{\min(V, F) - \min(V - T, F)}{F} =
\begin{cases}
T/F, & V \le F, \\[1ex]
(F + T - V)/F, & F < V < F + T, \\[1ex]
0, & V \ge F + T.
\end{cases}
$$

Compare the shape with §13.3. The uptier's excluded lender wrote a *digital put*: it loses everything below $K_1$ and little above. The drop-down's victim sold a *forward*: it loses $T/F$ in every state where it matters. And for any $\phi \ge 0$ the loss is capped by capacity, because $V - T + \phi D_u + (T - D_u)^+ \ge V - T$ implies

$$
\Delta R(V) \;\le\; \frac{T}{F} \;\le\; \frac{C^{\text{unsub}}}{F}.
$$

That bound is why `unsub_capacity_pct_ev` is a feature, and why the IP blockers exist: a blocker sets $T$ to zero for the assets it names. It also tells you how the market prices the two species. A digital put is a tail problem that the market prices slowly, as the probability of a low $V$ rises. A forward is a level problem that the market prices on the day the investment is announced.

Kaz has been reading the J.Crew filings. "So the restricted subsidiaries are on probation."

"In a sense," says Theo.

"And the unrestricted subsidiary has been released. For good behavior?"

"Released, yes," says Mags. "Good behavior, never." She is right on the law: an unrestricted subsidiary sits outside the covenants, which is exactly why value parked there is beyond the lenders' reach.

> **Docket Diary.** *J.Crew, 2016–2020.* **Dec 5, 2016:** J.Crew discloses that it "invest[ed] certain intellectual property in the Company's wholly owned unrestricted subsidiary, J.Crew Domestic Brand, LLC," and says the step "fully complied with the Company's Term Loan Agreement." **Feb 1, 2017:** the company sues Wilmington Savings Fund Society, the successor term loan agent, to confirm that position (8-K Ex. 99.1). **July 13, 2017:** the exchange closes. \$565.7mm of 7.75%/8.50% PIK toggle notes due 2019, issued at a holding company and structurally junior to the term loans, are exchanged for \$249.596mm of 13% Senior Secured Notes due 2021 of J.Crew Brand, LLC and J.Crew Brand Corp., "secured on a first priority lien basis by a 72.04% interest in the Licensed Marks," plus \$189.688mm of preferred stock and about 15% of parent equity. \$150mm of term loans are repurchased; \$97mm of new-money notes are issued at a 3% discount; the marks are licensed back for \$42.5mm plus \$16.5mm per year; and the agent is directed "to dismiss, with prejudice, certain litigation" (8-K, July 2017). **May 4, 2020:** Chapter 11 (Bankr. E.D. Va., No. 20-32181); emergence in September 2020. *The Ad Hoc Group, represented by counsel:* "We note for the record that the junior class became the senior class on the brand." In the formula, the PIK holders were the "different class" that $\phi \approx 0$ funds, and the term-lender consent and dismissal were, in effect, bought with the \$150mm repurchase: the knapsack again.

**PetSmart and the guarantee lever.** BC Partners bought PetSmart in 2015 for about \$8.7bn and bought Chewy in May 2017 for \$3.35bn. In June 2018 PetSmart moved 20% of Chewy to its parent, Argos Holdings, and 16.5% to an unrestricted subsidiary, and sued the term loan agent, Citibank, that month *(approx.; Wikipedia, citing Reuters, the FT and the WSJ)*. The lever was the guarantor-release clause: the position was that a guarantor that stops being wholly owned is released. Moving 36.5% of the shares was argued to release all of the guarantee, so the effective $T$ was the guarantee's value, not the shares'. That is leverage on the transfer, and it is why the code should compute $T$ from the release clause, not from the share count. Chewy's S-1 (Apr 29, 2019) records that "PetSmart settled existing litigation with the agent for its term loan lenders regarding these transfers in April 2019," and adds that "there can be no assurance that other PetSmart creditors may not seek to challenge these transfers." Chewy listed in June 2019 at \$22. The `chewy_blocker` (no release merely because a guarantor stops being wholly owned) exists because of those two sentences.

**When steps are judged together.** In *STG Logistics* (N.Y. Sup. Ct., 2025), the court viewed "amendments permitting a covenant strip, a drop-down exchange, and an intercompany loan – as a single integrated plan for purposes of analyzing 'sacred rights' (i.e., unanimous lender vote) claims," denied the motion to dismiss, and "shortly following the decision, the company filed for bankruptcy" (Wachtell, Feb 2026). A drop-down that needs only majority votes step by step can need unanimity as a whole. Section 13.9 makes that precise.

## 13.7 Double-Dips and Pari-Plus: A Waterfall Engine That Conserves Value

"I'm told the new financing is a double-dip," says Kaz. "Is that a hygiene issue?"

"At a party," says Mags. "In a capital structure, it's a structure."

The desk's working definition: a guarantee and an intercompany loan walk into the same collateral pool and order twice. Pari-plus adds a foreign subsidiary that buys the first round.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.165:* "Grants of security interests can similarly be viewed as provisions to override the general rule that property in an estate is shared pro rata among creditors."
>
> **Annotation.** Moyer frames liens (and, on the same page, guarantees and subordination) as overrides of the pari passu default. A double-dip is an override built from *claims* instead of liens: the new lender holds two claims of equal rank against the same obligor for one dollar of credit. Nothing about it is senior. It is counted twice in the pro rata denominator, and pro rata sharing does the rest. The desk's departure is computational. Moyer's overrides can be read off a priority chart. A double-dip can only be read off a *graph* of obligors, claims and equity ownership, which is why the engine below is a fixed-point solver rather than a lookup table.

**The closed form.** A special-purpose vehicle (SPV) borrows $F_2$ from new lenders and lends the cash to OpCo under an intercompany note that ranks pari passu with OpCo's existing first lien, $F_1$. OpCo also guarantees the SPV's debt, pari passu. In a pro rata distribution of OpCo's value $V$, three claims share: the first lien ($F_1$), the guarantee ($F_2$) and the note ($F_2$), at the rate $\rho = \min\big(1, V/(F_1 + 2F_2)\big)$. The new lenders collect $\rho F_2$ on the guarantee directly and, through the SPV, the $\rho F_2$ it collects on the note, capped at what they are owed. While $2\rho < 1$, that is, $V < (F_1 + 2F_2)/2$,

$$
R^{\text{DD}} = \frac{2V}{F_1 + 2F_2}, \qquad R^{\text{1L}} = \frac{V}{F_1 + 2F_2}.
$$

The double-dipper recovers exactly twice what the first lien recovers, from a claim of the same rank. With illustrative numbers $F_1 = 1{,}000$, $F_2 = 500$ (\$mm) and $V = 800$: without the dip both would get $800/1{,}500 = 53.3$ cents; with it, the first lien gets 40 and the new money 80. The \$133mm the first lien lost is exactly the \$133mm the new money gained. Check that before you check anything else.

Above $V = F_2 + F_1/2$ the new lenders are paid in full, and the excess the SPV collects on the note is SPV equity. If OpCo owns the SPV, that equity flows back into OpCo, raises every pro rata payment including the note's, and the solution is a fixed point. Let $A$ be OpCo's distributable value including the returned equity $(2\rho - 1)F_2$, with $\rho = A/(F_1 + 2F_2)$. Then

$$
A = V + \Big(\frac{2A}{F_1 + 2F_2} - 1\Big)F_2
\quad\Longrightarrow\quad
\rho = \frac{V - F_2}{F_1},
$$

so the new lenders take $F_2$ and the first lien takes everything else, as conservation demands. The regimes meet at $\rho = \tfrac12$, so recoveries are continuous and monotone in $V$. The fixed-point map has slope $2F_2/(F_1 + 2F_2) < 1$, so simple iteration converges geometrically.

Real structures have more entities, and the general tool is the clearing framework of Eisenberg and Noe (*Systemic Risk in Financial Systems*, Management Science, 2001), extended to priority classes. For a debtor $d$ with external value $e_d$, define its distributable value as external value plus intercompany receipts plus the residual equity $E_c$ of the subsidiaries $c$ it owns. A claim $j$ of rank $r$ owed by $d$ is then paid

$$
A_d(p) = e_d + \sum_{\ell:\ \text{cred}(\ell) = d} p_\ell + \sum_{c:\ \text{parent}(c) = d} E_c(p),
\qquad
p_j = \bar p_j \cdot \min\!\left(1,\ \frac{\big(A_d - \sum_{\text{rank}(m) < r} p_m\big)^+}{\sum_{\text{rank}(m) = r} \bar p_m}\right),
$$

where the sums in the fraction run over $d$'s own claims and $\bar p_j$ is the amount still owed on claim $j$ (face, less anything already collected from a co-obligor on the same debt). Iterate $p \mapsto \Phi(p)$ until $\|p^{(k+1)} - p^{(k)}\|_\infty < 10^{-10}$. The invariant is conservation: payments to outside creditors plus residual outside equity equal total external value, because every intercompany payment is one entity's outflow and another's inflow.

**Pari-plus.** Add a non-guarantor foreign subsidiary worth $V_f$ that guarantees the new money directly. Before the deal, $V_f$ reached the first lien only as equity flowing up to OpCo. After it, the new lenders take $\min(F_2, V_f)$ first and double-dip OpCo for the deficiency, so the first lien loses the foreign value and is diluted on the rest. With $V_f = 0$ the structure collapses to the double-dip, which the code asserts. Sabre's May 2023 financing is the template: a "\$665 million new senior secured credit facility" from "lenders led by affiliates of Centerbridge Partners, L.P." to Sabre Financial Borrower, LLC, "a newly created wholly-owned subsidiary of Sabre GLBL," "secured by an intercompany loan by the Borrower to Sabre GLBL" and by "direct guarantees from, and security interest in assets of, certain foreign subsidiaries of Sabre," with proceeds funding capped tenders for three series of notes (8-K Ex. 99.1, May 25, 2023).

### 13.7.1 Case Study: Trinseo (2023–2026), the Double-Dip Meets Chapter 11

On September 8, 2023, Trinseo announced "a senior secured term loan facility of \$1,077 million" borrowed by two SPVs, Trinseo Luxco Finance SPV S.à r.l. and Trinseo NA Finance SPV LLC. Of that, \$948mm was on-lent to OpCo as "2023 Term Loans" under its 2017 credit agreement. The SPV loans paid Term SOFR + 8.50% and matured May 3, 2028; the intercompany loans paid Adjusted Term SOFR + 9.66% and matured May 3, 2030. Proceeds repaid the 2018 term loans and redeemed \$385mm of 5.375% notes due 2025 (8-K, Sept 2023). Note the design: the intercompany loan pays more and runs longer than the external loan it funds, so the claim that shares pro rata with OpCo's lenders grows faster than the debt behind it.

Trinseo filed for Chapter 11 on May 26, 2026 (Bankr. S.D. Tex., lead case No. 26-90545, Judge Christopher Lopez). Its disclosure statement (dated May 25, 2026, filed as 8-K Ex. 99.2) is the first full-cycle test of the closed form, and the closed form turns out to be conservative. Funded debt was about \$2.9bn. Estimated recoveries: revolver (\$348mm) 99–100%; Super HoldCo first-lien term loans (\$1,266mm, including a \$115mm Tranche C from January 2025) **60–78%**; OpCo 2028 term loans (\$716mm) **2–9%**; 7.625% notes due 2029 (\$390mm) 0%. The OpCo intercompany term loans, \$1,508mm, were pledged to the Super HoldCo lenders. The restructuring support agreement of May 13, 2026 had 100% of the revolver, about 99.9% of the Super HoldCo first lien and about 86% of the OpCo term loans; 2025 adjusted EBITDA was \$162.5mm; the plan contemplates an \$850mm exit term loan.

The stylized engine says the double-dipper recovers twice what the first lien does. Trinseo's estimated multiple is roughly 7 to 39 (60/9 to 78/2). The engine's job is to say where the excess comes from: a revolver senior to everything; an intercompany claim of \$1,508mm against the \$948mm originally on-lent (later tranches, accrued interest and the make-wholes live in that gap; we do not decompose it); and collateral at Super HoldCo that OpCo's lenders do not share. The make-wholes are where the fight went. An "OpCo Investigation" flagged the intercompany make-whole claims, and the proposed settlement took the form of "a gift through a carve-out of the Collateral securing the Allowed OpCo Intercompany Term Loan Claims." CastleKnight, holding OpCo 2028 loans and 2029 notes, objects, and with Elevation CLO 2013-1 brought an adversary proceeding (No. 26-03208) seeking declaratory judgment on lien validity, priority and subordination; on June 23, 2026 the plaintiffs opposed judgment-on-the-pleadings motions by the debtors and the "Super HoldCo Lender Defendants."

How a systematic desk flags it: the September 2023 8-K is machine-readable evidence of the three ingredients (a new SPV obligor, an intercompany loan pari with the existing first lien, an upstream guarantee). The parser emits `double_dip_present = 1`, the clearing engine reprices every OpCo-level claim with the new denominator, and the trade is the pair: long the dip, short (or underweight) the claims it dilutes. The pair is a bet on the recovery multiple, which the engine computes across $V$. Exercise 4 asks you to rebuild the stack and find the $V$ that reproduces the disclosure statement's ranges.

> **Ways This Blows Up.** *Five ways a clearing engine lies.* (1) **Circular ownership with no outside value.** If entities own each other in a loop that has no external value, Eisenberg–Noe can have many clearing vectors: iterating down from face finds the greatest, up from zero the least. Run both. If they differ, the answer is a legal question, not a numerical one. (2) **Deficiency conventions.** The engine assumes a creditor may assert full face against each obligor until paid in full, collecting no more than face in total. Some documents and jurisdictions net co-obligor recoveries first, which shrinks the dip. Make it a parameter, never a constant. (3) **Substantive consolidation.** Moyer observes that "a substantive consolidation makes the two claims pari passu" (Moyer_Distressed_Debt_Analysis p.305). Consolidate OpCo and the SPV and the guarantee and the note become one claim; the dip disappears. (4) **The challenge list.** Moyer's checklist of attacks (p.351; list items joined) reads like an inventory of the engine's hidden parameters: "Invalidity of guarantees · Substantive consolidation · Critical creditor/vendor status · Interpretation of contractual subordination language · Violations of covenants · Transfers that might be deemed fraudulent conveyances." Each one deletes or resizes an edge in the claim graph. (5) **Claims at face plus premium.** Trinseo shows that the allowed amount of an intercompany claim is itself a litigated number. Price the dip over a range of allowed claims, not at one.

## 13.8 The Priming Risk Score

"You've told me how much I lose if I'm dealt out," says Ines. "Now tell me how often the dealer deals."

**From hazard to a fixed-horizon score.** The template is the proportional-hazards model Bohn and Stein use for default (Bohn_Stein_Active_Credit_Portfolio_Management p.233), applied to the LMT event:

$$
\lambda^{\text{LMT}}_i(t) = \lambda_0(t)\,e^{\beta^{\top} x_i(t)}, \qquad
\text{PRS}_i(t, h) = 1 - \exp\!\Big(-\int_t^{t+h} \lambda^{\text{LMT}}_i(u)\,du\Big) \in [0,1].
$$

($\lambda^{\text{LMT}}$ carries a superscript because $\lambda_t$ is reserved for default.) With roughly a hundred observed LMTs (Roe and Rotaru hand-collected 89 coercive ones), a time-varying baseline is a luxury. Fit at a fixed horizon $h = 1$ year with a logistic link on standardized features $z_i$: $\text{PRS}_i = \sigma(\beta_0 + \beta^{\top} z_i)$, $\sigma(u) = 1/(1+e^{-u})$. For small probabilities $1 - \exp(-e^{u}) \approx e^{u} \approx \sigma(u)$, so the logistic and the Cox model agree in the region where the desk lives.

**Priors, because 89 is not a sample size.** Put $\beta \sim \mathcal{N}(\beta^{\text{prior}}, \tau^2 I)$ on the slopes and a Beta$(a,b)$ prior on the base rate $\pi_0 = \sigma(\beta_0)$, the base-rate framing of Bohn–Stein p.447. In $\beta_0$-space, including the Jacobian, that prior has log density $a \ln \sigma(\beta_0) + b \ln(1 - \sigma(\beta_0))$. The MAP estimate is

$$
\hat\beta = \arg\max_{\beta}\; \sum_{i=1}^{n}\big[y_i \eta_i - \ln(1 + e^{\eta_i})\big] - \frac{\lVert \beta_{1:k} - \beta^{\text{prior}} \rVert^2}{2\tau^2} + a \ln \sigma(\beta_0) + b \ln\!\big(1 - \sigma(\beta_0)\big), \qquad \eta_i = \beta_0 + \beta_{1:k}^{\top} z_i .
$$

The first-order condition in $\beta_0$ says exactly what the base-rate prior does: $\sum_i (y_i - \hat p_i) + a(1 - \sigma(\hat\beta_0)) - b\,\sigma(\hat\beta_0) = 0$, so the mean fitted PRS equals the observed event rate plus a correction of order $\max(a,b)/n$. For the slopes, a quadratic expansion of the log-likelihood around the MLE (information matrix $H$) gives the shrinkage form

$$
\hat\beta_{1:k} \approx \Lambda\,\beta^{\text{prior}} + (I - \Lambda)\,\hat\beta^{\text{MLE}}, \qquad \Lambda = (H + \tau^{-2} I)^{-1}\tau^{-2},
$$

with boundary conditions $\tau \to \infty \Rightarrow \Lambda \to 0$ (the MLE) and $\tau \to 0 \Rightarrow \Lambda \to I$ (the prior). The code tests both limits.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.447:* "the Bayesian approach answers the question, “Given that I know that I have already observed zero defaults, what is the highest probability of default that I could expect with 95 percent certainty?”"
>
> **Annotation.** Bohn and Stein pose this for portfolios with few or no defaults. LMTs are the same problem one level up: the event is rare, its definition changed in 2020, and the population that generated the history (pre-blocker documents) is not the population you are pricing. The Beta prior turns "we have seen few events like this" into an honest upper bound rather than a zero. Where the desk departs from them: the prior must be *vintage-aware*. A base rate estimated on 2020–2022 documents overstates the risk of a 2026 agreement with a Serta blocker (Trend Watch, §13.3), so the prior's mean should come from events in documents of the same vintage, and its width should admit that there are few of them.

**What the desk prices.** The score is one factor of the expected priming loss, in fraction of par:

$$
\text{EPL}_i = \underbrace{\Pr(\text{LMT})}_{\text{PRS}_i} \cdot \Pr(\text{non-pro-rata} \mid \text{LMT}) \cdot \Pr(\text{excluded} \mid \text{NPR}) \cdot \mathbb{E}^{\mathbb{P}}\big[\Delta R^{\text{excl}}\big],
$$

and the quote is approximately $P \approx P_{\text{no-LMT}} - 100\cdot\text{EPL}_i - \text{risk premium}$, in points. The last factor comes from §13.3 (or §13.6 for a drop-down), the third from the knapsack of §13.4, the second from the co-op state of §13.5. **Measure discipline:** PRS is a $\mathbb{P}$-forecast of an event. The price impact is $\mathbb{Q}$-flavoured, because the marginal holder is averse to exactly this jump, and the *Serta* damages award shows a court measuring it with a market price. Never calibrate PRS to prices; regress price residuals on EPL and call the slope the premium.

> **Ways This Blows Up.** *Separation.* On the training data, `loan_px < 80` and `runway_months < 9` together nearly separate events from non-events. An unpenalized logistic responds by sending those coefficients toward infinity and reporting a PRS of 1.000 for every distressed name, which is confident and useless. The Gaussian prior keeps $\hat\beta$ finite. The prior's most important covariate is Theo's 13-week model, reborn as `runway_months`: the spreadsheet he carries for emotional support is now the only thing standing between the desk and an infinite coefficient.

### Specification for AI Implementation

*What ROBO built from the vague version.* Theo typed: "Flag every borrower that could be primed." ROBO returned the entire index, correctly: any agreement can be amended with 100% consent. The precise version names $\theta$ for the specific action, the `buyback_exception` enum, and a horizon. ROBO returned 11 names. One was the desk's own warehouse line.

**Schemas.** `entities`: `id` (str), `value` (float, \$mm, $\ge 0$), `parent` (entity id or `None`). `claims`: `id`, `creditor` (`"ext"` or entity id), `debtor` (entity id), `face` (\$mm, $>0$), `rank` (int, 1 = most senior), `reduce_by` (list of claim ids on the same debt owed by co-obligors). `features`: one row per borrower-year, columns as in the §13.2.1 table; `buyback_exception` one-hot; `y` = 1 if an LMT closed within 12 months. **Edge cases:** no claims at an entity (all value is residual); $N = 0$ or $p = 1$ in the uptier (guard the divisions); co-op share above $1 - \theta$ (return `None`, never an empty coalition); burn $\le 0$ in the runway (cap at 120 months); quasi-separation (prior required, never `tau=inf` in production). **Stability:** overflow-safe logistic via `tanh`; `logaddexp` in the likelihood; Newton steps with step-halving; clearing iteration capped at 10,000 with a convergence error, not a silent return.

<!-- EXPLAIN: Listing 13.1 -->
> **Code Companion: Listing 13.1.** Eisenberg-Noe clearing: pay by rank, pro rata within rank, route intercompany receipts and subsidiary equity upward; iterate to a fixed point. The full python listing is in [Appendix F, Listing 13.1](#code-13-1).

<!-- EXPLAIN: Listing 13.2 -->
> **Code Companion: Listing 13.2.** Per-dollar recoveries (R0, first-out, second-out, excluded), Section 13.3. The full python listing is in [Appendix F, Listing 13.2](#code-13-2).

<!-- EXPLAIN: Listing 13.3 -->
> **Code Companion: Listing 13.3.** MAP logistic: N(prior, tau^2) on slopes, Beta(a, b) on sig(b0). The full python listing is in [Appendix F, Listing 13.3](#code-13-3).

The three blocks are cumulative: (c) composes the knapsack's participation share from (b) and the Serta-shaped expected transfer, and in production the drop-down and double-dip transfers from (a) slot into the same last factor.

## 13.9 Autopsies: The Court Is a Random Variable

The $q$ in the litigation option of §13.4 has been the most volatile parameter on the desk since 2023. Two features carry it: the clause and the doctrine.

**Steps versus plans.** Write an LMT as a composition of document moves $\mathcal{D}_0 \to \mathcal{D}_1 \to \cdots \to \mathcal{D}_m$, where step $k$ needs holders with share $v_k(\mathcal{D}_{k-1})$ of the class to clear $\theta_k$. A step-by-step court asks whether $v_k(\mathcal{D}_{k-1}) \ge \theta_k$ for every $k$. An integrated court treats the composite as one move and measures support before anything happened, $v(\mathcal{D}_0) \ge \max_k \theta_k$, plus unanimity for any sacred right the composite touches. The gap $g = \max_k \theta_k - v(\mathcal{D}_0)$ is the feature `integration_gap`. When $g > 0$ the deal works only in a step-by-step forum, and $q$ becomes a bet on doctrine. Wesco/Incora is the textbook case: the group held more than two-thirds of the 2024 notes but not of the 2026 notes (§13.4), used a majority to issue itself enough secured notes to reach two-thirds, then used the two-thirds to release liens. Each step clears its own bar. The composite does not. *STG Logistics* (§13.6) is the same test applied to a drop-down.

> **Docket Diary.** *Wesco Aircraft/Incora, 2022–2026.* **2022:** the transaction closes. **2024:** Judge Isgur (Bankr. S.D. Tex.) sends to trial whether the deal was an "open market purchase" or a "redemption" and whether it was a "single, integrated transaction" (Ropes & Gray via HLS Roundtable, May 21, 2024); under his "domino theory," "the majority group did not have the requisite two-thirds majority at the time of the first amendment" (Wachtell). **2025:** District Judge Crane reverses, looking "no further than the language of the agreements, the sophistication of the parties, and the 'direct effect' of a specific amendment." **Jan 13, 2026:** the Fifth Circuit dockets the appeal, *Wesco v. 2026 Noteholders*, No. 26-20018. *The Ad Hoc Group, represented by counsel:* "We were two-thirds. Eventually." In the model, $g > 0$ and $q$ swung from high to low on doctrine alone; the excluded noteholders now hold an option on a Fifth Circuit panel.

**Forum is time-varying.** In 2023 a Texas bankruptcy court found *Serta*'s "open market purchase" "clear and unambiguous" in the borrower's favor. On Dec 31, 2024 the Fifth Circuit read the same words against the borrower, and New York's First Department upheld *Mitel*'s uptier under a bare "purchase" exception; Mitel nonetheless filed for Chapter 11 on Mar 10, 2025 and emerged on June 20, 2025 owned by its lenders *(approx.; Wikipedia citing Bloomberg)*. A PRS fitted with a static forum coefficient averages a sign flip, so interact `forum_ny_vs_tx` with `buyback_exception` and a post-2024 dummy. In the bankruptcy court itself the *Serta* rule keeps spreading: in *ConvergeOne* (S.D. Tex. district court, 2025, on appeal), backstop fees on a \$245mm exit rights offering were "a form of recovery on participating creditors' pre-bankruptcy debt claims, and therefore had to be open to all creditors in the applicable class, absent robust market testing" (Wachtell). The next observations are already docketed: *Invesco v. Robertshaw* (5th Cir. No. 26-20422) and the bond-side exit-consent fight over Lions Gate/Starz's 2024 exchange of \$389,861,000 of 5.500% notes due 2029 (*CPPIB Credit Investments II v. Deutsche Bank Trust Co. Americas*, Sup. Ct. N.Y. Cnty., Mar 17, 2026). IDO or it didn't happen: LMT P&L is the one place where "idiosyncratic" was defined by two courts, in two states, on the same day.

## 13.10 Desk Debrief

- **An LMT is the difference of two waterfalls.** In low states it is zero-sum among creditors; the liquidity story lives in high states. Compute $\Delta_j(V)$ before you read the press release.
- **Know your payoff shape.** Excluded from an uptier: short a soft digital put struck at $K_1$. Victim of a drop-down: short a forward capped at $C^{\text{unsub}}/F$. Diluted by a double-dip: someone is counted twice in your denominator.
- **The sponsor solves a knapsack** and leaves out the constrained, the fragmented and the litigious. Model your invitation probability, not your participation decision.
- **A co-op above $1 - \theta$ turns an auction into a bargain.** Deal-away capacity costs the co-op $\eta$ per dollar; carve-out premiums are Shapley values. (Cooperation agreements signed in this book so far: 2. Antitrust complaints about them: 2, and counting.)
- **One word can be the whole loss.** The court is a random variable with a clause, a forum, a doctrine and a vintage.
- **PRS is $\mathbb{P}$; the price is $\mathbb{Q}$.** Never calibrate the score to prices. The prior keeps $\hat\beta$ finite, and Theo's runway is the covariate that separates.
- **The LMT is not the terminal state.** Only 22% of coercive-LME firms avoided both re-default and bankruptcy within two years. Price the next event.

### The Spec You Hand the Robot

Build `lmt_engine.py` (numpy/scipy; `rng = np.random.default_rng(13)`; runs top to bottom; values in \$mm, recoveries in fraction of par, runway in months, PRS at a 12-month horizon). (1) `waterfall_clearing(entities, claims)`: priority ranks, pro rata within rank, intercompany receipts and subsidiary equity routed to parents, `reduce_by` for co-obligor claims on one debt; stop at $\lVert \Delta p \rVert_\infty < 10^{-10}$, raise after 10,000 iterations; assert conservation to $10^{-8}$, no payment above face, monotonicity in $V$, the double-dip closed form, pari-plus collapse at $V_f = 0$. (2) `uptier`, `priming_loss`: guard $N = 0$ and $p = 1$; assert conservation, zero loss for $V \ge F + N$, full loss for $V \le K_1$; expected loss by quadrature checked against Monte Carlo and the lognormal partial expectation. (3) `min_cost_coalition`: brute force to 12 holders, greedy beyond, `None` when a co-op exceeds $1 - \theta$; `shapley` by enumeration. (4) `fit_map`: Newton with step-halving, Gaussian slope prior, Beta base-rate prior; assert the intercept first-order condition, both $\tau$ limits, the bootstrap band, signs, and a holdout Brier score below the base rate. (5) `expected_priming_loss` $=$ PRS $\times$ P(NPR $\mid$ LMT) $\times$ P(excluded $\mid$ NPR) $\times$ $\mathbb{E}[\Delta R]$, inputs in $[0,1]$. Never fit PRS to prices.

### Exercises

1. **Unblend Serta.** Redo §13.3.1 with the \$1.95bn first lien and \$450mm second lien as separate classes. Parameterize the unknown lien split of the \$1.2bn exchanged, compute $K_1$ for the excluded first-lien lenders, and find the split at which the blended 44.8-point transfer at $V = \$1.075$bn is off by more than 10 points.
2. **The 5% veto.** A co-op holds A 20%, B 10% and C 5%, and the action needs $\theta = \tfrac23$. Show that each Shapley value is $\tfrac13$. Find the smallest block of C's loans that, sold to A, destroys C's veto, and explain why C will ask for more than par.
3. **Forward or digital?** For a drop-down with $T = 300$, $D_u = 280$, $\phi = 0.1$ and $F = 2{,}000$ (\$mm, illustrative), plot $\Delta R(V)$, verify $\Delta R \le T/F$, and compute its expectation under the lognormal in block (b). Then redo it with PetSmart-style leverage, where moving 36.5% of a subsidiary's shares releases its whole guarantee.
4. **Rebuild Trinseo.** From the figures in §13.7.1, build an entity graph for `waterfall_clearing` and find ranges of $V$ and of the allowed intercompany claim that reproduce both 60–78% and 2–9%. Which parameter matters most?
5. **ROBO minimizes priming loss.** Told to "build the portfolio with the lowest expected priming loss," ROBO bought only loans in which every amendment needs unanimous consent. Explain in one sentence why the portfolio is empty, then rewrite the objective with a carry constraint, a turnover limit and units.

### Deep-Dive Resource Graph

**Podcasts**
- Bloomberg *Odd Lots*, episodes on liability management and creditor-on-creditor violence (search the archive; episode titles not verified here).
- *Cloud 9fin* and Octus podcasts on LME structures and cooperation agreements (titles not verified).

**Practitioner Writing**
- Wachtell Lipton, *Liability Management 2026: For Better or Worse* (Feb 3, 2026): https://www.wlrk.com/FirmMemos/WLRK/WLRK.29921.26.pdf
- 9fin, H1 2026 LME update (Aug 28, 2026): https://9fin.com/insights/h1-2026-lme-update
- Harvard Law School Bankruptcy Roundtable, liability-management archive: https://bankruptcyroundtable.law.harvard.edu/category/liability-management/
- *Petition* archive: https://www.petition11.com/archive
- Mayer Brown on the *Serta* remand damages (July 2026); Paul, Weiss on *Serta* and *Mitel* (Jan 10, 2025); Octus on non-pro-rata uptiers (July 16, 2024); Matt Levine's *Money Stuff* columns on uptiers (titles only).

**Academic Papers**
- Buccola and Nini (2024), *Journal of Legal Studies* 53:489, on uptier restrictions in 600+ loan agreements (SSRN abstract 4143928, via HLS).
- Roe and Rotaru (2026), 89 coercive LMEs and their aftermath (SSRN abstract 6103369; HLS Roundtable, Feb 24, 2026).
- Antill, Jiang and Wang, LMEs and renegotiation debt overhang (SSRN abstract 4821620); Buccola and Kahan, *Getting to Yes* (SSRN abstract 5014946); Seaton, defensive cooperation agreements (SSRN abstract 5247506); Miller (SSRN abstract 5549919); Huang, Lewellen and Wang, Rule 2019 data (SSRN abstract 4854111); Parikh (SSRN abstract 4410235).
- Buccola (2023), *Efficacious Answers to the Non-Pro Rata Workout*, 171 U. Pa. L. Rev. 1859; Skeen (2023), *Uptier Exchange Transactions: Lawful Innovation or Lender-on-Lender Violence?*, 40 Yale J. Reg. 408.
- Eisenberg and Noe (2001), *Systemic Risk in Financial Systems*; Morris and Shin (1998), *Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks*; Jehiel, Moldovanu and Stacchetti (1996), *How (Not) to Sell Nuclear Weapons*.

**Data & Code**
- Fifth Circuit *Serta* opinion (rev. Feb 14, 2025): https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf
- CourtListener opinions: *Serta* https://www.courtlistener.com/opinion/10333637/, *Mitel* https://www.courtlistener.com/opinion/10309794/, *CPPIB v. Deutsche Bank Trust Co. Americas* https://www.courtlistener.com/opinion/11001279/
- CourtListener dockets: Wesco appeal https://www.courtlistener.com/docket/74956914/, Robertshaw appeal https://www.courtlistener.com/docket/74695342/, Trinseo case and adversary proceeding https://www.courtlistener.com/docket/73388469/ and https://www.courtlistener.com/docket/73394456/; REST API https://www.courtlistener.com/help/api/
- SEC EDGAR, for the J.Crew, Chewy, Sabre, Trinseo and Lions Gate filings cited by date above: https://www.sec.gov/edgar
- Federal Reserve *Financial Stability Report*, Nov 2025 https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf and May 2026 https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf; FEDS Notes https://www.federalreserve.gov/econres/notes/feds-notes/

<!-- STATUS: COMPLETE -->
