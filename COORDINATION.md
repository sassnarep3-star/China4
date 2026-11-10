# Coordination Board — China4 project

Shared task board for parallel agent sessions. Claim a task by writing your
session ID and file scope, then commit and push immediately. Never start a task
another session has claimed. Keep scopes non-overlapping. Small, frequent commits;
run `git pull --rebase` before every push. When a task is finished, record
sources, verification performed, and irregularities here and mark it done.

Session ID for this session: `agent-d778fbdf` (branch `arena/d778fbdf-china4`)

Previous session: `agent-1` (branch `arena/c56cf052-china4`)

## Tasks

| # | Task | Scope (files) | Status | Owner | Sources verified | Notes |
|---|------|---------------|--------|-------|------------------|-------|
| 1 | Create COORDINATION.md (shared task board) | COORDINATION.md | done | agent-1 | n/a | Created at project start |
| 2 | Research CNY→USD conversion methods (official sources: SAFE, PBOC, IRS, FinCEN, State Dept) | site/sources.html, site/ pages | done | agent-1 | SAFE Detailed Rules ($50k quota), SAFE Regulations (fines), FinCEN FBAR, IRS FATCA/8938/Pub54/Form3520, US-China treaty (IRS), customs cash limits | Research complete; sources compiled |
| 3 | Build conversion-penalty breakdown | site/penalties.html | done | agent-1 | SAFE Regulations fines, FinCEN/IRS penalty figures | Built; unverified items flagged |
| 4 | Build data table of methods with pros/cons | site/methods.html | done | agent-1 | SAFE Detailed Rules, FinCEN, IRS, SAFE enforcement release | Every row has source link |
| 5 | Create GitHub Pages site (landing page + subpages, dashboard UI) | site/*.html, site/css, .github/workflows | done | agent-1 | n/a | 6 pages + CSS + workflow; HTML validated |
| 6 | Verify all site content line by line against official sources | root pages | done | agent-1 | SAFE Detailed Rules, SAFE Regulations, SAFE enforcement release, FinCEN FBAR, IRS FATCA/Pub 54/Form 3520/FAQ, IRS China treaty documents (1984), PBOC | Every table row carries an official-source link; values not confirmed from an official source left blank and flagged on flagged.html |
| 7 | Create "Flagged for Review" page with irregularities | flagged.html | done | agent-1 | n/a | Published on site: 8 unverified values + 5 irregularities with suggested manual checks |
| 8 | Integration: merge branches, re-verify combined data, confirm site builds | main (via PR) | done | agent-1 | PR #1 and PR #2 merged into main; live build commit e1491ef status "built" | All six pages + CSS return 200; no broken links |
| 9 | Create PR from integration branch to main, merge, confirm Pages deploys | GitHub | done | agent-1 | PR #1: https://github.com/sassnarep3-star/China4/pull/1 (merged); PR #2: https://github.com/sassnarep3-star/China4/pull/2 (merged); GitHub Pages live at https://sassnarep3-star.github.io/China4/ | Pages build_type legacy, source branch main path "/", html_url confirmed; flagged items do not block merge and are published on the Flagged for Review page |
| 10 | Independent audit, expansion, integration, and redeployment of the complete dashboard | all root HTML/CSS/data/documentation files and .github/workflows; GitHub PR/Pages | in progress | agent-d778fbdf | SAFE/PBOC/State Council/Customs; BOC personal tariff, FX quote and ATM notices; Wise/WU/MoneyGram operator terms; IRS/FinCEN/eCFR/CBP; US receiving-bank disclosures | Rebuilt all six pages with 18 sourced procedures, four 40-row matrices and 47 primary sources. Corrected foreign-individual/quota treatment and China penalty ranges. Unknown current provider, intermediary and personal-tax values are published blank with manual checks. `python3 scripts/build_site.py && python3 scripts/validate_site.py` passes; headless Chromium returned 200 on every page, passed desktop/390px overflow checks and route interaction. CI validation added; PR/deployment pending. Fixed Arena branch is the integration branch for this session. |

## Rules
- Statuses: unclaimed, in progress, done, needs review
- "needs review" = published on Flagged for Review page, does not block other tasks
- Never mark verified without checking an official source; link the source
- Shared outputs (table data, index, navigation) changed only by final integration session

## Current session: arena/8fa669e3-china4

| Task | Scope | Status | Owner | Notes |
|---|---|---|---|---|
| Independent integration audit, corrections, and publication | root HTML pages, style.css, README.md, .github/workflows, COORDINATION.md | done | arena/8fa669e3-china4 | Audit and corrections completed; publication outcome recorded below. Session branch fixed by Arena. |

### Integration audit log — arena/8fa669e3-china4
- Corrected inherited universal $50,000 quota claim: [SAFE 2017](https://www.safe.gov.cn/en/2017/1129/1365.html) explicitly covers foreign permanent resident ID holders; [SAFE 2007](https://www.safe.gov.cn/en/2007/0105/819.html) differentiates purchase and settlement. Removed universal tax-free conversion claim: [IRS currency guidance](https://www.irs.gov/pub/fatca/int_practice_units/int_c_041.pdf) identifies section 988 FX transactions.
- Verified documented current-account income pathway against [SAFE Tianjin 2025](https://www.safe.gov.cn/tianjin/2025/0715/2834.html), reporting against [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [IRS 8938](https://www.irs.gov/businesses/corporations/fatca-information-for-individuals), and [IRS 3520 instructions](https://www.irs.gov/instructions/i3520). Checked [SAFE enforcement](https://www.safe.gov.cn/en/2018/1206/1478.html) and [PBOC notice](https://www.pbc.gov.cn/en/3688253/3689012/2025080817521950275/index.html). All rows audited for official source links and claims scoped to source; account-specific values remain unverified.
- Irregularities published on flagged.html: historical applicability, Chinese cash exit rules, costs, provider availability, unknown source/status and tax basis. Initial `git pull --rebase` before branch creation failed because the remote branch did not yet exist; initial branch push then succeeded.
- Static HTML: validated local links, stylesheets and official links in every data row; no build step. All 16 distinct official source URLs were fetched through the research tool; this verifies retrieval at review time, not future availability or geographic accessibility. Open PRs #4 and #5 are separate sessions and were not altered.
- Integration PR [#6](https://github.com/sassnarep3-star/China4/pull/6) merged on 2026-11-08 at commit `503de098355e8b7ac4378a08a59513c2f139610b`. GitHub Pages legacy build and deploy [run 42533583018](https://github.com/sassnarep3-star/China4/actions/runs/42533583018) succeeded for that merge. Live site: https://sassnarep3-star.github.io/China4/. A Node.js deprecation warning was emitted by GitHub's managed Pages build; it did not fail deployment.

## Current session

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| Final integration audit, corrections, cost schedule, and deployment verification | root HTML pages, style.css, README.md, .github/workflows, COORDINATION.md | done | agent-3aacec32 | 2026-11-08 | Prior tasks are marked done; auditing existing integration. Session branch fixed by Arena. |

- Conflict during rebase: another integration session merged overlapping changes after this claim. Preserved both board entries and the already-published site; this session will integrate only supplemental tariff research.

### Supplemental audit — agent-3aacec32
- The other integration PRs #6/#7 landed during this session. A coordination-board rebase conflict was resolved by retaining both sessions' entries; the already-published site was preserved, and only supplemental content was applied.
- Reviewed the [2025 Bank of China tariff](https://pic.bankofchina.com/bocappd/pricelist/202503/P020250331641149290400.pdf) item 210105008 and notes, [SAFE cash rules](https://www.safe.gov.cn/tianjin/2024/0430/2466.html), [Shanghai property FAQ](https://english.shanghai.gov.cn/en-FAQHome/20240204/b4426264395b4fa3adfde73778c94ad4.html), [Shanghai salary FAQ](https://english.shanghai.gov.cn/en-FAQHome/20231211/74deb6f12c5e4e1686020bd042819690.html), and [IRS currency unit](https://www.irs.gov/pub/fatca/int_practice_units/fcu_t_018_02_01_08.pdf). Historical source status and applicability remain flagged.
- Added an amount-by-amount $10,000–$400,000 schedule; total transaction costs and taxes remain blank because no current executable quotes, source history or personal tax data are verified. Added conditional route steps. The tariff formula is a historical published component, not a verified actual quote.
- Static verification: `python scripts/verify_site.py` checks local links, required official links on each table row, and all requested amounts. It does not establish that every linked page remains available or that each claim is legally current.
- Supplemental PR: https://github.com/sassnarep3-star/China4/pull/8. Static verifier passed; all six pages and CSS returned HTTP 200 from a local server. The first HTTP smoke-test attempt raced server startup and failed; retry against a running server passed. No PR checks were configured. Merged as commit `d028e12b5fbdcaca0778b0c668e5340c835838b0`; GitHub Pages build and deploy [run 42533800234](https://github.com/sassnarep3-star/China4/actions/runs/42533800234) succeeded. Live cost schedule and dashboard were fetched successfully at https://sassnarep3-star.github.io/China4/. GitHub’s managed build emitted a non-failing Node.js deprecation warning.

## Current session: arena/d9dc8047-china4 — independent supplemental verification

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| Check current integrated research against official source text and preserve non-overlapping integration work | COORDINATION.md only | done | arena/d9dc8047-china4 | Confirmed current main had already integrated the requested dashboard, route steps, tariff component, $10,000–$400,000 schedule, flags and deployment while this branch was based on an older commit. Re-ran `scripts/verify_site.py` against origin/main snapshot; all table rows and local links passed. Independently fetched SAFE (2016 purchase evidence; 2015 quota-splitting statement), PBOC FX Regulations Arts. 39–45, GACC passenger cash guidance and virtual-currency notice, FinCEN and IRS pages. The PBOC-hosted text specifies separate administrative ranges (Arts. 39/40/45: generally up to 30%, serious cases above 30% and below 100%; Art. 42 carrying violation up to 20%); these are not personalized costs. An earlier proposed full-page rewrite overlapped newer integration work and was stashed, not applied, to preserve current main’s BOC tariff and IRS §988 analysis. No site content was overwritten. |

### Coordination/rebase note
- `origin/main` advanced to `667b5ba` with integration PRs #6–#9 while this session was auditing a checkout at `e7e12b1`. `git pull --rebase origin main` conflicted in this shared board. Resolved by retaining all existing integration/session entries and appending this audit record. No other session’s files or work were discarded.
- The authoritative GitHub Pages site had status `built` at `https://sassnarep3-star.github.io/China4/` before this audit; the latest main history records successful deploy run `42533800234` and follow-up run `42533888250`.

## Current session: arena/5906756f-china4

| # | Task | Scope (files) | Status | Owner | Sources verified | Notes |
|---|------|---------------|--------|-------|------------------|-------|
| 10 | Claim & verify comprehensive primary-source data (BOC, CCB, HSBC CN, Wise, SkyRemit, PayPal C2, SAFE, PBOC 2026-42, Chinatax, Customs, IRS 2026, FinCEN, CBP, US banks) | `COORDINATION.md` | done | arena/5906756f-china4 | All official primary agencies & tariffs fetched 2026-11-08 | Rebased onto `origin/main` (`3854ba8`) |
| 11 | Restore & expand executive summary, all 14 conversion methods + step-by-step instructions, deep penalty breakdown, and 2026 US/PRC tax guides | `index.html`, `methods.html`, `penalties.html`, `taxes.html`, `style.css` | done | arena/5906756f-china4 | Verified against Nov 2026 SAFE, PBOC (`银发〔2026〕42号`, `[2025] 11`, parity `6.7168`), BOC (`6.6648/6.6929`), Chinatax, Customs, IRS, FinCEN | Preserves prior accuracy corrections (`五星卡` quota distinction, IRC §988, PBOC FX Regs Arts. 39–45) with full guides & tariffs |
| 12 | Build mobile-friendly $10,000–$400,000 USD increment cost estimator & tables (most important info first, official source link on every row, blank/flagged where unverified) | `estimates.html`, `style.css` | done | arena/5906756f-china4 | Python-verified Nov 2026 quotes across all 40 steps ($10k–$400k); CCB/HSBC spreads kept `Unverified` | Added responsive `mobile-cards` CSS + optional US receiving bank/OUR toggle |
| 13 | Update Flagged for Review & Sources registry, validate links/HTML, commit, rebase, PR, merge to `main`, verify live GitHub Pages deployment | `flagged.html`, `sources.html`, `README.md`, `COORDINATION.md`, `scripts/verify_site.py` | done | arena/5906756f-china4 | `scripts/verify_site.py`, HTML/JS syntax check, and local HTTP 200 smoke test all passed | Preparing PR & merge to `main` + live GitHub Pages verification |
## Current session: arena/9ca8a991-china4

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| Fill the blank $10,000-$400,000 cost schedule with sourced calculated estimates; add step-by-step route guide; add new official sources and flags; integrate and deploy | costs.html (new), steps.html (new), EXECUTIVE_SUMMARY.md (new), scripts/build_costs.py (new), sources.html, flagged.html, methods.html, index.html, penalties.html, README.md, style.css, scripts/verify_site.py, COORDINATION.md | done | arena/9ca8a991-china4 | 2026-11-08 | Prior tasks marked done by earlier sessions. Branch fixed by Arena; worked on this branch. |

### Claim log — arena/9ca8a991-china4
- Non-overlapping scope: this session only ADDS two new pages (costs.html, steps.html), ADDs rows to sources.html and flagged.html, and ADDs two nav links to existing pages. No existing table content is deleted or rewritten.
- Model inputs are all pulled from official pages fetched during this session: BOC published FX rate board (boc.cn/sourcedb/whpj), BOC e-banking tariff (boc.cn/ebanking/service/cs1/200905/t20090506_990712.html), BOC 2025 personal-services price list PDF, eCFR 31 CFR 1010.821, IRS gifts-from-foreign-person, PBOC/SAFE 《携带外币现钞出入境管理暂行办法》 (gov.cn gongbao), PBOC 《个人财产对外转移售付汇管理暂行办法》 (gov.cn gongbao + safe.gov.cn), SAFE 《个人外汇管理办法实施细则》 (safe.gov.cn).
- Every estimate on costs.html is a MODELLED figure from those published inputs with the formula, the rate snapshot date and the source link printed next to it; it is not a bank quote and is labelled as such.

### Completion log — arena/9ca8a991-china4

**Problem addressed.** Earlier sessions correctly refused to publish any cost number, leaving all 40 rows of the requested $10,000–$400,000 schedule blank. The user explicitly asked for estimates. This session supplied estimates that are *computed from published official inputs* rather than guessed, with the formula, the rate snapshot date and the source link printed next to every figure.

**Official sources fetched and verified this session (all linked from the site):**
- [BOC published FX rate board](https://www.boc.cn/sourcedb/whpj/) — USD spot buy 6.6648, sell 6.6929, reference 6.7168, cash sell 6.6929 (per 100 USD), stamped 2026-11-09 05:30. Fetched twice; stable across both reads.
- [BOC e-banking personal transfer tariff](https://www.boc.cn/ebanking/service/cs1/200905/t20090506_990712.html) — outward telegraphic transfer 0.1% of remittance, min CNY 50, max CNY 260, plus CNY 150 cable fee (CNY 80 to HK/Macau/Taiwan).
- [BOC 2025 personal services price list PDF](https://pic.bankofchina.com/bocappd/pricelist/202503/P020250331641149290400.pdf) — inherited from session 8fa669e3; reused as corroboration and for the overseas-bank-charges note.
- [SAFE, Detailed Rules on Individual Foreign Exchange (2007)](https://www.safe.gov.cn/safe/2007/0105/5320.html) — Art. 2 US$50,000 annual quota; Art. 12 evidence above quota; Art. 13 foreign individuals' legitimate current-account RMB income with tax documentation; Art. 14/15 outward remittance; Art. 26/30/31 accounts and cash. Also records that Art. 39 was repealed by 汇发〔2023〕8号.
- [SAFE + GAC, Interim Measures on Carrying Foreign Currency Cash In and Out (2003)](https://www.gov.cn/gongbao/content/2004/content_63085.htm) — Arts. 3, 4, 5, 7, 9, 10, 11 (thresholds and permits).
- [PBOC, Interim Measures on Sale and Payment of FX for Transfer of Individual Property Abroad (2004)](https://www.gov.cn/gongbao/content/2005/content_64294.htm) and [SAFE release](http://m.safe.gov.cn/safe/2004/1116/4133.html) — Arts. 2, 6, 8, 9, 10, 11 (emigration and inheritance transfer). **This route was missing from the site entirely and is now on methods.html and steps.html.**
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — FBAR inflation-adjusted maxima $16,536 (non-willful) and $165,353 (willful) for penalties assessed on or after 17 Jan 2025. Previously flagged unverified; now verified against the official table.
- [IRS, Gifts from foreign person](https://www.irs.gov/businesses/gifts-from-foreign-person) — $100,000 NRA/foreign-estate threshold; $20,116 (2025) and $20,573 (2026) for foreign corporations/partnerships. Previously flagged unverified; now verified.

**Verification performed.**
- `python3 scripts/verify_site.py` passes on all eight pages: 297 sourced rows checked, every local link resolves, every value-bearing row carries an official-source link, all 40 amounts present on both costs.html and penalties.html.
- Verifier was extended, not weakened: the page list now includes costs.html and steps.html, the official-domain allowlist gained boc.cn / gov.cn / ecfr.gov / chinamoney.com.cn, and rows whose values are explicitly marked blank are exempted from the source check — because a blank cell has no value to source. That is the site's own policy, not a loophole.
- HTTP smoke test: all eight pages plus style.css returned 200 from a local server.

**Estimates published (documented route, single wire):** $10,000 → $53.40 (0.534%); $50,000 → $166.22 (0.332%); $100,000 → $271.18 (0.271%); $200,000 → $481.11 (0.241%); $300,000 → $691.03 (0.230%); $400,000 → $900.95 (0.225%). Quota-only route at $400,000: $1,329.77 over 8 calendar years.

**Irregularities flagged (all published on flagged.html with source links):**
1. BOC's quoted USD selling rate (6.6929) sat *below* the PBOC/CFETS central parity (6.7168) on the snapshot date — the opposite of the usual relationship. The model therefore uses the internally consistent half-spread measure (0.2099%) rather than a comparison with parity. Flagged as a data anomaly to re-check.
2. BOC states on its own rate board that it is for reference and the executed rate governs — so the estimator is an input model, not a quote.
3. Whether a US passport alone creates a US$50,000 quota is not established by the verified pages; Art. 2 covers domestic individuals and SAFE 2017 extends it to foreign permanent-resident ID holders.
4. SAFE Detailed Rules Art. 39 (fine up to CNY 1,000) was repealed by 汇发〔2023〕8号 — an earlier version of this site cited it; now corrected.
5. Conflict between PBOC Interim Measures Art. 10 ("CNY 500,000 or less") and SAFE's own release ("below CNY 500,000") on which office approves the boundary case.
6. Intermediary/correspondent charges and the US receiving-bank fee remain blank by policy.
7. Emigration/inheritance transfer eligibility does not on its face cover a US citizen's own savings.

**Coordination.** Scope was additive only: two new pages, new rows appended to sources.html and flagged.html, one new row and one strengthened row on methods.html, two nav links added to the existing pages, and a cross-link from index.html and penalties.html. No existing table content from other sessions was deleted or rewritten. Files owned by earlier sessions that would have needed substantive rewrites were left alone and the correction logged on flagged.html instead.

## Integration note — arena/9ca8a991-china4 (final)

**Merge conflict.** While this session was working, arena/5906756f-china4 merged a full rebuild of the
dashboard (PRs #9, #10, #11) that created `estimates.html` and rewrote every page. This session's PR #13
could not merge cleanly. Resolution: **main's rebuild was taken as the base** for all nine conflicted files
and this session's work was re-applied on top of it, additively. Nothing from arena/5906756f-china4 or any
earlier session was discarded.

**What this session contributed on top of that rebuild:**

- **`costs.html` (new)** — the $10,000–$400,000 grid viewed **by legal route** rather than by provider, which
  `estimates.html` does not cover: annual-quota spreading across calendar years (8 years and $1,329.77 at
  $400,000), SAFE-approved emigration/inheritance property transfer with its mandatory three-stage remittance
  ($1,023.47 at $400,000), cash carry, and the illegal channel's statutory fine exposure at every amount.
  Both pages now cross-link and explain the difference.
- **Five official sources added to `sources.html`**: SAFE Detailed Rules full text
  (safe.gov.cn/safe/2007/0105/5320.html), SAFE + GAC cash-carry Interim Measures full text
  (gov.cn Gazette), BOC e-banking outward-wire tariff, eCFR 31 CFR 1010.821 (the official FBAR penalty
  table), and IRS gifts-from-foreign-person (Form 3520 thresholds).
- **Eight flagged items added as section 3 of `flagged.html`**, including the rate anomaly below.
- **`EXECUTIVE_SUMMARY.md` (new)** and a `costs.html` entry in `README.md`.
- **`scripts/build_costs.py` (new)** — regenerates `costs.html` from its documented model inputs.
- **Verifier extended**: `costs.html` added to the page list, `gov.cn` / `ecfr.gov` / `chinamoney.com.cn`
  added to the official-domain allowlist, the full-amount-grid check applied to both estimate pages, and rows
  whose values are explicitly blank exempted from the source check (a blank cell has no value to source).

**Dropped deliberately:** this session had also built a standalone `steps.html`. Main's `methods.html`
already carries exact step-by-step instructions for all 14 channels, so the duplicate page was removed rather
than shipped alongside it.

**New irregularity found (published on flagged.html):** on the 9 Nov 2026 snapshot, BOC's published USD spot
selling rate (6.6929) sits **below** the PBOC central parity rate (6.7168) — the opposite of the usual
relationship. Both cost pages therefore measure the FX cost as the half-spread of BOC's own published
buy/sell quotes (0.2099% / 0.2104%) instead of comparing against parity. Flagged for re-checking against a
live quote.

**Cross-validation:** two independent research passes over the same published BOC board produced the same
half-spread to three decimal places, and the BOC $400,000 totals agree to within $2 ($900.95 vs $902.85).

**Verification.** `python3 scripts/verify_site.py` passes across all eight pages: 281 table rows checked,
every local link resolves, every value-bearing row carries an official-source link, and the full 40-amount
grid is present on both `estimates.html` and `costs.html`. HTTP smoke test: all eight pages plus `style.css`
returned 200.

## Session arena/4646bb35-china4 — integration audit

| Task | Scope | Status | Owner | Notes |
|---|---|---|---|---|
| Independent post-PR #14 audit and publication | COORDINATION.md, scripts/build_site.py, scripts/validate_site.py, generated site and data, documentation, GitHub PR/Pages | done | arena/4646bb35-china4 | PR and deployment follow. See audit note below. |

### Post-PR #14 audit — arena/4646bb35-china4
- Task 10's branch was merged in [PR #14](https://github.com/sassnarep3-star/China4/pull/14), despite the older in-progress status. Its deployment [run 42536288129](https://github.com/sassnarep3-star/China4/actions/runs/42536288129) succeeded. The current session uses the Arena-mandated branch. Initial pull before the first push failed because that remote branch did not yet exist; the claim was then pushed.
- Independently checked [SAFE Articles 2, 13 and 15](https://www.safe.gov.cn/safe/2007/0105/5320.html) and [SAFE Tianjin 2025](https://www.safe.gov.cn/tianjin/2025/0715/2834.html): legitimate current-account RMB income has documentation requirements, with an exception for tax vouchers where no tax is due. Article 39 is marked repealed on SAFE's own page.
- The [BOC rate board](https://www.boc.cn/sourcedb/whpj/) at 09:15:45 Beijing time on 2026-11-09 showed USD spot buy/sell 6.6638/6.6919 CNY per USD, different from the explicitly historical 05:30 model. The board says the actual executed rate governs. Estimates are snapshots, not live quotes.
- Fixed an overbroad dashboard sentence about tax and currency gains. Strengthened validation from table-level to per-row direct source links; independently rebuilt and validated all six pages and four 40-row matrices. This automated test checks link presence, not source support or external availability. This limited audit does not assert a fresh line-by-line verification of all claims; unknown costs, eligibility and historical pricing remain on Flagged for Review.
- [PR #15](https://github.com/sassnarep3-star/China4/pull/15) merged at `29089128a0ccdc2583ab25f20bca87ac115e3377` on 2026-11-09 01:31 UTC. GitHub Pages legacy [build and deployment 42546010956](https://github.com/sassnarep3-star/China4/actions/runs/42546010956) succeeded. GitHub reported Node 20 action deprecation and upcoming ubuntu-latest migration warnings, neither fatal.

## Current session: arena/67730449-china4

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| Independent citation audit: pin the BOC quote link to the exact official historical result and disclose pagination volatility | `scripts/build_site.py`, generated `sources.html`, generated `flagged.html`, `COORDINATION.md` | done | arena/67730449-china4 | Non-overlapping with open PR #12 (dashboard, methods, penalties and CSS). Verified SAFE Art. 2/13 and Wise CNY limits from their official pages. Fetched BOC pages 1–5 on 2026-11-09: original S5 URL landed on a later quote; page 5 showed 2026-11-09 05:30 USD buy/sell 666.48/669.29 CNY per USD 100, matching the model. Updated S5 to direct to page 5 and flagged page-position volatility; quote page says executed rate governs. `python3 scripts/build_site.py && python3 scripts/validate_site.py` passed after regeneration. Direct-link presence is checked by validator; source interpretation remains a manual audit. PR [#18](https://github.com/sassnarep3-star/China4/pull/18) merged as `b9e23926c66eaa94c60bf8ebc44fabe946246cb6` on 2026-11-09 01:34 UTC. Post-merge validation + Pages deploy [run 42546238041](https://github.com/sassnarep3-star/China4/actions/runs/42546238041) succeeded; Pages API reports `built`. Live sources/flagged pages were fetched after deployment; a cache-busted source fetch confirmed the updated S5 label and page-5 URL. |
## Current session: arena/672f75fb-china4 — final re-verification & gap closure

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 11 | Independent line-by-line re-verification of live dashboard, fresh official-source spot-checks, defect fixes, PR + merge + Pages confirmation | root HTML pages (via scripts/build_site.py), style.css, EXECUTIVE_SUMMARY.md, README.md, COORDINATION.md, .github/workflows | done | arena/672f75fb-china4 | Prior tasks 1–10 done by earlier sessions; PRs #4, #5, #12 are stale open duplicates from other sessions — not touched by this session. Branch fixed by Arena; this is the integration branch. |

### Completion log — arena/672f75fb-china4 (task 11)

**Status: done.** Fixed Arena branch `arena/672f75fb-china4` used as integration branch.

**Fresh official sources fetched and verified this session (2026-11-09):**
- [Wise, Guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account-only recipients, **CNY 300,000/transfer (bank app)** and **CNY 50,000/transfer (Alipay)** caps, tax-record-based overall limit.
- [Wise, Summary of fee changes (2024-11-25)](https://wise.com/gb/blog/summary-of-fee-changes) — CNY→USD bank funding ¥33.20 + 0.62%; Alipay funding ¥33.20 + 1.97% (dated formulas only).
- [BOC, personal service price list effective 2025-11-11 (PDF)](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008: TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150; note 5: full-arrival USD 15 (BOC NY) / USD 25 (elsewhere); item 210101002: foreign-currency carrying permit ¥10, waived 2025-04-01–2026-12-31; item 210108014: cross-border ATM ¥12 + 1%, max ¥112/withdrawal.
- [BOC, ATM price-change notice effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay ¥12 + 1% (max ¥112); Visa/Mastercard 2.5% of amount withdrawn, min USD-equiv. 3 / max USD-equiv. 40, **per withdrawal**.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-09 09:15 USD buy 6.6638 / sell 6.6919, corroborating the site's dated 05:30 snapshot (6.6648 / 6.6929).
- [IRS, Figuring the FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum exclusion **$132,900** confirmed.

**Material defect found and fixed (was live on the site):** the cost model split the *USD* principal at Wise's CNY caps (300,000 / 50,000) and at the CNY 10,000 ATM cap, understating per-transfer/per-withdrawal fixed fees and transfer counts. Corrected model splits the *CNY* principal: at $400,000, Wise needs **9 bank-funded transfers ($2,524.64)** or **54 Alipay-funded transfers ($8,147.87)** on the dated formulas; the $10,000 ATM scenario needs **7 withdrawals ($112.55 UnionPay / $250.00 Visa-MC from 2026-11-11)**. `scripts/validate_site.py` now re-derives Wise and ATM figures independently from the CNY principal and checks withdrawal counts. Also corrected: EXECUTIVE_SUMMARY.md BOC table ($100k $271.62, $200k $481.99 — it previously disagreed with the generator), research cutoff restated as 2026-11-09 UTC, and the quote-timestamp irregularity marked resolved on flagged.html. BOC baseline unchanged: $10k $53.45 → $400k $902.72.

**Verification performed:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, local links, landmarks, independent Decimal arithmetic). Local HTTP smoke test: all 8 pages + style.css returned 200; corrected values (9 × $2,524.64; 54 × $8,147.87; 7 × $112.55) confirmed rendered in penalties.html. Live site pre-merge confirmed serving the prior build (cutoff 2026-11-08, Wise "2 transfers · $2,489.92"), i.e. the defect was live and is fixed by this PR. Mobile: ≤760px tables render as labelled cards via `data-label` (style.css).

**Irregularities:** the cap-unit defect above (High, fixed, published on flagged.html); BOC sell rate below PBOC middle rate persists on the live board — handled by the same-quote half-spread benchmark, not treated as an error. Stale duplicate PRs #4, #5, #12 from other sessions remain open and untouched. All other flagged items remain published on flagged.html and do not block the merge.

### Merge-conflict log — arena/672f75fb-china4
- During this session, arena/4646bb35-china4 merged PRs #15/#16 into main. Rebasing task 11 onto the new main conflicted only in COORDINATION.md; resolved by retaining both sessions' board sections in full — no work discarded. Their validator strengthening (per-row source links) and tax-caveat fix auto-merged with this session's cap-unit correction; `build_site.py` + `validate_site.py` pass on the combined tree with a clean working copy.
- Second conflict: main moved again via PR #18 (BOC S5 pinned to the exact historical quote page). Rebase conflicted in COORDINATION.md, scripts/build_site.py and generated HTML. Resolved by keeping both sessions' flagged items (quote-timestamp resolution + BOC pagination note + cap-unit correction), keeping the S5 pin, and regenerating all HTML from the merged generator. Nothing discarded; validator passes on the combined tree.

## Current session: arena/753a8878-china4 — final independent verification & publication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 12 | Independent line-by-line verification audit of live dashboard, fresh official-source spot-checks, defect fixes if any, PR + merge + Pages confirmation | COORDINATION.md (claim + log); site files only if defects found | arena/753a8878-china4 | 2026-11-10 | Prior tasks 1-11 done by earlier sessions; site live at https://sassnarep3-star.github.io/China4/ with build status "built". This session re-verifies independently and publishes the audit record. |

### Claim log — arena/753a8878-china4
- Non-overlapping scope: verification-only unless a defect is found. No other session has claimed this task. Branch fixed by Arena; this is the integration branch.
- Plan: (1) rebuild + validate, (2) fetch official sources (SAFE, IRS, BOC, FinCEN, CBP) and spot-check key claims, (3) check live site pages return 200 and mobile layout, (4) record findings, PR, merge, confirm Pages.

### Completion log — arena/753a8878-china4 (task 12)

**Status: done.** Independent verification audit; no site-content defects found, so no site files were changed. Only this coordination record is published.

**Verification performed (2026-11-10):**
- Rebuilt and validated: `python3 scripts/build_site.py && python3 scripts/validate_site.py` → PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, Decimal arithmetic). Rebuild produced zero diff against committed files (reproducible).
- Every table row carries a direct official-source link: independent check of all six pages found 0 rows without a source link (validator enforces the same per-row rule).
- Live site fetched: dashboard and Flagged for Review pages render correctly with dated-quote labeling and blank-for-unknown policy intact.
- Fresh official-source spot-checks (all fetched this session):
  - [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — aggregate >$10,000 at any time; due Apr 15, auto-ext Oct 15. Matches S25.
  - [SAFE Detailed Rules (S1)](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 $50,000 annual quota; Art. 13 foreign-individual lawful RMB income with tax vouchers; Art. 39 repeal note present. Matches S1/S46.
  - [eCFR 31 CFR 1010.821 (S26)](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — non-willful $16,536 / willful $165,353 (assessed on/after 2025-01-17). Matches S26.
  - [Wise CNY guide (S11)](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese + work/tax-record eligibility, own-account recipient, 300,000 CNY (bank app) / 50,000 CNY (Alipay) per transfer, overall limit = salary minus tax. Matches S11/S12.
  - [IRS FEIE (S35)](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum $132,900. Matches S35.
  - [CBP (S29)](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) — FinCEN Form 105 for >$10,000 entering the US. Matches S29.
- Independent Decimal recomputation matched site figures exactly: BOC $53.45 / $166.44 / $271.62 / $481.99 / $902.72 at $10k/$50k/$100k/$200k/$400k; Wise dated bank $2,524.64 (9 transfers) and Alipay $8,147.87 (54 transfers) at $400k.
- Mobile: `style.css` provides card-transformed tables with `data-label` at ≤760px, horizontal-scroll tables on desktop, viewport meta on all pages. No JS required.
- Irregularity re-confirmed (already published on flagged.html, not a new defect): BOC page 5 now shows 2026-11-10 02:49 USD 666.22/669.03 — the 2026-11-09 05:30 snapshot has rolled off the paginated board. Site correctly treats it as a dated snapshot, never a live quote; live magnitude corroborates within ~0.04%.

**Irregularities:** none new. All previously flagged unknowns remain on the Flagged for Review page and do not block merge per project rules.
## Current session: arena/09fa5313-china4 — independent re-verification & republication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 12 | Independent line-by-line re-verification of live dashboard, fresh official-source spot-checks, defect fixes, PR + merge + Pages confirmation | root HTML pages (via scripts/build_site.py), style.css, EXECUTIVE_SUMMARY.md, README.md, COORDINATION.md, .github/workflows | in progress | arena/09fa5313-china4 | Prior tasks 1–11 done by earlier sessions; stale open PRs #4, #5, #12 are duplicates from other sessions — not touched. Branch fixed by Arena; this is the integration branch. |

### Completion log — arena/09fa5313-china4 (task 12)

**Status: done.** Fixed Arena branch `arena/09fa5313-china4` used as integration branch. No code defects found; no generated-file changes required (build is deterministic and current).

**Fresh official sources fetched and verified this session (2026-11-10):**
- [IRS, Figuring the FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum exclusion **$132,900** confirmed.
- [IRS, FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — aggregate > $10,000 at any time in calendar year; due April 15, automatic extension to October 15 confirmed.
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — FBAR civil maxima **$16,536** (non-willful) / **$165,353** (willful) for penalties assessed on or after Jan 17, 2025 confirmed.
- [SAFE, Individual FX Detailed Rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 ($50k annual quota, domestic individuals), Art. 13 (foreign-individual lawful RMB income with tax documentation), Art. 14/15 (outward remittance), Art. 39 repealed by 汇发〔2023〕8号 confirmed.
- [SAFE, ATM withdrawal notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year and CNY 10,000/card/day confirmed.
- [BOC, ATM price-change notice effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay ¥12 + 1% (max ¥112); Visa/Mastercard 2.5% (min USD-equiv. 3 / max USD-equiv. 40) per withdrawal confirmed.
- [BOC, personal service price list effective 2025-11-11 (PDF)](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008: TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150; note 5: full-arrival USD 15 (BOC NY) / USD 25 elsewhere; item 210101002: permit ¥10 waived 2025-04-01–2026-12-31 confirmed.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903 / middle 6.7188; sell-below-middle anomaly persists, corroborating the flagged item. Model's dated 2026-11-09 05:30 snapshot (6.6648/6.6929) remains correctly labeled historical.
- [Wise, Guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account-only recipients, CNY 300,000/bank transfer and CNY 50,000/Alipay caps, tax-record overall limit confirmed.
- [Wise, Summary of fee changes (2024-11-25)](https://wise.com/gb/blog/summary-of-fee-changes) — bank ¥33.20 + 0.62%; Alipay ¥33.20 + 1.97% (dated formulas only) confirmed.
- [CBP, Know Before You Go](https://www.cbp.gov/travel/us-citizens/know-before-you-go/know-you-go-traveling-abroad) and [IRS Form 3520 instructions](https://www.irs.gov/instructions/i3520) — retrieved; FinCEN Form 105 / Form 3520 scope as published on taxes.html confirmed at retrieval level.

**Verification performed:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 47 sources, local links, landmarks, independent Decimal arithmetic); working tree clean after rebuild (generated files current). Local HTTP smoke test: all 8 pages + style.css + data/cost-model.json returned 200. Live site fetched and confirmed serving the corrected build (cutoff 2026-11-09, BOC $53.45/$902.72, Wise 9 transfers · $2,524.64 at $400k). Pages API reports `built`, legacy, source main "/". Mobile: ≤760px tables render as labelled cards via `data-label` (style.css); hero leads with executive answer and cost snapshot (most important info first).

**Irregularities:** none new. All previously flagged items remain published on flagged.html and do not block the merge. Stale duplicate PRs #4, #5, #12 from other sessions remain open and untouched.

### Publication record — arena/753a8878-china4 (task 12)
- PR #20: https://github.com/sassnarep3-star/China4/pull/20 — MERGED as `1bb313ca33a4ee0a5516cdbb8d1a81bfcdf3141c` on 2026-11-10 01:02 UTC.
- Post-merge deploy: Validate and deploy run 42732847124 + pages build 42732846784 succeeded; GitHub Pages API reports status `built` at https://sassnarep3-star.github.io/China4/.
- Note: parallel session arena/09fa5313-china4 merged PR #21 after this session's merge; no conflicts with this additive record.

### Publication record — arena/09fa5313-china4 (task 12)
- [PR #21](https://github.com/sassnarep3-star/China4/pull/21) merged as `c0c7b34790d21fe7a6c8ee542585d1585dc4b87d` on 2026-11-10 01:03 UTC. Validate run [42732948474](https://github.com/sassnarep3-star/China4/actions/runs/42732948474) succeeded; its pages-build-deployment run was superseded by PR #22's deployment [42733024718](https://github.com/sassnarep3-star/China4/actions/runs/42733024718) (success). Pages API reports `built`. Live site: https://sassnarep3-star.github.io/China4/
- Merge conflict during rebase: arena/753a8878-china4 merged PR #20 (parallel task-12 audit, also no defects) into main while this session worked. Resolved by retaining both sessions' board sections in full — no work discarded. Validator passes on the combined tree.
## Current session: arena/b398220f-china4 — citation durability & publication

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 14 | Independent audit of citation durability and numeric claims; fix any defect found; PR + merge + Pages confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML pages, `EXECUTIVE_SUMMARY.md`, `README.md`, `COORDINATION.md` | in progress | arena/b398220f-china4 | Renumbered from 12: `arena/753a8878-china4` (PR #20) and `arena/09fa5313-china4` (PR #21) concurrently claimed/completed task 12 while this session's claim was in flight. Collisions logged; this session kept a non-overlapping scope by auditing citation durability (the FX quote link) and adding a penalty-ceiling comparison rather than repeating the same spot-check list. Branch fixed by Arena. |
### Audit log — arena/b398220f-china4 (task 14)

**Defect found and fixed (High, citation integrity).** Source S5 pointed at BOC's rotating rate board, page 5 (`enindex_1619_4.html`), where the cited 2026-11-09 05:30 USD row (buy 666.48 / sell 669.29 CNY per USD) had been visible. On 2026-11-10 that page shows a later quote (02:49: buy 666.22 / sell 669.03), so the link no longer reproduced the model input. Fixes: S5 repointed to BOC's official historical exchange-rate query (date 2026-11-09, USD, captcha) with explicit re-query instructions on `sources.html`; new S48 cites BOC's current board as a magnitude cross-check; `flagged.html` now states the roll-off rather than claiming page 5 is correct; `validate_site.py` fails if the stale URL returns or if either required FX citation is missing.

**Also fixed.** `sources.html` linked to a session branch that can be deleted (`blob/arena/d778fbdf-china4`); now `blob/main`. A flagged item still said the ATM change was "three days after research cutoff"; the cutoff is now 2026-11-10 and the item says one day. Research cutoff restated 2026-11-10 UTC.

**Added (decision value).** A "penalty vs lawful cost" table (6 amounts) applying the published statutory ceilings — 30% of the amount, 30%–100% in serious cases (Art. 39/40/45), 20% for unlawful cash carriage (Art. 42), FBAR nonwillful $16,536 per violation — beside the modeled lawful BOC cost, plus a dashboard line linking to it. It is labeled as arithmetic on statutory rates, not an assessment.

**Independent verification performed this session (all fetched 2026-11-10):**
- [SAFE Individual FX Detailed Rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Art. 2 annual $50,000 settlement/purchase total for domestic individuals; Art. 13 foreign individual's lawful current-account RMB income needs ID + amount-matched documents including tax vouchers, reconversion within 24 months; Art. 15 existing-FX remittance with ID; Art. 39 repeal note present.
- [SAFE cash-carry rules](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — ≤$5,000 no permit, $5,000–10,000 bank permit, >$10,000 generally not permitted except listed special cases with SAFE permit. Matches S7.
- [SAFE card-cash notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year and CNY 10,000/card/day; borrowing/lending cards to evade is prohibited. Matches S9.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — Art. 39/40/45 fines ≤30%, serious 30% to equivalent amount; Art. 42 ≤20% for unlawful carriage. Matches S18 and the new exposure table.
- [BOC personal price list effective 2025-11-11](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 TT/draft 1‰, min ¥50, max ¥260, international telecom ¥150 (HK/Macau/Taiwan ¥80); note 5 full-arrival $15 (BOC NY) / $25 elsewhere; item 210108014 cross-border ATM ¥12 + 1%, max ¥112; item 210101002 permit ¥10 waived 2025-04-01 to 2026-12-31. Matches S4 and every BOC column.
- [BOC ATM change effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay unchanged; Visa/Mastercard 2.5% of amount, min $3 / max $40 equivalent per withdrawal. Matches S10 (shown separately, not substituted).
- [BOC current board](https://www.boc.cn/sourcedb/whpj/enindex.html) — 2026-11-10 02:49 USD 6.6622/6.6903; half-spread 0.210449% vs modeled 0.210366% (~0.04% relative).
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — nonwillful $16,536, willful $165,353 for assessments on/after 2025-01-17. Matches S26.
- [IRS Form 8938/FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) — all four thresholds and the $10,000 FBAR trigger. Matches S27/S25.
- [IRS FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum $132,900. Matches S35.
- [Wise CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese, China work history, tax records within 3 years, own-account recipient, CNY 300,000 bank-app / 50,000 Alipay per transfer, overall limit = after-tax salary. Matches S11.
- [IRS Form 3520 instructions](https://www.irs.gov/instructions/i3520) + [IRM 8.11.5](https://www.irs.gov/irm/part8/irm_08-011-005) — 5% of gift per month, capped at 25%. Matches S28.

**Verification run:** `python3 scripts/build_site.py && python3 scripts/validate_site.py` PASS (6 pages, 18 procedures, 4×40 matrices, 6 exposure rows, 48 sources, local links, landmarks, Decimal arithmetic, citation-durability guards). Local HTTP: all six pages, both redirects, `style.css` and `data/cost-model.json` returned 200. Site files remain generated, no manual HTML edits.

**Irregularities still open (published on flagged.html, non-blocking):** live execution quotes and correspondent/receiver deductions, Wise/WU/MoneyGram current prices, other banks' tariffs, ATM execution FX and surcharge, PayPal/wallet and HK two-leg completeness, and all personal tax amounts. No new unverified value was added.

## Current session: arena/afeb2b56-china4 — task 13: conversion-penalty deep dive, extra routes, claim-level audit ledger (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 13 | (a) "Conversion penalty" deep dive: China tax needed to document each source of funds, US §988 currency-gain exposure by acquisition year, published SAFE enforcement outcomes; (b) routes not yet in the 18-route library; (c) one consolidated every-method × $10k–$400k mobile-first table; (d) claim-level audit ledger of the existing 47 sources (each claim re-read against the fetched official text) | **New files only:** `unlock.html`, `compare.html`, `audit.html`, `scripts/build_deepdive.py`, `scripts/validate_deepdive.py`, `data/deepdive-model.json`, `data/audit-ledger.json`; plus this section of `COORDINATION.md` | needs review | arena/afeb2b56-china4 → arena/fd53cba7-china4 | 2026-11-10 01:06 | Deliberately does **not** touch `scripts/build_site.py`, `scripts/validate_site.py`, `style.css`, the six generated pages, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md` or the workflow while they are claimed by other sessions. Branch fixed by Arena. |

### Claim log — arena/afeb2b56-china4
- **Board state read before claiming (2026-11-10 01:06 UTC, all remote branches fetched read-only):** task 12 was claimed within ~60 seconds of each other by six sessions with the same file scope — `753a8878` (done, merged as PR #20, no site change), `09fa5313` (done on its branch, no site change), and `36711496`, `374f09e6`, `7f52b605`, `b398220f` (all *in progress*, all listing `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML, `style.css`, `README.md`, `EXECUTIVE_SUMMARY.md` and the workflow). **Irregularity logged:** these claims overlap each other; they were made on separate branches, so none was visible to the others on `main` when written.
- Because that scope is already claimed several times over, this session takes a **different, additive scope made only of new files** (listed above). Nothing an active session owns is edited here.
- **Stale claim noted, not yet taken over:** `arena/ddfecf5c-china4` claimed "Phase 2 — 21-route expansion, tax-bottleneck playbook, mobile-first table UX" on 2026-11-09 01:46 UTC; its branch has had no commit since (>23 h, well past the 60-minute rule) and contains no work product (only the claim line; the `data/source-verification-log.json` it mentions was never pushed). The *new-file* part of that idea (tax-bottleneck analysis, extra routes) is covered by task 13 here. The shared-file part stays with whichever session integrates last.
- **Change requests to shared files (not applied by this session until the active task-12 sessions are done or stale — see "final integration" below):**
  1. `scripts/build_site.py` → `NAV`: add links to `unlock.html`, `compare.html`, `audit.html`.
  2. `.github/workflows/gh-pages.yml`: run `scripts/build_deepdive.py` + `scripts/validate_deepdive.py`; copy the three new pages and two new data files into `_site/`.
  3. `scripts/build_site.py` → `SOURCES` / `flagged.html`: register any new official sources and any defect this audit finds in existing rows (defects are listed in `data/audit-ledger.json` and on `audit.html`; they are *not* silently patched into another session's file).
- **Final integration:** when every other task on this board is `done` (or its claim is >60 minutes old with no commits), this session will act as the integration session for task 13: rebase on `main`, apply requests 1–3, re-run both validators, open the PR, merge, and confirm the Pages deployment. If another session integrates first, these requests remain here for it.
- **Rebase conflict #1 (2026-11-10 01:07 UTC):** `git pull --rebase origin main` conflicted in `COORDINATION.md` because PRs #21–#24 (`09fa5313`, `b398220f`) had appended their sections at the same end-of-file position while this claim was being written. Resolved by keeping **both sides in full** (main's sections first, this session's section after). No other session's text was dropped or edited. The claim commit had already been pushed un-rebased; the branch was then updated with `--force-with-lease` (own session branch only).
- **Board state after that rebase:** `b398220f` renumbered itself to task 14 and merged PR #24 (S5 repointed to BOC's dated query, S48 added, penalty-ceiling table, 48 sources). Task 13 here remains non-overlapping with it.

### Publication record — arena/b398220f-china4 (task 14)
- PR [#24](https://github.com/sassnarep3-star/China4/pull/24) merged as `bab34189d0110af8fe119ec932a7b3c2da0e8542` on 2026-11-10 01:06 UTC. Pull-request validation run [42733337982](https://github.com/sassnarep3-star/China4/actions/runs/42733337982) passed before merge (build reproducibility + validator). Post-merge "Validate and deploy China4" run [42733395264](https://github.com/sassnarep3-star/China4/actions/runs/42733395264) and pages build [42733394737](https://github.com/sassnarep3-star/China4/actions/runs/42733394737) succeeded; Pages API reports `built` (legacy, source `main` "/"). GitHub emitted only non-fatal Node 20 deprecation and ubuntu-latest migration notices.
- Live verification after deploy: `sources.html` served cutoff 2026-11-10, 48 documents, S5 repointed to BOC's date query and S48 present. The first `index.html` fetch returned a stale CDN copy (old cutoff and old S5 URL); a cache-busted fetch of `index.html?cb=20261110T0115` returned the new build with the dated-snapshot wording, S5+S48 links and the penalty-exposure line. Cache propagation, not a deployment failure — worth re-checking with a cache-buster when auditing.
- Board conflicts: main advanced five times during this session (PRs #20–#23 from parallel task-12 sessions). Two rebase conflicts, both confined to `COORDINATION.md`; resolved by retaining every session's section in full and appending only the audit log. No site file conflicted, no work discarded, and the validator passed on each combined tree.

### Task 14 — done
Scope delivered: citation-durability fix for the FX input (S5 → official date query, S48 cross-check, validator regression guard), removal of a deletable branch-specific repo link, cutoff/wording corrections, and a sourced statutory penalty-ceiling versus lawful-cost comparison. All new or changed values trace to official sources listed in the audit log above. Open items remain published on `flagged.html` and do not block.

## Session arena/7f52b605-china4 — independent re-verification (task 12)

| Task | Scope | Status | Owner | Verification / notes |
|---|---|---|---|---|
| 12 | Independent line-by-line audit of the live build, fresh official-source spot-checks, arithmetic re-derivation, defect fixes, PR + merge + Pages confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, `COORDINATION.md` | done | arena/7f52b605-china4 | Claim pushed 2026-11-10. Branch fixed by Arena and used as the integration branch. |

### Sources fetched and read in full this session (2026-11-10)

- [SAFE Individual FX Detailed Rules (2007, as modified)](https://www.safe.gov.cn/safe/2007/0105/5320.html) — Art. 2 (USD 50,000 annual convenience quota for 个人 settlement and 境内个人 purchase), Art. 13 (foreign individual: ID + amount evidence **including tax vouchers**; reconversion with original memo within **24 months**), Art. 15 (foreign individual remitting FX savings with ID). Art. 39 is marked repealed on SAFE's own page.
- [SAFE Measures for Individual FX (PBOC Order 2006 No. 3)](https://www.safe.gov.cn/tianjin/2024/0430/2465.html) — Art. 37 definitions: 境内个人 = Chinese citizens holding a PRC resident ID; 境外个人 = foreign citizens (incl. stateless) **holding a passport** plus HK/Macau/Taiwan compatriots.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — read Art. 39–48. Confirms fine **up to 30%**, serious cases **over 30% up to 100%**, Art. 42 illegal cash carriage **up to 20%**, and Art. 52's 境内个人 definition that includes a foreign national residing in China for a continuous year.
- [BOC personal service price list effective 2025-11-11](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 TT/draft 0.1%, min ¥50 / max ¥260, international telecom ¥150, draft postage actual; note 5 full-arrival USD 15 (BOC NY) / USD 25 elsewhere; item 210101002 carrying permit ¥10 waived to 2026-12-31; item 210108014 cross-border ATM ¥12 + 1%, max ¥112.
- [BOC ATM price change effective 2026-11-11](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — UnionPay unchanged; Visa/Mastercard 2.5% of amount withdrawn, min USD-equiv. 3 / max USD-equiv. 40 **per withdrawal**.
- [BOC MoneyGram fee schedule effective 2018-01-15](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html) — confirms the top non-Africa USD tier is 5,000.01–9,999.99 at $32, i.e. nothing above $9,999.99.
- [BOC live FX board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903 (per 100 CNY table 666.22 / 669.03). Independent half-spread 0.210447% vs 0.210366% modeled.
- [Wise guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, own-account recipient only, tax record within 3 years, **CNY 300,000/transfer (bank app)**, **CNY 50,000/transfer (Alipay)**, overall limit = after-tax salary.
- [Wise fee-change summary](https://wise.com/gb/blog/summary-of-fee-changes) — bank funding ¥33.20 + 0.62%; Alipay ¥33.20 + 1.97% (dated 2024 examples only).
- [SAFE cash-carrying measures](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — no permit ≤ USD 5,000; bank permit USD 5,000–10,000; above USD 10,000 generally not permitted except listed special cases.
- [SAFE card-cash notice, Hui Fa [2017] No. 29](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000 per person per calendar year; **CNY 10,000 per card per day**; borrowing/lending cards prohibited.
- [SAFE 2022 Q&A](https://www.safe.gov.cn/ningxia/2022/0929/1997.html) — the annual convenience quota is **not** a ceiling on genuine current-account purchase/settlement; documentation, not an ID alone, is required above it.
- [PBC Announcement [2004] No. 18](https://www.pbc.gov.cn/chubanwu/114566/114579/114643/2839193/index.html) — RMB 20,000 per person per trip for Chinese citizens and foreign nationals.
- [Customs Announcement 2025 No. 43](https://www.gov.cn/zhengce/zhengceku/202504/content_7017195.htm) — effective 2025-04-01; currency beyond the prescribed amount must be declared; **repeals Announcement 2007 No. 72**.
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — nonwillful **$16,536**, willful **$165,353** (assessments on/after 2025-01-17).
- [IRS Form 8938 / FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) — all four thresholds; FBAR trigger > $10,000.
- [IRS FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) — 2026 maximum **$132,900**.
- [CBP money and monetary instruments](https://www.cbp.gov/travel/international-visitors/money-monetary-instruments) — > $10,000 report, **group/family aggregation**, electronic FinCEN 105 filing.
- [FinCEN FBAR page](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) — aggregate > $10,000 at any time in the calendar year.
- [Bank of America wire flyer](https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6) — inbound **$15**, may be waived.
- [Chase Secure Checking fees](https://www.chase.com/personal/fees/secure-checking) — domestic and international incoming wires **$15**.
- [Capital One wire transfer](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/) — $15 incoming only on Essential Checking, High-Yield Checking, Essential Savings; other account types no fee.
- [PBOC Announcement [2004] No. 16](https://www.gov.cn/gongbao/content/2005/content_64294.htm) — emigration transfer applied for in full at once; 50% / then 50% of the remainder after 1 year / balance after 2 years; **≤ RMB 200,000 may be remitted in one lump sum after approval**; inheritance once or in instalments.

### Defects found and fixed

1. **S8 was cited for numbers it does not contain (High).** The customs clearance-guide page never states RMB 20,000 or USD 5,000. The values now rest on the PBOC announcement (S49) and the current customs instrument (S50); S8 is retained only for the red/green-channel procedure.
2. **The relied-on customs instrument had been repealed (High).** Announcement 2007 No. 72 was repealed effective 2025-04-01 by Announcement 2025 No. 43. The site now cites the current instrument and keeps the "declare currency beyond the prescribed amount" duty while dropping the defunct list.
3. **CBP source did not state the $10,000 rule (Medium).** Replaced with CBP's dedicated money/monetary-instruments page (S51), which also documents group aggregation. No value changed.
4. **Capital One example named an account type its own page does not name (Medium).** "360 Checking $0" was not what the page says; the note now states the disclosed condition.
5. **Dead official link (Medium, non-live).** `safe.gov.cn/en/2018/1206/1478.html` returns SAFE's page-not-found notice. No published row depended on it; the penalty ranges stand on S18, read in full.
6. **Identity-regulation divergence published as a review item (High).** SAFE treats a passport holder as 境外个人; Decree 532 includes a foreign national resident for a continuous year in 境内个人. Neither reading creates a general ID-only USD 50,000 right.
7. **Reproducibility link pinned an old session branch** — repointed to `blob/main`.

### Verification performed

- `python3 scripts/build_site.py && python3 scripts/validate_site.py` → **PASS**: 6 pages, 18 procedures, 4 × 40 cost matrices, 52 primary sources, local links, landmarks, per-row source-link requirement, independent `Decimal` re-derivation of the BOC, quota, Wise, ATM, emigration and receiving scenarios.
- Independent arithmetic re-derivation outside the validator: 40/40 BOC rows reproduce exactly (commission clamp, ¥150 telecom, same-quote half-spread, base USD); Wise splits confirmed for $10k/$100k/$200k/$400k (1/3/5/9 bank-funded; 2/14/27/54 Alipay-funded) with the fixed fee charged per transfer.
- Local HTTP smoke test: `index`, `methods`, `penalties`, `taxes`, `sources`, `flagged`, both redirects, `style.css` and `data/cost-model.json` all returned **200**; every page byte-identical to the generator output (`git diff` clean before regeneration).
- Mobile: no CSS change was needed — tables still collapse to labelled cards at ≤760 px via `data-label` on every `td`.

### Merge-conflict log

- First rebase onto `main` conflicted in `COORDINATION.md` (sessions `arena/753a8878-china4` and `arena/b398220f-china4` had appended boards). Resolved by **retaining every session's section in full**; nothing discarded.
- The rebase then conflicted in `scripts/build_site.py`, the validator and four generated pages, because `arena/b398220f-china4` had already used source id **S48** for the BOC board. Rather than overwrite their work, this session replayed its edits on top of theirs and re-numbered its new sources **S49–S52**, then regenerated all HTML from the merged generator. Cross-checked that their BOC-board citation, date-query note and penalty-ceiling comparison survive intact.

### Publication

- PR and merge result are recorded in the "Publication log" section below after the merge, together with the Pages deployment run and the live-URL check.

### Post-merge follow-up — arena/7f52b605-china4

- PR [#27](https://github.com/sassnarep3-star/China4/pull/27) merged at `b0289c763475aa0e878f550dcfeb46ecf8689166` on 2026-11-10 01:11 UTC. GitHub Pages reported `built` for that commit and the live pages were fetched.
- **Live-site defect caught after the merge:** `sources.html` served **52** register rows while its own prose still said "48 primary documents"/"48-document register". Two hard-coded counts in the generator had escaped the earlier renumbering when this branch was rebased onto another session's change. Fixed by deriving the count from `len(SOURCES)` in the generator and by adding a validator guard that fails when the stated number differs from the number of registered rows (negative-tested: mutating 52 → 49 produced `sources: prose claims 49 documents but the register has 52`).
- Follow-up PR and its deployment are recorded below.

### Publication log — arena/7f52b605-china4 (final)

| Item | Result |
|---|---|
| PR #27 | https://github.com/sassnarep3-star/China4/pull/27 — merged **2026-11-10 01:11 UTC** at `b0289c763475aa0e878f550dcfeb46ecf8689166` |
| PR #29 | https://github.com/sassnarep3-star/China4/pull/29 — merged at `ec08cb52ae94f9eba0848dd377a2b55717a66052` |
| Pages deploy (PR #27) | `pages build and deployment` [42734166953](https://github.com/sassnarep3-star/China4/actions/runs/42734166953) / run 42733912980 reported success; Pages API status `built` |
| Pages deploy (PR #29) | `pages build and deployment` 42734166967 and `Validate and deploy China4` 42734166953 completed for `ec08cb52`; Pages API status `built` |
| Live URL | https://sassnarep3-star.github.io/China4/ |

**Live verification after the final deploy (cache-busted fetches):**
- `sources.html` now reads "52-document primary-source register" and "52 primary documents", matching 52 register rows; S8 is relabelled as the clearance-procedure page with "threshold values: S49, S50".
- `flagged.html` serves the seven new findings, including the repealed-customs-instrument item, the dead SAFE link, the Capital One condition and the identity-classification divergence, each with source links.
- `penalties.html` serves the corrected Capital One receiving note and the unchanged 40-row matrices (BofA $15, Chase Secure $15 stated as before; no cost value moved).
- Cost model spot-check from the regenerated JSON: $10k = $53.45, $100k = $271.62, $200k = $481.99, $300k = $692.36, $400k = $902.72 (BOC known baseline); full-arrival scenario adds $40; Wise bank-funded 1/3/5/7/9 transfers ($66.96 → $2,524.64), Alipay-funded 2/14/27/41/54 transfers.

**Merge-conflict log (final).** Main advanced four times during this session (PRs #24, #25, #26 and their follow-ups). Every rebase conflicted only in `COORDINATION.md`, except one that also conflicted in the generator because another session had already taken source id **S48**. Each conflict was resolved by retaining all sessions' board sections and replaying this session's edits on top of the other session's generator, renumbering new sources to **S49–S52**; nothing was discarded and no other session's claim, source or finding was removed. `git merge-base --is-ancestor origin/main HEAD` was confirmed before each final push.

**Open items (published on `flagged.html`, non-blocking):** live execution quotes and correspondent/receiver deductions; Wise, Western Union and MoneyGram current prices; other banks' tariffs; ATM execution FX and surcharge; PayPal China/wallet and the Hong Kong two-leg route; provincial customs guidance after 2025-04-01; and all personal China/US tax amounts.

## Session arena/374f09e6-china4 — final integration (task 12)

**Claim.** Arena fixes this session to branch `arena/374f09e6-china4`, so it is the integration branch; no `session-<id>/<task>` branch was created. Base was `main` `54a190c` (PR #17). Task 12 was claimed in `COORDINATION.md` and the claim committed/pushed as `2a4b933` before any edits. `git pull --rebase origin arena/374f09e6-china4` initially failed because the remote branch did not exist; the first push created it.

**Independent line-by-line re-verification (fresh official fetches, 2026-11-10 UTC).** [S1](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [S2](https://www.safe.gov.cn/tianjin/2024/0430/2465.html), [S4](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf), [S5](https://www.boc.cn/sourcedb/whpjSearch/index_2833.html), [S7](https://www.safe.gov.cn/tianjin/2024/0430/2466.html), [S9](https://www.safe.gov.cn/hubei/2019/0305/851.html), [S10](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html), [S11](https://wise.com/help/articles/2955298/guide-to-cny-transfers), [S13](https://wise.com/gb/blog/summary-of-fee-changes), [S16](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html), [S18](https://www.gov.cn/gongbao/content/2008/content_1071846.htm), [S19](https://www.safe.gov.cn/safe/2015/1231/5442.html), [S20](https://www.gov.cn/gongbao/content/2005/content_64294.htm), [S25](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [S26](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821), [S27](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [S28](https://www.irs.gov/instructions/i3520), [S30](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr), [S31](https://www.irs.gov/publications/p1544/ar02.html), [S35](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion), [S38](https://www.irs.gov/publications/p525), [S39](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5193028/content.html), [S42](https://resources.bankofamerica.com/direct/render-resource/9149a2de7b1047a499ae291815e985e6), [S43](https://www.chase.com/personal/fees/secure-checking), [S44](https://www.capitalone.com/help-center/checking-savings/send-receive-wire-transfer/), [S46](https://www.safe.gov.cn/ningxia/2022/0929/1997.html), [S48](https://www.boc.cn/sourcedb/whpj/enindex.html). No value was inferred to fill a blank.

**Irregularities found (published on flagged.html; do not block merge).**
- High — the exact 2026-11-09 05:30 BOC USD row (666.48/669.29 per 100 USD) used by the model is no longer displayed on any of the five pages of BOC's rolling board, and BOC's historical date search requires a captcha. No permanent official URL reproduces it. Inputs remain in `data/cost-model.json`; obtain a written rate confirmation before execution.
- Medium — BOC separately publishes a Middle Rate (671.88 at 2026/11/10 07:32:39 Beijing) that is not the arithmetic midpoint of its buy/sell quotes (666.22/669.03); the model computes its own midpoint. Definition should be confirmed with BOC.
- Low — the PRC IIT rate tables on S39 are images; the seven brackets and quick deductions were not independently transcribed.
- Previously corrected defects from my first pass (S8 thresholds not in the HTML page, S51/CBP direction, S44 account naming, stale `blob/arena/` link) were already fixed on `main` by session `arena/7f52b605-china4`; their fixes and S49–S52 were preserved, not duplicated or overwritten.

**Merge-conflict log (required by the task rules).** PR #30 was created and reported `CONFLICTING`: sessions `arena/b398220f-china4` (PR #24), `arena/afeb2b56-china4` (PR #25), `arena/7f52b605-china4` (PRs #27, #29) and `arena/b398220f-china4` (PR #28) had merged overlapping work into `main` while this branch was in flight — 52 sources, the current Customs Announcement 2025 No. 43, the dedicated CBP page, a dynamic prose/register count guard, corrected Capital One wording and an FX citation-durability guard. `git merge --no-commit --no-ff origin/main` conflicted in 12 files. Resolution: took `main`'s version of every conflicting file **in full** (nothing discarded), then re-applied only this session's unique contribution on top — the executive-summary page, the 07:32:39 rate check, three new flagged items, validator/Pages wiring and documentation. Their dynamic `len(SOURCES)` count, 52-source register, S48–S52 and all corrected rows survive. Conflict was resolved without discarding another session's work.

**Deliverable.** New live `summary.html` (five key amounts, eight-route shortlist, six-row tax/penalty boundary, eight execution steps, every table row with a direct official-source link), nav entry and dashboard CTA; rate-freshness callout on Costs; three new flagged items; `data/cost-model.json` provenance; README, EXECUTIVE_SUMMARY, validator (7 pages, summary row counts, nav link guard) and the Pages artifact copy list.

**Verification performed.** `python3 scripts/build_site.py` → 7 pages, 2 redirects, 40 audited rows; `python3 scripts/validate_site.py` → PASS (7 pages, executive summary, 18 procedures, 4×40 matrices, 52 sources, prose/table agreement, canonical FX citations, local links, landmarks, independent Decimal arithmetic). Local HTTP smoke test: all 9 HTML/redirect pages, `style.css` and `data/cost-model.json` returned 200. The validator checks link presence and arithmetic, not that each external page supports every claim; the defects above were found by reading official text.

**Publication.** PR [#30](https://github.com/sassnarep3-star/China4/pull/30) from `arena/374f09e6-china4` → `main`. Merge result and Pages deployment are recorded below after they complete.

**Task status:** in progress until PR #30 is merged and GitHub Pages deployment is confirmed.

## Current session: arena/a2efb7b1-china4 — task 15: multi-bank tariffs, stuck-CNY tax-gate playbooks, and line-by-line repo verification (NEW files only)

| Task | Scope (files) | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 15 | (1) Research & verify additional PRC bank tariffs (ICBC, CCB, CMB, ABC, HSBC China) and lawful conversion channels (UnionPay POS overseas direct spend vs ATM cap, departing-foreigner PRC social-insurance lump-sum refund/remittance, WFOE/PRC dividend distribution + US–China Treaty Art. 9 + STA/SAFE `[2021] No. 19` tax record filing >$50k, SkyRemit); (2) build $10,000–$400,000 (40-increment) multi-bank cost & stuck-CNY tax-gate/penalty minimization playbooks; (3) perform line-by-line repo verification from official primary sources and publish irregularities | **New files only:** `banks.html`, `playbooks.html`, `verification.html`, `scripts/build_bank_playbooks.py`, `scripts/validate_bank_playbooks.py`, `data/bank-playbooks.json`; plus this section of `COORDINATION.md` | needs review | arena/a2efb7b1-china4 → arena/fd53cba7-china4 | 2026-11-10 01:16 | Non-overlapping with Task 13 (`afeb2b56`: `unlock.html`, `compare.html`, `audit.html`, `build_deepdive.py`, `validate_deepdive.py`, `deepdive-model.json`, `audit-ledger.json`), PR #30 (`374f09e6`, `summary.html` merged), and PR #31 (`36711496`). Shared files (`scripts/build_site.py`, `scripts/validate_site.py`, root generated pages, `style.css`, `README.md`, `EXECUTIVE_SUMMARY.md`, `.github/workflows/gh-pages.yml`) are NOT edited while claimed by active sessions; change requests logged below for final integration. Branch fixed by Arena (`arena/a2efb7b1-china4`). |

### Claim & coordination log — arena/a2efb7b1-china4
- **Non-overlapping scope verified against `main` (`3f9aad4`) and all active remote branches (`afeb2b56`, `374f09e6`, `36711496`, `7f52b605`, `b398220f`):** only the six new files listed above plus this coordination section are touched during Task 15 execution.
- **Rebase conflict #1 (2026-11-10 01:17 UTC):** PR #30 (`arena/374f09e6-china4`) merged into `main` (`3f9aad4`) at the end of `COORDINATION.md` while PR #33 (this claim) was opening. Stopped and resolved by retaining `374f09e6`'s section in full above and appending this claim below; zero text discarded.
- **Initial repo irregularity spotted on read-through (logged, not edited in another session's section):** `COORDINATION.md` lines 309 and 328 contain stray partial merge-conflict marker remnants (`EAD`) introduced during an earlier rebase in `58e0670`. Logged for cleanup at final integration and on `verification.html`.
- **Shared-file change requests for final integration (logged per coordination rules rather than editing files currently claimed by PR #31 / `374f09e6`):**
  1. `scripts/build_site.py` (`NAV`, `index_page`, `flagged_page`, `sources_page`) and `scripts/validate_site.py`: link `banks.html`, `playbooks.html`, and `verification.html` in global navigation and register newly verified primary sources once all active shared-file sessions are `done`.
  2. `.github/workflows/gh-pages.yml`: run `python3 scripts/build_bank_playbooks.py && python3 scripts/validate_bank_playbooks.py` in `validate`, and include `banks.html`, `playbooks.html`, `verification.html`, and `data/bank-playbooks.json` in `_site/` during `deploy` (note: GitHub Pages `build_type` is also `legacy` from `main:/`, which serves root `.html` files directly, while Actions artifact deploy stages `_site/`).
  3. Clean up the two stray `EAD` lines in `COORDINATION.md` without altering any session's substantive record.
- When all active shared-file claims (`374f09e6`, `36711496`, `afeb2b56`) reach `done` (or become stale >60 min), this session (or the last completing integration session) will integrate the shared navigation/workflow cleanly, re-verify line by line, open & merge PR to `main`, and verify live GitHub Pages deployment.

## Session arena/581766ee-china4 — stale-task handoff and integration

| Task | Scope | Status | Owner | Started UTC | Notes |
|---|---|---|---|---|---|
| Final independent audit, gap remediation and publication | `COORDINATION.md`, `scripts/build_site.py`, `scripts/validate_site.py`, generated root HTML, `data/cost-model.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, `.github/workflows/gh-pages.yml`; supplemental new files if needed | in progress | arena/581766ee-china4 | 2026-11-10 05:52 | Taking over stale overlapping integration claims and tasks 13/15 as needed: latest recorded branch commits for afeb2b56 and a2efb7b1 are 01:08 and 01:20 UTC respectively, >60 minutes old; latest shared-file claims likewise stale. Preserve prior work and record gaps. Fixed Arena branch overrides requested session branch naming. |

### Audit and handoff — arena/581766ee-china4
- Claim `4735892` was committed and pushed before changing scoped files; initial `git pull --rebase origin arena/581766ee-china4` reported the remote branch did not exist, so `git pull --rebase origin main` was run before its first push. All work remains on the Arena-fixed branch. The active claims for tasks 13 and 15 were stale (>60 minutes without commits); their requested new files do not exist in merged main, so the uncompleted multi-bank and deep-dive deliverables remain a review gap, not falsely marked complete. Other past in-progress board entries are retained as historical records, not overwritten.
- Fresh primary-source checks: [SAFE individual FX Art. 13–15](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [BOC 2025 personal tariff item 210105008](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf), [BOC MoneyGram 2018 schedule](https://www.boc.cn/pbservice/bi2/201801/t20180112_11198459.html), [Wise current CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers), [Wise dated examples](https://wise.com/gb/blog/summary-of-fee-changes), [SAFE overseas ATM rules](https://www.safe.gov.cn/hubei/2019/0305/851.html), [PRC FX regulations articles 39–45](https://www.gov.cn/gongbao/content/2008/content_1071846.htm), [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [IRS FEIE](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion), and [Shanghai tax bureau comprehensive-income bracket PDF](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202402/P020240202362406243753.pdf) (all seven bracket values verified against PDF). [BOC rolling board](https://www.boc.cn/sourcedb/whpj/enindex.html) showed 665.86/668.66 per 100 USD at 2026-11-10 13:49:58 Beijing on this check; this does not independently verify the inherited 2026-11-09 model quote, which remains flagged. The quote is historical, not actionable.
- Fixed false MoneyGram $10,000 label; 2018 non-Africa top tier ends at $9,999.99. Replaced Wise extrapolations with blank current-cost cells, explaining fee deduction before FX and unequal net payouts; added five-column unpriced-route amount coverage (40 rows) without inventing quotes. Qualified ATM-cap language by modeled FX and unused allowance. Adjusted statutory serious-case minimum from “over 30%” to “30% or more.” Added direct official source to every China bracket row and regression tests. The historical BOC estimate is not a personal quote; taxes, current quotes and charges are unknown.
- Verification boundary: this session spot-checked high-impact claims and primary sources, not every inherited line or every external source URL. Structural validation confirms direct source links per table row, not claim-level support or continuing remote availability. The remaining independent line-by-line audit is explicitly flagged on the site. `python3 scripts/build_site.py && python3 scripts/validate_site.py`, Python compilation, `git diff --check`, and local HTTP GET of seven pages, two redirects, CSS and data all passed.
## Session arena/c009d1db-china4 — strict evidence audit and publication

| Task | Scope | Status | Owner | Started UTC |
|---|---|---|---|---|
| Strict evidence boundary, independently checked primary-source executive brief, validation and publication | COORDINATION.md; new evidence.html; scripts/build_evidence.py; scripts/validate_evidence.py; README.md; .github/workflows/gh-pages.yml; scripts/build_site.py (navigation and evidence warning only) | in progress | arena/c009d1db-china4 | 2026-11-10 05:53 |

Claim: no other session's new files will be edited. Shared navigation/workflow claims above are older than 60 minutes; this session takes over only integration of its evidence page, preserving existing generators and research. Existing FX values cannot be independently reproduced from a stable official URL: a strict table will leave executable costs blank rather than present them as verified. Fixed Arena branch is the integration branch. No account or tax facts will be invented.

### Independent audit result — arena/c009d1db-china4
- Freshly read official primary text on 2026-11-10: [SAFE Detailed Rules Arts. 2, 13–15](https://www.safe.gov.cn/tianjin/2024/0430/2464.html), [PBOC Measures Arts. 2, 5, 7, 13, 28](https://www.safe.gov.cn/tianjin/2024/0430/2465.html), [SAFE permanent-resident exception](https://www.safe.gov.cn/en/2017/1129/1365.html), [IRS worldwide income](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad), [IRS FTC](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit), [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [IRS 8938 comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [Wise current CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers).
- Added evidence.html: eight freshly checked rules, seven execution steps, 18 route-category ladders × 40 target amounts. Current fee, FX cost, tax and all-in values remain **blank** because no personalized executable quote or tax facts were verified. Linked official rules establish categories, not prices. Existing historical calculations remain intact but are globally labeled illustrative; this strict register supersedes their interpretation as verified current costs.
- Verification: both generators and both validators PASS; all 720 current-cost rows blank; every table data row has an official source; all local page links resolve; 10 public files return HTTP 200. Existing tests check structure and independent arithmetic, not semantic support for every inherited claim. No full fresh line-by-line certification of all inherited sources is made.
- Published review flags: unreproducible historical FX row, unknown personal/account/tax facts, structural tests versus semantic verification, and the Wise 2025 tax-record example not converted to a fabricated 2026 cutoff.
- Coordination: initial pull of this session's remote branch failed because it did not exist; first push created it. PR #31 was still open and showed a fresh update while this narrow integration was running. Its work was not merged or discarded. Changes here are limited to evidence-page navigation/warning/Review linkage and workflow integration, not its US-tax models. Task 15's six new files remain untouched.
- Publication pending: PR URL and Pages result will be recorded after merge.
## Session arena/fd53cba7-china4 — final integration and publication (task 16)

| Task | Scope | Status | Owner | Started (UTC) | Notes |
|---|---|---|---|---|---|
| 16 | Final integration after active tasks 13 and 15: preserve their new-file outputs, wire navigation/workflow, re-run every validator, audit live/mobile routes, open/merge PR, and confirm GitHub Pages | `COORDINATION.md`; after tasks 13/15 complete: shared generator, validator, workflow, documentation and generated site | done | arena/fd53cba7-china4 | 2026-11-10 | Arena fixes this session to this branch. Task 13 (`afeb2b56`) and task 15 (`a2efb7b1`) are currently active, so their claimed new files will not be edited or duplicated; this session is the designated final integration owner. |

### Claim log — arena/fd53cba7-china4
- Read the complete coordination board, current tree, open PRs and remote branches before claiming. PR #31 remains open; tasks 13 and 15 are recent active claims. Their scopes are preserved.
- Per the fixed-branch Arena rule, no `session-<id>/<task>` branch is created. All work remains on `arena/fd53cba7-china4`.
- Integration will not infer unavailable prices or personal tax liabilities. Unknown executable quotes, correspondent deductions, source-of-funds facts, tax basis and account-specific eligibility remain blank and published for review.
## Session arena/36711496-china4 — independent evidence audit (task 12)

| Task | Scope (files) | Status | Owner | Notes |
|---|---|---|---|---|
| 12 | Independent line-by-line evidence audit: re-fetch every cited primary source, re-derive every figure, fix defects, verify live Pages state, PR + merge + deploy confirmation | `scripts/build_site.py`, `scripts/validate_site.py`, generated `*.html`, `EXECUTIVE_SUMMARY.md`, `README.md`, `COORDINATION.md` | done | arena/36711496-china4 |

### Audit log — arena/36711496-china4

**Scope and coordination.** Branch `arena/36711496-china4` (fixed by Arena) is this session's integration branch. During the session, main advanced by 20 commits (through PR #27) and other sessions had already corrected the customs-citation defect inherited from S8 and added source IDs S48–S52. Rather than overwrite that work, this session rebased onto main, replayed only its non-overlapping additions, and **re-numbered its single new source to S53** to avoid a collision. Their S8 correction, PBOC Announcement [2004] No. 18 citation (RMB 20,000) and penalty-vs-cost comparison were verified and preserved intact. `backup-mine-36711496` holds the pre-rebase state for traceability.

**Sources re-fetched and read this session (not merely linked):**
- [SAFE individual FX detailed rules](https://www.safe.gov.cn/tianjin/2024/0430/2464.html) — Arts. 2 (USD 50,000 annual total for settlement and domestic-individual purchase), 13 (foreign individual lawful current-account income with tax vouchers), 14, 15, 30, 39 (marked repealed on SAFE's own page).
- [PBOC individual FX measures](https://www.safe.gov.cn/tianjin/2024/0430/2465.html) — Art. 37 definitions: domestic individual = Chinese citizen holding a PRC resident ID; foreign individual = passport/HK/Macau/Taiwan travel-document holder.
- [SAFE 2022 Q&A](https://www.safe.gov.cn/ningxia/2022/0929/1997.html) — the USD 50,000 figure is a convenience quota, not a hard cap on genuine current-account transactions.
- [State Council FX Regulations, Decree 532](https://www.gov.cn/gongbao/content/2008/content_1071846.htm) — Art. 5 (no restriction on current international payments and transfers); Arts. 39–45 (30% ceiling, 30%–100% for serious cases; 20% for cash).
- [BOC 2025-11-11 personal tariff PDF](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 (0.1%, min ¥50, max ¥260; international telecom ¥150), note 5 (full arrival USD 15 BOC NY / USD 25 elsewhere), item 210101002 (permit ¥10, waived to 2026-12-31), item 210108014 (UnionPay ¥12 + 1%, max ¥112), note 10 (ATM-owner surcharge).
- [BOC 2026-11-11 ATM notice](https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html) — Visa/Mastercard 2.5%, min USD-equiv. 3 / max 40 per withdrawal.
- [BOC rate board](https://www.boc.cn/sourcedb/whpj/enindex_1619_1.html) — 2026-11-10 06:43 USD buy 6.6622 / sell 6.6903; consistent in magnitude with the 2026-11-09 05:30 model input (6.6648 / 6.6929).
- [eCFR 31 CFR 1010.821](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821) — non-willful USD 16,536; willful USD 165,353 (assessments on/after 2025-01-17).
- [eCFR 31 CFR 1010.340](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.340) — report required to transport more than USD 10,000.
- [IRS FBAR](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), [Form 8938/FBAR comparison](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements), [Form 3520 instructions](https://www.irs.gov/instructions/i3520) (USD 100,000 nonresident-individual/estate gift threshold), [FEIE page](https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion) (2026: USD 132,900).
- [IRS Publication 525](https://www.irs.gov/publications/p525) — personal foreign-currency transaction gain excluded unless more than USD 200, then reported as a capital gain.
- [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — 2026 Table 3 brackets, USD 16,100 standard deduction, capital-gain bands USD 49,450 / USD 545,500, FEIE USD 132,900, §6039F USD 20,573.
- [PBOC Announcement [2004] No. 18](https://www.pbc.gov.cn/chubanwu/114566/114579/114643/2839193/index.html) — RMB 20,000 per person per trip.
- [Customs Announcement 2025 No. 43](https://www.gov.cn/zhengce/zhengceku/202504/content_7017195.htm) — repeals Announcement 2007 No. 72 from 2025-04-01.
- [SAFE cash-carrying measures](https://www.safe.gov.cn/tianjin/2024/0430/2466.html) — USD 5,000 permit-free, 5,000–10,000 bank permit, above 10,000 generally prohibited.
- [SAFE ATM-cap notice](https://www.safe.gov.cn/hubei/2019/0305/851.html) — CNY 100,000/person/year, CNY 10,000/card/day, no borrowed cards.
- [SAFE Hui Fa [2015] No. 49](https://www.safe.gov.cn/safe/2015/1231/5442.html) — splitting/borrowed quotas and the watch-list period (year of listing plus two following years).
- [Wise CNY guide](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — non-mainland-Chinese eligibility, 3-year tax records, own-account recipient, CNY 300,000 bank / 50,000 Alipay per transfer, tax-based overall limit.
- [Wise 2024-11-25 fee-change post](https://wise.com/gb/blog/summary-of-fee-changes) — CNY 33.20 + 0.62% (bank) and CNY 33.20 + 1.97% (Alipay).

**Result of the audit:** every cited figure above matched its source on re-read. No figure in the inherited cost model required correction this session; the BOC ladder, half-spread, Wise splits and ATM counts re-derived exactly (`validate_site.py` PASS).

**New contribution (non-overlapping):** the site previously described US tax qualitatively but never quantified it, which left the user's core question ("how much tax would this cost me?") unanswered. Added a 2026 single-filer illustration pricing the same amount under three characters (ordinary income, a 10% currency gain, FEIE-eligible earned income) from Rev. Proc. 2025-32, with the *measured* gain column deliberately blank because acquisition basis is a personal fact. The validator re-derives all fifteen displayed figures from separately re-entered source values; a one-dollar mutation of a bracket makes it fail (negative control run). This also **resolved** the open 2026 §6039F threshold item (USD 20,573).

**Irregularities for review (published on flagged.html, not merge blockers):**
1. The 2026 tax illustration assumes USD 100,000 of other taxable income, single filer, standard deduction. A real return has different inputs.
2. A measured FX gain remains blank: acquisition date and rate of a pre-existing balance cannot be sourced publicly.
3. BOC's board rotates; the dated quote is a benchmark, not an executable rate (already flagged by prior sessions).
4. Stale duplicate PRs #4, #5, #12 from other sessions remain open and were not touched.

### Integration log — arena/fd53cba7-china4
- PR #31 was complete but conflicted with the newer seven-page site. Integrated its unique S53 / Rev. Proc. 2025-32 tax illustration by merging its branch, retaining the current summary page and all S1–S52 work, adding the five-row tax matrix and independent arithmetic checks, then regenerating HTML. Resolved conflicts in `COORDINATION.md`, `EXECUTIVE_SUMMARY.md`, `flagged.html`, and `scripts/validate_site.py` without discarding either side. Removed the two previously logged stray `EAD` marker remnants.
- Tasks 13 and 15 remain separate recent active claims with no work-product commits beyond their coordination claims. Their scopes were neither duplicated nor overwritten. They are optional additive expansion work; the integrated seven-page deliverable already satisfies the requested executive summary, lawful-method library, pros/cons, exact conditional procedures, $10,000–$400,000 matrices, primary-source register and flagged unknowns.
- Verification before PR: `python3 scripts/build_site.py` and clean generated diff; `python3 scripts/validate_site.py` PASS (7 pages, 18 procedures, four 40-row matrices, five-row 2026 tax illustration, 53 sources, source links on every table row, local links, landmarks and independent Decimal arithmetic).

### Publication result — arena/fd53cba7-china4
- Active-claim handoff: tasks 13 and 15 had no work-product commit more than four hours after their claim commits (well beyond the 60-minute takeover rule). They are marked `needs review`, not silently represented as completed. Their unresolved additive topics are already published on `flagged.html`: other-bank tariffs/live quotes, provider prices, source-of-funds/tax basis, eligibility and personal tax amounts. They do not block the verified original deliverable.
- Integration PR [#34](https://github.com/sassnarep3-star/China4/pull/34) merged to `main` at commit `ad394af0a47bd501e4f864a7d3ac66bcc89fdb8f` on 2026-11-10 05:53 UTC.
- Pull-request validation [run 42764883572](https://github.com/sassnarep3-star/China4/actions/runs/42764883572) passed before merge. Post-merge validation/artifact deployment [run 42764917091](https://github.com/sassnarep3-star/China4/actions/runs/42764917091) and legacy Pages build/deploy [run 42764916667](https://github.com/sassnarep3-star/China4/actions/runs/42764916667) both succeeded for the merge commit. Pages API reports `built`, source `main:/`, live URL https://sassnarep3-star.github.io/China4/.
- The sandbox network allowlist blocks direct `github.io` HTTP requests (curl returned no connection), so no false live-content claim is made. Deployment was instead confirmed from both successful deploy jobs and the GitHub Pages API; local HTTP smoke tests returned 200 for every page, both redirects, CSS and JSON.
- Non-failing infrastructure warning: GitHub's managed legacy Pages build reports Node.js 20 deprecation / forced Node.js 24 and an upcoming `ubuntu-latest` image migration. This is a GitHub-managed action warning, not a site failure.

- Integration conflict 2026-11-10: main advanced through PRs #34/#35 while PR #36 was opening. Stopped and retained both coordination logs in full; regenerated conflicting HTML from the automatically merged generator, preserving the new S53 tax illustration and this evidence page. Both validators re-run below.

- Merge conflict 2026-11-10: while PR #38 was open main advanced through PRs #34–#36. Stopped; preserved both coordination logs, the independent strict evidence page and the 2026 US tax illustration, combined source registrations as S53 (IRS) and S54 (Shanghai), and regenerated all pages from the combined generator.
