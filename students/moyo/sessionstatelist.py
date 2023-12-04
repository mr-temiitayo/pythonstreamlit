# A boy went to the supermarket to get a list of items, 
# use ONLY one text box to ask the user for the 5 items he wants to get each time 
# Put each item entered/submitted in the customer’s list
# Display all items in the customer’s list

#ss is to help us store our variables so as to not get refreshed by any widget activity
import streamlit as st

st.title("Moyo's MegaSuperStore [MMSS]")

if 'userlist' not in st.session_state:
    st.session_state.userlist = []


item = st.text_input('Enter items to purchase')

if st.button("Submit"):
    st.session_state.userlist.append(item)
    st.write("All your items are:",st.session_state.userlist)


