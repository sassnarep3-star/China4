# China4

Research dashboard: how a US citizen can move funds held in a Chinese bank account
out of China as USD, what each legal route costs, and which penalties apply.

Built source-first: every value is traced to an official source, and anything that
cannot be confirmed from one is left blank and listed on the **Flagged for review**
page rather than inferred.

Live site: https://sassnarep3-star.github.io/China4/

## Pages

| Page | Contents |
|---|---|
| `index.html` | Dashboard and decision summary |
| `methods.html` | Every conversion route with pros, cons and official sources |
| `steps.html` | Step-by-step instructions for each route |
| `costs.html` | Cost estimator: $10,000–$400,000 in $10,000 steps, every legal route |
| `penalties.html` | Cost and penalty framework |
| `taxes.html` | US tax and reporting obligations |
| `flagged.html` | Unverified values and irregularities, with source links |
| `sources.html` | Every official source used |

`EXECUTIVE_SUMMARY.md` is the written executive summary.

## Build and verify

The site is static HTML. `costs.html` and `steps.html` are generated:

```
python3 scripts/build_costs.py
python3 scripts/verify_site.py
```

`verify_site.py` checks that every local link resolves, that every table row
carrying a value has an official-source link, and that all requested amounts from
$10,000 to $400,000 are present. Rows whose values are explicitly left blank are
exempt from the source check by design.

## Disclaimer

Research, not legal or tax advice. Not a bank quote and not a determination of
anyone's eligibility.
