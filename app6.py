import streamlit as st

st.markdown("""
<style>
    .stButton > button {
        background-color:blue;
        color: white;
        border-radius: 50%;
        }
        </style>






""",    unsafe_allow_html=True)





st.title("Basic Details App")

fname = st.text_input("Enter your First name")
lname = st.text_input("Enter your Last name")
Age = st.slider("Enter your Age",1 ,100)
city = st.selectbox("select your city,",["Nsk","Mumbai","Delhi","Pune"])
Year = st.date_input("Enter your Birth Year")
Education = st.radio("Select your Education",["High School","Bachelor's","Master's","PhD"])
Email = st.text_input("Enter your Email")
Phonenumber = st.text_input("Enter your Phone Number")




if st.button("Show Details"):
    st.write("Age:", Age)
    st.write("City:", city)
    st.write("Name:", fname)
    st.write("Last Name:", lname)
    st.write("Birth Year:", Year)
    st.write("Education:", Education)
    st.write("Email:", Email)
    st.write("Phone Number:", Phonenumber)
    