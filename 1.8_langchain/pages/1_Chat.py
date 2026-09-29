import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from core.chains import get_chat_chain


st.set_page_config(page_title="Chat", page_icon="🧑‍🎓")


if "history" not in st.session_state:
    # empty list is going to store the ai message and the human message
    st.session_state.history = []


chain=get_chat_chain()
# (AIMessage("message"), HumanMessage("message"))

for msg in st.session_state.history:
    role="user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)


# what if there is an input
person = "You are a helfuland friendly AI assistant."
user_input=st.chat_input("Ask your question...")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        full_reply=st.write_stream(
            chain.stream({"input":user_input, "history": st.session_state.history[:-1],"persona": persona})
    )        
    st.session_state.history.append(AIMessage(content=full_reply))



