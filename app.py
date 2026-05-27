import streamlit as st

# Setup Page
st.set_page_config(page_title="Fashion Sanctuary", layout="wide")

# 1. THE WELCOME PORTAL (Only shows if 'initialized' is False)
if 'initialized' not in st.session_state:
    st.title("✨ Welcome to your Fashion Sanctuary")
    st.write("Let's set up your profile for a perfect fit.")
    
    st.session_state.gender = st.radio("Select Profile", ["Masculine", "Feminine", "Neutral/Fluid"])
    st.session_state.unit = st.radio("Measurement Unit", ["cm", "inches"])
    
    if st.session_state.unit == "cm":
        st.session_state.chest = st.number_input("Chest (cm)")
    else:
        st.session_state.chest = st.number_input("Chest (inches)") * 2.54
        
    if st.button("Enter Studio"):
        st.session_state.initialized = True
        st.rerun() # Refresh to show Main Page

# 2. THE MAIN PAGE (Creative Hub)
else:
    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>Welcome back to your Sanctuary!</h1>", unsafe_allow_html=True)
    
    # Create two big, beautiful buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📸 Magic Mirror (Image Search)"):
            st.session_state.page = "image_search"
            
    with col2:
        if st.button("🎨 Design Studio (Create Outfit)"):
            st.session_state.page = "design_studio"
            
    # Show content based on which button was clicked
     if 'page' in st.session_state:
        if st.session_state.page == "design_studio":
            st.write("### Welcome to the Design Studio")
            # --- MANNEQUIN UI GOES HERE ---
       with studio:
                   st.subheader("🎨 Virtual Dress-Up Studio")
    
    # Selection Controls
    col_ctrl, col_view = st.columns([1, 1])
    
     with col_ctrl:
        skin = st.color_picker("Skin Tone", "#FFD1A9")
        top_c = st.color_picker("Top Color", "#FF6B6B")
        bot_c = st.color_picker("Bottom Color", "#4ECDC4")
        neck_type = st.selectbox("Neckline", ["Crew", "V-Neck", "Cowl", "Bandh-gala"])
        
     with col_view:
        # The Mannequin Engine (SVG Code)
        st.markdown(f"""
        <svg width="200" height="400" viewBox="0 0 200 400">
            <circle cx="100" cy="50" r="40" fill="{skin}" />
            <rect x="50" y="100" width="100" height="120" rx="10" fill="{top_c}" />
            <rect x="60" y="230" width="80" height="150" rx="10" fill="{bot_c}" />
            <text x="100" y="160" font-family="Arial" font-size="12" fill="white" text-anchor="middle">{neck_type}</text>
        </svg>
        """, unsafe_allow_html=True)
    
