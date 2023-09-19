import streamlit as st
import time

if st.checkbox('Buy Chicken: $35'):
    # Display a success message
    chickensuccess = st.success("Added chicken") #show success

    # Wait for 3 seconds
    time.sleep(3) # wait for 3 secs

    # Clear the success message
    chickensuccess.empty() #clear success
