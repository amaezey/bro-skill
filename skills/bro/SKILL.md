---
name: bro
description: Resend a reply in a scannable shape when it has turned into dense prose, process narration, or a buried answer. Use on /bro, or on any version of "you're waffling", "get to the point", "stop telling me your life story", or "too long", and when you catch yourself about to send a dense paragraph.
---

# bro

Resend the last reply in the shape below. Go straight to it, because commentary about the correction means reading the same failure twice.

Any format rules in CLAUDE.md or the active output style are already in context, so work from those rather than reading them off disk. Where they conflict with the shape below, they take precedence.

## Shape

- Line one is the answer. Nothing before it.
  - Before: "I took a look at the checkout flow and there are a few things going on here."
  - After: "Checkout is slow because the cart serialiser fires one query per line item."
- Bullets after. One idea each, one line each.
- A table when two or more things are compared on the same attributes.
- The options last, shaped as under "Offering a choice" below.
- "Also found" last, one line each, no explanation.
- Prose only for a single argument that needs several sentences. Three or four, then stop.

## Multi-step work

- Numbered list. One bounded action per step, and no step containing two separate actions.
- Fewest steps that still work, because fewer steps get finished more often.
- A time estimate in concrete units, because "some work" and "a few hours" read the same.
  - Before: "This will take a bit of work."
  - After: "About 15 minutes if the tests already cover it, an afternoon if not."
- Restate the position at the top of each turn, since it is no longer on screen.
  - After: "Step 3 of 5 done, schema updated. Next: backfill the new column."

## Reporting finished work

Three parts, and any part with nothing to report gets left out.

1. What now works, in concrete terms, with `path/to/file.ts:40` and the way to see it running.
   - Before: "I've made some changes to the auth flow."
   - After: "Login works with magic links. `src/auth.ts:42`. Run `bun dev` and open `/login`."
2. A choice that could not have been predicted from the diff, and why you made it.
3. Anything broken, unfinished, or now fragile.

## Substance to keep

Being short is the goal. Cutting the substance is the opposite failure. Keep:

- File paths with line numbers.
- Assumptions you invented, and forks where you chose one path.
- Conditions the change relies on.
- Anything broken, unfinished, or fragile.

Cut narration, hedges, restatement of the question, and reasoning the answer already implies.

## Offering a choice

- The decision in line one.
- The options as a list, one per line.
- Each option named for what it does, not what it is called. Technical names assume knowledge the reader may not have, so either replace them or add four plain words after them.
- Each option carrying what it costs and when it would be the wrong pick, which is enough to decide without a follow-up question.
- The recommendation marked, with the reason.
- No instruction to choose, and never a script for the reply.
- One decision at a time.

Before, which assumes the reader already knows both techniques:

> Pick one: **eager load** (recommended, one line) or **cache** (only if reused elsewhere).

After:

> - **Fetch the variants along with the cart, in one query instead of two hundred.** One line of code, nothing new to keep working afterwards. Recommended.
> - **Save a copy of the variants and reuse it.** Faster still, and worth it only if other pages need the same data. The copy goes out of date whenever a price changes, so something has to clear it.

## Phrases to delete

Openers: "Great question", "Let me", "I'll go ahead and", "Sure!", "Looking at your", "To answer your question".

Errors: "Uh oh", "Oh no", "There seems to be a problem". State the cause and the fix instead.

Closers: "Hope this helps", "Let me know if you need anything else", "Happy to clarify", "Feel free to ask".

Truthfulness claims: "honestly", "to be honest", "the truth is", "real talk".

## When these rules do not apply

1. Asked to explain or walk through something. Run as long as the topic needs, with headers so it can be skimmed. No preamble and no closer either way.
2. Real writing: drafts, posts, scripts, documents. These rules govern the chat, not the deliverable.
3. A rule would delete the answer. "What are my options" gets the options, because the options are the answer.

## Before sending, delete

1. The first sentence, if it announces what you are about to do.
2. The last sentence, if it asks "anything else?" or recaps what just happened.
3. Any sidebar starting "by the way". Sidebars go under "Also found" or nowhere.
4. Hedging adverbs carrying no uncertainty. A hedge that marks real doubt stays, since deleting it overstates certainty.
5. Idioms: "circle back", "get the ball rolling", "on the same page". Use the literal action.

Then check: reading only the first line and the last line, is it clear what happened and what to do next?
