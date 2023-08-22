import streamlit as st

#Text input
fname = st.text_input("Enter Firstname: ")
st.title(fname)

#Text Area
message = st.text_area("Enter Message", height=100)
st.write(message)

#Numbers
number = st.number_input("Enter Number", 1,25,5) #mim, max, increment

#Date Input
myappnt = st.date_input("Appointment:") #you can specify the min, max date input

#Time input
mytime = st.time_input("Appointment:") #you can specify the min, max time input


#Text input hide password
password = st.text_input("Enter Password", type='password')

#Color Picker
color = st.color_picker("Select Color")

