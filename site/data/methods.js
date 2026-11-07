/* Conversion/remittance channels. Regulatory facts in "how/limit" are drawn from the linked
   official sources (read line-by-line on 2026-11-07). Fee percentages reported by secondary
   sources are NOT shown here as fact — they are on the Flagged for Review page. */
window.DATA_METHOD_GROUPS = [
  {
    id: "primary",
    title: "A — Primary legal channels (recommended)",
    intro: "Fully compliant routes. The recurring theme of SAFE’s own Q&As: conversion is capped by what you can DOCUMENT as legal, taxed income — usually not by the US$50k convenience quota.",
    methods: [
      {
        name: "Documented after-tax income conversion at a bank (境外个人 channel) + international wire",
        category: "Bank purchase of FX against proven CNY income",
        status: "verified",
        statusLabel: "Recommended · fully legal",
        how: "As a foreign national (境外个人), bring your passport plus an audit trail — employment/service contract, employer income statement, bank entry records and the tax records (完税凭证/代扣代缴记录) — to the counter of your bank (e.g. a major FX-designated bank). The bank converts your <em>documented</em> legal CNY income to USD (汇发〔2007〕1号 art. 13; 2020 guideline art. 59) and wires it to your own account abroad. No fixed numerical ceiling is specified for qualifying documented current-account income; the bank must verify eligibility and supporting documents. If a single payment exceeds US$50,000 from a domestic payer to overseas, a tax filing form (税务备案表) may be required first (STA/SAFE 2013 No. 40); 境外个人 remitting own funds are handled under personal-FX rules (art. 4 of that announcement).",
        limit: "No fixed numerical ceiling for qualifying documented income",
        cost: "No general conversion tax identified; US currency gains may be taxable. Bank wire fee + sell-rate spread apply (amounts flagged as unverified). Underlying income must already bear China IIT (see Costs page).",
        pros: [
          "The exact channel SAFE built for this situation — explicitly confirmed for foreign employees’ salary in SAFE branch Q&As",
          "No artificial US$50k ceiling when documents are complete",
          "Clean audit trail that also satisfies US-side money-transfer questions",
          "Works for salary, service fees, rental income and documented property-sale proceeds"
        ],
        cons: [
          "Paperwork-heavy: bank reviews client, contract, income and tax records for consistency",
          "Money whose Chinese tax was never settled will be blocked until regularised (see IIT brackets on Costs page)",
          "Bank sell rate includes a spread; counter fees vary — see Flagged page for estimates to verify",
          "Once in an FX account in China, daily wire-out above US$50k requires current-account transaction documents (实施细则 art. 14)"
        ],
        sources: [
          { title: "SAFE Tianjin Q&A (2026) — guideline art. 59", url: "https://www.safe.gov.cn/tianjin/2026/0713/3088.html" },
          { title: "实施细则 full text (arts 13–15)", url: "https://www.safe.gov.cn/tianjin/2024/0430/2464.html" },
          { title: "STA/SAFE 2013 No. 40 (税务备案)", url: "https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html" },
          { title: "SAFE Hebei Q&A (2019) — salary & property-sale proceeds", url: "https://www.safe.gov.cn/hebei/2019/0118/1253.html" }
        ]
      },
      {
        name: "US$50,000 annual convenience quota (购汇便利化额度)",
        category: "Quota-based conversion at bank/app, ID only",
        status: "conditional",
        statusLabel: "Legal · situational",
        how: "ID-only conversion of up to US$50,000 equivalent per year. It applies to (a) 境内个人 (Chinese ID holders) buying FX, and (b) anyone’s 结汇 (selling FX into CNY). A US citizen on a work visa is an 境外个人 and SAFE says ordinary 境外个人 do <strong>not</strong> get the purchase quota — they use channel A1 above. Holders of a Chinese Permanent Residence ID Card (外国人永久居留身份证) DO qualify for the purchase quota.",
        limit: "US$50,000 equivalent per person per year",
        cost: "No conversion tax. Buy/sell spread only (rate set by the bank; estimates on Flagged page).",
        pros: [
          "Simplest possible route: valid ID only, at counter or app",
          "Above-quota remains possible with transaction-amount documents (SAFE: the quota is not a hard cap)"
        ],
        cons: [
          "Generally unavailable to a US citizen without a Chinese PR card",
          "Funds bought under the quota still need a lawful declared purpose for outbound use",
          "Never borrow someone else’s quota — that is prohibited splitting (see Section C)"
        ],
        sources: [
          { title: "2020 guideline arts 54–55 (gov.cn)", url: "https://www.gov.cn/zhengce/zhengceku/2020-08/31/content_5538828.htm" },
          { title: "SAFE Ningxia Q&A — quota is not a cap", url: "https://www.safe.gov.cn/ningxia/2022/0929/1997.html" },
          { title: "SAFE Tianjin Q&A — no quota for ordinary 境外个人", url: "https://www.safe.gov.cn/tianjin/2024/0621/2529.html" },
          { title: "SAFE Tianjin Q&A — PR-card holders qualify", url: "https://www.safe.gov.cn/tianjin/2025/1113/2926.html" }
        ]
      },
      {
        name: "Licensed fintech remittance (Wise) — CNY send-out",
        category: "App-based transfer to your own foreign account",
        status: "verified",
        statusLabel: "Legal · provider limits",
        how: "Wise states it enabled sending money OUT of China in July 2023: you convert CNY to USD/other currencies and send to <strong>your own</strong> bank account abroad or Wise balance. Per its own guide: max CNY 100,000 per transaction; the overall limit depends on your annual income in China and the tax you paid on it (i.e. it enforces the same documented-income principle).",
        limit: "CNY 100,000 per transfer (provider); total tied to documented taxed income",
        cost: "Provider fee + stated rate; exact CNY→USD fee not captured from an official pricing page → see Flagged page.",
        pros: [
          "Entirely online; built for foreign workers in China",
          "Operates inside the regulated documented-income framework",
          "Good for medium recurring amounts once identity/income verification is done"
        ],
        cons: [
          "Own-account only (no payments to third parties)",
          "Requires income/tax verification; limits scale with documented income",
          "Current availability/fees must be confirmed on Wise’s own pages (commercial source)"
        ],
        sources: [
          { title: "Wise — “Does Wise work in China” (provider’s own guide)", url: "https://wise.com/en-cn/blog/wise-work-in-china-send-money-to-and-from-china" }
        ]
      },
      {
        name: "UnionPay bank card — overseas ATM withdrawals & card spending",
        category: "Use Chinese cards abroad instead of converting funds",
        status: "verified",
        statusLabel: "Legal · supplements",
        how: "Spend with your UnionPay card abroad (card consumption is explicitly unaffected by withdrawal caps) and withdraw foreign-currency cash at ATMs. Cash withdrawals: all your mainland cards combined may not exceed RMB 100,000 equivalent per calendar year; each card is limited to RMB 10,000 equivalent per day (汇发〔2017〕29号). Over-limit → overseas ATM withdrawals suspended for the current and next calendar year. Conversion happens at the card network/bank rate.",
        limit: "RMB 100,000/yr (ATM cash, per person); RMB 10,000/day per card; card spending unaffected",
        cost: "ATM/issuer charges and conversion at card-network rates — figures vary by issuer (listed on Flagged page as unverified).",
        pros: [
          "Zero paperwork for amounts within the caps",
          "Works without converting a lump sum in China first",
          "Spending directly (hotels, tuition, living costs) is not capped by this rule"
        ],
        cons: [
          "Cash trickle only — unsuitable for moving a large balance",
          "Hard suspension of ATM access for 2 years if you exceed the annual cap",
          "You receive local-currency notes, not a USD bank balance"
        ],
        sources: [
          { title: "gov.cn — 汇发〔2017〕29号 full text", url: "https://www.gov.cn/xinwen/2017-12/31/content_5251954.htm" }
        ]
      },
      {
        name: "Carrying physical cash out of China",
        category: "Border cash rules + US entry declaration",
        status: "verified",
        statusLabel: "Legal · small scale",
        how: "Exit China with up to US$5,000 equivalent in foreign currency cash without any certificate; US$5,000–10,000 requires a bank-issued Carrying Certificate (携带证); above US$10,000 is in principle not permitted (special circumstances only, via a SAFE-issued certificate). RMB cash is capped at RMB 20,000 per trip. On arrival in the US, amounts over US$10,000 (cash or monetary instruments) must be reported to CBP on FinCEN Form 105 — reporting is not a tax and there is no cap on what you may legally bring in.",
        limit: "≤ US$5,000 free; ≤ US$10,000 with certificate; > US$10,000 restricted",
        cost: "No tax at either border. Bank may charge for the certificate (unverified, nominal). Risk: theft/loss, seizure risk if declarations or other applicable rules are violated.",
        pros: [
          "Immediate, bank-free transfer of small amounts",
          "No quota mechanics involved in the permitted tiers"
        ],
        cons: [
          "Useless for a large bank balance (effectively capped near US$10k/trip)",
          "Repeat crossings trigger tighter limits (same-day/15-day rules) — see source for detail",
          "Skipping the US FinCEN 105 declaration risks forfeiture of the whole amount (CBP)"
        ],
        sources: [
          { title: "gov.cn Gazette — Carrying Certificate rules", url: "https://www.gov.cn/gongbao/content/2004/content_63085.htm" },
          { title: "State Council OCA — RMB 20,000 limit", url: "https://www.gqb.gov.cn/news/2024/0320/58569.shtml" },
          { title: "CBP — Money and Monetary Instruments (FinCEN 105)", url: "https://www.cbp.gov/travel/international-visitors/money-monetary-instruments" }
        ]
      },
      {
        name: "Reconversion of leftover CNY from a previous exchange",
        category: "原兑回 channel",
        status: "verified",
        statusLabel: "Legal · small scale",
        how: "CNY you originally bought by converting USD (or other FX) can be re-converted back with your passport and the original exchange slip (原兑换水单) within 24 months of the original exchange (实施细则 art. 13(2)); tiny amounts (≤ US$500/day cumulative, or ≤ US$1,000 pre-departure at port-side venues) need only ID.",
        limit: "Original slips valid 24 months",
        cost: "Bank reconversion rate spread.",
        pros: ["No income documentation needed — the slip proves the origin", "Straightforward counter service"],
        cons: ["Only covers funds that were once FX-dealt in", "Slips older than 24 months are not usable"],
        sources: [
          { title: "实施细则 full text (art. 13)", url: "https://www.safe.gov.cn/tianjin/2024/0430/2464.html" }
        ]
      }
    ]
  },
  {
    id: "special",
    title: "B — Large-balance & special-purpose channels",
    intro: "For one-time or large exits: documented asset sales and the SAFE-administered transfer programs.",
    methods: [
      {
        name: "Sale of China real estate / assets → convert proceeds → remit",
        category: "Capital-item conversion with tax clearance",
        status: "verified",
        statusLabel: "Legal · documented",
        how: "Foreign nationals may convert and remit <em>documented</em> proceeds such as the sale of an apartment in China (SAFE Hebei Q&A lists 境内房产转让收入 alongside salary). Expect: transfer contract + registration proof, evidence the deed was transferred, tax payment certificates, and — where applicable, relevant outbound payment tax filing documentation (STA/SAFE 2013 No. 40; foreign individuals follow personal FX rules). Property-transfer income carries a flat 20% China IIT (个人所得税法 art. 3(3)); registration authorities check the tax voucher at transfer (art. 15).",
        limit: "Amounts equal to documented, taxed proceeds",
        cost: "20% IIT on the property-transfer gain (sale price less original cost and reasonable expenses) + deed/misc taxes at sale; bank wire costs after conversion.",
        pros: [
          "Established route for large one-off balances",
          "Tax clearance both unlocks the transfer and creates the perfect source-of-funds record for US purposes"
        ],
        cons: [
          "Slow; multiple agencies (property registration, tax, bank)",
          "20% IIT on gains is a real cost — but it is the property tax, not a conversion tax",
          "The €/¥ proceeds must match the documented transaction"
        ],
        sources: [
          { title: "SAFE Hebei Q&A (2019)", url: "https://www.safe.gov.cn/hebei/2019/0118/1253.html" },
          { title: "STA/SAFE 2013 No. 40 — outbound-payment tax filing", url: "https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html" },
          { title: "Individual Income Tax Law (arts 3, 15)", url: "https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html" }
        ]
      },
      {
        name: "Emigration / inheritance asset transfer program (移民财产转移 / 继承财产转移)",
        category: "SAFE-approved lump-sum transfer",
        status: "verified",
        statusLabel: "Legal · requires SAFE approval",
        how: "If you emigrated from mainland China (or inherited a mainland estate as a foreign citizen), PBOC Announcement 2004 No. 16 lets you apply to SAFE to liquidate and remit your legal assets abroad. Apply at the SAFE branch where your household registration was (or the deceased’s). ≤ RMB 500k approved locally; larger cases go to SAFE HQ. Emigration transfers are applied for in one go and paid out in stages within ~2 years (≤ RMB 200k can go in one shot). The bank remits according to the approved application — no cash withdrawal in China. Tax clearance for inherited property is part of the file.",
        limit: "Approval-based; staged payout over ~2 years for large emigration transfers",
        cost: "No conversion tax; asset liquidation taxes (e.g. property IIT) must be cleared as part of approval.",
        pros: [
          "A designated route for qualifying emigration asset transfers",
          "Explicitly designed for foreign citizens inheriting mainland estates",
          "Full legal cover: SAFE approval document satisfies both Chinese and US compliance questions"
        ],
        cons: [
          "Only available if you (or the estate) meet the emigration/inheritance criteria — not for money earned while simply working there",
          "Multi-month process with notarised/consular documents",
          "Assets under dispute, or of unproven legality, are refused"
        ],
        sources: [
          { title: "SAFE portal — PBOC Announcement 2004 No. 16 full text", url: "http://m.safe.gov.cn/safe/2004/1116/5461.html" }
        ]
      },
      {
        name: "Family remittances under each relative’s own quota (gifts / family support)",
        category: "Chinese-citizen relatives remit their own funds",
        status: "conditional",
        statusLabel: "Legal with strict conditions",
        how: "A Chinese-citizen relative (境内个人) may use their <em>own</em> US$50k annual convenience quota to convert and remit their <em>own</em> money to you abroad (e.g. as a gift or family support — a recognised current-account use). The vital distinction in Chinese law: borrowing other people’s quotas to move YOUR money is prohibited splitting (PBOC Order 2006 No. 3 art. 7; SAFE Shanghai guidance). US side: gifts from foreign persons are not taxable income to you, but aggregate gifts from related foreign persons above US$100,000 in a tax year must be reported on Form 3520 Part IV — informational only, no tax.",
        limit: "US$50k per relative per year (their own funds only)",
        cost: "Sender pays bank wire costs (fee figures unverified — see Flagged page); recipient owes no US income tax on a genuine gift.",
        pros: [
          "Legitimate for genuine intra-family transfers — sanctioned quota use, not evasion",
          "Keeps a clean documentary chain when the gift and kinship are real"
        ],
        cons: [
          "Cannot be used to launder YOUR balance through relatives’ names — that is exactly the prohibited “蚂蚁搬家” pattern",
          "Bank will assess the remittance purpose/authenticity",
          "Recipient must aggregate related donors for the US$100k Form 3520 trigger"
        ],
        sources: [
          { title: "个人外汇管理办法 art. 7 (gov.cn Gazette)", url: "https://www.gov.cn/gongbao/content/2007/content_786257.htm" },
          { title: "SAFE Shanghai guidance — do not lend/borrow quotas", url: "http://www.safe.gov.cn/shanghai/2019/1213/1198.html" },
          { title: "IRS — Gifts from foreign person (Form 3520 thresholds)", url: "https://www.irs.gov/businesses/gifts-from-foreign-person" }
        ]
      },
      {
        name: "Cross-border e-commerce settlement (business income)",
        category: "Merchant channel — not for private savings",
        status: "verified",
        statusLabel: "Legal · business only",
        how: "SAFE Shanghai’s 2026 policy Q&A confirms: 境内个人 engaged in cross-border e-commerce can settle through their FX account, and settlement with transaction-amount materials or electronic transaction data does NOT consume the annual convenience quota. Relevant only if the stuck money is legitimate business revenue.",
        limit: "Documented transaction amounts",
        cost: "Platform/bank settlement charges; income tax still applies to the business revenue.",
        pros: ["Built for exactly this data-rich business case", "No quota consumption"],
        cons: ["Requires genuine e-commerce transaction data", "Not applicable to personal savings or salary"],
        sources: [
          { title: "SAFE Shanghai — 2026 policy Q&A (跨境电商结售汇)", url: "https://www.safe.gov.cn/shanghai/2026/0402/2412.html" }
        ]
      },
      {
        name: "Alipay / WeChat Pay in-app international remittance",
        category: "Super-app remittance products",
        status: "unverified",
        statusLabel: "Conditionally available — details unverified",
        how: "Per Wise’s own guide, Alipay’s in-app international transfer feature is currently <strong>not</strong> usable by foreigners to send money OUT of China (Chinese users can send/receive within quota rules). Availability and limits change and may depend on the partner bank product. Current policies must be confirmed with Alipay/WeChat directly.",
        limit: "— (unverified)",
        cost: "— (unverified; provider’s published pricing should be checked in-app)",
        pros: ["Very convenient UX when it applies", "Runs inside the quota framework for eligible Chinese-national senders"],
        cons: [
          "A third-party guide says the feature may not be available to foreigners — confirm current status",
          "Limits/fees/tax documentation not verified from an official provider page → see Flagged page"
        ],
        sources: [
          { title: "Wise guide on Alipay international transfers (provider statement)", url: "https://wise.com/en-cn/blog/alipay-international-transfer-sending-and-receiving" }
        ]
      }
    ]
  },
  {
    id: "prohibited",
    title: "C — Prohibited or illegal “shortcuts” (do NOT use)",
    intro: "These circulate online as ways to beat the system. Each is tied here to the official rule or penalty text. “Pros” are why people attempt them; “cons” are the legal consequences.",
    methods: [
      {
        name: "Underground banks / “对敲” mirror transfers",
        category: "Illegal private FX dealing",
        status: "prohibited",
        statusLabel: "Illegal — heavy penalties",
        how: "You pay CNY to a domestic account controlled by an underground bank; an associate pays USD abroad to your account. China treats this as 私自/变相买卖外汇 (private or disguised FX dealing): under 外汇管理条例 art. 45 — warning, confiscation of illegal gains, and a fine up to 30% of the amount; in serious cases 30% up to 100% of the amount; criminal referral where it constitutes a crime. PBOC Order 2006 No. 3 art. 30 requires FX transactions go through licensed institutions.",
        limit: "—",
        cost: "Fines up to 100% of the amount + confiscation + criminal exposure; funds can be frozen as criminal proceeds.",
        pros: ["None that survive the risks below — speed and “no questions” are the lure"],
        cons: [
          "Fine of up to the FULL amount in serious cases (art. 45)",
          "Possible criminal prosecution (illegal-business-operation charges are applied to underground FX per SPC/SPP interpretation — primary text pending on Flagged page)",
          "Zero legal protection if the counterparty vanishes with your CNY",
          "Incoming unexplained USD can itself trigger US review"
        ],
        sources: [
          { title: "SAFE-hosted PDF — 外汇管理条例 (arts 39, 45)", url: "https://www.safe.gov.cn/heilongjiang/file/file/20170728/c8dd4cfd7f9b432faa691b7d23395809.pdf" },
          { title: "个人外汇管理办法 arts 7, 30 (gov.cn Gazette)", url: "https://www.gov.cn/gongbao/content/2007/content_786257.htm" }
        ]
      },
      {
        name: "Splitting (“蚂蚁搬家”): stacking other people’s quotas or cards",
        category: "Prohibited quota evasion",
        status: "prohibited",
        statusLabel: "Prohibited",
        how: "Recruiting 5+ friends/relatives to each convert US$50k and forward it to the same overseas account, or splitting your own transfers across many cards/accounts to dodge caps. PBOC Order 2006 No. 3 art. 7 forbids evading quota/authenticity management by splitting; SAFE Shanghai guidance: never lend your quota or borrow others’. The old detection fingerprints (汇发〔2009〕56号) and 2-year watch list (汇发〔2015〕43号) are marked repealed on SAFE’s site — the overarching prohibition stands, and banks report suspicious splitting to SAFE.",
        limit: "—",
        cost: "Fines under 外汇管理条例 for quota-evasion conduct recorded in SAFE enforcement bulletins (amounts on Flagged page, awaiting primary-source confirmation).",
        pros: ["Appears “each-transaction-legal” — that is precisely the design the rules target"],
        cons: [
          "Explicitly prohibited conduct — not a loophole",
          "Banks must refuse/report structured patterns",
          "Everyone involved (not just the organiser) can be sanctioned"
        ],
        sources: [
          { title: "个人外汇管理办法 art. 7 (gov.cn Gazette)", url: "https://www.gov.cn/gongbao/content/2007/content_786257.htm" },
          { title: "SAFE Shanghai guidance (2019)", url: "http://www.safe.gov.cn/shanghai/2019/1213/1198.html" },
          { title: "汇发〔2009〕56号 (marked repealed)", url: "https://www.safe.gov.cn/big5/big5/www.safe.gov.cn/safe/2009/1125/5439.html" }
        ]
      },
      {
        name: "Cryptocurrency OTC (buy USDT with CNY → sell for USD abroad)",
        category: "Illegal financial activity in PRC",
        status: "prohibited",
        statusLabel: "Illegal in China",
        how: "Ten regulators (PBOC, SAFE,公安部 etc.) in 银发〔2021〕237号: Virtual-currency-related business activity — including fiat↔crypto exchange and offshore exchanges serving mainland residents — is an illegal financial activity, strictly prohibited. Crypto-related civil dealings are void and losses fall on the participant. Banks/payment firms may not service crypto transfers and actively monitor accounts.",
        limit: "—",
        cost: "No legal protection (contracts void); accounts frozen in monitoring actions; potential liability per the notice.",
        pros: ["Technically frictionless — that is why it is the #1 monitored off-ramp"],
        cons: [
          "Expressly illegal as a business activity in China",
          "Managing a CNY→USDT→USD chain can be characterised as disguised FX dealing (art. 45 penalties)",
          "Bank-account freezes and counterparty fraud are endemic in OTC markets"
        ],
        sources: [
          { title: "gov.cn — 银发〔2021〕237号 full text", url: "https://www.gov.cn/zhengce/zhengceku/2021-10/08/content_5641404.htm" }
        ]
      },
      {
        name: "Fake trade invoices / mis-invoiced corporate transfers",
        category: "Fraudulent trade settlement (逃汇/套汇)",
        status: "prohibited",
        statusLabel: "Illegal — criminal exposure",
        how: "Routing personal money through fabricated import/export contracts. 外汇管理条例 art. 39 (逃汇: moving domestic FX abroad in violation or by deception) and art. 40 (obtaining FX with false/invalid documents): order to repatriate, fine up to 30% of the amount; in serious cases 30%–100%; criminal referral.",
        limit: "—",
        cost: "Fines scaled to the amount (up to 100%) + criminal liability for serious cases + company-level liability.",
        pros: ["None — this is document fraud on its face"],
        cons: [
          "Art. 39/40 fines can reach the full amount",
          "Bank authenticity review (KYC/documentation) is specifically built to catch this",
          "Tax fraud exposure on the fabricated trade on top of FX violations"
        ],
        sources: [
          { title: "SAFE-hosted PDF — 外汇管理条例 (arts 39–40)", url: "https://www.safe.gov.cn/heilongjiang/file/file/20170728/c8dd4cfd7f9b432faa691b7d23395809.pdf" }
        ]
      }
    ]
  }
];
