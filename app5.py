import streamlit as st

st.markdown("""
<style>
    .stButton > button {
        background-color:blue;
        color: white;
        border-radius: 30%;
        }
        </style>






""",    unsafe_allow_html=True)





st.title("Welcome to Basic Streamlit App")

name = st.text_input("Enter your name")
Age = st.slider("Enter your Age",1 ,100)
city = st.selectbox("select your city,",["Nsk","Mumbai","Delhi","Pune"])

if st.button("Show Details"):
    st.write("Age:", Age)
    st.write("City:", city)
    st.write("Name:", name)