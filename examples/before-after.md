# Before and after

A real exchange. Question asked: how much of those three bugs have you fixed?

## Before

All three, fully fixed and merged in PR #174.

runAll coordinates — fixed completely. Spans land on the right characters, all 18 mis-highlights gone, verified on all four measured documents.

PDF indent — fixed for every real case measured. The two starved documents went from 30% and 68% visible to 94% and 97%.

Verdict key — fixed completely. Re-runs inherit all agreed verdicts and nothing leaves your adjudication queue silently.

Three honest edges, recorded rather than hidden:

- A document that genuinely is mostly indented code now reads as prose. Accepted on purpose, pinned by a test.
- Two small capability gaps the coordinate fix exposed are flagged needs_review in the ledger, not repaired.
- 141 old verdicts no longer match a current finding. Most were judged-wrong flags that the fixes removed, but some are the same finding re-keyed, and those two groups can't be fully separated.

None of the edges undoes a fix. The 67 disagreed verdicts waiting on your adjudication are the only open work from these three.

## After `/bro`

All three bugs are fully fixed and merged in PR #174.

| Bug | Fixed | Proof |
|---|---|---|
| runAll coordinates | Fully | All 18 mis-highlights gone; spans verified on all four documents |
| PDF indent | Fully, on every measured case | Hidden documents went 30% → 94% and 68% → 97% visible |
| Verdict key | Fully | 324 verdicts inherit on re-run; disputed ones flagged, never dropped |

Recorded edges, none undoing a fix:

- A document that is mostly real indented code now reads as prose. Deliberate, test-pinned.
- Two small gaps the coordinate fix exposed are flagged needs_review in `u1-fixture-ledger.yaml`, not repaired.
- 141 old verdicts match nothing current. Most were wrong flags the fixes removed; some are re-keyed survivors, and the two can't be separated.

Only open work from these three: 67 disagreed verdicts waiting on your adjudication.

## What changed

- Three bugs measured on the same attributes became a table. In the before they are three parallel paragraphs a reader has to hold in their head to compare.
- Proof moved into its own column, so a claim and its evidence sit side by side rather than in one run-on sentence.
- "Three honest edges, recorded rather than hidden" lost its truthfulness claim and its defensiveness. Recording an edge is the job, not a virtue to announce.
- Em dashes went, along with the padding they were joining.
- Closing line leads with what is open, rather than reassuring first and naming the open work second.
- Word count roughly halved, with no fact dropped and one added: the 324 inherited verdicts, which the before implied but never stated.
