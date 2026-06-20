# Three Word Deliverables

## Contents

1. Required files
2. Heading hierarchy
3. Structured JSON input
4. Build procedure
5. Format and render QA

## 1. Required Files

For a completed full project, create exactly:

- `01_plant_manuscript_bilingual.docx`
- `02_peer_review_and_response.docx`
- `03_literature_audit_and_close_reading.docx`

Each file must begin with a visible document title, project metadata, version, and date.

## 2. Heading Hierarchy

Use real Word styles:

- Title: document title only
- Heading 1: major document division
- Heading 2: manuscript section, reviewer, or paper
- Heading 3: subsection, comment, response, close-reading section, or citation use
- Heading 4 only when essential

Do not skip from Heading 1 to Heading 3. Do not fake headings with bold body text.

### Manuscript File

```text
Title
Project Information
English Manuscript
  Title
  Abstract
  Keywords
  Introduction
  Materials and Methods
  Results
  Discussion
  Conclusion
  Declarations
  References
Academic Chinese Manuscript
  Corresponding complete section hierarchy
```

For reviews, replace original-research sections with the approved review hierarchy.

### Review and Response File

```text
Title
Editorial Synthesis
Reviewer 1
  R1.1
    Preserved comment
    Author response
    Manuscript change and location
    Re-review verification
Reviewer 2 ...
Final Re-Review Decision
Residual Risks
```

### Literature File

```text
Title
Search and Screening Record
Citation Audit Summary
Claim-Citation Matrix
Paper 1
  Metadata
  Full-Paper Close Reading
  Citation Use 1
    Manuscript claim
    Original source passage
    Academic Chinese translation
    Support grade and boundary
Paper 2 ...
Unresolved Evidence Gaps
```

## 3. Structured JSON Input

Use `scripts/build_word_package.py --init-template project.json` to create the input template. Fill it with verified project content, then run:

```text
python scripts/build_word_package.py project.json --output-dir output
```

The script must not be used to invent missing content. Remove placeholders or explicitly label unresolved fields before finalization.

## 4. Build Procedure

1. Load the `documents` skill.
2. Use the named `plant_academic_package` override below unless the target journal provides a Word template.
3. Build all three files from the same project version.
4. Reopen each file to verify that the package is structurally valid.
5. Run heading, style, table, image, accessibility, and metadata audits when available.
6. Render each file to page PNGs.
7. Inspect every page at 100%.
8. Correct defects and repeat rendering.

### Named Style Override: `plant_academic_package`

Base: `narrative_proposal`.

- Page: US Letter portrait.
- Margins: top 0.85 in, bottom 0.80 in, left/right 0.90 in.
- Header/footer distance: 0.492 in.
- Body: Times New Roman 10.5 pt; SimSun for Chinese; justified; 6 pt after; 1.15 line spacing.
- Title: Arial 22 pt bold, dark blue `#1F4E79`.
- Heading 1: Arial 15 pt bold, `#1F4E79`, 12 pt before, 5 pt after.
- Heading 2: Arial 12.5 pt bold, `#373737`, 10 pt before, 4 pt after.
- Heading 3: Arial 11 pt bold, `#505050`, 8 pt before, 3 pt after.
- Chinese headings: Microsoft YaHei fallback.
- Tables: fixed DXA geometry over the 6.70 in content width; 120 DXA indent; 80 DXA top/bottom and 120 DXA start/end cell margins; light-blue label/header fill `#D9EAF7`.
- Footer: centred page number.

Apply the same override to all three files so they read as one package.

## 5. Format and Render QA

Check every file for:

- non-empty title
- correct Heading 1/2/3 hierarchy
- no orphan heading at page bottom
- consistent fonts and scientific notation
- readable tables with repeated headers where needed
- captions kept with figures/tables
- page numbers and consistent headers/footers
- no clipping, overlap, missing glyph, broken reference, or excessive blank page
- no unresolved placeholders in a final file
- accurate English/Chinese correspondence

Write `word_package_validation.json` with file paths, structural checks, warnings, and render status. A structural pass without render inspection is not a full formatting pass.
