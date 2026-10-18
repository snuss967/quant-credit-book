# Media & Learning Ecosystem: Podcasts, Newsletters, Talks and Books for Systematic & Special-Situations Credit

**Item:** Podcasts on credit, distressed, market structure, and quant
**Prepared:** 2026-10-17 (researcher, Edition 1 to Edition 2 pipeline)
**Feeds:** every chapter's `### Deep-Dive Resource Graph`. Main users are Ch 2, 4, 13, 14, 17, 21, 22, 24, 26, 28 and App B/C. Proposed new App D.

**Method.** Earlier briefs marked almost every podcast TITLE-ONLY. This dossier instead reads the **publishers' own RSS feeds**, which are the primary record of what was published and when. On 2026-10-17 I downloaded and parsed:

- Bloomberg/Omny: *Odd Lots* (1,289 items), *The Credit Edge by Bloomberg Intelligence* (195), *Money Stuff: The Podcast* (119), *Masters in Business* (817), *Trillions* (274).
- Libsyn: *Capital Allocators* (831), *Macro Musings* (571).
- Transistor: *Cloud 9fin* (282), *Octus Radio* (500, ending Aug 2024), *The Octus Download* (37).
- Captivate: *Flirting with Models* (128), *Top Traders Unplugged*, *ReSolve Riffs*.

Feed links came from Apple's lookup record and Bloomberg's Omny programs/playlists endpoints. Titles, guests and dates are copied from the feeds. Dates are the feed `pubDate` in UTC.

Every episode URL below returned HTTP 200 on 2026-10-17. I also confirmed that each host 404s on a made-up path (omny.fm, capitalallocators.com, flirtingwithmodels.com, share.transistor.fm). For the soft-404 hosts (podscripts.co, macromusings.libsyn.com) I checked page titles one by one.

The shared WebSearch budget ran out after 7 queries in this session, so I did no open-web discovery beyond that. Episode and season numbers appear only where the publisher's feed title carries them ("EP.209", "S4E12"). Anything unverified is left out or marked **CHECK**.

---

## 1. Headline findings

1. **There is now a dated, on-record estimate of systematic credit's market share.** On *The Credit Edge* (2026-10-08), Blackstone's Adam Dwinells (head of corporate bond strategies) put Blackstone's systematic credit at about $40B. He said it "can and should be a $100 billion business". He sized systematically managed portfolios at "about 1%–2% in US corporate credit now" and expects 20–25%, matching equities, "over the next decade". Man Numeric's Paul Kamenski said in March 2024 that quant holds "very low single digits" of fixed income. These two datapoints anchor the Ch 4 / App C trend line.
2. **The next frontier for quant credit is loans, CLOs and EM.** Acadian's Scott Richardson (*Credit Edge*, 2026-02-19) said an issuer-level selection approach works in leveraged loans and "could be extended to structured things that sit on top of that, CLOs".
3. **LME law is now a regular media beat.** 9fin runs a monthly LME-legal series (*Jane's LME Addiction*, since Jan 2025), plus *LME Doomscrolling* (since Apr 2026) and *The In-Court Report* (since Dec 2025). The recurring subjects are DQ lists, voting caps, co-op antitrust and the 2026 Serta/Del Monte/American Tire rulings. Creditor organization has become a Ch 13 state variable in its own right.
4. **The private-credit narrative arc shows up in episode titles almost month for month,** matching the Ch 17 trend research:
   - *Odd Lots*: "booming" (Nov 2023), "goes dark" (Sep 2024), "what's actually going on" (Apr 2026), "entangled with insurance" (Jul 2026).
   - *Credit Edge*: "BDC storm" (Apr 2026), then "bad PIK" (Aug 2026).
   - *Money Stuff*: OBDC/OBDC II (Nov 2025), then Boaz Weinstein's tenders (Mar 2026).
5. **No episode explains portfolio trading or ETF creation/redemption.** Across all 1,289 *Odd Lots* items, nothing matches "portfolio trading", "creation/redemption" or "authorized participant". The best market-structure audio is older:
   - Chris White (2015 and 2020)
   - Morningstar on bond pricing (2021)
   - Larry Harris on FIMSAC (2021)
   - Ellen Correia Golay on Treasury all-to-all trading (2026)

   Ch 19–20 fill a real public-explanation gap.
6. ***Flirting with Models* has only three explicitly credit or fixed-income episodes in 128:** Obenshain (2021), Ralph Smith (2022) and Rosenberg (2025). The rest is useful but adjacent.

---

## 2. Podcast episodes by book topic

Format: **Show: "Title"** (feed date), guest, URL. One line on why it is worth the time.

### 2.1 The systematic-credit industry and factors (Ch 4, 9, 11, 12)

- **Credit Edge: "Blackstone Is Predicting a Big Surge in Quant Credit Investing"** (2026-10-08), Adam Dwinells. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/blackstone-is-predicting-a-big-surge-in-quant-credit-investing
  - The shelf's Blackstone paper, updated with current AUM and market share.
- **Credit Edge: "Acadian Sees Quants Moving to Loans, CLOs"** (2026-02-19), Scott Richardson. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos
  - Covers alternative data, private credit, and execution "without giving a liver and a kidney to Goldman Sachs".
- **Man Group *Long Story Short*: "Extra Credit: Algorithmic Advantage – Systematic Investing in Credit"** (recorded Mar 2024; the page gives no publication date), Robert Lam and Paul Kamenski (Man Numeric). https://www.man.com/maninstitute/extra-credit-algorithmic-advantage
  - Companion to `Man_Quantitative_Credit_Alpha_Early_Mover_2022`.
  - Lam's argument: 1–2% of idiosyncratic alpha tilts a 6–7% IG cycle return.
- **Flirting with Models: "Jeff Rosenberg – The Past, Present, and Future of Systematic Fixed Income (S7E19)"** (2025-08-18), BlackRock. https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
  - Quant FI from its sell-side origins to BlackRock's buy-side "topology". Pair with `BlackRock_Systematic_High_Yield_Credit`.
- **Flirting with Models: "Greg Obenshain - Quantitative Credit (S4E12)"** (2021-07-19), Verdad. https://www.flirtingwithmodels.com/episodes/nQBct6plzWH
  - An ex-Apollo HY PM argues that credit excess returns come from improving versus declining credit, and that "even just acquiring data may be an edge".
- **Flirting with Models: "Ralph Smith - Scientific Investing in Fixed Income (S5E7)"** (2022-07-11), BlueCove. https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd
  - How breadth and liquidity limit credit strategies, and why assumptions about bond *availability* change backtests (Ch 7, 9).
- **Masters in Business: "Rick Rieder on Fixed Income Investments"** (2023-02-10). https://omny.fm/shows/masters-in-business/rick-rieder-on-fixed-income-investments
  - **Capital Allocators: "Dan Ivascyn – Fixed Income in the Limelight Again (EP.298)"** (2023-02-20). https://www.capitalallocators.com/podcast/fixed-income-in-the-limelight-again/
  - **Odd Lots: "Dan Ivascyn Is Excited About a New Era in Fixed Income"** (2025-12-08, the show's 10-year anniversary). https://omny.fm/shows/odd-lots/dan-ivascyn-is-excited-about-a-new-era-in-fixed-income
  - Discretionary multi-sector allocators: the contrast cases for Ch 12.
- **Credit Edge: "Dimensional Says High-Yield Public Debt Has the Edge Over Private"** (2025-05-29), Savina Rizova. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/dimensional-says-public-debt-has-the-edge-over-private
  - A factor house's prior: "There is no outperformance relative to high-yield public bonds."
- **Credit Edge: "TCW Chops Credit Risk to Lowest in 30 Years as CCCs 'Cry Uncle'"** (2026-10-15), Bryan Whalen. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tcw-chops-credit-risk-to-lowest-in-30-years-as-cccs-cry-uncle
  - CCC distress as the leading edge of contagion. Live material for Ch 11's CCC problem.
- **Credit Edge: "Fridson Sees High Yield Going Distressed in Recession"** (2025-05-01). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fridson-sees-high-yield-going-distressed-in-recession
  - A dated, falsifiable call ("back to 1,000 basis points on the high-yield index") for App C to score.

### 2.2 Trend, carry, hedging and tails (Ch 5, 10, 23)

- **Flirting with Models: "Roberto Croce - Trend and Carry Within Assets, Across Assets, and Over Time (S6E8)"** (2023-06-19). https://www.flirtingwithmodels.com/episodes/fN5gzryMqiE
  - The trend-plus-carry combination that Ch 10 ports to CDX.
- **Flirting with Models: "Moritz Heiden & Moritz Seibert – Trend-Following Spreads (S7E25)"** (2026-01-12). https://www.flirtingwithmodels.com/episodes/1iIqmQ7piJd
  - Trend applied to calendar and product spreads under deliberate capacity limits.
- **Flirting with Models: "Hari Krishnan - Market Tremors & Tail Hedging (S5E11)"** (2022-08-08). https://www.flirtingwithmodels.com/episodes/MeUsl8ow3Z3
  - Mean-field theory and "dominant agents" as a lens on tail risk (Ch 5, 23).
- **Credit Edge: "Goldman Tells Credit Investors to Buy Cheap Hedges"** (2025-02-13), Lotfi Karoui. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/goldman-tells-credit-investors-to-buy-cheap-hedges
  - Hedge cost versus the left tail.
- **Top Traders Unplugged: "SI422: Why Trend Following Rewards Patience ft. Katy Kaminski"** (2026-10-17). https://www.toptradersunplugged.com/podcast/why-trend-following-rewards-patience-ft-katy-kaminski/
  - **Top Traders Unplugged: "TTU153: Why Investors Keep Getting Trend Following Wrong ft. Patrick Welton"** (2026-09-30). https://www.toptradersunplugged.com/podcast/why-investors-keep-getting-trend-following-wrong-ft-patrick-welton/
  - The current CTA debate.

### 2.3 Market structure, pricing and ETFs (Ch 2, 18, 20, 22)

- **Odd Lots: "Episode 2: Under the Hood of the $8 Trln Corporate Bond Market"** (2015-11-16), Chris White (ex-Goldman, GSessions). https://omny.fm/shows/odd-lots/episode-2-under-the-hood-of-the-8-trln-corporate-b
  - The pre-revolution baseline: phone trading and a failed dealer platform. This opens Ch 2's timeline.
- **Odd Lots: "How The Bond Market Changed During A Veteran Trader's Decades On Wall Street"** (2017-07-31), Rob Elson. https://omny.fm/shows/odd-lots/how-the-bond-market-changed-during-a-veteran-trade
  - An oral history of the voice desk.
- **Odd Lots: "What We Can Learn About Market Liquidity By Looking At Everyday Life"** (2017-10-09), Karthik Shashidhar. https://omny.fm/shows/odd-lots/what-we-can-learn-about-market-liquidity-by-lookin
  - Why liquidity "evaporates". A Ch 18 opener.
- **Odd Lots: "A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True"** (2020-03-23), Chris White. https://omny.fm/shows/odd-lots/a-longstanding-fear-about-the-corporate-debt-marke
  - Recorded during March 2020: fragmented pricing and the BBB overhang. A mood check for the Ch 20 case.
- **Odd Lots: "How The Crisis Nearly Blew Up One Of The World's Safest Trades"** (2020-03-26), Josh Younger. https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s
  - The Treasury cash–futures basis failure, rates-side twin of the credit-ETF dislocation.
- **Odd Lots: "Why the True Price of a Bond Can Still Be Hard To Know"** (2021-04-05), Morningstar's Kowara and Jacobson. https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
  - Dispersion in evaluated prices is the input to NAV uncertainty in Ch 20 and to marks in Ch 17.
- **Odd Lots: "Here's Why It's So Hard to Fix the Corporate Bond Market"** (2021-11-18), Larry Harris. https://podscripts.co/podcasts/odd-lots/heres-why-its-so-hard-to-fix-the-corporate-bond-market (the feed links only to bloomberg.com/oddlots)
  - The author of *Trading and Exchanges*, ex-SEC chief economist, on why FIMSAC "hasn't had much success". Essential for Ch 22.
- **Odd Lots: "Darrell Duffie On How to Fix the World's Most Important Market"** (2023-08-28). https://omny.fm/shows/odd-lots/darrell-duffie-on-how-to-fix-the-world-s-most-impo
  - Duffie's Jackson Hole paper on Treasury market structure.
- **Odd Lots: "What We Learned About Treasuries on the Night of April 8"** (2025-04-28). https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8
  - The 2025 breakdown of the safe-haven trade, for hedge-ratio instability in Ch 8 and Ch 22.
- **Macro Musings: "Ellen Correia Golay on All-to-All Trading and Treasury Market Liquidity"** (2026-09-21). https://macromusings.libsyn.com/ellen-correia-golay-on
  - Covers the "dash for cash", all-to-all trading and principal trading firms: the Treasury analogue of Ch 2.
- **Odd Lots: "Episode 18: The Obscure Report That Spawned the ETF Industry"** (2016-03-07), Eric Balchunas. https://omny.fm/shows/odd-lots/episode-18-the-obscure-report-that-spawned-the-etf
  - The 1987 SEC-report origin of the AP machinery.
- **Trillions: "What the Actual ETF Is Going on Right Now"** (2020-03-19). https://omny.fm/shows/trillions/what-the-actual-etf-is-going-on-right-now
  - Recorded live on ETF liquidity and fixed income during the crash.
- **Masters in Business: "BlackRock's Global Co-Head of iShares Fixed Income ETFs Stephen Laipply"** (2025-06-20). https://omny.fm/shows/masters-in-business/blackrocks-global-co-head-of-ishares-fixed-income-etfs-stephen-laipply
  - The issuer's view of who drives bond-ETF flows.
- **Flirting with Models: "Thao Tran – Market Making Illiquid, Non-Fungible Assets (S7E14)"** (2025-02-03). https://www.flirtingwithmodels.com/episodes/eNEcTaLcPCU
  - Inventory risk when every unit is unique. The closest public analogue to quoting an off-the-run bond in Ch 18.
- **Flirting with Models: "Liquidity Cascades"** (2020-09-20). https://www.flirtingwithmodels.com/episodes/R80rhK4yck3
  - A reading of the Newfound paper "The Coordinated Risk of Uncoordinated Market Participants".
- **Odd Lots: "How the Speed of a Trade Got Down to Nearly the Speed of Light"** (2026-03-02), Donald MacKenzie. https://omny.fm/shows/odd-lots/how-the-speed-of-a-trade-got-nearly-down-to-the-speed-of-light
  - For Ch 27.

### 2.4 LMEs, restructuring and distressed (Ch 3, 13, 14, 16)

*Cloud 9fin* (share.transistor.fm):
- **"Not Your Daughter's Liens — Sid Levinson and team recall the original uptier LME"** (2026-03-10). https://share.transistor.fm/s/cf13a6ad
  - The 2017 NYDJ deal as the first uptier, told by majority-lender counsel.
  - It is compared with Serta, J.Crew, Envision, Robertshaw, Trimark, Boardriders, PetSmart/Chewy, Caesars and Xerox, which makes it a ready-made Ch 13 genealogy.
- **"Introducing Jane's LME addiction: The bookends of the Serta era"** (2025-01-08). https://share.transistor.fm/s/faa4e74d
  - The Fifth Circuit's Serta decision.
- **"Eat, sleep, drive — Breaking down the Del Monte, Serta & American Tire trifecta"** (2026-07-21). https://share.transistor.fm/s/1c4df313
  - Judge Lopez's Serta ruling set against Judges Kaplan's and Goldblatt's approaches, on pro rata sharing, sacred rights and LME damages. The 2026 regime-shift inputs for Ch 14.
- **"LME Doomscrolling — Data-driven reality check"** (2026-04-07), Mark Roe and Vasile Rotaru. https://share.transistor.fm/s/1f62123b
  - Their study "Liability Management's Limited Runway: Corporate Restructuring Today" tracks how non-pro-rata coercive LMEs fare. Re-default priors for Ch 14.
- **Co-ops, DQ lists and voting caps:**
  - "Co-op agreements through the eye of American Needle" (2024-09-25): the Sherman Act theory. https://share.transistor.fm/s/44a5c9af
  - "Jane's LME Addiction — Co-Optimum — Navigating the Altice USA antitrust litigation" (2026-01-13). https://share.transistor.fm/s/40588778
  - "Jane's LME Addiction — DQ lists are overrated" (2025-07-17, with Jason Mudrick). https://share.transistor.fm/s/cce68471
  - "Jane's LME Addiction — Are lender voting and concentration caps the new and improved DQ lists?" (2025-11-13): new "anti-co-op" language for Ch 25 to parse. https://share.transistor.fm/s/ea154cb9
  - "Jane's LME Addiction — BofA drops in on a double Black Diamond navigating uncharted DQ litigation slopes" (2026-08-10). https://share.transistor.fm/s/3af5e46f
  - "Jane's LME Addiction — The minority report with Shai Schmidt" (2025-09-15): when minority holders should organize, negotiate or litigate. https://share.transistor.fm/s/a41d627c
- **"Securitize for a J.Crew reprise"** (2023-07-06). https://share.transistor.fm/s/5101c481
  - Loose securitization baskets as the next trapdoor: a concrete clause for Ch 25 to flag.
- **"LME Doomscrolling — Just because you can, doesn't mean you should"** (2026-08-31), Bill Derrough (Jefferies). https://share.transistor.fm/s/6a6999bb
  - A banker known for high creditor participation, close to the reader's own seat.
- **"The In-Court Report with Cat Corey — The latest on backstop fees in rights offerings and DIP financings"** (2025-12-09), Vince Buccola. https://share.transistor.fm/s/ad684efa
  - Backstop economics after ConvergeOne. Core Ch 16 material.
- **"It Hertz you to see it"** (2024-06-26). https://share.transistor.fm/s/d607390a
  - Hertz in 2024, the sequel to the book's Hertz 2020 case.

*Bloomberg and others:*
- **Odd Lots: "Inside the Blood Sport of Creditor-on-Creditor Violence"** (2024-11-25), Sujeet Indap (FT). https://omny.fm/shows/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-vio
  - The best general-audience account of how cov-lite paper led to LMEs.
- **Capital Allocators: "Max Frumes and Sujeet Indap – Inside the Sausage Factory of the Caesar's Restructuring (EP.209)"** (2021-08-16). https://www.capitalallocators.com/podcast/inside-the-sausage-factory-of-the-caesars-restructuring/
  - Pre-LME-era context for Ch 3.
- **Credit Edge: "Divisive Debt Maneuvers; Bank Stress Returns"** (2023-04-27). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/divisive-debt-maneuvers-bank-stress-returns
  - The 2023 wave of drop-down suits.
- **Credit Edge: "Distressed Creditors Play Nice; Telecoms in Focus"** (2023-07-27). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/distressed-creditors-play-nice-telecoms-in-focus
  - Carvana 2023 as a "rare case" of cooperation that eliminated $1.2B of debt.
- **Credit Edge: "Altice 'Jenga Tower' Menaces Global Credit Markets"** (2024-04-25). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/altice-jenga-tower-menaces-global-credit-markets
  - **Credit Edge: "Fidelity Fears Creditor Violence Spread; Altice Focus"** (2024-02-15). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fidelity-fears-creditor-violence-spread-altice-foc
  - US-style LMEs reaching Europe.
- **Credit Edge: "Junk Companies Are in Debt Covenant 'La La Land,' Says Fox Legal"** (2025-07-31). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/junk-companies-are-in-debt-covenant-la-la-land-says-fox-legal
  - Add-backs that are "departures from reality": Ch 13's EBITDA-cap thesis.
- **Credit Edge: "Kirkland & Ellis Sees More Distressed Lenders Flipping Company Boards"** (2026-10-01), H.T. Flanagan. https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/kirkland-ellis-sees-more-distressed-lenders-flipping-company-boards
  - Board-replacement remedies used "with greater frequency".
- **Credit Edge: "Lumen's CFO Looks Ahead After 'Moonshot' Debt Deal That Worked"** (2026-09-17). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/lumen-s-cfo-looks-ahead-after-moonshot-debt-deal-that-worked
  - The issuer's side of a giant out-of-court restructuring ("keep as many winners as possible").
- **Credit Edge: "Judge's Downfall Shocks Bankruptcy World; Oil M&A"** (2023-10-19). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/judge-s-downfall-shocks-bankruptcy-world-oil-m-a
  - Venue risk, for Ch 16.
- **Credit Edge distressed-cycle panel.** Score these calls in App C:
  - "Mudrick Sees Seven-Year Default Wave as Rates Stay Up" (2025-08-14). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/mudrick-sees-seven-year-default-wave-as-rates-stay-up
  - "Distressed Buyer H.I.G. Sees Most Loan Distress in Years (Podcast)" (2026-02-05). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/distressed-buyer-h-i-g-sees-most-loan-distress-in-years-podcast
  - "Bain Sees Software Debt Defaults Spiking" (2026-02-26). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bain-sees-software-debt-defaults-spiking
  - "Davidson Kempner Sees a $770 Billion Stressed Debt Opportunity" (2026-04-16; "year three of what's already the longest default cycle in 20 years"). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/davidson-kempner-sees-a-770-billion-stressed-debt-opportunity
  - "Magnetar Scours $600 Billion Stressed Debt Pile for Bond, Loan Value" (2026-09-24). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/magnetar-scours-600-billion-stressed-debt-pile-for-bond-loan-value
  - "Sculptor Sees Opportunity in Busted Capital Structures" (2024-09-05). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/sculptor-sees-opportunity-in-busted-capital-struct
- **Founder interviews.** How distressed shops are actually organized, for Ch 3 and Ch 28 team design:
  - Masters in Business: "King Street's Brian Higgins On Navigating Distressed Markets" (2024-10-18). https://omny.fm/shows/masters-in-business/king-streets-brian-higgins-on-navigating-distresse
  - Masters in Business: "Dominique Mielle on Luck and Resilience in Finance" (2023-03-24). https://omny.fm/shows/masters-in-business/dominique-mielle-on-luck-and-resilience-in-finance
  - Capital Allocators: "Josh Friedman – Master Class in Credit Investing at Canyon (EP.263)" (2022-07-25). https://www.capitalallocators.com/podcast/master-class-in-credit-investing-at-canyon/
  - Capital Allocators: "Tony Yoseloff – Forty Years of Davidson Kempner (EP.313)" (2023-05-08). https://www.capitalallocators.com/podcast/forty-years-of-davidson-kempner/
  - Capital Allocators: "Jeff Aronson – Building Centerbridge Across the Capital Structure (EP.468)" (2025-11-03). https://www.capitalallocators.com/podcast/building-centerbridge-across-the-capital-structure/
- **The Octus Download: "EP 22 | Judge Michael B. Kaplan, Vegas Squeeze & the First Brands Conspiracy"** (2025-12-23). https://share.transistor.fm/s/aaf0387e
  - **The Octus Download: "EP 21 | How Bankruptcy Really Works: Inside the System with Josh Sussberg"** (2025-12-10). https://share.transistor.fm/s/81750469
  - A sitting bankruptcy judge, and Kirkland's restructuring head.
- **Octus Radio: "Conversations With Reorg: Akin Gump Discusses Liability Management Exercises"** (2023-03-21). https://share.transistor.fm/s/155fa539

### 2.5 Private credit and convergence (Ch 17; also 12, 14)

- **Odd Lots arc.** Each episode is a dated waypoint on Ch 17's spine:
  - "Why Private Credit's Been Booming Even as Interest Rates Go Up" (2023-11-20; Laura Holson, New Mountain). https://omny.fm/shows/odd-lots/why-private-credits-been-booming-even-as-interest
  - "The Black Hole of Private Credit That's Swallowing the Economy" (2024-09-02; Ellias and de Fontenay, "The Credit Markets Go Dark"). https://omny.fm/shows/odd-lots/the-black-hole-of-private-credit-thats-swallowing
  - "Apollo Explains How Big Tech Is Disrupting Credit Markets" (2024-10-14; Rob Bittencourt). https://omny.fm/shows/odd-lots/101024-odd-lots-rob-bittencourt-v1
  - "How Banks and Private Credit Became the Best of Frenemies" (2024-10-24; Huw van Steenis). https://omny.fm/shows/odd-lots/102424-odd-lots-huw-van-steenis-master-3
  - "How Oaktree's Head of Sourcing Finds the Next Great Deal" (2024-11-28). https://omny.fm/shows/odd-lots/how-oaktrees-head-of-sourcing-finds-the-next-great
  - "Blackstone's Michael Zawadzki on How Private Credit Got so Big" (2026-01-23). https://omny.fm/shows/odd-lots/blackstones-michael-zawadzki-on-how-private-credit-got-so-big
  - "What's Actually Going On With Private Credit" (2026-04-27; Osterweis). https://omny.fm/shows/odd-lots/whats-actually-going-on-with-private-credit
  - "Why Private Credit Got Entangled With Insurance" (2026-07-31; Granato and Drall, "Private Credit's State Backstop: How Private Equity Socializes Risk Through Insurers"). https://omny.fm/shows/odd-lots/why-private-credit-got-entangled-with-insurance
- **Money Stuff: The Podcast:**
  - "Funny Business Is My Business: PRIV, HHH, WARS" (2025-02-28; the PRIV ETF launch). https://omny.fm/shows/money-stuff-the-podcast/funny-business-is-my-business-priv-hhh-wars
  - "Bat Tat: Labubu, OBDC, Frank" (2025-11-21; OBDC/OBDC II, private-credit marks). https://omny.fm/shows/money-stuff-the-podcast/bat-tat-labubu-obdc-frank
  - "Man Not Bird" (2026-03-13; marking private credit to market, NAV arbitrage). https://omny.fm/shows/money-stuff-the-podcast/man-not-bird
  - "Boaz Weinstein" (2026-03-19). https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
    - Saba's tenders for OBDC II and SREIT, public-versus-private BDC discounts, "volatility laundering". The practitioner statement of what a public-markets desk can arbitrage.
  - "Frisky Dentists" (2026-05-15; trading private credit, daily pricing, CLOs). https://omny.fm/shows/money-stuff-the-podcast/frisky-dentists
- **Credit Edge:**
  - "PGIM Sees 'Chilling Effect' on Private Credit From BDC Storm" (2026-04-02). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/pgim-sees-chilling-effect-on-private-credit-from-bdc-storm
  - "BDC Veteran Expects Private Credit Fund Stress as Banks Pull Back" (2026-03-19). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bdc-veteran-expects-private-credit-fund-stress-as-banks-pull-back
  - "HarbourVest Expects Private Credit Secondaries Volume to Double" (2026-05-07; "run-rating above $50 billion"). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/harbourvest-expects-private-credit-secondaries-volume-to-double
  - "Investors Keeping Score on 'Bad PIK', Benefit Street Partners' Kumar Says" (2026-08-06). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/investors-keeping-score-on-bad-pik-and-stale-marks-benefit-street-partners-kumar-says
  - "Janus Is Skeptical of Private Credit's Push Into ETFs" (2025-04-03). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/janus-is-skeptical-of-private-credit-s-push-into-etfs
- **Trillions: "The Apollo ETF Landing"** (2024-09-26). https://omny.fm/shows/trillions/the-apollo-etf-landing
  - The PRIV filing and Apollo's "liquidity backstop".
- **Capital Allocators:**
  - "Howard Marks – Navigating Private Credit (EP.439)" (2025-04-07). https://www.capitalallocators.com/podcast/navigating-private-credit/
  - "Kieran Goodwin – Private Credit Concerns (EP.494)" (2026-03-30; Saba). https://www.capitalallocators.com/podcast/private-credit-concerns/
  - "Kipp deVeer – The World of Private Credit at Ares (EP.329)" (2023-07-24). https://www.capitalallocators.com/podcast/the-world-of-private-credit-at-ares/
  - "Scott Kleinman – Apollo's Integrated Alternatives Platform (EP.481)" (2026-01-19). https://www.capitalallocators.com/podcast/apollos-integrated-alternatives-platform/
- **Masters in Business:**
  - "The Future of Private Credit with Erik Hirsch" (2025-07-31). https://omny.fm/shows/masters-in-business/the-future-of-private-credit-with-erik-hirsch
  - "Building a Global Private Credit Firm and 'Trading' Planes with Victor Khosla" (2024-09-19). https://omny.fm/shows/masters-in-business/building-a-global-private-credit-firm-and-trading
- **Macro Musings: "Richard Berner on Growth of the Private Credit and the Role of Fiscal Dominance on Treasury Markets"** (2026-01-19, ex-OFR director). https://macromusings.libsyn.com/richard-berner-on-growth-of-the-private-credit-and-the-role-of-fiscal-dominance-on-treasury-markets
- **Cloud 9fin:**
  - "Getting real about synthetic PIKs" (2024-09-18). https://share.transistor.fm/s/86021e09
  - "Decoding the software lending shock in private credit with MSCI" (2026-04-03). https://share.transistor.fm/s/3914343b

### 2.6 Loans and CLOs (Ch 21)

- **Capital Allocators: "Thomas Majewski – Empty Rooms: Masterclass on CLOs at Eagle Point Credit Management (EP. 284)"** (2022-12-01). https://www.capitalallocators.com/podcast/empty-rooms-masterclass-on-clos-at-eagle-point-credit-management/
  - **Credit Edge: "Bull Run in Loans Slams CLO Equity Buyers, Says Eagle Point's Majewski"** (2026-07-16). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bull-run-in-loans-slams-clo-equity-buyers-says-eagle-point-s-majewski
  - Same manager in 2022 and 2026: CLO equity versus repricing waves.
- **Capital Allocators: "Shiloh Bates – CLO Investing at Flat Rock Global (EP.379)"** (2024-04-11). https://www.capitalallocators.com/podcast/clo-investing-at-flat-rock-global/
  - The author of *CLO Investing* (2023).
- **Capital Allocators: "Greg Lippmann – The Big Short and Structured Credit at LibreMax (EP.270)"** (2022-09-12). https://www.capitalallocators.com/podcast/the-big-short-and-structured-credit-at-libremax/
- **Credit Edge CLO cluster:**
  - "Hedge Funds Are Diving Into CLOs; AT1s Revitalize" (2023-09-07). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/hedge-funds-are-diving-into-clos-at1s-revitalize
  - "Altice Stress Weighs on CLO Market, Sound Point Says" (2024-03-28). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/altice-stress-weighs-on-clo-market-sound-point-say
  - "PGIM Lauds 'Bulletproof' CLOs as Credit Risks Rise" (2025-06-12). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/pgim-lauds-bulletproof-clos-as-credit-risks-rise
  - "Tetragon Sees Midteens Gain in Riskiest CLO Tranche" (2025-08-21). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tetragon-sees-midteens-gain-in-riskiest-clo-tranche
  - "CLOs Are Tough to Blow Up, Crescent Says" (2025-10-02). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/clos-are-tough-to-blow-up-crescent-says
  - "Loan Defaults Outpace Bonds; Country Garden Woes" (2023-08-17). https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/loan-defaults-outpace-bonds-country-garden-woes
- **Cloud 9fin: "Bringing loan data from fax to the future"** (2025-03-06), FIS. https://share.transistor.fm/s/14a1ade2
  - Loan data still moves partly by fax: the plumbing behind Ch 21's settlement-lag math.
- **Odd Lots: "The Hottest Way for Banks to Get Risk Off Their Balance Sheets"** (2024-08-22). https://omny.fm/shows/odd-lots/the-hottest-way-for-banks-to-get-risk-off-their-ba
  - Synthetic risk transfers and bank capital (Ch 21, 22).

### 2.7 CDS, basis and cap-structure arbitrage (Ch 23, 24)

- **Cloud 9fin: "Distressed Diaries — Ardagh CDS and the empty glass paradox"** (2026-01-21). https://share.transistor.fm/s/903a348d
  - Arini argued that bonds already marked for equitization had zero outstanding principal ("Schrödinger's Obligations"). Per the feed text, the EMEA Determinations Committee rejected the challenge in a split vote, with Citi and Pimco dissenting. A 2026 case module for Ch 24.
- **Masters in Business: "Boaz Weinstein on Credit Investments"** (2022-05-13). https://omny.fm/shows/masters-in-business/boaz-weinstein-on-credit-investments
  - **Masters in Business: "Boaz Weinstein on Investors' Unknown Risk"** (2022-11-24). https://omny.fm/shows/masters-in-business/boaz-weinstein-on-investors-unknown-risk
  - From Deutsche Bank credit-trading co-head to Saba.
- **Capital Allocators: "Nancy Zimmerman – People, Process, and Fixed Income Arbitrage at Bracebridge (EP.517)"** (2026-09-28). https://www.capitalallocators.com/podcast/people-process-and-fixed-income-arbitrage-at-bracebridge/

### 2.8 NLP, AI and systems (Ch 7, 25, 26, 27)

- **Odd Lots: "AI Can Tell Us Something About Credit Market Weakness"** (2025-12-04), Noetica's Dan Wertman. https://omny.fm/shows/odd-lots/ai-can-tell-us-something-about-credit-market-weakness
  - AI-measured drift in deal-document language: the commercial twin of Ch 25.
- **Cloud 9fin: "Claude Code shook credit. What breaks next?"** (2026-07-02). https://share.transistor.fm/s/7a979a47
  - An AI coding agent as a *credit* shock: the software sell-off, and Medallia handing the keys to lenders.
- **Odd Lots: "How Hudson River Trading Actually Uses AI"** (2025-10-31). https://omny.fm/shows/odd-lots/how-hudson-river-trading-actually-uses-ai
  - **Odd Lots: "Inside Hudson River Trading's Blistering Token Burn"** (2026-06-05). https://omny.fm/shows/odd-lots/inside-hudson-river-tradings-blistering-token-burn
  - **Odd Lots: "One of the World's Largest Hedge Funds on Its 86x Growth in Token Spending"** (2026-07-09, Man Group CTO Gary Collier and Head of Data & AI Tushara Fernando). https://omny.fm/shows/odd-lots/one-of-the-worlds-largest-hedge-funds-on-its-86x-growth-in-token-spending
  - How firms budget and govern LLM use: anchors for Ch 26.
- **Flirting with Models: "Ben Wellington – Complex Feature Engineering at Two Sigma (S7E32)"** (2026-07-06). https://www.flirtingwithmodels.com/episodes/mDCRKBfrVHQ
  - **Flirting with Models: "Stacie Mintz – Turning Qualitative Fundamentals into Quantitative Factors (S7E33)"** (2026-08-03). https://www.flirtingwithmodels.com/episodes/K0x0u3fbJvh
- **Odd Lots: "Inigo Fraser-Jenkins and Aaron Brown Debate The Future Of Quant Investing"** (2020-11-23). https://omny.fm/shows/odd-lots/inigo-fraser-jenkins-and-aaron-brown-debate-the-fu
  - **Odd Lots: "What It Takes To Win At Quant Investing"** (2020-10-08, Ciamac Moallemi). https://omny.fm/shows/odd-lots/what-it-takes-to-win-at-quant-investing
- **Masters in Business: "David Snyderman on Specialty Finance and Data in Investing"** (2024-03-01, Magnetar). https://omny.fm/shows/masters-in-business/david-snyderman-on-specialty-finance-and-data-in-i

### 2.9 PM playbook and multi-strats (Ch 28)

- **Odd Lots: "How to Succeed at Multi-Strategy Hedge Funds"** (2024-05-20). https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds
  - **Odd Lots: "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds"** (2025-06-21, recorded live 2025-06-12). https://omny.fm/shows/odd-lots/giuseppe-paleologo-on-quant-investing-at-multi-strat-hedge-funds
  - Audio companions to `Paleologo_Advanced_Portfolio_Management`.
- **Risk, crowding and capital allocation inside pods:**
  - Odd Lots: "How the Rise of 'Pod Shops' Is Reshaping the Way Markets Trade" (2024-02-26). https://omny.fm/shows/odd-lots/022624-odd-lots-krishna-kumar-master-1
  - Odd Lots: "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (2024-07-25). https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really
  - Odd Lots: "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (2024-10-07, Dan Morillo). https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master
- **Founders on running a credit or multi-strategy platform.** "Credit microcycles" is the discretionary counterpart to Ch 10's regime models:
  - Capital Allocators: "Dmitry Balyasny – Multi-Strategy Platform at BAM (EP.341)" (2023-10-02). https://www.capitalallocators.com/podcast/multi-strategy-platform-at-bam/
  - Capital Allocators: "Jonathan Lewinsohn – Credit Microcycles at Diameter (EP.484)" (2026-02-02). https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/
  - Capital Allocators: "Luke Ellis – The Man Behind The Man Group (EP.214)" (2021-09-20). https://www.capitalallocators.com/podcast/the-man-behind-the-man-group/
- **Odd Lots: "What David Barse Learned From Watching A Credit Fund Blow Up"** (2018-10-01). https://omny.fm/shows/odd-lots/what-david-barse-learned-from-watching-a-credit-fu
  - Third Avenue's late-2015 meltdown: the canonical liquidity-mismatch case.

### 2.10 Credit-cycle color (Ch 1, 14)

- **Odd Lots: "Oaktree's Wayne Dahl on Credit Markets Right Now"** (2023-09-18). https://omny.fm/shows/odd-lots/oaktrees-wayne-dahl-on-credit-markets-right-now
  - **Odd Lots: "The Next Stage of the Credit Cycle with Oaktree's Poli"** (2024-09-19). https://omny.fm/shows/odd-lots/the-next-stage-of-the-credit-cycle-with-oaktree-s
- **Odd Lots: "The Anonymous Meme Account Chronicling Credit Market Craziness"** (2024-01-25, High Yield Harry). https://omny.fm/shows/odd-lots/the-anonymous-meme-account-chronicling-credit-mark
  - The house voice in human form.
- **Masters in Business: "Oaktree Howard Marks: Masters in Business (Audio)"** (2015-07-19, on high yield). https://omny.fm/shows/masters-in-business/oaktree-howard-marks-masters-in-business-audio
  - **Capital Allocators: "David Breazzano - High Yields and Low Risk at Polen Capital (EP.405)"** (2024-09-12). https://www.capitalallocators.com/podcast/high-yields-and-low-risk-at-polen-capital/
  - High-yield history from people in it since the early 1980s.
- **Money Stuff: "No Nap Rooms: Credit, Peace, 24X"** (2025-10-17). https://omny.fm/shows/money-stuff-the-podcast/no-nap-rooms-credit-peace-24x
  - "Late-cycle credit accidents" and banks versus private credit.

---

## 3. Show directory

| Show | Verified root | Why subscribe |
|---|---|---|
| Odd Lots | https://omny.fm/shows/odd-lots | Broadest finance show. Credit episodes recur several times a year, with private credit as a running arc. |
| The Credit Edge (Bloomberg Intelligence) | https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence | Weekly since Feb 2023, one named buy-side CIO per episode. Usable as a sentiment panel (§7). |
| Money Stuff: The Podcast | https://omny.fm/shows/money-stuff-the-podcast | Audio companion to Matt Levine's column, and the house style's spiritual parent. |
| Masters in Business | https://omny.fm/shows/masters-in-business | Long-form interviews with credit founders. |
| Capital Allocators | https://www.capitalallocators.com/ | Deepest EP-numbered credit back catalog. |
| Flirting with Models | https://www.flirtingwithmodels.com/ | Quant process. Mostly adjacent to credit. |
| Cloud 9fin | https://9fin.com/podcasts | Best LME-legal audio. Runs monthly series. |
| Octus Radio / The Octus Download | feeds.transistor.fm/octus-radio, /the-octus-download | Restructuring news at the level of the docket. octus.com returned 403 to my fetch. |
| Macro Musings | episode pages on macromusings.libsyn.com | Treasury market structure and the Fed. |
| Top Traders Unplugged | https://www.toptradersunplugged.com/ | Trend-following practitioners. |
| ISDA podcast | https://www.isda.org/2026/10/01/episode-60-modelling-margin/ | Derivatives plumbing. Ep. 60 covers margin modeling. |

---

## 4. Newsletters, blogs and portals (live on 2026-10-17)

- **Howard Marks memos:** https://www.oaktreecapital.com/insights/memos
  - Credit-relevant titles on the page: "What's Going on in Private Credit?" (Apr 9, 2026), "Cockroaches in the Coal Mine" (Nov 6, 2025), "Gimme Credit" (Mar 6, 2025), "The Impact of Debt" (May 8, 2024).
- **PETITION:** https://www.petition11.com/
  - "Curated financial news, analysis and commentary with an emphasis on distressed investing, restructuring and bankruptcy." The irreverent restructuring voice closest to ours.
- **Net Interest:** https://www.netinterest.co/
  - Bank economics, for dealer capital in Ch 22.
- **The Diff:** https://www.thediff.co/
  - "Inflections in Finance and Tech."
- **Credit Slips:** https://creditslips.org/
  - Bankruptcy academics' blog. Fast reads on LME and venue rulings.
- **Liberty Street Economics:** https://libertystreeteconomics.newyorkfed.org/
- **FEDS Notes:** https://www.federalreserve.gov/econres/notes/feds-notes/default.htm
  - Together with Liberty Street, the primary stream behind the Ch 17 and Ch 22 trend numbers.
- **Verdad archive:** https://verdadcap.com/archive
  - Includes "The Reflexivity of Credit Markets" (Apr 20, 2026) and "Echoes of Junk Bonds Past" (Apr 6, 2026), companions to the Obenshain episode.
- **Quant research portals:**
  - Man insights: https://www.man.com/insights
  - AQR: https://www.aqr.com/Insights/Research
  - Robeco: https://www.robeco.com/en-int/insights
- **Vendor research (mostly paywalled):**
  - 9fin insights: https://9fin.com/insights
  - CreditSights: https://www.creditsights.com/
  - KBRA: https://www.kbra.com/
- **Not verifiable this session:**
  - Blocked (403): Money Stuff newsletter page, FT Alphaville, Alpha Architect, Tradeweb insights, Harvard Bankruptcy Roundtable, octus.com.
  - Quantpedia returned 466.
  - These paths returned 404: MarketAxess /research, FINRA's TRACE "about" path, Apollo "Daily Spark", BlackRock *The Bid*.
  - Cite all of these by name only.

## 5. Talks, seminars and courses

- **The Microstructure Exchange:** https://microstructure.exchange/
  - A virtual academic forum of one-hour Zoom talks with an archive.
  - Listed: Farshid Abdi (with Marco Rossi and Botao Wu), "Overnight Corporate Bond Trading" (Sept 15, 2026). It studies trades executed between 6:30 p.m. and 8:00 a.m. that TRACE does not disseminate until the next morning. This is a new latency fact for Ch 18 and 22.
- **MIT OpenCourseWare 18.S096, "Topics in Mathematics with Applications in Finance" (Fall 2013):** https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/
  - A free math-for-finance lecture course, as a prerequisite for Part II. Only the course title was verified, not its syllabus.
- **Live-recorded episodes:** Paleologo (Bloomberg Equity Intelligence Summit, 2025-06-12) and Wayne Dahl (Future Proof, 2023).

## 6. Books (existence verified through the publisher feed text of the episode cited; no links)

- Max Frumes and Sujeet Indap, *The Caesars Palace Coup: How a Billionaire Brawl Over the Famous Casino Exposed the Corruption of the Private Equity Industry*. Out by Aug 2021 (CA EP.209); subtitle as given in Odd Lots, 2024-11-25.
- Dominique Mielle, *Damsel in Distressed: My Life in the Golden Age of Hedge Funds* (2021, per MIB 2023-03-24).
- Shiloh Bates, *CLO Investing* (2023, per CA EP.379).
- William D. Cohan, *Money to Burn: The Unvarnished Truth About Leon Black, Apollo, and the Rise of a New Wall Street* (2026, per Cloud 9fin 2026-09-08).
- Robin Wigglesworth, *A Fabulous Debt: the Epic Story of How Bonds Built the Modern World* (per TTU IL53, 2026-09-16). Includes the Milken junk-bond story.
- Donald MacKenzie, *Trading at the Speed of Light* (2021, per Odd Lots 2026-03-02).
- Karthik Shashidhar, *Between the Buyer and the Seller* (per Odd Lots 2017-10-09).
- Antti Ilmanen, *Investing Amid Low Expected Returns* (per ReSolve Riffs 2022-04-13).
- Eric Balchunas, *The Bogle Effect* (per ReSolve Riffs 2022-03-23).

## 7. Papers named in verified episode text (title-only leads)

| Title | Authors | Named in | Use |
|---|---|---|---|
| "Liability Management's Limited Runway: Corporate Restructuring Today" | Roe, Rotaru | Cloud 9fin 2026-04-07 | Ch 14 re-default priors (**CHECK** SSRN id) |
| "Private Credit's State Backstop: How Private Equity Socializes Risk Through Insurers" | Granato, Drall | Odd Lots 2026-07-31 | Ch 17 insurance channel |
| "The Credit Markets Go Dark" | Ellias, de Fontenay | Odd Lots 2024-09-02 | Ch 17 governance |
| "Bond Pricing: Agreeing To Disagree" | Kowara, Jacobson | Odd Lots 2021-04-05 | Ch 20 NAV uncertainty |
| "Liquidity Cascades: The Coordinated Risk of Uncoordinated Market Participants" | Newfound | FWM 2020-09-20 | Ch 18, 28 |
| "Overnight Corporate Bond Trading" | Abdi, Rossi, Wu | Microstructure Exchange 2026-09-15 | Ch 18, 22 |

**CHECK:** A WebSearch hit this session (https://alternativecreditinvestor.com/2026/07/01/creditor-on-creditor-violence-heats-up-as-lenders-weaponise-co-ops/) attributes to an Oxford study the finding that more than 80% of 89 LMEs defaulted within 36 months. Verify the primary source before Ch 14 uses it.

**Feeds as data (Ch 25–26, App B).** The feeds are free, timestamped and machine-readable. *Credit Edge* alone is about 195 weekly items naming firm, speaker and stance. That is a small panel of buy-side narrative to code and test against HY OAS or BDC price/NAV. The Odd Lots RSS also lists per-episode Omny transcript endpoints (`api.omny.fm/.../transcript?format=TextWithTimestamps`), which supports an NLP pipeline. Building it is future work.

## 8. Shelf pairings

> [SOURCE EXTRACTION] "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes." — `Man_Revolutions_in_Credit_Trading_2023 p.2`

The "before" is the Chris White (2015) and Larry Harris (2021) episodes. The "after" is Dwinells and Richardson in 2026, who argue about where to *extend* systematic credit, not whether it can execute.

> [SOURCE EXTRACTION] "It was always thought that credit would follow swiftly on the tails of the equity market in developing a substantial quant investment universe." — `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.5`

The "very low single digits" (2024) and "about 1%–2%" (2026) remarks say it still has not. Ch 4 should model penetration as the slow variable and AUM as the fast one.

> [SOURCE EXTRACTION] "An investor that holds the fulcrum security which likely will receive a significant portion of the reorganized firm's equity may oppose the sale because it could diminish long-term enterprise value." — `Moyer_Distressed_Debt_Analysis p.339`

The board-flip, co-op and DQ-list episodes show fulcrum holders acting *before* any 363 sale. Ch 13 and Ch 16 should extend Moyer's in-court game to that out-of-court stage.

## 9. Gaps and CHECK list

- No verified episode is primarily about credit portfolio trading or credit-ETF creation/redemption. Next session: try S&P Global and Risk.net podcasts.
- Petition's author and the Harvard Bankruptcy Roundtable were unverified.
- Top Traders Unplugged feed links point to `localhost`. Only the two TTU URLs above were fetched directly.
- Macro Musings, Menand and Younger on "Money and the Public Debt: Treasury Market Liquidity as a Legal Phenomenon" (2023-10-02) is in the feed, but its link is truncated and soft-404s. Cite it title-only.

---

## Sources (URLs verified this session, 2026-10-17)

**Publisher feeds and APIs (fetched and parsed):**
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/podcast.rss (Odd Lots)
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/e74a35e9-c028-4e5f-a3f7-afb10164a717/8792a2e9-d66c-4038-a1fe-afb101654894/podcast.rss (Credit Edge)
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/ee4336cb-155f-4488-90e0-b1400134e40e/77e6a3a7-290d-4a82-8164-b14001353ef2/podcast.rss (Money Stuff)
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/4e4cd910-40a1-4619-a5f3-ae2b0012ffff/5873a3cb-298f-40bc-b71f-ae2b0013000d/podcast.rss (Masters in Business)
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/ee08231b-2e0c-40d0-afa9-ae3c0021f0dc/ab3c08b0-6606-450f-a60c-ae3c0021f0e6/podcast.rss (Trillions)
- https://api.omny.fm/orgs/e73c998e-6e60-432f-8610-ae210140c5b1/programs
- https://rss.libsyn.com/shows/94820/destinations/482814.xml (Capital Allocators)
- https://rss.libsyn.com/shows/138806/destinations/865793.xml (Macro Musings)
- https://feeds.transistor.fm/cloud-9fin
- https://feeds.transistor.fm/octus-radio
- https://feeds.transistor.fm/the-octus-download
- https://feeds.captivate.fm/flirting-with-models/
- https://feeds.captivate.fm/top-traders-unplugged/
- https://feeds.captivate.fm/resolve-gestalt-university/
- https://app.podcastai.com/api/v1/portal/shows/flirting-with-models/episodes
- https://www.capitalallocators.com/podcast-sitemap.xml
- https://itunes.apple.com/lookup?id=1056200096
- https://itunes.apple.com/lookup?id=1402620531&entity=podcastEpisode&limit=200
- https://podscripts.co/podcasts/odd-lots

**Show and directory pages:**
- https://omny.fm/shows/odd-lots
- https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence
- https://omny.fm/shows/money-stuff-the-podcast
- https://omny.fm/shows/masters-in-business
- https://www.capitalallocators.com/
- https://www.flirtingwithmodels.com/
- https://www.flirtingwithmodels.com/episodes
- https://9fin.com/podcasts
- https://www.toptradersunplugged.com/
- https://podcasts.apple.com/us/podcast/odd-lots/id1056200096
- https://podcasts.apple.com/us/podcast/money-stuff-the-podcast/id1739582836

**Episode pages:** every episode URL in §2–3 (about 140) returned HTTP 200 on 2026-10-17. Hosts: omny.fm, capitalallocators.com, flirtingwithmodels.com, share.transistor.fm, macromusings.libsyn.com, podscripts.co, toptradersunplugged.com, man.com, isda.org. Soft-404 hosts were title-checked.

**Newsletter, research and course pages:**
- https://www.man.com/maninstitute/extra-credit-algorithmic-advantage
- https://www.oaktreecapital.com/insights/memos
- https://www.petition11.com/
- https://www.netinterest.co/
- https://www.thediff.co/
- https://creditslips.org/
- https://libertystreeteconomics.newyorkfed.org/
- https://www.federalreserve.gov/econres/notes/feds-notes/default.htm
- https://verdadcap.com/archive
- https://www.man.com/insights
- https://www.aqr.com/Insights/Research
- https://www.robeco.com/en-int/insights
- https://9fin.com/insights
- https://www.creditsights.com/
- https://www.kbra.com/
- https://microstructure.exchange/
- https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/
- https://www.isda.org/2026/10/01/episode-60-modelling-margin/

**WebSearch results (existence only):**
- https://alternativecreditinvestor.com/2026/07/01/creditor-on-creditor-violence-heats-up-as-lenders-weaponise-co-ops/
- https://podscripts.co/podcasts/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-violence
- https://octus.com/resources/articles/rx-101-creditor-on-creditor-violence

**Shelf:** `Man_Revolutions_in_Credit_Trading_2023 p.2`, `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.5`, `Moyer_Distressed_Debt_Analysis p.339`.

---

## Book placement

**All chapters:** replace the TITLE-ONLY podcast lines in each `### Deep-Dive Resource Graph` with the dated, linked items from §2 for that chapter. All links were verified on 2026-10-17.

**By chapter:**
- **Ch 2:**
  - Build an oral-history timeline box from White (2015), Elson (2017), White (2020), Morningstar (2021), Harris (2021) and Golay (2026).
  - Add the Man 2023 p.2 pairing.
- **Ch 3:** career models from Frumes/Indap, Indap, Mielle, Friedman, Higgins and Derrough.
- **Ch 4:**
  - Trend Watch box: **systematic share of US corporate credit, about 1–2% (Oct 2026) versus a 20–25% target**, with Kamenski (Mar 2024) as the earlier point.
  - Use Rosenberg, Obenshain and Ralph Smith.
- **Ch 7:** Ralph Smith (availability bias), Wellington, Mintz, Moallemi, Fraser-Jenkins/Brown.
- **Ch 9–11:** Croce, Takahe, the TTU pair, Karoui, Fridson; TCW's "CCCs cry uncle" for the Ch 11 CCC section.
- **Ch 12:** Rieder, Ivascyn (2023 and 2025), Dimensional.
- **Ch 13 (largest user):**
  - The NYDJ-to-Serta genealogy.
  - The DQ-list, voting-cap and co-op antitrust series.
  - Fox Legal, Kirkland board flips, Securitize-for-J.Crew.
- **Ch 14:**
  - The Roe–Rotaru study and the Serta/Del Monte/American Tire episode.
  - The distressed-cycle panel.
  - "Claude Code shook credit" as an AI-driven sector-shock regime.
- **Ch 16:** backstop fees (ConvergeOne), Hertz 2024, Judge Kaplan, Sussberg, venue risk.
- **Ch 17:**
  - The Odd Lots, Money Stuff (OBDC → Weinstein) and Credit Edge (BDC, PIK, secondaries) arcs.
  - Trillions on the Apollo ETF.
  - The Oaktree memo of Apr 9, 2026, and the three papers in §7.
- **Ch 18 / 22:** Thao Tran, Liquidity Cascades, Shashidhar, Duffie, Younger, April 8, Golay, and the Abdi–Rossi–Wu overnight TRACE talk.
- **Ch 20:** Balchunas, Trillions Mar 2020, Laipply, Janus.
- **Ch 21:** the Majewski 2022/2026 pair, Bates, the CLO cluster, FIS loan-data "fax".
- **Ch 24:** Ardagh CDS deliverability, plus Weinstein.
- **Ch 25 / 26:** Noetica, HRT (two episodes), Man's 86× token spend.
- **Ch 28:** the Paleologo pair, Morillo, Falk-Wallace, Kumar, Balyasny, Lewinsohn, Barse/Third Avenue.

**New sections and chapters justified:**
1. **New App D `93_appD_media_syllabus`, "The Listening & Reading Syllabus".**
   - This dossier, refreshed each edition and keyed to chapters, with a ten-episode "start here" path.
   - One verified list is cheaper to maintain than 28 scattered ones.
2. **New Ch 13-B `13_ch13b_creditor_organization_coops_dq_lists`, "Creditor Organization as a State Variable: Co-ops, DQ Lists, Voting Caps, Board Flips and Antitrust."**
   - The 2024–26 record (nine-plus dedicated episodes) shows that organizing speed now decides LME outcomes as much as basket capacity does.
3. **Ch 24 section "Deliverable-Obligation Fights in the LME Era: Ardagh 2026"** (equitization-pending bonds; DC split votes).
4. **Ch 25 or 26 section "Mining Market Narrative: Podcast Feeds and Transcripts as Alternative Data"** (a Credit Edge sentiment panel tested against spreads).
5. **Ch 17 section "The BDC Discount Trade: Tenders, NAVs and Volatility Laundering"** (Saba/OBDC II via Money Stuff 2026-03-19 and CA EP.494).
6. **App C entries:**
   - Dwinells (Oct 2026); Kamenski (Mar 2024).
   - HarbourVest's PC-secondaries run-rate above $50B (May 2026).
   - Davidson Kempner's $770B (Apr 2026); Magnetar's $600B (Sep 2026).
   - Man's 86× token-spend growth (Jul 2026); Fridson's 1,000bp call (May 2025).


> **SUPERSEDED (2026-10-18).** This partial Edition 1 dossier is replaced by media_episodes_posts_parts_I_II / _III_IV / _V_VIII. Kept for history; do not resume it.
