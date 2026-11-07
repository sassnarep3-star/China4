/* “Conversion penalty” breakdown — separating myths, preconditions, friction costs and true penalties. */
window.DATA_COST_ROWS = [
  {
    item: "CNY→USD conversion tax (China)",
    type: "myth-busted",
    amount: "None",
    detail: "Buying FX (购汇) at a bank is a settlement act, not a taxable event. What banks demand is proof the RMB income was legal and taxed (完税证明 included in the source-of-funds file) — per 实施细则 art. 13 and the 2020 guideline art. 59. The perceived “conversion tax” is usually this tax-clearance requirement, plus bank charges.",
    status: "verified",
    source: { title: "SAFE Tianjin Q&A citing 2020 guideline art. 59", url: "https://www.safe.gov.cn/tianjin/2026/0713/3088.html" }
  },
  {
    item: "CNY→USD conversion tax (US)",
    type: "myth-busted",
    amount: "Personal FX gains may be taxable above the $200 exception",
    detail: "IRC §988(e)(1): this section “shall not apply to any section 988 transaction entered into by an individual which is a personal transaction.” §988(e)(2): on a personal disposition of foreign currency, “no gain shall be recognized… by reason of changes in exchange rates” — unless the gain on the transaction exceeds $200. Converting your own savings is therefore generally tax-free; a per-transaction FX gain above $200 may be taxable; its characterization depends on the transaction.",
    status: "verified",
    source: { title: "26 U.S.C. §988 (govinfo, official US Code text)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleA-chap1-subchapN-partIII-subpartJ-sec988.htm" }
  },
  {
    item: "China Individual Income Tax on the underlying income (wages/comprehensive income)",
    type: "precondition",
    amount: "7 progressive brackets, 3%–45% (see table below)",
    detail: "Banks convert what they can prove was taxed. If the account balance is salary/service/fees earned in China, IIT should already have been withheld by the payer (个人所得税法 arts 9–14). If it was NOT settled, it must be regularised with the tax authority first — with brackets per Table 1 of the amended law (60,000/yr basic deduction for residents; non-resident wages compute monthly after a 5,000/month deduction).",
    status: "verified",
    source: { title: "STA — Individual Income Tax Law (full text)", url: "https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html" },
    source2: { title: "STA Shanghai — Chairman’s Order No. 9 with Rate Table 1", url: "https://shanghai.chinatax.gov.cn/yptax/ztzl/xgrsdszc/201809/t441739.html" }
  },
  {
    item: "China IIT on property-transfer proceeds",
    type: "precondition",
    amount: "20% of the gain",
    detail: "财产转让所得 uses a 20% proportional rate on the gain (transfer income less original value and reasonable expenses). Registration authorities verify the tax voucher (完税凭证) when the property changes hands — so the chain exists before conversion (IIT Law arts 3(3), 6(5), 15).",
    status: "verified",
    source: { title: "STA — Individual Income Tax Law (full text)", url: "https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html" }
  },
  {
    item: "Outbound-payment tax filing (税务备案) for single payments > US$50,000",
    type: "precondition",
    amount: "Filing duty (not a tax rate); threshold US$50,000 per payment",
    detail: "STA/SAFE announcement 2013 No. 40 (amended 2021 No. 19): before a domestic institution/individual pays over US$50k in a single cross-border payment for services/income/current transfers (incl. 境外个人在境内的工作报酬), file the 服务贸易等项目对外支付税务备案表 with the competent tax authority. Exemptions listed in art. 3 (e.g. private study-travel-family use of FX); 境外个人 remitting own funds are handled under personal-FX rules (art. 4). The bank applies the FX rules after the stamped filing.",
    status: "verified",
    source: { title: "STA database — announcement 2013 No. 40 (as amended)", url: "https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html" }
  },
  {
    item: "Bank wire fee + cable fee (mainland China bank)",
    type: "friction cost",
    amount: "",
    detail: "Widely repeated figures (e.g. remittance fee 0.1% of the amount, min RMB 50 / max RMB 260, plus cable fee RMB 80/150) appear on secondary Q&A pages and third-party guides quoting Bank of China’s personal tariff — but the current personal tariff was not retrievable from an official BOC page in this project. Amount intentionally left blank: see Flagged for Review for the secondary references; confirm at your branch or the bank’s official price schedule.",
    status: "unverified",
    source: { title: "See Flagged for Review (FR-1)", url: "flagged.html#fr-1" }
  },
  {
    item: "Exchange-rate spread (bank sell rate vs mid-market)",
    type: "friction cost",
    amount: "",
    detail: "Banks sell USD at their posted cash/remittance sell rate, not the SAFE mid-price. One third-party guide measured a ~0.3% gap on a sample day — a single anecdotal data point, not an official rate schedule. Left blank here and listed for verification.",
    status: "unverified",
    source: { title: "See Flagged for Review (FR-2)", url: "flagged.html#fr-2" }
  },
  {
    item: "Intermediary / receiving-bank charges",
    type: "friction cost",
    amount: "",
    detail: "SWIFT transfers can be trimmed by correspondent banks and the receiving US bank. Bank of China’s official <em>corporate</em> price list states foreign-bank charges are passed through at cost (“凡业务发生的境外银行收费，按实收取”) — evidence of the mechanic, not of personal amounts. Personal charge amounts: unverified, see Flagged page.",
    status: "unverified",
    source: { title: "BOC official (corporate) tariff — fee-pass-through line", url: "https://www.boc.cn/cbservice/cb3/cb33/200807/t20080701_852.html" }
  },
  {
    item: "Overseas ATM withdrawal caps (opportunity/friction cost)",
    type: "friction cost",
    amount: "RMB 100,000/yr per person · RMB 10,000/day per card",
    detail: "汇发〔2017〕29号 caps mainland-bank-card overseas cash withdrawals; exceeding suspends overseas ATM access for the current AND next year. Card spending abroad is unaffected per the SAFE Q&A accompanying the notice.",
    status: "verified",
    source: { title: "gov.cn — 汇发〔2017〕29号", url: "https://www.gov.cn/xinwen/2017-12/31/content_5251954.htm" }
  },
  {
    item: "PENALTY — private/underground FX dealing (China)",
    type: "true-penalty",
    amount: "Fine ≤ 30% of amount; serious cases 30%–100%; illegal gains confiscated; possible criminal referral",
    detail: "外汇管理条例 (2008) art. 45. Same ladder in art. 39 for 逃汇 (moving FX abroad in violation/deception) and art. 40 for 套汇 (false documents). This is the “tax” that actually materialises if money exits illegally.",
    status: "verified",
    source: { title: "SAFE-hosted PDF — 外汇管理条例 arts 39, 40, 45", url: "https://www.safe.gov.cn/heilongjiang/file/file/20170728/c8dd4cfd7f9b432faa691b7d23395809.pdf" }
  },
  {
    item: "PENALTY — crypto channel (China)",
    type: "true-penalty",
    amount: "Activity banned; civil dealings void; related crimes referred to judicial organs",
    detail: "银发〔2021〕237号: all virtual-currency business activities (incl. offshore exchanges serving mainland residents) are illegal financial activities, strictly prohibited and demolished by law; civil acts contrary to public order are void and losses fall on participants.",
    status: "verified",
    source: { title: "gov.cn — 银发〔2021〕237号", url: "https://www.gov.cn/zhengce/zhengceku/2021-10/08/content_5641404.htm" }
  },
  {
    item: "PENALTY — FBAR non-filing (US)",
    type: "true-penalty",
    amount: "Statute: ≤ $10,000 (non-willful); willful: greater of $100,000 or 50% of the account balance",
    detail: "31 U.S.C. §5321(a)(5): civil money penalty for violating §5314 (FBAR) — ≤$10,000 baseline, reasonable-cause exception; willful violations: maximum becomes the greater of $100,000 or 50% of the balance/transaction amount. NOTE: these statutory figures are subject to inflation adjustment in the regulations — current-year numbers are on the Flagged page.",
    status: "verified",
    source: { title: "31 U.S.C. §5321(a)(5) (govinfo, official US Code text)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title31/html/USCODE-2023-title31-subtitleIV-chap53-subchapII-sec5321.htm" }
  },
  {
    item: "PENALTY — Form 8938 non-filing (US)",
    type: "true-penalty",
    amount: "$10,000 + $10,000 per 30-day period after 90-day IRS notice (add’l capped at $50,000)",
    detail: "26 U.S.C. §6038D(d): failure to disclose specified foreign financial assets → $10,000; continued failure after notice → +$10,000 per 30 days, capped at $50,000 additional; reasonable-cause exception (§6038D(g)).",
    status: "verified",
    source: { title: "26 U.S.C. §6038D (govinfo, official US Code text)", url: "https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm" }
  },
  {
    item: "PENALTY — Form 3520 non-filing (US)",
    type: "true-penalty",
    amount: "Penalties under IRC §6039F(c) — magnitude not confirmed in this project (see Flagged FR-6)",
    detail: "The IRS “Gifts from foreign person” page states: filing late or incomplete/incorrect Form 3520 may lead to penalties under section 6039F(c) unless reasonable cause. The widely cited 5%/month, 25%-cap figure comes from §6039F(c)’s text, which was NOT retrievable from an official source in this project — flagged rather than asserted.",
    status: "verified",
    source: { title: "IRS — Gifts from foreign person", url: "https://www.irs.gov/businesses/gifts-from-foreign-person" }
  },
  {
    item: "PENALTY — failing FinCEN 105 cash declaration (US)",
    type: "true-penalty",
    amount: "Forfeiture/seizure of the monetary instruments; civil/criminal penalties possible",
    detail: "CBP: individuals who fail to file or file falsely risk forfeiture and seizure of the currency/monetary instruments and may face civil or criminal penalties (31 U.S.C. 5317/5321/5322/5332; 31 CFR 1010). Carrying more than $10,000 itself is legal — non-declaration is the violation.",
    status: "verified",
    source: { title: "CBP — Money and Other Monetary Instruments", url: "https://www.cbp.gov/travel/international-visitors/money-monetary-instruments" }
  }
];

/* China IIT — Rate Table 1 (comprehensive income), verbatim from Chairman’s Order No. 9
   as republished by the Shanghai tax authority (official chinatax.gov.cn subdomain). */
window.DATA_IIT_BRACKETS = [
  { bracket: "1", taxable: "≤ RMB 36,000", rate: "3%" },
  { bracket: "2", taxable: "> RMB 36,000 – 144,000", rate: "10%" },
  { bracket: "3", taxable: "> RMB 144,000 – 300,000", rate: "20%" },
  { bracket: "4", taxable: "> RMB 300,000 – 420,000", rate: "25%" },
  { bracket: "5", taxable: "> RMB 420,000 – 660,000", rate: "30%" },
  { bracket: "6", taxable: "> RMB 660,000 – 960,000", rate: "35%" },
  { bracket: "7", taxable: "> RMB 960,000", rate: "45%" }
];
