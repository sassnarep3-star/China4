#!/usr/bin/env python3
"""Static integrity checks for the GitHub Pages deliverable."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
OFFICIAL_DOMAINS = {
    "safe.gov.cn", "chinatax.gov.cn", "irs.gov", "govinfo.gov",
    "fincen.gov", "customs.gov.cn"
}

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)

def check_json(name):
    try:
        return json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"data/{name}.json is invalid: {exc}")

def check_sources(rows, label):
    for index, row in enumerate(rows, 1):
        sources = row.get("sources")
        if not sources:
            fail(f"{label} row {index} has no official source link")
        for source in sources:
            url = source.get("url", "")
            host = (urlparse(url).hostname or "").lower()
            if urlparse(url).scheme not in ("http", "https") or not any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS):
                fail(f"{label} row {index} has non-official/invalid source URL: {url}")

def main():
    html_files = sorted(ROOT.rglob("*.html"))
    if not html_files:
        fail("no HTML entry pages found")
    broken = []
    for html_file in html_files:
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for link in parser.links:
            parsed = urlparse(link)
            if parsed.scheme or link.startswith("#") or link.startswith("//"):
                continue
            path = (html_file.parent / parsed.path).resolve()
            if path.is_dir():
                path = path / "index.html"
            if not path.exists():
                broken.append(f"{html_file.relative_to(ROOT)} -> {link}")
    if broken:
        fail("broken internal links:\n  " + "\n  ".join(broken))

    for name in ("routes", "tax", "costs", "requirements", "sources", "flags"):
        rows = check_json(name)
        if not isinstance(rows, list) or not rows:
            fail(f"data/{name}.json must contain a non-empty list")
        if name == "sources":
            for index, source in enumerate(rows, 1):
                host = (urlparse(source.get("url", "")).hostname or "").lower()
                if not any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS):
                    fail(f"source register entry {index} is not on an official domain")
        else:
            check_sources(rows, name)
        if name == "costs":
            for index, row in enumerate(rows, 1):
                if "Unverified" in row.get("status", "") and row.get("amount"):
                    fail(f"cost row {index} has an unverified value filled in")

    if not (ROOT / ".nojekyll").exists():
        fail(".nojekyll missing")
    print(f"OK: {len(html_files)} HTML pages, 6 data files, all table rows sourced, no broken internal links.")

if __name__ == "__main__":
    main()
