# App Z fix log: Ch 28 PM Playbook (numbers editor)

Notes found in state/appZ/28_ch28_pm_playbook.md: 1.

## Note 1 (Z.28.2, Kaz's 93%, re-audited): "a Beta recovery of mean 0.6"
- Note: read literally, "Beta recovery of mean 0.6" is 60% recovery (mean loss 0.4), but the bond's base case (L = 0.6, 40% recovery) and Listing 28.3's `kelly_random_loss(0.045, 0.031, 3.0, 2.0, 1.00)` use a Beta *loss* of mean 0.6; the exercise also gives no shape and the answer depends on it.
- Recomputation (python3, /tmp/claude-0/ed28/k.py; c = 4.5%, lambda_P = 1.5%, L = L_max U, L_max = 1, numerical Kelly on E[ln(1 - fL)]):
  - Q leg: lambda_Q = 0.045/0.6 = 7.5%, f* = 1/0.6 - 0.075/0.045 = 0. P leg: f* = 1.6667 - 0.3333 = 1.3333 (1.307 with sigma = 5%). Both match the solution.
  - Mean-loss-0.6 Betas: g'(1) = c - lambda a/(b-1), and a = 1.5b, so g'(1) >= 0 iff b >= 2. Beta(3,2) f* = 1.0000 (g'(1) = 0.045 - 0.045 = 0 exactly); Beta(6,4) 1.0000; Beta(4.5,3) 1.0000; Beta(1.8,1.2) 0.962; Beta(1.5,1) 0.948; Beta(1.2,0.8) 0.931. So the solution's "b >= 2 pins f* at 1.0, Beta(1.5,1) gives 0.95" is correct.
  - Literal reading (mean loss 0.4): Beta(2,3) loss also gives 1.0000 (g'(1) = 0.03 > 0), but a mean-0.4 loss with b < 2 (e.g. Beta(1,1.5)) would sit inside the cliff, so the shape matters either way. Listing 28.3 itself (lambda = 3.1%) gives f_loose 0.812 < f_tight 0.935 < f_const 0.978, consistent with its asserts.
- Ruling: FIXED. The note is right. The exercise's "recovery" contradicts the same bond's L = 0.6 and the listing's mean-0.6 loss, and omits the shape that decides the answer. The chapter's own sentence (section 28.4, "Recovery is not a constant either") already defines L = L_max U, so U is a loss fraction.
- Edit (book_src/28_ch28_pm_playbook.md, Exercise 2, one clause):
  - OLD: set $L_{\max} = 1$ with a Beta recovery of mean 0.6 and recompute.
  - NEW: set $L_{\max} = 1$ with a $\text{Beta}(3, 2)$ loss of mean 0.6, as in Listing 28.3, and recompute.
- Solution: Z.28.2 already says "$U \sim \text{Beta}(3, 2)$, Listing 28.3's shape with mean loss 0.6", so its text agrees with the fixed exercise and needed no edit. The NOTE paragraph was deleted from state/appZ/28_ch28_pm_playbook.md. The merged copy in book_src/99_appZb_solutions_parts_v_to_viii.md carries the same solution text without a NOTE; no change needed.
- Left alone (outside scope): the duplicate of this note in state/appZ/_editor_notes.md (aggregate file), and the generated files under output/. Chapter prose and the listing (which is not wrong: it uses lambda = 3.1%, not the exercise's 1.5%) are unchanged.

Summary: 1 note handled, 1 fixed, 0 ruled wrong, 0 softened.

<!-- STATUS: COMPLETE -->
