#!/usr/bin/env python3
"""Dependency-free structural and independent arithmetic validation for China4."""
from __future__ import annotations

from collections import Counter
from decimal import Decimal as D, ROUND_CEILING
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "summary.html", "methods.html", "penalties.html", "taxes.html", "sources.html", "flagged.html"]
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


class AuditParser(HTMLParser):
    def __init__(self, filename: str):
        super().__init__(convert_charrefs=True)
        self.filename = filename
        self.stack: list[str] = []
        self.ids: list[str] = []
        self.links: list[str] = []
        self.tables: list[dict] = []
        self.current_table: dict | None = None
        self.details = 0
        self.h1 = 0
        self.main = 0
        self.lang = False
        self.viewport = False

    def handle_starttag(self, tag: str, attrs_list):
        attrs = dict(attrs_list)
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
            self.links.append(attrs["href"])
        if tag == "details" and "route" in attrs.get("class", "").split():
            self.details += 1
        if tag == "table":
            self.current_table = {"rows": 0, "in_body": False, "sources": 0, "row_sources": [], "in_row": False}
        if tag == "tbody" and self.current_table is not None:
            self.current_table["in_body"] = True
        if tag == "tr" and self.current_table is not None and self.current_table["in_body"]:
            self.current_table["rows"] += 1
            self.current_table["in_row"] = True
            self.current_table["row_sources"].append([])
        if tag == "a" and self.current_table is not None and "source" in attrs.get("class", "").split():
            self.current_table["sources"] += 1
            if self.current_table["in_row"]:
                self.current_table["row_sources"][-1].append(attrs.get("href", ""))
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
        if tag == "tr" and self.current_table is not None:
            self.current_table["in_row"] = False
        if tag == "tbody" and self.current_table is not None:
            self.current_table["in_body"] = False
        if tag == "table" and self.current_table is not None:
            self.tables.append(self.current_table)
            self.current_table = None


def ceil_int(x: D) -> int:
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def pieces(amount: D, cap: D):
    count = ceil_int(amount / cap)
    last = amount - cap * (count - 1)
    return [cap] * (count - 1) + [last]


def close(actual: D, expected: D, label: str):
    if abs(actual - expected) > D("1e-24"):
        fail(f"arithmetic {label}: {actual} != {expected}")


def validate_arithmetic():
    data = json.loads((ROOT / "data/cost-model.json").read_text())
    rows = data["rows"]
    if len(rows) != 40:
        fail(f"cost-model: expected 40 rows, found {len(rows)}")
    buy, sell = D("6.6648"), D("6.6929")
    mid = (buy + sell) / 2
    close(D(data["inputs"]["internal_same_quote_midpoint"]), mid, "midpoint")
    close(D(data["inputs"]["half_spread_fraction"]), (sell - mid) / mid, "half-spread")
    previous = D(0)
    for index, raw in enumerate(rows, 1):
        amount = D(index * 10000)
        r = {k: D(v) if isinstance(v, str) and re.fullmatch(r"-?\d+(\.\d+)?", v) else v for k, v in raw.items()}
        if D(raw["amount_usd"]) != amount:
            fail(f"row {index}: wrong amount ladder")
        principal = amount * sell
        commission = min(D(260), max(D(50), principal * D("0.001")))
        spread = principal * (sell - mid) / mid
        base = commission + D(150) + spread
        close(D(raw["principal_cny"]), principal, f"{amount} principal")
        close(D(raw["commission_cny"]), commission, f"{amount} commission")
        close(D(raw["spread_cny"]), spread, f"{amount} spread")
        close(D(raw["base_cny"]), base, f"{amount} base CNY")
        close(D(raw["base_usd"]), base / sell, f"{amount} base USD")
        close(D(raw["existing_usd_wire_usd"]), (commission + D(150)) / sell, f"{amount} existing USD")
        close(D(raw["draft_known_usd"]), (commission + spread) / sell, f"{amount} draft")
        close(D(raw["full_arrival_other_us_plus_bofa_usd"]), base / sell + D(40), f"{amount} receiving scenario")
        emigration_parts = [amount] if principal <= D(200000) else [amount / 2, amount / 4, amount / 4]
        emigration_total = D(0)
        for part in emigration_parts:
            p = part * sell
            c = min(D(260), max(D(50), p * D("0.001")))
            emigration_total += c + D(150) + p * (sell - mid) / mid
        if raw["emigration_wires"] != len(emigration_parts):
            fail(f"{amount}: emigration wire count")
        close(D(raw["emigration_staged_total_usd"]), emigration_total / sell, f"{amount} emigration")
        close(D(raw["inheritance_one_wire_total_usd"]), base / sell, f"{amount} inheritance")
        close(D(raw["property_sale_one_wire_total_usd"]), base / sell, f"{amount} property sale")
        annual = pieces(amount, D(50000))
        annual_total = D(0)
        for part in annual:
            p = part * sell
            c = min(D(260), max(D(50), p * D("0.001")))
            annual_total += c + D(150) + p * (sell - mid) / mid
        if raw["quota_wires"] != len(annual):
            fail(f"{amount}: quota wire count")
        close(D(raw["quota_total_usd"]), annual_total / sell, f"{amount} annual model")
        if amount == D(10000):
            close(D(raw["base_usd"]), D("53.44836522396977101779300253214629"), "known 10k regression")
            if "atm_unionpay_fee_usd" not in raw:
                fail("10k ATM model missing")
            # ATM: CNY 10,000/card/day split; fees apply per withdrawal.
            atm_pieces = pieces(principal, D(10000))
            union_fee = sum((min(D(112), D(12) + D("0.01") * part) for part in atm_pieces), D(0)) / sell
            future_fee = sum((min(D(40), max(D(3), D("0.025") * part / sell)) for part in atm_pieces), D(0))
            if raw["atm_unionpay_withdrawals"] != len(atm_pieces):
                fail("10k ATM UnionPay withdrawal count")
            if raw["atm_future_card_withdrawals"] != len(atm_pieces):
                fail("10k ATM future-card withdrawal count")
            close(D(raw["atm_unionpay_fee_usd"]), union_fee, "10k ATM UnionPay fee")
            close(D(raw["atm_future_card_fee_usd"]), future_fee, "10k ATM future-card fee")
        else:
            if "atm_unionpay_fee_usd" in raw or "atm_future_card_fee_usd" in raw:
                fail(f"{amount}: infeasible ATM amount incorrectly priced")
        current = D(raw["base_usd"])
        if current <= previous:
            fail(f"{amount}: BOC cost not strictly increasing")
        previous = current


def validate_us_tax():
    """Re-derive the 2026 US tax illustration from Rev. Proc. 2025-32 values.

    Independent of build_site.py: the floors, rates, tax-at-floor, capital-gain
    thresholds, standard deduction and FEIE amount are re-entered here from the
    published source.
    """
    brackets = [
        (D("0"), D("0.10"), D("0")),
        (D("12400"), D("0.12"), D("1240")),
        (D("50400"), D("0.22"), D("5800")),
        (D("105700"), D("0.24"), D("17966")),
        (D("201775"), D("0.32"), D("41024")),
        (D("256225"), D("0.35"), D("58448")),
        (D("640600"), D("0.37"), D("192979.25")),
    ]
    zero_max, fifteen_max, feie, other = D("49450"), D("545500"), D("132900"), D("100000")

    def ordinary(taxable):
        if taxable <= 0:
            return D(0)
        floor, rate, base = brackets[0]
        for f, r, b in brackets:
            if taxable > f:
                floor, rate, base = f, r, b
        return base + rate * (taxable - floor)

    def ltcg(start, gain):
        if gain <= 0:
            return D(0)
        begin, end = max(start, D(0)), max(start, D(0)) + gain
        mid = max(D(0), min(end, fifteen_max) - max(begin, zero_max))
        high = max(D(0), end - max(begin, fifteen_max))
        return D("0.15") * mid + D("0.20") * high

    for taxable, expected in [("12400", "1240"), ("50400", "5800"), ("105700", "17966"),
                              ("201775", "41024"), ("256225", "58448"), ("400000", "108769.25")]:
        close(ordinary(D(taxable)), D(expected), f"2026 ordinary tax at {taxable}")
    close(ltcg(D(40000), D(9000)), D("0"), "2026 LTCG inside the 0% band")
    close(ltcg(D("49450"), D("1050")), D("157.50"), "2026 LTCG crossing the 15% threshold")

    text = (ROOT / "taxes.html").read_text(encoding="utf-8")
    for amount in ("10000", "50000", "100000", "200000", "400000"):
        value = D(amount)
        for rendered in (ordinary(other + value) - ordinary(other),
                         ltcg(other, value * D("0.10")),
                         ordinary(max(D(0), other + value - feie))):
            if f"${rendered:,.2f}" not in text:
                fail(f"taxes: missing recomputed value ${rendered:,.2f} for {amount}")


def main():
    parsed = {}
    source_urls = set()
    for page in PAGES:
        path = ROOT / page
        text = path.read_text(encoding="utf-8")
        if not text.startswith("<!DOCTYPE html>"):
            fail(f"{page}: missing HTML5 doctype")
        if "{{" in text or "}}" in text:
            fail(f"{page}: unexpanded template marker")
        parser = AuditParser(page)
        parser.feed(text)
        parser.close()
        parsed[page] = parser
        if parser.stack:
            fail(f"{page}: unclosed tags {parser.stack}")
        if not parser.lang or not parser.viewport or parser.h1 != 1 or parser.main != 1:
            fail(f"{page}: landmark/viewport/lang failure")
        duplicates = [key for key, count in Counter(parser.ids).items() if count > 1]
        if duplicates:
            fail(f"{page}: duplicate IDs {duplicates}")
        for href in parser.links:
            if href == "#" or href.startswith("javascript:"):
                fail(f"{page}: invalid link {href}")
            if href.startswith("http"):
                parts = urlsplit(href)
                if parts.scheme != "https":
                    fail(f"{page}: non-HTTPS external link {href}")
                source_urls.add(href)
            elif not href.startswith(("mailto:", "tel:")):
                target, _, anchor = href.partition("#")
                target_path = (ROOT / (target or page)).resolve()
                if ROOT not in target_path.parents and target_path != ROOT:
                    fail(f"{page}: local link escapes root {href}")
                elif not target_path.exists():
                    fail(f"{page}: missing local link target {href}")
                elif anchor and target_path.suffix == ".html":
                    target_parser = parsed.get(target_path.name)
                    if target_parser is None:
                        target_parser = AuditParser(target_path.name)
                        target_parser.feed(target_path.read_text(encoding="utf-8"))
                    if anchor not in target_parser.ids:
                        fail(f"{page}: missing anchor {href}")
    if parsed["methods.html"].details != 18:
        fail(f"methods: expected 18 route procedures, found {parsed['methods.html'].details}")
    index_counts = [t["rows"] for t in parsed["index.html"].tables]
    if index_counts != [4, 18]:
        fail(f"index: expected snapshot 4 and routes 18, found {index_counts}")
    penalty_counts = [t["rows"] for t in parsed["penalties.html"].tables]
    if penalty_counts != [40, 40, 40, 40, 40, 6, 8]:
        fail(f"penalties: expected five 40-row matrices + 6 exposure + 8 penalty rows, found {penalty_counts}")
    summary_counts = [t["rows"] for t in parsed["summary.html"].tables]
    if summary_counts != [5, 8, 6]:
        fail(f"summary: expected 5 key amounts, 8 routes and 6 tax rows, found {summary_counts}")
    tax_counts = [t["rows"] for t in parsed["taxes.html"].tables]
    if tax_counts[-1] != 5:
        fail(f"taxes: expected a 5-row US tax illustration, found {tax_counts}")
    for page, parser in parsed.items():
        for number, t in enumerate(parser.tables, 1):
            for row_number, links in enumerate(t["row_sources"], 1):
                if not links or not any(url.startswith("https://") or url.startswith("http://") for url in links):
                    fail(f"{page} table {number} row {row_number}: no direct source link")
    source_rows = parsed["sources.html"].tables[0]["rows"] if len(parsed["sources.html"].tables) == 1 else -1
    if len(parsed["sources.html"].tables) != 1 or source_rows < 47:
        fail(f"sources: expected one register with at least 47 primary-source rows, found {source_rows}")
    # Guard the prose/table agreement that drifted on 2026-11-10: the stated count
    # must equal the number of registered rows.
    sources_text = (ROOT / "sources.html").read_text(encoding="utf-8")
    for claimed in re.findall(r"(\d+)[- ](?:document primary-source register|primary documents)", sources_text):
        if int(claimed) != source_rows:
            fail(f"sources: prose claims {claimed} documents but the register has {source_rows}")
    # Citation-durability guards: the rotating BOC page that used to hold the
    # cited 2026-11-09 row must not be cited again, and the dated quote must be
    # traceable to BOC's official date-query tool plus the live board.
    if "enindex_1619_4.html" in source_urls:
        fail("sources: stale BOC paginated URL reused for the dated FX quote")
    for required in ("https://www.boc.cn/sourcedb/whpjSearch/index_2833.html",
                     "https://www.boc.cn/sourcedb/whpj/enindex.html"):
        if required not in source_urls:
            fail(f"sources: missing required FX citation {required}")
    for stale_link in ("blob/arena/",):
        for page, parser in parsed.items():
            for href in parser.links:
                if stale_link in href:
                    fail(f"{page}: branch-specific repository link {href}")
    for page, parser in parsed.items():
        if ("summary.html" not in parser.links) and page not in ("estimates.html", "costs.html"):
            fail(f"{page}: navigation link to executive summary missing")
    for alias in ("estimates.html", "costs.html"):
        alias_text = (ROOT / alias).read_text(encoding="utf-8")
        if 'http-equiv="refresh" content="0; url=penalties.html"' not in alias_text or 'href="penalties.html"' not in alias_text:
            fail(f"{alias}: compatibility redirect missing")
    banned_hosts = ["fdi.gov.cn", "expatarrivals.com", "travelchinaguide.com", "wise.com/gb/blog/send-money-china-to-usa"]
    for url in source_urls:
        if any(host in url for host in banned_hosts):
            fail(f"secondary/legacy source remains: {url}")
    # Regressions for previously misleading claims and a required primary source.
    if "Dated 2018 USD 10k tier" in (ROOT / "index.html").read_text(encoding="utf-8"):
        fail("MoneyGram tier incorrectly described as covering $10,000")
    if "https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202402/P020240202362406243753.pdf" not in source_urls:
        fail("missing official annual IIT bracket source")
    if "same net USD received" not in (ROOT / "penalties.html").read_text(encoding="utf-8"):
        fail("Wise gross-vs-net comparison caveat missing")
    validate_arithmetic()
    validate_us_tax()
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} validation issue(s)")
        for error in ERRORS:
            print(f" - {error}")
        sys.exit(1)
    print(f"PASS: 7 HTML pages, executive summary, 18 procedures, 5×40 cost matrices, 2026 US tax illustration, {source_rows} sources, prose/table count agreement, local links, landmarks and independent Decimal arithmetic.")


if __name__ == "__main__":
    main()
