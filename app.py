import streamlit as st
import pandas as pd

# 1. THE SHOPPING WAREHOUSE (Mock Data)
# In a full app, this would pull from millions of real clothes across the web
inventory = [
    {"name": "Silk Cowl-Neck Camisole", "brand": "Zara via App", "category": "Top", "neckline": "Cowl Neck", "back_style": "Standard", "price": 39.99, "quality": "High (100% Silk)", "chest": 88, "waist": 70},
    {"name": "Satin Drape V-Neck Top", "brand": "ASOS via App", "category": "Top", "neckline": "V-Neck", "back_style": "Standard", "price": 25.00, "quality": "Medium (Satin-Poly)", "chest": 86, "waist": 68},
    {"name": "Backless Summer Crop Top", "brand": "H&M via App", "category": "Top", "neckline": "V-Neck", "back_style": "Backless", "price": 19.99, "quality": "Medium (Linen Blend)", "chest": 84, "waist": 66},
    {"name": "Racerback Ribbed Tank", "brand": "Nordstrom via App", "category": "Top", "neckline": "Scoop Neck", "back_style": "Racerback", "price": 22.50, "quality": "High (Ribbed Cotton)", "chest": 90, "waist": 72},
    {"name": "High-Waisted Wide-Leg Trousers", "brand": "Mango via App", "category": "Bottom", "neckline": "N/A", "back_style": "N/A", "price": 59.99, "quality": "High (Tailored Wool Blend)", "chest": 0, "waist": 70},
    {"name": "Relaxed Tailored Chinos", "brand": "Amazon Fashion", "category": "Bottom", "neckline": "N/A", "back_style": "N/A", "price": 29.99, "quality": "Medium (Cotton Twill)", "chest": 0, "waist": 74}
]
df = pd.DataFrame(inventory)

# 2. WEBSITE VISUAL LAYOUT
st.set_page_config(page_title="Universal Fashion Search", page_icon="👔", layout="wide")
st.title("👔 Universal Omnichannel Fashion Search Engine")
st.write("Find the exact clothing items looking across all shopping platforms, tailored to your budget and exact body fit.")

st.markdown("---")

# Sidebar for inputs
st.sidebar.header("📐 Step 1: Your Perfect Fit Profile")
user_chest = st.sidebar.number_input("Chest Circumference (cm)", value=88)
user_waist = st.sidebar.number_input("Waist Circumference (cm)", value=70)

st.sidebar.header("🎨 Step 2: Design Your Outfit")
search_mode = st.sidebar.radio("Choose Search Type:", ["Custom Outfit Builder", "Image Upload Search (Simulation)"])

if search_mode == "Custom Outfit Builder":
    neck_select = st.sidebar.selectbox("Top Neckline", ["Cowl Neck", "V-Neck", "Scoop Neck"])
    back_select = st.sidebar.selectbox("Top Back Style", ["Standard", "Backless", "Racerback"])
    bottom_select = st.sidebar.selectbox("Bottom Silhouette", ["Wide-Leg Trousers", "Tailored Chinos"])
else:
    uploaded_file = st.sidebar.file_uploader("Upload style inspiration image...", type=["jpg", "png", "jpeg"])
    st.sidebar.info("Simulation mode: Uploading an image parses style tags automatically using AI features.")
    neck_select, back_select, bottom_select = "Cowl Neck", "Standard", "Wide-Leg Trousers" # Fallback defaults for simulation

# 3. SEARCH & MATCHING ENGINE LOGIC
if st.sidebar.button("Scan All Shopping Apps", type="primary"):
    st.subheader("✨ Sourced Marketplace Matches Found For You")
    
    # Filter by Style Configurations
    if search_mode == "Custom Outfit Builder":
        filtered_df = df[
            ((df["neckline"] == neck_select) & (df["back_style"] == back_select)) | 
            (df["name"].str.contains(bottom_select.split('-')[0], case=False))
        ]
    else:
        filtered_df = df.copy() # Simulation returns full catalog for visual matching demo
        
    # Filter by Fit Profile (Allowing a tiny +/- 4cm tolerance)
    valid_matches = filtered_df[
        ((filtered_df["category"] == "Top") & (abs(filtered_df["chest"] - user_chest) <= 4)) |
        ((filtered_df["category"] == "Bottom") & (abs(filtered_df["waist"] - user_waist) <= 4))
    ]
    
    if valid_matches.empty:
        st.warning("No exact item matches your physical dimension thresholds on major retail networks right now. Try slightly adjusting size tolerances.")
    else:
        # Sort by lowest price & high quality
        sorted_results = valid_matches.sort_values(by=["price", "quality"], ascending=[True, False])
        
        # Display items nicely on the screen
        for index, row in sorted_results.iterrows():
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"### **{row['name']}**")
                    st.caption(f"Sourced Platform: **{row['brand']}** | Material: *{row['quality']}*")
                with col2:
                    st.markdown(f"## **${row['price']}**")
                st.info(f"✅ Sizing Match Validated: Configured specifications seamlessly match your personal dimensions.")
                st.markdown("---")
