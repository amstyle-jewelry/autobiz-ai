import streamlit as st

st.set_page_config(page_title="AutoBiz AI - Jewelry", layout="wide")
st.title("💎 AutoBiz AI: Jewelry Sales Automation")
st.write("Professional AI-powered tool for jewelry showrooms.")

st.sidebar.header("Account Status")
st.sidebar.info("Plan: Professional ($50/month)")

st.header("Upload Jewelry Design")
uploaded_file = st.file_uploader("Upload product image for AI analysis", type=['jpg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Analyzing design...', use_column_width=True)
    st.success("AI search active: Finding international wholesale buyers...")

st.header("Manage Deals")
st.write("Negotiation bot is ready. Manage your global trade leads below.")
