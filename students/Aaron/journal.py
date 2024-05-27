# A journal app that a user can create, view, update notes

import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Select Option',['Create Note', 'View Note', 'Update Note'])

readnotes = pd.read_csv('notes.csv')


if menu == 'Create Note':
    head1,head2,head3 = st.columns(3)
    with head2:
        st.header(":blue[create notes]")

    title1,title2 = st.columns(2)
    with title1:
        notetitle = st.text_input("Enter the title for your new note")
    with title2:
        notedate = st.date_input("Select the note date") 

    notecontent = st.text_area("Enter your note content",height=250)
    
# Title,Date,Content
    if st.button(':blue[Save Note]'):
        if notetitle and notecontent:
            notedict = {'Title':[notetitle],'Date':[notedate],'Content':[notecontent]}
            notetable = pd.DataFrame(notedict)
            notejoin = pd.concat([readnotes,notetable],ignore_index=True)
            notejoin.to_csv('notes.csv',index=False)
            save1,save2= st.columns(2)
            with save1:
                st.success("Note Saved Successfully!")


#---------------------------VIEW NOTES------------------------------------------

if menu == 'View Note':
    head1,head2,head3 = st.columns(3)
    with head2:
        st.header(":blue[view notes]")

    read_titles = readnotes['Title'].to_list()

    selected_title = st.selectbox("Select note to view",read_titles)

    filter_title = readnotes[readnotes['Title'] == selected_title]
    # st.write(filter_title)
    filter_content = filter_title['Content'].iloc[0]
    filter_date = filter_title['Date'].iloc[0]

    st.write("")
    st.write("")
    date1,date2 = st.columns(2)
    with date1:
        st.subheader(":blue[**Selected note content**]")
    with date2:
        st.subheader(filter_date)

    st.divider()
    st.write("")
    st.write(filter_content)
