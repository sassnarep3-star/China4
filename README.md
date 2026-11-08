# China4 — lawful CNY-to-USD research dashboard

Static GitHub Pages dashboard for a US citizen researching lawful ways to convert/remit CNY from a mainland Chinese bank account to USD. It separates **transfer fees/FX friction**, **actual taxes**, and **reporting penalties**; unverified numeric values are blank and flagged.

Live site: <https://sassnarep3-star.github.io/China4/>

## Most important files

- `EXECUTIVE_SUMMARY.md` — source-first answer and primary links.
- `index.html` — dashboard, decision table, key numbers and category links.
- `methods.html` + `category-*.html` — 32 methods with status, pros/cons and category subpages.
- `costs.html` + `costs.csv` — 40 rows per method, USD 10,000–400,000 in USD 10,000 increments (1,280 rows).
- `procedures.html` — exact step-by-step procedures and document lists.
- `taxes.html`, `penalties.html` — tax/reporting triggers and penalty distinctions.
- `sources.html` — 60-entry source registry with publisher, locator, access status and caveats.
- `flagged.html` — unverified/conditional items left blank on purpose.
- `audit.html` + `research/audit/line_audit.csv` — independent line-by-line audit of the 1,344-line legacy baseline and 2,633-line archived main snapshot.
- `COORDINATION.md` — session claims, task status and PR/merge/deployment log.
- `VERIFICATION.md` — reproducible checks and verification policy.

## Reproduce locally

Python 3.11+; no third-party packages are required.

```bash
python scripts/build_data.py
python scripts/build_site.py
python -m unittest discover -s tests -v
python scripts/check_site.py
```

Optional local preview:

```bash
python -m http.server 8000 --bind 0.0.0.0
```

## Data policy

- Government/regulator sources establish law; operator pages establish only published product terms.
- Every cost/table row links to a registered official source.
- Unknown FX spread, routing, tax, professional costs, all-in cost and net USD are **blank**, not zero.
- Published CNY/USD components and formulas are preserved as text; no historical reference rate is used to invent a customer quote.
- Prohibited workarounds are published as risk entries, not recommendations.

## Deployment

`.github/workflows/gh-pages.yml` rebuilds data and HTML, runs unit tests and the full static site check, then deploys to GitHub Pages from `main`. The site is static HTML/CSS/CSV/JSON and does not require JavaScript for core content.

## Preserved prior work

`archive/main-98e5b00/` preserves the `origin/main` snapshot fetched during final integration (PR #14). It is not the active deliverable; see `archive/main-98e5b00/ARCHIVE_NOTICE.md` and `audit.html`.
