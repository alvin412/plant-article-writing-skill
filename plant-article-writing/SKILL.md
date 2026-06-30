---
name: plant-article-writing
description: "Route broad plant-science article requests to four focused skills: full-paper literature reading with optional confirmed Zotero notes, plant review writing, plant original-research writing, and target-journal finalization. Use when the user asks generally to write, review, verify, revise, or finalize a plant biology or crop-science article and the correct specialized workflow must be selected."
---

# Plant Article Writing Router

Route the request; do not duplicate the child workflows.

## Route

- Use `reading-literature` for full-paper reading, source-evidence extraction, claim verification, citation support grading, or saving confirmed close-reading notes to Zotero.
- Use `plant-review-article` for a narrative review, perspective, scoping review, systematic review, or meta-analysis in plant or crop science.
- Use `plant-research-article` for an original plant-science research manuscript based on user-supplied methods, data, results, figures, and analyses.
- Use `article-finalize` for final English-manuscript formatting and compliance review against a named journal's current instructions or template.

## Combined Requests

For a new full article, route first to the matching writing skill. That skill must use `reading-literature` for every substantive cited source. Use `article-finalize` only after a manuscript exists and the target journal or its instructions are known.

If the request remains ambiguous after inspecting the supplied materials, ask whether the work is a review, an original research article, literature reading, or journal finalization. Do not start substantive drafting under this router.
