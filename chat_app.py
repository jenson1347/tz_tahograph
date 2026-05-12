import streamlit as st
from router.router import route
from main import process_message

st.set_page_config(
    page_title="AI Assistant",
    layout="wide"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

prompt = st.chat_input(
    "Введите сообщение"
)

if prompt:

    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        response = process_message(prompt)
        
        st.markdown(prompt)


    with st.chat_message("assistant"):

        try:
            assistant_message = response["message"]
        except:
            assistant_message = f"Задача выполнена, {response['result']['API_response']}"

        st.markdown(assistant_message)

        st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )