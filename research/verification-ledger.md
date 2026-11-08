# Verification ledger — session `agent-2`

Every source below was fetched and read directly on **2026-11-08**. This ledger records
what was actually read, what it established, and what it did **not** establish. The
machine-readable version is `data/sources.json`; the site renders from that.

Policy: a value is published only if it was read in an official source. Otherwise the
field is `null`, renders as a dash, and carries a flag on `flagged.html`. Nothing is
inferred, interpolated, or taken from a secondary site.

---

## Chinese primary instruments

### S01 — 个人外汇管理办法实施细则 (Huifa [2007] No. 1)
`https://www.safe.gov.cn/safe/2007/0105/5320.html`

Read in full, both chunks. Page is marked **（已修改）** (as amended).

Established verbatim:
- **Art. 2** — `对个人结汇和境内个人购汇实行年度总额管理。年度总额分别为每人每年等值5万美元。`
  The annual total binds *settlement* for all individuals and *purchase* for **domestic
  individuals only**. This is the correction to the site's central error.
- **Art. 3** — purchased FX may be remitted abroad, deposited to one's own FX savings
  account, or carried out under the relevant rules.
- **Art. 6** — banks must perform authenticity review and must not fabricate transactions.
- **Art. 9(1)** — personal foreign-trade operators use their own FX settlement account,
  managed as an institution.
- **Art. 10** — documentary basis for above-quota settlement by domestic individuals
  (donations, family support, inheritance, insurance, royalties, services, employment,
  overseas investment returns).
- **Art. 12** — above-quota *purchase* by a domestic individual: ID plus documents
  evidencing the transaction amount.
- **Art. 13(1)** — non-domestic individual converts lawful current-account RMB income on
  ID plus supporting documents **including tax vouchers** (`含税务凭证`). **No annual
  numeric cap is stated.**
- **Art. 13(2)** — reconversion of unused RMB via the original exchange memo, valid
  **24 months**; ID-only tiers of **USD 500/day**, or **USD 1,000/day** at pre-departure
  offsite locations.
- **Art. 14** — domestic individual outward remittance from an FX savings account:
  **USD 50,000 per day** on ID alone; above that, authenticity vouchers. Hand-held
  banknotes: **USD 10,000 per day**.
- **Art. 15(1)** — non-domestic individual remits FX from a savings account on **ID alone**;
  no numeric ceiling stated. Art. 15(2) banknotes: USD 10,000/day.
- **Arts. 16, 17, 18, 20** — ODI, QDII, employee share plans, and the cross-reference to the
  property-transfer Interim Measures.
- **Art. 28(3)** — transfers between a domestic and a non-domestic individual are managed
  **as cross-border transactions**.
- **Art. 30** — FX banknote withdrawal **USD 10,000/day** direct; above that, pre-filing with SAFE.
- **Art. 31** — FX banknote deposit **USD 5,000/day** direct; above that, Customs declaration
  or original withdrawal slip.
- **Art. 35(5)** — domestic cards used overseas with FX repayment are outside the individual
  FX settlement system.

Repeal confirmed from the note printed on the page itself:
> 根据…（汇发〔2023〕8号）附件3…以下内容已被废止：《个人外汇管理办法实施细则》…第三十九条。

**Art. 39 is repealed.** The old RMB 1,000 individual fine is not current law. Also noted:
Art. 9(2) was amended by Huifa [2016] No. 13.

### S02 — 中华人民共和国外汇管理条例 (State Council Order No. 532)
`https://www.safe.gov.cn/safe/2008/0806/5321.html`

Read in full. Chapter 7 quoted verbatim into `data/penalties.json`.

- **Art. 52(2)** — `境内个人，是指中国公民和在中华人民共和国境内连续居住满1年的外国人…`
  A foreigner continuously resident **one full year** is a domestic individual.
- **Art. 5** — `国家对经常性国际支付和转移不予限制。` Current-account payments are not restricted.
- **Arts. 39, 40, 41, 44, 45** — all use the same formula:
  `处…30%以下的罚款；情节严重的，处…30%以上等值以下的罚款`
  → up to 30%; serious cases 30% up to **100%**. `等值` = the equivalent amount.
  **This disproves the site's "30%–300%" and "30%–500%" claims.**
- **Art. 42** — carrying violations: warning plus a possible fine up to **20%**; Customs
  provisions prevail where they apply.
- **Art. 46** — unlicensed FX business: gains ≥ RMB 500,000 → **1–5× the gains**; otherwise
  **RMB 500,000–2,000,000**. This is the operator provision, not a customer fine.
- **Art. 48** — reporting/document/account/registration failures: institutions up to
  RMB 300,000, **individuals up to RMB 50,000**.

### S03 — Huifa [2015] No. 49 (quota splitting)
`https://www.safe.gov.cn/safe/2015/1231/5442.html`

Item 2: splitting prohibited. Lending your quota → risk-warning letter, repeat → watch list.
Borrowing another's → immediate watch list. Watch period = **year of listing + 2 consecutive
years**, counter-only with documentary proof.

**Conflict flagged (I-04):** a secondary site labels this circular wholly repealed; the
official SAFE page carries no repeal marker. Official position treated as controlling; the
substantive warning is independently supported by Order 532 Arts. 39–40.

### S04 — Huifa [2003] No. 102 (carrying foreign-currency banknotes)
`https://www.safe.gov.cn/tianjin/2024/0430/2466.html`

SAFE Tianjin's reproduction of the national circular, read in full. Covering notice item 2:
≤ USD 5,000 no permit; > 5,000 to 10,000 bank-issued Carrying Permit; **in principle no more
than USD 10,000**, SAFE permit only for five listed special cases. Item 3: Customs no longer
administers the carriage of foreign-currency **payment instruments and securities** — the
basis for the bank-draft route.

Note: the previously used MOFCOM reprint
(`cws.mofcom.gov.cn/article/xxfb/202005/20200502962089.shtml`) now returns HTTP 500 and is
**not** cited. This SAFE page is the live official source.

### S05 — Customs reply confirming the RMB 20,000 cash limit
`http://www.customs.gov.cn/eportal/ui?pageId=374112&msgDataId=7cebfa81134447ad8a57883790a3e68d`

Jiangmen Customs reply, 2021-03-12: `每人每次携带现金的限额是人民币20000元，外币5000美元，
但当天多次往返及短期内多次往返者除外。`

**Caveat (F09):** this is an official Customs reply, not the primary PBOC Announcement
[2004] No. 18. The figure is published because the source is official; the caveat records
that the primary instrument was not reached. The previously cited Guangzhou Customs page
is now 404.

### S06 — Yinfa [2021] No. 237 (virtual currency)
`https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212551974141/index.html`

Full 16-item text read. Item 1(2): fiat-to-virtual-currency exchange is an **illegal financial
activity**, strictly prohibited. Item 1(3): overseas exchanges serving mainland residents
online likewise. Item 1(4): related civil acts contrary to public order are **void**, losses
borne by the participant. Item 4(9): banks and payment institutions barred from providing
accounts, transfers, settlement, collateral or insurance.

The old URL `/113469/4348521/index.html` is 404 — replaced (I-02).

### S07 — Yinfa [2020] No. 330 (cross-border RMB)
`https://www.pbc.gov.cn/huobizhengceersi/214481/214511/3406535/7c4cab88dc26405d9aba84feee8059e0/index.html`

Item 13 supports banks handling **individual current-account cross-border RMB settlement**,
expressly including salary and other lawful income. Effective 2021-02-04.

**Did not establish (F01):** no numeric limit and no document list for individuals. Bank-specific
limits left blank. Item 15 concerns inbound RMB to NRA accounts and is *not* an outbound
individual route — an earlier reading of this was corrected.

### S08 — PBOC Announcement [2004] No. 16 (outbound property transfer)
`http://m.safe.gov.cn/safe/2004/1116/4133.html`

Two channels only: **emigration transfer** and **inheritance transfer**. Art. 6 staged
remittance (half, then half the remainder after 1 year, then all after 2 years); lump sum
if ≤ **RMB 200,000**. Art. 10 approval split at **RMB 500,000** (local branch vs head office).
Art. 11 funds must go to the applicant's **own overseas account**; no domestic FX banknote
withdrawal. Art. 12 refusal where property is judicially restricted, in pending proceedings,
or lawful source cannot be shown. Art. 9 document list including the **tax certificate**.
Effective 2004-12-01.

### S09 / S10 — Huifa [2024] No. 12 s.6.4, confirmed still applied in 2026
`https://www.gov.cn/zhengce/zhengceku/202404/content_6945036.htm`
`https://www.safe.gov.cn/tianjin/2026/0319/3018.html`

The 2024 capital-account guidelines govern outbound property transfer approval. SAFE Tianjin's
Q&A published **2026-03-19** confirms s.6.4 is operative: emigration filed at the emigrant's
former hukou locality, inheritance at the decedent's. This is the currency check that the
2004 measures have not been superseded in practice.

### S11 — Individual Income Tax Law
`https://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3970366/content.html`

Arts. 1–22 read. Residence = domicile or **≥ 183 days**. Art. 3 rates: comprehensive **3–45%**,
business **5–35%**, interest/dividends/property lease/**property transfer**/incidental **20%**.
Property-transfer income = proceeds − original value − reasonable expenses. **Arts. 10(5) and
13: tax clearance before cancelling household registration on emigration** — which is why the
tax step gates the emigration-transfer channel.

### S23 — SAFE in-force catalogue as at 2026-06-30
`https://www.safe.gov.cn/safe/file/file/20260805/d2d0d6ce1441436eadc8bc600eb79c43.pdf`

Confirms Order 532, PBOC Order 2006 No. 3, Huifa [2007] No. 1 and Huifa [2003] No. 102 all
remain in force. Used as the currency check on the whole Chinese rule set.

---

## Bank tariff (institution's own published prices)

### S12 / S13 — Bank of China service price list, ch.3 personal finance
`https://pic.bankofchina.com/bocappd/pricelist/202511/P020251110646838136627.pdf`
`https://www.boc.cn/custserv/fd5/`

All 6 pages read. Effective **2025-11-11**.

- **210105008** cross-border wire/draft: **0.1% (1‰), min RMB 50, max RMB 260** per transaction;
  cable **RMB 80** HK/Macao/Taiwan, **RMB 150** international; amendment ≤ RMB 50; refund RMB 20.
- **Note 5** full-value arrival (OUR), only where an intermediary is needed, on top of the above:
  **USD 15** if the beneficiary bank accounts at BOC New York, else **USD 25**; EUR 25 (≤ €1m);
  AUD ≤ 15; other ≤ €50 equivalent.
- **Note 4** overseas bank charges **passed through at actual cost** — unquantifiable in advance.
- **210107011** **no FX conversion fee at BOC's own branches**; self-service machines ≤ RMB 60;
  agent outlets ≤ 0.1%.
- **210101002** deposit certificate RMB 20–40; credit certificate ≤ RMB 100; FX carrying permit
  RMB 10 but **waived 2025-04-01 → 2026-12-31**.
- **210108014** cross-border ATM **RMB 12 + 1%, max RMB 112**; Great Wall International Debit
  Card overseas 0.5%, min USD 3, max USD 5.
- **210106010** clean collection 0.1%, RMB 50–250, plus postage; RMB 10 return fee.
- **Note 11** temporary waivers lapse when the next tariff takes effect.

**Did not establish (F06):** the **FX bid-ask spread**. No official spread figure exists in
this tariff. The commonly quoted 0.24%–0.3% appears only on secondary sites and is **not used**.
This is the largest cost on a large conversion and it is deliberately blank.

### S25 — BOC tariff change effective 2026-11-11
`https://www.boc.cn/pbservice/bi2/202608/t20260811_25684907.html`

Published 2026-08-11, read in full. Changes **only item 210108014**. From **2026-11-11**:
- UnionPay overseas: unchanged at RMB 12 + 1%, max RMB 112.
- **Mastercard / VISA overseas: 2.5% of the withdrawal, min USD 3, max USD 40 equivalent** —
  replacing 0.5% / min USD 3 / max USD 5.

Three days after this review. Both figures are published side by side (I-03, F10). Practical
consequence: use UnionPay, not Mastercard or VISA, for overseas cash after that date.

---

## US primary sources

### S14 — 31 CFR 1010.821 (FinCEN civil penalties)
`https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-H/section-1010.821`

Table 1, column headed **"penalties assessed on or after January 17, 2025"**:
non-willful **$16,536** (statutory $10,000); willful **$165,353** (statutory $100,000).
eCFR shows Title 31 current to 2026-11-05 with no later amendment to this section.

Corroborated by `https://www.federalregister.gov/documents/2026-07-07/2026-13629/no-adjustment-to-civil-monetary-penalty-amounts`
— the 2026 adjustment was **cancelled** (OMB M-26-11; no October 2025 CPI-U), so the 2025
figures still govern. **The site's figures were right; its "2026 adjustment" label was wrong** (I-07).

### S15 — FinCEN FBAR
`https://www.fincen.gov/report-foreign-bank-and-financial-accounts`

FBAR required if the **aggregate** value of foreign accounts **exceeds $10,000 at any time**
in the calendar year. Individuals may e-file without registering.

### S16 — IRS FATCA summary
`https://www.irs.gov/businesses/corporations/summary-of-fatca-reporting-for-us-taxpayers`

Full Form 8938 threshold matrix: US single/MFS **$50,000** year-end / **$75,000** any time;
US MFJ **$100,000/$150,000**; abroad single **$200,000/$300,000**; abroad MFJ **$400,000/$600,000**.
Penalties: **$10,000**, up to **$50,000** additional after IRS notice, **40%** on related
understatement. **Six-year** limitations period if > $5,000 of income omitted. FBAR due
**15 April**. Treasury Fiscal Service year-end rate for conversion. **Form 8938 does not
relieve the FBAR obligation.**

### S17 — Instructions for Form 3520 (Rev. 12-2025)
`https://www.irs.gov/pub/irs-pdf/i3520.pdf` — penalties are in **chunk 2**

- Who Must File **4(a)**: more than **$100,000** from a nonresident alien individual or
  foreign estate, aggregating related persons. **Not indexed.**
- **4(b)**: foreign corporations/partnerships use the **s.6039F** threshold.
- **s.6677**: greater of **$10,000** or **35%** of gross value (transfers/distributions);
  **5%** for grantor-trust assets; further penalties after 90 days' notice, capped at the
  gross reportable amount.
- **s.6039F**: **5% of the gift per month, capped at 25%**.
- **s.6662(j)**: raises the 20% understatement penalty to **40%**.
- Foreign secrecy law is **not** reasonable cause.

**This resolves I-08:** the site conflated the $100,000 individual/estate threshold with the
$20,573 corporation/partnership threshold.

### S18 — Rev. Proc. 2025-32
`https://www.irs.gov/pub/irs-drop/rp-25-32.pdf` — **chunk 5** contains both sections

- **s.4.39** — FEIE for tax years beginning in **2026 = $132,900**.
- **s.4.47** — **s.6039F** foreign-gift threshold for 2026 = **$20,573**.

The site's $130,000 was the 2025 figure; its $20,573 was correct but mislabelled (A-08).

### S19 — 26 U.S.C. 988
`https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleA-chap1-subchapN-partIII-subpartJ-sec988.htm`

Read across chunks 0–2. **s.988(e) is in chunk 2**, now quoted verbatim:

> **(e)(2)** "no gain shall be recognized … by reason of changes in exchange rates after such
> currency was acquired … The preceding sentence shall not apply if the gain which would
> otherwise be recognized on the transaction **exceeds $200**."

> **(e)(3)** "personal transaction" excludes any transaction to the extent allocable expenses
> meet **s.162** or **s.212** — so an investment deposit is not automatically personal.

Also: **(a)(1)(A)** gain/loss is **ordinary**; **(c)(1)(C)(i)** any disposition of nonfunctional
currency is a 988 transaction, **(ii)** expressly covering foreign-currency bank deposits;
**(a)(3)** source follows residence, i.e. the **s.911(d)(3) tax home**.

**This disproves the site's blanket "no US tax on conversion"** (A-10, I-12). The $200
exclusion is **gain-only** and a **cliff**, not an allowance.

### S20 — IRS China treaty documents
`https://www.irs.gov/businesses/international-businesses/china-tax-treaty-documents`

Index confirms only the **1984** treaty and **1984** technical explanation; no later protocol
listed. **Did not establish (F07):** article-level rates — the PDFs were not read, so no
dividend/interest/royalty rate is quoted anywhere on the site.

### S21 — CBP money and monetary instruments
`https://www.cbp.gov/travel/international-visitors/money-monetary-instruments`

Modified 2025-11-24. Report amounts **exceeding $10,000** entering **or leaving** the US.
**The threshold is collective for families/groups**, not per person. Instrument definitions
given; a check to a named payee that is unendorsed or restrictively endorsed is **not** a
monetary instrument. Penalties cite 31 USC 5317/5321/5322/5332.

Replaces the 404 `/know-before-you-visit/money` URL (I-02). Wording note (I-06): some CBP
newsroom text says "$10,000 or greater"; the controlling page says **exceeding**, which the
site uses throughout.

### S22 / S24 — official but stale, cited with caveats
`https://www.irs.gov/individuals/international-taxpayers/foreign-earned-income-exclusion`
`https://www.irs.gov/irm/part5/irm_05-021-006`

The FEIE landing page prints amounts only through **2023**; IRM 5.21.6's exhibit still shows
a **30 June** FBAR deadline with no extensions and un-indexed $10,000/$100,000 penalties.
Both are official but out of date. Cited only for rules they still state correctly; current
figures come from S18, S16, S15 and S14. Logged as **I-05**.

---

## Dead ends — do not retry

| URL | Result | Replacement |
|-----|--------|-------------|
| `cbp.gov/travel/international-visitors/know-before-you-visit/money` | 404 | S21 |
| `pbc.gov.cn/goutongjiaoliu/113456/113469/4348521/index.html` | 404 | S06 |
| `guangzhou.customs.gov.cn/.../3800229/index.html` | 404 | S05 |
| `cws.mofcom.gov.cn/article/xxfb/202005/20200502962089.shtml` | HTTP 500 | S04 |
| `dcj.mofcom.gov.cn/.../20030900122517.html` | fetch failed | S04 |
| `safe.gov.cn/safe/2007/0105/5321.html` | 404 | S02 is `/2008/0806/5321.html` |
| `irs.gov/individuals/international-taxpayers/comparison-of-form-8938-and-fbar-requirements` | 404 | S16 |

Also: `curl` from the build sandbox reaches only allowlisted hosts, so bulk external link
checking is impossible. `tools/verify.py` therefore checks provenance and internal structure
only; external liveness was established by individual fetches recorded above.

## Remaining gaps

11 values are blank and flagged. The two that matter most:

- **F06 — the FX spread.** The dominant cost on a large transfer, and no official figure
  exists. The site explains how to measure it rather than quoting a secondary number.
- **F02 — the annual overseas ATM withdrawal cap.** The RMB 100,000 figure is ubiquitous in
  secondary sources but the underlying SAFE circular was not read officially, so it is blank.
