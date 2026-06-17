# Plant Full Manuscript And Review Workflow

Use this reference when the user asks for a complete plant-science manuscript, review article, literature review, manuscript outline, manuscript revision, or citation check.

This workflow borrows four strengths from the writing-related skills:

- `academic-paper`: phase-based workflow, outline gate, literature matrix, revision loop, and citation compliance.
- `nature-writing`: argument-first drafting, section-specific jobs, and evidence-boundary discipline.
- `nature-polishing`: paragraph diagnosis before sentence polishing and claim-strength calibration.
- `nature-reader`: source-grounded bilingual close reading with stable anchors.
- `nature-academic-search`: multi-source search, deduplication, citation verification, and fallback routing when evidence is thin.

## Operating Rule

Do not fabricate references, findings, mechanisms, sample sizes, or validation. If the evidence base is insufficient, stop the draft at the affected claim, mark the gap, and search or ask for the missing source.

For a new full manuscript or review article, always produce an outline first and wait for user confirmation before drafting body sections. Existing section-polish requests do not require an outline unless the section logic is broken.

## Phase 0: Intake

Record the minimum configuration before major writing:

- paper type: original research, review, perspective, methods/resource, or revision
- target journal or style: Nature-family, generic SCI, or user-specified journal
- output language: English, Chinese, or bilingual
- citation style: numbered, author-year, journal-specific, or user-supplied
- plant context: species, cultivar/accession, tissue, cell type, developmental stage, stress/treatment, trait, pathway, gene family, omics layer, and breeding context
- evidence base: user data, supplied PDFs, Zotero folder, DOI list, existing draft, figures/tables, and required references
- constraints: word count, section order, figure/table count, deadline, and whether the user wants full paper or staged writing

Output a compact Paper Configuration Record and a proposed next step.

## Phase 1: Reading Corpus And Bilingual Notes

When source papers are read during writing, create a compact note for each paper instead of only extracting a citation.

Use this note structure:

```markdown
### [First author Year] [Short title]

- Metadata: title; authors; journal; year; DOI/PMID/URL; Zotero key if available.
- Source anchor: page/section/block ID when available; figure/table IDs when used.
- Original key claim: one or two exact-meaning English claims, paraphrased if copyright limits apply.
- Academic Chinese interpretation: formal Chinese explanation of the claim, evidence, and boundary.
- Plant context: species; tissue/cell type; genotype; developmental stage; stress/treatment; trait.
- Evidence type: review synthesis, GWAS/QTL/eQTL/TWAS, pangenome, expression, single-cell/spatial, mutant, overexpression, knockout, complementation, biochemical assay, field trial, or other.
- Useful for: Introduction / Review section / Results interpretation / Discussion / Future perspective.
- Limitations: evidence weakness, species boundary, context boundary, correlation-vs-causation issue, or missing validation.
- Citation slot: the exact manuscript claim this paper can support.
```

If a full PDF or DOI is provided and detailed reading is needed, follow the `nature-reader` pattern: build source anchors, preserve figure/table context, keep original/Chinese paired blocks for substantive claims, and answer later questions from the source anchors rather than memory.

## Phase 2: Literature Synthesis

Build a literature matrix before drafting Introduction, Discussion, or a review body.

Minimum matrix columns:

- theme or mechanism
- paper and year
- plant system
- evidence type
- central finding
- strength of evidence
- limitation or disagreement
- manuscript citation slot

For review articles, organize by synthesis logic, not chronology. Good grouping axes include mechanism, molecular scale, tissue/cell type, species, technology, evidence strength, and translation boundary.

For original research manuscripts, map each background claim and discussion interpretation to at least one verified source or the user's own result.

## Phase 3: Outline Gate

For a new full manuscript, provide:

- working title options
- one-sentence central claim
- paper type and target audience
- section-by-section outline
- key claim for each section
- required evidence, figures, tables, and citations
- missing inputs or weak evidence
- drafting order

For a review article, also provide:

- review thesis
- scope and exclusions
- review archetype: mechanism-centered, technology/resource, gene-family/pathway, crop-improvement, or multi-scale synthesis
- proposed figures, tables, and boxes
- unresolved questions and future directions

Wait for explicit user confirmation before drafting body sections.

## Phase 4: Drafting

Draft in the order that reduces hallucination risk:

1. Results or core evidence summary when user data are available.
2. Methods or resource description when reproducibility details are available.
3. Introduction after the literature matrix is sufficient.
4. Discussion after Results and citation slots are mapped.
5. Abstract, title, keywords, and conclusion last.

For review articles:

1. Write the Introduction and scope.
2. Draft major synthesis sections in outline order.
3. Add figures/tables/boxes concepts.
4. Write future perspectives.
5. Write abstract, title, and keywords last.

Every section should follow:

`claim -> evidence -> plant context -> boundary -> significance`

Use plant-specific context rather than generic academic phrasing. Name species, tissues, cell types, developmental stages, stresses, pathways, gene families, alleles, technologies, and validation types when they matter.

## Phase 5: Evidence Rescue For Introduction And Discussion

Run an evidence sufficiency check before drafting or revising Introduction and Discussion.

Trigger evidence rescue when:

- a paragraph uses generic phrases such as `many studies have shown` without specific studies
- a mechanism is asserted without a source
- a claim depends on recent progress but sources are older than 10 years and not seminal
- a discussion interpretation lacks prior-work comparison
- a review section has only one paper supporting a broad claim
- citations are from unrelated species, tissues, treatments, or methods without stating the boundary

When triggered, follow a `nature-academic-search` style workflow:

1. Query construction: include organism synonyms, gene/protein names, pathway terms, trait terms, stress/treatment terms, method terms, and key abbreviations.
2. Source routing: search high-reliability sources first, such as PubMed/PMC, CrossRef, publisher metadata, and relevant preprint databases when appropriate.
3. Parallel search: search independent databases when tools are available.
4. Deduplicate: merge by DOI first, then title and first author.
5. Rank: prefer relevance to the exact claim, recency, plant-system match, evidence strength, and journal reliability.
6. Verify: confirm DOI, title, journal, year, and publication status before citing.
7. Read: make a bilingual close-reading note for papers that will support nontrivial claims.
8. Assign: attach each verified source to a specific manuscript claim or citation slot.

Do not add unverified citations to final prose.

## Phase 6: Revision

For revision requests, produce a concise revision plan before rewriting if the draft has structural problems.

Revision checklist:

- Does each paragraph have one job?
- Does each claim have a result or citation?
- Are Results and Discussion separated?
- Are causal claims supported by perturbation, complementation, biochemical, or field evidence?
- Are candidate genes labelled as candidates unless causality is established?
- Are contradictory studies acknowledged?
- Are limitations explicit and useful?
- Are reviewer-facing risks addressed?

When reviewer comments are provided, classify each comment as major, minor, editorial, or citation-related; then revise only the affected sections unless the user asks for a full rewrite.

## Phase 7: Citation Check

Before finalization:

- Extract all in-text citations.
- Verify reference-list matches and remove citation orphans.
- Resolve DOI/PMID/title metadata when possible.
- Check year, journal, title, and author mismatches.
- Flag unsupported claims and citation overreach.
- Flag outdated sources when a recent review or primary paper is expected.
- Confirm that review claims have multiple sources or a clear reason for relying on one source.

Report statuses as:

`verified`, `metadata_mismatch`, `missing_reference`, `uncited_reference`, `weak_support`, `manual_needed`.

## Expected Outputs

Use only the outputs needed for the current request:

- Paper Configuration Record
- detailed outline
- bilingual close-reading notes
- literature matrix
- evidence map
- polished English manuscript text
- academic Chinese rendering
- revision plan and revised text
- citation audit report
- missing-evidence list

Keep final manuscript prose clean. Put workflow artifacts before or after the manuscript text, not inside it.
