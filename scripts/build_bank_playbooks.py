#!/usr/bin/env python3
"""Build the additive task-17 bank, playbook and verification pages.

The JSON file is the sole editorial source for the new pages. The inherited
BOC cost ladder is read from data/cost-model.json so the 40-row evidence
matrix agrees with the existing dashboard; nothing in the shared generator
or existing root HTML is modified.
"""
from __future__ import annotations

from decimal import Decimal
from html import escape
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data/bank-playbooks.json"
DEFAULT_COST_MODEL = ROOT / "data/cost-model.json"
PAGES = ("banks.html", "playbooks.html", "verification.html")


def esc(value) -> str:
    return escape(str(value), quote=True)


def source_links(ids, sources) -> str:
    out = []
    for sid in ids:
        if sid not in sources:
            raise KeyError(f"unknown source id {sid!r}")
        item = sources[sid]
        label = f"{item['publisher']}: {item['title']}"
        out.append(
            f'<a class="source" href="{esc(item["url"])}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="{esc(label)}">[{esc(sid)}]</a>'
        )
    if not out:
        raise ValueError("every sourced row needs at least one source")
    return " ".join(out)


def tag_class(value: str) -> str:
    text = value.lower()
    if "high" in text or "not independently" in text or "no row" in text or "unproven" in text or "avoid" in text:
        return "bad"
    if "medium" in text or "not extractable" in text or "blank" in text or "historical" in text or "dynamic" in text or "fact-specific" in text:
        return "mixed"
    if "matches" in text or "documented" in text or "low" in text:
        return "good"
    return "mixed"


def tag(value: str) -> str:
    return f'<span class="tag {tag_class(value)}">{esc(value)}</span>'


def table(headers, rows, caption="", cls="", table_id=None, tag_columns=()):
    """Render a responsive data table. Each row must carry source ids."""
    full_headers = list(headers) + ["Official sources"]
    head = "".join(f'<th scope="col">{esc(h)}</th>' for h in full_headers)
    body = []
    for row in rows:
        cells = list(row["cells"])
        if len(cells) != len(headers):
            raise ValueError(f"row {row.get('id', '?')} has {len(cells)} cells, expected {len(headers)}")
        rendered = []
        for index, cell in enumerate(cells):
            value = tag(cell) if index in tag_columns else esc(cell)
            rendered.append(f'<td data-label="{esc(headers[index])}">{value}</td>')
        rendered.append(
            f'<td data-label="Official sources">{source_links(row["sources"], SOURCES)}</td>'
        )
        body.append("<tr>" + "".join(rendered) + "</tr>")
    id_attr = f' id="{esc(table_id)}"' if table_id else ""
    caption_html = f"<caption>{esc(caption)}</caption>" if caption else ""
    return (
        f'<div class="table-wrap"><table class="data {esc(cls)}"{id_attr}>'
        f"{caption_html}<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )


def layout(filename, title, subtitle, body, data) -> str:
    nav_links = "".join(
        '<a href="{href}"{active}><span>{short}</span><small>{desc}</small></a>'.format(
            href=esc(href),
            active=' class="active" aria-current="page"' if href == filename else "",
            short=esc(short),
            desc=esc(desc),
        )
        for href, short, desc in data["metadata"]["nav"]
    )
    cutoff = esc(data["metadata"]["research_cutoff_utc"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(subtitle)}">
<meta name="theme-color" content="#102a43">
<title>{esc(title)} — China4 Research</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to research</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="index.html" aria-label="China4 home"><span class="mark">C4</span><span>China4 <small>evidence desk</small></span></a>
<nav aria-label="Primary navigation">{nav_links}</nav>
</div></header>
<main class="container" id="main">
<div class="page-heading"><div><p class="eyebrow">CNY → USD · additive task-17 evidence</p><h1>{esc(title)}</h1><p class="page-sub">{esc(subtitle)}</p></div><div class="as-of"><span>Research cutoff</span><strong>{cutoff}</strong><small>Executable quotes: blank</small></div></div>
{body}
<div class="disclaimer"><strong>Research, not individualized legal, tax, or investment advice.</strong> Eligibility follows the source and character of funds, identity used at the bank, tax residence, and transaction purpose. Obtain a written all-in bank/provider quote and qualified cross-border tax review before execution. “—” means unknown or unavailable, never zero.</div>
</main>
<footer class="site-footer"><div class="inner"><div><strong>China4 evidence desk · task 17</strong><p>Additive evidence generated from <code>data/bank-playbooks.json</code>; the BOC ladder is read from <code>data/cost-model.json</code>.</p></div><div><p>Reviewed {cutoff}. FX and fees change.</p><p><a href="flagged.html">Read unresolved items before acting</a> · <a href="data/bank-playbooks.json">Task-17 data</a> · <a href="https://github.com/sassnarep3-star/China4">Repository</a></p></div></div></footer>
</body></html>'''


def money(value: Decimal) -> str:
    return f"${value:,.2f}"


def amount_matrix(data, cost_model):
    config = data["matrix_config"]
    rows = []
    cost_rows = cost_model["rows"]
    if len(cost_rows) != config["amount_count"]:
        raise ValueError("cost model row count does not match matrix config")
    for index, raw in enumerate(cost_rows, 1):
        amount = config["amount_start_usd"] + (index - 1) * config["amount_step_usd"]
        if Decimal(str(raw["amount_usd"])) != Decimal(amount):
            raise ValueError(f"cost model row {index} amount mismatch")
        base = Decimal(str(raw["base_usd"])).quantize(Decimal("0.01"))
        rows.append({
            "cells": [
                money(Decimal(amount)),
                money(base),
                "BOC tariff: 0.1%; min CNY50; max CNY260 + CNY150 telegram; dated rate is not durable",
                "—",
                "—",
                "Documented source-of-funds/tax evidence; FBAR/Form 8938 if thresholds met; personal FX-gain basis blank",
            ],
            "sources": ["T16", "T18", "T19", "T41", "T43", "T44"],
        })
    return rows


def render_banks(data) -> str:
    sources = data["sources"]
    bank_rows = [{
        "cells": [
            r["institution"], r["channel"], r["document"], r["commission"], r["telegram"],
            r["full_arrival"], r["current_executable_quote"], r["status"], r["notes"],
        ],
        "sources": r["sources"],
    } for r in data["bank_rows"]]
    condition_rows = [{
        "cells": [r["id"], r["topic"], r["rule"]],
        "sources": r["sources"],
    } for r in data["condition_rows"]]
    source_rows = [{
        "cells": [sid, item["publisher"], item["title"], item["reading"]],
        "sources": [sid],
    } for sid, item in sorted(sources.items())]
    body = f'''
<div class="hero"><div class="hero-copy"><p class="eyebrow light">Multi-bank tariff evidence</p><h2>Published schedules are evidence, not executable quotes.</h2><p>Eight bank/provider rows distinguish a dated tariff, a historical branch page, a dynamic catalogue, and a provider fee structure. Every current all-in quote remains <strong>—</strong> until a written same-time quote exists.</p><div class="hero-actions"><a class="cta" href="#bank-tariffs">Compare published rows</a><a class="cta secondary" href="playbooks.html">Open route playbooks</a><a class="cta secondary" href="verification.html">Read the verification ledger</a></div></div><div class="hero-panel"><span>Task-17 register</span><strong>{len(sources)}</strong><small>official / provider sources re-read</small><hr><span>Fee rows</span><strong>{len(data["bank_rows"])}</strong><small>bank and provider structures</small><hr><p>{esc(data["metadata"]["blank_legend"])}</p></div></div>
<div class="callout warn"><h2>Quote warning</h2><p>{esc(data["metadata"]["quote_warning"])} {source_links(["T16", "T22", "T30", "T31"], sources)}</p></div>
<section class="section" id="bank-tariffs"><div class="section-heading"><p class="eyebrow">01 · Tariffs</p><h2>Published outward-remittance and provider fee rows</h2><a href="#source-register">Jump to source register</a></div>{table(["Institution / provider", "Channel", "Document / date", "Published fee", "Telegram / channel fees", "Full-arrival / downstream fees", "Current executable quote", "Evidence status", "Notes"], bank_rows, caption="Documented fees are transcribed from the linked source; blanks are never inferred as zero.", cls="matrix", table_id="fee-table", tag_columns=(7,))}</section>
<section class="section" id="bank-conditions"><div class="section-heading"><p class="eyebrow">02 · Eligibility</p><h2>Non-tariff conditions that change the route</h2><a href="playbooks.html#route-playbooks">Apply in a playbook</a></div>{table(["ID", "Topic", "Rule / boundary"], condition_rows, caption="Classification, documentation, cash, card and reporting boundaries re-read for task 17.", table_id="condition-table")}</section>
<section class="section" id="quote-checklist"><div class="section-heading"><p class="eyebrow">03 · Execution</p><h2>What a written quote must contain</h2></div><div class="steps three"><div><span>1</span><h3>Same-time inputs</h3><p>Ask for the FX selling rate, commission, telegram, cash-to-remittance spread, full-arrival charge and expected final recipient amount at the same quote time.</p><p class="source-line">{source_links(["T16", "T20", "T21", "T22", "T31"], sources)}</p></div><div><span>2</span><h3>Route conditions</h3><p>Confirm identity classification, lawful source-of-funds/tax documents, own-account destination, tax-filing number where applicable, and any channel fee.</p><p class="source-line">{source_links(["T01", "T02", "T07", "T28", "T29", "T33"], sources)}</p></div><div><span>3</span><h3>Downstream deductions</h3><p>Ask explicitly about intermediary/receiving-bank deductions and SHA/BEN/OUR allocation. A 'free' bank fee is not an all-in quote.</p><p class="source-line">{source_links(["T16", "T22", "T26", "T31", "T32"], sources)}</p></div></div></section>
<section class="section" id="source-register"><div class="section-heading"><p class="eyebrow">04 · Sources</p><h2>Task-17 source register</h2><a href="sources.html">Inherited S1–S53 register</a></div>{table(["ID", "Publisher", "Title", "Reading status"], source_rows, caption="T IDs are local to task 17; they do not renumber the inherited S1–S53 register.", table_id="task17-sources")}</section>
'''
    return layout("banks.html", "Multi-bank tariff evidence", "Official bank tariffs, provider fee structures, eligibility boundaries and a source register for the additive task-17 pages.", body, data)


def render_playbooks(data, cost_model) -> str:
    sources = data["sources"]
    matrix_rows = amount_matrix(data, cost_model)
    quick_links = "".join(
        f'<div><span>{esc(p["id"])}</span><h3><a href="#{esc(p["id"].lower())}">{esc(p["title"])}</a></h3><p>{esc(p["summary"])}</p></div>'
        for p in data["playbooks"]
    )
    route_blocks = []
    for p in data["playbooks"]:
        steps = "".join(
            f'<li>{esc(s["text"])} <span class="source-line">{source_links(s["sources"], sources)}</span></li>'
            for s in p["steps"]
        )
        unknowns = "".join(f"<li>{esc(u)}</li>" for u in p["unknowns"])
        route_blocks.append(f'''
<details class="route" id="{esc(p['id'].lower())}" open>
<summary><span class="route-title">{esc(p['id'])} · {esc(p['title'])}</span><span class="tag good">Documented route</span></summary>
<div class="route-body"><p>{esc(p['summary'])}</p><ol class="procedure">{steps}</ol>
<div class="route-cost"><strong>Quote gate.</strong> <p>{esc(p['quote_gate'])} <span class="source-line">{source_links(p['sources'], sources)}</span></p></div>
<div class="pros-cons"><div><h3>Still unknown</h3><ul>{unknowns}</ul></div><div><h3>Source set</h3><p class="source-line">{source_links(p['sources'], sources)}</p><p>Every step above carries its own official source links.</p></div></div>
</div></details>''')
    penalty_rows = [
        {"cells": ["No evasion", "Decree 532 Arts. 39–45 set 30% ordinary ceilings and 30%–100% serious-case ceilings for specified FX offences; cash and private-exchange violations have their own ceilings.", "Penalty exposure is not a transaction cost or a minimization strategy."], "sources": ["T04", "T05", "T06"]},
        {"cells": ["Do not split", "Hui Fa [2015] No. 49 prohibits splitting/borrowed quotas and imposes a watch list for the listing year plus two following years.", "A lower visible fee is irrelevant if the route is unlawful."], "sources": ["T05", "T06"]},
        {"cells": ["Quote before execution", "No official page supplied a simultaneous executable CNY→USD rate, full fee stack and expected final recipient amount for these facts.", "Keep current-cost cells blank and obtain written same-time quotes."], "sources": ["T16", "T18", "T19", "T22", "T31"]},
    ]
    body = f'''
<div class="hero"><div class="hero-copy"><p class="eyebrow light">Route playbooks</p><h2>Route fit comes before price.</h2><p>Nine conditional procedures connect identity classification, source-of-funds/tax evidence, lawful channels, documented quotes and US reporting. The 40-row ladder shows the inherited BOC known baseline while leaving every other current all-in cost blank.</p><div class="hero-actions"><a class="cta" href="#route-playbooks">Open procedures</a><a class="cta secondary" href="#amount-ladder">$10k–$400k ladder</a><a class="cta secondary" href="banks.html">Tariff evidence</a></div></div><div class="hero-panel"><span>Playbooks</span><strong>{len(data['playbooks'])}</strong><small>conditional documented procedures</small><hr><span>Amount ladder</span><strong>{len(matrix_rows)}</strong><small>$10,000 increments</small><hr><p>Current all-in quotes for other banks and providers are deliberately blank.</p></div></div>
<div class="callout info"><h2>How to use these playbooks</h2><p>Choose the playbook that matches the legal character of the funds, then satisfy its evidence gate before comparing prices. Do not recharacterize personal savings as a service payment, dividend, social-insurance refund or cash withdrawal to fit a rule. {source_links(['T01', 'T02', 'T04', 'T13', 'T35'], sources)}</p></div>
<section class="section" id="playbook-index"><div class="section-heading"><p class="eyebrow">01 · Index</p><h2>Conditional routes</h2></div><div class="steps three">{quick_links}</div></section>
<section class="section" id="amount-ladder"><div class="section-heading"><p class="eyebrow">02 · Evidence matrix</p><h2>$10,000–$400,000 amount ladder</h2><a href="penalties.html">Inherited cost matrices</a></div>{table(['Amount (USD)', 'BOC known baseline (USD)', 'BOC published tariff', 'Other-bank current all-in cost', 'Provider current all-in cost', 'Tax / reporting gate'], matrix_rows, caption='BOC baseline is the inherited known-cost model, not a current executable quote. Every other current-cost cell is blank.', cls='matrix', table_id='amount-table')}</section>
<section class="section" id="route-playbooks"><div class="section-heading"><p class="eyebrow">03 · Procedures</p><h2>Exact conditional procedures</h2></div><div class="route-list">{''.join(route_blocks)}</div></section>
<section class="section" id="penalty-boundary"><div class="section-heading"><p class="eyebrow">04 · Boundaries</p><h2>Penalty minimization means avoiding penalties, not evading rules</h2></div>{table(['Boundary', 'Rule', 'Why it matters'], penalty_rows, caption='Statutory ceilings are enforcement exposure, not a cost-saving technique.', table_id='penalty-table')}</section>
'''
    return layout("playbooks.html", "Lawful route playbooks", "Nine conditional procedures, a 40-row evidence ladder and explicit stop conditions for documented CNY-to-USD transfers.", body, data)


def render_verification(data) -> str:
    sources = data["sources"]
    verification_rows = [{
        "cells": [r["id"], r["claim"], r["reading"], r["result"], r["limit"]],
        "sources": r["sources"],
    } for r in data["verification_rows"]]
    irregularity_rows = [{
        "cells": [r["id"], r["severity"], r["topic"], r["finding"], r["action"]],
        "sources": r["sources"],
    } for r in data["irregularities"]]
    canonical_rows = [{
        "cells": [key.replace("_", " "), item["value"]],
        "sources": item["sources"],
    } for key, item in sorted(data["canonical_facts"].items())]
    build_cards = "".join(
        f'<div><span>{i:02d}</span><h3>Automated check</h3><p>{esc(text)}</p></div>'
        for i, text in enumerate(data["build_checks"], 1)
    )
    body = f'''
<div class="hero"><div class="hero-copy"><p class="eyebrow light">Row-by-row ledger</p><h2>What was re-read, what matches, and what remains blank.</h2><p>Task 17 verifies its own additive rows from freshly re-read official/provider pages. It does not claim a full line-by-line re-fetch of the inherited S1–S53 register or a re-derivation of the existing Rev. Proc. 2025-32 tax illustration.</p><div class="hero-actions"><a class="cta" href="#verification-ledger">Verification ledger</a><a class="cta secondary" href="#irregularities">Irregularities</a><a class="cta secondary" href="banks.html#source-register">Source register</a></div></div><div class="hero-panel"><span>Ledger rows</span><strong>{len(data['verification_rows'])}</strong><small>claim / reading / result / limit</small><hr><span>Irregularities</span><strong>{len(data['irregularities'])}</strong><small>published, not merge blockers</small><hr><p>{esc(data['metadata']['blank_legend'])}</p></div></div>
<div class="callout warn"><h2>Scope boundary</h2><p>Inherited S1–S53 links in <a href="sources.html">sources.html</a> and the five-row Rev. Proc. 2025-32 tax illustration were verified by the earlier integration session, not re-derived in task 17. No new “verified” mark is applied here to those inherited values. {source_links(['T47'], sources)}</p></div>
<section class="section" id="verification-ledger"><div class="section-heading"><p class="eyebrow">01 · Ledger</p><h2>Claim-by-claim verification</h2></div>{table(['ID', 'Claim / source text', 'Reading', 'Result', 'Limit'], verification_rows, caption='“Matches source” means the cited official text was re-read and the fact agrees; it does not mean a live quote exists.', table_id='ledger-table', tag_columns=(3,))}</section>
<section class="section" id="irregularities"><div class="section-heading"><p class="eyebrow">02 · Irregularities</p><h2>Published irregularities and open items</h2></div>{table(['ID', 'Severity', 'Topic', 'Finding', 'Action'], irregularity_rows, caption='These are review flags, not blockers for the additive new files.', table_id='irregularity-table', tag_columns=(1,))}</section>
<section class="section" id="canonical-checks"><div class="section-heading"><p class="eyebrow">03 · Canonical facts</p><h2>Values independently re-checked by the validator</h2></div>{table(['Canonical fact', 'Expected value'], canonical_rows, caption='The validator hardcodes these values separately from the JSON and checks both the data and generated HTML.', table_id='canonical-table')}</section>
<section class="section" id="scope-boundary"><div class="section-heading"><p class="eyebrow">04 · Scope</p><h2>No false “verified” mark</h2></div><div class="callout info"><h2>Inherited work remains inherited</h2><p>The current seven-page dashboard, the 53-source register, the 18 procedures and the five-row 2026 tax illustration were integrated by PR #34. Task 17 adds only new files. The integration owner should preserve PR #34's own verification record and add these three pages to navigation, the Pages artifact and CI. {source_links(['T47'], sources)}</p></div></section>
<section class="section" id="build-checks"><div class="section-heading"><p class="eyebrow">05 · Build</p><h2>Reproducibility checks</h2></div><div class="steps three">{build_cards}</div></section>
'''
    return layout("verification.html", "Row-by-row verification", "Fresh task-17 source reads, canonical fact checks, irregularities and an explicit inherited-work scope boundary.", body, data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="task-17 JSON data file")
    parser.add_argument("--cost-model", type=Path, default=DEFAULT_COST_MODEL, help="inherited BOC cost-model JSON")
    parser.add_argument("--output-dir", type=Path, default=ROOT, help="directory for generated HTML")
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    cost_model = json.loads(args.cost_model.read_text(encoding="utf-8"))
    global SOURCES
    SOURCES = data["sources"]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pages = {
        "banks.html": render_banks(data),
        "playbooks.html": render_playbooks(data, cost_model),
        "verification.html": render_verification(data),
    }
    for filename, html in pages.items():
        (args.output_dir / filename).write_text(html, encoding="utf-8")
    print(
        f"Built {len(pages)} additive pages, {data['matrix_config']['amount_count']} audited amount rows "
        f"and {len(SOURCES)} sources."
    )


if __name__ == "__main__":
    main()
