"""Checks the advanced data files. Run from the project root:
    python data/advanced/validate_advanced_data.py
Only needs Python. Exits with an error message if something is wrong."""
import csv, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VALID_DISEASES = {"HEALTHY", "RICE_BLAST", "BROWN_SPOT", "BACTERIAL_LEAF_BLIGHT"}
problems = []

def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, restkey="_EXTRA"))

for path in sorted(glob.glob(os.path.join(HERE, "*.csv"))):
    name = os.path.basename(path)
    rows = read(path)
    if not rows:
        problems.append(f"{name}: no rows"); continue
    ids = set()
    for i, r in enumerate(rows, 2):
        if "_EXTRA" in r or None in r.values():
            problems.append(f"{name} line {i}: wrong number of columns")
        if not (r.get("data_label") or "").strip():
            problems.append(f"{name} line {i}: missing data_label")
        first = list(r.values())[0]
        if first in ids:
            problems.append(f"{name} line {i}: duplicate id {first}")
        ids.add(first)
        if "disease_id" in r and r["disease_id"] not in VALID_DISEASES:
            problems.append(f"{name} line {i}: unknown disease_id {r['disease_id']}")
        if name.endswith("_sample.csv") and name not in ("questions_sample.csv",):
            label = r.get("product_name") or r.get("supplier_name") or r.get("display_name") or ""
            if "SAMPLE" not in label:
                problems.append(f"{name} line {i}: sample row not named SAMPLE")
        if name == "products_sample.csv" and (r["price_inr"].strip() or r["verified"] != "false"):
            problems.append(f"{name} line {i}: sample product must have no price and verified=false")
        if name == "experts_sample.csv" and r["verification_status"] != "SAMPLE_NOT_REAL":
            problems.append(f"{name} line {i}: expert must be marked SAMPLE_NOT_REAL")
    print(f"ok  {name}: {len(rows)} rows")

if problems:
    print("\nPROBLEMS:"); [print(" -", p) for p in problems]; sys.exit(1)
print("\nAll checks passed.")
