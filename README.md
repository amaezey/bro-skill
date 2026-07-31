# bro

A Claude Code skill that resends a reply in scannable shape: answer on line one, detail in bullets, comparisons in a table, ranked options at bottom.

## Install

```bash
git clone https://github.com/amaezey/bro-skill.git
cp -r bro-skill/skills/bro ~/.claude/skills/
```

Restart Claude Code.

## Use

Type `/bro`. It also fires on "you're waffling", "get to the point", "stop telling me your life story", and "too long".

A real before and after sits in [examples/before-after.md](examples/before-after.md).

## What it enforces

- Answer on line one, nothing in front of it.
- Bullets after, one idea and one line each.
- A table when two or more things are compared on same attributes.
- Two to four ranked options at bottom, best first, one line of trade-off each, named for what they do rather than what they are called.
- Numbered steps, time estimates in concrete units, and a restated position for multi-step work.
- A list of openers, closers, and error phrases to delete.
- A delete pass before sending: announcing first sentence, recap, sidebar, empty hedge, idiom.

Being short is the goal. Cutting substance is the opposite failure, so file paths, invented assumptions, forks taken, and anything fragile stay in.

## Overrides

Rules stand down for explain requests, real writing such as drafts and documents, and any rule that would delete an answer itself. Format rules in your `CLAUDE.md` or active output style take precedence where they conflict.

## Evaluations

17 cases with a weighted rubric, in [evals/](evals/). Concision carries 10% and correctness 35%, so a reply that strips substance to look tidy scores worse than a longer correct one.

```bash
python3 scripts/run_evals.py validate
```

## Credit

Built on [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), MIT:

- Eval harness, rubric, and runner config are vendored unchanged, so results from both skills score on identical machinery.
- Pre-send delete pass, paired examples, ranked options, and break-the-rules section are adapted into the skill.

## Licence

MIT.
