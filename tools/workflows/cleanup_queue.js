export const meta = {
  name: 'ed2-cleanup-queue',
  description: 'Work the open items in state/cleanup_queue.md: Sonnet fixers grouped by file (so no two agents edit the same chapter), each followed by a Sonnet reviewer who checks the fixes against the diff',
  phases: [
    { title: 'Fix', detail: 'Sonnet: one agent per file group', model: 'sonnet' },
    { title: 'Review', detail: 'Sonnet: check each fix in the diff', model: 'sonnet' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const ITEM_SCHEMA = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, status: { type: 'string', enum: ['fixed', 'already-fixed', 'softened', 'deferred'] }, note: { type: 'string' } }, required: ['key', 'status', 'note'] } } }, required: ['items'] }
const fixer = g => `You are a CLEANUP EDITOR for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Your group: ${g.name}. Log: state/revisions/ed2/cleanup_${g.name}.md.
FIRST: if the log ends with ${MARK}, read it and return its item statuses. If it exists, skip the items it already rules on.
Your items come from state/cleanup_queue.md; read the full text of each there (grep -n for the key phrase). Only touch the files your items name: other agents are editing other chapters at the same time.
${g.items.map((it, i) => `${i + 1}. [${it.key}] ${it.text}`).join('\n')}
For each item:
- Check first whether a later pass already fixed it (grep the current text). If so, log "already-fixed" with the evidence.
- Otherwise make the SMALLEST correct fix, in the chapter's voice. Recompute numbers in python3 (throwaway scripts under /tmp). For facts about the real world, use the dossiers in state/research/ first, then web search and fetch (load them via ToolSearch; at most 6 web calls for the group). If a fact cannot be verified, soften the claim to what the sources support; never invent a number, quote, date or URL. Figures: follow tools/figures/style.py and open each PNG before embedding.
- If the item needs the owner's decision or a larger rewrite than a fix, log "deferred" with the reason and change nothing.
- Log: the item key, what you found, the exact old → new text (or the files written), and the status.
Never change a story beat, never remove a topic, and never rewrite prose beyond the fix. Pandoc math: $...$ inline. Escape currency as \\$.
Your FINAL action is appending a line containing exactly ${MARK} to the log. Return the structured item statuses.`
const reviewer = (g, r) => `You are a REVIEWER of cleanup fixes in the book in ${ROOT}. Work from ${ROOT}.
Group: ${g.name}. The fixer's log: state/revisions/ed2/cleanup_${g.name}.md. Its reported statuses: ${JSON.stringify(r && r.items || [])}.
Output: append a section "## Review" to the log, then ${MARK} on its own line (if the log already contains "## Review", stop and return "done").
For each item marked fixed or softened: read the changed text in the file (grep for the new text; git diff -U2 on the file shows uncommitted changes, and git log -p -3 -- <file> recent ones). Check that (a) the fix is right (recompute numbers in python3 where there are any), (b) nothing else in the paragraph was damaged (math delimiters, currency escapes, cross-references, the story), and (c) the same wrong value does not survive elsewhere in the book (grep book_src/ for the old value or phrase; fix any stragglers with one small Edit each). For items marked already-fixed, confirm with one grep. If a fix is wrong, correct it with a small Edit and say so.
Return a 40-word summary: items confirmed, corrected, stragglers fixed.`
const out = await pipeline(args.groups,
  g => agent(fixer(g), { label: `fix:${g.name}`, phase: 'Fix', model: 'sonnet', schema: ITEM_SCHEMA }),
  (r, g) => agent(reviewer(g, r), { label: `review:${g.name}`, phase: 'Review', model: 'sonnet' }).then(v => ({ group: g.name, items: r && r.items, review: v })))
return out
