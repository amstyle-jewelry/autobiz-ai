import streamlit as st
from openai import OpenAI
from duckduckgo_search import DDGS
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# --- APP CONFIGURATION ---
st.set_page_config(page_title="AutoBiz Autonomous Agent", layout="wide")
st.title("🤖 AutoBiz: Fully Autonomous Sales Agent")

# API Setup from Secrets
try:
    openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Please set OPENAI_API_KEY in Streamlit Secrets.")

# --- AGENT FUNCTIONS ---
def run_autonomous_agent(product_query):
    # 1. Internet Scouting
    with DDGS() as ddgs:
        results = list(ddgs.text(product_query, max_results=3))
    
    # 2. AI Negotiation
    prompt = f"Product: {product_query}. Results: {results}. Write a professional pitch."
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- UI ---
cat = st.selectbox("Category", ["Necklace", "Ring", "Bracelet", "Other"])
mat = st.selectbox("Material", ["Gold", "Silver"])

if st.button("🚀 Start Autonomous Scouting"):
    with st.spinner("Agent is searching and negotiating..."):
        report = run_autonomous_agent(f"wholesale {mat} {cat} buyers globally")
        st.write("### AI Negotiation Report:")
        st.write(report)
        
        # 1. WhatsApp Alert
        try:
            twilio_client = Client(st.secrets["TWILIO_SID"], st.secrets["TWILIO_AUTH_TOKEN"])
            twilio_client.messages.create(
                body=f"AutoBiz Agent Update: {report[:100]}", 
                from_='whatsapp:+14155238886', 
                to='whatsapp:+923016372254'
            )
            st.success("WhatsApp Alert Sent!")
        except Exception as e:
            st.error(f"WhatsApp Error: {e}")
            
        # 2. Gmail Alert
        try:
            msg = EmailMessage()
            msg.set_content(report)
            msg['Subject'] = "AutoBiz Autonomous Deal Report"
            msg['From'] = "shahzebbhutta813@gmail.com"
            msg['To'] = "shahzebbhutta813@gmail.com"
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("shahzebbhutta813@gmail.com", st.secrets["GMAIL_APP_PASSWORD"])
                smtp.send_message(msg)
            st.success("Email Report Sent!")
        except Exception as e:
            st.error(f"Gmail Error: {e}")
            
