# Media & Learning Ecosystem: Podcasts, Newsletters, Talks and Books for Systematic & Special-Situations Credit

**Item:** Podcasts on credit, distressed, market structure, and quant
**Prepared:** 2026-10-17 (researcher, Edition 1 to Edition 2 pipeline)
**Feeds:** every chapter's `### Deep-Dive Resource Graph`. Primary users are Ch 2, 4, 13, 14, 17, 21, 22, 24, 26, 28 and App B/C. Proposed new App D.

**Method and verification standard.** Earlier briefs had to mark nearly every podcast TITLE-ONLY because the shared WebSearch budget kept running out. This dossier gets around that by reading the publishers' own RSS feeds, which are the primary record of what was published and when. On 2026-10-17 I downloaded and parsed these feeds:

- Bloomberg's Omny feeds for *Odd Lots* (1,289 items), *The Credit Edge by Bloomberg Intelligence* (195 items), *Money Stuff: The Podcast* (119), *Masters in Business* (817) and *Trillions* (274).
- Libsyn feeds for *Capital Allocators* (831) and *Macro Musings* (571).
- Transistor feeds for *Cloud 9fin* (282), *Octus Radio* (500, ending Aug 2024) and *The Octus Download* (37).
- Captivate feeds for *Flirting with Models* (128), *Top Traders Unplugged* (975) and *ReSolve Riffs* (248).

Feed links came from Apple's lookup record and Bloomberg's Omny programs/playlists endpoints (`api.omny.fm/orgs/<org>/programs`). Titles, guests and dates below are copied from those feeds. Dates are the feed `pubDate` in UTC, so a US evening release can show the next day.

Every episode URL given here returned HTTP 200 on 2026-10-17. I also confirmed that each host returns 404 for a made-up path (omny.fm, capitalallocators.com, flirtingwithmodels.com, share.transistor.fm). For the two hosts that return a soft 404 (podscripts.co and macromusings.libsyn.com), I checked the page title for each link. Flirting with Models episode handles came from the show's portal API (`app.podcastai.com/api/v1/portal/shows/flirting-with-models/episodes`).

The WebSearch budget ran out after about 14 queries. Nothing below rests on a search I could not repeat. Items I could not verify are left out or marked **CHECK**. Episode or season numbers appear only where the publisher's own feed title carries them (e.g., "EP.209", "S4E12").

---

## 1. Headline findings (what the media record itself tells us)

1. **The best dated statement of the systematic-credit share is now on audio.** On *The Credit Edge* (2026-10-08), Adam Dwinells, Blackstone Credit & Insurance's head of corporate bond strategies, said Blackstone's systematic credit business is about $40B and "can and should be a $100 billion business". He put systematically managed portfolios at about 1–2% of US corporate credit today and expects 20–25%, matching equities, "over the next decade". Pair this with Man Numeric's Paul Kamenski in March 2024: quant holds "very low single digits" of fixed-income share (Man *Long Story Short*, "Extra Credit"). That gives two dated datapoints for the Ch 4 / App C trend line.
2. **The industry's own view of the next frontier is loans, CLOs and EM.** Acadian's Scott Richardson, director of systematic credit (*Credit Edge*, 2026-02-19), said an issuer approach to security selection can work in leveraged loans and "could be extended to structured things that sit on top of that, CLOs and the like". This supports a Ch 21 section on systematic loan selection.
3. **LME law has become a standing beat.** 9fin started a monthly LME-legal series (*Jane's LME Addiction*, from Jan 2025), a second LME series (*LME Doomscrolling*, from Apr 2026) and an in-court series (*The In-Court Report*, from Dec 2025). Recurring topics are DQ lists, voting and concentration caps, co-op antitrust (Optimum/Altice USA) and the 2026 Del Monte / Serta / American Tire rulings. For Ch 13, the creditor-organization layer has become as important as the document trapdoors.
4. **The private-credit narrative arc is in the episode titles.** On *Odd Lots* it runs "booming" (Nov 2023), then "goes dark" (Sep 2024), then "what's actually going on" (Apr 2026), then "entangled with insurance" (Jul 2026). *Credit Edge* runs "BDC storm" (Apr 2026), then "bad PIK" (Aug 2026). *Money Stuff* runs OBDC/OBDC II (Nov 2025), then Boaz Weinstein's tenders (Mar 2026). This mirrors the Ch 17 trend research almost month for month.
5. **No portfolio-trading episode turned up.** I scanned all 1,289 *Odd Lots* feed items: none has "portfolio trading" in its title or description, and none covers credit-ETF creation/redemption specifically. The best audio on bond market structure is older: Chris White (2015, 2020), Rob Elson (2017), Morningstar on bond pricing (2021), Larry Harris on FIMSAC (2021), and a Treasury-side bridge in Ellen Correia Golay on all-to-all trading (*Macro Musings*, 2026-09-21). Ch 19–20 are therefore filling a gap in what is publicly explained.
6. ***Flirting with Models* has exactly three explicitly credit or fixed-income episodes** in 128: Greg Obenshain (S4E12, 2021), Ralph Smith (S5E7, 2022) and Jeff Rosenberg (S7E19, 2025). Its value for this book is mostly adjacent: trend, carry, liquidity cascades and illiquid market-making.

---

## 2. Podcast episodes by book topic

Format: **Show — "Title"** (feed date) · guest · URL · why it is worth the reader's time.

### 2.1 The systematic-credit industry and factor investing (Ch 4, 9, 11, 12)

- **Credit Edge — "Blackstone Is Predicting a Big Surge in Quant Credit Investing"** (2026-10-08) · Adam Dwinells (Blackstone BCBS) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/blackstone-is-predicting-a-big-surge-in-quant-credit-investing · The shelf's Blackstone paper, as audio, with current AUM and market-share numbers.
- **Credit Edge — "Acadian Sees Quants Moving to Loans, CLOs"** (2026-02-19) · Scott Richardson (Acadian) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/acadian-sees-quants-moving-to-loans-clos · A leading quant-credit academic-practitioner on extending to loans and structured credit, alternative data, and execution costs ("without giving a liver and a kidney to Goldman Sachs").
- **Man Group *Long Story Short* — "Extra Credit: Algorithmic Advantage – Systematic Investing in Credit"** (recorded Mar 2024; no publication date on the page) · Robert Lam, Paul Kamenski (Man Numeric), host Danilo Rippa · https://www.man.com/maninstitute/extra-credit-algorithmic-advantage · Companion to `Man_Quantitative_Credit_Alpha_Early_Mover_2022`. It includes the "very low single digits" market-share remark and the idea that 1–2% of idiosyncratic alpha tilts a 6–7% IG cycle return.
- **Flirting with Models — "Jeff Rosenberg – The Past, Present, and Future of Systematic Fixed Income (S7E19)"** (2025-08-18) · BlackRock Systematic Fixed Income · https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN · Traces quant fixed income from sell-side origins to BlackRock's buy-side "topology" of systematic FI. Pair it with `BlackRock_Systematic_High_Yield_Credit`.
- **Flirting with Models — "Greg Obenshain - Quantitative Credit (S4E12)"** (2021-07-19) · Verdad · https://www.flirtingwithmodels.com/episodes/nQBct6plzWH · An ex-Apollo HY PM turned quant argues that credit excess return comes from spotting improving and declining credit conditions, and that "acquiring data may be an edge".
- **Flirting with Models — "Ralph Smith - Scientific Investing in Fixed Income (S5E7)"** (2022-07-11) · BlueCove · https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd · How credit versus rates breadth and liquidity limit strategy design, and why assumptions about bond *availability* change backtests. Directly relevant to Ch 7 and Ch 9.
- **Flirting with Models — "Stacie Mintz – Turning Qualitative Fundamentals into Quantitative Factors (S7E33)"** (2026-08-03) · https://www.flirtingwithmodels.com/episodes/K0x0u3fbJvh · The RSSG-bridge problem in equity form: encoding analyst judgment as features.
- **Masters in Business — "Rick Rieder on Fixed Income Investments"** (2023-02-10) · BlackRock global FI CIO · https://omny.fm/shows/masters-in-business/rick-rieder-on-fixed-income-investments · A discretionary multi-sector allocator's frame, useful as the Ch 12 contrast case.
- **Capital Allocators — "Dan Ivascyn – Fixed Income in the Limelight Again (EP.298)"** (2023-02-20) · PIMCO Group CIO · https://www.capitalallocators.com/podcast/fixed-income-in-the-limelight-again/ · Pair with *Odd Lots* "Dan Ivascyn Is Excited About a New Era in Fixed Income" (2025-12-08, https://omny.fm/shows/odd-lots/dan-ivascyn-is-excited-about-a-new-era-in-fixed-income), the show's 10-year-anniversary episode, for a two-point view of the regime change.
- **Masters in Business — "Financing In The AI Boom: Masters in Business with Bob Michele"** (2026-10-16) · JPMorgan global FICC CIO · https://omny.fm/shows/masters-in-business/financing-in-the-ai-boom-masters-in-business-with-bob-michele · Current macro-credit allocator view on AI-capex funding.
- **Credit Edge — "Dimensional Says High-Yield Public Debt Has the Edge Over Private"** (2025-05-29) · Savina Rizova · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/dimensional-says-public-debt-has-the-edge-over-private · Quote: "There is no outperformance relative to high-yield public bonds". A factor-house prior for the Ch 12 and Ch 17 allocation debate.
- **Credit Edge — "TCW Chops Credit Risk to Lowest in 30 Years as CCCs 'Cry Uncle'"** (2026-10-15) · Bryan Whalen · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tcw-chops-credit-risk-to-lowest-in-30-years-as-cccs-cry-uncle · CCC distress as the leading edge of contagion. Live material for Ch 11's "CCC problem".
- **Credit Edge — "Fridson Sees High Yield Going Distressed in Recession"** (2025-05-01) · Marty Fridson · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fridson-sees-high-yield-going-distressed-in-recession · A dated, falsifiable call ("back to 1,000 basis points on the high-yield index") to score in the Ch 11 / App C tracker.

### 2.2 Trend, carry, hedging and tail behavior (Ch 5, 10, 23)

- **Flirting with Models — "Roberto Croce - Trend and Carry Within Assets, Across Assets, and Over Time (S6E8)"** (2023-06-19) · https://www.flirtingwithmodels.com/episodes/fN5gzryMqiE · The trend-plus-carry combination that Ch 10 ports to CDX.
- **Flirting with Models — "Moritz Heiden & Moritz Seibert – Trend-Following Spreads (S7E25)"** (2026-01-12) · Takahe · https://www.flirtingwithmodels.com/episodes/1iIqmQ7piJd · Trend on spreads under capacity limits, an analogue for trend in off-the-run credit spreads.
- **Flirting with Models — "Hari Krishnan - Market Tremors & Tail Hedging (S5E11)"** (2022-08-08) · https://www.flirtingwithmodels.com/episodes/MeUsl8ow3Z3 · Crowding-driven tail risk. Supports Ch 5 tails and Ch 23 hedging.
- **Credit Edge — "Goldman Tells Credit Investors to Buy Cheap Hedges"** (2025-02-13) · Lotfi Karoui · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/goldman-tells-credit-investors-to-buy-cheap-hedges · A strategist on hedge cost versus left-tail exposure ("the cost of hedging is the lowest it's been in probably a very long time").
- **Top Traders Unplugged — "SI422: Why Trend Following Rewards Patience ft. Katy Kaminski"** (2026-10-17) · https://www.toptradersunplugged.com/podcast/why-trend-following-rewards-patience-ft-katy-kaminski/ ; **"TTU153: Why Investors Keep Getting Trend Following Wrong ft. Patrick Welton"** (2026-09-30) · https://www.toptradersunplugged.com/podcast/why-investors-keep-getting-trend-following-wrong-ft-patrick-welton/ · The current CTA debate that Ch 10 sits inside.

### 2.3 Market structure, electronification, pricing and ETFs (Ch 2, 18, 19, 20, 22)

- **Odd Lots — "Episode 2: Under the Hood of the $8 Trln Corporate Bond Market"** (2015-11-16) · Chris White (ex-Goldman, GSessions) · https://omny.fm/shows/odd-lots/episode-2-under-the-hood-of-the-8-trln-corporate-b · The pre-revolution baseline, when bonds traded by phone and a failed dealer-run platform was the cautionary tale. Opens Ch 2's timeline.
- **Odd Lots — "How The Bond Market Changed During A Veteran Trader's Decades On Wall Street"** (2017-07-31) · Rob Elson · https://omny.fm/shows/odd-lots/how-the-bond-market-changed-during-a-veteran-trade · An oral history of the voice desk.
- **Odd Lots — "What We Can Learn About Market Liquidity By Looking At Everyday Life"** (2017-10-09) · Karthik Shashidhar · https://omny.fm/shows/odd-lots/what-we-can-learn-about-market-liquidity-by-lookin · An intuitive account of matching markets and why liquidity "evaporates". A good Ch 18 opener.
- **Odd Lots — "A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True"** (2020-03-23) · Chris White (Viable Markets) · https://omny.fm/shows/odd-lots/a-longstanding-fear-about-the-corporate-debt-marke · Recorded during the March 2020 dislocation. It covers fragmented pricing and the BBB overhang, and is a primary-source mood check for the Ch 20 case study.
- **Odd Lots — "How The Crisis Nearly Blew Up One Of The World's Safest Trades"** (2020-03-26) · Josh Younger (JPMorgan) · https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s · Treasury cash–futures basis failure. The rates-side twin of the credit-ETF dislocation (Ch 20, Ch 22).
- **Odd Lots — "Why the True Price of a Bond Can Still Be Hard To Know"** (2021-04-05) · Morningstar's Maciej Kowara and Eric Jacobson · https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to · Based on their report "Bond Pricing: Agreeing To Disagree". Evaluated-price dispersion is the NAV-uncertainty input to Ch 20 and the mark-model problem in Ch 17.
- **Odd Lots — "Here's Why It's So Hard to Fix the Corporate Bond Market"** (2021-11-18) · Larry Harris (USC; ex-SEC chief economist; FIMSAC) · https://podscripts.co/podcasts/odd-lots/heres-why-its-so-hard-to-fix-the-corporate-bond-market (the publisher feed links only to bloomberg.com/oddlots) · The author of *Trading and Exchanges* on why FIMSAC "hasn't had much success". Essential for Ch 22.
- **Odd Lots — "Darrell Duffie On How to Fix the World's Most Important Market"** (2023-08-28) · https://omny.fm/shows/odd-lots/darrell-duffie-on-how-to-fix-the-world-s-most-impo · Dealer balance-sheet capacity and central clearing. The Treasury-clearing mandate background for Ch 22.
- **Odd Lots — "What We Learned About Treasuries on the Night of April 8"** (2025-04-28) · https://omny.fm/shows/odd-lots/what-we-learned-about-treasuries-on-the-night-of-april-8 · The 2025 safe-haven breakdown, for Ch 8's hedge-ratio instability and Ch 22.
- **Macro Musings — "Ellen Correia Golay on All-to-All Trading and Treasury Market Liquidity"** (2026-09-21) · NY Fed · https://macromusings.libsyn.com/ellen-correia-golay-on · Covers the March 2020 "dash for cash", all-to-all reform and principal trading firms, the Treasury analogue of Ch 2's all-to-all story. Earlier episode: "Ellen Correia Golay on the Keys to Improving Treasury Market Resiliency" (2024-11-25), https://macromusings.libsyn.com/ellen-correia-golay-on-the-keys-to-improving-treasury-market-resiliency.
- **Odd Lots — "Episode 18: The Obscure Report That Spawned the ETF Industry"** (2016-03-07) · Eric Balchunas · https://omny.fm/shows/odd-lots/episode-18-the-obscure-report-that-spawned-the-etf · The 1987 SEC-report origin story behind Ch 20's AP machinery.
- **Odd Lots — "ETFs Are Eating the Financial World and They're Not Done Yet"** (2017-10-23) · Eric Balchunas, Joel Weber · https://omny.fm/shows/odd-lots/etfs-are-eating-the-financial-world-and-theyre-not · Context on ETF growth.
- **Trillions — "What the Actual ETF Is Going on Right Now"** (2020-03-19) · Katherine Greifeld · https://omny.fm/shows/trillions/what-the-actual-etf-is-going-on-right-now · Recorded in real time on ETF liquidity and fixed income during the March 2020 crash.
- **Masters in Business — "BlackRock's Global Co-Head of iShares Fixed Income ETFs Stephen Laipply"** (2025-06-20) · https://omny.fm/shows/masters-in-business/blackrocks-global-co-head-of-ishares-fixed-income-etfs-stephen-laipply · The issuer's view of who uses bond ETFs and why. Background for HYG/LQD in Ch 20.
- **Flirting with Models — "Thao Tran – Market Making Illiquid, Non-Fungible Assets (S7E14)"** (2025-02-03) · https://www.flirtingwithmodels.com/episodes/eNEcTaLcPCU · Inventory risk when each unit is unique (NFTs). This is the closest public audio analogue to quoting an off-the-run bond in Ch 18.
- **Flirting with Models — "Liquidity Cascades"** (2020-09-20) · Newfound paper reading · https://www.flirtingwithmodels.com/episodes/R80rhK4yck3 · "The Coordinated Risk of Uncoordinated Market Participants", a narrative model of liquidity spirals for Ch 18 and Ch 28.
- **Odd Lots — "How the Speed of a Trade Got Down to Nearly the Speed of Light"** (2026-03-02) · Donald MacKenzie · https://omny.fm/shows/odd-lots/how-the-speed-of-a-trade-got-nearly-down-to-the-speed-of-light · The sociology of the latency arms race (Ch 27).

### 2.4 Liability management, restructuring and distressed (Ch 3, 13, 14, 16)

*Cloud 9fin* episodes (feed links on share.transistor.fm):
- **"Not Your Daughter's Liens — Sid Levinson and team recall the original uptier LME"** (2026-03-10) · https://share.transistor.fm/s/cf13a6ad · The 2017 NYDJ deal as the first uptier, from counsel to the majority lenders. They compare it with Serta, J.Crew, Envision, Robertshaw, Trimark, Boardriders, PetSmart/Chewy, Caesars and Xerox, which makes it a ready-made Ch 13 genealogy.
- **"Introducing Jane's LME addiction: The bookends of the Serta era"** (2025-01-08) · https://share.transistor.fm/s/faa4e74d · Walks through the Fifth Circuit's Serta decision.
- **"Eat, sleep, drive — Breaking down the Del Monte, Serta & American Tire trifecta"** (2026-07-21) · Ropes & Gray · https://share.transistor.fm/s/1c4df313 · Judge Lopez's Serta ruling alongside Kaplan (Del Monte) and Goldblatt (American Tire) on pro rata sharing, sacred rights and LME damages. These are the 2026 regime-shift inputs for Ch 14.
- **"LME Doomscrolling — Data-driven reality check"** (2026-04-07) · Mark Roe and Vasile Rotaru (Harvard Law) · https://share.transistor.fm/s/1f62123b · Their study "Liability Management's Limited Runway: Corporate Restructuring Today" measures how non-pro-rata coercive LMEs fare. It supplies Ch 14 re-default priors.
- **"Co-op agreements through the eye of American Needle"** (2024-09-25) · https://share.transistor.fm/s/44a5c9af · The Sherman Act theory against cooperation agreements.
- **"Jane's LME Addiction — Co-Optimum — Navigating the Altice USA antitrust litigation"** (2026-01-13) · Cleary Gottlieb · https://share.transistor.fm/s/40588778 · The live co-op antitrust test case.
- **"Jane's LME Addiction — DQ lists are overrated"** (2025-07-17) · Jason Mudrick; Akin Gump · https://share.transistor.fm/s/cce68471
- **"Jane's LME Addiction — Are lender voting and concentration caps the new and improved DQ lists?"** (2025-11-13) · Davis Polk · https://share.transistor.fm/s/ea154cb9 · New "anti-co-op" document language, which Ch 25 should parse.
- **"Jane's LME Addiction — BofA drops in on a double Black Diamond navigating uncharted DQ litigation slopes"** (2026-08-10) · https://share.transistor.fm/s/3af5e46f · The Black Diamond v. Bank of America trial on enforcing DQ lists.
- **"Jane's LME Addiction — The minority report with Shai Schmidt"** (2025-09-15) · https://share.transistor.fm/s/a41d627c · When minority holders should organize, negotiate or litigate, as a game-theory input for Ch 13.
- **"Jane's LME Addiction — Is a deal away going your way?"** (2025-08-13) · Sound Point · https://share.transistor.fm/s/777d460b · Credible versus bluff "deal-away" threats in private-credit LMEs.
- **"LME Doomscrolling — Just because you can, doesn't mean you should"** (2026-08-31) · Bill Derrough (Jefferies) · https://share.transistor.fm/s/6a6999bb · A banker known for high creditor-participation deals, close to the reader's own RSSG seat.
- **"Liability Management with Andy Hagan, Tom Richards and Gilles Teerlinck of Weil, Gotshal & Manges"** (2023-04-06) · https://share.transistor.fm/s/ad25aba2
- **"Securitize for a J.Crew reprise"** (2023-07-06) · https://share.transistor.fm/s/5101c481 · Loose securitization baskets as the next trapdoor. Gives Ch 25 a concrete clause to flag.
- **"Drop-downs, the Lycra variant"** (2023-05-18) · https://share.transistor.fm/s/74bfd3a2
- **"The ABCs of private credit LMEs, with Freshfields"** (2024-06-07) · https://share.transistor.fm/s/51aeecca
- **"The In-Court Report with Cat Corey — The latest on backstop fees in rights offerings and DIP financings"** (2025-12-09) · Vince Buccola (Chicago Law) · https://share.transistor.fm/s/ad684efa · Backstop economics after ConvergeOne. Core material for Ch 16.
- **"It Hertz you to see it"** (2024-06-26) · https://share.transistor.fm/s/d607390a · A Hertz 2024 sequel to the book's Hertz 2020 post-reorg case.

*Bloomberg and other shows*:
- **Odd Lots — "Inside the Blood Sport of Creditor-on-Creditor Violence"** (2024-11-25) · Sujeet Indap (FT) · https://omny.fm/shows/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-vio · The best general-audience introduction to why cov-lite paper led to LMEs.
- **Capital Allocators — "Max Frumes and Sujeet Indap – Inside the Sausage Factory of the Caesar's Restructuring (EP.209)"** (2021-08-16) · https://www.capitalallocators.com/podcast/inside-the-sausage-factory-of-the-caesars-restructuring/ · The authors of *The Caesars Palace Coup* on a PE restructuring "gone wrong". Pre-LME-era context for Ch 3.
- **Credit Edge — "Divisive Debt Maneuvers; Bank Stress Returns"** (2023-04-27) · Reshmi Basu · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/divisive-debt-maneuvers-bank-stress-returns · The 2023 wave of drop-down lawsuits.
- **Credit Edge — "Distressed Creditors Play Nice; Telecoms in Focus"** (2023-07-27) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/distressed-creditors-play-nice-telecoms-in-focus · Carvana 2023 as a "rare case" of lender cooperation, eliminating $1.2B of debt. Primary color for the Carvana case study.
- **Credit Edge — "Fidelity Fears Creditor Violence Spread; Altice Focus"** (2024-02-15) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/fidelity-fears-creditor-violence-spread-altice-foc ; **"Altice 'Jenga Tower' Menaces Global Credit Markets"** (2024-04-25) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/altice-jenga-tower-menaces-global-credit-markets · US-style LMEs reaching Europe (Altice France, more than €24B of debt).
- **Credit Edge — "Junk Companies Are in Debt Covenant 'La La Land,' Says Fox Legal"** (2025-07-31) · Sabrina Fox · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/junk-companies-are-in-debt-covenant-la-la-land-says-fox-legal · A covenant trainer on add-backs that are "departures from reality", which is Ch 13's EBITDA-cap thesis in one sentence.
- **Credit Edge — "Kirkland & Ellis Sees More Distressed Lenders Flipping Company Boards"** (2026-10-01) · H.T. Flanagan · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/kirkland-ellis-sees-more-distressed-lenders-flipping-company-boards · Board-replacement remedies used "with greater frequency". A new state variable for Ch 13.
- **Credit Edge — "Lumen's CFO Looks Ahead After 'Moonshot' Debt Deal That Worked"** (2026-09-17) · Chris Stansbury · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/lumen-s-cfo-looks-ahead-after-moonshot-debt-deal-that-worked · The issuer's account of one of the largest out-of-court restructurings ("keep as many winners as possible").
- **Credit Edge — "Judge's Downfall Shocks Bankruptcy World; Oil M&A"** (2023-10-19) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/judge-s-downfall-shocks-bankruptcy-world-oil-m-a · Venue risk after the Texas judge's resignation, for Ch 16 forum modeling.
- **Credit Edge, distressed-cycle panel** (score these calls in App C):
  - "Mudrick Sees Seven-Year Default Wave as Rates Stay Up" (2025-08-14), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/mudrick-sees-seven-year-default-wave-as-rates-stay-up
  - "Distressed Buyer H.I.G. Sees Most Loan Distress in Years (Podcast)" (2026-02-05), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/distressed-buyer-h-i-g-sees-most-loan-distress-in-years-podcast
  - "Bain Sees Software Debt Defaults Spiking" (2026-02-26; "double digits"), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bain-sees-software-debt-defaults-spiking
  - "Davidson Kempner Sees a $770 Billion Stressed Debt Opportunity" (2026-04-16; "year three of… the longest default cycle in 20 years"), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/davidson-kempner-sees-a-770-billion-stressed-debt-opportunity
  - "Magnetar Scours $600 Billion Stressed Debt Pile for Bond, Loan Value" (2026-09-24), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/magnetar-scours-600-billion-stressed-debt-pile-for-bond-loan-value
  - "Sculptor Sees Opportunity in Busted Capital Structures" (2024-09-05), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/sculptor-sees-opportunity-in-busted-capital-struct
- **Masters in Business — "King Street's Brian Higgins On Navigating Distressed Markets"** (2024-10-18) · https://omny.fm/shows/masters-in-business/king-streets-brian-higgins-on-navigating-distresse ; also **Capital Allocators — "King Street"** (Manager Meeting EP.21 in the feed, 2021-11-24) · https://www.capitalallocators.com/podcast/king-street/
- **Masters in Business — "Dominique Mielle on Luck and Resilience in Finance"** (2023-03-24) · ex-Canyon partner · https://omny.fm/shows/masters-in-business/dominique-mielle-on-luck-and-resilience-in-finance ; **Capital Allocators — "Josh Friedman – Master Class in Credit Investing at Canyon (EP.263)"** (2022-07-25) · https://www.capitalallocators.com/podcast/master-class-in-credit-investing-at-canyon/ · The Canyon lineage of distressed credit and risk arbitrage.
- **Capital Allocators — "Peter Troob – Monkey Business in High Yield (EP.59)"** (2018-07-02) · https://www.capitalallocators.com/podcast/monkey-business-in-high-yield/ ; **"Andrew Milgram – Mid-Market Distressed Investing at Marblegate (Manager Meetings EP.29)"** (2022-04-21) · https://www.capitalallocators.com/podcast/mid-market-distressed-investing-at-marblegate/ ; **"Tony Yoseloff – Forty Years of Davidson Kempner (EP.313)"** (2023-05-08) · https://www.capitalallocators.com/podcast/forty-years-of-davidson-kempner/ ; **"Jeff Aronson – Building Centerbridge Across the Capital Structure (EP.468)"** (2025-11-03) · https://www.capitalallocators.com/podcast/building-centerbridge-across-the-capital-structure/ · Founder-level accounts of how distressed shops are organized, for Ch 28's team design.
- **Masters in Business — "Jim Millstein on the Fed and AIG's Restructuring (Podcast)"** (2018-10-26) · former Treasury chief restructuring officer · https://omny.fm/shows/masters-in-business/jim-millstein-on-the-fed-and-aig-s-restructuring-p
- **The Octus Download — "EP 21 | How Bankruptcy Really Works: Inside the System with Josh Sussberg"** (2025-12-10) · Kirkland & Ellis · https://share.transistor.fm/s/81750469 ; **"EP 22 | Judge Michael B. Kaplan, Vegas Squeeze & the First Brands Conspiracy"** (2025-12-23) · US Bankruptcy Judge, D.N.J. · https://share.transistor.fm/s/aaf0387e ; **"EP 31 | Michael Gatto on Distressed Debt…"** (2026-06-10) · Silver Point · https://share.transistor.fm/s/ae8e9543 · Both sides of the courtroom, the bench included.
- **Octus Radio — "Conversations With Reorg: Akin Gump Discusses Liability Management Exercises"** (2023-03-21) · https://share.transistor.fm/s/155fa539 ; **"Reorg Special Podcast: Altice France - Creditors Mobilize as Drahi Tries to Wield the Stick"** (2024-03-27) · https://share.transistor.fm/s/635346d3 ; **"Italian Telcos Open Fiber, Eolo Struggle; J. Crew Blocker Trends; Primary Highlights"** (2023-11-28) · https://share.transistor.fm/s/e0222425 · Blocker-adoption trends, which Ch 25 can use as an annotation target.

### 2.5 Private credit and public–private convergence (Ch 17, also 12, 14)

- **Odd Lots arc:**
  - "Why Private Credit's Been Booming Even as Interest Rates Go Up" (2023-11-20; Laura Holson, New Mountain), https://omny.fm/shows/odd-lots/why-private-credits-been-booming-even-as-interest
  - "This Is the Impact of Billions Flowing Into Private Credit" (2024-01-08; Ben Emons), https://omny.fm/shows/odd-lots/this-is-the-impact-of-billions-flowing-into-privat
  - "The Black Hole of Private Credit That's Swallowing the Economy" (2024-09-02; Jared Ellias and Elisabeth de Fontenay on their paper "The Credit Markets Go Dark"), https://omny.fm/shows/odd-lots/the-black-hole-of-private-credit-thats-swallowing
  - "Apollo Explains How Big Tech Is Disrupting Credit Markets" (2024-10-14; Rob Bittencourt), https://omny.fm/shows/odd-lots/101024-odd-lots-rob-bittencourt-v1
  - "How Banks and Private Credit Became the Best of Frenemies" (2024-10-24; Huw van Steenis), https://omny.fm/shows/odd-lots/102424-odd-lots-huw-van-steenis-master-3
  - "How Oaktree's Head of Sourcing Finds the Next Great Deal" (2024-11-28; Milwood Hobbs), https://omny.fm/shows/odd-lots/how-oaktrees-head-of-sourcing-finds-the-next-great
  - "Blackstone's Michael Zawadzki on How Private Credit Got so Big" (2026-01-23), https://omny.fm/shows/odd-lots/blackstones-michael-zawadzki-on-how-private-credit-got-so-big
  - "What's Actually Going On With Private Credit" (2026-04-27; Osterweis's John Sheehan and Craig Manchuck), https://omny.fm/shows/odd-lots/whats-actually-going-on-with-private-credit
  - "Why Private Credit Got Entangled With Insurance" (2026-07-31; Andrew Granato and Pranjal Drall, "Private Credit's State Backstop: How Private Equity Socializes Risk Through Insurers"), https://omny.fm/shows/odd-lots/why-private-credit-got-entangled-with-insurance
  - Together these give Ch 17's narrative spine, each episode a dated waypoint. The insurance episode pairs with the NAIC/RBC thread in `trend_private_credit_convergence.md`.
- **Money Stuff: The Podcast:**
  - "Funny Business Is My Business: PRIV, HHH, WARS" (2025-02-28; the Apollo/State Street private-credit ETF launch), https://omny.fm/shows/money-stuff-the-podcast/funny-business-is-my-business-priv-hhh-wars
  - "Bat Tat: Labubu, OBDC, Frank" (2025-11-21; OBDC/OBDC II, private-credit marks), https://omny.fm/shows/money-stuff-the-podcast/bat-tat-labubu-obdc-frank
  - "Man Not Bird" (2026-03-13; marking private credit to market, NAV arbitrage), https://omny.fm/shows/money-stuff-the-podcast/man-not-bird
  - "Boaz Weinstein" (2026-03-19; Saba's tenders for OBDC II and SREIT, public versus private BDC discounts, "volatility laundering"), https://omny.fm/shows/money-stuff-the-podcast/boaz-weinstein
  - "Frisky Dentists" (2026-05-15; CLOs, trading private credit, daily pricing), https://omny.fm/shows/money-stuff-the-podcast/frisky-dentists
  - "Good Game: WBD, Tricolor, TAE" (2025-12-19; double-pledging, cooperation agreements), https://omny.fm/shows/money-stuff-the-podcast/good-game-wbd-tricolor-tae
  - The Weinstein episode is the practitioner statement of Ch 17's "what a public-markets desk can arbitrage" thesis.
- **Credit Edge:**
  - "PGIM Sees 'Chilling Effect' on Private Credit From BDC Storm" (2026-04-02), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/pgim-sees-chilling-effect-on-private-credit-from-bdc-storm
  - "BDC Veteran Expects Private Credit Fund Stress as Banks Pull Back" (2026-03-19; SLR's Michael Gross), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bdc-veteran-expects-private-credit-fund-stress-as-banks-pull-back
  - "HarbourVest Expects Private Credit Secondaries Volume to Double" (2026-05-07; "run-rating above $50 billion"), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/harbourvest-expects-private-credit-secondaries-volume-to-double
  - "Investors Keeping Score on 'Bad PIK', Benefit Street Partners' Kumar Says" (2026-08-06), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/investors-keeping-score-on-bad-pik-and-stale-marks-benefit-street-partners-kumar-says
  - "Janus Is Skeptical of Private Credit's Push Into ETFs" (2025-04-03), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/janus-is-skeptical-of-private-credit-s-push-into-etfs
  - "Citi Warns of Private Debt Risk as 'Tourists' Are Forced to Sell" (2026-04-30), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/citi-warns-of-private-debt-risk-as-tourists-are-forced-to-sell
  - "Silver Point Sees 'Game Over' for Some Private Debt Funds When Cycle Turns" (2025-06-18), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/silver-point-sees-game-over-for-some-private-debt-funds-when-cycle-turns
  - "Monarch Sees Bigger Hazard Than Fraud" (2025-10-23), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/monarch-sees-bigger-hazard-than-fraud
- **Trillions — "The Apollo ETF Landing"** (2024-09-26) · https://omny.fm/shows/trillions/the-apollo-etf-landing · The PRIV filing and Apollo's "liquidity backstop". Pairs with the firm-bid mechanics in Ch 17.
- **Capital Allocators:**
  - "Howard Marks – Navigating Private Credit (EP.439)" (2025-04-07), https://www.capitalallocators.com/podcast/navigating-private-credit/
  - "Kieran Goodwin – Private Credit Concerns (EP.494)" (2026-03-30; Saba), https://www.capitalallocators.com/podcast/private-credit-concerns/
  - "Kipp deVeer – The World of Private Credit at Ares (EP.329)" (2023-07-24), https://www.capitalallocators.com/podcast/the-world-of-private-credit-at-ares/
  - "Ron Kantowitz – Direct Lending's Evolution and Invesco's Edge (EP.457)" (2025-07-17), https://www.capitalallocators.com/podcast/direct-lendings-evolution-and-invescos-edge/
  - "Scott Kleinman – Apollo's Integrated Alternatives Platform (EP.481)" (2026-01-19), https://www.capitalallocators.com/podcast/apollos-integrated-alternatives-platform/
- **Masters in Business:**
  - "Ken Kencel on the Rise of Private Capital" (2023-03-31; Churchill/Nuveen), https://omny.fm/shows/masters-in-business/ken-kencel-on-the-rise-of-private-equity-credit
  - "Armen Panossian on Credit in a Time of Rising Rates" (2023-09-22; Oaktree), https://omny.fm/shows/masters-in-business/armen-panossian-on-credit-in-a-time-of-rising-rate
  - "Building a Global Private Credit Firm and 'Trading' Planes with Victor Khosla" (2024-09-19; SVP), https://omny.fm/shows/masters-in-business/building-a-global-private-credit-firm-and-trading
  - "The Future of Private Credit with Erik Hirsch" (2025-07-31; Hamilton Lane), https://omny.fm/shows/masters-in-business/the-future-of-private-credit-with-erik-hirsch
- **Macro Musings — "Richard Berner on Growth of the Private Credit and the Role of Fiscal Dominance on Treasury Markets"** (2026-01-19) · ex-OFR director · https://macromusings.libsyn.com/richard-berner-on-growth-of-the-private-credit-and-the-role-of-fiscal-dominance-on-treasury-markets · The financial-stability regulator's frame.
- **Cloud 9fin:**
  - "Getting real about synthetic PIKs" (2024-09-18), https://share.transistor.fm/s/86021e09
  - "Decoding the software lending shock in private credit with MSCI" (2026-04-03), https://share.transistor.fm/s/3914343b
  - "Distressed Diaries — More private credit cockroaches crawling out?" (2025-11-06), https://share.transistor.fm/s/58e29ad3
  - "William Cohan reveals how Apollo and Leon Black ushered in the private credit boom amid fortune and scandal" (2026-09-08), https://share.transistor.fm/s/a9168970

### 2.6 Leveraged loans and CLOs (Ch 21)

- **Capital Allocators — "Thomas Majewski – Empty Rooms: Masterclass on CLOs at Eagle Point Credit Management (EP. 284)"** (2022-12-01) · https://www.capitalallocators.com/podcast/empty-rooms-masterclass-on-clos-at-eagle-point-credit-management/ ; follow with **Credit Edge — "Bull Run in Loans Slams CLO Equity Buyers, Says Eagle Point's Majewski"** (2026-07-16) · https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/bull-run-in-loans-slams-clo-equity-buyers-says-eagle-point-s-majewski · The same manager in 2022 and 2026: CLO equity's sensitivity to repricing waves, which is Ch 21's repricing-wave section in miniature.
- **Capital Allocators — "Shiloh Bates – CLO Investing at Flat Rock Global (EP.379)"** (2024-04-11) · https://www.capitalallocators.com/podcast/clo-investing-at-flat-rock-global/ · The author of the 2023 book *CLO Investing* on structure, payoff rules and history.
- **Capital Allocators — "Brett Jefferson – Inefficiencies in Structured Credit at Hildene…"** (First Meeting EP.19, 2020-05-25) · https://www.capitalallocators.com/podcast/first-meeting-ep-19-capturing-inefficiencies-in-structured-credit-at-hildene-capital-management/ ; **"Greg Lippmann – The Big Short and Structured Credit at LibreMax (EP.270)"** (2022-09-12) · https://www.capitalallocators.com/podcast/the-big-short-and-structured-credit-at-libremax/
- **Credit Edge, CLO cluster:**
  - "Hedge Funds Are Diving Into CLOs; AT1s Revitalize" (2023-09-07), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/hedge-funds-are-diving-into-clos-at1s-revitalize
  - "Altice Stress Weighs on CLO Market, Sound Point Says" (2024-03-28), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/altice-stress-weighs-on-clo-market-sound-point-say
  - "PGIM Lauds 'Bulletproof' CLOs as Credit Risks Rise" (2025-06-12), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/pgim-lauds-bulletproof-clos-as-credit-risks-rise
  - "Tetragon Sees Midteens Gain in Riskiest CLO Tranche" (2025-08-21), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/tetragon-sees-midteens-gain-in-riskiest-clo-tranche
  - "CLOs Are Tough to Blow Up, Crescent Says" (2025-10-02), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/clos-are-tough-to-blow-up-crescent-says
  - "Loan Defaults Outpace Bonds; Country Garden Woes" (2023-08-17; the loan-versus-bond default divergence), https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence/loan-defaults-outpace-bonds-country-garden-woes
- **Cloud 9fin — "Bringing loan data from fax to the future"** (2025-03-06) · FIS · https://share.transistor.fm/s/14a1ade2 · Loan settlement still runs partly on fax. This is the plumbing story behind Ch 21's settlement-lag math.
- **Odd Lots — "The Hottest Way for Banks to Get Risk Off Their Balance Sheets"** (2024-08-22) · Michael Shemi (Guy Carpenter) · https://omny.fm/shows/odd-lots/the-hottest-way-for-banks-to-get-risk-off-their-ba · Synthetic risk transfers, the bank-capital side of Ch 21 and Ch 22.

### 2.7 CDS, basis and capital-structure arbitrage (Ch 23, 24)

- **Cloud 9fin — "Distressed Diaries — Ardagh CDS and the empty glass paradox"** (2026-01-21) · https://share.transistor.fm/s/903a348d · Arini challenged whether bonds already marked for equitization were deliverable ("Schrödinger's Obligations"). The EMEA DC rejected the challenge in a split vote, with Citi and Pimco dissenting according to the feed text. This is a ready-made 2026 case for Ch 24's deliverable-obligation section.
- **Masters in Business — "Boaz Weinstein on Credit Investments"** (2022-05-13) · https://omny.fm/shows/masters-in-business/boaz-weinstein-on-credit-investments ; **"Boaz Weinstein on Investors' Unknown Risk"** (2022-11-24) · https://omny.fm/shows/masters-in-business/boaz-weinstein-on-investors-unknown-risk · The Deutsche Bank credit-trading founder of Saba on CDS-era cap-structure trading and tail convexity.
- **Capital Allocators — "Nancy Zimmerman – People, Process, and Fixed Income Arbitrage at Bracebridge (EP.517)"** (2026-09-28) · https://www.capitalallocators.com/podcast/people-process-and-fixed-income-arbitrage-at-bracebridge/ · Thirty years of relative-value process. Context for Ch 24's basis trades and Ch 28.

### 2.8 NLP, AI agents and systems (Ch 25, 26, 27)

- **Odd Lots — "AI Can Tell Us Something About Credit Market Weakness"** (2025-12-04) · Dan Wertman (Noetica) · https://omny.fm/shows/odd-lots/ai-can-tell-us-something-about-credit-market-weakness · AI-measured trends in the language of deal documents. The commercial version of Ch 25's covenant AST.
- **Cloud 9fin — "Claude Code shook credit. What breaks next?"** (2026-07-02) · https://share.transistor.fm/s/7a979a47 · An AI coding agent as a *credit* shock (software sell-off, Medallia handing keys to lenders). This is the Ch 26 / Ch 14 bridge.
- **Odd Lots — "How Hudson River Trading Actually Uses AI"** (2025-10-31) · https://omny.fm/shows/odd-lots/how-hudson-river-trading-actually-uses-ai ; **"Inside Hudson River Trading's Blistering Token Burn"** (2026-06-05) · https://omny.fm/shows/odd-lots/inside-hudson-river-tradings-blistering-token-burn ; **"One of the World's Largest Hedge Funds on Its 86x Growth in Token Spending"** (2026-07-09; Man Group CTO Gary Collier and Head of Data & AI Tushara Fernando) · https://omny.fm/shows/odd-lots/one-of-the-worlds-largest-hedge-funds-on-its-86x-growth-in-token-spending · How a market maker and a quant manager actually budget and govern LLM use. These are the Ch 26 operating-manual anchors.
- **Flirting with Models — "Ben Wellington – Complex Feature Engineering at Two Sigma (S7E32)"** (2026-07-06) · https://www.flirtingwithmodels.com/episodes/mDCRKBfrVHQ · Feature-engineering discipline for Ch 7.
- **Odd Lots — "What It Takes To Win At Quant Investing"** (2020-10-08; Ciamac Moallemi) · https://omny.fm/shows/odd-lots/what-it-takes-to-win-at-quant-investing ; **"Inigo Fraser-Jenkins and Aaron Brown Debate The Future Of Quant Investing"** (2020-11-23) · https://omny.fm/shows/odd-lots/inigo-fraser-jenkins-and-aaron-brown-debate-the-fu · The quant-winter argument. Its stationarity worries are Ch 7's.
- **Masters in Business — "David Snyderman on Specialty Finance and Data in Investing"** (2024-03-01) · Magnetar, ex-Citadel global credit · https://omny.fm/shows/masters-in-business/david-snyderman-on-specialty-finance-and-data-in-i

### 2.9 The PM playbook: multi-strats, pods and risk (Ch 28)

- **Odd Lots:**
  - "How to Succeed at Multi-Strategy Hedge Funds" (2024-05-20; Giuseppe Paleologo), https://omny.fm/shows/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds
  - "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (2025-06-21, recorded live 2025-06-12), https://omny.fm/shows/odd-lots/giuseppe-paleologo-on-quant-investing-at-multi-strat-hedge-funds
  - Both are the audio companions to the shelf's `Paleologo_Advanced_Portfolio_Management`.
- **Odd Lots:**
  - "How the Rise of 'Pod Shops' Is Reshaping the Way Markets Trade" (2024-02-26; Krishna Kumar), https://omny.fm/shows/odd-lots/022624-odd-lots-krishna-kumar-master-1
  - "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (2024-07-25; Rich Falk-Wallace, ex-Citadel), https://omny.fm/shows/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really
  - "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (2024-10-07; Dan Morillo, ex-Citadel), https://omny.fm/shows/odd-lots/100724-odd-lots-dan-morillo-master
  - Covers crowding, capital allocation and drawdown rules, which become Ch 28's stop-loss and allocation equations.
- **Capital Allocators:**
  - "Dmitry Balyasny – Multi-Strategy Platform at BAM (EP.341)" (2023-10-02), https://www.capitalallocators.com/podcast/multi-strategy-platform-at-bam/
  - "Luke Ellis – The Man Behind The Man Group (EP.214)" (2021-09-20), https://www.capitalallocators.com/podcast/the-man-behind-the-man-group/
  - "Jonathan Lewinsohn – Credit Microcycles at Diameter (EP.484)" (2026-02-02), https://www.capitalallocators.com/podcast/credit-microcycles-at-diameter/
  - A credit-specific founder on "microcycles": a discretionary counterpart to Ch 10's regime models.
- **Odd Lots — "What David Barse Learned From Watching A Credit Fund Blow Up"** (2018-10-01) · https://omny.fm/shows/odd-lots/what-david-barse-learned-from-watching-a-credit-fu · The CEO of Third Avenue on the Dec 2015 fund meltdown. The canonical Ch 28 case of liquidity mismatch in distressed credit.

### 2.10 Credit cycle color (Ch 1, 5, 14)

- **Odd Lots:**
  - "Oaktree's Wayne Dahl on Credit Markets Right Now" (2023-09-18), https://omny.fm/shows/odd-lots/oaktrees-wayne-dahl-on-credit-markets-right-now
  - "The Next Stage of the Credit Cycle with Oaktree's Poli" (2024-09-19), https://omny.fm/shows/odd-lots/the-next-stage-of-the-credit-cycle-with-oaktree-s
  - "The Anonymous Meme Account Chronicling Credit Market Craziness" (2024-01-25; High Yield Harry), https://omny.fm/shows/odd-lots/the-anonymous-meme-account-chronicling-credit-mark
  - High Yield Harry is the book's tone in human form: running gags that ride on correct ideas.
- **Masters in Business — "Oaktree Howard Marks: Masters in Business (Audio)"** (2015-07-19; discusses high yield) · https://omny.fm/shows/masters-in-business/oaktree-howard-marks-masters-in-business-audio ; **"Mark Jenkins on Leveraged Finance and Pension Plans"** (2022-04-21; Carlyle Global Credit) · https://omny.fm/shows/masters-in-business/mark-jenkins-on-leveraged-finance-and-pension-plan
- **Capital Allocators — "David Breazzano - High Yields and Low Risk at Polen Capital (EP.405)"** (2024-09-12) · https://www.capitalallocators.com/podcast/high-yields-and-low-risk-at-polen-capital/ ; **"Chris Acito – Credit Where Credit is Due (EP.33)"** (2017-12-11) · https://www.capitalallocators.com/podcast/credit-where-credit-is-due/ · HY history from a manager investing since the early 1980s.
- **Money Stuff — "Garlic Cartel: Markets, Credit, Code"** (2024-11-08) · https://omny.fm/shows/money-stuff-the-podcast/garlic-cartel-markets-credit-code ; **"No Nap Rooms: Credit, Peace, 24X"** (2025-10-17; "late-cycle credit accidents", banks versus private credit) · https://omny.fm/shows/money-stuff-the-podcast/no-nap-rooms-credit-peace-24x ; **"Another Great Convergence: 7bps, APO, HOOD"** (2025-02-07; plans for private-credit trading) · https://omny.fm/shows/money-stuff-the-podcast/another-great-convergence-7bps-apo-hood

---

## 3. Show directory (subscribe-level, one line each)

| Show | Root URL (verified) | Why subscribe |
|---|---|---|
| Odd Lots (Bloomberg) | https://omny.fm/shows/odd-lots | The widest finance show. Credit appears about monthly and private credit is a recurring arc. |
| The Credit Edge by Bloomberg Intelligence | https://omny.fm/shows/the-credit-edge-by-bloomberg-intelligence | Weekly since Feb 2023 with one named buy-side CIO per episode. A ready-made panel of dated, quotable views (see §7 for using it as a sentiment dataset). |
| Money Stuff: The Podcast | https://omny.fm/shows/money-stuff-the-podcast | The audio companion to Matt Levine's column (feed description), and the house style's spiritual parent. |
| Masters in Business | https://omny.fm/shows/masters-in-business | Long-form career interviews. Strongest on credit founders (Weinstein, Higgins, Khosla, Snyderman). |
| Capital Allocators | https://www.capitalallocators.com/ | The allocator's lens. Its EP-numbered credit back catalog is the deepest of any show here. |
| Flirting with Models | https://www.flirtingwithmodels.com/ | Quant process. Mostly adjacent to credit, but rigorous. |
| Cloud 9fin | https://9fin.com/podcasts | The best LME-legal audio anywhere, with monthly series. |
| Octus Radio / The Octus Download | https://share.transistor.fm/s/81750469 (episode) · feeds `feeds.transistor.fm/octus-radio`, `feeds.transistor.fm/the-octus-download` | Docket-level restructuring news (formerly Reorg). octus.com returned 403 to automated fetch. |
| Macro Musings | https://macromusings.libsyn.com/ellen-correia-golay-on (episode) | Treasury market structure and the Fed. |
| Trillions (Bloomberg) | https://omny.fm/shows/trillions/the-apollo-etf-landing (episode) | ETF structure, including private credit in ETFs. |
| Top Traders Unplugged | https://www.toptradersunplugged.com/ | Trend-following practitioners (Ch 10). |
| ISDA podcast | https://www.isda.org/2026/10/01/episode-60-modelling-margin/ | Derivatives plumbing (margin, documentation). Episode 60 is on margin modeling. |

---

## 4. Newsletters, blogs and research portals (verified live 2026-10-17)

- **Howard Marks memos (Oaktree)**, https://www.oaktreecapital.com/insights/memos · Recent memos on the page: "What's Going on in Private Credit?" (Apr 9, 2026), "Cockroaches in the Coal Mine" (Nov 6, 2025), "Gimme Credit" (Mar 6, 2025), "The Impact of Debt" (May 8, 2024). They are cycle-psychology essays that Ch 14 and Ch 17 can quote by title and date.
- **PETITION**, https://www.petition11.com/ · Describes itself as "curated financial news, analysis and commentary with an emphasis on distressed investing, restructuring and bankruptcy". The irreverent restructuring voice closest to this book's.
- **Net Interest (Marc Rubinstein)**, https://www.netinterest.co/ · Bank and financial-institution economics. Useful for the dealer-capital sections of Ch 22.
- **The Diff (Byrne Hobart)**, https://www.thediff.co/ · "Inflections in Finance and Tech". Market-structure and AI-economics essays.
- **Credit Slips**, https://creditslips.org/ · "A Discussion on Credit, Finance & Bankruptcy" by bankruptcy academics. Fast commentary on LME and venue rulings.
- **Liberty Street Economics (NY Fed)**, https://libertystreeteconomics.newyorkfed.org/ ; **FEDS Notes (Federal Reserve Board)**, https://www.federalreserve.gov/econres/notes/feds-notes/default.htm · The primary-source stream behind most of the Ch 17 and Ch 22 trend numbers.
- **Verdad research archive**, https://verdadcap.com/archive · Credit-relevant posts include "The Reflexivity of Credit Markets" (Apr 20, 2026) and "Echoes of Junk Bonds Past" (Apr 6, 2026). It is the written companion to the Obenshain episode.
- **Man Group insights**, https://www.man.com/insights (the Man Institute URL redirects here) · Where the shelf's two Man papers and the *Long Story Short* podcast live.
- **AQR research**, https://www.aqr.com/Insights/Research ; **Robeco insights**, https://www.robeco.com/en-int/insights · The academic-style quant-credit factor literature (Ch 9).
- **9fin insights**, https://9fin.com/insights ; **CreditSights**, https://www.creditsights.com/ ; **KBRA**, https://www.kbra.com/ · Vendor research. Mostly paywalled but cited across Ch 13, 14 and 17.
- **Octus article "RX 101: Creditor-on-Creditor Violence"**, https://octus.com/resources/articles/rx-101-creditor-on-creditor-violence (surfaced by a WebSearch result this session; direct fetch hit a 403 Cloudflare wall) · A primer-level glossary for Ch 13.

**Checked but not usable this session:** Money Stuff newsletter page (bloomberg.com, 403), FT Alphaville (403), Alpha Architect (403), Tradeweb insights (403), Quantpedia (466), Harvard Bankruptcy Roundtable (403), MarketAxess /research (404), FINRA TRACE "about" path (404), Apollo "Daily Spark" path (404), BlackRock *The Bid* path (404). Cite these by name only until a later session verifies them.

---

## 5. Talks, seminars and courses

- **The Microstructure Exchange**, https://microstructure.exchange/ · A virtual academic forum of one-hour Zoom webinars with an archive. On the current page: **Farshid Abdi (with Marco Rossi and Botao Wu), "Overnight Corporate Bond Trading," Sept 15, 2026**. It concerns trades executed between 6:30 p.m. and 8:00 a.m. that TRACE does not disseminate until the next morning. That is a new TRACE-latency fact for Ch 18 and Ch 22.
- **Live-recorded Odd Lots episodes:** Paleologo at the Bloomberg Equity Intelligence Summit (recorded 2025-06-12) and Wayne Dahl at Future Proof (2023-09-18). Both are listed above.
- **MIT OpenCourseWare 18.S096, "Topics in Mathematics with Applications in Finance" (Fall 2013)**, https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/ · Free lectures covering the Ch 5–6 prerequisites (stochastic processes, Itô calculus, regression, time series).
- **ISDA podcast Episode 60, "Modelling Margin"** (2026-10-01), https://www.isda.org/2026/10/01/episode-60-modelling-margin/

---

## 6. Books (existence verified via the publisher feed text of the episodes named; no links)

- Max Frumes & Sujeet Indap, *The Caesars Palace Coup: How a Billionaire Brawl Over the Famous Casino Exposed the Corruption of the Private Equity Industry* (out by Aug 2021, per Capital Allocators EP.209; full subtitle from the Odd Lots 2024-11-25 feed text). Ch 3 and Ch 13 required reading.
- Dominique Mielle, *Damsel in Distressed: My Life in the Golden Age of Hedge Funds* (2021, per MIB 2023-03-24). Canyon-era distressed practice.
- Shiloh Bates, *CLO Investing* (2023, per Capital Allocators EP.379). Ch 21's practitioner text.
- William D. Cohan, *Money to Burn: The Unvarnished Truth About Leon Black, Apollo, and the Rise of a New Wall Street* (2026, per Cloud 9fin 2026-09-08). History for Ch 17.
- Robin Wigglesworth, *A Fabulous Debt: the Epic Story of How Bonds Built the Modern World* (per TTU IL53, 2026-09-16). Includes the Milken junk-bond chapter of history.
- Donald MacKenzie, *Trading at the Speed of Light* (2021, per Odd Lots 2026-03-02). Ch 27.
- Karthik Shashidhar, *Between the Buyer and the Seller* (per Odd Lots 2017-10-09). Liquidity intuition for Ch 18.
- Antti Ilmanen, *Investing Amid Low Expected Returns* (per ReSolve Riffs 2022-04-13). Ch 9 and Ch 12.
- Eric Balchunas, *The Bogle Effect* (per ReSolve Riffs 2022-03-23). ETF history for Ch 20.

## 7. Papers and studies named in verified episode text (title-only research leads)

| Title | Authors | Named in | Use |
|---|---|---|---|
| "Liability Management's Limited Runway: Corporate Restructuring Today" | Mark Roe, Vasile Rotaru | Cloud 9fin, 2026-04-07 | Long-run outcomes of non-pro-rata coercive LMEs; Ch 14 re-default priors. **CHECK** SSRN id before linking. |
| "Private Credit's State Backstop: How Private Equity Socializes Risk Through Insurers" | Andrew Granato, Pranjal Drall | Odd Lots, 2026-07-31 | Ch 17 insurance channel. |
| "The Credit Markets Go Dark" | Jared Ellias, Elisabeth de Fontenay | Odd Lots, 2024-09-02 | Governance cost of private credit; Ch 17. |
| "Bond Pricing: Agreeing To Disagree" | Maciej Kowara, Eric Jacobson (Morningstar) | Odd Lots, 2021-04-05 | Evaluated-price dispersion; Ch 20 NAV uncertainty. |
| "Liquidity Cascades: The Coordinated Risk of Uncoordinated Market Participants" | Newfound Research | Flirting with Models, 2020-09-20 | Liquidity-spiral narrative; Ch 18 and Ch 28. |
| "Overnight Corporate Bond Trading" | Abdi, Rossi, Wu | Microstructure Exchange, 2026-09-15 | TRACE dissemination lag; Ch 18 and Ch 22. |

A WebSearch result this session (alternativecreditinvestor.com, 2026-07-01, https://alternativecreditinvestor.com/2026/07/01/creditor-on-creditor-violence-heats-up-as-lenders-weaponise-co-ops/) attributes to a University of Oxford study the finding that more than 80% of 89 LME transactions defaulted within 36 months. **CHECK** the primary study before Ch 14 uses the figure.

### Using the feeds as data (a note for Ch 25–26 and App B)

The feeds are free, timestamped, machine-readable text. *The Credit Edge* alone gives about 195 weekly items since 2023-02-28, each naming a firm, a speaker and a directional view, often quoted. That is a small but real panel of buy-side narrative to code (bullish/bearish on private credit, CLOs, HY, distress) and test against subsequent HY OAS or BDC price-to-NAV. Omny also exposes per-episode transcript endpoints in the feed (`api.omny.fm/.../transcript?format=TextWithTimestamps`, seen in the Odd Lots RSS), which supports an NLP pipeline for Ch 25 or 26. Running it is future work. This session only established that the endpoints are listed.

---

## 8. Shelf pairings (source anchors for the resource graphs)

> [SOURCE EXTRACTION] "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes." — `Man_Revolutions_in_Credit_Trading_2023 p.2`

This pairs with the 2015 Chris White and 2021 Larry Harris *Odd Lots* episodes, which give the market-structure "before", and with Dwinells (2026) and Richardson (2026), which give the "after". The 2026 conversations are about where to *extend* systematic credit (loans, CLOs, EM) rather than whether it can execute at all. That shift is Ch 2's thesis in two dated quotes.

> [SOURCE EXTRACTION] "It was always thought that credit would follow swiftly on the tails of the equity market in developing a substantial quant investment universe." — `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.5`

The 2024 "very low single digits" and 2026 "about 1%–2%" remarks show that, as of Oct 2026, it still has not. Ch 4 should treat penetration as the slow variable and AUM growth (Blackstone's $40B aiming for $100B) as the fast one.

> [SOURCE EXTRACTION] "An investor that holds the fulcrum security which likely will receive a significant portion of the reorganized firm's equity may oppose the sale because it could diminish long-term enterprise value." — `Moyer_Distressed_Debt_Analysis p.339`

The Kirkland board-flipping episode (2026-10-01) and the 9fin co-op and DQ-list series describe how fulcrum holders now act *before* any 363 sale: by organizing, capping votes or replacing directors. Ch 13 and Ch 16 should extend Moyer's in-court game to this out-of-court stage.

---

## 9. Gaps and CHECK list

- No verified episode, on any show scanned, is primarily about **credit portfolio trading** or **credit-ETF creation/redemption**. Next session: S&P Global and Risk.net podcasts, which earlier briefs mention TITLE-ONLY.
- **Petition's** author line and the **Harvard Bankruptcy Roundtable** were not verifiable (no author on the fetched page; 403).
- The **Oxford LME default** figure (above) is from a press summary only.
- *Top Traders Unplugged* feed links point to `localhost`. Only the two TTU URLs above were verified by direct fetch.
- The *Macro Musings* Menand–Younger episode "Money and the Public Debt: Treasury Market Liquidity as a Legal Phenomenon" (2023-10-02) is in the feed, but its feed link is truncated and soft-404s. Cite it title-only.

---

## Sources (URLs verified this session, 2026-10-17)

**Publisher feeds and APIs (fetched and parsed):**
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/8a94442e-5a74-4fa2-8b8d-ae27003a8d6b/982f5071-765c-403d-969d-ae27003a8d83/podcast.rss
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/e74a35e9-c028-4e5f-a3f7-afb10164a717/8792a2e9-d66c-4038-a1fe-afb101654894/podcast.rss
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/ee4336cb-155f-4488-90e0-b1400134e40e/77e6a3a7-290d-4a82-8164-b14001353ef2/podcast.rss
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/4e4cd910-40a1-4619-a5f3-ae2b0012ffff/5873a3cb-298f-40bc-b71f-ae2b0013000d/podcast.rss
- https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/ee08231b-2e0c-40d0-afa9-ae3c0021f0dc/ab3c08b0-6606-450f-a60c-ae3c0021f0e6/podcast.rss
- https://api.omny.fm/orgs/e73c998e-6e60-432f-8610-ae210140c5b1/programs
- https://rss.libsyn.com/shows/94820/destinations/482814.xml
- https://rss.libsyn.com/shows/138806/destinations/865793.xml
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

**Episode pages:** every episode URL in §2 and §3 returned HTTP 200 on 2026-10-17 (about 150 URLs across omny.fm, capitalallocators.com, flirtingwithmodels.com, share.transistor.fm, macromusings.libsyn.com, podscripts.co, toptradersunplugged.com, man.com and isda.org). Soft-404 hosts were title-checked.

**Newsletters, research and course pages:**
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

**Surfaced by WebSearch this session (existence only):**
- https://octus.com/resources/articles/rx-101-creditor-on-creditor-violence
- https://alternativecreditinvestor.com/2026/07/01/creditor-on-creditor-violence-heats-up-as-lenders-weaponise-co-ops/
- https://www.mfdf.org/news-resources/news/2026/02/04/interesting-listen---odd-lots--podcast-highlights-private-credit-growth
- https://podscripts.co/podcasts/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-violence

**Shelf:** `Man_Revolutions_in_Credit_Trading_2023 p.2`; `Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.5`; `Moyer_Distressed_Debt_Analysis p.339`.

---

## Book placement

**Every chapter:** replace the TITLE-ONLY podcast lines in each `### Deep-Dive Resource Graph` with the dated, linked items from §2 for that chapter. The integrity rule is satisfied because every link was verified on 2026-10-17.

**By chapter:**
- **Ch 2:**
  - White 2015, Elson 2017, White 2020, Morningstar 2021, Harris 2021 and Golay 2026 form an "oral history" timeline box from voice to all-to-all.
  - Use the Man 2023 p.2 pairing.
- **Ch 3:**
  - Frumes/Indap (CA EP.209), Indap (Odd Lots 2024), Mielle, Friedman, Higgins and Derrough serve as RSSG-to-buy-side career models.
- **Ch 4:**
  - Dwinells (2026-10-08) and Richardson (2026-02-19) plus Man "Extra Credit" (Mar 2024) supply a **Trend Watch box: "Systematic share of US corporate credit: ~1–2% (Oct 2026) vs. 20–25% target"**. Log it in App C.
- **Ch 7:** Ralph Smith (bond-availability bias), Wellington, Mintz, Moallemi, Fraser-Jenkins/Brown.
- **Ch 9 / 10 / 11:**
  - Obenshain, Croce, Takahe, the TTU pair, Karoui (hedging) and Fridson.
  - TCW's "CCCs cry uncle" goes in the Ch 11 CCC section.
- **Ch 12:** Rieder, Ivascyn (two points in time), Michele, Dimensional.
- **Ch 13 (largest user):**
  - The NYDJ-to-Serta genealogy and the DQ-list, voting-cap and co-op-antitrust episodes.
  - Fox Legal (add-backs), Kirkland (board flips), Securitize-for-J.Crew and Lycra.
- **Ch 14:**
  - The Roe–Rotaru study, the Del Monte/Serta/American Tire episode and the distressed-cycle panel (Mudrick, H.I.G., Bain, Davidson Kempner, Magnetar).
  - "Claude Code shook credit" as an AI-driven sector-shock regime.
- **Ch 16:** In-Court Report on backstop fees (ConvergeOne), Hertz 2024, Sussberg, Judge Kaplan, the Judge Jones fallout.
- **Ch 17:** the Odd Lots arc, the Money Stuff OBDC/Weinstein arc, Credit Edge BDC/PIK/secondaries, the Trillions Apollo ETF episode, the Oaktree memo of Apr 9, 2026, and the three papers in §7.
- **Ch 18 / 22:**
  - Thao Tran, Liquidity Cascades, Shashidhar, Duffie, Younger (2020 basis), April 8 2025, Golay.
  - The Abdi–Rossi–Wu overnight TRACE talk.
- **Ch 20:** Balchunas (two episodes), Trillions Mar 2020, Laipply, Janus.
- **Ch 21:** the Majewski 2022/2026 pair, Bates, the CLO cluster, and the FIS loan-data "fax" episode.
- **Ch 24:** Ardagh CDS deliverability (2026-01-21) as a new case module, plus Weinstein.
- **Ch 25 / 26:** Noetica, HRT (two episodes), Man Group 86× token spend, and the feeds-as-data note in §7.
- **Ch 28:** the Paleologo pair, Morillo, Falk-Wallace, Kumar, Balyasny, Lewinsohn, Zimmerman, Barse/Third Avenue.

**New sections and chapters this research justifies:**
1. **New App D `93_appD_media_syllabus`, "The Listening & Reading Syllabus".** This dossier, kept current each edition: dated, linked and keyed to chapters, with a "start here" ten-episode path. The book promises a media ecosystem, and one curated, verified list is cheaper to maintain than 28 scattered ones.
2. **New Ch 13-B `13_ch13b_creditor_organization_coops_dq_lists`, "Creditor Organization as a State Variable: Co-ops, DQ Lists, Voting Caps, Board Flips and Antitrust."** The 2024–2026 media record (nine-plus dedicated episodes) shows that who can organize, and how fast, now decides LME outcomes as much as basket capacity does.
3. **Ch 24 new section "Deliverable-Obligation Fights in the LME Era: Ardagh 2026"**, on equitization-pending bonds and DC split votes.
4. **Ch 25 or 26 new section "Mining Market Narrative: Podcast Feeds and Transcripts as Alternative Data"**, which builds a Credit Edge sentiment panel and tests it against spreads.
5. **Ch 17 new section "The BDC Discount Trade: Tenders, NAVs and Volatility Laundering"**, anchored on Saba's OBDC II tender as discussed on Money Stuff (2026-03-19) and Capital Allocators EP.494.
6. **App C entries:**
   - Systematic share (Oct 2026), Kamenski (Mar 2024).
   - HarbourVest's PC-secondaries run-rate above $50B (May 2026).
   - Davidson Kempner's $770B stressed loans (Apr 2026), Magnetar's $600B stressed pile (Sep 2026).
   - Man Group's 86× token-spend growth (Jul 2026), Fridson's 1,000bp recession call (May 2025).
