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
            
st.set_page_config(page_title="Fashion Sanctuary Game", layout="wide")

# Session state to store user's current "wardrobe" choices
if 'top_color' not in st.session_state:
    st.session_state.top_color = "#FF6B6B"
    st.session_state.bot_color = "#4ECDC4"
    st.session_state.neck = "Crew"

st.title("🎮 Fashion Sanctuary: Dress-Up Studio")

# Layout: Sidebar for "Dressing Room" controls
with st.sidebar:
    st.header("👗 Dressing Room")
    st.session_state.top_color = st.color_picker("Top Color", st.session_state.top_color)
    st.session_state.bot_color = st.color_picker("Bottom Color", st.session_state.bot_color)
    st.session_state.neck = st.selectbox("Neckline Style", ["Crew", "V-Neck", "Cowl", "Bandh-gala", "Halter"])
    st.session_state.style = st.selectbox("Style Category", ["Western", "Indian", "Fusion"])

# Main Canvas: The "Doll" Area
st.subheader("Your Mannequin")
st.markdown(f"""
<div style="display: flex; justify-content: center; align-items: center; height: 500px; background-color: #f0f2f6; border-radius: 20px;">
    <svg width="300" height="500" viewBox="0 0 300 500">
        <circle cx="150" cy="80" r="50" fill="#FFD1A9" />
        <rect x="120" y="130" width="60" height="200" rx="10" fill="#FFD1A9" />
        
        <rect x="80" y="140" width="140" height="100" rx="15" fill="{st.session_state.top_color}" />
        <text x="150" y="190" font-family="Verdana" font-size="14" fill="white" text-anchor="middle">{st.session_state.neck}</text>
        
        <rect x="90" y="240" width="120" height="150" rx="10" fill="{st.session_state.bot_color}" />
        
        <text x="150" y="450" font-family="Arial" font-size="20" font-weight="bold" fill="#333" text-anchor="middle">
            Style: {st.session_state.style}
        </text>
    </svg>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.info("💡 **How to play:** Use the sidebar on the left to change your outfit. The mannequin updates in real-time!")

            
