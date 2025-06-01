import streamlit as st
import openai
import os

# Set up OpenAI key (from Streamlit Secrets or environment)
openai.api_key = os.getenv("OPENAI_API_KEY", st.secrets["OPENAI_API_KEY"])

st.title("💰 Website Pricing Assistant")

st.write("Answer a few quick questions and get an estimated website project cost.")

# --- Questions ---
pages = st.selectbox("How many pages do you need?", ["1–5", "6–10", "10+"])
ecommerce = st.radio("Do you need e-commerce?", ["Yes", "No"])
branding = st.radio("Do you need branding / logo design?", ["Yes", "No"])
content = st.radio("Do you need help with content writing?", ["Yes", "No"])

# --- Calculate Price ---
base_price = 1000
page_price = {"1–5": 0, "6–10": 500, "10+": 1000}
ecom_price = 1200 if ecommerce == "Yes" else 0
branding_price = 600 if branding == "Yes" else 0
content_price = 300 if content == "Yes" else 0

total = base_price + page_price[pages] + ecom_price + branding_price + content_price

# --- Show Results ---
if st.button("Calculate My Price"):
    st.success(f"🎯 Your estimated total: **${total}**")

    # Optional GPT summary
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful website consultant."},
            {"role": "user", "content": f"My total is ${total}. I chose: {pages} pages, e-commerce: {ecommerce}, branding: {branding}, content help: {content}."}
        ]
    )
    st.markdown("### 🤖 AI Assistant Says:")
    st.write(response["choices"][0]["message"]["content"])
