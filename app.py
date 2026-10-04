import streamlit as st

st.set_page_config(
    page_title="Agro Solutions",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Agro Solutions")

st.write(
    "Explore chemical, organic and plant-derived approaches "
    "for rice disease management."
)

st.divider()

st.subheader("🌾 Select a Rice Disease")

disease = st.selectbox(
    "Choose disease",
    [
        "Rice Blast",
        "Brown Spot",
        "Bacterial Leaf Blight",
    ]
)

st.write("Selected disease:", disease)

st.subheader("🌱 Solution Categories")

col1, col2 = st.columns(2)

with col1:
    st.info("⚗️ Chemical Solutions")
    st.write(
        "Disease-specific chemical management information "
        "will be added here."
    )

with col2:
    st.success("🌿 Organic / Plant-Based Solutions")
    st.write(
        "Medicinal-plant-derived compounds and biological "
        "approaches will be added here."
    )
