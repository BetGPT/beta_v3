import streamlit as st
import chat
from context_manager import get_conversation_context

st.set_page_config(page_title="BetGPT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("<style>body{background-color:#f5f5f5;}</style>", unsafe_allow_html=True)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = get_conversation_context()

def update_chat_display(chat_container):
    chat_container.empty()
    display_messages = [message for message in st.session_state.conversation_history if message["role"] != "system"]

    for message in display_messages:
        if message["role"] == "user":
            chat_container.write(f'<div style="text-align:right;margin-bottom:5px;"><span style="display:inline-block;background-color:#00bfff;border-radius:10px;padding:5px 10px;color:#fff;">You: {message["content"]}</span></div>', unsafe_allow_html=True)
        else:
            chat_container.write(f'<div style="text-align:left;margin-bottom:5px;"><span style="display:inline-block;background-color:#ededed;border-radius:10px;padding:5px 10px;color:#000;">Assistant: {message["content"]}</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.title("BetGPT")
    st.write("Ask about today's NBA games.")
    
    chat_container = st.empty()
    update_chat_display(chat_container)
    
    user_input = st.text_input("Type your message here...", value=st.session_state.get("user_input", ""), key="user_input")
    send_button = st.button("Send")

    if send_button or (user_input and (st.session_state.get("last_message") != user_input)):
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        response = chat.chatgpt_completion(st.session_state.conversation_history)
        st.session_state.conversation_history.append({"role": "assistant", "content": response})
        st.session_state["last_message"] = user_input
        update_chat_display(chat_container)
        st.session_state["user_input"] = ""  # Clear input field
