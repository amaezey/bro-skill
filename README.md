# bro

A Claude Code skill that resends a drifted reply in a scannable shape: answer on line one, detail in bullets, comparisons in a table, choices you can pick in a word.

## Install

```bash
git clone https://github.com/amaezey/bro-skill.git
cp -r bro-skill/skills/bro ~/.claude/skills/
```

Restart Claude Code.

## Use

Type `/bro`. It also fires on "you're waffling", "get to the point", "stop telling me your life story", and "too long".

## What it enforces

- The answer on line one, nothing in front of it.
- Bullets after, one idea and one line each.
- A table when two or more things are compared on the same attributes.
- Options at the end as a list, each named for what it does rather than what it is called, carrying its cost and the case where it would be wrong, with the recommendation marked.
- Numbered steps, time estimates in concrete units, and a restated position for multi-step work.
- A named list of openers, closers, and error phrases that never survive.
- A delete pass before sending: the announcing first sentence, the recap, the sidebar, the empty hedge, the idiom.

Short is the goal, thin is the opposite failure. File paths, invented assumptions, forks taken, and anything fragile stay in.

## Overrides

The shape gives way for explain requests, real writing such as drafts and documents, and any rule that would delete the answer itself. Format rules in your `CLAUDE.md` or active output style win where they conflict.

## Credit

The pre-send delete pass, the paired examples, and the break-the-rules section are adapted from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), MIT.

## Licence

MIT.
