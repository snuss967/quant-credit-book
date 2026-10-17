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
