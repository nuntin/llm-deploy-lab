import streamlit as st
import requests

# -----------------------
# Logo
# -----------------------
st.image("https://i.imgur.com/OG5xKXW.png", width=100)
st.title("LLM Web Interface 🌍")

# -----------------------
# Language Selection
# -----------------------
lang = st.radio("🌐 Choose language", ["English", "ไทย"])

# -----------------------
# Input Prompt
# -----------------------
prompt = st.text_input("✍️ Enter your question:")

# -----------------------
# Translation (Thai ↔ English) using LibreTranslate API
# -----------------------
def translate(text, src, tgt):
    try:
        res = requests.post("https://libretranslate.de/translate", data={
            "q": text,
            "source": src,
            "target": tgt,
            "format": "text"
        })
        return res.json()["translatedText"]
    except:
        return text  # fallback if API fails

# -----------------------
# Submit Prompt and Get Result
# -----------------------
if st.button("🚀 Submit"):
    if lang == "ไทย":
        translated_prompt = translate(prompt, "th", "en")
    else:
        translated_prompt = prompt

    try:
        # Send prompt to FastAPI backend
        response = requests.post("http://llm-api:8000/generate", json={"prompt": translated_prompt})
        raw_output = response.json()["result"]  # use "result" as returned from FastAPI
    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
        raw_output = ""

    # Translate output back to Thai if needed
    if lang == "ไทย" and raw_output:
        final_output = translate(raw_output, "en", "th")
    else:
        final_output = raw_output

    st.markdown("### 🤖 Answer")
    st.write(final_output)
