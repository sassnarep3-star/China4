# China4 — getting money out of China

A source-verified research dashboard for a US citizen holding renminbi in a Chinese bank account: every lawful conversion route we could document, what each one costs, the China and US penalties for getting it wrong, and a cost table from **$10,000 to $400,000 in $10,000 steps**.

**Live site:** https://sassnarep3-star.github.io/China4/

## Pages

| Page | What it answers |
| --- | --- |
| `index.html` | Executive summary, the short answer, key numbers, which rule applies to you |
| `costs.html` | The 40-row cost table, the formula, per-method comparison, illegal-route exposure |
| `methods.html` | 17 routes with limits, pros, cons and an official source on every row |
| `penalties.html` | Exact China fine ranges by article, US reporting penalties, the "30%–300%" correction |
| `taxes.html` | FBAR, Form 8938, Form 3520, FinCEN 105, the currency-gain question, the treaty |
| `playbook.html` | Six lawful routes step by step, with the document list for each |
| `flagged.html` | Every value that could not be confirmed from an official source, plus corrected irregularities |
| `sources.html` | The full source registry with what each text establishes and its retrieval status |

## How it is built

Static HTML/CSS, no runtime dependencies. `build.py` holds the source registry, the verified cost inputs and the page templates, and writes every page plus the audit files in `data/`.

```bash
python3 build.py        # regenerate all pages, then validate
```

`build.py` fails if a page has a broken internal link, if any table row lacks an external source link, or if a template artefact leaks into the output.

Audit outputs, regenerated each build:

- `data/cost_table.csv` — the 40-row cost table with every component of the arithmetic
- `data/inputs.json` — the exchange rate and tariff inputs with their quote timestamp
- `data/sources.json` — the source registry, including retrieval notes

CI (`.github/workflows/verify.yml`) rebuilds the site and fails if the committed HTML differs from the generator's output, so the published pages cannot drift from the data.

## Cost model

One documented bank conversion and wire:

```
mid        = (6.6648 + 6.6929) / 2 = 6.67885 CNY per USD     # Bank of China quote, 2026-11-09 05:30 Beijing
spread     = amount × (6.6929 − mid) ÷ 6.6929                  # 0.2099% one-way
wire fee   = clamp(0.001 × amount × 6.6929, RMB 50, RMB 260) + RMB 150
total cost = spread + wire fee ÷ 6.6929
```

- $10,000 → **$53** (0.53%)
- $50,000 → **$166** (0.33%)
- $400,000 → **$901** (0.23%)

No tax is included because converting and wiring your own after-tax money is not a taxable event in either country. The figures exclude US receiving-bank and intermediary fees, which are flagged as unverified.

## Verification policy

1. A value is printed only if it comes from an official source, or from arithmetic on such a value with the formula shown.
2. Every table row carries a link to an official source.
3. Values that could not be confirmed are left blank and published on `flagged.html` — they are never inferred or estimated.
4. Where SAFE publishes Chinese and English versions, the Chinese text is used, because SAFE states that the Chinese prevails.
5. Superseded texts are cited only to explain an outdated figure, never to state current law.

Everything is research, not legal or tax advice. Bank branches apply these rules unevenly and individual facts decide the outcome.

## Licence and contributions

Content is compiled from public government and bank publications, each linked on the site. See `COORDINATION.md` for how parallel sessions should claim work.
