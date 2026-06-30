---
name: article-finalize
description: "Finalize an existing scientific manuscript against a specified journal's current author instructions, article type, reference style, template, nomenclature, typography, language, figures, tables, declarations, and submission requirements. Use when the user asks for target-journal formatting, reference reformatting, final gene and protein name checks, English language finalization, or a submission-readiness audit. Output an English-only finalized manuscript and a bilingual compliance report; do not regenerate peer-review responses."
---

# Article Finalize

Read `references/journal-finalization-checklist.md` before editing or auditing a manuscript.

## Required Inputs

Obtain:

- the exact manuscript version to finalize;
- target journal and article type;
- current official author instructions, template, and reference style, or authorization to retrieve them;
- figures, tables, supplements, declarations, and reference data needed for the submission package.

If the journal, article type, authoritative instructions, or manuscript version is uncertain, stop and ask. Do not guess a journal rule.

## Workflow

1. Freeze and identify the input manuscript version.
2. Build a requirement matrix from official journal sources and the supplied template.
3. Verify bibliography metadata before applying the journal's reference style.
4. Apply required section order, length, headings, title page, abstract form, keywords, references, figures, tables, legends, declarations, line numbering, anonymization, and file conventions.
5. Audit gene, allele, mutant, genotype, transcript, construct, and protein typography using the journal and organism-specific nomenclature rules.
6. Polish the English language without changing verified scientific meaning or claim strength.
7. Record every material format or language change and every unresolved item.
8. Reopen the outputs, render every page, inspect visually, correct defects, and re-render.

Use the available `docx` skill for Word editing and render-inspect-revise QA. Use `reading-literature` only when resolving a substantive citation-support problem rather than a formatting issue.

## Required Final Files

Create under `deliverables/`:

1. `01_journal_formatted_manuscript_en.docx` — English manuscript only.
2. `02_journal_compliance_audit_bilingual.docx` — complete English and academic-Chinese audit report.

Do not regenerate a peer-review or point-by-point response file.

Place downloaded instructions, templates, extracted requirements, reference exports, terminology ledgers, working copies, validation reports, and rendered page images under `intermediate_files/`.

If any blocking requirement cannot be verified or satisfied, keep the deliverables clearly marked as not submission-ready and list the exact blocker. Never claim full journal compliance without current authoritative instructions and completed visual QA.
