# bro

A Claude Code skill that snaps a reply back into a scannable shape.

Assistants drift. Twenty tool calls into a session, the answer you asked for arrives as a five sentence paragraph that opens with what the model tried first and buries the result somewhere in the middle. `/bro` resends that reply with the answer on line one, the detail in bullets, comparisons in a table, and the choices at the end as things you can pick in a word.

## Install

Copy the skill into your skills directory:

```bash
git clone https://github.com/amaezey/bro-skill.git
cp -r bro-skill/skills/bro ~/.claude/skills/
```

Restart Claude Code, or run `/reload-skills` if your setup has it.

## Use

Type `/bro`.

It also fires on its own when you say any version of "you're waffling", "get to the point", "stop telling me your life story", or "too long", so you can swear at it in your own words.

## What it enforces

- The answer on line one, with nothing in front of it.
- Bullets after, one idea and one line each.
- A table when two or more things are compared on the same attributes.
- Closing choices written to be picked rather than composed, with the recommendation marked.
- Numbered steps, concrete time estimates, and a restated position for multi-step work.
- A named list of openers, closers, and error phrases that never survive.
- A delete pass before sending: the announcing first sentence, the recap, the sidebar, the empty hedge, the idiom.

It also guards the other direction. Short is the goal, thin is the opposite failure, so file paths, invented assumptions, forks taken, and anything fragile stay in the reply no matter how tight it gets.

## Where it gets out of the way

Three cases override the shape: a request to explain or walk through something, real writing such as drafts and documents, and any rule that would delete the answer itself. Asked for options, you get the options.

## Deferring to your own rules

Format rules already in your `CLAUDE.md` or active output style win where they conflict. The skill is a reset toward scannability, not a replacement for how you have already told Claude to write.

## Credit

The pre-send delete pass, the paired bad and good examples, and the break-the-rules section are adapted from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), MIT licensed. That skill shapes output for a reader with ADHD and is worth reading in its own right.

## Licence

MIT.
