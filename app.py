"""
RiceCare AI — Home
Main entry point for the multipage Streamlit application.
"""

import streamlit as st

from utils import styling
from utils.model_utils import is_demo_mode

st.set_page_config(
    page_title="RiceCare AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

styling.inject_global_css()

# ================= SIDEBAR =================

with st.sidebar:
    st.markdown("### 🌾 RiceCare AI")
    st.caption(
        "AI-powered rice disease detection, "
        "agro solutions and bioinformatics research."
    )

    if is_demo_mode():
        st.warning(
            "⚙️ Demo Mode\n\n"
            "No trained model found in `/model`. "
            "Predictions currently use demo mode."
        )
    else:
        st.success("✅ Trained model loaded")

# ================= HERO =================

styling.hero(
    "🌾 RiceCare AI",
    "AI-Powered Rice Disease & Molecular Insights",
    "An integrated platform connecting rice disease detection, "
    "agricultural solutions and bioinformatics research.",
)

st.markdown("<br>", unsafe_allow_html=True)

# ================= THREE INTERFACES =================

st.markdown("## Choose Your Interface")
st.caption("Select the area you want to explore.")

col1, col2, col3 = st.columns(3)

# ================= FARMER =================

with col1:
    st.markdown(
        """
        <div class="rc-card">
            <h2>👨‍🌾 Farmer Care</h2>
            <p>
            Identify rice leaf diseases using AI,
            understand symptoms and explore disease information.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("📷 Enter Farmer Care", use_container_width=True):
        st.switch_page("pages/Analyze_My_Plant.py")

# ================= AGRO SOLUTIONS =================

with col2:
    st.markdown(
        """
        <div class="rc-card">
            <h2>🌱 Agro Solutions</h2>
            <p>
            Explore chemical, organic and
            plant-derived approaches for rice disease management.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🌱 Explore Solutions", use_container_width=True):
        st.switch_page("pages/3_Agro_Solutions.py")

# ================= AGRO RESEARCH =================

with col3:
    st.markdown(
        """
        <div class="rc-card">
            <h2>🧬 Agro Research</h2>
            <p>
            Explore DNA, proteins, BLAST, MSA,
            molecular information and computational research.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🔬 Enter Agro Research", use_container_width=True):
        st.switch_page("pages/3_Molecular_Information.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# ================= WORKFLOW =================

st.markdown("## 🔬 How RiceCare AI Connects Everything")

styling.flow_diagram(
    [
        "🌾 Rice Plant",
        "🤖 AI Detection",
        "🌱 Agro Solutions",
        "🧬 Molecular Research",
    ]
)

# ================= HIGHLIGHTS =================

st.markdown("## Project Highlights")

h1, h2, h3, h4 = st.columns(4)

with h1:
    st.markdown(
        """
        <div class="rc-card">
            <h4>🌾 Rice Diseases</h4>
            <p>
            Rice Blast · Brown Spot ·
            Bacterial Leaf Blight
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h2:
    st.markdown(
        """
        <div class="rc-card">
            <h4>🤖 AI Detection</h4>
            <p>
            Image-based rice leaf
            disease classification.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h3:
    st.markdown(
        """
        <div class="rc-card">
            <h4>🌱 Agro Solutions</h4>
            <p>
            Chemical, organic and
            plant-derived approaches.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h4:
    st.markdown(
        """
        <div class="rc-card">
            <h4>🧬 Bioinformatics</h4>
            <p>
            BLAST · MSA · Protein
            analysis · Molecular research
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

styling.disclaimer()
styling.footer()
