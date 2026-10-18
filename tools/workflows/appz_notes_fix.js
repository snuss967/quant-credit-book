export const meta = {
  name: 'ed2-appz-notes-fix',
  description: 'Resolve the App Z "NOTE (for the editor)" discrepancies: Sonnet recomputes each, fixes the chapter text minimally, aligns the App Z solution, logs the ruling',
  phases: [{ title: 'Fix', detail: 'Sonnet, one agent per chapter, two lanes', model: 'sonnet' }],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const prompt = stem => `You are a NUMBERS EDITOR for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Chapter: book_src/${stem}.md. Its worked solutions: state/appZ/${stem}.md. Log: state/revisions/ed2/${stem}.appz_fix.md.
FIRST: if the log ends with ${MARK}, stop and return "done". If it exists, skip the notes it already rules on.
While solving the exercises, the App Z author left paragraphs starting "NOTE (for the editor):" in the solutions file wherever the chapter's own text, check value, hint, listing output, or figure caption disagrees with a careful computation. Run grep -n "NOTE (for the editor)" state/appZ/${stem}.md and handle each in order:
1. Read the note, the exercise in the chapter, and the section it cites (grep -n, then sed -n the range). If it concerns an Appendix F listing, read it in book_src/95_appF_code_companion.md.
2. Recompute the disputed number yourself in python3 (throwaway scripts under /tmp only). Decide which is right. Most notes are right, but not all: rule on the evidence.
3. If the chapter is wrong or misleading: make the SMALLEST edit that makes it right (a number, a clause, a caption, a check value), in the chapter's voice; touch nothing else. If a figure script (tools/figures/*.py) prints the wrong number into a figure, fix the script and re-run it. If the fix is a sourced fact you cannot verify from files in the repo (a price, a date, a court figure), soften the claim to what the sources in state/research/ support instead of inventing a number.
4. Then make the solution agree with the fixed chapter: edit the App Z solution's text if it quoted the old value, and DELETE the NOTE paragraph from state/appZ/${stem}.md. If you rule the note wrong, delete it too and keep the solution correct.
5. Append to the log: the note in one line, your recomputation, the ruling (fixed / note wrong / softened), and the exact old → new text.
Never rewrite prose beyond the fix, never change a story beat, and never remove a topic. Pandoc math: $...$ inline. Escape currency as \\$.
Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 30-word summary: notes handled, fixed, ruled wrong.`
const lane = async stems => { const out = []; for (const s of stems) out.push({ s, r: await agent(prompt(s), { label: `zfix:${s.slice(0, 6)}`, phase: 'Fix', model: 'sonnet' }) }); return out }
return await parallel(args.lanes.map(l => () => lane(l)))
