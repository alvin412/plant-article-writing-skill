# Stable review issue ledger

Required record fields:
`issue_id`, `review_perspective`, `severity`, `blocking`, `claim_pointer`, `evidence_pointer`, `certainty`, `concern`, `why_it_matters`, `resolution_test`, `author_decision`, `change_location`, `recheck_status`.

Use `CRITICAL` for a demonstrated central-claim or integrity failure that prevents the stated conclusion; `MAJOR` for an important evidentiary, conceptual or reproducibility weakness; `MINOR` for a bounded correctable presentation issue. Independently mark whether the major/critical issue blocks **the particular claim**, not the entire scientific project.

Certainty values: `CONFIRMED` (with demonstrable source), `POTENTIAL` (clear rationale but unresolved), `NOT_ASSESSABLE` (missing input). A missing evidence pointer must never be invented.

Issue example (schematic only):
```json
{"issue_id":"R2-M01","review_perspective":"methods-statistics","severity":"MAJOR","blocking":true,"claim_pointer":"Results 2, sentence 4","evidence_pointer":"Figure 2 legend / source data absent","certainty":"NOT_ASSESSABLE","concern":"Independent experimental unit not defined","why_it_matters":"Potential pseudoreplication","resolution_test":"Provide randomized unit and nesting; align statistical model","author_decision":"pending","change_location":null,"recheck_status":"OPEN"}
```

Reviewer and editor reports should avoid demeaning language. Scores are optional, cannot replace specific evidence, and do not predict acceptance. Both real and simulated reviews must be unmistakably labeled.