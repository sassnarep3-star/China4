# China4 evidence desk

A static, primary-source research dashboard for lawful CNY→USD conversion and US–China tax/reporting analysis. It is designed for a US citizen holding CNY in a Chinese bank account, but distinguishes identity, source of funds, and special property routes instead of assuming one rule fits everyone.

Live deployment: **https://sassnarep3-star.github.io/China4/**

## Fresh audit (2026-11-10)

Start with **[Verified evidence brief](https://sassnarep3-star.github.io/China4/evidence.html)**: eight freshly checked rules, execution steps, explicit audit limits and 18 × 40 strictly blank current-cost rows. The blank register supersedes any interpretation of the historical scenario figures as verified executable costs. Current quote and personal-tax values could not be verified; no universal cheapest route is claimed. Review flags are linked from the global Review page. The older 52-source catalog was not independently re-verified in full in this narrow audit.

## Pages

- **Dashboard** — executive decision guidance and 18-route comparison.
- **Summary** — the executive brief: answer, key costs, route shortlist, tax boundary and eight execution steps.
- **Methods** — pros, cons, constraints, and exact procedures for each route.
- **Costs** — four 40-row matrices covering $10,000 through $400,000 in $10,000 increments, including special property routes, a statutory penalty-ceiling versus lawful-cost comparison, and corrected penalties.
- **Taxes** — China IIT, US worldwide income, FBAR, Form 8938, Form 3520, cash reporting, FEIE/FTC, treaty and filing corrections, plus a sourced 2026 illustration of what the same amount costs under different tax characters.
- **Flagged for Review** — unresolved values, irregularities and required manual verification.
- **Sources** — the full primary-source register with direct manual-review links; the count is generated from `SOURCES` so prose cannot drift.

The former `estimates.html` and `costs.html` URLs remain as compatibility redirects to the consolidated matrices, so older links do not serve conflicting figures.

Unknown institution-specific values remain blank; a dash never means zero. Historical prices and future effective dates are explicitly labeled. This is general research, not individualized legal, tax or investment advice.

## Rebuild and validate

Requires Python 3.11+ and no third-party packages:

```sh
python3 scripts/build_site.py
python3 scripts/build_evidence.py
python3 scripts/validate_site.py
python3 scripts/validate_evidence.py
```

`build_site.py` uses `Decimal` arithmetic to regenerate all seven HTML pages and `data/cost-model.json`. The validator independently recalculates the amount ladder, BOC fees/FX benchmark, conditional annual schedule and dated Wise scenarios; it also checks HTML nesting, landmarks, local links, anchors, source counts, route counts and matrix row counts. It also requires a direct source link in each table body row; this structural check does not prove that a linked source supports every claim or that external links are live.

The GitHub Actions workflow rebuilds and validates pull requests, verifies generated files are current, then deploys only the public site files from `main` to GitHub Pages.

## Local preview

```sh
python3 -m http.server 8080 --bind 0.0.0.0
```

Open `http://localhost:8080/`. No JavaScript, web fonts, cookies or runtime data requests are required.

## Evidence and model boundary

The BOC model uses the personal tariff effective 2025-11-11 and the explicitly dated BOC USD retail quote timestamped 2026-11-09 05:30 Beijing time. Because BOC's board rotates, that row is cited through BOC's official historical date query (2026-11-09, USD) instead of a page number, and the current board is cited separately as a magnitude cross-check. The query requires a captcha, so the exact dated row is not permanently retrievable from a static official URL; the inputs are preserved in `data/cost-model.json` and the limitation is published on **Flagged for Review**. Wise formulas are historical examples published 2024-11-25, not current quotes. Current provider quotes, correspondent deductions, account-specific receiving fees, underlying taxes and professional costs must be verified before execution. See the site's **Flagged for Review** page for the complete boundary.
