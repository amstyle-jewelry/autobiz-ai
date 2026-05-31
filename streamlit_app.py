import streamlit as st
import time

# Branding Setup
st.set_page_config(page_title="A.m Style | Global AI Agency", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main-header {background: #000; padding: 20px; border-radius: 15px; text-align: center; color: #FFD700;}
    .stButton>button {width: 100%; border-radius: 5px; background-color: #FFD700; color: #000; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>A.m Style | Autonomous Global Scout</h1></div>", unsafe_allow_html=True)

# Admin Configuration (Aapke liye)
ADMIN_EMAIL = "shahzeb@amstyle.com" 

# Session State Initialization
if 'access' not in st.session_state: st.session_state.access = "guest"

# Authentication Logic
st.sidebar.header("Login")
user_email = st.sidebar.text_input("Enter Email")

if st.sidebar.button("Login"):
    if user_email == ADMIN_EMAIL:
        st.session_state.access = "admin"
        st.rerun()
    elif "paid_user" in st.session_state:
        st.session_state.access = "pro"
        st.rerun()

# --- APP LOGIC ---

if st.session_state.access == "admin":
    st.success("Admin Mode: Welcome back, Shahzeb.")
    show_app = True
elif st.session_state.access == "pro":
    st.success("Welcome, Pro Member.")
    show_app = True
else:
    show_app = False
    st.warning("Access Restricted: This is a high-end AI tool.")
    st.subheader("Subscription: $100/Month")
    if st.button("Pay $100 via Stripe & Activate"):
        # Yahan Stripe ka link trigger hoga
        st.session_state.paid_user = True
        st.session_state.access = "pro"
        st.rerun()

# Main AI Functionality
if show_app:
    
if show_app:
    uploaded_file = st.file_uploader("Upload Product Photo", type=['jpg', 'png'], key="main_upload")
    if uploaded_file:
        st.image(uploaded_file, caption="Analyzing Product Features...")
        
        # Details inputs
        c1, c2, c3 = st.columns(3)
        weight = c1.text_input("Weight (Grams)")
        carat = c2.text_input("Carat (e.g. 22K)")
        price = c3.text_input("Price ($)")
        material = st.selectbox("Select Material", ["Gold", "Silver"])
        
        if st.button("Execute Global AI Hunt"):
            with st.spinner("AI is scanning global markets..."):
                time.sleep(3) # AI Simulation
                
                # Sabhi details ke sath display
                st.write("### Product & Market Analysis")
                st.write(f"**Material:** {material}")
                st.write(f"**Weight:** {weight}g | **Carat:** {carat} | **Price:** ${price}")
                
                st.write("🌐 **Global Leads Identified:**")
                st.info("Lead 1: Alibaba Wholesaler, China - Match: 98% - Status: Contacted")
                st.info("Lead 2: Amazon Prime Distributor, USA - Match: 94% - Status: Pending")
                st.info("Lead 3: TikTok Shop Influencer, UK - Match: 91% - Status: Outreach Done")
                
                # Final confirmation message
                st.success(f"Proposal sent for {material} ({weight}g, {carat}, ${price}) successfully.")
        
