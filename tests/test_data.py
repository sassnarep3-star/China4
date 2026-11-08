import csv
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_data


class DataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.procedures = json.loads((ROOT / "research/procedures.json").read_text())
        cls.registry = json.loads((ROOT / "research/sources/registry.json").read_text())
        cls.findings = json.loads((ROOT / "research/findings.json").read_text())
        cls.rows = build_data.build_rows(cls.procedures, cls.registry)

    def test_inputs_validate(self):
        build_data.validate_inputs(self.procedures, self.registry, self.findings)

    def test_exact_40_by_28_grid(self):
        self.assertEqual(len(self.rows), len(self.procedures["methods"]) * 40)
        self.assertGreaterEqual(len(self.procedures["methods"]), 28)
        for method in self.procedures["methods"]:
            amounts = [r["amount_usd"] for r in self.rows if r["method_id"] == method["id"]]
            self.assertEqual(amounts, list(range(10000, 400001, 10000)), method["id"])

    def test_unknown_numeric_costs_are_blank(self):
        for row in self.rows:
            for field in build_data.NUMERIC_COST_FIELDS:
                self.assertIsNone(row[field], (row["method_id"], row["amount_usd"], field))

    def test_every_row_has_registered_official_source(self):
        sources = {s["id"]: s for s in self.registry["sources"]}
        for row in self.rows:
            self.assertIn(row["source_id"], sources)
            self.assertEqual(row["source_url"], sources[row["source_id"]]["url"])
            self.assertTrue(row["source_url"].startswith(("https://", "http://")))
            self.assertNotEqual(sources[row["source_id"]].get("access"), "not_found")

    def test_csv_matches_json_and_blanks(self):
        with (ROOT / "costs.csv").open(newline="") as fh:
            csv_rows = list(csv.DictReader(fh))
        self.assertEqual(len(csv_rows), len(self.rows))
        for csv_row, row in zip(csv_rows, self.rows):
            self.assertEqual(int(csv_row["amount_usd"]), row["amount_usd"])
            self.assertEqual(csv_row["method_id"], row["method_id"])
            self.assertEqual(csv_row["source_url"], row["source_url"])
            for field in build_data.NUMERIC_COST_FIELDS:
                self.assertEqual(csv_row[field], "")
        canonical = json.loads((ROOT / "research/costs.json").read_text())
        self.assertEqual(canonical["rows"], self.rows)

    def test_prohibited_and_closed_loop_are_not_recommended(self):
        for method in self.procedures["methods"]:
            if method["category"] == "prohibited":
                self.assertEqual(method["status"], "prohibited")
                self.assertIn("Do not", " ".join(method["steps"]))
            if method["status"] == "closed_loop":
                self.assertIn("not", method["summary"].lower())

    def test_boc_components_not_invented_usd_total(self):
        row = next(r for r in self.rows if r["method_id"] == "bank_salary_tt" and r["amount_usd"] == 10000)
        self.assertIn("CNY 50", row["published_components"])
        self.assertIn("CNY 260", row["published_components"])
        self.assertIn("CNY 150", row["published_components"])
        self.assertIsNone(row["all_in_cost_usd"])
        self.assertIsNone(row["net_usd"])

    def test_flags_exist(self):
        flags = {f["id"] for f in self.findings["open_flags"]}
        for method in self.procedures["methods"]:
            for flag in method["flags"]:
                self.assertIn(flag, flags)


if __name__ == "__main__":
    unittest.main()
