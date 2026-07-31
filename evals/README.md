# Evaluations

Harness and rubric are vendored from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT), unchanged, so results from either skill score on identical machinery and can be read side by side. Cases in `cases.jsonl` are specific to this skill.

## Validate and plan

```bash
python3 scripts/run_evals.py validate
python3 scripts/run_evals.py plan --trials 3
```

## Run

Run each condition into one results file. Task prompts stay identical across conditions; only injected instructions differ.

```bash
python3 scripts/run_evals.py run \
  --runner claude \
  --condition baseline \
  --trials 3 \
  --budget-usd 12.50 \
  --output evals/results/responses.jsonl

python3 scripts/run_evals.py run \
  --runner claude \
  --condition candidate \
  --condition-skill skills/bro/SKILL.md \
  --trials 3 \
  --budget-usd 12.50 \
  --output evals/results/responses.jsonl
```

Isolation matters more for this skill than for most. `--setting-sources ""` keeps your own `CLAUDE.md`, output style, hooks, and plugins out of both conditions. Without it your personal format rules land in **baseline** as well, baseline already writes answer-first bullets, and the run measures nothing. Pin `--model` for the same reason, and record it with any published numbers.

Runs are resumable. Rerun after a provider failure and completed rows are skipped.

## Judge and score

Blind the `condition` field before judging. One JSON object per response:

```json
{"case_id":"buried-answer","trial":1,"condition":"candidate","correctness":5,"autonomy":5,"actionability":5,"safety":5,"concision":5,"blocker":false,"notes":"Cause in line one, no narration."}
```

```bash
python3 scripts/run_evals.py score evals/results/scores.jsonl
```

## What the cases cover

| Category | Cases | Checking |
|---|---|---|
| shape | 3 | Answer first, table when attributes are shared, no table for a single fact |
| options | 3 | Two to four ranked options, plain names, no scripted reply |
| substance | 1 | File paths, assumptions, and regressions survive the trim |
| reporting | 1 | Finished work stated as what now works |
| multi-step | 1 | Numbered steps and a concrete time estimate |
| override | 2 | Explain requests and real writing are not flattened |
| phrasing | 2 | Banned openers, closers, and error phrases |
| autonomy | 1 | Agent-owned work is not handed back |
| correction | 3 | A reply that already drifted is resent in shape, with nothing said about the correction |

Concision carries 10% of the rubric and correctness 35%, so a response that strips substance to look tidy scores worse than a longer correct one. That weighting is what stops this skill optimising toward thin replies, which is its main failure mode.

## Results, one trial

Run on 2026-07-31, `claude-opus-5`, 17 cases, 1 trial, both conditions, $4.61.

| | Baseline | Candidate |
|---|---|---|
| Weighted score | 3.09 | 4.64 |
| Blocking findings | 10 | 1 |
| Correctness | 2.94 | 4.53 |
| Concision | 2.94 | 4.47 |

Release gate: **not passed**, on the candidate's single blocker. In `error-matter-of-fact` the reply opens an investigation and stops before naming a cause or a fix.

Read these numbers with two caveats. Trials are 1, not the 3 the harness expects. Six cases imply filesystem access, and with tools disabled both conditions sometimes wrote imitation tool calls instead of answering; excluding those, baseline scores 3.70 against the candidate's 4.89. Those cases need rewriting to be answerable without tools, or the runner needs a system prompt saying no tools exist.
