import streamlit as st
import google.generativeai as genai

# 1. إعداد الصفحة
st.set_page_config(page_title="RO_MIND AI", page_icon="🤖")

# 2. الربط مع جوجل
genai.configure(api_key="AIzaSyDXJr5jU1WQjCg3Nb30sXsZjiQU3l0OD8c")

# استخدمت الاسم ده لأنه الأضمن وبيشتغل مع كل النسخ
model = genai.GenerativeModel('gemini-pro') 

st.title("🤖 RO_MIND AI")
st.write("أهلاً بيكي يا دكتورة.. RO_MIND جاهز لمساعدتك!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("سؤالك إيه؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            # تعليمات الشخصية
            full_prompt = f"أنت RO_MIND، مدرس مصري مرح. رد بالعامية المصرية: {prompt}"
            response = model.generate_content(full_prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"حصلت مشكلة في الرد: {e}")
