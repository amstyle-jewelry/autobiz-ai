import streamlit as st
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION ---
ADMIN_EMAIL = "shahzebbhutta813@gmail.com"
EMAIL_PASS = "yahan_apna_google_app_password_dalein" # Google se generate karein

def send_negotiation_email(buyer_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = ADMIN_EMAIL
    msg['To'] = buyer_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ADMIN_EMAIL, EMAIL_PASS)
        smtp.send_message(msg)

# --- UI & LOGIC ---
st.title("🚀 AutoBiz VIP: Full-Auto Agent")

if 'user' not in st.session_state: st.session_state.user = None

email_input = st.text_input("Login with your Gmail")
if st.button("Login"):
    st.session_state.user = email_input

if st.session_state.user == ADMIN_EMAIL:
    st.success("Admin Access Granted")
    target_buyer = st.text_input("Buyer Email")
    if st.button("Send Automated Offer"):
        send_negotiation_email(target_buyer, "Jewelry Proposal", "I have a high-quality necklace for you.")
        st.write("Email sent successfully to buyer!")
        
