#!/usr/bin/env python3
"""Dependency-free validation for the additive task-17 pages.

Checks the editorial JSON, independently re-derives the inherited BOC
40-row ladder, parses the generated HTML, verifies every table row and
playbook step has an official source link, and checks local links/anchors.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal as D, getcontext
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data/bank-playbooks.json"
DEFAULT_COST_MODEL = ROOT / "data/cost-model.json"
PAGES = ("banks.html", "playbooks.html", "verification.html")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
ERRORS: list[str] = []

getcontext().prec = 34

# Hardcoded separately from data/bank-playbooks.json so a mutation is caught.
EXPECTED_FACTS = {
    "boc_commission": "0.1%; min CNY50; max CNY260",
    "boc_telegram_us": "CNY150",
    "boc_full_arrival_other_usd": "USD25",
    "abc_commission": "0.1%; min CNY20; max CNY200",
    "abc_telegram": "CNY80",
    "abc_full_arrival_usd": "USD25",
    "abc_express": "USD15 + 0.25%; min USD15; max USD50",
    "ccb_online_commission": "0.1%; min CNY20; max CNY300",
    "ccb_online_telegram": "CNY80",
    "hsbc_premier_commission": "0.1%; min CNY100; max CNY500",
    "hsbc_premier_telegram": "CNY120",
    "hsbc_full_arrival_prepay": "CNY200",
    "skyremit_fixed_fee": "CNY79",
    "skyremit_single_limit": "CNY500–CNY300,000",
    "skyremit_wallet_channel_fee": "0.8%",
    "atm_annual_cap": "CNY100,000",
    "atm_daily_cap": "CNY10,000",
    "tax_filing_threshold_usd": "USD50,000",
    "cash_no_permit_usd": "USD5,000",
    "cash_bank_permit_usd": "USD10,000",
    "rmb_cash_limit": "CNY20,000",
    "cbp_report_threshold_usd": "USD10,000",
    "fbar_threshold_usd": "USD10,000",
    "fx_gain_threshold_usd": "USD200",
    "foreign_dividend_rate": "20%",
    "eit_reduced_rate": "10%",
    "treaty_rate_cap": "10%",
}

EXPECTED_TABLE_ROWS = {
    "banks.html": {"fee-table": 8, "condition-table": 12, "task17-sources": 49},
    "playbooks.html": {"amount-table": 40, "penalty-table": 3},
    "verification.html": {"ledger-table": 28, "irregularity-table": 16, "canonical-table": 27},
}

REQUIRED_KEYS = {
    "metadata", "sources", "bank_rows", "condition_rows", "playbooks",
    "verification_rows", "irregularities", "canonical_facts", "matrix_config", "build_checks",
}


def fail(message: str) -> None:
    ERRORS.append(message)


def close(actual: D, expected: D, label: str) -> None:
    if abs(actual - expected) > D("1e-20"):
        fail(f"arithmetic {label}: {actual} != {expected}")


def money(value: D) -> str:
    return f"${value:,.2f}"


def walk_source_lists(node, path="$"):
    """Yield (path, source-id-list) for every object with a `sources` key."""
    if isinstance(node, dict):
        if "sources" in node and isinstance(node["sources"], list):
            yield path, node["sources"]
        for key, value in node.items():
            yield from walk_source_lists(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_source_lists(value, f"{path}[{index}]")


class AuditParser(HTMLParser):
    def __init__(self, filename: str):
        super().__init__(convert_charrefs=True)
        self.filename = filename
        self.stack: list[str] = []
        self.ids: list[str] = []
        self.links: list[tuple[str, dict]] = []
        self.source_links: list[tuple[str, dict]] = []
        self.tables: list[dict] = []
        self.current_table: dict | None = None
        self.details_route = 0
        self.procedure_steps: list[int] = []
        self.in_procedure = False
        self.in_procedure_li = False
        self.h1 = 0
        self.main = 0
        self.lang = False
        self.viewport = False
        self.td_missing_label = 0

    def handle_starttag(self, tag: str, attrs_list):
        attrs = dict(attrs_list)
        classes = attrs.get("class", "").split()
        if tag == "html" and attrs.get("lang") == "en":
            self.lang = True
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport = True
        if tag == "h1":
            self.h1 += 1
        if tag == "main":
            self.main += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs:
            href = attrs["href"]
            self.links.append((href, attrs))
            if "source" in classes:
                self.source_links.append((href, attrs))
                if self.current_table is not None and self.current_table["in_row"]:
                    self.current_table["row_sources"][-1].append(href)
                if self.in_procedure_li and self.procedure_steps:
                    self.procedure_steps[-1] += 1
        if tag == "details" and "route" in classes:
            self.details_route += 1
        if tag == "ol" and "procedure" in classes:
            self.in_procedure = True
        if tag == "li" and self.in_procedure:
            self.in_procedure_li = True
            self.procedure_steps.append(0)
        if tag == "td" and "data-label" not in attrs:
            self.td_missing_label += 1
        if tag == "table":
            self.current_table = {
                "id": attrs.get("id", ""),
                "rows": 0,
                "in_body": False,
                "in_row": False,
                "row_sources": [],
            }
        if tag == "tbody" and self.current_table is not None:
            self.current_table["in_body"] = True
        if tag == "tr" and self.current_table is not None and self.current_table["in_body"]:
            self.current_table["rows"] += 1
            self.current_table["in_row"] = True
            self.current_table["row_sources"].append([])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs_list):
        self.handle_starttag(tag, attrs_list)
        if tag not in VOID and self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_endtag(self, tag: str):
        if tag in VOID:
            return
        if not self.stack:
            fail(f"{self.filename}: unexpected </{tag}>")
            return
        if self.stack[-1] != tag:
            fail(f"{self.filename}: expected </{self.stack[-1]}> before </{tag}>")
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag == "li" and self.in_procedure_li:
            self.in_procedure_li = False
        if tag == "ol" and self.in_procedure:
            self.in_procedure = False
        if tag == "tr" and self.current_table is not None:
            self.current_table["in_row"] = False
        if tag == "tbody" and self.current_table is not None:
            self.current_table["in_body"] = False
        if tag == "table" and self.current_table is not None:
            self.tables.append(self.current_table)
            self.current_table = None


def ids_in_file(path: Path) -> set[str]:
    try:
        return set(re.findall(r'id="([^"]+)"', path.read_text(encoding="utf-8")))
    except (OSError, UnicodeDecodeError):
        return set()


def validate_data(data, cost_model, pages_root: Path) -> dict:
    missing = REQUIRED_KEYS - set(data)
    if missing:
        fail(f"data missing keys: {sorted(missing)}")
    sources = data.get("sources", {})
    if len(sources) != 49:
        fail(f"expected 49 sources, found {len(sources)}")
    source_urls = set()
    for sid, item in sorted(sources.items()):
        if not re.fullmatch(r"T\d{2}", sid):
            fail(f"source id {sid!r} is not Tnn")
        for key in ("publisher", "title", "url", "reading"):
            if not item.get(key):
                fail(f"source {sid} missing {key}")
        parsed = urlsplit(item.get("url", ""))
        if parsed.scheme != "https" or not parsed.netloc:
            fail(f"source {sid} is not an https URL: {item.get('url')}")
        if "verified" in item.get("reading", "").lower():
            fail(f"source {sid} reading status must not claim 'verified': {item.get('reading')}")
        if item.get("url") in source_urls:
            fail(f"duplicate source URL: {item.get('url')}")
        source_urls.add(item.get("url"))

    used = set()
    for path, refs in walk_source_lists(data):
        if not isinstance(refs, list) or not refs:
            fail(f"{path}: empty or invalid sources list")
            continue
        for sid in refs:
            if sid not in sources:
                fail(f"{path}: unknown source id {sid!r}")
            used.add(sid)
    unused = sorted(set(sources) - used)
    if unused:
        fail(f"unused source ids: {unused}")

    for key, expected in EXPECTED_FACTS.items():
        item = data.get("canonical_facts", {}).get(key)
        if not item or item.get("value") != expected:
            fail(f"canonical fact {key}: expected {expected!r}, got {item.get('value') if item else None!r}")
        for sid in item.get("sources", []) if item else []:
            if sid not in sources:
                fail(f"canonical fact {key}: unknown source {sid}")
    extra_facts = set(data.get("canonical_facts", {})) - set(EXPECTED_FACTS)
    if extra_facts:
        fail(f"unexpected canonical fact keys: {sorted(extra_facts)}")

    bank_rows = data.get("bank_rows", [])
    if len(bank_rows) != 8:
        fail(f"expected 8 bank/provider rows, found {len(bank_rows)}")
    for row in bank_rows:
        quote = row.get("current_executable_quote")
        if quote not in {"—", "Not available"} or re.search(r"\d", str(quote)):
            fail(f"{row.get('id')}: current executable quote must stay blank, got {quote!r}")
        if "verified" in row.get("status", "").lower():
            fail(f"{row.get('id')}: status must not claim 'verified'")
        for field in ("institution", "channel", "document", "commission", "telegram", "full_arrival", "status", "notes"):
            if not row.get(field):
                fail(f"{row.get('id')}: missing {field}")
    if [r.get("commission") for r in bank_rows if r.get("id") in {"B05", "B06"}] != ["Not extractable", "Not extractable"]:
        fail("CMB and ICBC commission cells must remain 'Not extractable'")

    if len(data.get("condition_rows", [])) != 12:
        fail(f"expected 12 condition rows, found {len(data.get('condition_rows', []))}")

    playbooks = data.get("playbooks", [])
    if len(playbooks) != 9:
        fail(f"expected 9 playbooks, found {len(playbooks)}")
    expected_step_count = 0
    for p in playbooks:
        steps = p.get("steps", [])
        if len(steps) < 6:
            fail(f"{p.get('id')}: expected at least 6 steps, found {len(steps)}")
        expected_step_count += len(steps)
        for index, s in enumerate(steps, 1):
            if not s.get("text") or not s.get("sources"):
                fail(f"{p.get('id')} step {index}: missing text or sources")
        if not p.get("unknowns") or not p.get("sources") or not p.get("quote_gate"):
            fail(f"{p.get('id')}: missing unknowns, source set, or quote gate")

    results = {r.get("result") for r in data.get("verification_rows", [])}
    allowed_results = {"Matches source", "No row extractable", "No text tariff row extracted", "Not independently re-derived"}
    if len(data.get("verification_rows", [])) != 28:
        fail(f"expected 28 verification rows, found {len(data.get('verification_rows', []))}")
    if results - allowed_results:
        fail(f"unexpected verification results: {sorted(results - allowed_results)}")
    for r in data.get("verification_rows", []):
        if "verified" in r.get("result", "").lower():
            fail(f"{r.get('id')}: result must not claim 'verified'")
    if len(data.get("irregularities", [])) != 16:
        fail(f"expected 16 irregularities, found {len(data.get('irregularities', []))}")
    for r in data.get("irregularities", []):
        if r.get("severity") not in {"High", "Medium", "Low"}:
            fail(f"{r.get('id')}: invalid severity {r.get('severity')!r}")

    config = data.get("matrix_config", {})
    if config.get("amount_start_usd") != 10000 or config.get("amount_step_usd") != 10000 or config.get("amount_count") != 40:
        fail(f"matrix config must be 10000/10000/40, got {config}")

    # Independent Decimal re-derivation of the inherited BOC known-cost ladder.
    rows = cost_model.get("rows", [])
    if len(rows) != 40:
        fail(f"cost model: expected 40 rows, found {len(rows)}")
    buy, sell = D("6.6648"), D("6.6929")
    mid = (buy + sell) / 2
    expected_bases = []
    for index, raw in enumerate(rows, 1):
        amount = D(index * 10000)
        if D(str(raw["amount_usd"])) != amount:
            fail(f"cost model row {index}: wrong amount ladder")
        principal = amount * sell
        commission = min(D(260), max(D(50), principal * D("0.001")))
        spread = principal * (sell - mid) / mid
        base_cny = commission + D(150) + spread
        base_usd = base_cny / sell
        expected_bases.append(base_usd)
        close(D(str(raw["principal_cny"])), principal, f"{amount} principal")
        close(D(str(raw["commission_cny"])), commission, f"{amount} commission")
        close(D(str(raw["spread_cny"])), spread, f"{amount} spread")
        close(D(str(raw["base_cny"])), base_cny, f"{amount} base CNY")
        close(D(str(raw["base_usd"])), base_usd, f"{amount} base USD")
        if D(str(raw["telecom_cny"])) != D(150):
            fail(f"cost model row {index}: telecom is not CNY150")

    # Validate generated pages.
    parsers = {}
    for filename in PAGES:
        path = pages_root / filename
        if not path.is_file():
            fail(f"missing generated page {filename}")
            continue
        parser = AuditParser(filename)
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        parsers[filename] = parser
        if parser.stack:
            fail(f"{filename}: unbalanced tags remain: {parser.stack[-5:]}")
        if not parser.lang:
            fail(f"{filename}: html lang=en missing")
        if not parser.viewport:
            fail(f"{filename}: viewport meta missing")
        if parser.h1 != 1:
            fail(f"{filename}: expected exactly one h1, found {parser.h1}")
        if parser.main != 1:
            fail(f"{filename}: expected exactly one main, found {parser.main}")
        if parser.td_missing_label:
            fail(f"{filename}: {parser.td_missing_label} td cells missing data-label")
        duplicates = [k for k, v in Counter(parser.ids).items() if v > 1]
        if duplicates:
            fail(f"{filename}: duplicate ids {duplicates}")
        for table in parser.tables:
            if not table["id"]:
                fail(f"{filename}: table without id")
            for index, row_sources in enumerate(table["row_sources"], 1):
                if not row_sources:
                    fail(f"{filename} table {table['id']} row {index}: no source link")
            if table["rows"] != len(table["row_sources"]):
                fail(f"{filename} table {table['id']}: row/source tracking mismatch")
        for table_id, expected_rows in EXPECTED_TABLE_ROWS.get(filename, {}).items():
            matches = [t for t in parser.tables if t["id"] == table_id]
            if len(matches) != 1:
                fail(f"{filename}: expected exactly one table id={table_id}, found {len(matches)}")
            elif matches[0]["rows"] != expected_rows:
                fail(f"{filename} table {table_id}: expected {expected_rows} rows, found {matches[0]['rows']}")

    # Playbook procedure citations.
    playbook_parser = parsers.get("playbooks.html")
    if playbook_parser:
        if playbook_parser.details_route != 9:
            fail(f"playbooks.html: expected 9 details.route blocks, found {playbook_parser.details_route}")
        if len(playbook_parser.procedure_steps) != expected_step_count:
            fail(f"playbooks.html: expected {expected_step_count} procedure steps, found {len(playbook_parser.procedure_steps)}")
        if any(count == 0 for count in playbook_parser.procedure_steps):
            fail("playbooks.html: at least one procedure step has no official source link")
        for p in playbooks:
            if p["id"].lower() not in playbook_parser.ids:
                fail(f"playbooks.html: missing anchor {p['id'].lower()}")

    # Canonical values must appear in the generated verification page.
    verification_path = pages_root / "verification.html"
    verification_html = verification_path.read_text(encoding="utf-8") if verification_path.is_file() else ""
    for key, value in EXPECTED_FACTS.items():
        if escape(value, quote=True) not in verification_html:
            fail(f"verification.html: canonical value {key}={value!r} missing")

    # Blank quote cells must remain blank in both the fee table and amount matrix.
    banks_html = (pages_root / "banks.html").read_text(encoding="utf-8") if (pages_root / "banks.html").is_file() else ""
    playbooks_html = (pages_root / "playbooks.html").read_text(encoding="utf-8") if (pages_root / "playbooks.html").is_file() else ""
    if banks_html.count('<td data-label="Current executable quote">—</td>') != 8:
        fail("banks.html: expected 8 blank current-executable-quote cells")
    for label in ("Other-bank current all-in cost", "Provider current all-in cost"):
        expected = f'<td data-label="{label}">—</td>'
        if playbooks_html.count(expected) != 40:
            fail(f"playbooks.html: expected 40 blank '{label}' cells, found {playbooks_html.count(expected)}")
    for index, base in enumerate(expected_bases, 1):
        amount_text = money(D(index * 10000))
        value_text = money(base.quantize(D("0.01")))
        if amount_text not in playbooks_html:
            fail(f"playbooks.html: amount {amount_text} missing")
        if f'<td data-label="BOC known baseline (USD)">{value_text}</td>' not in playbooks_html:
            fail(f"playbooks.html: BOC baseline {value_text} for {amount_text} missing")

    # Source-link hygiene and local link/anchor checks.
    all_source_hrefs = []
    for filename, parser in parsers.items():
        for href, attrs in parser.source_links:
            all_source_hrefs.append(href)
            parsed = urlsplit(href)
            if parsed.scheme != "https" or not parsed.netloc:
                fail(f"{filename}: source link is not https: {href}")
            if attrs.get("target") != "_blank" or "noopener" not in attrs.get("rel", "") or "noreferrer" not in attrs.get("rel", ""):
                fail(f"{filename}: source link missing target/rel safety: {href}")
            if not attrs.get("aria-label"):
                fail(f"{filename}: source link missing aria-label: {href}")
            if href not in source_urls:
                fail(f"{filename}: source link not in register: {href}")
    if set(all_source_hrefs) != source_urls:
        missing_urls = sorted(source_urls - set(all_source_hrefs))
        extra_urls = sorted(set(all_source_hrefs) - source_urls)
        if missing_urls:
            fail(f"source URLs never linked in generated pages: {missing_urls}")
        if extra_urls:
            fail(f"generated pages contain unregistered source URLs: {extra_urls}")

    id_cache = {filename: set(parser.ids) for filename, parser in parsers.items()}
    for filename, parser in parsers.items():
        for href, attrs in parser.links:
            if href.startswith("#"):
                target = href[1:]
                if target not in parser.ids:
                    fail(f"{filename}: broken same-page anchor {href}")
                continue
            if href.startswith("https://"):
                if not urlsplit(href).netloc:
                    fail(f"{filename}: external https link without host: {href}")
                continue
            if href.startswith("http://") or href.startswith("//"):
                fail(f"{filename}: non-https link: {href}")
            if href.startswith("mailto:") or href.startswith("tel:"):
                continue
            local_path, _, fragment = href.partition("#")
            if not local_path:
                continue
            candidate = pages_root / local_path
            if not candidate.exists():
                candidate = ROOT / local_path
            if not candidate.exists():
                fail(f"{filename}: broken local link {href}")
                continue
            if fragment:
                if candidate.suffix == ".html":
                    key = candidate.name
                    if key not in id_cache:
                        id_cache[key] = ids_in_file(candidate)
                    if fragment not in id_cache[key]:
                        fail(f"{filename}: broken local anchor {href}")

    # No global navigation link may point at a missing page.
    for href, _short, _desc in data.get("metadata", {}).get("nav", []):
        candidate = pages_root / href
        if not candidate.exists():
            candidate = ROOT / href
        if not candidate.exists():
            fail(f"nav link target missing: {href}")

    return {
        "sources": len(sources),
        "bank_rows": len(bank_rows),
        "playbooks": len(playbooks),
        "steps": expected_step_count,
        "verification_rows": len(data.get("verification_rows", [])),
        "irregularities": len(data.get("irregularities", [])),
        "canonical_facts": len(EXPECTED_FACTS),
        "tables": sum(len(p.tables) for p in parsers.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="task-17 JSON data file")
    parser.add_argument("--cost-model", type=Path, default=DEFAULT_COST_MODEL, help="inherited BOC cost-model JSON")
    parser.add_argument("--pages-root", type=Path, default=ROOT, help="directory containing generated HTML")
    args = parser.parse_args()
    try:
        data = json.loads(args.data.read_text(encoding="utf-8"))
        cost_model = json.loads(args.cost_model.read_text(encoding="utf-8"))
        result = validate_data(data, cost_model, args.pages_root)
    except Exception as exc:  # negative controls should produce a nonzero exit, not a traceback
        fail(f"fatal validation error: {type(exc).__name__}: {exc}")
        result = {}
    if ERRORS:
        print(f"FAIL: {len(ERRORS)} problem(s)", file=sys.stderr)
        for error in ERRORS:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(
        "PASS: 3 additive pages, "
        f"{result['sources']} sources, {result['bank_rows']} fee rows, "
        f"{result['playbooks']} playbooks/{result['steps']} cited steps, "
        f"{result['verification_rows']} ledger rows, {result['irregularities']} irregularities, "
        f"{result['canonical_facts']} canonical facts, 40 re-derived amount rows, "
        f"{result['tables']} sourced tables, links and anchors."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
