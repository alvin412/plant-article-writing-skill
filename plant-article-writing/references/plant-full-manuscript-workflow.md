# Plant Full Manuscript and Review Workflow

## Contents

1. Project record
2. Stage workflow
3. Stage deliverables
4. State and version tracking
5. Drafting order
6. Final package

## 1. Project Record

Create a Paper Configuration Record containing:

- manuscript type and workflow mode
- English and Chinese working titles
- central claim or review thesis
- target journal, readership, article type, word limit, and citation style
- species, genotype, tissue, cell type, developmental stage, treatment, stress, environment, trait, pathway, and breeding context
- available data, figures, tables, protocols, source papers, Zotero collection, and existing drafts
- search date range, inclusion boundaries, output language, deadline, and missing inputs
- project version, date, and current stage

The user must confirm this record and the detailed outline before body drafting.

## 2. Stage Workflow

### Stage 0: Intake

Classify the project and detect available materials. Select the plant article archetype:

- natural variation -> mechanism -> adaptation or breeding
- genome or pangenome resource -> trait genetics
- single-cell, spatial, or multi-omics atlas -> regulatory insight
- immunity or hormone crosstalk -> molecular mechanism
- developmental or transcription-factor module -> trait output
- multi-omics prioritization -> functional gene discovery
- plant review, perspective, scoping review, or systematic review

Output: Paper Configuration Record.

### Stage 1: Outline Approval

Produce:

- 3-5 working titles
- one-sentence central argument
- scope and exclusions
- section and subsection hierarchy
- paragraph-level jobs for major sections
- expected claims, evidence types, citation slots, figures, tables, and boxes
- missing evidence and likely reviewer risks
- word allocation and drafting order

Stop and wait for explicit approval.

### Stage 2: Corpus and Search

Build:

- reproducible search record
- deduplicated source corpus
- inclusion/exclusion record
- literature matrix
- terminology ledger
- paper-level close-reading queue

Use `systematic-review-and-search.md` and `citation-and-close-reading-audit.md`.

### Stage 3: Evidence and Argument Blueprint

Map each planned paragraph to:

`paragraph job -> claim -> supporting source or result -> plant context -> boundary -> counterevidence -> significance`

Flag:

- unsupported claims
- single-source broad claims
- species/tissue/treatment mismatch
- review-only support where primary evidence is available
- contradictory evidence
- association-to-causation drift

Do not draft unsupported paragraph claims.

### Stage 4: Drafting

For original research, draft in this order when materials permit:

1. Results.
2. Methods.
3. Introduction.
4. Discussion.
5. Conclusion.
6. Abstract, title, and keywords.
7. Submission statements and figure legends.

For reviews:

1. Introduction and scope.
2. Synthesis sections in approved outline order.
3. Contradictions, evidence limitations, and translation boundaries.
4. Figures, tables, and boxes.
5. Future perspectives.
6. Abstract, title, and keywords.

Use:

`claim -> grouped evidence -> contrast/tension -> interpretation -> boundary -> next question`

### Stage 5: Integrity Gate 1

Audit from scratch:

- references and identifiers
- claim-citation alignment
- statistics and quantitative consistency
- figure/table references
- method completeness
- terminology and gene/protein typography
- originality and non-fabrication
- results-discussion separation
- required sections and declarations

Any fabricated, unverifiable, materially unsupported, or internally contradictory content is `BLOCK`.

### Stage 6: Independent Peer Review

Run the reviewer panel in `quality-gates-and-peer-review.md`. Reviewers do not rewrite the manuscript. Produce independent reports, editorial synthesis, decision, and revision roadmap.

Critical issues block finalization.

### Stage 7: Revision and Response

Create a traceability matrix for every editor and reviewer item. Revise only after deciding whether to:

- accept and revise
- partially accept
- clarify presentation
- add analysis or evidence
- acknowledge limitation
- respectfully disagree with evidence

Record exact changed section, paragraph, figure, table, or supplement location.

### Stage 8: Re-Review

Verify each response against the revised manuscript. Do not accept an author's claimed change without locating it.

Classify each item:

- `verified-resolved`
- `partially-resolved`
- `not-resolved`
- `new-risk`
- `justified-disagreement`

Major unresolved issues return to Stage 7.

### Stage 9: Integrity Gate 2

Repeat the complete Stage 5 audit from scratch. Also check that revisions did not create:

- new citation mismatches
- claim inflation
- English/Chinese divergence
- broken cross-references
- duplicated or missing sections
- unresolved response-letter claims

Only `PASS` may proceed.

### Stage 10: Submission and Figure/Data Gate

Use `submission-figures-and-data.md` to check:

- figure conclusion and panel evidence logic
- legends, statistics, sample sizes, error bars, and image integrity
- Data Availability, Code Availability, materials/protocol availability
- author contributions, funding, conflicts, ethics, acknowledgements, and AI disclosure
- target-journal requirements

### Stage 11: Three Word Files

Build the package specified in `word-deliverables.md`. Use real titles and Heading 1/2/3 styles. Keep the English and Chinese manuscripts complete and aligned.

### Stage 12: Word QA and Release

For all three files:

1. Reopen and structurally validate.
2. Audit heading hierarchy and numbering.
3. Audit tables, figures, captions, references, headers/footers, page breaks, fonts, and spacing.
4. Render every page to PNG.
5. Inspect every page at 100%.
6. Fix every defect and render again.
7. Release only the latest passing files.

## 3. Stage Deliverables

- Paper Configuration Record
- approved detailed outline
- search and screening record
- literature matrix
- terminology ledger
- bilingual close-reading notes
- claim-evidence map
- English and Chinese drafts
- Integrity Gate 1 report
- independent reviewer reports and editorial decision
- revision roadmap and response matrix
- re-review report
- Integrity Gate 2 report
- submission and figure/data checklist
- three Word files and format QA report

## 4. State and Version Tracking

Maintain a project manifest:

```text
project_id:
version:
current_stage:
approved_outline_version:
manuscript_version:
corpus_version:
review_round:
integrity_1_status:
re_review_status:
integrity_2_status:
word_qa_status:
unresolved_items:
last_updated:
```

Never overwrite the only copy of a major artifact. Keep versioned manuscript, response, and audit inputs until final release.

## 5. Drafting Quality

- One paragraph, one job.
- Start paragraphs with the scientific or synthesis claim.
- Keep claims near their supporting results or citations.
- Use reverse outlining after each completed section.
- Keep the terminology ledger authoritative.
- Weaken or remove claims that exceed evidence.
- Name contradictory evidence and alternative explanations.
- End Discussion and review sections with bounded interpretation, not promotion.

## 6. Final Package

The final package is incomplete until all three Word files exist and pass structural and visual QA. The literature file is not a simple bibliography: it must allow an auditor to move from each manuscript claim to the cited paper, source location, supporting passage, translation, support grade, and evidence boundary.
