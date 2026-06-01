import streamlit as st
import openai

# API Key setup (Aap ise environment variables se secure karein)
st.set_page_config(page_title="AutoBiz AI - Global Scout", layout="wide")

st.title("🚀 AutoBiz AI: Global Lead Finder")
st.subheader("Jewelry Wholesale Business Automation Tool")

# Sidebar for configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Main Interface
product_name = st.text_input("Product ka naam likhein (e.g., 22k Gold Engagement Rings):")
target_country = st.selectbox("Target Market:", ["UK", "UAE", "USA", "Canada", "Germany"])

if st.button("Generate Leads & Pitch"):
    if not api_key:
        st.error("Please enter your API Key.")
    elif not product_name:
        st.warning("Please enter a product name.")
    else:
        try:
            client = openai.OpenAI(api_key=api_key)
            
            with st.spinner('AI data analyze kar raha hai...'):
                # AI Prompt to find leads and write a pitch
                prompt = f"""
                Act as a professional B2B Jewelry Sales Expert. 
                Identify the types of retailers in {target_country} who would be interested in {product_name}.
                1. Provide a list of 3 types of businesses to target.
                2. Write a highly professional, short cold-email pitch to send to these leads.
                3. Suggest 3 key selling points that appeal to {target_country} market.
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "You are a world-class business growth consultant."},
                              {"role": "user", "content": prompt}]
                )
                
                st.success("Analysis Complete!")
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.write("Developed by Shahzeb Bhutta | AutoBiz AI Project")
