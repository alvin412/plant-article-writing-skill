# Quality Gates and Plant Peer Review

## Contents

1. Gate model
2. Integrity audit
3. Reviewer panel
4. Editorial synthesis
5. Revision traceability
6. Re-review

## 1. Gate Model

Use:

- `PASS`: no blocking defect.
- `WARN`: non-blocking limitation is disclosed.
- `BLOCK`: stop progression until corrected or explicitly removed from the deliverable.

The following always block:

- fabricated or nonexistent citation
- unverifiable result, sample size, method, statistic, mechanism, or novelty claim
- materially wrong citation-to-claim relationship
- causal language unsupported by the evidence
- missing core Methods needed for reproducibility
- inconsistent key results across text, table, figure, abstract, or language version
- unresolved critical reviewer issue
- a final Word file that fails structural or visual QA

## 2. Integrity Audit

Audit five layers independently:

1. **Bibliographic integrity**
   - DOI/PMID/title/authors/journal/year/status
   - duplicates, orphans, missing references, correction or retraction notices

2. **Claim integrity**
   - exact claim supported
   - model/species/tissue/treatment/trait match
   - support strength and scope
   - primary versus review source

3. **Data and statistical integrity**
   - values agree across text, figures, tables, and supplement
   - sample size, biological/technical replicates, tests, multiple testing, effect direction, and uncertainty are reported
   - no result is invented from a visual impression

4. **Method and reproducibility integrity**
   - biological materials, growth conditions, treatments, sampling, assays, software, versions, thresholds, and analysis choices are sufficient

5. **Narrative integrity**
   - Abstract, Results, Discussion, Conclusion, figures, and Chinese version make the same bounded claim
   - limitations and alternatives are not hidden
   - distinctive source wording, self-plagiarism, unexplained text reuse, and repetitive AI-like phrasing are flagged for revision

Record each finding with ID, severity, location, evidence, required action, owner, and status.

## 3. Reviewer Panel

Use independent reports. Do not let one reviewer copy another.

### Editor

Assess:

- journal fit and article type
- novelty and field significance
- likely plant-science readership
- manuscript coherence and presentation
- desk-reject risks

### Plant Domain Reviewer

Assess:

- biological accuracy
- pathway, gene-family, stress, development, or crop context
- literature coverage and competing models
- species and tissue boundaries
- mechanistic and agronomic interpretation

### Methods and Statistics Reviewer

Assess:

- design, controls, replication, randomization, normalization
- model assumptions and statistical validity
- reproducibility and data reporting
- whether methods support the stated inference

### Genetics, Omics, or Breeding Reviewer

Invoke when relevant. Assess:

- population structure, mapping model, thresholds, LD, PVE, validation
- batch effects, annotation, trajectory/network inference, spatial resolution
- candidate prioritization and causal validation
- field performance, genotype dependence, and breeding translation

### Devil's Advocate

Identify:

- strongest alternative explanation
- confirmation bias and cherry-picking
- unsupported novelty or causal language
- missing decisive control
- contradictory evidence
- the strongest reason for rejection

## 4. Report Contract

Each issue must contain:

```text
Issue ID:
Severity: Critical / Major / Minor / Editorial
Location:
Problem:
Evidence or rationale:
Required action:
Verification criterion:
```

The editorial synthesis must distinguish consensus from disagreement and issue one posture:

- proceed to minor revision
- major revision required
- major restructuring required
- not ready for submission

Do not claim to make a real editor's decision.

## 5. Revision Traceability

Use one row per comment:

```text
ID | Preserved comment | Decision | Author response | Manuscript change |
Location | Evidence added | Verification | Status
```

Allowed status:

- `open`
- `revised-awaiting-verification`
- `verified-resolved`
- `partially-resolved`
- `justified-disagreement`
- `not-resolved`

Never state that a change was made unless it exists in the revised manuscript.

## 6. Re-Review

Check every item against:

- revised manuscript
- response text
- new analysis, figure, table, citation, or limitation
- exact stated location

Then inspect the revised manuscript for new risks introduced by the changes. Re-review is not a rubber stamp.
