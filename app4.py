import streamlit as st

st.title("Basic Chatbot App")

Question = st.text_input("Ask a question")

if st.button("Get Answer"):
    st.write("you asked:", Question)
    st.write("Answer: This is a basic chatbot app built with Streamlit.")