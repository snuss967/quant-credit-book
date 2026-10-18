export const meta = {
  name: 'ed2-new-chapter-finish',
  description: 'Finish newly written chapters: Sonnet fact-check, cross-reference and Pair Book ledger pass, then figures, figure check and resource graph (chapter_pipeline), then App Z solve and number-fix (appz_complete)',
  phases: [
    { title: 'Fact-check', detail: 'Sonnet: facts, quotes, cross-references, ledger', model: 'sonnet' },
    { title: 'Figures', detail: 'chapter_pipeline: figures, figcheck, resgraph', model: 'sonnet' },
    { title: 'App Z', detail: 'appz_complete: solve and fix', model: 'sonnet' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const factcheck = c => `You are a FACT-CHECKER for a newly written chapter of the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Chapter: book_src/${c.stem}.md (label ${c.tag}). Its brief: state/advisor_briefs/${c.stem}.md. Report: state/revisions/ed2/${c.stem}.factcheck.md.
FIRST: if the report ends with ${MARK}, stop and return "done". If it exists, resume after the last item it covers.
The book's hard rules: no fabricated quotes, identifiers, docket numbers, paper ids or URLs; real people and firms appear only through their sourced public record; fictional composites (the pod "Vantress Capital Management", Dov Adler, Wen Zhao, Marcus Oyelaran, Owen Achterberg, and the canon cast in state/cast_bible.md) are labeled as composites.
Check, fixing problems directly in the chapter with small Edits, and write the report as you go:
1. The brief's CHECK list (grep -n "CHECK" in the brief): resolve each against the dossiers it names or the web.
2. Every claim about real events, firms, people, dates, amounts, prices, ratings, rulings, docket entries, papers and URLs: verify against the dossiers in state/research/ (grep) first, then web search and fetch (load them via ToolSearch; at most 20 web calls, primary sources first). Fix what is wrong; hedge or remove what cannot be verified. Every quotation of a real person must be verbatim from a source you can point to; otherwise paraphrase it with attribution or remove it.
3. Cross-references: every "§N.M", "Chapter N" or "Listing" reference points at something that exists (grep -n "^#" in the target file; Appendix F anchors in book_src/95_appF_code_companion.md). Fix wrong numbers.
4. The Pair Book: for every pair (PB-nn) this chapter opens, stresses or closes, update its row in state/rv_pair_book.md (status and chapter) with one small Edit per row; other agents are editing other rows, so match the row text exactly and touch nothing else.
5. Hygiene: no code blocks in the chapter except \`\`\`text diagrams; math delimiters balanced; currency escaped as \\$; no line of --- directly before text; the last line is ${MARK}.
Never rewrite a scene beyond the fix and never remove a topic. The report lists what you checked, what you fixed, and what remains doubtful. Your FINAL action is appending a line containing exactly ${MARK} to the report. Return a 50-word summary.`
const PRE = args.pre_commit || '9ac1c379053d9d0254e9d524d9a40efdec4a2c71'
const out = await pipeline(args.chapters,
  c => agent(factcheck(c), { label: `fact:${c.tag}`, phase: 'Fact-check', model: 'sonnet' }),
  async (fc, c) => ({ fc, figs: await workflow({ scriptPath: `${ROOT}/tools/workflows/chapter_pipeline.js` }, { pre_commit: PRE, stems: [c.stem], stages: ['figures', 'figcheck', 'resgraph'] }) }),
  async (prev, c) => ({ ...prev, appz: await workflow({ scriptPath: `${ROOT}/tools/workflows/appz_complete.js` }, { chapters: [c], gates: [], do4d: false }) }))
return out.map((r, i) => ({ stem: args.chapters[i].stem, ...r }))
