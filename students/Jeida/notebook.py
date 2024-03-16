#create a notbook/journal to keep your information, you can save them, view and still edit them
#use pandas for this project

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox("Select Action", ['Create Note','View Notes','Update Note'])

notes = pd.read_csv('notes.csv')

if menu == 'Create Note':
    body1,body2,body3 = st.columns([0.2,4,0.2])

    with body2:
        with st.form('New form',clear_on_submit=True):
            st.header(':orange[Create A New Note]')

            note1,note2 = st.columns(2)

            with note1:
                notetitle = st.text_input("Enter the title for your new note")

            with note2:
                notedate = st.date_input('Select note date')

            notecontent = st.text_area("Enter your new note:",height=200)

            save1,save2 = st.columns(2)
            with save1:
                if st.form_submit_button('Save Note'):
                    if notetitle and notecontent:
                        newnotedict = {'Title':[notetitle],'Date':[notedate],'Note Content':[notecontent]} #Title,Date,Note Content
                        newnotedf = pd.DataFrame(newnotedict)
                        combinednotes = pd.concat([notes,newnotedf])
                        combinednotes.to_csv('notes.csv')
                        st.success("Note Saved Successfully!")

elif notes == 'View Notes':
    pass