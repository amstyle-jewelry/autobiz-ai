import streamlit as st

# --- CONFIGURATION ---
MY_WHATSAPP = "+923016372254"
ADMIN_EMAIL = "shahzebbhutta813@gmail.com"

st.set_page_config(page_title="AutoBiz AI: Professional Agent", layout="wide")
st.title("💎 AutoBiz AI: Autonomous Jewelry Sales Agent")

# --- LOGIN & SUBSCRIPTION LOGIC ---
user_email = st.text_input("Enter your business email to login:")

if user_email == ADMIN_EMAIL:
    st.success("Welcome Shahzeb! System Active.")
    
    # --- PRODUCT SPECIFICATION INPUTS ---
    st.subheader("Product Details for Auto-Negotiation")
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader("Upload Jewelry Photo")
        # Yeh raha naya Jewelry Type function
        jewelry_type = st.selectbox("Jewelry Category", ["Necklace", "Ring", "Bracelet", "Earrings", "Pendant"])
        material = st.selectbox("Material Type", ["Gold", "Silver", "Platinum"])
    
    with col2:
        karat = st.selectbox("Purity (Karat/Grade)", ["24K", "22K", "21K", "18K", "925 Sterling (Silver)"])
        weight = st.number_input("Weight (Grams)", min_value=0.1)
        gram_price = st.number_input("Price per Gram ($)", min_value=0.1)
        total_quantity = st.number_input("Target Order Quantity", value=1000)

    if st.button("🚀 Start 24/7 Global Scouting"):
        if uploaded_file:
            st.info(f"Agent: Analyzing {jewelry_type} ({karat} {material}) at ${gram_price}/g...")
            st.write("Agent: Scanning Global Markets (Alibaba/Amazon/Dubai Souk)...")
            
            # Simulated AI Agent logic
            st.success("Deal Finalized!")
            st.write(f"✅ **Order:** {total_quantity} pieces of {jewelry_type}")
            st.write(f"✅ **Material Details:** {karat} {material} | {weight}g per piece")
            st.write(f"✅ **Rate:** ${gram_price} per gram")
            st.write(f"🔔 **WhatsApp Alert Sent to:** {MY_WHATSAPP}")
            st.write("Full buyer contact and invoice sent to your Gmail.")
        else:
            st.error("Please upload a photo!")

elif user_email:
    st.warning("Access restricted. Please pay $100 subscription to continue.")
    st.markdown("[Click here to pay $100](https://stripe.com/pay-link)")
            
