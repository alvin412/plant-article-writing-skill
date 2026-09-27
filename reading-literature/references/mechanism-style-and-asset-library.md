# Optional scientific illustration learning and asset collection

Run only when the user asks to learn a figure's style, collect reusable assets, or reconstruct a named scientific subject. A literature-reading request, high JIF, or attractive mechanism figure does not activate this workflow. No journal-metric lookup is required.

## Scope and source record

Identify the requested figure or subject and record paper identity, DOI/PMID, figure anchor, source URL or Zotero key, access date, and rights state. For style analysis alone, return an original description of palette, line language, hierarchy, abstraction, labels, and relation grammar; do not build assets automatically.

Use licensed, user-owned, or newly reconstructed generic scientific assets. Do not crop copyrighted artwork into the reusable library or copy distinctive panels. Unknown rights allow factual/style analysis, not reuse of protected expression. Preserve scientific context and do not infer evidence from a visual model alone.

## Optional reconstruction

When editable assets are requested, use the available tool appropriate to the chosen output. Figma is optional; load its applicable skill only if using it. Native SVG, Illustrator, or PowerPoint construction is appropriate when it satisfies the requested editability. Keep labels editable, arrows and semantic subjects independent, and distinguish vector geometry from retained raster images. Never represent a flattened complete figure as editable artwork.

Reconstruct generic structure with new geometry and record provenance. Verify the rendered appearance and actual editability before admitting an asset. Do not activate a paid vector service merely because it is installed.

## Library location and records

The library belongs to this skill at `assets/mechanism-figure-library/`. Its existing `catalog.json` uses `schema_version` and `assets`; preserve those keys and existing entries. Store incomplete or rights-unclear material under `_intake/`, excluded from the catalog.

Store each admitted subject once under `<category>/<asset-id>/`, with `manifest.json`, an editable asset, a PNG preview, and a provenance note. Use a stable identifier such as `generic--chloroplast-v01`. Choose a descriptive scientific category and retrieval tags without duplicating files across categories.

Each manifest records `asset_id`, `category`, subject, species/context, source identity and anchor, rights, reconstruction decisions, relative editable/preview/provenance paths, editability limits, QA status, and update date. Every file path must resolve inside the asset package. Upsert catalog entries by `asset_id`, preserve unrelated records, then reopen the JSON and verify all referenced files. If a record already exists, update its package rather than adding a duplicate.

## Delivery

Deliver only the requested style analysis or asset package and identify any library update. Report unresolved rights or editability limits honestly. A failed optional asset operation does not invalidate an otherwise completed literature-reading task.
