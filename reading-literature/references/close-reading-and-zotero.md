# Close Reading, Claim Verification, and Zotero Notes

## 1. Source Record

Record:

```text
Citation key:
Title and authors:
Journal and year:
JIF value, edition year, and verification source:
DOI / PMID / PMCID / URL:
Zotero item key:
Article type and publication status:
Access state: full-text / partial-reading / abstract-only / metadata-only
Correction, retraction, or expression-of-concern status:
Plant context:
Intended manuscript claim or section:
```

## 2. Full-Paper Reading Record

For each substantive section capture:

```text
Section:
Source anchors:
English analytical note:
Academic Chinese note:
Key evidence:
Methods and controls:
Figures and tables:
Plant context and conditions:
Evidence strength:
Limitations and alternative explanations:
Potential manuscript uses:
Field terminology candidates:
Reported research logic:
Inferred research ideas:
```

For Results, follow the evidence chain from design and controls to quantitative result and figure or table. For Discussion, distinguish demonstrated findings from interpretation, extrapolation, and speculation. Include relevant supplementary evidence.

If full text is incomplete, label the record `partial-reading` and list which sections were unavailable. An abstract-only or metadata-only record cannot establish a nontrivial manuscript claim.

## 3. Claim-Citation Audit

Use one record per citation occurrence:

```text
Claim ID:
Manuscript sentence and location:
Cited source:
Claim type:
Exact source anchor:
Short original excerpt:
Academic Chinese translation:
Matched entities and conditions:
Support grade:
Scope mismatch or boundary:
Audit decision: PASS / WARN / BLOCK
```

Grades:

- `strong`: directly tests and supports the relationship in a matching context.
- `partial`: supports only part of the statement or a narrower or different context.
- `background`: supports general context but not the specific assertion.
- `contradictory`: challenges or limits the statement.
- `metadata-only`: relevance is inferred only from title or metadata.
- `not-supported`: the paper does not support the statement.

`metadata-only` and `not-supported` cannot remain as final evidence. If no exact support can be located, block the claim until it is revised or a suitable source is found.

## 4. Zotero Child Note

Use a non-destructive child note attached to the exact bibliographic item. Suggested title:

```text
Codex full-paper close reading | YYYY-MM-DD | project or claim ID
```

Suggested note body:

```text
Purpose and manuscript use
Bibliographic identity
Reading completeness and access state
English analytical summary
学术中文分析摘要
Methods and controls
Key results with source anchors
Relevant figures and tables
Claim-support decisions
Limitations and alternative explanations
Unresolved checks
High-impact terminology and research-logic synthesis
Skill domain update status
```

Preserve existing notes. Append only when the user identifies the destination note and authorizes appending. Otherwise create a new dated child note.

Use this fallback order:

1. Direct Zotero note-write tool, when callable.
2. Zotero item lookup plus Zotero Desktop interface control.
3. Local note saved under the current project's `intermediate_files/literature_notes/` folder, explicitly marked `NOT_SYNCED_TO_ZOTERO`.

Verification requires locating the saved child note after the write and checking its parent item, title, and substantive content.
