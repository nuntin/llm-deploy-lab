# web_ui.py
import streamlit as st
import requests

st.title("LLM Web Interface")

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    response = requests.get("http://localhost:8000/predict", params={"prompt": prompt})
    st.write(response.json()["response"])