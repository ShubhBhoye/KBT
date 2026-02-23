import streamlit as st

st.title("Basic Calculator App")

Number1 =st.number_input("Enter first number",format="%f")
Number2 =st.number_input("Enter second number",format="%f")

operation = st.selectbox("Select operation",["Add","Subtract","Multiply","Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("Result:", Number1 + Number2)
    elif operation == "Subtract":
        st.write("Result:", Number1 - Number2)
    elif operation == "Multiply":
        st.write("Result:", Number1 * Number2)
    elif operation == "Divide":
        if Number2 != 0:
            st.write("Result:", Number1 / Number2)
        else:
            st.write("Cannot Divide by zero")