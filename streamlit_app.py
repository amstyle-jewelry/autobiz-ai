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
    uploaded_file = st.file_uploader("Upload Product Photo", type=['jpg', 'png'])
    if uploaded_file:
        st.image(uploaded_file, caption="Analyzing Product Features...")
        if st.button("🚀 Execute Global AI Hunt"):
            with st.spinner("A.m Style AI is scanning global markets..."):
                time.sleep(3) # AI Simulation
                st.write("### 🌐 Global Leads Identified:")
                st.info("Lead 1: Alibaba Wholesaler, China - Match: 98% - Status: Contacted")
                st.info("Lead 2: Amazon Prime Distributor, USA - Match: 94% - Status: Pending")
                st.info("Lead 3: TikTok Shop Influencer, UK - Match: 91% - Status: Outreach Done")
                st.success("Proposals successfully sent by A.m Style AI Agent.")
                
