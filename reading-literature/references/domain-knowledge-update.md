# Routed Domain-Knowledge Updates

Run only when the user requests knowledge or terminology accumulation, a domain-file update, or the complete three-artifact reading package. Ordinary citation checking and full-paper reading do not authorize this additional mode. An existing verified evidence record is sufficient; a new mind map or bilingual note is not a prerequisite.

## 1. Classification and Target Selection

Verify the latest available Clarivate Journal Impact Factor and record its edition year, source, and access date. Unless the author specifies another criterion, use:

- **High-level journal:** verified `JIF >= 10.0` -> `references/domain-<topic-slug>.md`.
- **Every other journal:** verified `JIF < 10.0`, unavailable JIF, or `JIF-unverified` -> `references/domain-<journal-slug>.md`.

Do not substitute CiteScore, SJR, quartile, reputation, or an estimated value for a verified JIF. Journal metrics route the file only; they do not establish paper-level evidence quality.

Define the scope before choosing a topic slug:

```text
Topic and focal object:
Plant species or crop scope:
Tissue, cell type, stage, treatment, environment, and trait:
Mechanistic, methodological, or breeding focus:
Time window and exclusions:
```

For a journal slug, use the verified canonical journal title and maintain aliases for standard abbreviations or former titles. Normalise to a stable filesystem-safe lowercase slug. Never create a second file merely because a later paper uses a journal abbreviation.

## 2. Required Domain-File Schema

Every journal- or topic-based file must contain:

1. Scope, definition, and exclusions.
2. Journal identity and aliases for a journal file, or topic identity and aliases for a topic file.
3. Routing basis, including JIF value, edition, verification source, access date, and status.
4. Verified terminology ledger.
5. Preferred academic expression guidance expressed as original guidance rather than copied prose.
6. Reported research-logic patterns and transferable design principles.
7. Clearly labelled inferred research ideas with decisive experiments.
8. Contradictions, limitations, and unresolved questions.
9. Source registry with DOI or PMID, exact source anchors, reading status, journal, and publication status.
10. Version date and update history.

## 3. Terminology Ledger

Create or update one record per concept:

```text
Canonical English term:
Accepted abbreviation:
Academic Chinese term:
Definition in this scope:
Preferred usage or collocation:
Variant or deprecated usage:
Plant context and boundary:
Source papers and exact anchors:
Independent-source count:
Status: source-specific / provisional / supported convention / disputed
Confidence:
```

Preserve alternatives and their contexts when sources disagree. Do not make a term canonical merely because it appears in one journal or one high-JIF paper.

## 4. Research Logic and Ideas

For each paper record its question, gap, hypothesis or model, experimental chain, key controls, primary readouts, analyses, decisive evidence, limitations, alternative explanations, and transferable design principle.

For cross-paper synthesis record shared assumptions, convergent strategies, complementary scales, contradictory models, missing causal links, unresolved plant contexts, and discriminating experiments.

Label every new idea as an inference:

```text
Idea ID and title:
Evidence basis and reasoning chain:
Testable hypothesis:
Minimal decisive experiment:
Controls and readouts:
Expected discriminating outcomes:
Feasibility and required resources:
Novelty-overlap risk:
Biological and translational boundary:
Priority:
```

Do not present an idea as novel until a separate novelty search has been completed.

## 5. Journal-File Rules

Use `references/domain-<journal-slug>.md` for every paper whose journal is not verified as high-level. For requested updates, merge evidence from the same canonical journal into that file. Deduplicate sources by DOI or PMID and concepts by meaning rather than spelling.

Treat terminology, expression patterns, and research strategies in a journal file as journal-scoped evidence. Do not label them field consensus. Retain each paper's exact provenance, conflicts, and access limitations. A `JIF-unverified` journal file must state that status prominently.

## 6. Topic-File Rules

Use `references/domain-<topic-slug>.md` for a paper from a verified high-level journal. Merge it into the stable topic file selected by biological or methodological scope. Do not create a paper-title-based topic file.

Treat one or two independent papers as provisional. Require at least three independent, directly relevant, full-text-read papers before describing a term, expression pattern, or research strategy as a supported field convention. Preserve seminal or decisive lower-JIF evidence in the scientific analysis, but route the current paper's required update according to its own journal classification.

## 7. Controlled Update Procedure

After verifying the source evidence needed for the requested update:

1. Resolve the canonical target path and inspect the existing file if present.
2. Deduplicate by concept and DOI or PMID.
3. Preserve earlier provenance, disagreements, and update history.
4. Merge only claims supported by exact full-text anchors; label partial-access boundaries.
5. Keep short claim-specific excerpts only when needed for verification.
6. Show the exact diff.
7. Check the updated domain file for valid source anchors, duplicate records, and preserved conflicts. Run the skill validator only if skill instructions or metadata changed.
8. Report the exact updated path; do not synchronize additional copies unless requested.

A request for this knowledge-update mode or the complete three-artifact package authorizes one domain-file update in the active skill copy. Ask only when the authoritative copy or target scope is genuinely ambiguous. Never silently update multiple divergent copies, and never change `SKILL.md` trigger metadata or workflow rules as part of a scientific content update.
