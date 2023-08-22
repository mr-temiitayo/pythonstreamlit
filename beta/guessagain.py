import streamlit as st
import random

values_to_reset = {
    'cpunumber': random.randint(0, 10),
    'guess': 0
}

def reset():
 #this loop will get values from values_to_reset dict and assign to sessionstate keys
        for var, value in values_to_reset.items(): #var =key, value = value in the dict
            st.session_state[var] = value #reset each sessionstate key to its value in values to reset values dict

def code():
    st.title("Guess The Number Game")

#this loop will reset values in values_to_reset dict
    for value in values_to_reset.keys(): #loop through the dictionary for variable values
        if value not in st.session_state: # if each value in dict key is not saved in sessionstate
            st.session_state[value] = values_to_reset[value] #assign the session state of each key you got from dict[value]

    # Get user's name through text input
    name = st.text_input("Enter your game name")
    guess = st.number_input("Guess my number from 1-10",0,10,value=st.session_state.guess)

    # Retrieve 'cpunumber' value and generate a random number
    cpunumber = st.session_state.cpunumber

    # Display computer's random number
    st.write("Computer random number is:", cpunumber)
    st.write(cpunumber)
    # Button to add 1 to the random number
    if st.button("Click To Guess"):
#        cpunumber += 1
#        st.session_state.cpunumber = cpunumber #to update changes
        if guess == cpunumber:
            st.success(f'{name} your guess is correct')
        
        else:
            st.error(f'Your guess is incorrect')

    # Button to reset the random number
    if st.button("Reset"):
        reset()


code()
