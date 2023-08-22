#Savings App
#Create a python program for daily savings for a user, add up all his savings from sunday to saturday


import streamlit as st


st.title("Daily savings")


"""


I will need your:


* Name


"""


Name = st.text_input("Enter your name")


Monady= st.number_input("How much do you want to save on Monday",value=0,step= 1,format="%d")


Tuesday= st.number_input("How much do you want to save on Tuesday",value=0,step= 1,format="%d")


Wednasday= st.number_input("How much do you want to save on Wednasday",value=0,step= 1,format="%d")


Thursday= st.number_input("How much do you want to save on Thursday",value=0,step= 1,format="%d")


Friday= st.number_input("How much do you want to save on Friday",value=0,step= 1,format="%d")


Saturday= st.number_input("How much do you want to save on Saturday",value=0,step= 1,format="%d")


Sunday= st.number_input("How much do you want to save on Sunday",value=0,step= 1,format="%d")


saved = Monady + Tuesday + Wednasday + Thursday + Friday + Saturday + Sunday


if st.button("Show How much i saved"):
 st.write("You have saved",saved,"Dollars")



