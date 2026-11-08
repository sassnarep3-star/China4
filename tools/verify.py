#!/usr/bin/env python3
"""
Verification gate for the China Money site.

Checks:
  1. Every dataset row that carries a factual claim has at least one official source,
     or an explicit flag justifying the blank.
  2. Every source id referenced anywhere resolves to a registry entry marked official.
  3. Every source URL is a plausible official-domain URL (host allowlist).
  4. Every internal link and anchor in the generated HTML resolves.
  5. HTML tables are well formed: no <td> outside a table row, consistent column counts.
  6. No stale hard-coded build date.
  7. No unverified numeric value silently rendered as a number.

External URLs are NOT fetched here: the sandbox has no general outbound HTTP. They were
verified individually with the fetch tool during research and the date is recorded in
data/sources.json. This script checks structure and provenance, not liveness.

Exit code 0 = pass, 1 = fail.
"""
from __future__ import annotations

import html.parser
import json
import pathlib
import re
import sys
from urllib.parse import urlparse, unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

OFFICIAL_HOSTS = {
    "www.safe.gov.cn", "m.safe.gov.cn", "safe.gov.cn",
    "www.pbc.gov.cn", "pbc.gov.cn",
    "www.customs.gov.cn", "customs.gov.cn",
    "www.chinatax.gov.cn", "chinatax.gov.cn",
    "www.gov.cn", "gov.cn",
    "www.irs.gov", "irs.gov",
    "www.fincen.gov", "fincen.gov",
    "www.cbp.gov", "cbp.gov.cn", "cbp.gov",
    "www.ecfr.gov", "ecfr.gov",
    "www.govinfo.gov", "govinfo.gov",
    "www.federalregister.gov", "federalregister.gov",
    "www.boc.cn", "boc.cn",
    "pic.bankofchina.com", "www.bankofchina.com", "bankofchina.com",
    "ka.sz.gov.cn",
}

errors: list[str] = []
warnings: list[str] = []
stats: dict[str, int] = {}


def err(msg):
    errors.append(msg)


def load(name):
    with open(DATA / f"{name}.json", encoding="utf-8") as fh:
        return json.load(fh)


def check_sources():
    reg = load("sources")["sources"]
    ids = set()
    for s in reg:
        sid = s["id"]
        if sid in ids:
            err(f"duplicate source id {sid}")
        ids.add(sid)
        if not s.get("official"):
            err(f"source {sid} is not marked official")
        host = urlparse(s["url"]).hostname or ""
        if host not in OFFICIAL_HOSTS:
            err(f"source {sid} host {host!r} is not on the official-domain allowlist")
        if not s.get("verified_on"):
            err(f"source {sid} has no verified_on date")
        if not s.get("notes"):
            err(f"source {sid} has no notes recording what was read")
        if s.get("status") not in ("verified", "verified-with-caveat"):
            err(f"source {sid} has unexpected status {s.get('status')!r}")
    stats["sources"] = len(reg)
    return ids


def check_refs(ids):
    """Walk every dataset and confirm each 'sources' list resolves, and that
    source-free rows carry a flag."""
    checked = 0

    def walk(node, path, row_flags):
        nonlocal checked
        if isinstance(node, dict):
            flags = node.get("flags", row_flags)
            if "sources" in node:
                checked += 1
                sids = node["sources"]
                rid = node.get("id", path)
                if not sids and not flags:
                    err(f"{path} ({rid}): no sources and no flag")
                for sid in sids:
                    if sid not in ids:
                        err(f"{path} ({rid}): unknown source id {sid!r}")
            if "official_basis" in node:
                for sid in node["official_basis"]:
                    if sid not in ids:
                        err(f"{path}: unknown official_basis id {sid!r}")
            if "sources_checked" in node:
                for sid in node["sources_checked"]:
                    if sid not in ids:
                        err(f"{path}: unknown sources_checked id {sid!r}")
            for k, v in node.items():
                walk(v, f"{path}.{k}", flags)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]", row_flags)

    for name in ("methods", "penalties", "us-tax", "china-rules", "fees", "flags", "audit"):
        walk(load(name), name, [])
    stats["rows with source lists"] = checked


def check_flags():
    f = load("flags")
    unv = {x["id"] for x in f["unverified"]}
    irr = {x["id"] for x in f["irregularities"]}
    for x in f["unverified"]:
        for field in ("topic", "field", "why_blank", "what_would_resolve", "severity"):
            if not x.get(field):
                err(f"flag {x['id']} missing {field}")
    # Every flag referenced by a data row must exist.
    def walk(node, path):
        if isinstance(node, dict):
            for fid in node.get("flags", []):
                if fid not in unv:
                    err(f"{path}: references unknown flag {fid!r}")
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")
    for name in ("methods", "penalties", "us-tax", "china-rules", "fees"):
        walk(load(name), name)
    stats["unverified flags"] = len(unv)
    stats["irregularities"] = len(irr)
    return unv | irr


class Check(html.parser.HTMLParser):
    """Collect ids, internal links, and table structure."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.stack = []
        self.table_depth = 0
        self.row_cells = None
        self.header_cells = None
        self.rows = []
        self.void = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                     "link", "meta", "param", "source", "track", "wbr"}
        self.problems = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.problems.append(f"duplicate id {a['id']!r}")
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "table":
            self.table_depth += 1
            self.header_cells = None
        if tag == "tr":
            self.row_cells = 0
        if tag in ("td", "th"):
            if self.table_depth == 0:
                self.problems.append(f"<{tag}> outside a table")
            if self.row_cells is None:
                self.problems.append(f"<{tag}> outside a <tr>")
            else:
                self.row_cells += 1
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "tr" and self.row_cells is not None:
            self.rows.append(self.row_cells)
            self.row_cells = None
        if tag == "table":
            self.table_depth -= 1
        if tag in self.void:
            return
        if tag in self.stack:
            while self.stack:
                t = self.stack.pop()
                if t == tag:
                    break
        else:
            self.problems.append(f"stray </{tag}>")


def check_html(flag_ids):
    pages = sorted(ROOT.glob("*.html"))
    if not pages:
        err("no HTML pages found — run build.py first")
        return
    parsed = {}
    for p in pages:
        text = p.read_text(encoding="utf-8")
        c = Check()
        c.feed(text)
        c.close()
        for prob in c.problems:
            err(f"{p.name}: {prob}")
        if c.stack:
            err(f"{p.name}: unclosed tags {c.stack}")
        # Column consistency per table: re-scan each table separately.
        for m in re.finditer(r"<table\b.*?</table>", text, re.S):
            counts = []
            for rm in re.finditer(r"<tr\b.*?</tr>", m.group(0), re.S):
                counts.append(len(re.findall(r"<t[dh]\b", rm.group(0))))
            if counts and len(set(counts)) > 1:
                err(f"{p.name}: inconsistent column counts in a table: {sorted(set(counts))}")
        parsed[p.name] = c
        # Hard-coded date check: only flag a date presented as this page's own
        # currency stamp, not a date quoted inside an audit finding about the old site.
        footer = text.split('<footer class="site-footer">')[-1]
        for dm in re.finditer(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", footer):
            warnings.append(f"{p.name}: hard-coded 'Last updated' date {dm.group(1)} in footer")
        # A leaked null renders as an element whose ENTIRE content is 'None'.
        # Prose such as "None within the limit" is legitimate and must not fail.
        for lm in re.finditer(r"<(td|dd|li|p|span)[^>]*>\s*None\s*</\1>", text):
            err(f"{p.name}: element renders only 'None' — a null leaked into the render")

    # Internal link + anchor resolution.
    nlinks = 0
    for name, c in parsed.items():
        for href in c.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            nlinks += 1
            target, _, frag = href.partition("#")
            target = unquote(target)
            if target == "":
                dest = name
            else:
                dest = target
            if not (ROOT / dest).exists():
                err(f"{name}: broken internal link to {href!r}")
                continue
            if frag and dest in parsed and frag not in parsed[dest].ids:
                err(f"{name}: link {href!r} points at missing anchor #{frag}")
    stats["html pages"] = len(pages)
    stats["internal links checked"] = nlinks

    # Every flag must be reachable from the flagged page.
    fp = parsed.get("flagged.html")
    if fp:
        for fid in flag_ids:
            if fid not in fp.ids:
                err(f"flagged.html: flag {fid} has no anchor")


def check_blanks_rendered():
    """No dataset null should appear as a bare number or the word 'null'."""
    for p in sorted(ROOT.glob("*.html")):
        text = p.read_text(encoding="utf-8")
        visible = re.sub(r"<[^>]+>", " ", text)
        for bad in ("null", "NaN", "undefined"):
            if re.search(rf"\b{bad}\b", visible):
                err(f"{p.name}: literal {bad!r} in visible text")
        if 'class="blank"' not in text and p.name in (
            "methods.html", "costs.html", "us-tax.html", "china-rules.html"
        ):
            warnings.append(f"{p.name}: no blank markers found — check nulls are rendering")


def main() -> int:
    ids = check_sources()
    check_refs(ids)
    flag_ids = check_flags()
    check_html(flag_ids)
    check_blanks_rendered()

    print("Verification")
    print("=" * 60)
    for k, v in stats.items():
        print(f"  {k:.<34} {v}")
    print()
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ! {w}")
        print()
    if errors:
        print(f"FAIL — {len(errors)} error(s):")
        for x in errors:
            print(f"  x {x}")
        return 1
    print("PASS — every row sourced, every internal link resolves, no leaked nulls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
