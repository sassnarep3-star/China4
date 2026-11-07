/* China-side FX rules — every row cross-checked against the linked official page on 2026-11-07.
   Status "verified" = the claim text was read on the official page itself.
   Status "historical" = official page exists but the document is marked repealed (已废止). */
window.DATA_RULES = [
  {
    area: "Individual conversion quota",
    rule: "USD 50,000 / person / year is a convenience quota — not a hard cap",
    detail: "个人结汇和境内个人购汇实行年度便利化额度管理，便利化额度分别为每人每年等值5万美元。个人凭本人有效身份证件在银行办理年度便利化额度内的结汇和购汇。SAFE Q&A adds: the quota is NOT an annual limit — above-quota business is allowed with supporting documents (see rows below).",
    value: "US$50,000 equivalent/year",
    status: "verified",
    source: { title: "SAFE — Current Account FX Business Guideline (2020), arts 54–55 (汇发〔2020〕14号, gov.cn)", url: "https://www.gov.cn/zhengce/zhengceku/2020-08/31/content_5538828.htm" }
  },
  {
    area: "Individual conversion quota",
    rule: "Quota is not a limit: current-account conversions above US$50k are lawful with documents",
    detail: "SAFE policy Q&A: “我国对于真实、合法的经常项目和已开放的资本项目下购汇和结汇都没有金额限制…年度便利化额度不是个人每年购汇或者结汇的限额，只是超过等值5万美元的购汇或结汇不能仅凭本人有效身份证件办理.”",
    value: "No cap for genuine documented current-account items",
    status: "verified",
    source: { title: "SAFE Ningxia branch — policy Q&A (2022)", url: "https://www.safe.gov.cn/ningxia/2022/0929/1997.html" }
  },
  {
    area: "Foreign nationals (境外个人)",
    rule: "Foreign nationals convert legal CNY income with ID + income-source documents incl. tax vouchers — no fixed ceiling",
    detail: "Guideline 2020 art. 59: “境外个人在境内取得的经常项目合法人民币收入，凭本人有效身份证件和有交易额的购汇资金来源材料（含税务凭证）在银行办理购汇.” Also 《个人外汇管理办法实施细则》art. 13: same rule + reconversion of unused CNY within 24 months with the original exchange slip (原兑换水单).",
    value: "Documented amount; no fixed ceiling",
    status: "verified",
    source: { title: "SAFE Tianjin branch — personal FX Q&A (2026)", url: "https://www.safe.gov.cn/tianjin/2026/0713/3088.html" },
    source2: { title: "SAFE Tianjin — 个人外汇管理办法实施细则 full text (art. 13)", url: "https://www.safe.gov.cn/tianjin/2024/0430/2464.html" }
  },
  {
    area: "Foreign nationals (境外个人)",
    rule: "Ordinary foreign passport holders do NOT get the US$50k purchase convenience quota",
    detail: "SAFE: 境外个人 do not use the purchase convenience quota; they buy FX against documented legal RMB income instead. Exception: holders of the Foreigner’s Permanent Residence ID Card (外国人永久居留身份证) DO qualify for the US$50k purchase convenience quota.",
    value: "Quota: none (except PR-card holders)",
    status: "verified",
    source: { title: "SAFE Tianjin — Q&A 2024 (境外个人是否享受年度便利化额度购汇)", url: "https://www.safe.gov.cn/tianjin/2024/0621/2529.html" },
    source2: { title: "SAFE Tianjin — Q&A 2025 (PR card holders)", url: "https://www.safe.gov.cn/tianjin/2025/1113/2926.html" }
  },
  {
    area: "Foreign nationals (境外个人)",
    rule: "Salary and China property-sale proceeds are convertible for foreign nationals",
    detail: "SAFE knowledge Q&A: “境外个人在境内取得的经常项目项下的合法人民币收入，如工资或境内房产转让收入，以及原兑换未用完的人民币资金，可以凭本人有效身份证件及相关证明材料在银行办理购汇及汇出.”",
    value: "—",
    status: "verified",
    source: { title: "SAFE Hebei branch — 外汇知识问答 (2019)", url: "https://www.safe.gov.cn/hebei/2019/0118/1253.html" }
  },
  {
    area: "Wiring money out",
    rule: "FX savings account → overseas: ≤ US$50k/day with just ID; more with transaction documents",
    detail: "实施细则 art. 14: “外汇储蓄账户内外汇汇出境外当日累计等值5万美元以下（含）的，凭本人有效身份证件在银行办理；超过上述金额的，凭经常项目项下有交易额的真实性凭证办理.” Cash in hand wired out: ≤ US$10k/day with ID (art. 15 for 境外个人).",
    value: "≤ US$50,000/day (ID only); higher with documents",
    status: "verified",
    source: { title: "SAFE Tianjin — 个人外汇管理办法实施细则 full text (arts 14–15)", url: "https://www.safe.gov.cn/tianjin/2024/0430/2464.html" }
  },
  {
    area: "Wiring money out",
    rule: "Outbound payments > US$50k in a single payment need a tax-authority filing (备案表) first — domestic institutions/individuals; foreign individuals follow personal-FX rules",
    detail: "国家税务总局/外汇局公告2013年第40号 (as amended by 2021年第19号): single outbound payment of equivalent more than US$50,000 for services/income/current transfers (incl. 境外个人在境内的工作报酬) requires a 税务备案表 filed with the competent tax authority before bank payment. Exemptions include private FX use like study/tourism/family visits abroad; art. 4: 境外个人 follow the personal FX administration rules.",
    value: "Filing threshold: > US$50,000 per payment",
    status: "verified",
    source: { title: "State Taxation Administration — announcement 2013 No. 40 (as amended)", url: "https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194375/content.html" }
  },
  {
    area: "Cash carriage across the border",
    rule: "Foreign-currency cash OUT of China: ≤ US$5,000 free to carry; US$5,000–10,000 needs a bank Carrying Certificate; > US$10,000 in principle not allowed (special cases need a SAFE-issued certificate)",
    detail: "《携带外币现钞出入境管理暂行办法》(汇发〔2003〕102号): ≤US$5,000 no 《携带证》/customs clears; >US$5,000–≤US$10,000 bank-issued certificate; >US$10,000 “原则上不得携带” except special cases with a SAFE-branch certificate; multiple certificates totalling > US$10k are not cleared. Entry INTO China: declare above US$5,000 in writing.",
    value: "US$5,000 / US$10,000 tiers",
    status: "verified",
    source: { title: "gov.cn State Council Gazette — full text of the Interim Measure", url: "https://www.gov.cn/gongbao/content/2004/content_63085.htm" }
  },
  {
    area: "Cash carriage across the border",
    rule: "RMB cash across the border: max RMB 20,000 per person per trip",
    detail: "中国人民银行公告〔2004〕第18号: 中国公民出入境、外国人入出境每人每次携带的人民币限额为20000元. Reported on an official State Council Overseas Chinese Affairs Office (gqb.gov.cn) page.",
    value: "RMB 20,000 per trip",
    status: "verified",
    source: { title: "State Council OCA (gqb.gov.cn) — travel cash rules (2024)", url: "https://www.gqb.gov.cn/news/2024/0320/58569.shtml" }
  },
  {
    area: "Bank cards abroad",
    rule: "Mainland bank cards used at overseas ATMs: RMB 100,000 per PERSON per calendar year (all cards combined); RMB 10,000 per card per day",
    detail: "汇发〔2017〕29号: “个人持境内银行卡在境外提取现金，本人名下银行卡（含附属卡）合计每个自然年度不得超过等值10万元人民币…每卡每日…等值1万元人民币.” Over-limit → overseas ATM cash withdrawals suspended for the current AND next calendar year. Borrowing/lending cards to evade is prohibited. In effect since 2018-01-01. Card SPENDING abroad for consumption is unaffected (SAFE press Q&A attached to the notice).",
    value: "RMB 100,000/yr per person; RMB 10,000/day per card",
    status: "verified",
    source: { title: "gov.cn — SAFE notice 汇发〔2017〕29号 full text", url: "https://www.gov.cn/xinwen/2017-12/31/content_5251954.htm" }
  },
  {
    area: "Prohibited conduct",
    rule: "Splitting conversions/remittances across other people’s quotas (“蚂蚁搬家”) is prohibited",
    detail: "《个人外汇管理办法》(PBOC Order 2006 No. 3) art. 7: “不得以分拆等方式逃避限额监管，也不得使用虚假商业单据或者凭证逃避真实性管理.” SAFE Shanghai 2019 guidance likewise warns: 不得出借本人或借用他人额度 — do not lend your quota or borrow others’.",
    value: "—",
    status: "verified",
    source: { title: "gov.cn State Council Gazette — 个人外汇管理办法 (art. 7)", url: "https://www.gov.cn/gongbao/content/2007/content_786257.htm" },
    source2: { title: "SAFE Shanghai branch — personal FX guidance (2019)", url: "http://www.safe.gov.cn/shanghai/2019/1213/1198.html" }
  },
  {
    area: "Prohibited conduct",
    rule: "Splitting-detection notice 汇发〔2009〕56号 and “watch list” notice 汇发〔2015〕43号 are marked REPEALED (已废止) on SAFE’s official pages",
    detail: "The famous “5-or-more people / 5-plus-transactions” splitting fingerprints circulated online come from 汇发〔2009〕56号; the 2-year “关注名单” regime came from SAFE’s Dec-2015 notice. SAFE’s own copies of both are labelled 已废止 (repealed). The overarching prohibition in PBOC Order 2006 No. 3 art. 7 remains in force; treat the old fingerprint lists as historical context, not current law.",
    value: "—",
    status: "historical",
    source: { title: "SAFE — 汇发〔2009〕56号 (marked 已废止)", url: "https://www.safe.gov.cn/big5/big5/www.safe.gov.cn/safe/2009/1125/5439.html" },
    source2: { title: "SAFE Guangdong — 汇发〔2015〕43号 (marked 已废止)", url: "http://m.safe.gov.cn/big5/big5/www.safe.gov.cn/guangdong/2016/0104/216.html" }
  },
  {
    area: "Prohibited conduct",
    rule: "Private/underground FX dealing: fine up to 30% of the amount (serious cases 30%–100%) plus confiscation of illegal gains; criminal referral possible",
    detail: "《外汇管理条例》(2008 revision, State Council Order 532) art. 45: “私自买卖外汇、变相买卖外汇、倒买倒卖外汇或者非法介绍买卖外汇数额较大的，由外汇管理机关给予警告，没收违法所得，处违法金额30%以下的罚款；情节严重的，处违法金额30%以上等值以下的罚款；构成犯罪的，依法追究刑事责任.” Art. 39 (逃汇, moving FX abroad in violation) uses the same 30% / 30–100% fine ladder. PBOC Order 2006 No. 3 art. 30: FX transactions must run through licensed institutions.",
    value: "Fines: up to 30% of amount; serious: 30%–100%",
    status: "verified",
    source: { title: "SAFE-hosted official PDF — 外汇管理条例 full text (arts 39, 45)", url: "https://www.safe.gov.cn/heilongjiang/file/file/20170728/c8dd4cfd7f9b432faa691b7d23395809.pdf" }
  },
  {
    area: "Prohibited conduct",
    rule: "Cryptocurrency exchange for moving money out is an illegal financial activity in China",
    detail: "银发〔2021〕237号 (PBOC + 9 other agencies, incl. SAFE): “虚拟货币相关业务活动属于非法金融活动…一律严格禁止，坚决依法取缔” — covers fiat↔crypto exchange, acting as central counterparty, and offshore exchanges serving mainland residents. Crypto-related civil dealings are void; losses are borne by the participant.",
    value: "—",
    status: "verified",
    source: { title: "gov.cn — 银发〔2021〕237号 full text", url: "https://www.gov.cn/zhengce/zhengceku/2021-10/08/content_5641404.htm" }
  },
  {
    area: "Large one-time exits",
    rule: "Emigration & inheritance asset-transfer program: SAFE-approved conversion and remittance of liquidated personal assets",
    detail: "《个人财产对外转移售付汇管理暂行办法》(PBOC Announcement 2004 No. 16): people who emigrated from the mainland (or foreign/HK/MO residents inheriting mainland estates) may apply to SAFE to convert and remit legal assets. ≤ RMB 500k approved by a local SAFE branch; larger amounts go to SAFE HQ. Emigration transfers: apply once for the total, remit in stages over ~2 years (≤20万 one-shot). Requires documentation incl. tax clearance; wired directly to the applicant’s own account abroad (no cash withdrawal in China). Effective 2004-12-01.",
    value: "Approval: SAFE branch ≤ RMB 500k; HQ above",
    status: "verified",
    source: { title: "SAFE portal — PBOC Announcement 2004 No. 16 full text", url: "http://m.safe.gov.cn/safe/2004/1116/5461.html" }
  },
  {
    area: "Income tax precondition (what banks check)",
    rule: "China IIT: comprehensive income (wages etc.) at 7 progressive brackets 3%–45%; property-transfer gains at a flat 20%",
    detail: "《个人所得税法》(2018 7th amendment) art. 3: 综合所得适用3%–45%超额累进税率; 财产转让/利息股息红利/偶然所得适用20%比例税率. Banks validating a source-of-funds chain expect the income to be taxed (完税证明/代扣记录). Full bracket table is on the Costs & Penalties page.",
    value: "3%–45% (wages) / 20% (property transfer)",
    status: "verified",
    source: { title: "State Taxation Administration — Individual Income Tax Law full text", url: "https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html" }
  }
];
