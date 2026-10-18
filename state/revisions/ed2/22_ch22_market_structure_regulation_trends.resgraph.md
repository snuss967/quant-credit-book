# Resource graph upgrade log: 22_ch22_market_structure_regulation_trends (Edition 2, U3b)

Dossier: state/research/media_episodes_posts_parts_V_VIII.md, section 22_ch22_market_structure_regulation_trends (6 rows), plus the publisher-feed record for the Odd Lots and Money Stuff episodes (fetched this session). Chapter has one resource list: "### Deep-Dive Resource Graph" (end of chapter). No log existed at start; the "STATUS: COMPLETE" comment already at the end of the chapter file is the chapter's own marker and was left untouched.

## Deep-Dive Resource Graph, upgraded (one block rewrite plus one small follow-up Edit to drop the Money Stuff clause)

Replaced (channel-level -> specific):
- Bloomberg Odd Lots (archive pointer, title only) -> Odd Lots, "How The Crisis Nearly Blew Up One Of The World's Safest Trades" (Josh Younger, 2020-03-26), serving the basis-trade half of the March 2020 case in 22.4.3. Title, date, URL and description checked against the Omny publisher feed.
- Macro Musings (title only) -> Macro Musings, "Samim Ghamami on How to Reform the Treasury Market" (2024-08-19), dossier row, serving 22.4.
- Matt Levine, Money Stuff (newsletter, title only; TRACE, Treasury clearing, manufactured credit events) -> Money Stuff: The Podcast, "T+Lunchtime: Settlement, Musk, Hwang" (2024-05-31), serving 22.3.3 (T+1). Title, date, URL and description checked against the Money Stuff: The Podcast feed (119 items). No episode in that feed is about TRACE, Treasury clearing or manufactured credit events; the manufactured-events pointer is now a cross-reference to the Chapter 24 graph instead of a new item.

Added (6, all dossier rows for this chapter, plus one from the plumbing-thread section): 
- The SIFMA Podcast, "Preparing for US Treasury Clearing: Industry Readiness and the Done-Away Framework" (2026-07-31), 22.4.
- Macro Musings, "Anat Admati on the US Banking System and the Basel III Endgame" (2024-03-18), 22.5.1.
- SEC Commissioner Uyeda, "Remarks at the 2026 U.S. Treasury Market Conference" (2026-09-22), 22.4 timeline.
- Fed Vice Chair Bowman, "Modernizing Financial Regulation: Initial Observations from eSLR" (2026-10-01), 22.5.
- ISDA derivatiViews (O'Malia), "How Efficiency Enhances Resilience in the Financial System" (2026-10-13), 22.4-22.5.
- Microstructure Exchange webinar, Abdi, "Overnight Corporate Bond Trading" (2026-09-15), 22.2 (dossier V-VIII section 18 row, verified; same URL as in Chapter 18).

Kept unchanged: all FINRA notices and rule filings, SEC and Fed press releases and speeches, CFTC, ISDA research portal, ESMA, MarketAxess 8-K, title-only DTCC/SIFMA/ICI T+1 report and TRACE FactBook, all Academic Papers, all Data & Code.

Spares verified but left out (6-item cap): Odd Lots, "Darrell Duffie On How to Fix the World's Most Important Market" (2023-08-28, https://omny.fm/shows/odd-lots/darrell-duffie-on-how-to-fix-the-world-s-most-impo); Odd Lots, "A New Way for the Fed to Fight a Market Crisis" (Kashyap, 2024-08-28, https://omny.fm/shows/odd-lots/a-new-way-for-the-fed-to-fight-a-market-crisis); Odd Lots, "Why Treasury Market Spasms That Shouldn't Happen Keep Happening" (Yesha Yadav, 2021-04-08, https://omny.fm/shows/odd-lots/why-treasury-market-spasms-that-shouldnt-happen-ke); Macro Musings, "Ellen Correia Golay on All-to-All Trading and Treasury Market Liquidity" (2026-09-21, https://macromusings.libsyn.com/ellen-correia-golay-on).

## Verification notes (flag for the fact-check pass)
- Uyeda figures (about 165% rise in FICC daily cleared volume; "will not be extended" compliance dates) are the dossier's WebFetch reading of the SEC page; sec.gov returns 403 to curl. Check before print.
- Web calls this session: 2 (Odd Lots RSS, Money Stuff RSS). Dossier rows used as written; no titles, dates or URLs invented.
- The Younger episode URL is the Omny slug as the feed gives it (truncated slug is the feed's own).

<!-- STATUS: COMPLETE -->
