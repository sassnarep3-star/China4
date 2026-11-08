#!/usr/bin/env python3
"""Build reproducible cost rows/CSV from verified research inputs.

No FX rate, tax result, routing fee or all-in total is inferred. Unknown numeric
USD cells are emitted as empty strings (CSV) / null (JSON). Published operator
components are preserved as text with their currency and conditions.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AMOUNTS = list(range(10_000, 400_001, 10_000))
NUMERIC_COST_FIELDS = [
    "fx_spread_usd", "conversion_fee_usd", "transfer_fee_usd",
    "routing_receiving_usd", "tax_usd", "reporting_preparation_usd",
    "all_in_cost_usd", "net_usd",
]
CSV_FIELDS = [
    "amount_usd", "method_id", "method_name", "category", "route_status",
    "feasibility_note", *NUMERIC_COST_FIELDS, "published_components", "formula",
    "flags", "source_id", "source_url", "source_title",
]

BOC_TT = (
    "BOC current tariff effective 2025-11-11: cross-border TT commission 0.1% of remittance amount, "
    "minimum CNY 50, maximum CNY 260 per transaction; TT cable CNY 150 outside HK/Macao/TW or CNY 80 "
    "to those regions; overseas bank charges actual. Conditional USD full-arrival service: USD 15 if "
    "receiving bank has a BOC New York account, otherwise USD 25, only for eligible indirect routing. "
    "Fee currency conversion uses BOC's transaction-time buying rate if collected in FX."
)
BOC_DRAFT = (
    "BOC current tariff: demand-draft commission 0.1%, minimum CNY 50, maximum CNY 260; postage actual; "
    "overseas collection/receiving charges actual. Receiving-bank acceptance and hold time must be confirmed."
)
COMPONENTS: dict[str, tuple[str, str, str]] = {
    "boc_tt": (
        BOC_TT,
        "commission_CNY = min(max(0.001 * gross_remittance_CNY_equivalent, 50), 260); "
        "cable_CNY = 150 (international) or 80 (HK/Macao/TW); all_in_USD = FX_friction + fees_USD + routing_USD + tax_USD + preparation_USD",
        "boc_tariff",
    ),
    "boc_draft": (
        BOC_DRAFT,
        "commission_CNY = min(max(0.001 * gross_remittance_CNY_equivalent, 50), 260); postage/receiving actual; all_in_USD unknown",
        "boc_tariff",
    ),
    "wise_quote": (
        "Wise describes mid-market pricing and amount/method-dependent fees, but no static CNY-to-USD corridor quote was verified. "
        "Published funding caps: bank-app CNY 300,000/transfer; Alipay CNY 50,000/transfer; overall limit generally documented salary net of China tax.",
        "all_in_USD = live Wise fee + FX/routing difference + tax_USD + preparation_USD; obtain executable quote",
        "wise_cny",
    ),
    "sky_reference": (
        "SkyRemit official notice publishes CNY 79 per transaction and CNY 300,000 per transfer; current terms say final billed amount controls. "
        "Number of transactions depends on the executed CNY quote and approved limit.",
        "reference_service_fee_CNY = 79 * executed_transaction_count; all_in_USD unknown without live rate/fee and tax facts",
        "sky_limit",
    ),
    "wu_quote": (
        "Western Union China page verifies partner-bank outbound service and cash-pickup instructions; no fee, FX quote or US-passport/US-bank limit was verified.",
        "all_in_USD = operator fee + FX friction + delivery/receiving charges + tax_USD; obtain partner-bank quote",
        "wu_cn",
    ),
    "property_quote": (
        "No universal property-remittance fee verified. Bank tariff, property agent, notarization/translation, local transaction taxes and receiving charges depend on the actual sale and bank.",
        "net_sale_CNY = sale_price - allowed_taxes_fees; remittance_USD quote unknown; tax_USD depends on local calculation and US gain/currency analysis",
        "safe_property_amended",
    ),
    "migration_safe": (
        "Cited SAFE administrative service guide: no administrative permission fee. Bank purchase/remittance, FX, translation/notarization and receiving charges are separate and unverified.",
        "SAFE_permission_fee_CNY = 0; all_in_USD = bank_FX_fees_USD + professional_USD + tax_USD; unknown",
        "safe_migration",
    ),
    "inheritance_safe": (
        "Cited SAFE administrative service guide: no administrative permission fee. Bank, inheritance/title, translation/notarization and receiving charges are separate and unverified.",
        "SAFE_permission_fee_CNY = 0; all_in_USD = bank_FX_fees_USD + professional_USD + tax_USD; unknown",
        "safe_inheritance",
    ),
    "dividend_withholding": (
        "From 2026-09-01, foreign-individual FIE dividends: 20% PRC IIT withholding under announcement 2026 No. 27, subject to separately established treaty entitlement. "
        "Bank/FX fees unverified. The 20% applies to dividend income, not automatically to the USD transfer target.",
        "PRC_withholding_CNY = 0.20 * taxable_dividend_CNY (if no treaty reduction); all_in_USD unknown; US tax/FTC separate",
        "cn_dividends_2026",
    ),
    "trade_quote": (
        "Genuine trade settlement fees depend on the bank/settlement institution and transaction documents; no universal fee verified. Business taxes are separate.",
        "all_in_USD = settlement_fee + FX friction + business_tax_USD + professional_USD; unknown",
        "safe_faq",
    ),
    "rmb_quote": (
        "PBOC current-account RMB policy verified; domestic remittance fee, offshore RMB acceptance/conversion spread and receiving fees are unverified.",
        "all_in_USD = RMB_remittance_fee + offshore_conversion_friction + receiving_fee + tax_USD; compare against direct CNY-to-USD quote",
        "pboc_rmb",
    ),
    "atm_boc": (
        "SAFE cap: CNY 100,000 equivalent/person/calendar year across all domestic cards; CNY 10,000/card/day. "
        "BOC current international debit: 0.5% of withdrawal, min USD 3/max USD 5 per withdrawal; ordinary debit: CNY 12 + 1%, max CNY 112. "
        "Foreign ATM surcharge may apply. Announced change effective 2026-11-11: UnionPay CNY 12 + 1% max CNY 112; Visa/MC 2.5% min USD 3/max USD 40.",
        "fee_per_withdrawal = min(max(0.005 * withdrawal_USD, 3), 5) for current BOC international debit; total unknown because withdrawal count/rates/caps apply",
        "boc_tariff",
    ),
    "cash_permit": (
        "BOC carrying-permit fee CNY 10, waived 2025-04-01 through 2026-12-31. FX cash spread, travel and US deposit costs unverified. "
        "China permit bands and US FinCEN 105 declaration are separate from tax.",
        "permit_fee_CNY = 0 during stated BOC waiver; all_in_USD = FX_cash_friction + travel/deposit costs + tax_USD; unknown",
        "boc_tariff",
    ),
    "hk_witness": (
        "BOC overseas account-opening witness service: maximum CNY 400 per account, charged to the委托方. This is account opening only, not a transfer quote.",
        "witness_fee_CNY <= 400; transfer all_in_USD requires a separate lawful source route",
        "boc_tariff",
    ),
    "closed_loop": (
        "Closed-loop/institutional investment channel; product fees and redemption costs are not verified and it is not a free USD-to-US-account remittance route.",
        "not_applicable_as_personal_remittance_quote",
        "hkma_wmc",
    ),
    "unverified": (
        "No current official route eligibility/fee/limit verification. Numeric costs remain blank.",
        "unknown; do not infer from another corridor or stale schedule",
        "safe_rules",
    ),
    "not_applicable": (
        "Merchant acquiring or other non-personal-savings use case; no personal remittance cost calculated.",
        "not_applicable",
        "wechat_merchant",
    ),
    "prohibited": (
        "Excluded unlawful workaround. Statutory penalties are violation-specific sanctions, not transfer fees or expected costs.",
        "do_not_use; no lawful quote",
        "safe_fx_reg",
    ),
}


def load_json(rel: str) -> Any:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def validate_inputs(procedures: dict, registry: dict, findings: dict) -> None:
    sources = {s["id"]: s for s in registry["sources"]}
    flags = {f["id"] for f in findings["open_flags"]}
    ids = [m["id"] for m in procedures["methods"]]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate method id")
    grid = procedures["amount_grid_usd"]
    if list(range(grid["start"], grid["stop"] + 1, grid["step"])) != AMOUNTS:
        raise ValueError("amount grid must be 10000..400000 step 10000")
    for m in procedures["methods"]:
        if m["cost_rule"] not in COMPONENTS:
            raise ValueError(f"unknown cost rule {m['cost_rule']}")
        for sid in m["sources"]:
            if sid not in sources:
                raise ValueError(f"{m['id']} missing source {sid}")
        for fid in m["flags"]:
            if fid not in flags:
                raise ValueError(f"{m['id']} missing flag {fid}")
        if not m["steps"] or not m["sources"]:
            raise ValueError(f"{m['id']} missing steps/sources")


def feasibility(method: dict, amount: int) -> str:
    status = method["status"]
    if status == "prohibited":
        return "Excluded unlawful workaround; no lawful amount/cost quote."
    if status == "not_personal_route":
        return "Not a verified personal savings-remittance route."
    if status == "closed_loop":
        return "Not a free USD-to-US-account disposal route; closed-loop/product rules apply."
    if status == "supporting_only":
        return "Supporting step only; a separate lawful source/conversion route is required."
    if status == "unverified":
        return "Route eligibility/limits unverified; do not proceed without current official operator/bank confirmation."
    if method["id"] == "unionpay_atm":
        return "Large target generally unsuitable: CNY 100,000/person/year and CNY 10,000/card/day caps apply."
    if method["id"] == "cash_carry":
        return "Large target unsuitable/exceptional: China export permits and US declaration rules apply; do not split to evade."
    if method["id"] in {"wise_salary", "skyremit_salary"}:
        return "Subject to documented after-tax income, operator review and per-transaction CNY caps; transaction count depends on executed quote."
    if method["id"] == "bank_domestic_current_tt":
        return "Only if bank classifies customer as domestic individual; quota/document rules apply."
    return f"Conditional on lawful source, bank/operator approval and documents for USD {amount:,}; no fixed legal cap assumed."


def build_rows(procedures: dict, registry: dict) -> list[dict]:
    sources = {s["id"]: s for s in registry["sources"]}
    rows = []
    for m in procedures["methods"]:
        components, formula, default_source = COMPONENTS[m["cost_rule"]]
        sid = default_source if default_source in sources else m["sources"][0]
        # Prefer a route-specific primary source when the default is generic.
        if m["cost_rule"] == "unverified":
            # Do not cite a failed/404 operator URL as the row's official source.
            usable = [s for s in m["sources"] if s != "safe_rules" and sources[s].get("access") != "not_found"]
            sid = usable[0] if usable else "safe_rules"
        if m["cost_rule"] == "prohibited":
            sid = "pboc_crypto_2026" if m["id"] == "crypto_p2p" else "safe_fx_reg"
        if m["cost_rule"] == "closed_loop":
            sid = "hkma_wmc" if m["id"] == "wmc_southbound" else "safe_rules"
        src = sources[sid]
        for amount in AMOUNTS:
            row = {
                "amount_usd": amount,
                "method_id": m["id"],
                "method_name": m["name"],
                "category": m["category"],
                "route_status": m["status"],
                "feasibility_note": feasibility(m, amount),
                **{k: None for k in NUMERIC_COST_FIELDS},
                "published_components": components,
                "formula": formula,
                "flags": ";".join(m["flags"]),
                "source_id": sid,
                "source_url": src["url"],
                "source_title": f"{src['publisher']} — {src['title']}",
            }
            rows.append(row)
    return rows


def write_outputs(rows: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "as_of": "2026-11-08",
        "amount_grid_usd": AMOUNTS,
        "method_count": len({r['method_id'] for r in rows}),
        "row_count": len(rows),
        "numeric_policy": "Unknown/unverified numeric USD values are null in JSON and empty in CSV. Published components are text, not executable quotes.",
        "rows": rows,
    }
    (out_dir / "costs.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (out_dir / "costs.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row[k] is None else row[k]) for k in CSV_FIELDS})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate inputs and expected row count without writing")
    args = parser.parse_args()
    procedures = load_json("research/procedures.json")
    registry = load_json("research/sources/registry.json")
    findings = load_json("research/findings.json")
    validate_inputs(procedures, registry, findings)
    rows = build_rows(procedures, registry)
    expected = len(procedures["methods"]) * len(AMOUNTS)
    if len(rows) != expected:
        raise ValueError(f"expected {expected} rows, got {len(rows)}")
    if args.check:
        print(f"OK: {len(procedures['methods'])} methods x {len(AMOUNTS)} amounts = {len(rows)} rows; unknown numeric costs remain blank")
        return
    write_outputs(rows, ROOT / "research")
    # Public download lives at the site root; the canonical JSON remains under research/.
    with (ROOT / "costs.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row[k] is None else row[k]) for k in CSV_FIELDS})
    print(f"Wrote research/costs.json, research/costs.csv and costs.csv ({len(rows)} rows)")


if __name__ == "__main__":
    main()
