import html
import streamlit as st

from utils import styling, data_loader, advanced_data

st.set_page_config(page_title="Agro Solutions — RiceCare AI", page_icon="🌱", layout="wide")
styling.inject_global_css()

st.markdown("## 🌱 Agro Solutions")
st.caption("General information on rice disease management, nutrients and farm support. "
           "Chemical, biological, natural, traditional and farm-practice approaches are kept separate.")

st.warning(
    "**Read first.** This is general information, **not a prescription** and not checked by an "
    "agricultural expert yet. An AI result from a photo is only a prediction, so confirm the problem "
    "with a local agriculture officer before treating. No doses are given here."
)


def esc(x):
    return html.escape(str(x))


def treatment_card(row):
    st.markdown(
        f"""
        <div class="rc-card" style="margin-bottom:0.8rem; height:auto;">
            <h4>{esc(row['approach_name'])}</h4>
            <p><b>What it is:</b> {esc(row['description'])}</p>
            <p><b>Evidence:</b> {esc(row['evidence_level'])}</p>
            <p><b>Safety:</b> {esc(row['safety_note'])}</p>
            <span class="rc-badge rc-badge-gold">{esc(row['verification_status'])}</span>
            <span class="rc-badge rc-badge-teal">{esc(row['data_label'])}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


tab_treat, tab_nutr, tab_schemes, tab_market = st.tabs(
    ["🌾 Disease management", "🧂 Nutrients", "🏛️ Government schemes", "🛒 Suppliers & products"]
)

# ---------------- DISEASE MANAGEMENT ----------------
with tab_treat:
    if advanced_data.load_treatments().empty:
        st.error("`data/advanced/treatment_options.csv` was not found. Upload the advanced data folder.")
    else:
        disease_ids = [d for d in data_loader.DISEASE_CLASSES if d != "HEALTHY"]
        names = {d: data_loader.get_disease_info(d)["disease_name"] for d in disease_ids}
        choice = st.selectbox(
            "Choose a disease",
            options=["— choose —"] + disease_ids,
            format_func=lambda d: d if d == "— choose —" else names[d],
        )
        if choice != "— choose —":
            tabs = st.tabs(list(advanced_data.CATEGORY_LABELS.values()))
            for tab, category in zip(tabs, advanced_data.CATEGORY_LABELS):
                with tab:
                    rows = advanced_data.get_treatments(choice, category)
                    if not rows:
                        st.caption("No entries for this category yet.")
                    for r in rows:
                        treatment_card(r)
            st.caption("Active ingredients are named only as commonly referenced in public extension "
                       "material. Always check current registration and the product label.")

# ---------------- NUTRIENTS ----------------
with tab_nutr:
    df = advanced_data.load_nutrients()
    if df.empty:
        st.error("`data/advanced/nutrient_issues.csv` was not found.")
    else:
        st.info("A soil test and plant test at an approved lab is the reliable way to confirm a nutrient "
                "problem. Some nutrient problems look like disease. Amounts are not given here.")
        for _, r in df.iterrows():
            st.markdown(f"**{esc(r['nutrient'])}**: {esc(r['issue_type'])}")
            st.markdown(f"- Typical symptoms: {r['typical_symptoms']}")
            st.markdown(f"- Notes: {r['link_to_disease_or_notes']}")
            st.caption(f"Label: {r['data_label']}")

# ---------------- SCHEMES ----------------
with tab_schemes:
    df = advanced_data.load_schemes()
    if df.empty:
        st.error("`data/advanced/government_schemes.csv` was not found.")
    else:
        st.warning("Scheme names only. Benefits and eligibility change, so check the official site before acting.")
        for _, r in df.iterrows():
            st.markdown(f"**{esc(r['scheme_name'])}** ({esc(r['type'])})")
            st.write(r["what_it_is"])
            portal = r["official_portal"]
            if portal.startswith("VERIFY"):
                st.caption("Official website: not listed here. Search for the official government site.")
            else:
                st.caption(f"Official website: {portal}")
            st.caption(f"{r['verification_status']}")

# ---------------- SUPPLIERS & PRODUCTS ----------------
def real_product_card(r, supplier):
    verified = str(r["verified"]).strip().lower() == "true"
    badge = ("<span class='rc-badge'>Details verified</span>" if verified else
             "<span class='rc-badge rc-badge-gold'>Supplier claim, not verified</span>")
    if r["price_inr"].strip():
        src = r["price_source"].strip() or "source not stated"
        when = r["last_checked"].strip() or "date not stated"
        price = f"₹{esc(r['price_inr'])} {esc(r['price_unit'])} (source: {esc(src)}, checked: {esc(when)})"
    else:
        price = "Not listed"
    reg = r["registration_number"].strip() or "Not provided"
    st.markdown(
        f"""
        <div class="rc-card" style="margin-bottom:0.8rem; height:auto;">
            <h4>{esc(r['product_name'])}</h4>
            <p><b>Category:</b> {esc(r['category'])} &nbsp;|&nbsp; <b>Supplier:</b> {esc(supplier)}</p>
            <p><b>Price:</b> {price}</p>
            <p><b>Availability:</b> {esc(r['availability'] or 'Unknown')} &nbsp;|&nbsp;
               <b>Registration no.:</b> {esc(reg)}</p>
            <p><b>Supplier says:</b> {esc(r['supplier_claim'] or 'Nothing stated')}</p>
            {badge}
            <span class="rc-badge rc-badge-teal">{esc(r['data_label'])}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


with tab_market:
    real_sup, real_prod = advanced_data.load_real_listings()

    if not real_prod.empty:
        st.info("Listings below were entered by the RiceCare AI team. Prices and claims come from the "
                "stated source and may be out of date. Registration numbers should be checked on the "
                "official registry before buying.")
        cats = ["All"] + sorted(real_prod["category"].unique())
        cat = st.selectbox("Product category", cats, key="real_cat")
        shown = real_prod if cat == "All" else real_prod[real_prod["category"] == cat]
        names = dict(zip(real_sup["supplier_id"], real_sup["supplier_name"]))
        for _, r in shown.iterrows():
            real_product_card(r, names.get(r["supplier_id"], "unknown"))
    else:
        st.error("**SAMPLE DATA ONLY.** No real listings have been added yet. The suppliers and products "
                 "below are fictional placeholders to test the page. They are not real businesses, and "
                 "no prices or registrations are shown.")
        sup = advanced_data.load_suppliers()
        prod = advanced_data.load_products()
        if sup.empty or prod.empty:
            st.error("Sample supplier or product files were not found in `data/advanced/`.")
        else:
            cats = ["All"] + sorted(prod["category"].unique())
            cat = st.selectbox("Product category", cats)
            shown = prod if cat == "All" else prod[prod["category"] == cat]
            names = dict(zip(sup["supplier_id"], sup["supplier_name"]))
            for _, r in shown.iterrows():
                st.markdown(f"**{esc(r['product_name'])}**")
                st.caption(f"Category: {r['category']} · Supplier: {names.get(r['supplier_id'], 'unknown')}")
                st.caption("Claim: " + r["supplier_claim"] + " · Price: not listed · Registration: sample only · "
                           "Verified: no")

styling.disclaimer()
styling.footer()
