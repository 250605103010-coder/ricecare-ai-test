"""
advanced_data.py
----------------
Loads the extra portal data from data/advanced/ (treatments, nutrients, schemes,
sample suppliers and products). Separate from data_loader.py so nothing
existing is changed. Every row carries a `data_label` that the pages show.
"""

import os
import pandas as pd

ADV_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "advanced"
)

LISTINGS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "listings"
)

# Order and display names for the treatment categories. Kept separate on purpose.
CATEGORY_LABELS = {
    "CHEMICAL": "🧪 Chemical",
    "BIOLOGICAL": "🦠 Biological",
    "NATURAL": "🌿 Natural",
    "TRADITIONAL": "🏺 Traditional",
    "CULTURAL_PRACTICE": "🌾 Farm practices",
}


def _read(name):
    path = os.path.join(ADV_DIR, name)
    if not os.path.exists(path):
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def load_treatments():
    return _read("treatment_options.csv")


def get_treatments(disease_id: str, category: str) -> list:
    df = load_treatments()
    if df.empty:
        return []
    m = df[(df["disease_id"] == disease_id) & (df["category"] == category)]
    return m.to_dict(orient="records")


def load_nutrients():
    return _read("nutrient_issues.csv")


def load_schemes():
    return _read("government_schemes.csv")


def load_suppliers():
    return _read("suppliers_sample.csv")


def load_products():
    return _read("products_sample.csv")


def is_sample_label(label: str) -> bool:
    return str(label).startswith(("SAMPLE", "SYNTHETIC"))


def _read_listing(name):
    path = os.path.join(LISTINGS_DIR, name)
    if not os.path.exists(path):
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def load_real_listings():
    """Returns (suppliers, products) for REAL listings. Only suppliers who agreed
    to be listed (consent_to_list = yes) and their products are returned."""
    sup = _read_listing("suppliers.csv")
    prod = _read_listing("products.csv")
    if sup.empty or prod.empty:
        return pd.DataFrame(), pd.DataFrame()
    sup = sup[sup["consent_to_list"].str.strip().str.lower() == "yes"]
    prod = prod[prod["supplier_id"].isin(sup["supplier_id"])]
    return sup, prod
