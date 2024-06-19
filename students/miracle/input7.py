import streamlit as st 
name=st.text_input('please enter your name')
gift_cars=st.number_input('please enter the number of gift cars')
bought_cars=st.number_input('please enter the number of bought cars')
gave_away_cars=st.number_input('please enter the number of gave away cars')
total_cars=gift_cars + bought_cars
net_number=gave_away_cars-total_cars
net_cars=st.number_input("please input net number of cars")
st.write("hi",name,'you have a net total of',net_cars,'toy cars after accounting for the ones you gave away')











