import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="RO_MIND AI", page_icon="🤖")
genai.configure(api_key="AIzaSyDXJr5jU1WQjCg3Nb30sXsZjiQU3l0OD8c")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 RO_MIND AI")
st.write("أهلاً بيكي يا دكتورة.. اسألي RO_MIND في أي حاجة!")

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
        response = model.generate_content(f"أنت RO_MIND، مساعد مصري مرح: {prompt}")
        st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

