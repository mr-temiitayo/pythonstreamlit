import streamlit as st
import pandas as pd
import time

st.set_page_config(layout='wide')
st.title("Data Editor App")

timestamp = int(time.time())

st.write(timestamp)

col1,co2 = st.columns(2)

with col1:
    upload_csv = st.file_uploader('Upload CSV File',type=['csv'])



    
if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file,use_container_width=True)

    save1,save2,space = st.columns([1,1,4])
    message,space2 = st.columns(2)
    with save1:
        if st.button('Save on Original File'):
            edit_csv.to_csv(upload_csv.name,index=False)
            col3,col4 = st.columns([1,2])
            with message:
                st.success('Original CSV File Saved')


    with save2:
        if st.button('Save A Copy'):
            new_filename = (f'{upload_csv.name}_{timestamp}.csv')
            csv_copy = edit_csv.to_csv(index=False)
            st.download_button(label='Download CSV Copy',file_name = new_filename, data=csv_copy,mime='text/csv')
            with message:
                st.success('Copy CSV File Saved')

#what if you want to edit and save a copy, not to overwrite the original data??
#homework: create your own file to practice with another database