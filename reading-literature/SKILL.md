---
name: reading-literature
description: "Verify a scientific claim, closely read a paper, or audit its research map. Knowledge and asset accumulation are separate opt-in modes."
---

# Reading Literature

## Choose the requested mode first

| Request | Mode and output | References to read |
|---|---|---|
| Check whether a paper supports a sentence, verify a citation, extract a result, or explain one figure | Targeted evidence check: answer with the support verdict, exact source anchors, relevant methods and limits; use a small table for a batch | `references/claim-verification.md` |
| Closely read or analyse an entire paper | Full-paper reading: a complete bilingual analytical note and a verified research-mind-map PNG by default; honour a requested note-only, map-only, or single-language output | `references/close-reading-and-zotero.md`; `references/research-mind-map.md` only when producing or auditing a map |
| Update domain knowledge, terminology, or an explicitly requested complete three-artifact reading package | Evidence check or full reading as needed, plus one controlled domain-file update | `references/domain-knowledge-update.md` |
| Learn illustration style, collect or reconstruct reusable scientific assets | Visual-asset collection for the specified paper, figure, or batch | `references/mechanism-style-and-asset-library.md` |

Select the narrowest sufficient mode from the request and existing context without another confirmation. Calling this skill from a manuscript citation audit means targeted evidence checking. Do not automatically add other modes, extra languages, journal-metric lookups, library writes, or Figma work. Read each relevant reference once per task unless it changes.

## Evidence contract

- Never invent source passages, results, statistics, identities, figure interpretations, citations, or write/verification results.
- Read the source sections necessary to resolve the claim, including relevant methods, controls, legends, and supplements. Expand reading when ambiguity or contradictory evidence requires it.
- Full-paper mode reads all substantive available sections. Clearly distinguish full-text, partial-reading, abstract-only, and metadata-only access; never promote partial access into full-paper verification.
- Preserve species, genotype, tissue, developmental stage, treatment, environment, methods, and generalisation boundaries.
- Separate direct results, author interpretation/model, inference, contradictions, and unsupported statements. Grade citation support as `strong`, `partial`, `background`, `contradictory`, `metadata-only`, or `not-supported`.
- Reuse previously verified evidence records when the source version, anchors, and claim scope still match. Recheck changed or unresolved claims; a new use of the same paper does not require recreating its reading artifacts.
- Journal prestige and impact factor do not determine the strength of scientific evidence. Retrieve JIF only for an explicit metric request or the selected knowledge-file routing convention.

## Full-paper workflow

1. Identify the paper, its publication status, intended use, and available source material.
2. Read the available substantive sections, figures, tables, and supplements; build a source-anchored evidence ledger and conflict register.
3. When a map is requested or included by default, render and visually verify it using `references/research-mind-map.md`. A supplied map is audited against source evidence.
4. Write the complete English analytical note followed by the complete academic-Chinese note unless another language scope was requested. Keep the analytical content original and evidence-bound.
5. Save the requested outputs under `deliverables/`; keep extraction data, JSON, ledgers, and rendered QA intermediates under `intermediate_files/`.
6. Run knowledge-file updates or asset collection only when the user requested those modes. A request for the complete three-artifact package includes the PNG, bilingual note, and one domain update; it does not include visual-asset collection.

## Output and Zotero scope

Targeted checks may finish in chat and do not require files. Full-paper mode retains stable filenames such as `01_<paper-slug>_research_mind_map.png` and `02_Codex_full-paper_close_reading_<YYYY-MM-DD>_<project-or-claim-ID>_bilingual.md`. There is no fixed artifact count outside an explicitly requested package.

Write to Zotero only when the current request authorizes the exact paper or defined batch. Use the available Zotero skill, preserve existing notes, and verify the parent, title, and substantive content after a write. Use the most direct reliable write capability, with desktop UI control as a fallback. If synchronization fails, preserve the local result and report `NOT_SYNCED_TO_ZOTERO`. Existing authorization remains valid; do not ask again.

## Copyright

Use original analytical notes and short claim-specific excerpts within applicable rights. Open access alone does not establish permission to reproduce a complete article. Preserve attribution and source provenance.
