import streamlit as st
import pandas as pd

# Create a DataFrame to store notes
notes_df = pd.DataFrame(columns=["User", "Note"])

# Streamlit app title
st.title("Simple Note Taking App")

# User login
username = st.text_input("Enter your username:")
if not username:
    st.warning("Please enter a username.")
    st.stop()

# Sidebar for user options
st.sidebar.header("Options")
if st.sidebar.button("Add Note"):
    note_text = st.text_area("Enter your note:")
    if note_text:
        notes_df = notes_df.append({"User": username, "Note": note_text}, ignore_index=True)
        st.success("Note added successfully!")

# Display user's notes
user_notes = notes_df[notes_df["User"] == username]["Note"]
if not user_notes.empty:
    st.header("Your Notes:")
    for i, note in enumerate(user_notes, start=1):
        st.write(f"{i}. {note}")
else:
    st.warning("You haven't added any notes yet.")



