# Write a Python program to find out the net number of toy cars a child has after receiving them on multiple occasions and giving some away.

# Start by asking for the child’s name and store it in a variable called name.
# Ask how many toy cars they received on the first occasion and store it in a variable called occasion1_cars (as an integer).
# Ask how many toy cars they received on the second occasion and store it in a variable called occasion2_cars (as an integer).
# Calculate the total number of toy cars they have by multiplying occasion1_cars and occasion2_cars.
# Ask how many toy cars they lost or gave away and store it in a variable called lost_cars (as an integer).
# Subtract the lost_cars from the total number of toy cars to get the net number of cars.
# Store the net number of cars in a variable called net_cars.
# Print a message that includes the child’s name and the net number of toy cars in a friendly sentence, like this:
# “Hi [name]! You have a net total of [net_cars] toy cars after accounting for the ones you lost or gave away.”
import streamlit as st
name=st.text_input('please enter your name ')
occasion1_cars=st.number_input('please enter the number of cars you received on the first occassion')
occasion2_cars=st.number_input('please enter the number of cars you received on the second occasion')
total_cars=occasion1_cars+occasion2_cars
lost_cars=st.number_input('please enter the number of lost cars')
net_number=total_cars-lost_cars
net_cars=net_number
st.write("hi",name,'you have a net total of',net_cars,'toy after accounting for the ones you lost or gave away')





