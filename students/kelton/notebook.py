#create a notbook/journal to keep your information, 
#you can save them, view and still edit them
#use pandas for this project

import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Select Action',['Create Note','View Note','Update Note'])

readcsv = pd.read_csv('notes.csv')

if menu == 'Create Note':
    st.header(":orange[Create A New Note]")

    col1,col2 = st.columns(2)

    with col1:

        notetitle = st.text_input("Enter the title for your new note")

    with col2:
        notedate = st.date_input('Select note date')

    notecontent = st.text_area("Enter your new note",height=200)

    if st.button('Save Note'):
        notedict = {'Title':[notetitle],'Date':[notedate],'Content':[notecontent]}
        notedf = pd.DataFrame(notedict)
        combinednotes = pd.concat([readcsv,notedf],ignore_index=True)
        combinednotes.to_csv('notes.csv',index=False)
        st.success("Note Saved Sucessfully!")


if menu == 'View Note':
    # st.header(":orange[View Your Notes]")
    notetitles = readcsv['Title'].to_list()
    # st.write(notetitles)
    select_notetitle = st.selectbox('Select a note',notetitles)

    filtertitle = readcsv[readcsv['Title'] == select_notetitle]
    # st.write(filtertitle)
    content = filtertitle['Content'].iloc[0]
    st.write(f':orange[Selected Note Content:]')
    st.write(content)

if menu == 'Update Note':
    # st.header(":orange[View Your Notes]")
    notetitles = readcsv['Title'].to_list()
    # st.write(notetitles)
    select_notetitle = st.selectbox('Select a note',notetitles)

    filtertitle = readcsv[readcsv['Title'] == select_notetitle]
    # st.write(filtertitle)
    content = filtertitle['Content'].iloc[0]

    updatenote = st.text_area("Edit the selected note",content,height=200)
    #to overwrite a content,item. we use loc
    if st.button('Save Updated Note'):
        readcsv.loc[readcsv['Title'] == select_notetitle, 'Content'] = updatenote
        readcsv.to_csv('notes.csv',index=False)
        st.success('Note Updated Successfully!')