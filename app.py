import streamlit as st

from utils import styling
from utils.model_utils import is_demo_mode

st.set_page_config(
    page_title="RiceCare AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================= GOOGLE LOGIN =================

if not st.user.is_logged_in:

    st.markdown(
        """
        <div style="text-align:center; margin-top:120px;">
            <h1>🌾 RiceCare AI</h1>
            <h3>AI-Powered Rice Disease & Molecular Insights</h3>
            <p>Please sign in with your Google account to continue.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button(
            "🔐 Continue with Google",
            use_container_width=True
        ):
            st.login("google")

    st.stop()


# ================= SIDEBAR =================

with st.sidebar:
    st.markdown("### 🌾 RiceCare AI")

    st.success("✅ Logged in")

    if st.user.name:
        st.write(f"👤 **{st.user.name}**")

    if st.user.email:
        st.caption(st.user.email)

    if is_demo_mode():
        st.warning(
            "⚙️ Demo Mode\n\n"
            "No trained model found in `/model`."
        )
    else:
        st.success("🤖 Trained model loaded")

    if st.button("🚪 Logout", use_container_width=True):
        st.logout()


# ================= MAIN PAGE =================

styling.inject_global_css()

styling.hero(
    "🌾 RiceCare AI",
    "AI-Powered Rice Disease & Molecular Insights",
    "An integrated platform connecting rice disease detection, "
    "agricultural solutions and bioinformatics research.",
)

st.markdown("<br>", unsafe_allow_html=True)

# ================= INTERFACES =================

st.markdown("## Choose Your Interface")
st.caption("Select the area you want to explore.")

col1, col2, col3 = st.columns(3)


# ================= FARMER CARE =================

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

    if st.button(
        "📷 Enter Farmer Care",
        use_container_width=True
    ):
        st.switch_page("Analyze_My_Plant.py")


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

    if st.button(
        "🌱 Explore Solutions",
        use_container_width=True
    ):
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

    if st.button(
        "🔬 Enter Agro Research",
        use_container_width=True
    ):
        st.switch_page("pages/3_Molecular_Information.py")


# ================= WORKFLOW =================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("## 🔬 How RiceCare AI Connects Everything")

styling.flow_diagram(
    [
        "🌾 Rice Plant",
        "🤖 AI Detection",
        "🌱 Agro Solutions",
        "🧬 Agro Research",
    ]
)


# ================= PROJECT HIGHLIGHTS =================

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


# ================= FOOTER =================

st.markdown("<br>", unsafe_allow_html=True)

styling.disclaimer()
styling.footer()
