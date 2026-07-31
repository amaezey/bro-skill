# Before and after

A real exchange, with project identifiers swapped for generic ones. Question asked: how much of those three bugs have you fixed?

## Before

All three, fully fixed and merged in PR #21.

Highlight coordinates — fixed completely. Spans land on the right characters, all 18 mis-highlights gone, verified on all four measured documents.

PDF text extraction — fixed for every real case measured. The two starved documents went from 30% and 68% visible to 94% and 97%.

Review key — fixed completely. Re-runs inherit all agreed reviews and nothing leaves your queue silently.

Three honest edges, recorded rather than hidden:

- A document that genuinely is mostly indented code now reads as prose. Accepted on purpose, pinned by a test.
- Two small capability gaps the coordinate fix exposed are flagged needs_review in the ledger, not repaired.
- 141 old reviews no longer match a current finding. Most were judged-wrong flags that the fixes removed, but some are the same finding re-keyed, and those two groups can't be fully separated.

None of the edges undoes a fix. The 67 disputed reviews waiting on you are the only open work from these three.

## After `/bro`

All three bugs are fully fixed and merged in PR #21.

| Bug | Fixed | Proof |
|---|---|---|
| Highlight coordinates | Fully | All 18 mis-highlights gone; spans verified on all four documents |
| PDF text extraction | Fully, on every measured case | Hidden documents went 30% → 94% and 68% → 97% visible |
| Review key | Fully | 324 reviews inherit on re-run; disputed ones flagged, never dropped |

Recorded edges, none undoing a fix:

- A document that is mostly real indented code now reads as prose. Deliberate, test-pinned.
- Two small gaps the coordinate fix exposed are flagged needs_review in `fixtures.yaml`, not repaired.
- 141 old reviews match nothing current. Most were wrong flags the fixes removed; some are re-keyed survivors, and the two can't be separated.

Only open work from these three: 67 disputed reviews waiting on you.

## What changed

- Three bugs measured on the same attributes became a table. In the before they are three parallel paragraphs a reader has to hold in their head to compare.
- Proof moved into its own column, so a claim and its evidence sit side by side rather than in one run-on sentence.
- "Three honest edges, recorded rather than hidden" lost its truthfulness claim and its defensiveness. Recording an edge is the job, not a virtue to announce.
- Em dashes went, along with the padding they were joining.
- Closing line leads with what is open, rather than reassuring first and naming open work second.
- Word count roughly halved, with no fact dropped and one added: 324 inherited reviews, which the before implied but never stated.
