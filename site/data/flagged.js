/* Flagged for Review — every item that could NOT be verified line-by-line on an official source
   in this project, plus repo-review irregularities. Nothing here blocks the verified tables;
   these items are published so the owner can confirm them after the site is live.
   "tried" = what the research actually checked on 2026-11-07. */
window.DATA_FLAGGED = [
  {
    id: "FR-1",
    source: "https://www.boc.cn/cbservice/cb3/cb33/200807/t20080701_852.html",
    area: "Fees",
    item: "Bank of China personal outward-remittance tariff: “0.1% of amount, min RMB 50 / max RMB 260, cable fee RMB 80 (HK/MO/TW) or RMB 150 (others)”",
    detail: "Shown by multiple secondary guides quoting BOC’s personal tariff; the official personal price-schedule page/PDF could not be retrieved and read in this project, so the numbers are NOT used as fact anywhere on this site.",
    tried: "Searched official banking sources; BOC corporate tariff page was retrieved (and is cited for the pass-through mechanic), but the personal tariff page was not reachable in-session.",
    secondary: "zhidao.baidu.com (BOC fee Q&A); wise.com/zh-cn blog on BOC transfers; exiap.cn BOC guide",
    action: "Confirm at a BOC branch or boc.cn “个人客户服务收费标准” before relying on any figure.",
    status: "unverified"
  },
  {
    id: "FR-2",
    source: "https://www.boc.cn/sourcedb/whpj/",
    area: "Fees",
    item: "Typical bank FX spread CNY→USD (one guide measured ~0.3% off mid-market on 27 Apr 2024)",
    detail: "Anecdotal single-day observation from a third-party guide; banks post daily buy/sell rates (现汇卖出价) and the spread moves with the market. No official figure is published as a fixed rate schedule for the spread itself.",
    tried: "Secondary guide example noted; no official spread schedule found.",
    secondary: "wise.com/zh-cn blog (BOC remittance article)",
    action: "Compare the bank’s posted sell rate (卖出价) against SAFE’s central parity on the day of conversion.",
    status: "unverified"
  },
  {
    id: "FR-3",
    source: "https://wise.com/en-cn/blog/wise-work-in-china-send-money-to-and-from-china",
    area: "Channels",
    item: "Wise current CNY→USD pricing and the up-to-date per-transfer cap",
    detail: "Wise’s own blog (retrieved) states: send-out enabled Jul 2023; CNY 100,000 per transaction; overall limit tied to documented income and tax paid; own-account only. The live fee for a given transfer is quoted dynamically in-app and was not captured.",
    tried: "Provider blog read; live pricing calculator not captured from an official page.",
    secondary: "— (provider blog is the source used for the verified product facts)",
    action: "Check Wise’s in-app quote and help centre on the transfer day.",
    status: "unverified"
  },
  {
    id: "FR-4",
    source: "https://wise.com/en-cn/blog/alipay-international-transfer-sending-and-receiving",
    area: "Channels",
    item: "Alipay / WeChat Pay international remittance availability for foreign nationals today",
    detail: "Wise’s guide (retrieved) states foreigners could not use Alipay to send money out of China at that time (Dec 2023). Partner-bank products change; no official Alipay/WeChat product page was retrieved to confirm current status, limits or required documents.",
    tried: "Provider statement captured from Wise blog; Alipay/WeChat official product pages not retrieved.",
    secondary: "wise.com/en-cn blog (Alipay transfers)",
    action: "Ask Alipay/WeChat support or test in-app with your verified identity.",
    status: "unverified"
  },
  {
    id: "FR-5",
    source: "https://www.safe.gov.cn/heilongjiang/file/file/20170728/c8dd4cfd7f9b432faa691b7d23395809.pdf",
    area: "Penalties (China)",
    item: "Criminal thresholds for underground/private FX dealing: SPC/SPP 2019 interpretation — 非法经营罪 “情节严重” at RMB 5,000,000 transaction scale or RMB 100,000 illicit gains (“情节特别严重” RMB 25,000,000 / RMB 500,000)",
    detail: "Quoted by multiple law-firm and news analyses, and consistent with SAFE republications about underground banking — but the primary SPC/SPP text on an official court/procuratorate site was not retrieved in this project.",
    tried: "Secondary legal analyses read (zhonglun.com; sina republication of a SAFE-branch piece).",
    secondary: "zhonglun.com/research/articles/6642.html; gd.sina.cn/shunde (SAFE-branch republication)",
    action: "Retrieve 《关于办理非法从事资金支付结算业务、非法买卖外汇刑事案件适用法律若干问题的解释》 from court.gov.cn / spp.gov.cn for line-by-line confirmation.",
    status: "unverified"
  },
  {
    id: "FR-6",
    source: "https://www.irs.gov/businesses/gifts-from-foreign-person",
    area: "Penalties (US)",
    item: "Form 3520 numeric penalty schedule — commonly cited as 5% of the gift per month late, capped at 25% (IRC §6039F(c))",
    detail: "The IRS “Gifts from foreign person” page (retrieved) confirms penalties under §6039F(c) exist where there is no reasonable cause, but the statutory text page (govinfo) for §6039F was not reachable in-session to confirm the 5%/25% figures line-by-line.",
    tried: "IRS instructional page retrieved (mechanism confirmed); 26 U.S.C. §6039F page not retrieved.",
    secondary: "Multiple CPA/tax resources consistently describe 5%/month, 25% cap",
    action: "Read §6039F(c) at uscode.house.gov or govinfo.gov before negotiating any penalty exposure.",
    status: "unverified"
  },
  {
    id: "FR-7",
    source: "https://www.govinfo.gov/content/pkg/USCODE-2023-title31/html/USCODE-2023-title31-subtitleIV-chap53-subchapII-sec5321.htm",
    area: "Penalties (US)",
    item: "Current inflation-adjusted FBAR penalty amounts for 2026 (third-party tables cite e.g. ~$16,536 non-willful / ~$165,353 willful floor)",
    detail: "Statutory baselines ($10,000; greater of $100,000 or 50%) are verified on the official 31 U.S.C. §5321 text. The annual inflation-adjusted numbers come from 31 CFR adjustments — retrieved only via third-party summaries, not the current Federal Register rule page.",
    tried: "Official statute text verified; current adjusted amounts found only in third-party guides.",
    secondary: "taxesforexpats.com; myexpattaxes.com; brighttax.com (all agree on the 2026 figures)",
    action: "Check the latest 31 CFR 1010.821 civil-penalty inflation adjustment (Federal Register).",
    status: "unverified"
  },
  {
    id: "FR-8",
    source: "https://www.irs.gov/instructions/i8938",
    area: "US reporting",
    item: "Form 8938 higher thresholds for taxpayers living abroad ($200,000/$300,000 single; $400,000/$600,000 joint)",
    detail: "The IRS Form 8938 page retrieved in-session clearly listed the US-resident thresholds (single/MFS $50k/$75k, MFJ $100k/$150k) and notes higher thresholds for taxpayers residing abroad; the specific abroad figures were taken from third-party guides and are consistent, but the IRS page section with the abroad numbers was not captured in-session.",
    tried: "IRS page partially captured; abroad threshold values from third parties.",
    secondary: "Multiple tax-prep resources; IRS Form 8938 instructions PDF",
    action: "Confirm your residency-specific threshold in the current Form 8938 instructions on irs.gov.",
    status: "unverified"
  },
  {
    id: "FR-9",
    source: "https://www.safe.gov.cn/shanghai/2019/1213/1198.html",
    area: "Penalties (China)",
    item: "SAFE enforcement-bulletin case figures (e.g. reported fines for splitting and underground-bank use, incl. an ≈RMB 830k fine on a US$2.45m split case and multi-million-yuan personal fines)",
    detail: "Reported amounts come from media republications of SAFE case bulletins; the SAFE bulletin pages with matching numbers were not retrieved line-by-line, so case amounts are NOT used as data on this site.",
    tried: "Secondary round-up articles read (m.mpaypass.com.cn 2019-06-06).",
    secondary: "移动支付网 summary of SAFE 通报",
    action: "Match each case to the original SAFE 通报典型违规案例 bulletin on safe.gov.cn.",
    status: "unverified"
  },
  {
    id: "FR-10",
    source: "https://www.gov.cn/zhengce/zhengceku/2020-08/31/content_5538828.htm",
    area: "Rules (China)",
    item: "“Quota resets every January 1st” (calendar-year mechanics of the US$50k convenience quota)",
    detail: "Official texts say “每人每年” (per person per year) and the ATM rule explicitly says 自然年度 (calendar year), but the precise Jan-1 reset statement for the US$50k quota was found only in secondary explainers. Immaterial in practice, but flagged for strictness.",
    tried: "2020 guideline and SAFE Q&As retrieved; explicit reset clause not located.",
    secondary: "Various Chinese-language explainers",
    action: "Not needed for planning; banks display remaining annual quota in-app.",
    status: "unverified"
  },
  {
    id: "FR-11",
    source: "https://www.safe.gov.cn/tianjin/2026/0713/3088.html",
    area: "Channels",
    item: "“Remit CNY to your own Hong Kong account, then convert freely — Hong Kong has no exchange controls”",
    detail: "Widely repeated; however (a) the mainland→HK remittance step still follows the same personal-FX rules as any outbound transfer, and (b) the HK “no exchange controls” statement was not retrieved from an HKMA/HK government page in this project. The method therefore appears nowhere in the main tables.",
    tried: "No official HKMA page retrieved.",
    secondary: "—",
    action: "If pursuing the HK route, confirm both the mainland-side remittance basis and HK-side conversion freedom on official pages.",
    status: "unverified"
  },
  {
    id: "FR-12",
    source: "https://github.com/sassnarep3-star/China4/blob/1fbdfdb5891c31ff4f588e040d1b9970e8d74505/README.md",
    area: "Repo review",
    item: "Repo contained no prior data to verify",
    detail: "Pre-existing inventory at session start: exactly one file — README.md containing only “# China4”. No prior claims, data tables or site existed; nothing to dispute. Irregularity: none beyond the absence of content.",
    tried: "Full file-tree inventory + git history (single initial commit 1fbdfdb).",
    secondary: "—",
    action: "None. Recorded for completeness of the line-by-line repo review.",
    status: "verified"
  }
];
