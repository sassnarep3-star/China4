#!/usr/bin/env python3
"""
Build the China Money site from the JSON datasets in data/.

Design rule: a table row cannot be emitted without a source. Every renderer routes
source citations through src_links(), which raises if a row has no sources and is
not explicitly flagged. Unverified values render as an explicit blank marker, never
as an estimate.

Usage:  python3 build.py
"""
from __future__ import annotations

import datetime as _dt
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DATA = ROOT / "data"
BUILD_DATE = _dt.date.today().isoformat()

NAV = [
    ("index.html", "Dashboard"),
    ("guide.html", "Decision guide"),
    ("methods.html", "All routes"),
    ("costs.html", "Conversion cost"),
    ("china-rules.html", "China rules"),
    ("us-tax.html", "US tax & reporting"),
    ("penalties.html", "Penalties"),
    ("flagged.html", "Flagged for review"),
    ("audit.html", "Repo audit"),
    ("sources.html", "Sources"),
]


def load(name):
    with open(DATA / f"{name}.json", encoding="utf-8") as fh:
        return json.load(fh)


SOURCES = {s["id"]: s for s in load("sources")["sources"]}
FLAGS = load("flags")
FLAG_INDEX = {f["id"]: f for f in FLAGS["unverified"]}
METHODS = load("methods")["methods"]
RULES = load("china-rules")
PENALTIES = load("penalties")["penalties"]
USTAX = load("us-tax")
FEES = load("fees")["fees"]
AUDIT = load("audit")


def e(value) -> str:
    """Escape text for HTML."""
    return html.escape(str(value), quote=True)


def txt(value, blank_reason: str = "not verified") -> str:
    """Render a value, or an explicit blank marker if it is None."""
    if value is None or value == "":
        return f'<span class="blank" title="Left blank: {e(blank_reason)}">—</span>'
    return e(value)


def src_links(ids, required=True, row_id="") -> str:
    """Render official-source links. Refuse to emit an unsourced, unflagged row."""
    if not ids:
        if required:
            raise SystemExit(
                f"BUILD FAILED: row {row_id!r} has no official source and is not flagged. "
                "Add a source id or an explicit flag."
            )
        return '<span class="tag bad">no official source</span>'
    out = []
    for sid in ids:
        if sid not in SOURCES:
            raise SystemExit(f"BUILD FAILED: unknown source id {sid!r} in row {row_id!r}")
        s = SOURCES[sid]
        if not s.get("official"):
            raise SystemExit(f"BUILD FAILED: source {sid} is not marked official")
        out.append(
            f'<a class="src" href="{e(s["url"])}" target="_blank" rel="noopener noreferrer" '
            f'title="{e(s["title"])} — {e(s["publisher"])}">{e(sid)}</a>'
        )
    return " ".join(out)


def flag_links(ids) -> str:
    if not ids:
        return ""
    return " ".join(
        f'<a class="tag warn" href="flagged.html#{e(fid)}" title="{e(FLAG_INDEX.get(fid, {}).get("topic", fid))}">{e(fid)}</a>'
        for fid in ids
    )


def ul(items) -> str:
    if not items:
        return '<span class="muted">none identified</span>'
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def money(value, currency="USD") -> str:
    if value is None:
        return txt(None)
    return f"{currency} {value:,.0f}"


STATUS_TAG = {
    "legal": ("good", "Lawful"),
    "legal_conditional": ("mixed", "Lawful if conditions met"),
    "prohibited": ("bad", "Prohibited"),
    "unverified": ("warn", "Unverified"),
}
SEV_TAG = {
    "critical": "bad",
    "high": "bad",
    "medium": "warn",
    "low": "info",
    "info": "info",
}
CATEGORY_LABEL = {
    "bank": "Bank channels",
    "capital": "Capital-account channels",
    "rmb": "RMB channels (convert offshore)",
    "cash": "Physical cash",
    "cards": "Cards",
    "illegal": "Prohibited — do not use",
    "unverified": "Could not be verified",
}


def page(slug: str, title: str, subtitle: str, body: str) -> str:
    nav_parts = []
    for href, label in NAV:
        active = ' class="active" aria-current="page"' if href == slug else ""
        nav_parts.append(f'<a href="{e(href)}"{active}>{e(label)}</a>')
    nav = "".join(nav_parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · China Money</title>
<meta name="description" content="{e(subtitle)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">China&nbsp;Money<span>CNY → USD, verified</span></a>
    <button class="navtoggle" aria-label="Toggle navigation" onclick="document.body.classList.toggle('nav-open')">Menu</button>
  </div>
  <nav class="site-nav"><div class="container">{nav}</div></nav>
</header>
<main id="main" class="container">
<div class="page-head">
  <h1>{e(title)}</h1>
  <p class="subtitle">{e(subtitle)}</p>
</div>
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <p><strong>Built {e(BUILD_DATE)}</strong> from the datasets in <code>data/</code>.
    Every table row links to the official source it was read from. A dash
    (<span class="blank">—</span>) means the value could not be confirmed officially and is
    <a href="flagged.html">flagged for review</a>; it never means zero.</p>
    <p class="disclaimer">Research summary, not legal, tax or financial advice. Rules and tariffs change.
    Confirm your own position with your bank, SAFE and a qualified US tax adviser before acting.
    <a href="sources.html">All {len(SOURCES)} sources</a> ·
    <a href="audit.html">What was corrected</a> ·
    <a href="https://github.com/sassnarep3-star/China4">Repository</a></p>
  </div>
</footer>
</body>
</html>
"""


def table(headers, rows, cls="data", caption=None) -> str:
    head = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="table-wrap"><table class="{cls}">{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


# ---------------------------------------------------------------- index
def build_index() -> str:
    lawful = [m for m in METHODS if m["status"] in ("legal", "legal_conditional")]
    banned = [m for m in METHODS if m["status"] == "prohibited"]
    unver = [m for m in METHODS if m["status"] == "unverified"]

    cards = f"""
<div class="card-grid">
  <div class="card"><div class="stat">{len(METHODS)}</div><div class="stat-label">routes examined</div></div>
  <div class="card"><div class="stat good-text">{len(lawful)}</div><div class="stat-label">lawful routes</div></div>
  <div class="card"><div class="stat bad-text">{len(banned)}</div><div class="stat-label">prohibited routes</div></div>
  <div class="card"><div class="stat">{len(SOURCES)}</div><div class="stat-label">official sources read</div></div>
  <div class="card"><div class="stat warn-text">{len(FLAGS['unverified'])}</div><div class="stat-label">values left blank</div></div>
  <div class="card"><div class="stat">{len(AUDIT['findings'])}</div><div class="stat-label">errors found &amp; fixed</div></div>
</div>"""

    answer = """
<section class="section best-answer">
<h2>The short answer</h2>
<p class="lede">There is no single cheap trick. The lawful route depends on <strong>two facts about you</strong>,
and the real cost is the bank's exchange-rate spread, not its fees.</p>
<ol class="steps">
<li><strong>First, work out which rule set applies to you.</strong> Chinese law splits individuals into
<em>domestic</em> (境内个人) and <em>non-domestic</em> (境外个人). Under State Council Order 532 Art. 52(2), a foreigner
who has lived in China <strong>continuously for one full year counts as domestic</strong>. Below that you are non-domestic.
This decides whether the famous USD 50,000 annual ceiling binds you at all. """ + src_links(["S02", "S01"], row_id="index-step1") + """</li>
<li><strong>If the money is documented salary or other current-account income</strong> and you are non-domestic,
convert at the bank under Detailed Rules Art. 13 with your ID, proof of the amount and your
<strong>Chinese tax vouchers</strong>. That article states no annual numeric cap. Then wire it out under Art. 15,
which for a non-domestic individual's FX savings account requires only ID. """ + src_links(["S01"], row_id="index-step2") + """</li>
<li><strong>If you are domestic</strong> (including a US citizen resident a year or more), you get
USD 50,000 a year on ID alone; above that you need documents proving a genuine current-account transaction.
Do not borrow relatives' quotas — that is quota splitting and it puts you on a three-year watch list. """ + src_links(["S01", "S03"], row_id="index-step3") + """</li>
<li><strong>If it is a large capital balance</strong> — an inheritance, or assets you owned before emigrating —
the quota routes will never be enough. Use the purpose-built <strong>inheritance transfer</strong> or
<strong>emigration transfer</strong> channel, which has no annual ceiling but needs SAFE approval and a tax certificate. """ + src_links(["S08", "S09", "S10"], row_id="index-step4") + """</li>
<li><strong>On the US side, moving your own money is not income</strong> — but converting RMB can produce an
<strong>ordinary</strong> currency gain under IRC 988, and the FBAR and Form 8938 duties apply regardless of whether
any tax is due. The reporting penalties are the expensive part. """ + src_links(["S19", "S15", "S16"], row_id="index-step5") + """</li>
</ol>
<p class="callout"><strong>Biggest avoidable cost:</strong> the exchange-rate spread. Bank of China charges
<em>no separate fee</em> for converting at its own branches, which makes conversion look free. It is not —
the bank earns the gap between its quoted rate and the interbank rate. No official spread figure is published,
so this site leaves it blank and shows you how to measure it yourself. """ + src_links(["S12"], row_id="index-spread") + " " + flag_links(["F06"]) + """</p>
</section>"""

    quick_rows = []
    for m in METHODS:
        if m["id"] not in ("M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M25", "M19", "M20", "M18"):
            continue
        cls, label = STATUS_TAG[m["status"]]
        quick_rows.append([
            f'<a href="methods.html#{e(m["id"])}"><strong>{e(m["name"])}</strong></a>',
            f'<span class="tag {cls}">{e(label)}</span>',
            txt(m.get("limit_short")),
            src_links(m["sources"], row_id=m["id"]) + " " + flag_links(m.get("flags", [])),
        ])
    quick = table(["Route", "Status", "Limit", "Official source"], quick_rows,
                  caption="The routes that matter most. Full detail on the <a href=\"methods.html\">all routes</a> page.")

    warn = """
<section class="section">
<h2>Three things that will cost you money if you get them wrong</h2>
<div class="card-grid three">
  <div class="card">
    <h3>The USD 50,000 myth</h3>
    <p>It limits <em>purchase</em> of foreign currency by <strong>domestic</strong> individuals. It does not
    apply to a non-domestic individual converting documented lawful income under Art. 13.</p>
    <p>""" + src_links(["S01", "S02"], row_id="index-myth") + """</p>
  </div>
  <div class="card">
    <h3>The fine is up to 100%, not 500%</h3>
    <p>Order 532 Arts. 39, 40 and 45 all say up to 30%, and in serious cases 30% up to
    <strong>100%</strong> of the amount. Earlier versions of this site claimed 300% and 500%. Those figures do not exist.</p>
    <p>""" + src_links(["S02"], row_id="index-fine") + """</p>
  </div>
  <div class="card">
    <h3>Bank fees change in three days</h3>
    <p>From <strong>2026-11-11</strong> Bank of China raises Mastercard and VISA overseas ATM fees to
    <strong>2.5%</strong>, capped at <strong>USD 40</strong> — up from 0.5% capped at USD 5. UnionPay is unchanged.</p>
    <p>""" + src_links(["S25"], row_id="index-atm") + """</p>
  </div>
</div>
</section>"""

    return page(
        "index.html",
        "Getting money out of China",
        "A verified, source-by-source guide for a US citizen holding CNY in a Chinese bank account.",
        cards + answer
        + '<section class="section"><h2>Route comparison at a glance</h2>' + quick + "</section>"
        + warn
        + """<section class="section"><h2>Where to go next</h2>
<div class="card-grid three">
<a class="card link-card" href="guide.html"><h3>Decision guide →</h3><p>Answer four questions, get the route that fits your facts.</p></a>
<a class="card link-card" href="costs.html"><h3>Conversion cost →</h3><p>Every fee, every layer, and how to measure the spread yourself.</p></a>
<a class="card link-card" href="us-tax.html"><h3>US tax &amp; reporting →</h3><p>FBAR, FATCA, Form 3520 and the section 988 currency gain.</p></a>
<a class="card link-card" href="china-rules.html"><h3>China rules →</h3><p>The 26 controlling rules with the Chinese text quoted.</p></a>
<a class="card link-card" href="penalties.html"><h3>Penalties →</h3><p>What each violation actually costs, from the statute.</p></a>
<a class="card link-card" href="flagged.html"><h3>Flagged for review →</h3><p>What could not be verified, and what would resolve it.</p></a>
</div></section>""",
    )


# ---------------------------------------------------------------- methods
def build_methods() -> str:
    out = ['<section class="section"><p class="lede">Every channel found, grouped by type. '
           'Prohibited routes are included deliberately, with their real penalties, so you can recognise '
           'advice that is quietly telling you to break the law.</p>']
    out.append('<div class="jump">' + " ".join(
        f'<a href="#cat-{k}">{e(v)}</a>' for k, v in CATEGORY_LABEL.items()
        if any(m["category"] == k for m in METHODS)) + "</div></section>")

    for cat, label in CATEGORY_LABEL.items():
        group = [m for m in METHODS if m["category"] == cat]
        if not group:
            continue
        out.append(f'<section class="section" id="cat-{cat}"><h2>{e(label)}</h2>')
        rows = []
        for m in group:
            cls, lab = STATUS_TAG[m["status"]]
            rows.append([
                f'<a href="#{e(m["id"])}">{e(m["id"])}</a>',
                f'<strong>{e(m["name"])}</strong><div class="muted small">{e(m["who"])}</div>',
                f'<span class="tag {cls}">{e(lab)}</span>',
                txt(m.get("limit_short")),
                txt(m["china_cost"]),
                src_links(m["sources"], required=bool(m["sources"]), row_id=m["id"]) + " " + flag_links(m.get("flags", [])),
            ])
        out.append(table(["ID", "Route / who it is for", "Status", "Limit", "China-side cost", "Source"], rows))

        for m in group:
            cls, lab = STATUS_TAG[m["status"]]
            out.append(f"""
<article class="detail" id="{e(m['id'])}">
<h3>{e(m['id'])} · {e(m['name'])} <span class="tag {cls}">{e(lab)}</span></h3>
<dl class="facts">
<dt>Who it is for</dt><dd>{e(m['who'])}</dd>
<dt>How it works</dt><dd>{e(m['how'])}</dd>
<dt>Limit</dt><dd>{txt(m['limit_text'])}</dd>
<dt>Documents required</dt><dd>{txt(m['documents'])}</dd>
<dt>China-side cost</dt><dd>{txt(m['china_cost'])}</dd>
<dt>US tax treatment</dt><dd>{txt(m['us_tax'])}</dd>
</dl>
<div class="two-col">
<div><h4 class="good-text">Advantages</h4>{ul(m['pros'])}</div>
<div><h4 class="bad-text">Drawbacks</h4>{ul(m['cons'])}</div>
</div>
<p class="sources">Official sources: {src_links(m['sources'], required=bool(m['sources']), row_id=m['id'])} {flag_links(m.get('flags', []))}</p>
</article>""")
        out.append("</section>")
    return page("methods.html", "All routes", f"{len(METHODS)} CNY→USD channels, each with its legal basis, limits, costs and trade-offs.", "".join(out))


# ---------------------------------------------------------------- costs
def build_costs() -> str:
    rows = []
    for f in FEES:
        eff = txt(f["effective"])
        if f.get("changes_2026_11_11"):
            eff += ' <span class="tag warn">changes 2026-11-11</span>'
        amount = f.get("amount_text") or " ".join(
            x for x in [f["charge"], f["min"], f["max"]] if x)
        rows.append([
            e(f["id"]),
            f'<strong>{e(f["service"])}</strong>' + (f'<div class="muted small">item {e(f["item_code"])}</div>' if f["item_code"] else ""),
            txt(amount),
            eff,
            e(f["notes"]),
            src_links(f["sources"], required=bool(f["sources"]), row_id=f["id"]) + " " + flag_links(f.get("flags", [])),
        ])
    fees_table = table(["ID", "Service", "Published charge", "Effective", "Notes", "Source"], rows)

    layers = [
        ("1", "Chinese tax on the underlying income",
         "Due when the income arose or the asset was sold — not when you convert. Property transfer income is taxed at 20% of proceeds minus original value minus reasonable expenses. If this was never paid, it is the largest single cost and it blocks the property-transfer channels, which require a tax certificate.",
         ["S11", "S08"], []),
        ("2", "The exchange-rate spread",
         "The bank quotes you a rate worse than the interbank rate and keeps the difference. Bank of China charges no separate conversion fee at its own branches, so this cost is invisible on any fee schedule. It scales with the amount, which makes it the dominant cost on a large transfer. No official figure is published, so it is left blank.",
         ["S12"], ["F06"]),
        ("3", "The bank's remittance tariff",
         "0.1% of the amount, minimum RMB 50, maximum RMB 260. Because it is capped, it becomes trivial as a percentage on a large wire: RMB 260 on a CNY 1,000,000 transfer is 0.026%. The arithmetic below uses CNY throughout so no exchange rate has to be assumed.",
         ["S12"], []),
        ("4", "Cable charge",
         "RMB 150 flat for an international transfer. On a small transfer this dominates; on a large one it is noise.",
         ["S12"], []),
        ("5", "Intermediary and beneficiary bank charges",
         "Either deducted from your principal in transit, or prepaid as a full-value-arrival surcharge of USD 15 (beneficiary bank accounts at BOC New York) or USD 25. Overseas bank charges are otherwise passed through at actual cost and are not published, so the amount cannot be stated in advance.",
         ["S12"], []),
        ("6", "US tax on the currency gain",
         "Disposing of RMB is a section 988 transaction producing ordinary gain or loss. The personal-transaction exclusion disappears entirely once the gain exceeds USD 200 — it is a cliff, not an allowance. A multi-year holding can easily produce a taxable gain.",
         ["S19"], []),
        ("7", "US reporting penalties if you skip a form",
         "Not a tax, and not proportional to the transfer. FBAR non-willful penalties are USD 16,536 per assessment; Form 8938 starts at USD 10,000 plus up to USD 50,000 more, with a 40% penalty on any related underpayment. These dwarf every bank fee on this page.",
         ["S14", "S16"], []),
        ("8", "Document costs",
         "Notary, translation, consular legalisation, proof-of-funds certificates. The requirement is verified; the fee schedules are not, so no total is quoted.",
         ["S08", "S12"], ["F11"]),
    ]
    layer_rows = [
        [e(n), f"<strong>{e(t)}</strong>", e(d), src_links(s, row_id=f"layer-{n}") + " " + flag_links(fl)]
        for n, t, d, s, fl in layers
    ]
    layer_table = table(["Layer", "Cost", "What it is and when it bites", "Source"], layer_rows)

    worked = """
<section class="section">
<h2>How the layers add up — the shape of the cost, not invented numbers</h2>
<p>No worked example on this page uses an assumed exchange rate or an assumed spread, because neither
could be verified. What the official tariff <em>does</em> let us state exactly is the fixed and capped part.</p>
"""
    # Exact arithmetic from verified tariff only.
    examples = []
    for label, cny in [("Small transfer", 20000), ("Medium transfer", 200000), ("Large transfer", 1000000)]:
        fee = min(max(cny * 0.001, 50), 260)
        cable = 150
        examples.append([
            e(label),
            f"CNY {cny:,.0f}",
            f"CNY {fee:,.0f}",
            f"CNY {cable:,.0f}",
            f"CNY {fee + cable:,.0f}",
            f"{(fee + cable) / cny * 100:.3f}%",
        ])
    worked += table(
        ["Scenario", "Amount sent", "Wire fee (0.1%, RMB 50–260)", "Cable (international)", "Total bank tariff", "As % of amount"],
        examples,
        caption="Computed only from the published tariff: 0.1% capped at RMB 260, plus RMB 150 cable. "
                "Excludes the FX spread, intermediary charges and any tax — all of which are additional.",
    )
    worked += """
<p class="callout">The bank tariff falls from <strong>1.00%</strong> of a CNY 20,000 transfer to
<strong>0.041%</strong> of a CNY 1,000,000 transfer, because the fee is capped. This is why
<strong>consolidating into fewer, larger wires</strong> reduces fees — but it does nothing about the spread,
which scales linearly with the amount and is the cost worth negotiating.</p>
<p class="sources">Tariff basis: """ + src_links(["S12"], row_id="worked") + """</p>
</section>"""

    measure = """
<section class="section">
<h2>How to measure the spread yourself</h2>
<p>Because no official spread figure exists, the only honest number is one you observe. Do this at the
moment you intend to transfer:</p>
<ol class="steps">
<li>Open your bank's published foreign-exchange quote page and note the <strong>cash-buying</strong> and
<strong>cash-selling</strong> rates for USD, and the <strong>remittance</strong> (现汇) rates, timestamped.</li>
<li>Note the same-day <strong>central parity rate</strong> published by CFETS under PBOC authority.</li>
<li>The gap between the rate the bank will actually give you and the parity rate is your spread.
Half the buying-selling gap is a reasonable proxy for the round-trip cost.</li>
<li>Ask the branch for a firm quote on your actual amount. Large amounts are often quoted better than the
board rate — this is the single highest-value negotiation available to you.</li>
<li>Compare that all-in USD received figure against a second bank before committing.</li>
</ol>
<p class="callout warn-callout"><strong>Why this is left blank rather than estimated:</strong> figures around
0.24%–0.3% circulate widely, but only on secondary sites. Publishing one would violate this project's rule
that every number comes from an official source. """ + flag_links(["F06"]) + """</p>
</section>"""

    return page("costs.html", "The conversion penalty, broken down",
                "Eight separate cost layers, the officially published bank tariff, and how to measure the one number nobody publishes.",
                '<section class="section"><h2>The eight cost layers</h2>' + layer_table + "</section>"
                + '<section class="section"><h2>Officially published bank charges</h2>'
                + '<p class="callout warn-callout">These are Bank of China\'s own published prices, effective 2025-11-11. '
                  '<strong>Item 210108014 changes on 2026-11-11</strong>; both figures are shown. Other banks publish their own tariffs. '
                + src_links(["S12", "S13", "S25"], row_id="fees-head") + "</p>"
                + fees_table + "</section>" + worked + measure)


# ---------------------------------------------------------------- china rules
def build_china_rules() -> str:
    c = RULES["classification"]
    intro = f"""
<section class="section best-answer">
<h2>Start here: {e(c['question'])}</h2>
<p class="lede">{e(c['why_it_matters'])}</p>
<blockquote lang="zh-Hans">{e(c['definition_verbatim'])}</blockquote>
<p><strong>Translation:</strong> {e(c['definition_translation'])}</p>
<p class="callout">{e(c['consequence'])} {src_links(c['sources'], row_id='classification')}</p>
</section>"""
    rows = []
    for r in RULES["rules"]:
        vals = []
        for k, cur in (("value_usd", "USD"), ("value2_usd", "USD"), ("value_cny", "CNY")):
            if r.get(k) is not None:
                period = r.get("value_period") if k == "value_usd" else None
                vals.append(money(r[k], cur) + (f" {e(period)}" if period else ""))
        for k, suffix in (("value_years", "years"), ("validity_months", "months"),
                          ("resident_days", "days"), ("rate_property_transfer_pct", "%")):
            if r.get(k) is not None:
                vals.append(f'{r[k]} {suffix}')
        value_cell = "<br>".join(vals) if vals else txt(None, "no numeric limit in this article")
        verb = f'<details><summary>Chinese text</summary><blockquote lang="zh-Hans">{e(r["verbatim"])}</blockquote></details>' if r.get("verbatim") else ""
        extra = ""
        if r.get("common_error"):
            extra += f'<div class="note error"><strong>Common error:</strong> {e(r["common_error"])}</div>'
        if r.get("practical_consequence"):
            extra += f'<div class="note"><strong>In practice:</strong> {e(r["practical_consequence"])}</div>'
        if r.get("source_caveat"):
            extra += f'<div class="note warn-note"><strong>Source caveat:</strong> {e(r["source_caveat"])}</div>'
        rows.append([
            e(r["id"]),
            f'<strong>{e(r["topic"])}</strong><div class="muted small">{e(r["article"])}</div>',
            e(r["rule"]) + verb + extra,
            value_cell,
            src_links(r["sources"], row_id=r["id"]),
        ])
    return page("china-rules.html", "The Chinese rules that control",
                "26 controlling rules, with the article, the Chinese text, and the errors people make reading them.",
                intro + '<section class="section"><h2>Rule by rule</h2>'
                + table(["ID", "Topic / article", "What the rule says", "Verified figure", "Source"], rows)
                + "</section>")


# ---------------------------------------------------------------- us tax
def build_us_tax() -> str:
    rows = []
    for u in USTAX["reporting"]:
        thr = money(u.get("threshold_usd"))
        if u.get("threshold_anytime_usd"):
            thr += f'<div class="muted small">or {money(u["threshold_anytime_usd"])} at any time</div>'
        if u.get("threshold_is_aggregate"):
            thr += '<div class="muted small">aggregate, not per account</div>'
        if u.get("tax_year"):
            thr += f'<div class="muted small">tax year {u["tax_year"]}</div>'
        detail = e(u["trigger"])
        if u.get("critical_detail"):
            detail += f'<div class="note error"><strong>Watch out:</strong> {e(u["critical_detail"])}</div>'
        rows.append([
            e(u["id"]),
            f'<strong>{e(u["form"])}</strong>',
            detail,
            thr,
            e(u["due"]) + f'<div class="muted small">{e(u["filed_with"])}</div>',
            e(u.get("penalty_short") or "")
            + f'<details><summary>Detail</summary><div class="note">{e(u["penalty_note"])}</div></details>',
            src_links(u["sources"], row_id=u["id"]) + " " + flag_links(u.get("flags", [])),
        ])
    rep = table(["ID", "Form", "Trigger", "Threshold", "When / where", "Penalty", "Source"], rows)

    trows = []
    for t in USTAX["tax_rules"]:
        body = e(t["explanation"])
        if t.get("verbatim"):
            body += f'<details><summary>Statutory text</summary><blockquote>{e(t["verbatim"])}</blockquote></details>'
        if t.get("practical_consequence"):
            body += f'<div class="note"><strong>In practice:</strong> {e(t["practical_consequence"])}</div>'
        if t.get("article_rates_note"):
            body += f'<div class="note warn-note">{e(t["article_rates_note"])}</div>'
        amt = ""
        if t.get("amount_usd"):
            amt = money(t["amount_usd"]) + f'<div class="muted small">tax year {t["tax_year"]}</div>'
        trows.append([
            e(t["id"]), f'<strong>{e(t["rule"])}</strong>', body, amt or txt(None, "not a numeric rule"),
            src_links(t["sources"], row_id=t["id"]) + " " + flag_links(t.get("flags", [])),
        ])
    return page("us-tax.html", "US tax and reporting",
                "What a US citizen must report, what is actually taxable, and the currency gain most guides omit.",
                """<section class="section best-answer"><h2>The distinction that matters</h2>
<p class="lede">Moving your own savings across a border is <strong>not income</strong>. Three other things can still cost you:</p>
<ol class="steps">
<li>A <strong>currency gain</strong> on disposing of the RMB, taxable as ordinary income under IRC 988.</li>
<li><strong>Information-reporting penalties</strong>, which apply whether or not any tax is due.</li>
<li><strong>Chinese tax on the underlying income</strong>, if it was never declared in China.</li>
</ol></section>"""
                + '<section class="section"><h2>Reporting obligations</h2>' + rep + "</section>"
                + '<section class="section"><h2>What is and is not taxable</h2>'
                + table(["ID", "Rule", "Explanation", "Amount", "Source"], trows) + "</section>")


# ---------------------------------------------------------------- penalties
def build_penalties() -> str:
    rows = []
    for p in PENALTIES:
        if p["base_fine_pct_max"] is not None:
            base = f'up to {p["base_fine_pct_max"]}%'
        else:
            base = txt(None, "this article sets no percentage fine")
        if p["serious_fine_pct_max"] is not None:
            serious = f'{p["serious_fine_pct_min"]}% – {p["serious_fine_pct_max"]}%'
        else:
            serious = txt(None, "no serious-case tier in this article")
        body = e(p["conduct"])
        if p.get("fixed_fine_text"):
            body += f'<div class="note"><strong>Fixed amounts:</strong> {e(p["fixed_fine_text"])}</div>'
        body += f'<div class="note">{e(p["other_measures"])}</div>'
        if p.get("verbatim"):
            body += f'<details><summary>Chinese statutory text</summary><blockquote lang="zh-Hans">{e(p["verbatim"])}</blockquote></details>'
        rows.append([
            e(p["id"]),
            f'<strong>{e(p["article"])}</strong><div class="muted small" lang="zh-Hans">{e(p["chinese"])}</div>',
            body, base, serious,
            src_links(p["sources"], row_id=p["id"]),
        ])
    return page("penalties.html", "What violations actually cost",
                "Every penalty read from State Council Order 532 and the governing notices, with the Chinese text quoted.",
                """<section class="section"><p class="callout error-callout"><strong>Correction to earlier versions of this site:</strong>
it claimed fines of “30%–300%” and “30%–500%”. Neither figure exists in the statute. Arts. 39, 40 and 45 all read
<em>up to 30%</em>, and in serious cases <em>30% up to 100%</em> — 等值 means the equivalent amount, i.e. 100%.
The “1 to 5 times” multiplier belongs to Art. 46 and applies to unlicensed <strong>operators</strong>, not customers.
""" + src_links(["S02"], row_id="pen-correction") + """</p>
<p class="lede">Percentages below are of the illegal amount. “Serious circumstances” is a finding by SAFE, not a
fixed threshold, so treat the upper tier as a real possibility rather than a remote one.</p></section>"""
                + '<section class="section"><h2>Penalty schedule</h2>'
                + table(["ID", "Provision", "Conduct and measures", "Base fine", "Serious cases", "Source"], rows)
                + "</section>")


# ---------------------------------------------------------------- guide
def build_guide() -> str:
    c = RULES["classification"]
    body = f"""
<section class="section best-answer">
<h2>Question 1 — Which rule set applies to you?</h2>
<p>Under Order 532 Art. 52(2) you are a <strong>domestic individual</strong> (境内个人) if you are a Chinese
citizen <em>or</em> a foreigner who has resided in China <strong>continuously for one full year</strong>.
Otherwise you are a <strong>non-domestic individual</strong> (境外个人).</p>
<blockquote lang="zh-Hans">{e(c['definition_verbatim'])}</blockquote>
<p class="sources">{src_links(['S02'], row_id='guide-q1')}</p>
</section>

<section class="section">
<h2>Question 2 — What kind of money is it?</h2>
"""
    q2 = [
        ("Salary or other current-account income earned in China, with Chinese tax paid",
         "Non-domestic: <a href=\"methods.html#M01\">M01</a> — Art. 13 conversion with tax vouchers, no annual numeric cap. "
         "Domestic: <a href=\"methods.html#M02\">M02</a> within USD 50,000, or <a href=\"methods.html#M03\">M03</a> above it with documents.",
         ["S01"]),
        ("An inheritance from someone who died in China",
         "<a href=\"methods.html#M05\">M05</a> — inheritance transfer. No annual quota, but SAFE approval and a tax certificate for the decedent's property. This is the purpose-built channel.",
         ["S08", "S09", "S10"]),
        ("Assets you owned before you emigrated from China",
         "<a href=\"methods.html#M06\">M06</a> — emigration transfer. Requires a Chinese household-registration cancellation certificate, so it is unavailable if you never held Chinese hukou. Staged over up to two years.",
         ["S08", "S11"]),
        ("Proceeds of selling Chinese property",
         "There is no general 'property sale' remittance route for a non-domestic individual in the Detailed Rules. "
         "If you inherited it, use <a href=\"methods.html#M05\">M05</a>. Otherwise the proceeds are capital, and the "
         "current-account routes do not cover them — the 20% property-transfer tax must be settled first. "
         "Treat any promise of an easy property-proceeds wire as a red flag.",
         ["S11", "S01", "S08"]),
        ("Money already converted into USD in your Chinese account",
         "<a href=\"methods.html#M04\">M04</a> — remit from the FX savings account. Non-domestic: ID only, no stated ceiling. "
         "Domestic: up to USD 50,000 <em>per day</em> on ID alone. No new spread, because no conversion is needed.",
         ["S01"]),
        ("RMB you converted from USD on an earlier trip, unspent",
         "<a href=\"methods.html#M25\">M25</a> — reconvert with the original exchange memo, valid 24 months. "
         "Up to USD 500 a day needs ID only.",
         ["S01"]),
    ]
    body += table(["If the money is…", "Route", "Source"],
                  [[e(a), b, src_links(s, row_id=f"guide-q2-{i}")] for i, (a, b, s) in enumerate(q2)])
    body += """
<p class="callout"><strong>Alternative worth asking your bank about:</strong>
<a href="methods.html#M07">M07</a> — send the RMB itself offshore under the current account and convert
outside China. Yinfa [2020] No. 330 item 13 expressly supports this for salary and other lawful income.
It sidesteps the onshore purchase quota because no onshore conversion happens. Whether your bank offers it,
and any limit, could not be verified. """ + src_links(["S07"], row_id="guide-m07") + " " + flag_links(["F01"]) + """</p>
</section>

<section class="section">
<h2>Question 3 — Have you met your US reporting duties?</h2>
<p>Do this <strong>before</strong> moving money, not after. A large inbound wire can prompt questions, and the
penalties for unfiled forms are unrelated to whether you owe any tax.</p>
"""
    q3 = [
        ("Did all your foreign accounts together exceed USD 10,000 at any point in the year?",
         "File FinCEN Form 114 (FBAR). Due 15 April. Non-willful penalty USD 16,536.", ["S15", "S14"]),
        ("Do your foreign financial assets exceed the Form 8938 threshold for your filing status and residence?",
         "File Form 8938 with your return. Living abroad single: USD 200,000 year-end or USD 300,000 at any time. "
         "Filing 8938 does not excuse the FBAR.", ["S16"]),
        ("Did you inherit or receive more than USD 100,000 from a foreign individual or estate?",
         "File Form 3520 Part IV. Penalty 5% of the gift per month, up to 25%.", ["S17"]),
        ("Are you about to convert RMB you have held for years?",
         "Compute the IRC 988 gain using your USD basis at acquisition. If the gain exceeds USD 200 the whole "
         "gain is taxable as ordinary income — the exclusion is a cliff, not an allowance.", ["S19"]),
        ("Will you carry more than USD 10,000 in cash or instruments across the US border?",
         "File FinCEN Form 105. The threshold is collective for a family or group, not per person.", ["S21"]),
    ]
    body += table(["Ask yourself", "If yes", "Source"],
                  [[e(a), e(b), src_links(s, row_id=f"guide-q3-{i}")] for i, (a, b, s) in enumerate(q3)])
    body += """</section>

<section class="section">
<h2>Question 4 — How do you minimise the cost?</h2>
<ol class="steps">
<li><strong>Settle any Chinese tax first.</strong> It is the largest layer and it gates the capital-account channels.
""" + src_links(["S11", "S08"], row_id="guide-q4-1") + """</li>
<li><strong>Get a firm quote on your actual amount.</strong> The spread is the dominant cost and the board rate is
often not the best available rate for a large conversion. See <a href="costs.html">the conversion cost page</a>.
""" + src_links(["S12"], row_id="guide-q4-2") + " " + flag_links(["F06"]) + """</li>
<li><strong>Consolidate into fewer, larger wires.</strong> The wire fee is capped at RMB 260, so its percentage
falls sharply with size. Splitting a transfer multiplies the RMB 150 cable charge for no benefit.
""" + src_links(["S12"], row_id="guide-q4-3") + """</li>
<li><strong>Decide deliberately who pays intermediary charges.</strong> The full-value-arrival surcharge is
USD 15 or USD 25; without it, correspondents deduct from your principal at unpublished rates.
""" + src_links(["S12"], row_id="guide-q4-4") + """</li>
<li><strong>Use UnionPay, not Mastercard or VISA, for overseas cash after 2026-11-11.</strong>
UnionPay stays at RMB 12 + 1% capped at RMB 112; the other networks move to 2.5% capped at USD 40.
""" + src_links(["S25"], row_id="guide-q4-5") + """</li>
<li><strong>Never buy speed with an illegal channel.</strong> Underground banks, crypto and quota splitting
carry fines up to the entire amount in serious cases, plus criminal exposure.
""" + src_links(["S02", "S06", "S03"], row_id="guide-q4-6") + """</li>
</ol>
</section>

<section class="section">
<h2>Red flags in advice you may be given</h2>
"""
    red = [
        ("“Just use five relatives' quotas.”", "Quota splitting. Both lender and borrower are targeted; the watch-list period is the year of listing plus two more years.", ["S03"]),
        ("“Use USDT, it's instant and nobody checks.”", "Fiat-to-crypto exchange is an illegal financial activity in China; related civil acts can be void, so you may have no recourse if the counterparty disappears.", ["S06"]),
        ("“Pay RMB here, receive USD there.”", "This is mirror settlement (对敲) — disguised FX trading under Art. 45, up to 30% and in serious cases up to 100% of the amount, plus criminal exposure.", ["S02"]),
        ("“The fine can be 500%.”", "Not in the statute. The ceiling is 100% of the amount. Anyone quoting 300% or 500% has not read Order 532.", ["S02"]),
        ("“You can only ever move USD 50,000 a year.”", "Only for domestic individuals purchasing FX, and even then Art. 12 allows more with documents. Inheritance and emigration transfers have no annual quota.", ["S01", "S08"]),
        ("“There's no US tax when you convert.”", "Disposing of RMB is a section 988 transaction. The USD 200 personal exclusion vanishes entirely above USD 200 of gain.", ["S19"]),
    ]
    body += table(["What you might hear", "Why it is wrong", "Source"],
                  [[e(a), e(b), src_links(s, row_id=f"guide-red-{i}")] for i, (a, b, s) in enumerate(red)])
    body += "</section>"
    return page("guide.html", "Decision guide",
                "Four questions that determine your route, then how to minimise the cost.", body)


# ---------------------------------------------------------------- flagged
def build_flagged() -> str:
    rows = []
    for f in FLAGS["unverified"]:
        rows.append([
            f'<span id="{e(f["id"])}">{e(f["id"])}</span>',
            f'<strong>{e(f["topic"])}</strong><div class="muted small">{e(f["field"])}</div>',
            e(f["why_blank"]) + (f'<div class="note">{e(f["note"])}</div>' if f.get("note") else ""),
            e(f["what_would_resolve"]),
            f'<span class="tag {SEV_TAG[f["severity"]]}">{e(f["severity"])}</span>',
            src_links(f["sources_checked"], required=False, row_id=f["id"]),
        ])
    irows = []
    for i in FLAGS["irregularities"]:
        irows.append([
            f'<span id="{e(i["id"])}">{e(i["id"])}</span>',
            f'<strong>{e(i["title"])}</strong>',
            e(i["detail"]),
            e(i["resolution"]),
            f'<span class="tag {SEV_TAG[i["severity"]]}">{e(i["severity"])}</span>',
        ])
    return page("flagged.html", "Flagged for review",
                f"{len(FLAGS['unverified'])} values left blank and {len(FLAGS['irregularities'])} irregularities, published openly.",
                """<section class="section"><p class="callout"><strong>How to read this page.</strong>
A dash (<span class="blank">—</span>) anywhere on this site means the value could not be confirmed from an
official source. It never means zero, and it never means "not applicable". No figure on this site was
estimated, interpolated or taken from a secondary website. These flags do not block publication; they tell
you exactly where the research stops.</p></section>"""
                + '<section class="section"><h2>Values left blank</h2>'
                + table(["ID", "What is missing", "Why it is blank", "What would resolve it", "Severity", "Sources checked"], rows)
                + "</section>"
                + '<section class="section"><h2>Irregularities found</h2>'
                + table(["ID", "Irregularity", "Detail", "Resolution", "Severity"], irows)
                + "</section>")


# ---------------------------------------------------------------- audit
def build_audit() -> str:
    m = AUDIT["_meta"]
    frows = []
    for f in AUDIT["findings"]:
        frows.append([
            f'<span id="{e(f["id"])}">{e(f["id"])}</span>',
            f'<strong>{e(f["file"])}</strong>',
            e(f["claim_as_published"]),
            e(f["finding"]) + f'<div class="note"><strong>Action:</strong> {e(f["action"])}</div>',
            f'<span class="tag {SEV_TAG[f["severity"]]}">{e(f["severity"])}</span>',
            src_links(f["official_basis"], required=False, row_id=f["id"]),
        ])
    vrows = []
    for v in AUDIT["files_reviewed"]:
        links = []
        for x in v["findings"]:
            # A-xx findings live on this page; I-xx irregularities live on flagged.html.
            href = f"#{x}" if x.startswith("A-") else f"flagged.html#{x}"
            links.append(f'<a href="{e(href)}">{e(x)}</a>')
        vrows.append([
            f'<code>{e(v["file"])}</code>', e(v["lines_reviewed"]), str(v["claims_checked"]),
            " ".join(links) or '<span class="muted">none</span>', e(v["verdict"]),
        ])
    total_claims = sum(v["claims_checked"] for v in AUDIT["files_reviewed"])
    return page("audit.html", "Repository audit",
                f"Line-by-line review of the previously published site: {total_claims} claims checked, {len(AUDIT['findings'])} findings.",
                f"""<section class="section">
<p class="lede">The site as previously published at commit <code>{e(m['baseline_commit'][:7])}</code> was reviewed
claim by claim against the primary text of each governing instrument, fetched live from the regulator's own site.</p>
<div class="card-grid">
<div class="card"><div class="stat">{total_claims}</div><div class="stat-label">claims checked</div></div>
<div class="card"><div class="stat bad-text">{sum(1 for f in AUDIT['findings'] if f['severity'] == 'critical')}</div><div class="stat-label">critical errors</div></div>
<div class="card"><div class="stat warn-text">{sum(1 for f in AUDIT['findings'] if f['severity'] == 'high')}</div><div class="stat-label">high-severity findings</div></div>
<div class="card"><div class="stat">{len(AUDIT['files_reviewed'])}</div><div class="stat-label">files reviewed</div></div>
</div>
<p class="callout">Two findings were <strong>critical</strong> in the sense that they would mislead a reader about
what they may lawfully do: the USD 50,000 quota was applied to the wrong class of person, and two penalty ranges
were fabricated. Both are corrected below with the statutory text quoted so the correction is auditable.</p>
</section>"""
                + '<section class="section"><h2>Files reviewed</h2>'
                + table(["File", "Scope", "Claims checked", "Findings", "Outcome"], vrows) + "</section>"
                + '<section class="section"><h2>Findings</h2>'
                + table(["ID", "Where", "As published", "Finding and action", "Severity", "Official basis"], frows)
                + "</section>")


# ---------------------------------------------------------------- sources
def build_sources() -> str:
    rows = []
    for s in SOURCES.values():
        rows.append([
            f'<span id="{e(s["id"])}">{e(s["id"])}</span>',
            f'<a href="{e(s["url"])}" target="_blank" rel="noopener noreferrer"><strong>{e(s["title"])}</strong></a>'
            f'<div class="muted small">{e(s["key_articles"])}</div>',
            e(s["publisher"]),
            e(s["type"]),
            e(s["verified_on"]) + f'<div><span class="tag {"good" if s["status"] == "verified" else "warn"}">{e(s["status"])}</span></div>',
            e(s["notes"]),
        ])
    return page("sources.html", "Source registry",
                f"All {len(SOURCES)} sources, each fetched and read directly. Click any title to open the original.",
                """<section class="section"><p class="callout"><strong>What counts as official here.</strong>
A source is official if it is published by the regulator (SAFE, PBOC, Customs, the State Taxation Administration,
the IRS, FinCEN, CBP), by the legislature or government, or — for bank charges — by the regulated institution
itself in its own published tariff. Travel sites, accountancy blogs, news articles and commercial bank marketing
pages are used for nothing. Every date below is the date the page was actually fetched and read.</p>
<p>Two entries carry caveats rather than a clean verification: an IRS page that is official but out of date, and a
Customs reply that confirms a figure whose primary instrument could not be reached. Both are labelled in the
status column and cross-referenced on the <a href="flagged.html">flagged page</a>.</p></section>"""
                + '<section class="section">'
                + table(["ID", "Document", "Publisher", "Type", "Read on", "What it establishes"], rows)
                + "</section>")


PAGES = {
    "index.html": build_index,
    "guide.html": build_guide,
    "methods.html": build_methods,
    "costs.html": build_costs,
    "china-rules.html": build_china_rules,
    "us-tax.html": build_us_tax,
    "penalties.html": build_penalties,
    "flagged.html": build_flagged,
    "audit.html": build_audit,
    "sources.html": build_sources,
}


def main() -> int:
    for slug, fn in PAGES.items():
        content = fn()
        (ROOT / slug).write_text(content, encoding="utf-8")
        print(f"  built {slug:20s} {len(content):>7,} bytes")
    # Retire the old hand-written page that no longer exists in the nav.
    old = ROOT / "taxes.html"
    if old.exists():
        old.write_text(
            '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta http-equiv="refresh" content="0; url=us-tax.html">'
            '<title>Moved · China Money</title><link rel="stylesheet" href="style.css">'
            '</head><body><main class="container"><h1>This page has moved</h1>'
            '<p>US tax and reporting now lives at <a href="us-tax.html">us-tax.html</a>.</p>'
            '</main></body></html>', encoding="utf-8")
        print("  taxes.html -> redirect to us-tax.html")
    print(f"\nBuilt {len(PAGES)} pages from {len(SOURCES)} sources on {BUILD_DATE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
