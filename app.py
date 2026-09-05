import streamlit as st
import os

st.set_page_config(page_title="المساعد القانوني", page_icon="️")
st.title("️ المساعد القانوني الذكي")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("️ مفتاح API غير موجود. يرجى إضافته في إعدادات التطبيق.")
    st.stop()

st.success("✅ التطبيق يعمل بنجاح!")
st.write("مرحباً بك في المساعد القانوني الذكي")

# صندوق إدخال بسيط
user_input = st.text_input("اكتب سؤالك القانوني هنا:")

if user_input:
    st.write(f"سؤالك: {user_input}")
    st.info("سيتم الرد عليك قريباً...")
