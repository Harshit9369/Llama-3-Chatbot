from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="llama3")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = llm.invoke(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})