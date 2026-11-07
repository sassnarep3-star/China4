# China Money — CNY to USD Field Guide

A static, source-linked dashboard on lawful ways to convert or use funds held in a mainland China bank account, the distinction between FX controls and taxes, U.S. tax/account-reporting considerations, transaction requirements, and facts still requiring bank or professional confirmation.

## Live site

After GitHub Pages has deployed, open the repository's Pages URL from **Settings → Pages** (the `github-pages` deployment job also publishes the URL). Pages deployment is automated on pushes to `main` and can be manually triggered from Actions.

## Pages

- [Executive summary](index.html)
- [Transfer route comparison](routes/)
- [Tax and costs](tax/)
- [Document/process requirements](requirements/)
- [Official source register](sources/)
- [Flagged for Review](review/)
- [Detailed methodology and findings](research/findings.md)
- [Coordination board](COORDINATION.md)

## Key finding

The SAFE annual USD 50,000 equivalent amount is an ID-only facilitation threshold for specified settlement and FX-purchase categories; it is not described as a tax or universal hard ceiling. Purchase-quota eligibility depends on customer category, including domestic individuals and overseas individuals holding a Chinese foreign permanent-residence ID. Genuine, lawful transactions may be processed above the facilitation threshold with supporting evidence and bank review. A U.S. citizen should first confirm how the bank classifies the account holder and whether the balance is qualifying legal current-account income, existing foreign currency, or another category. No account-specific outcome is assumed.

## Research scope and limitations

- Research snapshot: 7 November 2026 (UTC).
- Sources are linked directly to SAFE, China's State Taxation Administration and Customs, U.S. IRS, FinCEN, and the U.S. Government Publishing Office/U.S. Code.
- Each displayed data-table row links to at least one official source. Unverified numerical values (bank quote, wire charges, tax amount, net USD) are left blank.
- Published rules do not substitute for a bank's written, current handling of the actual account or an individualized tax opinion. Older SAFE materials are flagged for current confirmation.
- Do not use false-purpose invoices, split payments or another person's quota, underground transfer, or crypto/P2P channels to evade controls.
- This material is general research, not legal/tax advice or a guarantee that a bank will accept a specific transaction.

## Build and verify locally

No package install is required. Run:

```sh
python3 assets/verify.py
```

The verifier checks page-local navigation, JSON validity, official-source domains for all data rows, required row citations, and that unverified fee amounts stay blank. GitHub Actions runs it for pull requests and deploys the static files to Pages on `main`.
