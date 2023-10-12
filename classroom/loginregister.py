import streamlit as st
import pandas as pd
import os

# Initialize a CSV file to store user data
user_data_file = "user_data.csv"

# Load user data from the CSV file
user_df = pd.read_csv(user_data_file)

# Streamlit app title
st.title("User Registration and Login")

# Page selection in the sidebar (registration, login, or view users)
page = st.sidebar.radio("Select a page:", ["Register", "Login", "View Users"])

if page == "Register":
    st.sidebar.header("User Registration")

    username = st.sidebar.text_input("Username:")
    password = st.sidebar.text_input("Password:", type="password")


    if st.sidebar.button("Register"):
        if username and password:
            # Store user data in the CSV file
            new_user = pd.DataFrame({"Username": [username], "Password": [password]})
            user_df = pd.concat([user_df, new_user], ignore_index=True)
            user_df.to_csv(user_data_file, index=False)
            st.sidebar.success("Registration successful. You can now log in.")
        else:
            st.sidebar.error("Please enter a username and password.")

elif page == "Login":
    st.sidebar.header("User Login")

    username = st.sidebar.text_input("Username:")
    password = st.sidebar.text_input("Password:", type="password")

    if st.sidebar.button("Login"):
        user_exists = (user_df["Username"].str.lower() == username.lower()) & (user_df["Password"] == password)
        if user_exists.any():
            st.sidebar.success("Login successful. You have access.")

            # Show a notepad after successful login
            st.title("You are now logged in")

        else:
            st.sidebar.error("Login failed. Please check your username and password.")

elif page == "View Users":
    if not user_df.empty:
        st.dataframe(user_df, use_container_width=True)
    else:
        st.sidebar.info("No users registered yet.")
