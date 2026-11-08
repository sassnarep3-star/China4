# Verification log

Research/build date: 2026-11-08. Branch: `arena/06824257-china4`.

## Local reproducible checks

Commands:

```bash
python scripts/build_data.py
python scripts/build_site.py
python -m unittest discover -s tests -v
python scripts/check_site.py
```

Expected results:

- 32 methods × 40 amounts = 1,280 cost rows.
- Exact USD 10,000–400,000 grid in USD 10,000 increments for every method.
- Unknown numeric USD costs remain null in JSON and empty in CSV/HTML.
- Every cost row and source-required table row has a registered official source link.
- 1,344 baseline lines across 10 files are covered by `research/audit/line_audit.csv`; 2,633 archived main snapshot lines are covered by `research/audit/main_snapshot_line_audit.csv`.
- Local links/anchors, table captions, `th scope`, landmarks, skip link, one `h1`, viewport and no-JS core content are checked.
- CSS includes focus-visible, horizontal table scrolling, mobile media queries and reduced-motion handling.

## Source verification policy

- Government/regulator publications establish legal rules.
- Operator pages establish only that operator's published product terms, not legal permission or a personalized quote.
- Failed fetches are recorded but not used as verified route sources.
- Stale/future-dated terms are flagged: PayPal C2 2021 fee schedule, BOC ATM change effective 2026-11-11, superseded foreign-individual dividend exemption FAQ.
- Unverified personal tax, FX spread, routing and all-in totals are blank, not zero.

## Deployment gate

`.github/workflows/gh-pages.yml` rebuilds data and the static dashboard, runs unit tests and the full site check, then deploys to GitHub Pages only from `main`.

## PR / merge / live log

- Coordination claim commit: `f5faf92`.
- Source registry commit: `1ef8f28`.
- Audit/findings commit: `0c15450`.
- Procedures/cost model commit: `ee4bf89`.
- Check harness/CI gate commit: `9e7b353` and follow-up `a139e1b`.
- Final integration PR/merge/deployment results are recorded in `COORDINATION.md` after the live check.
