import streamlit as st

st.set_page_config(page_title="Fashion Sanctuary", layout="wide")

# Initializing session state to remember user profile
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

# 1. WELCOME PORTAL
if not st.session_state.initialized:
    st.title("✨ Welcome to your Fashion Sanctuary")
    st.write("Set up your profile to begin your creative journey.")
    
    st.session_state.gender = st.radio("Select Profile", ["Masculine", "Feminine", "Neutral/Fluid"])
    st.session_state.unit = st.radio("Measurement Unit", ["cm", "inches"])
    
    if st.button("Enter Studio"):
        st.session_state.initialized = True
        st.rerun()

# 2. MAIN CREATIVE HUB
else:
    st.title("👗 Fashion Sanctuary: Creative Studio")
    
    # Creating the separate "Windows" (Tabs)
    explorer, studio = st.tabs(["🔍 Global Fashion Explorer", "🎨 Virtual Design Studio"])

    with explorer:
        st.header("Search Global Inventory")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📸 Magic Mirror (Image Search)"):
                st.session_state.page = "image_search"
        with col2:
            if st.button("🎨 Design Studio (Create Outfit)"):
                st.session_state.page = "design_studio"

    with studio:
        st.subheader("🎨 Virtual Dress-Up Studio")
        st.write("Use the controls below to customize your mannequin.")
        
        col_ctrl, col_view = st.columns([1, 1])
        
        with col_ctrl:
            skin = st.color_picker("Skin Tone", "#FFD1A9")
            top_c = st.color_picker("Top Color", "#FF6B6B")
            bot_c = st.color_picker("Bottom Color", "#4ECDC4")
            neck_type = st.selectbox("Neckline", ["Crew", "V-Neck", "Cowl", "Bandh-gala"])
            
        with col_view:
            # The Mannequin Engine (Layered SVG)
            st.markdown(f"""
            <div style="text-align: center;">
                <svg width="200" height="400" viewBox="0 0 200 400">
                    <circle cx="100" cy="50" r="40" fill="{skin}" />
                    <rect x="50" y="100" width="100" height="120" rx="10" fill="{top_c}" />
                    <rect x="60" y="230" width="80" height="150" rx="10" fill="{bot_c}" />
                    <text x="100" y="160" font-family="Arial" font-size="12" fill="white" text-anchor="middle">{neck_type}</text>
                </svg>
            </div>
            """, unsafe_allow_html=True)
            
