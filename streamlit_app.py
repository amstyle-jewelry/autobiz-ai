import openai
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# --- REAL API CONFIGURATION (Yahan apni actual Keys dalni hain) ---
openai.api_key = "YOUR_OPENAI_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

def negotiate_with_buyer(buyer_email, product_details):
    # GPT-4o real negotiation karega
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Negotiate this: {product_details}"}]
    )
    return response.choices[0].message.content

def send_real_whatsapp_alert(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_='whatsapp:+14155238886', # Twilio ka number
        to='whatsapp:+923016372254'    # Aapka number
    )

def send_real_email(buyer_email, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = "Official Business Deal"
    msg['From'] = "shahzebbhutta813@gmail.com"
    msg['To'] = buyer_email
    
    # Gmail SMTP Server connect karein
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("shahzebbhutta813@gmail.com", "YOUR_APP_PASSWORD")
        smtp.send_message(msg)
        
