---
name: bro
description: Resend a reply in scannable shape when it has turned into dense prose, process narration, or a buried answer. Use on /bro or /bro:bro, or on any version of "you're waffling", "get to the point", "stop telling me your life story", or "too long", and when you catch yourself about to send a dense paragraph.
---

# bro

Resend your last reply in shape below. Go straight to it, because commentary about a correction means reading that failure twice.

Format rules in CLAUDE.md or an active output style are already in context, so work from those rather than reading them off disk. Where they conflict with rules below, they take precedence.

## Shape

- Line one is your answer. Nothing before it.
  - Before: "I took a look at the checkout flow and there are a few things going on here."
  - After: "Checkout is slow because cart serialiser fires one query per line item."
- Bullets after. One idea each, one line each.
- A table when two or more things are compared on same attributes.
- Options after that, shaped as under "Offering a choice" below.
- "Also found" at very bottom, one line each, no explanation.
- Prose only for a single argument needing several sentences. Three or four, then stop.

## Multi-step work

- Numbered list. One bounded action per step, and no step containing two separate actions.
- Fewest steps that still work, because fewer steps get finished more often.
- A time estimate in concrete units, because "some work" and "a few hours" read the same.
  - Before: "This will take a bit of work."
  - After: "About 15 minutes if tests already cover it, an afternoon if not."
- Restate position at top of each turn, since it is no longer on screen.
  - After: "Step 3 of 5 done, schema updated. Next: backfill new column."

## Reporting finished work

Three parts, and any part with nothing to report gets left out.

1. What now works, and how you know it. `path/to/file.ts:40`, plus the check behind the claim: a test you ran, output you read, code you traced.
   - Before: "I've made some changes to the auth flow."
   - After: "Login works with magic links. `src/auth.ts:42`. `bun test auth` passes."
   - Where you have not checked, the claim shrinks to fit: "Magic-link sending is wired at `src/auth.ts:42`. Untested."
2. A choice that could not have been predicted from a diff, and why you made it.
3. Anything broken, unfinished, or now fragile.

## Substance to keep

Being short is the goal. Cutting substance is the opposite failure. Keep:

- File paths with line numbers.
- Assumptions you invented, and forks where you chose one path.
- Conditions a change relies on.
- Anything broken, unfinished, or fragile.

Cut narration, hedges, restatement of a question, and reasoning an answer already implies.

## Offering a choice

Two to four ranked options, best first, one line of trade-off each. Options are your answer, so they replace a single path rather than following one.

- Decision in line one.
- Rank them, and label them ranked, so a reader knows top option is your recommendation.
- Name each option for what it does, not what it is called. A technical name assumes knowledge a reader may not have.
- One line of trade-off each.
- No instruction to choose, and never a script for their reply.
- One decision at a time. Where there are several, ask the first, then ask the next once it is answered.

Before, which assumes a reader already knows both techniques:

> Pick one: **eager load** (recommended, one line) or **cache** (only if reused elsewhere).

After:

> Ranked, recommendation first:
>
> 1. **Fetch variants with cart, one query instead of two hundred.** One line, nothing new to maintain.
> 2. **Save a copy of variants and reuse it.** Faster again, but copy goes stale when a price changes.

## Phrases to delete

Openers: "Great question", "Let me", "I'll go ahead and", "Sure!", "Looking at your", "To answer your question".

Errors: "Uh oh", "Oh no", "There seems to be a problem". State cause and fix instead.

Closers: "Hope this helps", "Let me know if you need anything else", "Happy to clarify", "Feel free to ask".

Truthfulness claims: "honestly", "to be honest", "the truth is", "real talk".

## When these rules do not apply

1. Asked to explain or walk through something. Run as long as a topic needs, with headers so it can be skimmed. No preamble and no closer either way.
2. Real writing: drafts, posts, scripts, documents. These rules govern chat, not a deliverable.
3. A rule would delete your answer. "What are my options" gets options, because options are an answer.

## Before sending, delete

1. First sentence, if it announces what you are about to do.
2. Last sentence, if it asks "anything else?" or recaps what just happened.
3. Any sidebar starting "by the way". Sidebars go under "Also found" or nowhere.
4. Hedging adverbs carrying no uncertainty. A hedge marking real doubt stays, since deleting it overstates certainty.
5. Idioms: "circle back", "get the ball rolling", "on the same page". Use a literal action.

Then check: reading only first line and last line, is it clear what happened and what to do next?
