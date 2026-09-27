# High-Impact Domain Terminology and Research-Logic Synthesis

## Contents

1. Scope and JIF verification
2. Qualifying literature set
3. Terminology and expression synthesis
4. Research-logic and idea synthesis
5. Candidate domain update
6. Approval and update procedure

## 1. Scope and JIF Verification

Define the domain boundary before synthesis:

```text
Topic and focal object:
Plant species or crop scope:
Tissue, cell type, stage, treatment, stress, environment, and trait:
Mechanistic, methodological, or breeding focus:
Time window and exclusions:
```

Use the latest verifiable Clarivate Journal Impact Factor by default. Record:

```text
Journal:
JIF value:
JIF edition year:
Verification source and access date:
Metric status: verified / JIF-unverified
```

Do not infer JIF from reputation, quartile, CiteScore, SJR, or an unsourced web table. Do not treat JIF as paper-level evidence quality. If the author specifies a JIF edition, use that edition consistently.

## 2. Qualifying Literature Set

Include a paper in the high-impact synthesis only when all are true:

- it is directly relevant to the defined domain;
- its journal has a verified `JIF >= 10.0`;
- all substantive available sections have been read;
- the paper's identity, status, and source anchors are verified.

Start with the current article corpus. When fewer than three qualifying papers are available and search tools are permitted, perform a focused supplementary search for directly relevant sources. Record databases, exact queries, dates, filters, and selection reasons. Do not pad the set with tangential papers merely to reach a count.

Use other high-quality or seminal papers for scientific evidence even when their journal JIF is below 10. The threshold set is a terminology and research-strategy lens, not the complete evidence base.

## 3. Terminology and Expression Synthesis

Create one row per candidate term:

```text
Canonical English term:
Accepted abbreviation:
Academic Chinese term:
Definition in this domain:
Preferred usage or collocation:
Variant or deprecated usage:
Plant context and boundary:
Source papers and exact anchors:
Occurrence count and independent-source count:
Status: provisional / supported convention / disputed
Confidence:
```

Extract accepted terminology, technical verbs, relation words, method names, evidence-strength language, and field-specific distinctions. Convert recurring expression patterns into original guidance; do not copy distinctive sentences or create a phrase bank of copyrighted prose.

When sources disagree, preserve the alternatives and their contexts. Do not force one term into canonical status merely because it appears in a high-JIF journal.

## 4. Research-Logic and Idea Synthesis

### Reported Research Logic

For each paper record:

```text
Research question:
Knowledge gap:
Hypothesis or model:
Experimental or analytical chain:
Key controls and comparisons:
Primary readouts:
Analysis and validation logic:
Decisive evidence:
Limitations and alternative explanations:
Transferable design principle:
```

### Cross-Paper Research Map

Synthesize:

```text
Shared assumptions:
Convergent strategies:
Complementary methods or scales:
Contradictory models:
Missing causal links:
Unresolved plant contexts:
Methods that would discriminate between models:
```

### New Research Ideas

Clearly label every new idea as an inference rather than a source finding:

```text
Idea ID and concise title:
Evidence basis:
Reasoning chain:
Testable hypothesis:
Minimal decisive experiment:
Controls and readouts:
Expected discriminating outcomes:
Feasibility and required resources:
Novelty-overlap risk:
Biological and translational boundary:
Priority: high / medium / low
```

Do not present an idea as novel until a separate novelty search has been completed.

## 5. Candidate Domain Update

Generate a candidate update only from traceable synthesis. Use a direct reference file under the skill's `references/` directory:

```text
references/domain-<topic-slug>.md
```

The candidate file must contain:

1. Domain definition and exclusions.
2. Verified terminology ledger.
3. Preferred academic expression guidance.
4. Reported research-logic patterns.
5. Inferred research ideas and their status.
6. Contradictions and unresolved questions.
7. Source registry with DOI or PMID, source anchors, JIF value, edition year, verification source, and reading status.
8. Version date and update history.

Do not add full copyrighted passages. Store short claim-specific excerpts only when needed for verification.

## 6. Approval and Update Procedure

Present before writing:

```text
Domain file to create or update:
New terms:
Changed terms:
Research-logic additions:
New inferred ideas:
Conflicts retained:
Sources and JIF verification:
Entries excluded and why:
Target copy: workspace source / installed copy / repository copy
```

Ask for explicit author approval. After approval:

1. Re-read the existing domain file if present.
2. Deduplicate by concept, not spelling alone.
3. Preserve previous provenance and conflicting usages.
4. Write only the approved entries.
5. Show the exact diff.
6. Run the skill validator.
7. Report synchronization state across workspace, installed, and repository copies.

Never update the skill from an abstract-only, metadata-only, JIF-unverified, or tangential source. Never modify trigger metadata or core workflow rules as part of a scientific domain-content update unless the author requests a separate skill-design change.
