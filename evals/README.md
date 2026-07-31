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

## Results

Run 2026-08-01, `claude-opus-5`, 3 trials, both conditions, tools enabled against a rebuilt fixture repo.

Two sets, because the rules are used two ways. `cases.jsonl` injects them as a standing style governing original work. `cases-correction.jsonl` hands over a reply that already drifted plus a trigger phrase, which is the only shape `/bro` itself ever sees.

| | Standing style | | Correction | |
|---|---|---|---|---|
| | Baseline | Candidate | Baseline | Candidate |
| Weighted score | 4.19 | 4.67 | 3.83 | **4.81** |
| Blocking findings | 5 | 1 | 8 | **1** |
| Correctness | 4.49 | 4.53 | 3.64 | 4.75 |
| Actionability | 3.63 | 4.86 | 3.64 | 4.86 |
| Concision | 3.33 | 4.78 | 3.75 | 4.83 |
| Safety | 4.90 | 4.71 | 4.58 | 4.97 |

Release gate fails on both sets, for one blocker each. See `TODO.md` for the two fixes.

Known defects:

- Over-application. One trial in three turned a requested blog draft into bullets.
- `c-jargon-options` is the only case where the candidate loses. It ranked and shortened the options without translating the jargon the user said they did not understand.
- On the standing-style set, safety drops 0.19 on one case: told a feature works, the candidate reports it working where baseline reads the file and refuses. Partly addressed by requiring the check behind a claim.

