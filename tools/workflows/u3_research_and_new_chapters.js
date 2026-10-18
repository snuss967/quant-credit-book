export const meta = {
  name: 'ed2-u3-research-and-new-chapters',
  description: 'Edition 2 U3: Sonnet research on specific episodes/posts, other investors\' public perspectives and quant-shop life; optionally Fable briefs + Opus writers for 01_ch01b and 04_ch04c',
  phases: [
    { title: 'Research', detail: 'Sonnet dossiers', model: 'sonnet' },
    { title: 'Brief', detail: 'Fable brief per new chapter', model: 'fable' },
    { title: 'Write', detail: 'lean Opus writer per new chapter' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const VOICE = `VOICE (Edition 2 user directives; these outrank older guidance and the reviews): read "## 8. Edition 2 Voice Amendments" in state/style_bible.md and state/user_directives_ed2.md, and follow them. Teach the way an engaging novel teaches: lead with scenes and real credit events, build intuition before formulas, and be less prescriptive (fewer bare statements and imperatives; more "here is what happened, and here is the idea that would have helped"; more judgment about when a tool applies and when it breaks). Put a "> **Math, Gently.**" box at the first use of each mathematical concept, building blocks included. Add "> **View From Another Seat.**" boxes where another kind of investor or dealer would see the situation differently (name real firms only for publicly stated views, with a citation). Include a labeled fictional quant-shop-life vignette, and the boring parts are welcome. Remove no topics.
CODE: chapters carry no code. Where a listing belongs, first build up to it: explain in prose what problem it solves at this point in the story, what it computes, why it is built that way, its inputs and outputs, when to use it and when not, and the edge case that bites. Then put a line containing exactly <!-- EXPLAINED --> and the fenced python listing immediately after. The orchestrator moves listings to Appendix F mechanically and leaves a link.`
const DURABILITY = `DURABILITY (non-negotiable; usage limits can kill you at any moment and anything not on disk is lost):
- If your output file already exists, READ IT FIRST. If it ends with ${MARK}, report and stop. If not, continue from where it stops without rewriting.
- Otherwise create the file within your first few tool calls (title plus section headings), then append facts and sections as you find and draft them. Never hold more than ~10 sourced facts or ~1,500 words only in context.
- Your FINAL action is appending a line containing exactly ${MARK}.`
const RULES = {
  media: `A SPECIFIC-ITEMS MEDIA dossier. For EACH chapter or primer in scope, list 4–8 specific items: podcast EPISODES (show, episode title, date, guests, URL), blog posts and essays (author, title, date, URL), and talks or lectures (title, venue, date, URL), each with one line on why it is worth the reader's time and which section it serves. Never list a channel, a show, or a blog's homepage on its own. Verify that each item exists by fetching its own page; leave out anything you cannot verify (you may list it under "Unverified leads" at the end). Never invent episode numbers, dates, or URLs. Start from state/research/media_podcasts_credit_quant.md and state/research/map_media_eco.md: refine them into specific items rather than duplicating them. Format: one "## <file stem>" section per chapter, each with a table | type | item | date | URL | why / section |.`,
  perspectives: `A PERSPECTIVES dossier. For EACH firm in scope: its seat (what it buys or trades, holding period, where it sits in the capital structure, how it sources risk, how it is funded); its publicly stated views on credit, with short exact quotes (≤40 words, verbatim) from shareholder letters, investor-day or earnings-call transcripts, memos, interviews, podcasts, or reputable press, each with speaker, date, and URL (if you paraphrase, say so); its role in named real credit events (lender, LMT participant or excluded lender, DIP provider, plan sponsor, dealer, liquidity provider), sourced; and a short "how this seat would look at the same bond as our desk" paragraph. Never invent quotes or attribute views without a source. End with a comparison table of the seats (horizon, capital, edge, constraints, what makes them buy, what makes them sell).`,
  life: `A QUANT-SHOP LIFE dossier: public, citable accounts of what daily work looks like at market makers, multi-strategy pods, systematic asset managers, bank credit-trading desks, and distressed funds. Sources: memoirs and books (with page references where you can find them), interviews, podcasts, firm engineering and research blogs, careers pages, conference talks, and regulatory documents that describe processes (best execution, SR 11-7 model risk, the FINRA TRACE rules). For each source, extract the concrete mundane details: hours, meetings, the morning P&L explain, risk limits, data cleaning, deployment, model review, compliance, reconciliation, vendor feeds, on-call. Then write 15 or more VIGNETTE SEEDS: shop type, the scene, the mundane task, the concept it can teach, and the sources it rests on. Never put invented words in a real person's mouth.`,
}
const SCHEMA = { type: 'object', properties: { path: { type: 'string' }, summary: { type: 'string' }, complete: { type: 'boolean' } }, required: ['path', 'summary', 'complete'] }
const research = it => `You are a RESEARCHER for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; the TOC is in SYSTEM_PROMPT.md section 3; reader: a restructuring banker moving to a systematic credit desk). Work from ${ROOT}. Today is ${args.today}.
Item: **${it.title}**
Scope: ${it.scope}
Research with web search and web fetch (load them via ToolSearch). Search is shared and rate-limited, so prefer fetching known primary pages directly. Record a source for every fact. Run ls state/research first and build on existing dossiers rather than duplicating them.
Write state/research/${it.kind}_${it.slug}.md (3,000–7,000 words). ${RULES[it.kind]}
End with "Sources" (URLs verified this session) and "Book placement" (which chapters should use which items).
${DURABILITY}
Do not modify other files. Return the structured summary.`

async function withRetry(fn, label) {
  const r = await fn()
  if (r) return r
  log(`${label} failed once; retrying`)
  return await fn()
}
const done = await pipeline(args.items, it => withRetry(() => agent(research(it), { label: `${it.kind}:${it.slug}`, phase: 'Research', model: 'sonnet', schema: SCHEMA }), it.slug))
log(`${done.filter(Boolean).length}/${args.items.length} dossiers`)
if (!args.chapters || !args.chapters.length) return { done }

const briefP = c => `You are a FABLE ADVISOR for a new Edition 2 chapter of the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a PJT RSSG restructuring banker moving to a systematic credit desk). Work from ${ROOT}.
New file: book_src/${c.stem}.md: "${c.title}". Output: state/advisor_briefs/${c.stem}.md.
FIRST: if the output exists and ends with ${MARK}, stop and return "exists".
Read: state/user_directives_ed2.md (this chapter is the user's own request; its scope is there and under "Edition 2 additions" in SYSTEM_PROMPT.md: grep -n "${c.stem}"); "## 8. Edition 2 Voice Amendments" and the cast section of state/style_bible.md; these dossiers: ${c.dossiers.join(', ')} (read the ones that exist); and state/reviews/ed2/synthesis.md if it exists (grep for related items). Grep book_src/ headings (state/digests/book_outline.md) for cross-references. No web research. At most about 20 tool calls.
Scope: ${c.scope}
Write 1,500–2,500 words: the thesis and the "aha"; a numbered section outline built as a sequence of scenes (each with its setting, the mundane or dramatic task, what goes wrong, and what the reader learns); the real, sourced facts and public perspectives to use in each scene (with dossier paths, and CHECK on shaky ones); where to put Math, Gently and View From Another Seat boxes; humor beats with the canon cast; three figure ideas; and cross-references into existing chapters. Fictional composites must be labeled as such; real people and firms appear only through their sourced public record.
DURABILITY: write in two passes. Your FINAL action is appending a line containing exactly ${MARK}. Return a 60-word summary.`
const writeP = c => `You are a WRITER for Edition 2 of the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Your file: book_src/${c.stem}.md, new chapter: "${c.title}". Its Fable brief is state/advisor_briefs/${c.stem}.md.
FIRST check the file on disk: if it ends with ${MARK}, stop. If it is partial, resume it by appending only. If it is missing, create it. If the brief is missing or lacks ${MARK}, stop and return "no brief".
Read only: state/style_bible.md (all of it: voice, canon cast, notation, and §8), state/user_directives_ed2.md, the brief, and the dossiers the brief names (grep and sed only what you need). Grep book_src/ for cross-references. Web: at most 5 calls, only for facts the brief marks CHECK; if you cannot verify a fact, write around it.
${VOICE}
Write 8,000–12,000 words, built as scenes: rigorous where it teaches, honest about the boring parts, and genuinely funny, with every joke riding on a correct idea. Label fictional composites as such. Include a Desk Debrief, exercises WITH brief solutions, and a \`### Deep-Dive Resource Graph\` of specific, verified items (episodes, posts, papers, books). Add "Used in / builds on" cross-references.
Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Never put a line of --- directly before text. Write in 3–5 large passes. Do not run builds or code.
DURABILITY: append each pass immediately. Your FINAL action is appending a line containing exactly ${MARK}. Return a 60-word summary.`
const written = await pipeline(args.chapters,
  c => agent(briefP(c), { label: `brief:${c.stem}`, phase: 'Brief', model: 'fable', effort: 'high' }).then(r => ({ c, brief: r })),
  x => agent(writeP(x.c), { label: `write:${x.c.stem}`, phase: 'Write' }).then(r => ({ stem: x.c.stem, brief: x.brief, write: r })))
return { done, written }
