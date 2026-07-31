#!/usr/bin/env bash
# Run every trial against a freshly built fixture.
#
# Runs on a subscription, so no dollar cap is applied: --allow-unmetered.
#
# Several cases mutate the repository they run in: fix a typo, correct an
# import. Reusing one fixture would let trial 2 find the work already done, so
# each trial gets its own copy and each condition gets its own directory.
#
#   ./scripts/run_paired.sh 3 evals/results/responses.jsonl
set -euo pipefail

CASES="${3:-evals/cases.jsonl}"
TRIALS="${1:-3}"
OUTPUT="${2:-evals/results/responses.jsonl}"
SKILL="skills/bro/SKILL.md"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p "$(dirname "$OUTPUT")"

for trial in $(seq 1 "$TRIALS"); do
  for condition in baseline candidate; do
    fixture="/tmp/bro-fixture-${condition}-${trial}"
    python3 scripts/make_fixture.py "$fixture" >/dev/null

    args=(--runner claude --cases "$CASES" --condition "$condition" --trials 1
          --trial-offset "$((trial - 1))" --cwd "$fixture"
          --allow-unmetered --output "$OUTPUT")
    if [ "$condition" = candidate ]; then
      args+=(--condition-skill "$SKILL")
    fi

    echo "trial ${trial}, ${condition}"
    env -u ANTHROPIC_API_KEY python3 scripts/run_evals.py run "${args[@]}"
    rm -rf "$fixture"
  done
done

echo "rows: $(wc -l < "$OUTPUT")"
