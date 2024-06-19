# Write a Python program to find out the net number of toy cars a child has after receiving them in multiple sets and giving some away.

# Start by asking for the child’s name and store it in a variable called name.
# Ask how many sets of toy cars they received, and store this value in a variable called sets_received (as an integer).
# Ask how many toy cars are in each set, and store this value in a variable called cars_per_set (as an integer).
# Calculate the total number of toy cars they have by multiplying sets_received and cars_per_set.
# Ask how many additional individual toy cars they received as gifts and store it in a variable called gift_cars (as an integer).
# Add gift_cars to the total number of toy cars calculated in step 4.
# Ask how many toy cars they gave away and store it in a variable called gave_away_cars (as an integer).
# Subtract gave_away_cars from the total number of toy cars to get the net number of cars.
# Store the net number of cars in a variable called net_cars.
# Print a message that includes the child’s name and the net number of toy cars in a friendly sentence, like this:
# “Hi [name]! You have a net total of [net_cars] toy cars after accounting for the ones you gave away.”
import streamlit as st
name=st.text_input('please enter your name')
sets_received=st.number_input('please enter how many cars received')
cars_per_set=st.number_input('how many toy cars are in each set')
total_cars=sets_received*cars_per_set
gift_cars=st.number_input('how many cars were received as gift')
overall_total_cars=gift_cars+total_cars
gave_away_cars=st.number_input('how many toy cars were given away')
net_number=total_cars-gave_away_cars
net_cars=net_number
st.write("hi",name,'you have a net total of',net_cars,'toy cars after accounting for the ones you gave away')


