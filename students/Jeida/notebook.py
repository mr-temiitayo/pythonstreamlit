#create a notbook/journal to keep your information, you can save them, view and still edit them
#use pandas for this project

import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
space = st.write('')
menu = st.sidebar.selectbox("Select Action", ['Create Note','View Notes','Update Note'])

notes = pd.read_csv('notes.csv')

if menu == 'Create Note':
    body1,body2,body3 = st.columns([0.2,4,0.2])

    with body2:
        with st.form('New form',clear_on_submit=True):
            st.header(':green[Create A New Note]')

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
                        combinednotes = pd.concat([notes,newnotedf],ignore_index=True)
                        combinednotes.to_csv('notes.csv',index=False)
                        st.success("Note Saved Successfully!")

elif menu == 'View Notes':
    st.header(':green[View Your Notes]')
    notes_titles = notes['Title'].to_list()
    title1, title2 = st.columns([0.4,0.2])
    with title1:
        selected_title = st.selectbox("Select a note to view",notes_titles)
        st.write('')
        st.write('')


    filter_title = notes[notes['Title'] == selected_title]
    # st.table(filter_title)
    content = filter_title['Note Content'].iloc[0]
    
    st.subheader(f':orange[Selected Note Content:]')
    st.write(content)


elif menu == 'Update Note':
    st.header(':green[Update Your Notes]')
    notes_titles = notes['Title'].to_list()
    title1, title2 = st.columns([0.4,0.2])
    with title1:
        selected_title = st.selectbox("Select a note to update",notes_titles)
        st.write('')
        st.write('')
    filter_title = notes[notes['Title'] == selected_title]
    # st.table(filter_title)
    content = filter_title['Note Content'].iloc[0]
    updated_note = st.text_area("Edit the selected note:",content,350)
    