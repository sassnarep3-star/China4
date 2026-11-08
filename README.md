# China Money — getting CNY out of China, verified

**Live site: https://sassnarep3-star.github.io/China4/**

Research for a **US citizen** holding CNY in a Chinese bank account who wants it in USD
with the least tax and penalty cost. Every number on the site was read from an official
source. Anything that could not be confirmed is left **blank and flagged** — never estimated.

## What is here

| Page | Contents |
|------|----------|
| `index.html` | Dashboard and executive summary |
| `guide.html` | Decision guide — four questions that determine your route |
| `methods.html` | All 25 channels, with legal basis, limits, costs, pros and cons |
| `costs.html` | The conversion penalty in eight layers, plus the published bank tariff |
| `china-rules.html` | 26 controlling Chinese rules, with the Chinese text quoted |
| `us-tax.html` | FBAR, FATCA, Form 3520, and the IRC 988 currency gain |
| `penalties.html` | Every penalty from the statute, with the Chinese text |
| `flagged.html` | 11 values left blank and 14 irregularities, published openly |
| `audit.html` | Line-by-line review of the previously published site: 109 claims, 16 findings |
| `sources.html` | All 25 sources, each fetched and read directly |

## How it is built

The JSON files in `data/` are the single source of truth. `build.py` renders every page
from them, so a claim cannot appear on one page and contradict another.

```bash
python3 build.py          # regenerate all pages
python3 tools/verify.py   # verification gate; exit 1 on any failure
```

`tools/verify.py` fails the build if:

- a factual row has no official source and no explicit flag
- a source id does not resolve, or its host is not on the official-domain allowlist
- an internal link or anchor is broken
- a table has inconsistent column counts, or a `<td>` sits outside a row
- a null leaks into the rendered page as a literal value
- the committed HTML does not match what `build.py` generates

CI runs both steps on every push and pull request, and refuses to deploy if either fails.

## Verification policy

A source counts as official only if it is published by the regulator (SAFE, PBOC, Customs,
the State Taxation Administration, IRS, FinCEN, CBP), by the legislature or government, or —
for bank charges — by the regulated institution in its own published tariff. Travel sites,
accountancy blogs and news articles are used for nothing.

A dash (—) means *not verified*. It never means zero and never means *not applicable*.
`data/sources.json` records the date each source was actually fetched and read.

External URLs are not fetched by `tools/verify.py`: the build sandbox has no general
outbound HTTP. Each was verified individually during research and the date recorded.
The verifier checks provenance and structure, not liveness.

## Substantive corrections to the previous version

The earlier published site contained two critical errors and several material ones.
Full detail with statutory text is on `audit.html`. In brief:

- **The USD 50,000 quota was applied to the wrong class of person.** It binds *purchase*
  by 境内个人 only. A foreigner becomes 境内个人 only after one full year of continuous
  residence (Order 532 Art. 52(2)); below that, Art. 13 applies with tax vouchers and
  states no annual numeric cap.
- **Two penalty ranges were fabricated.** "30%–300%" and "30%–500%" do not exist.
  Arts. 39, 40 and 45 read up to 30%, and in serious cases 30% up to **100%** (等值).
- **"No US tax on conversion" was wrong.** Disposing of RMB is an IRC 988 transaction
  producing *ordinary* gain; the $200 personal exclusion is a gain-only cliff.
- **Two Form 3520 thresholds were conflated.** $20,573 (2026) is for gifts from foreign
  corporations and partnerships; gifts from a foreign individual or estate use a
  non-indexed "more than $100,000".
- **Missing channels added**, including the inheritance and emigration transfer routes —
  the only lawful channels for a large capital balance.
- **Bank fees were filled in** from Bank of China's own published tariff, including a
  change effective 2026-11-11 that raises Mastercard/VISA overseas ATM fees to 2.5%.

## Not advice

This is a research summary, not legal, tax or financial advice. Rules and tariffs change.
Confirm your own position with your bank, SAFE and a qualified US tax adviser before acting.

## Coordination

`COORDINATION.md` is the shared task board for parallel sessions. Claim before working,
keep file scopes non-overlapping, and run `git pull --rebase` before every push.
