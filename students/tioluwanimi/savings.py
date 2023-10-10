import streamlit as st
#Create a python program for daily savings for a user,
#add up all his savings from sunday to saturday
col1,col2,col3= st.columns(3)

with col1:
    sunday = st.number_input("Enter the amount you want to save this sunday" )
with col2:
    monday = st.number_input("Enter the amount you want to save this monday ")
with col3:
    tuesday = st.number_input("Enter the amount you want to save this tuesday ")
with col1:
    wednesday = st.number_input("Enter the amount you want to save this wednesday ")
with col2:
    thursday = st.number_input("Enter the amount you want to save this thursday ")
with col3:
    friday = st.number_input("Enter the amount you want to save this friday ")
with col1:
    saturday = st.number_input("Enter the amount you want to save this saturday ")

savings = (sunday + monday + tuesday + wednesday + thursday + friday + saturday)
with col2:
    st.write('')
    st.write('')
    st.write('')
    if st.button('Check the amount you saved'):
        with col3:
            st.write('')
            st.write('')
            st.write('')
            st.subheader(f"Savings: ${savings}")

