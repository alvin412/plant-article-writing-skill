from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any


EXPECTED_LAYERS = ["Background", "Shapes", "Icons", "Text"]
LICENSE_STATES = {
    "user-owned",
    "open-license",
    "permission-confirmed",
    "style-reference-only",
}


def load_object(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def require_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()


def validate_entry(entry: dict[str, Any], entry_path: Path) -> None:
    require_text(entry.get("asset_id"), "asset_id")
    require_text(entry.get("title"), "title")

    source = entry.get("source_paper")
    if not isinstance(source, dict):
        raise ValueError("source_paper must be an object")
    for field in ("title", "doi_or_pmid", "journal", "figure_anchor"):
        require_text(source.get(field), f"source_paper.{field}")

    license_status = require_text(entry.get("license_status"), "license_status")
    if license_status not in LICENSE_STATES:
        allowed = ", ".join(sorted(LICENSE_STATES))
        raise ValueError(f"license_status must be one of: {allowed}")

    if entry.get("reconstruction_mode") != "hybrid":
        raise ValueError("reconstruction_mode must be 'hybrid'")
    if entry.get("top_level_layers") != EXPECTED_LAYERS:
        raise ValueError(f"top_level_layers must equal {EXPECTED_LAYERS}")

    for field in ("style_profile_path", "editable_pdf_path", "preview_path"):
        rel = Path(require_text(entry.get(field), field))
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError(f"{field} must be a safe path relative to the library root")

    for field in ("topics", "biological_entities"):
        values = entry.get(field)
        if not isinstance(values, list) or not all(
            isinstance(value, str) and value.strip() for value in values
        ):
            raise ValueError(f"{field} must be a list of non-empty strings")

    editability = entry.get("editability")
    if not isinstance(editability, dict):
        raise ValueError("editability must be an object")
    required_true = (
        "live_text",
        "editable_vector_arrows",
        "svg_icons_where_practical",
    )
    for field in required_true:
        if editability.get(field) is not True:
            raise ValueError(f"editability.{field} must be true")
    if editability.get("whole_figure_embed") is not False:
        raise ValueError("editability.whole_figure_embed must be false")
    image_count = editability.get("independent_complex_image_count")
    if not isinstance(image_count, int) or isinstance(image_count, bool) or image_count < 0:
        raise ValueError(
            "editability.independent_complex_image_count must be a non-negative integer"
        )

    updated_at = require_text(entry.get("updated_at"), "updated_at")
    try:
        date.fromisoformat(updated_at)
    except ValueError as exc:
        raise ValueError("updated_at must use YYYY-MM-DD") from exc

    if entry_path.suffix.lower() != ".json":
        raise ValueError("entry manifest must be a .json file")


def validate_catalog(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    if catalog.get("schema_version") != 1:
        raise ValueError("catalog.schema_version must be 1")
    assets = catalog.get("assets")
    if not isinstance(assets, list) or not all(isinstance(item, dict) for item in assets):
        raise ValueError("catalog.assets must be a list of objects")
    seen: set[str] = set()
    for item in assets:
        asset_id = require_text(item.get("asset_id"), "catalog asset_id")
        if asset_id in seen:
            raise ValueError(f"catalog contains duplicate asset_id: {asset_id}")
        seen.add(asset_id)
    return assets


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate and upsert one mechanism-asset manifest into the library catalog."
    )
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument("--entry", required=True, type=Path)
    args = parser.parse_args()

    catalog_path = args.catalog.resolve()
    entry_path = args.entry.resolve()
    entry = load_object(entry_path)
    validate_entry(entry, entry_path)

    if catalog_path.exists():
        catalog = load_object(catalog_path)
    else:
        catalog = {"schema_version": 1, "assets": []}
    assets = validate_catalog(catalog)

    entry_record = dict(entry)
    try:
        entry_record["manifest_path"] = entry_path.relative_to(
            catalog_path.parent
        ).as_posix()
    except ValueError as exc:
        raise ValueError("entry manifest must be inside the catalog directory") from exc

    asset_id = entry_record["asset_id"]
    for index, current in enumerate(assets):
        if current.get("asset_id") == asset_id:
            assets[index] = entry_record
            action = "updated"
            break
    else:
        assets.append(entry_record)
        action = "added"

    assets.sort(key=lambda item: str(item.get("asset_id", "")).casefold())
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    with catalog_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(catalog, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"OK: {action} {asset_id}; total={len(assets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
