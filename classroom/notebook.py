#CREATE DOWNLOAD TITLENOTE FOR ONE AND FOR ALLL

import streamlit as st
import pandas as pd

# Streamlit sidebar for actions
action = st.sidebar.radio("Select Action", ["Create Note", "View Notes", "Update Note"])

# Initialize the notes DataFrame
try:
    notes = pd.read_csv("notes.csv")
except FileNotFoundError:
    notes = pd.DataFrame(columns=["Note Title", "Note"])

if action == "Create Note":
    st.header("**Create a New Note**")

    # Text area to input a new note title
    new_note_title = st.text_input("Enter the title for your new note:")

    # Text area to input a new note
    new_note = st.text_area("Enter your new note:")

    if st.button("Save Note"):
        if new_note_title and new_note:  # Check if a title and note content are provided
            # Append the new note with its title to the DataFrame
            new_note_df = pd.DataFrame({"Note Title": [new_note_title], "Note": [new_note]})
            notes = pd.concat([notes, new_note_df], ignore_index=True)

            # Save the updated notes to the CSV file
            notes.to_csv("notes.csv", index=False)

            st.success("Note saved successfully!")
        else:
            st.error("Please provide a title and content for your note.")

elif action == "View Notes":
    st.subheader("**View Notes**")

    if not notes.empty:
        # Display all note titles in a list
        note_titles = notes["Note Title"].values
        selected_note_title = st.selectbox("Select a note to view:",note_titles)

        #----------------------
        filter_content = notes[notes['Note Title'] == selected_note_title]
        content = filter_content['Note'].iloc[0]


        #--------------------------
        # selected_note_content = notes.loc[notes["Note Title"] == selected_note_title, "Note"]
        #loc means locate the row that match the condition
        st.write(f"**Selected Note Title: {selected_note_title}**")
        st.write('')
        # st.write('')
        st.write(f"**Selected Note Content:**")
        st.write(f'**{content}**')
    else:
        st.warning("No notes available. Create some notes first.")

elif action == "Update Note":
    st.subheader("**Update Note**")

    if not notes.empty:
        # Display all note titles in a list
        note_titles = notes["Note Title"].values
        selected_note_title = st.selectbox("Select a note to update:", note_titles)

        #----------------------
        filter_content = notes[notes['Note Title'] == selected_note_title]
        content = filter_content['Note'].iloc[0]
        updated_note = st.text_area("Edit the selected note:",content)

        #--------------------------
        # updated_note = st.text_area("Edit the selected note:",notes.loc[notes["Note Title"] == selected_note_title, "Note"])

        if st.button("Save Updated Note"):
            # to update a paticular cell in your dataframe
            notes.loc[notes["Note Title"] == selected_note_title, "Note"] = updated_note

            # Save the updated notes to the CSV file
            notes.to_csv("notes.csv", index=False)

            st.success("Note updated successfully!")
    else:
        st.warning("No notes available. Create some notes first.")
