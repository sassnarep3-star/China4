# Coordination board

Session identifier: `97c2d0a5` (Arena branch `arena/97c2d0a5-china4`). The branch is fixed by the Arena workspace; per-session branch instructions cannot be followed without leaving the tracked branch.

| Task | Status | Owner | File scope |
|---|---|---|---|
| Official-source research: lawful CNY-to-USD/remittance paths, applicable tax distinctions, controls, costs, and flags | done | 97c2d0a5 | `research/` |
| Final integration: dashboard, categorized tables, executive summary, flagged-review page, build/link verification, GitHub Pages workflow | in progress | 97c2d0a5 | `index.html`, `assets/`, `data/`, `.github/`, `README.md`, `routes/`, `tax/`, `requirements/`, `sources/`, `review/`, `research/findings.md` (source-link correction during integration re-verification) |

## Activity log

- 2026-11-07 — Initialized board after confirming no existing coordination file, claims, or competing work in repository. Owner is using the required Arena-tracked branch; no other active task claims are present. Research claim was limited to `research/`.
- 2026-11-07 — Research completed in `research/findings.md`. Sources checked directly at official SAFE, State Taxation Administration, China Customs, IRS, FinCEN, and U.S. Government Publishing Office pages. Verified key items include the USD 50,000 personal FX facilitation threshold (not a hard ceiling for authentic documented current-account transactions), anti-splitting rules, individual income tax categories/residency, U.S. worldwide income/foreign tax credit/FBAR/Form 8938, FX gain rules, and physical-cash requirements. All 12 route rows link to official sources. Unverified bank-specific fees, conversion quote, taxpayer liability, account eligibility, and current interpretation of older SAFE rules are left blank and listed for review. Source/date/verification notes and the full official source register are in `research/findings.md`.
- 2026-11-07 — No other task claims existed. Final integration claimed by the same session after research completion; site/data/build scope is separate from `research/`.
- 2026-11-07 — During final line-by-line re-verification, removed an unrelated 2010 SAFE page previously matched to unused-RMB card-search text and replaced it with a directly verified 2026 SAFE Tianjin FAQ covering the 24-month original-receipt reconversion rule and its small-amount ID-only cases. The unrelated citation is not in the deliverable. Integration scope now includes that single research-file citation correction.
- 2026-11-07 — Implemented responsive static dashboard, 12 source-linked routes, China/U.S. tax and blank cost ledgers, document checklist, source register and Flagged for Review page. Local validation passed: all six HTML pages have working internal links, JSON parses, all data rows contain official-domain sources, and unverified cost amounts remain blank. GitHub Actions includes verification and Pages deployment; live deployment is pending PR merge and the Pages run.
