/* US-side tax & reporting obligations for a citizen moving CNY → USD out of China.
   Every "verified" row was read on the linked official page on 2026-11-07. */
window.DATA_US_ROWS = [
  {
    regime: "FBAR (FinCEN Form 114)",
    trigger: "Aggregate value of ALL foreign financial accounts exceeds $10,000 at any time in the calendar year",
    action: "File electronically via FinCEN’s BSA E-Filing System (individuals may file without registering). Not a tax form — a disclosure.",
    penalty: "31 U.S.C. §5321(a)(5): ≤ $10,000 non-willful; willful → greater of $100,000 or 50% of balance (statutory figures; inflation-adjusted amounts flagged)",
    notes: "Your China bank accounts count while they remain open — before, during and after the transfer. IRS guidance confirms the $10,000 aggregate-at-any-time test; FinCEN page hosts the filing channel and due-date clarification PDFs.",
    status: "verified",
    source: { title: "IRS newsroom — FBAR details", url: "https://www.irs.gov/newsroom/details-on-reporting-foreign-bank-and-financial-accounts" },
    source2: { title: "FinCEN — Report Foreign Bank and Financial Accounts", url: "https://www.fincen.gov/report-foreign-bank-and-financial-accounts" },
    source3: { title: "31 U.S.C. §5321 (govinfo)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title31/html/USCODE-2023-title31-subtitleIV-chap53-subchapII-sec5321.htm" }
  },
  {
    regime: "Form 8938 — FATCA specified foreign financial assets",
    trigger: "More than $50,000 on the last day / $75,000 at any time (unmarried, living in the US); married filing jointly in the US: $100,000 / $150,000. “living abroad” higher thresholds exist but were not confirmed on the IRS page captured → Flagged page.",
    action: "Attach to the annual income tax return.",
    penalty: "26 U.S.C. §6038D(d): $10,000; +$10,000 per 30 days of continued failure after IRS notice, additional penalties capped at $50,000; reasonable-cause exception (§6038D(g)).",
    notes: "Statutory baseline in §6038D(a) is aggregate value > $50,000; IRS sets the higher filing-status thresholds. Foreign bank accounts held during the transfer year are covered.",
    status: "verified",
    source: { title: "IRS — Do I need to file Form 8938", url: "https://www.irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets" },
    source2: { title: "26 U.S.C. §6038D (govinfo)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm" }
  },
  {
    regime: "Form 3520 — large foreign gifts/bequests (Part IV)",
    trigger: "More than $100,000 received during the tax year from a nonresident alien individual or foreign estate (aggregated with related foreign persons); foreign corporations/partnerships: > $20,116 (2025) / $20,573 (2026, inflation-adjusted). Each gift over $5,000 itemised once triggered.",
    action: "File Form 3520 by the 15th day of the 4th month after tax-year end (generally April 15; June 15 if living abroad; extensions do not go beyond Oct 15 for this form).",
    penalty: "Penalties possible under IRC §6039F(c) per the IRS page; numeric schedule unverified in this project → Flagged FR-6.",
    notes: "The gift itself is generally NOT US-taxable income to the recipient — Form 3520 is an information return. Directly relevant if Chinese relatives send you family gifts from China.",
    status: "verified",
    source: { title: "IRS — Gifts from foreign person", url: "https://www.irs.gov/businesses/gifts-from-foreign-person" },
    source2: { title: "IRS — Instructions for Form 3520 (“Who Must File”, item 4)", url: "https://www.irs.gov/instructions/i3520" },
    source3: { title: "IRS — About Form 3520", url: "https://www.irs.gov/forms-pubs/about-form-3520" }
  },
  {
    regime: "FinCEN Form 105 (CMIR) — physical cash/monetary instruments across the US border",
    trigger: "Entering or leaving the US physically transporting, mailing or shipping more than $10,000 in currency/monetary instruments (household members travelling together are aggregated).",
    action: "File FinCEN Form 105 — electronically before travel at fincen105.cbp.dhs.gov, or on paper at the port of entry/departure. There is NO limit on how much you may legally carry.",
    penalty: "Failure to file (or false filing): forfeiture/seizure of the instruments and possible civil or criminal penalties (CBP cites 31 U.S.C. 5317/5321/5322/5332; 31 CFR 1010).",
    notes: "Relevant only if you choose the cash-carriage channel out of China (which itself is capped near US$10k/trip by Chinese rules).",
    status: "verified",
    source: { title: "CBP — Money and Other Monetary Instruments", url: "https://www.cbp.gov/travel/international-visitors/money-monetary-instruments" }
  },
  {
    regime: "Foreign-currency conversion gains — IRC §988",
    trigger: "Disposition of nonfunctional currency (e.g. converting CNY to USD).",
    action: "Personal transactions of an individual are excluded from §988 (§988(e)(1)); even within a personal transaction, FX gain is not recognized unless the gain “exceeds $200” per transaction (§988(e)(2)).",
    penalty: "None for the ordinary personal conversion; gains above $200 may be taxable; their characterization depends on the transaction.",
    notes: "Moving your own money is not a taxable event in itself; currency appreciation may be taxable depending on the transaction.",
    status: "verified",
    source: { title: "26 U.S.C. §988 (govinfo)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleA-chap1-subchapN-partIII-subpartJ-sec988.htm" }
  },
  {
    regime: "Foreign Tax Credit (Form 1116)",
    trigger: "China IIT withheld/paid on the same income the US taxes.",
    action: "Claim a credit (or itemized deduction) for qualifying foreign income taxes on Form 1116; subject to eligibility and limitations, including rules for excluded income.",
    penalty: "—",
    notes: "Prevents double taxation of the Chinese salary that later gets wired out; operate at the income-tax return, independent of the remittance.",
    status: "verified",
    source: { title: "IRS — Foreign Tax Credit", url: "https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit" }
  },
  {
    regime: "USD translation rule",
    trigger: "Any foreign-currency income/expense affecting US tax computation.",
    action: "Translate at the exchange rate prevailing when received/paid/accrued; US tax determinations generally use USD, subject to functional currency rules; reference rates: Treasury Reporting Rates of Exchange.",
    penalty: "—",
    notes: "Use Treasury Dec-31 rate for FBAR account values (per IRS newsroom page’s valuation guidance).",
    status: "verified",
    source: { title: "IRS — Foreign currency and currency exchange rates", url: "https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates" }
  }
];
