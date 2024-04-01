import streamlit as st

try:
    number1 = st.text_input("Enter first number")
    number2 = st.text_input("Enter second number")


    if st.button("Add"):
        addition = int(number1) + int(number2)
        st.write("The addition is",addition)

    if st.button("Division"):
        division = int(number1) / int(number2)
        st.write("The division is",division)

except ZeroDivisionError:
    st.write("You cannot divide by zero")
except:
    st.write("Please enter only numbers")