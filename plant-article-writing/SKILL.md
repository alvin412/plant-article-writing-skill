---
name: plant-article-writing
description: "Route an ambiguous plant-science writing request to literature reading, review writing, or original-research writing."
---

# Plant writing router

Use the most specific existing context to select one workflow:

- Paper reading or claim verification: `reading-literature`, with only the requested reading scope.
- Review, perspective, systematic review, or meta-analysis: `plant-review-article`.
- Original manuscript based on supplied experiments or analyses: `plant-research-article`.

An explicit article type goes directly to its focused skill. A paragraph edit stays a paragraph edit; use the full package only for a full manuscript request. Ask one clarification only if the supplied materials cannot resolve an article-type distinction that changes the work.
