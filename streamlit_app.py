import streamlit as st
import openai
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION (Direct Integration) ---
ADMIN_EMAIL = "shahzebbhutta813@gmail.com"
MY_WHATSAPP = "+923016372254"

# --- CORE FUNCTIONS ---
def send_whatsapp_alert(details):
    # Twilio API connection
    client = Client(st.secrets["TWILIO_SID"], st.secrets["TWILIO_AUTH_TOKEN"])
    message = client.messages.create(
        body=f"AutoBiz Alert: New Deal! {details}",
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{MY_WHATSAPP}'
    )
    return message.sid

def send_email_alert(details):
    # Gmail SMTP connection
    msg = EmailMessage()
    msg.set_content(f"New Order Details:\n{details}")
    msg['Subject'] = "Official Order Alert - AutoBiz AI"
    msg['From'] = ADMIN_EMAIL
    msg['To'] = ADMIN_EMAIL
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ADMIN_EMAIL, st.secrets["GMAIL_APP_PASSWORD"])
        smtp.send_message(msg)

# --- UI INTERFACE ---
st.title("💎 AutoBiz AI: Autonomous Sales Agent")
user_input = st.text_input("Enter login email:")

if user_input == ADMIN_EMAIL:
    st.write("System Active")
    # Product Inputs
    cat = st.selectbox("Category", ["Necklace", "Ring", "Bracelet"])
    mat = st.selectbox("Material", ["Gold", "Silver"])
    price = st.number_input("Price ($)")
    qty = st.number_input("Quantity")

    if st.button("Finalize Deal"):
        deal_info = f"{qty} pcs of {mat} {cat} at ${price}/g"
        
        # Real Integration Calls
        send_whatsapp_alert(deal_info)
        send_email_alert(deal_info)
        
        st.success("Deal Finalized! Check your WhatsApp and Gmail.")
        
