# Resource graph upgrade log: 23_ch23_cross_asset_convexity_and_vol_surface (Edition 2, U3b)

Dossier: state/research/media_episodes_posts_parts_V_VIII.md, section 23_ch23_cross_asset_convexity_and_vol_surface.
Dossier gap noted there: no episode on capital-structure arbitrage, convertibles, CreditGrades, Carr or jump-to-default; the dossier rows serve the Merton identity (23.1) and the bank-run cases (23.8).

## Deep-Dive Resource Graph (end of chapter, one Edit)

Replaced (channel-level -> specific):
- Bloomberg Odd Lots (archive pointer, no episode) -> "Dan Davies On What Brought Down Silicon Valley Bank" (2023-03-14); the "Credit Suisse AT1s" and "convertible bonds" claims had no verified Odd Lots episode, so the AT1 topic is served by The Credit Edge (below) and convertibles are noted as a gap.
- Flirting with Models (channel, no episode) -> "Dean Curnutt - The Reflexivity of Equity Volatility (S6E16)" (2023-09-11). The old line's "convertible-arbitrage managers" claim was not supported by any episode found; dropped with a one-line gap note.

Added (6; 5 from the dossier, 1 verified by me):
- Odd Lots, Lev Menand, "The Regulatory Blunder That Gave Us the Silicon Valley Bank Disaster" (2023-03-16) (23.8 Case B) [dossier]
- The Credit Edge, "Swiss AT1 Bond Carnage, Leisure Sector Risk" (2023-03-23) (23.8 Case C) [dossier]
- Merton, Nobel Prize Lecture (1997-12-09) (23.1) [dossier]
- Bowman, "Initial Findings from Independent Review of Silicon Valley Bank" (2026-09-18) (23.8 Case B) [dossier]
- BCBS, "Report on the 2023 banking turmoil" (2023-10-05) (23.8 Cases B and C) [dossier]
- Flirting with Models, "Kris Abdelmessih - Life Through a Volatility Lens (S7E10)" (2024-07-29) (23.4-23.5) [verified by me]
New group "Talks and Reports" created for Merton, Bowman and BCBS.

Unresolved: Matt Levine *Money Stuff* line (Practitioner Writing) is newsletter-level; the dossier has no Levine column for this chapter and the web-call budget was spent on the Flirting with Models verification, so the line was kept and annotated "No specific column is cited here." Candidate for a later pass: Levine on SVB (March 2023) and on the Credit Suisse AT1 write-down (March 2023); Bloomberg blocks scripted fetches.
Kept unchanged: BIS Quarterly Review June 2005, Fed SVB review, FDIC releases, FINMA/UBS, Cboe, Resonanz/iCapital, CreditGrades Technical Document, all academic papers, all data and code items, shelf cross-references.

## Verification notes (flag for the fact-check pass)
- Dossier items used as written (titles, dates, URLs, one-line reasons): Davies, Menand, Credit Edge, Merton, Bowman, BCBS.
- Flirting with Models: the feed's own links for the Curnutt and Obenshain episodes return 404, so the episode URLs were rebuilt from the podcastai portal handles (https://www.flirtingwithmodels.com/episodes/<handle>), the same pattern the dossier uses for the Paleologo episode. Fetched by curl: Curnutt (l8s5fwO9IGb) and Abdelmessih (EdhZsWMO5mh) both return 200 with the expected page title; a made-up handle returns 404, so a 200 means the episode exists. Dates (2023-09-11, 2024-07-29) are from the RSS item and the portal API. The "why" lines paraphrase the RSS descriptions; the Curnutt link to the ROBO loop (23.1, Exercise 1) is the editor's reading, not the episode's claim.
- Not used: Greg Obenshain, "Quantitative Credit" (S4E12, 2021-07-19; handle nQBct6plzWH), verified in the feed and API but not page-checked and a loose fit; cap of 3-6 additions.
- Web calls used: 6 (feed fetch, two failed WebFetch of feed-linked pages, one status batch, the portal API, one page-check batch). No titles, dates or URLs invented.

<!-- STATUS: COMPLETE -->
