---
name: reading-literature
description: "Read scientific papers beyond the abstract, create bilingual full-paper analytical notes, trace claims to exact source passages and figures or tables, grade citation support, synthesize field terminology and research logic from directly relevant papers in journals with a verified JIF of at least 10, propose controlled domain-knowledge updates, and optionally save verified notes into Zotero after confirmation. Use for literature close reading, evidence extraction, citation verification, high-impact literature synthesis, research-idea mapping, manuscript evidence maps, Zotero reading notes, or evidence-backed updates to scientific domain references."
---

# Reading Literature

Read `references/close-reading-and-zotero.md` before starting a close-reading or Zotero-note task. Also read `references/high-impact-domain-synthesis.md` whenever journal metrics, field terminology, research logic, research ideas, or skill-domain updates are involved.

## Core Contract

- Read all substantive available sections, not only the abstract.
- Never imply full-paper verification when only metadata, an abstract, or partial text is available.
- Separate directly demonstrated findings from author interpretation.
- Preserve species, genotype, tissue or cell type, developmental stage, treatment, environment, trait, method, and evidence boundaries.
- Treat JIF as a journal-level selection signal, not proof that a paper or claim is high quality.
- Never invent a passage, location, result, statistic, identifier, or Zotero write result.

## Workflow

1. Identify the exact paper by title, DOI or PMID, and Zotero item key when available.
2. Record the manuscript claim or section for which the paper is being read.
3. Obtain the available full text lawfully. Mark unavailable sections and access limitations.
4. Read the Introduction, Methods, Results, Discussion, substantive supplements, and relevant figures and tables.
5. Produce English and academic-Chinese analytical notes using the reference schema.
6. Locate the exact source anchor for every intended citation use.
7. Grade support as `strong`, `partial`, `background`, `contradictory`, `metadata-only`, or `not-supported`.
8. Verify the journal metric and identify directly relevant, full-text-read papers with `JIF >= 10.0` using the high-impact synthesis rules.
9. Automatically synthesize the qualifying set's field terminology, preferred academic expression patterns, reported research logic, and transferable research ideas.
10. Present a provenance-backed candidate domain update and ask whether the author wants it written into the skill's domain references.
11. Return the notes, evidence decision, terminology ledger, research-logic map, and update status to the calling article workflow.

## High-Impact Domain Synthesis Gate

Use the latest verifiable Clarivate Journal Impact Factor by default and record its edition year and source. Do not substitute CiteScore, SJR, quartile, journal reputation, or an estimated value. Mark unavailable metrics `JIF-unverified` and exclude them from the threshold set.

Apply the threshold only to the terminology and research-logic synthesis. Never discard a directly relevant seminal or methodologically decisive paper merely because its journal has `JIF < 10`.

Synthesize terminology and research thinking without copying source prose. Separate:

- established field terms and preferred usage;
- recurring academic collocations and argument patterns expressed as paraphrased guidance;
- research questions, gaps, hypotheses, causal chains, designs, controls, readouts, analyses, and limitations actually reported by the papers;
- new research ideas inferred from the combined evidence, each labelled as an inference with feasibility, novelty risk, and a decisive experiment.

Treat one or two qualifying papers as provisional. Do not label a usage pattern or research strategy as field consensus without support from at least three independent, directly relevant, full-text-read papers.

## Skill Domain Update Gate

After producing the synthesis, show a candidate update summary and ask whether to update a domain reference such as `references/domain-<topic-slug>.md`. Require explicit approval of the entries and target copy before writing.

Never silently modify the core `SKILL.md`, an installed skill, or a GitHub repository. Write approved scientific content only to a dedicated domain reference file, preserve provenance and conflicts, show the resulting diff, validate the skill, and report whether the source, installed, and repository copies remain synchronized.

## Zotero Note Gate

After the close-reading note is ready, ask whether the user wants it written to the matching Zotero item's notes. Do not write before explicit confirmation unless the current request already explicitly authorizes that exact write.

Before writing, show or verify:

- paper title and DOI or PMID;
- Zotero item key and target library or collection when available;
- whether the action creates a new child note or appends to an identified note;
- the consent scope: this paper, a named batch, or the current project.

Use a directly available Zotero note-write capability first. If direct note writing is unavailable, use the Zotero integration to locate the exact item and then use Zotero Desktop interface control to create or append the child note. Never overwrite an existing note silently.

After writing, reopen or list the item's child notes and verify the saved title and content. If writing or verification fails, stop, preserve the note as a local intermediate file, and report that Zotero was not updated. Never claim success based only on an attempted click or request.

## Copyright Boundary

Use analytical notes and short, claim-specific excerpts. Do not reproduce a complete copyrighted article. Longer extracts are allowed only when the source is user-provided, licensed for that use, or clearly open access.
