import streamlit as st
from openai import OpenAI
from duckduckgo_search import DDGS
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

st.title("🤖 AutoBiz: Fully Autonomous Agent")

# API Setup
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def run_agent(product_query):
    # 1. Autonomous Scouting
    with DDGS() as ddgs:
        results = list(ddgs.text(product_query, max_results=3))
    
    # 2. AI Negotiation
    prompt = f"Product: {product_query}. Results: {results}. Write a professional pitch."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- UI & LOGIC ---
cat = st.selectbox("Category", ["Necklace", "Ring", "Bracelet"])
mat = st.selectbox("Material", ["Gold", "Silver"])

if st.button("Start Autonomous Scouting"):
    report = run_agent(f"wholesale {mat} {cat} buyers globally")
    st.write(report)
    
    # 1. WhatsApp Alert
    twilio_client = Client(st.secrets["TWILIO_SID"], st.secrets["TWILIO_AUTH_TOKEN"])
    twilio_client.messages.create(body=f"Agent Update: {report[:50]}", from_='whatsapp:+14155238886', to='whatsapp:+923016372254')
    
    # 2. Gmail Alert (Aapka Gmail)
    msg = EmailMessage()
    msg.set_content(report)
    msg['Subject'] = "AutoBiz Autonomous Deal Report"
    msg['From'] = "shahzebbhutta813@gmail.com"
    msg['To'] = "shahzebbhutta813@gmail.com"
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("shahzebbhutta813@gmail.com", st.secrets["GMAIL_APP_PASSWORD"])
        smtp.send_message(msg)
    
    st.success("Report sent to your WhatsApp and Gmail!")
