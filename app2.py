import streamlit as st

st.title("Welcome to Basic Streamlit App")

name = st.text_input("Enter your name")
Age = st.slider("Enter your Age",1 ,100)
city = st.selectbox("select your city,",["Nsk","Mumbai","Delhi","Pune"])

if st.button("Show Details"):
    st.write("Age:", Age)
    st.write("City:", city)
    st.write("Name:", name)