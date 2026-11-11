# Verification spot-check — 2026-11-11 (session arena/86fdde1c-china4, task 26)

Independent re-read of a sample of load-bearing official sources against the live site.
No value was changed; no new price, rate, or tax amount was introduced. Unknowns remain blank on the site.

## Sources re-read and compared

| # | Claim on the site | Official source re-read | Result |
|---|---|---|---|
| 1 | FBAR: aggregate foreign accounts over USD 10,000 at any time in the calendar year; due April 15 with automatic extension to October 15 | [IRS FBAR page](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — "the aggregate value of those foreign financial accounts exceeded $10,000 at any time during the calendar year reported"; "due April 15 … automatic extension to October 15" | Matches source |
| 2 | Wise CNY outbound eligibility: sender not mainland Chinese, has worked in China, holds a Chinese tax record showing taxes paid within the last 3 years; recipient must be an account the sender owns; CNY 300,000 per transfer from the China bank app, CNY 50,000 from Alipay | [Wise, Guide to CNY transfers](https://wise.com/help/articles/2955298/guide-to-cny-transfers) — "You're not mainland Chinese", "You're working or have worked in China before", "valid tax record … showing taxes paid within the last 3 years", "you can only send CNY from China to another account you own", "maximum you can send in one transfer is 300,000 CNY" (bank app), "50,000 CNY" (Alipay) | Matches source. The site uses the rolling "last three years" phrasing; no fixed start year is printed on the site. |
| 3 | USD 50,000 is a convenience quota, not a hard cap on genuine current-account purchase/settlement | [SAFE Ningxia 2022 Q&A](https://www.safe.gov.cn/ningxia/2022/0929/1997.html) — "年度便利化额度不是个人每年购汇或者结汇的限额" (the annual convenience quota is not a limit on personal annual purchase/settlement); Arts. 54–57 of the Current Account FX Guidelines | Matches source |
| 4 | Personal foreign-currency transaction gain over USD 200 is reported as a capital gain | [IRS Publication 525 (2025)](https://www.irs.gov/publications/p525) — "If you have a gain on a personal foreign currency transaction because of changes in exchange rates, you don't have to include that gain in your income unless it's more than $200. If the gain is more than $200, report it as a capital gain." | Matches source |
| 5 | BOC personal tariff: cross-border TT/draft commission 0.1%, minimum CNY 50, maximum CNY 260; international telecom CNY 150; overseas ATM CNY 12 + 1%, capped at CNY 112; full-arrival USD 15 (recipient bank holds an account at BOC New York) or USD 25 otherwise; foreign-currency carrying permit CNY 10, waived 2025-04-01 to 2026-12-31 | [BOC personal tariff PDF, effective 2025-11-11](https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf) — item 210105008 (1‰, min 50, max 260; international telecom 150), item 210108014 (12 + 1%, max 112), note 5 (USD 15 / USD 25), item 210101002 (permit CNY 10, waived to 2026-12-31) | Every published BOC fee component reconfirmed |
| 6 | Headline modeled cost: USD 53.45 at USD 10,000 and USD 902.72 at USD 400,000 (published wire tariff + CNY 150 telecom + same-quote half-spread benchmark) | Re-derived independently in Python (Decimal) from the published inputs in `data/cost-model.json`: sell 6.6929, buy 6.6648, midpoint 6.67885, half-spread fraction 0.0021036556 (half-width relative to midpoint). USD 10,000 → CNY 66,929 principal, commission CNY 66.93, telecom CNY 150, spread CNY 140.80, total CNY 357.72 → USD 53.45. USD 400,000 → commission capped at CNY 260, total USD 902.72. | Arithmetic correct. Note: the half-spread is defined relative to the midpoint, not the sell rate; the site documents it as an arithmetic benchmark, not a guaranteed markup. |

## Repository and live-site checks

- Full rebuild from the five builders produced **zero diff** before any edit; all seven validators pass (`validate_site`, `validate_evidence`, `validate_bank_playbooks`, `validate_method_treaty`, `validate_taxlayers`, `validate_effective_dates`, `validate_publication`).
- Live site fetched and confirmed serving current content: headline USD 53.45 / USD 902.72, the cost-snapshot table, and the 18-route inventory are present at https://sassnarep3-star.github.io/China4/.
- Pages API at claim time: `status: built`, `build_type: legacy`, source `main:/`.

## Irregularities found

None in the spot-checked claims. The known standing items remain published on the Flagged for Review page and do not block publication: no live provider quote exists (Wise/WU/MoneyGram cells stay blank by policy), the dated BOC quote row is not permanently retrievable (captcha-gated date query), and legacy branch publishing serves the repository root.

## What this session did not do

It did not obtain a live provider quote, did not determine the account's classification, source of funds, tax history, or acquisition basis, and did not give legal or tax advice. Those remain blank on the site and are listed on *Flagged for Review*.
