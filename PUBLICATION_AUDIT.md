# Publication integrity audit — 2026-11-11

## Executive conclusion

The existing dashboard offers an executive summary, decision questions, procedures, pros/cons, and $10,000–$400,000 ladders. **It does not establish the cheapest executable route for this account.** Current all-in costs and personal taxes remain unverified. Use [the strict blank-cost register](https://sassnarep3-star.github.io/China4/evidence.html) rather than interpreting historical scenarios as bank quotes.

The key unresolved facts are account identity/FX classification, source and year of funds, lawful purchase/remittance category, tax-paid records, US reporting history, and a same-time bank/provider quote. A different payment channel does not remove tax owed on underlying income. Never borrow quotas, misdescribe a payment, or split it to evade review.

## Scope and checks actually performed

- Rebuilt four generators; ran all six validators. All 16 root HTML pages have valid local link targets and anchors under the offline publication check. Existing validators rederive scenario arithmetic and check source-link presence. **These are not substantive line-by-line verification of every legal claim.** External-link availability and mobile visual rendering were not freshly certified by this session.
- Re-read selected official documents through page retrieval: [SAFE's 2007 explanation](https://www.safe.gov.cn/en/2007/0105/819.html) distinguishes individual FX sales from domestic-individual purchases and describes authenticity review above the quota. This historical explanation alone does not establish current personal eligibility.
- [IRS currency guidance](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates) requires tax amounts in functional currency, generally USD, using the relevant transaction-time rate. It does not supply a live consumer conversion quote or determine this person's tax.
- [GitHub's official custom-workflow requirements](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) require enabling the appropriate publishing mode and show the deployment step ID used by the environment URL.

## Confirmed publication irregularity and treatment

The authenticated Pages API reported `build_type: legacy`, source `main:/`, URL `https://sassnarep3-star.github.io/China4/`. For merge bb0040c, [Actions run 42949549582](https://github.com/sassnarep3-star/China4/actions/runs/42949549582) validated successfully but failed at Deploy to GitHub Pages. The independent [legacy run 42949549183](https://github.com/sassnarep3-star/China4/actions/runs/42949549183) succeeded. Failed-step metadata was retrieved; the detailed log-download host was inaccessible, so the exact error text was not verified.

An attempt to switch publishing mode returned HTTP 403, `Resource not accessible by integration`. This is a repository-settings permission limitation, not a request for credentials. During integration, concurrent PR #56 removed the redundant Actions deploy job. This session preserves that fix and adds an all-page link/anchor publication check in CI. There is no competing Actions deploy job. Legacy branch publishing remains active; it can expose root scripts, data, and coordination notes. No private financial records or secrets should be committed. An administrator can optionally enable Actions publishing to restrict the public payload to staged HTML/CSS/JSON.

The issue and verification limits are published on **Flagged for Review**. No personal fees or taxes were invented to fill missing values. No claim is made that every inherited external source was reverified in this session.
