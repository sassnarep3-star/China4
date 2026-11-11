# China4 evidence desk

A static, primary-source research dashboard for lawful CNY→USD conversion and US–China tax/reporting analysis. It is designed for a US citizen holding CNY in a Chinese bank account, but distinguishes identity, source of funds, and special property routes instead of assuming one rule fits everyone.

Live deployment: **https://sassnarep3-star.github.io/China4/**

## Tariff effective-date update (2026-11-11)

Re-read [BOC’s official ATM notice](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html): overseas Visa/Mastercard pricing is now effective at 2.5%, minimum USD3 and maximum USD40 equivalent per withdrawal. UnionPay remains CNY12 + 1%, capped at CNY112. Corrected the obsolete “future” label; the dated FX model has **not** been refreshed, and these issuer fees are not all-in costs. This narrow update is not a new verification of every inherited source.

Run `python3 scripts/validate_effective_dates.py` for the rollover regression check.

## Fresh audit (2026-11-11)

Start with **[Verified evidence brief](https://sassnarep3-star.github.io/China4/evidence.html)**: eight freshly checked rules, execution steps, explicit audit limits and 18 × 40 strictly blank current-cost rows. The blank register supersedes any interpretation of the historical scenario figures as verified executable costs. Current quote and personal-tax values could not be verified; no universal cheapest route is claimed. Review flags are linked from the global Review page. The older 52-source catalog was not independently re-verified in full in this narrow audit.

The 2026-11-11 audit re-read the load-bearing sources (SAFE individual FX rules, BOC tariff and rate board, IRS FBAR and Publication 525, FinCEN FBAR, Wise CNY guide, SAFE 2022 quota clarification) and added the **[Before You Decide](https://sassnarep3-star.github.io/China4/questions.html)** checklist: fourteen decision questions with known answers, unknowns and discovery steps, a missing-information checklist, and seven sequential decision gates.

## Pages

- **Dashboard** — executive decision guidance and 18-route comparison.
- **Summary** — the executive brief: answer, key costs, route shortlist, tax boundary and eight execution steps.
- **Questions** — the before-you-decide checklist: fourteen questions with known answers, unknowns and discovery steps, plus seven sequential decision gates.
- **Method matrix** — [40-amount bank tariff and provider-cap comparison](method-matrix.html), illustrative only.
- **Treaty & filings** — [treaty relief, outbound filings, and remediation](treaty-filings.html).
- **Tax gate** — [what actually costs tax when CNY becomes USD](taxgate.html): China IIT by source of funds, the bank's tax-voucher gate, penalty arithmetic and the order to fix it in.
- **Methods** — pros, cons, constraints, and exact procedures for each route.
- **Costs** — five 40-row matrices covering $10,000 through $400,000 in $10,000 increments, including unpriced routes, special property routes and statutory penalty ceilings.
- **Taxes** — China IIT, US worldwide income, FBAR, Form 8938, Form 3520, cash reporting, FEIE/FTC, treaty and filing corrections, plus a sourced 2026 tax illustration.
- **Flagged for Review** — unresolved values, irregularities and required manual verification.
- **Sources** — the primary-source register with direct manual-review links; the count is generated from `SOURCES`.
- **Banks** — published tariffs and provider fee structures for BOC, ABC, CCB, HSBC, CMB, ICBC, SkyRemit and Wise, with eligibility boundaries and a task-17 source register.
- **Playbooks** — documented step-by-step procedures for the conditional lawful routes, each step tied to the official rule it follows.
- **Verification** — the row-by-row ledger: what was checked against which official text, what was re-derived independently, and what remains unverified.


The former `estimates.html` and `costs.html` URLs remain as compatibility redirects to the consolidated matrices, so older links do not serve conflicting figures.

Unknown institution-specific values remain blank; a dash never means zero. Historical prices and future effective dates are explicitly labeled. This is general research, not individualized legal, tax or investment advice.

## Rebuild and validate

Requires Python 3.11+ and no third-party packages:

```sh
python3 scripts/build_site.py
python3 scripts/build_evidence.py
python3 scripts/build_bank_playbooks.py
python3 scripts/build_method_treaty.py
python3 scripts/build_taxgate.py
python3 scripts/validate_site.py
python3 scripts/validate_evidence.py
python3 scripts/validate_bank_playbooks.py
python3 scripts/validate_method_treaty.py
python3 scripts/validate_taxgate.py
```

`build_site.py` uses `Decimal` arithmetic to regenerate all eight HTML pages and `data/cost-model.json`. `build_bank_playbooks.py` generates the three additive pages from `data/bank-playbooks.json`. The validators independently recalculate the amount ladder, BOC fees/FX benchmark, conditional annual schedule and published tariff scenarios; they also check HTML nesting, landmarks, local links, anchors, source counts, route counts and matrix row counts. They require a direct source link in each table body row; this structural check does not prove that a linked source supports every claim or that external links are live.

The GitHub Actions workflow rebuilds and validates pull requests and main, and checks that generated files are current. GitHub Pages is separately configured to publish the repository root from `main`; that branch deployment is not gated by this workflow, so require the PR validation to pass before merging. The root publisher also makes repository files, including data and coordination records, publicly accessible; do not commit sensitive information.

## Local preview

```sh
python3 -m http.server 8080 --bind 0.0.0.0
```

Open `http://localhost:8080/`. No JavaScript, web fonts, cookies or runtime data requests are required.

## Evidence and model boundary

The BOC model uses the personal tariff effective 2025-11-11 and the explicitly dated BOC USD retail quote timestamped 2026-11-09 05:30 Beijing time. Because BOC's board rotates, that row is cited through BOC's official historical date query (2026-11-09, USD) instead of a page number, and the current board is cited separately as a magnitude cross-check. The query requires a captcha, so the exact dated row is not permanently retrievable from a static official URL; the inputs are preserved in `data/cost-model.json` and the limitation is published on **Flagged for Review**. Wise examples published in 2024 do not establish current prices, so the cost cells are blank. Current provider quotes, correspondent deductions, account-specific receiving fees, underlying taxes and professional costs must be verified before execution. Wise fees are deducted from CNY before conversion; compare quotes for the same net USD payout. See the site's **Flagged for Review** page for the complete boundary.
