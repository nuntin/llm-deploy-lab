import streamlit as st
import requests

# -----------------------
# โลโก้
# -----------------------
st.image("https://i.imgur.com/OG5xKXW.png", width=100)  # เปลี่ยน URL เป็นโลโก้มึงเองได้
st.title("LLM Web Interface 🌍")

# -----------------------
# ภาษา
# -----------------------
lang = st.radio("🌐 เลือกภาษา", ["English", "ไทย"])

# -----------------------
# ป้อนคำถาม
# -----------------------
prompt = st.text_input("✍️ ใส่คำถามของคุณ:")

# -----------------------
# Translate ก่อนส่ง (ใช้ LibreTranslate API demo)
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
        return text  # fallback

# -----------------------
# ส่งคำถาม และรับผลลัพธ์
# -----------------------
if st.button("🚀 ถามเลย"):
    if lang == "ไทย":
        translated_prompt = translate(prompt, "th", "en")
    else:
        translated_prompt = prompt

    # ส่ง prompt ไปยัง FastAPI
    try:
        response = requests.get("http://llm-api:8000/predict", params={"prompt": translated_prompt})
        raw_output = response.json()["response"]
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาด: {e}")
        raw_output = ""

    # แปลคำตอบกลับ (ถ้าเป็นภาษาไทย)
    if lang == "ไทย" and raw_output:
        final_output = translate(raw_output, "en", "th")
    else:
        final_output = raw_output

    st.markdown("### 🤖 คำตอบ")
    st.write(final_output)