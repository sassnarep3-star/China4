#!/usr/bin/env python3
"""Generate the static China4 dashboard from canonical research JSON."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = "2026-11-08"
REPO = "https://github.com/sassnarep3-star/China4"
LIVE = "https://sassnarep3-star.github.io/China4/"
AMOUNTS = list(range(10_000, 400_001, 10_000))

NAV = [
    ("index.html", "Dashboard"),
    ("methods.html", "Methods"),
    ("costs.html", "Cost tables"),
    ("procedures.html", "Procedures"),
    ("taxes.html", "Tax & reporting"),
    ("penalties.html", "Penalties"),
    ("sources.html", "Sources"),
    ("flagged.html", "Flagged for Review"),
    ("audit.html", "Audit"),
    ("verification.html", "Verification"),
]
CATEGORIES = [
    ("bank", "Bank channels", "category-bank.html", "Regulated bank conversion/remittance and draft options."),
    ("digital", "Digital operators", "category-digital.html", "Wise, SkyRemit, WU and unverified app routes."),
    ("special", "Property & status routes", "category-special.html", "Property sale, migration, inheritance and dividends."),
    ("business", "Business & RMB routes", "category-business.html", "Genuine trade and current-account RMB settlement."),
    ("cash_cards", "Cash & cards", "category-cash-cards.html", "ATM and cash carrying, with caps and declarations."),
    ("investments", "Investment/support channels", "category-investments.html", "Account witness, WMC and QDII; mostly not free disposal routes."),
    ("prohibited", "Excluded workarounds", "category-prohibited.html", "Underground, crypto, fake trade and quota borrowing risks."),
]


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def link(href: str, text: str, cls: str = "") -> str:
    c = f' class="{e(cls)}"' if cls else ""
    return f'<a{c} href="{e(href)}">{e(text)}</a>'


def source_links(ids: list[str], sources: dict) -> str:
    parts = []
    for sid in ids:
        s = sources[sid]
        if s.get("access") == "not_found":
            parts.append(f'<span class="tag bad">failed fetch</span> {e(s["publisher"])} attempted URL (not linked)')
        else:
            parts.append(link(s["url"], f'{s["publisher"]}: {s["title"]}', "source"))
    return " · ".join(parts)


def page(title: str, active: str, body: str, subtitle: str = "") -> str:
    nav_parts = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        nav_parts.append(f'<a href="{e(href)}"{current}>{e(label)}</a>')
    nav = "\n".join(nav_parts)
    sub = f'<p class="page-sub">{subtitle}</p>' if subtitle else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} — China4</title>
<meta name="description" content="Lawful CNY-to-USD research dashboard for US citizens: source-matched routes, costs, tax, reporting and flags.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true">C4</span> China4</a>
    <nav aria-label="Primary navigation">{nav}</nav>
  </div>
</header>
<main id="main" class="container">
<h1>{e(title)}</h1>
{sub}
{body}
</main>
<footer class="site-footer">
  <div class="inner">
    <p>Research date {AS_OF}. Not legal or tax advice; confirm current bank/operator terms and personal tax facts.</p>
    <p>{link(REPO, "GitHub repository")} · {link(LIVE, "Live GitHub Pages site")} · {link("costs.csv", "Download complete cost CSV")}</p>
  </div>
</footer>
</body>
</html>
"""


def table(caption: str, headers: list[str], rows: list[list[str]], require_source: bool = True, cost_method: str | None = None) -> str:
    cls = "data require-source" if require_source else "data"
    extra = f' data-cost-table="{e(cost_method)}"' if cost_method else ""
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "\n".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f"""<div class="table-scroll" role="region" aria-label="{e(caption)}" tabindex="0">
<table class="{cls}"{extra}>
<caption>{e(caption)}</caption>
<thead><tr>{head}</tr></thead>
<tbody>
{body}
</tbody>
</table>
</div>"""


def blank_cell(label: str) -> str:
    return f'<span class="blank" role="img" aria-label="{e(label)}: unverified, left blank"></span>'


def method_anchor(mid: str) -> str:
    return f"proc-{mid}"


def cost_anchor(mid: str) -> str:
    return f"cost-{mid}"


def render_index(findings, procedures, sources) -> str:
    claims = {c["id"]: c for c in findings["claims"]}
    rows = []
    decision = [
        ("China salary", "Bank TT; eligible Wise/SkyRemit own-account service", "Contract, income details, tax records, own US account", ["safe_rules", "icbc_fx", "wise_cny", "sky_terms"]),
        ("Unused RMB from earlier exchange", "Bank reconversion", "Original memo within 24 months; qualifying card evidence", ["safe_rules", "icbc_fx"]),
        ("Other lawful current-account RMB income", "Bank documented current-account purchase/remittance", "Transaction-amount source/tax evidence", ["safe_rules", "safe_faq"]),
        ("Mainland property sale", "Bank property-sale proceeds review", "Registered sale/title/tax documents", ["safe_property_amended", "icbc_fx", "cn_home_sale_shanghai"]),
        ("Pre-migration assets", "Migration transfer via competent SAFE branch", "Status, former hukou, source/title, tax documents", ["safe_migration", "safe_property_venue_2026"]),
        ("Mainland inheritance", "Inheritance transfer via decedent’s former-hukou SAFE branch", "Inheritance instrument, title, identity, tax documents", ["safe_inheritance", "safe_property_venue_2026"]),
        ("FIE dividend", "Corporate distribution + withholding + bank review", "Profit resolution, withholding, registration documents", ["cn_dividends_2026"]),
        ("Genuine trade/e-commerce", "Compliant trade settlement account", "Registration, contracts, logistics/transaction evidence", ["safe_faq", "safe_rules"]),
        ("Small travel cash need", "Overseas ATM or controlled cash carry", "Card/permit/declaration records", ["safe_cards", "china_customs", "cbp_105"]),
    ]
    for source, route, evidence, sids in decision:
        rows.append([e(source), e(route), e(evidence), source_links(sids, sources)])
    cards = []
    for key, title, href, desc in CATEGORIES:
        count = sum(1 for m in procedures["methods"] if m["category"] == key)
        cards.append(f'<article class="card"><h3>{link(href, title)}</h3><p class="big">{count} <small>methods</small></p><p>{e(desc)}</p></article>')
    key_numbers = [
        ("USD 50,000", "Facilitation quota, not a universal outbound cap", ["safe_rules", "safe_faq"]),
        ("USD 132,900", "2026 FEIE maximum; earned income and eligibility tests apply", ["irs_2555"]),
        ("USD 10,000", "FBAR aggregate account-value trigger, not a transfer-size trigger", ["fincen_fbar"]),
        ("CNY 100,000", "Overseas card cash withdrawal cap per person per calendar year", ["safe_cards"]),
        ("20%", "PRC IIT on foreign-individual FIE dividends from 2026-09-01", ["cn_dividends_2026"]),
        ("Blank", "Unverified all-in USD totals are intentionally not guessed", ["boc_tariff", "wise_pricing"]),
    ]
    number_cards = "".join(
        f'<article class="card"><h3>{e(big)}</h3><p>{e(text)}</p><p class="small">{source_links(sids, sources)}</p></article>'
        for big, text, sids in key_numbers
    )
    body = f"""
<section class="hero" aria-labelledby="hero-heading">
  <h2 id="hero-heading">Most important answer first</h2>
  <p>{e(findings['bottom_line'])}</p>
  <p class="cta-row">{link('methods.html', 'Compare all methods', 'cta')} {link('costs.html', 'Open 1,120 cost rows', 'cta secondary')} {link('procedures.html', 'Step-by-step procedures', 'cta secondary')}</p>
</section>
<section class="callout ok" aria-labelledby="short-answer">
  <h2 id="short-answer">The lawful starting point</h2>
  <p>Match the route to the actual source of the CNY. For documented China salary or other lawful current-account income, start with a bank or an eligible own-account salary service and compare same-time all-in net-USD quotes. Do not treat the USD 50,000 facilitation quota as a universal outbound cap, and do not assume “already taxed in China” means “no US tax.”</p>
  <p class="small">{source_links(['safe_rules','safe_faq','icbc_fx','irs_worldwide','irc_988'], sources)}</p>
</section>
<section aria-labelledby="decision-title">
  <h2 id="decision-title">Source-of-funds decision table</h2>
  {table('Choose the route by the actual source of funds', ['Actual source','First lawful route to investigate','Key evidence','Official sources'], rows)}
</section>
<section aria-labelledby="numbers-title">
  <h2 id="numbers-title">Key numbers and corrections</h2>
  <div class="card-grid">{number_cards}</div>
</section>
<section aria-labelledby="categories-title">
  <h2 id="categories-title">Category subpages</h2>
  <div class="card-grid">{''.join(cards)}</div>
</section>
<section aria-labelledby="summary-title">
  <h2 id="summary-title">Executive summary</h2>
  <p>{link('EXECUTIVE_SUMMARY.md', 'Read the full executive summary')} or use the dashboard sections below.</p>
  <ol class="plain-list">
    <li><strong>Costs:</strong> BOC publishes TT/draft commission 0.1%, min CNY 50/max CNY 260, plus cable CNY 150/80; overseas charges actual. No customer-specific FX/all-in USD quote was verified. {source_links(['boc_tariff'], sources)}</li>
    <li><strong>Tax:</strong> US citizens generally report worldwide income; CNY disposition can produce IRC §988 currency gain/loss. Compare eligible FTC/FEIE without double benefit. {source_links(['irs_worldwide','irc_988','irs_ftc','irs_2555'], sources)}</li>
    <li><strong>Reporting:</strong> FBAR, Form 8938 and Form 3520 have different triggers; reporting is not a transfer tax. {source_links(['fincen_fbar','irs_8938','irs_3520'], sources)}</li>
    <li><strong>Excluded:</strong> underground matchers, borrowed quotas, fake invoices and mainland crypto exchange workarounds are not lawful planning options. {source_links(['safe_fx_reg','pboc_crypto_2026'], sources)}</li>
  </ol>
</section>
<section class="callout warn" aria-labelledby="flags-title">
  <h2 id="flags-title">Flagged for Review</h2>
  <p>Unverified values are blank, not zero. The flag register covers FX/all-in quotes, personal tax, operator limits, local property tax, migration staging, dividend transition, future ATM tariffs and professional costs.</p>
  <p>{link('flagged.html', 'Open the flag register')} · {link('audit.html', 'Open the line-by-line audit')}</p>
</section>
"""
    return page("CNY to USD for US citizens", "index.html", body, "Lawful routes, verified cost components, tax/reporting distinctions and complete amount tables.")


def render_methods(procedures, sources) -> str:
    rows = []
    for m in procedures["methods"]:
        rows.append([
            link(f'category-{m["category"].replace("_","-")}.html', m["name"]),
            e(m["category"]),
            f'<span class="tag {status_class(m["status"])}">{e(m["status"].replace("_"," "))}</span>',
            e(m["limits"]),
            e("; ".join(m["pros"][:2])),
            e("; ".join(m["cons"][:2])),
            link(f'procedures.html#{method_anchor(m["id"])}', "Steps") + " · " + link(f'costs.html#{cost_anchor(m["id"])}', "Costs"),
            source_links(m["sources"][:3], sources),
        ])
    cards = "".join(
        f'<article class="card"><h3>{link(href, title)}</h3><p>{e(desc)}</p></article>'
        for _, title, href, desc in CATEGORIES
    )
    body = f"""
<p>Every method has a procedure page anchor and a 40-row cost table. Status labels distinguish verified routes, conditional routes, operator-published terms, supporting-only steps, closed-loop channels, unverified products and prohibited workarounds.</p>
<div class="card-grid">{cards}</div>
{table('All 28 methods compared', ['Method','Category','Status','Limits / eligibility','Pros','Cons','Details','Official sources'], rows)}
"""
    return page("Conversion and remittance methods", "methods.html", body, "Source-matched options, pros/cons and links to exact procedures and cost rows.")


def status_class(status: str) -> str:
    if status in {"verified_route", "operator_verified"}:
        return "good"
    if status in {"conditional", "supporting_only", "closed_loop"}:
        return "info"
    if status in {"unverified", "not_personal_route"}:
        return "mixed"
    return "bad"


def render_category(key: str, title: str, desc: str, procedures, sources) -> str:
    methods = [m for m in procedures["methods"] if m["category"] == key]
    sections = []
    for m in methods:
        pros = "".join(f"<li>{e(x)}</li>" for x in m["pros"])
        cons = "".join(f"<li>{e(x)}</li>" for x in m["cons"])
        sections.append(f"""
<article class="method-card" id="method-{e(m['id'])}">
  <h2>{e(m['name'])} <span class="tag {status_class(m['status'])}">{e(m['status'].replace('_',' '))}</span></h2>
  <p>{e(m['summary'])}</p>
  <p><strong>Eligibility:</strong> {e(m['eligibility'])}</p>
  <p><strong>Limits:</strong> {e(m['limits'])}</p>
  <div class="two-col"><div><h3>Pros</h3><ul>{pros}</ul></div><div><h3>Cons</h3><ul>{cons}</ul></div></div>
  <p>{link(f'procedures.html#{method_anchor(m["id"])}', 'Exact step-by-step procedure')} · {link(f'costs.html#{cost_anchor(m["id"])}', '40-row cost table')}</p>
  <p class="small">{source_links(m['sources'], sources)}</p>
</article>""")
    body = f"<p>{e(desc)}</p>{''.join(sections)}"
    return page(title, "methods.html", body, "Category subpage with source-linked method summaries.")


def render_costs(procedures, costs, sources) -> str:
    rows_by_method = {}
    for row in costs["rows"]:
        rows_by_method.setdefault(row["method_id"], []).append(row)
    sections = []
    jump = " · ".join(link(f'#{cost_anchor(m["id"])}', m["name"]) for m in procedures["methods"])
    for m in procedures["methods"]:
        rows = []
        for r in rows_by_method[m["id"]]:
            rows.append([
                f'<span data-amount="{r["amount_usd"]}">USD {r["amount_usd"]:,}</span>',
                e(r["feasibility_note"]),
                blank_cell("FX spread USD"),
                blank_cell("Conversion fee USD"),
                blank_cell("Transfer fee USD"),
                blank_cell("Routing/receiving USD"),
                blank_cell("Tax USD"),
                blank_cell("Reporting preparation USD"),
                blank_cell("All-in cost USD"),
                blank_cell("Net USD"),
                link(r["source_url"], r["source_title"], "source"),
            ])
        sections.append(f"""
<details class="cost-method" id="{cost_anchor(m['id'])}" open>
<summary>{e(m['name'])} <span class="tag {status_class(m['status'])}">{e(m['status'].replace('_',' '))}</span></summary>
<p>{e(m['summary'])}</p>
<p><strong>Published components:</strong> {e(rows_by_method[m['id']][0]['published_components'])}</p>
<p><strong>Formula:</strong> <code>{e(rows_by_method[m['id']][0]['formula'])}</code></p>
<p class="small">Blank numeric USD cells are unverified and flagged; they are not zero. {link('flagged.html', 'Flag register')} · {link(f'procedures.html#{method_anchor(m["id"])}', 'Procedure')}</p>
{table(f'USD 10,000–400,000 cost rows for {m["name"]}', ['Gross USD target','Feasibility / conditions','FX spread USD','Conversion fee USD','Transfer fee USD','Routing/receiving USD','Tax USD','Reporting prep USD','All-in cost USD','Net USD','Official source'], rows, cost_method=m['id'])}
</details>""")
    body = f"""
<p>{e(costs['numeric_policy'])}</p>
<p>{link('costs.csv', 'Download complete CSV (1,120 rows)')} · {link('research/costs.json', 'Canonical JSON')} · {link('research/costs.csv', 'Research CSV copy')}</p>
<nav class="jump" aria-label="Cost table jump links">{jump}</nav>
{''.join(sections)}
"""
    return page("Cost tables: USD 10,000–400,000", "costs.html", body, "40 rows for every method. Unknown numeric values remain blank and flagged.")


def render_procedures(procedures, sources) -> str:
    sections = []
    for m in procedures["methods"]:
        docs = "".join(f"<li>{e(d)}</li>" for d in m["documents"]) or "<li>No document checklist published; obtain current bank/operator requirements.</li>"
        steps = "".join(f"<li>{e(s)}</li>" for s in m["steps"])
        flags = ", ".join(link(f'flagged.html#{f}', f) for f in m["flags"]) or "None specific beyond general verification policy."
        sections.append(f"""
<section class="procedure" id="{method_anchor(m['id'])}">
  <h2>{e(m['name'])} <span class="tag {status_class(m['status'])}">{e(m['status'].replace('_',' '))}</span></h2>
  <p>{e(m['summary'])}</p>
  <p><strong>Eligibility:</strong> {e(m['eligibility'])}</p>
  <p><strong>Limits:</strong> {e(m['limits'])}</p>
  <h3>Documents / inputs</h3><ul>{docs}</ul>
  <h3>Exact steps</h3><ol>{steps}</ol>
  <p><strong>Flags:</strong> {flags}</p>
  <p>{link(f'costs.html#{cost_anchor(m["id"])}', 'Cost table')} · {link(f'category-{m["category"].replace("_","-")}.html', 'Category page')}</p>
  <p class="small">{source_links(m['sources'], sources)}</p>
</section>""")
    return page("Step-by-step procedures", "procedures.html", "".join(sections), "Procedures are source-matched; they do not authorize quota evasion or false documents.")


def render_taxes(findings, sources) -> str:
    tax_rows = [[e(r["item"]), e(r["china"]), e(r["us"]), blank_cell("Personal tax USD"), source_links(r["sources"], sources)] for r in findings["tax_matrix"]]
    report_rows = [[e(r["form"]), e(r["trigger"]), e(r["filing"]), e(r["penalty"]), source_links(r["sources"], sources)] for r in findings["reporting"]]
    relief = "".join(f"<li>{e(x)}</li>" for x in findings["legitimate_cost_reduction"])
    body = f"""
<section class="callout info"><h2>Core distinction</h2><p>Moving previously reported principal is not a second income item, but underlying income/gain and CNY disposition can still matter. Reporting forms are not transfer taxes. Numeric personal tax remains blank without residence, income, basis, treaty and state facts.</p><p class="small">{source_links(['irs_worldwide','irc_988','cn_iit'], sources)}</p></section>
<h2>China / US tax matrix</h2>
{table('Tax treatment by item', ['Item','China rule','US rule','Personal tax USD','Official sources'], tax_rows)}
<h2>Reporting forms and triggers</h2>
{table('US reporting and border declarations', ['Form / declaration','Trigger','Filing','Penalty / consequence','Official sources'], report_rows)}
<h2>Legitimate ways to reduce cost and risk</h2><ul>{relief}</ul>
"""
    return page("Tax and reporting obligations", "taxes.html", body, "Federal US analysis plus China tax rules; not a personalized tax opinion.")


def render_penalties(findings, sources) -> str:
    china_rows = [
        ["Foreign-exchange evasion", "Repatriation order; ordinarily up to 30% fine; serious cases 30%–100%; possible criminal liability", "Not a transfer fee; depends on violation and seriousness", source_links(["safe_fx_reg"], sources)],
        ["Illegal/disguised/illegal FX trading", "Confiscation; ordinarily up to 30%; serious cases 30%–100%; possible criminal liability", "Underground matchers and unauthorized exchange business", source_links(["safe_fx_reg", "pboc_crypto_2026"], sources)],
        ["False-document FX purchase", "Similar evasion/false-document penalty bands", "Fake invoices or distorted trade documents", source_links(["safe_fx_reg", "safe_rules"], sources)],
        ["Cash-export violation", "Warning and up to 20% fine under cited Regulations", "Customs/permit rules are separate from tax", source_links(["safe_fx_reg", "china_customs"], sources)],
    ]
    us_rows = [[e(r["form"]), e(r["trigger"]), e(r["penalty"]), source_links(r["sources"], sources)] for r in findings["reporting"]]
    body = f"""
<section class="callout warn"><h2>Penalties are not prices</h2><p>Lawful transfer budgeting should include FX friction, published fees, routing/receiving charges, professional preparation and actual tax. Statutory penalties are sanctions for violations or reporting failures, not expected costs of a lawful route.</p></section>
<h2>China-side sanctions</h2>
{table('China FX violation penalties', ['Violation','Penalty framework','Distinction','Official sources'], china_rows)}
<h2>US reporting / border consequences</h2>
{table('US reporting penalties and consequences', ['Form / declaration','Trigger','Penalty / consequence','Official sources'], us_rows)}
<h2>Corrected legacy errors</h2>
<ul>
<li>Removed unsupported 30%–300% and 30%–500% fine multipliers. {source_links(['safe_fx_reg'], sources)}</li>
<li>Removed blanket “no US tax” and “no China tax” claims. {source_links(['irs_worldwide','irc_988','cn_iit'], sources)}</li>
<li>Removed invented 1%–3% FX spread and USD 15–50 wire estimates. {source_links(['boc_tariff','wise_pricing'], sources)}</li>
</ul>
"""
    return page("Penalty breakdown", "penalties.html", body, "Separate transfer fees/FX friction from actual taxes and reporting penalties.")


def render_sources(registry) -> str:
    rows = []
    failed = []
    for s in registry["sources"]:
        if s.get("access") == "not_found":
            failed.append(f'<li>{e(s["publisher"])} — {e(s["title"])}: attempted URL <code>{e(s["url"])}</code> returned 404; not used as a verified route source.</li>')
            continue
        rows.append([
            link(s["url"], s["title"], "source"),
            e(s["publisher"]),
            e(s["type"]),
            e(s.get("access", "")),
            e(s.get("locator", "")),
            e(s.get("establishes", "")),
            e(s.get("caveat", "")),
        ])
    body = f"""
<p>{e(registry['policy'])}</p>
{table('Source registry', ['Source','Publisher','Type','Access status','Locator','What it establishes','Caveat'], rows)}
<h2>Failed fetches / unverified attempts</h2><ul>{''.join(failed) or '<li>None recorded.</li>'}</ul>
"""
    return page("Sources and verification registry", "sources.html", body, "Primary government/regulator sources establish law; operator pages establish published product terms only.")


def render_flagged(findings, sources) -> str:
    rows = []
    for f in findings["open_flags"]:
        rows.append([
            f'<span id="{e(f["id"])}">{e(f["item"])}</span>',
            e(f["reason"]),
            e(f["action"]),
            source_links(f["sources"], sources),
        ])
    body = f"""
<p>Flags do not block publication. They prevent guessed values from being presented as verified. Numeric cells affected by these flags remain blank in the cost tables and CSV.</p>
{table('Flagged for Review register', ['Item','Why unverified / conditional','Published treatment / next check','Official sources'], rows)}
<p>{link('audit.html', 'See legacy irregularities and line-by-line audit')}</p>
"""
    return page("Flagged for Review", "flagged.html", body, "Unverified values, stale terms, local implementation gaps and personal-fact dependencies.")


def render_audit(sources) -> str:
    audit = load("research/audit/issues.json")
    rows = []
    for i in audit["issues"]:
        rows.append([
            e(i["id"]),
            f'<span class="tag { "bad" if i["severity"] in {"critical","high"} else "mixed" }">{e(i["severity"])}</span>',
            e(i["title"]),
            e(", ".join(i["files"])),
            e(i["correction"]),
            source_links(i["sources"], sources),
        ])
    body = f"""
<p>{e(audit['method'])}</p>
<p>Baseline commit: <code>{e(audit['baseline_commit'])}</code>. Coverage: 1,344 lines across 10 baseline files; 776 content lines mapped to issues. {link('research/audit/line_audit.csv', 'Download full line audit CSV')} · {link('research/audit/issues.json', 'Issue JSON')}</p>
{table('Legacy audit issues and corrections', ['ID','Severity','Issue','Files','Correction','Official sources'], rows)}
"""
    return page("Line-by-line legacy audit", "audit.html", body, "Independent re-audit; prior done/verified labels were not treated as evidence.")


def render_verification() -> str:
    body = f"""
<h2>Reproducible local commands</h2>
<pre><code>python scripts/build_data.py
python scripts/build_site.py
python -m unittest discover -s tests -v
python scripts/check_site.py</code></pre>
<h2>Checks enforced</h2>
<ul>
<li>28 methods × 40 amounts = 1,120 cost rows; exact USD 10,000–400,000 grid.</li>
<li>Unknown numeric USD costs remain null/empty; every row has a registered official source URL.</li>
<li>Canonical JSON/CSV reproducibility; 1,344-line legacy audit coverage.</li>
<li>Local links and anchors, source-required table rows, one h1, landmarks, skip link, table captions, th scope, no JavaScript dependency.</li>
<li>Responsive CSS rules: focus-visible, horizontal table scroll, media queries and reduced motion.</li>
</ul>
<h2>Deployment gate</h2>
<p>The GitHub Pages workflow rebuilds data and the static dashboard, runs unit tests and the full site check, then uploads/deploys only from <code>main</code>. See {link(REPO + '/actions', 'GitHub Actions')} and {link(LIVE, 'live site')}.</p>
<p>{link('VERIFICATION.md', 'Verification log')} · {link('COORDINATION.md', 'Coordination and PR/merge log')}</p>
"""
    return page("Verification and build checks", "verification.html", body, "Automated checks run before merge and before Pages deployment.")


def main() -> None:
    procedures = load("research/procedures.json")
    registry = load("research/sources/registry.json")
    findings = load("research/findings.json")
    costs = load("research/costs.json")
    sources = {s["id"]: s for s in registry["sources"]}
    pages = {
        "index.html": render_index(findings, procedures, sources),
        "methods.html": render_methods(procedures, sources),
        "costs.html": render_costs(procedures, costs, sources),
        "procedures.html": render_procedures(procedures, sources),
        "taxes.html": render_taxes(findings, sources),
        "penalties.html": render_penalties(findings, sources),
        "sources.html": render_sources(registry),
        "flagged.html": render_flagged(findings, sources),
        "audit.html": render_audit(sources),
        "verification.html": render_verification(),
    }
    for key, title, href, desc in CATEGORIES:
        pages[href] = render_category(key, title, desc, procedures, sources)
    for name, content in pages.items():
        (ROOT / name).write_text(content, encoding="utf-8")
    print(f"Wrote {len(pages)} HTML pages")


if __name__ == "__main__":
    main()
