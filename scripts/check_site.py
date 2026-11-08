#!/usr/bin/env python3
"""Static data, link, source-citation and accessibility checks for China4.

Uses only the Python standard library so GitHub Pages CI needs no package install.
External URLs are syntax-checked and cross-checked against the source registry;
the registry records whether each source was fetched, searched, or not found.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_data  # noqa: E402

AMOUNTS = list(range(10_000, 400_001, 10_000))
EXTERNAL_SCHEMES = {"http", "https"}
IGNORED_SCHEMES = {"mailto", "tel", "data", "javascript"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicate_ids: list[str] = []
        self.links: list[str] = []
        self.external_links: list[str] = []
        self.lang: str | None = None
        self.title: str | None = None
        self.viewport = False
        self.h1 = 0
        self.main = 0
        self.skip_link = False
        self.nav_label = False
        self.scripts = 0
        self.tables: list[dict] = []
        self._table_stack: list[dict] = []
        self._in_tbody = False
        self._in_thead = False
        self._row: dict | None = None
        self._in_title = False
        self._title_parts: list[str] = []
        self._th_scope_missing = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: (v or "") for k, v in attrs}
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicate_ids.append(a["id"])
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = True
        if tag == "title":
            self._in_title = True
            self._title_parts = []
        if tag == "h1":
            self.h1 += 1
        if tag == "main":
            self.main += 1
        if tag == "a":
            href = a.get("href", "")
            if href:
                self.links.append(href)
                if urlparse(href).scheme in EXTERNAL_SCHEMES:
                    self.external_links.append(href)
                if href == "#main" and "skip" in a.get("class", "").lower():
                    self.skip_link = True
            if self._row is not None and urlparse(href).scheme in EXTERNAL_SCHEMES:
                self._row["source"] = True
        if tag == "nav" and a.get("aria-label"):
            self.nav_label = True
        if tag == "script":
            self.scripts += 1
        if tag == "table":
            self._table_stack.append({
                "require_source": "require-source" in a.get("class", ""),
                "cost_method": a.get("data-cost-table"),
                "caption": False,
                "label": bool(a.get("aria-label") or a.get("aria-labelledby")),
                "rows": [],
                "amounts": [],
            })
        if tag == "caption" and self._table_stack:
            self._table_stack[-1]["caption"] = True
        if tag == "thead":
            self._in_thead = True
        if tag == "tbody":
            self._in_tbody = True
        if tag == "tr" and self._table_stack:
            self._row = {"source": False, "amount": None}
        if tag == "th" and self._table_stack and not a.get("scope"):
            self._th_scope_missing += 1
        if tag == "td" and self._row is not None and "data-amount" in a:
            try:
                self._row["amount"] = int(a["data-amount"])
            except ValueError:
                pass

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.title = "".join(self._title_parts).strip()
        if tag == "thead":
            self._in_thead = False
        if tag == "tbody":
            self._in_tbody = False
        if tag == "tr" and self._table_stack and self._row is not None:
            table = self._table_stack[-1]
            if self._in_tbody and not self._in_thead:
                table["rows"].append(self._row)
                if self._row["amount"] is not None:
                    table["amounts"].append(self._row["amount"])
            self._row = None
        if tag == "table" and self._table_stack:
            self.tables.append(self._table_stack.pop())

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_data(errors: list[str]) -> dict:
    procedures = json.loads((ROOT / "research/procedures.json").read_text())
    registry = json.loads((ROOT / "research/sources/registry.json").read_text())
    findings = json.loads((ROOT / "research/findings.json").read_text())
    build_data.validate_inputs(procedures, registry, findings)
    rows = build_data.build_rows(procedures, registry)
    expected = len(procedures["methods"]) * len(AMOUNTS)
    if len(rows) != expected:
        fail(errors, f"cost row count {len(rows)} != {expected}")
    by_method: dict[str, list[int]] = {}
    for row in rows:
        by_method.setdefault(row["method_id"], []).append(row["amount_usd"])
        if not row["source_url"] or urlparse(row["source_url"]).scheme not in EXTERNAL_SCHEMES:
            fail(errors, f"missing official source URL: {row['method_id']} {row['amount_usd']}")
        for field in build_data.NUMERIC_COST_FIELDS:
            if row[field] is not None:
                fail(errors, f"unverified numeric cost was filled: {row['method_id']} {field}")
    for mid, amounts in by_method.items():
        if amounts != AMOUNTS:
            fail(errors, f"method {mid} does not have the exact 40-row amount grid")
    # Public CSV must match canonical rows and leave unknown numeric cells empty.
    with (ROOT / "costs.csv").open(newline="") as fh:
        csv_rows = list(csv.DictReader(fh))
    if len(csv_rows) != expected:
        fail(errors, "costs.csv row count mismatch")
    for i, (csv_row, row) in enumerate(zip(csv_rows, rows), 1):
        for field in build_data.NUMERIC_COST_FIELDS:
            if csv_row[field] != "":
                fail(errors, f"costs.csv line {i} filled unknown {field}")
        if csv_row["source_url"] != row["source_url"]:
            fail(errors, f"costs.csv line {i} source mismatch")
    canonical = json.loads((ROOT / "research/costs.json").read_text())
    if canonical["row_count"] != expected or canonical["rows"] != rows:
        fail(errors, "research/costs.json is not reproducible from current inputs")
    # Audit coverage.
    with (ROOT / "research/audit/line_audit.csv").open(newline="") as fh:
        audit = list(csv.DictReader(fh))
    if len(audit) != 1344:
        fail(errors, f"audit line count {len(audit)} != 1344 baseline lines")
    issues = json.loads((ROOT / "research/audit/issues.json").read_text())
    source_ids = {s["id"] for s in registry["sources"]}
    for issue in issues["issues"]:
        for sid in issue["sources"]:
            if sid not in source_ids:
                fail(errors, f"audit issue {issue['id']} missing source {sid}")
    return {"methods": len(procedures["methods"]), "cost_rows": expected, "audit_lines": len(audit), "sources": len(registry["sources"])}


def resolve_local(href: str, page: Path) -> tuple[Path | None, str | None]:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None, None
    path_part = unquote(parsed.path)
    target = page if not path_part else (page.parent / path_part).resolve()
    fragment = unquote(parsed.fragment) if parsed.fragment else None
    return target, fragment


def check_html(errors: list[str]) -> dict:
    pages = sorted(ROOT.glob("*.html"))
    if not pages:
        fail(errors, "no HTML pages found")
    parsers: dict[Path, PageParser] = {}
    registry = json.loads((ROOT / "research/sources/registry.json").read_text())
    registered_urls = {s["url"] for s in registry["sources"] if s.get("access") != "not_found"}
    cost_tables_seen: set[str] = set()
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
        parsers[page] = parser
        rel = page.relative_to(ROOT)
        if parser.lang != "en":
            fail(errors, f"{rel}: missing lang=en")
        if not parser.title:
            fail(errors, f"{rel}: missing title")
        if not parser.viewport:
            fail(errors, f"{rel}: missing viewport meta")
        if parser.h1 != 1:
            fail(errors, f"{rel}: expected exactly one h1, got {parser.h1}")
        if parser.main != 1:
            fail(errors, f"{rel}: expected one main landmark")
        if not parser.skip_link:
            fail(errors, f"{rel}: missing skip-to-main link")
        if not parser.nav_label:
            fail(errors, f"{rel}: nav missing aria-label")
        if parser.duplicate_ids:
            fail(errors, f"{rel}: duplicate ids {parser.duplicate_ids}")
        if parser.scripts:
            fail(errors, f"{rel}: core site must not require JavaScript")
        if parser._th_scope_missing:
            fail(errors, f"{rel}: {parser._th_scope_missing} th cells missing scope")
        for table in parser.tables:
            if not (table["caption"] or table["label"]):
                fail(errors, f"{rel}: table missing caption/aria-label")
            if table["require_source"]:
                for i, row in enumerate(table["rows"], 1):
                    if not row["source"]:
                        fail(errors, f"{rel}: source-required table row {i} lacks external source link")
            if table["cost_method"]:
                cost_tables_seen.add(table["cost_method"])
                if table["amounts"] != AMOUNTS:
                    fail(errors, f"{rel}: cost table {table['cost_method']} does not contain exact 40 amounts")
        for href in parser.links:
            parsed = urlparse(href)
            if parsed.scheme in IGNORED_SCHEMES:
                fail(errors, f"{rel}: disallowed link scheme {href}")
                continue
            if parsed.scheme in EXTERNAL_SCHEMES:
                if href not in registered_urls and "github.com" not in href and "sassnarep3-star.github.io" not in href:
                    fail(errors, f"{rel}: external source not in registry: {href}")
                continue
            target, fragment = resolve_local(href, page)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                fail(errors, f"{rel}: link escapes site root: {href}")
                continue
            if not target.exists():
                fail(errors, f"{rel}: broken local link {href}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = parsers.get(target)
                if target_parser is None:
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    target_parser.close()
                    parsers[target] = target_parser
                if fragment not in target_parser.ids:
                    fail(errors, f"{rel}: broken anchor {href}")
    expected_methods = {m["id"] for m in json.loads((ROOT / "research/procedures.json").read_text())["methods"]}
    missing = expected_methods - cost_tables_seen
    if missing:
        fail(errors, f"missing published cost tables: {sorted(missing)}")
    css = (ROOT / "style.css").read_text()
    for needle in [":focus-visible", "overflow-x", "@media", "prefers-reduced-motion"]:
        if needle not in css:
            fail(errors, f"style.css missing responsive/accessibility rule {needle}")
    return {"pages": len(pages), "cost_tables": len(cost_tables_seen)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-only", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    stats = check_data(errors)
    if not args.data_only:
        stats.update(check_html(errors))
    if errors:
        print("CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print("CHECK PASSED", json.dumps(stats, sort_keys=True))


if __name__ == "__main__":
    main()
