import streamlit as st
import pandas as pd
import time
import os

timestamp = int(time.time())


st.title('Data Editor App | New CSV')

data_file = st.file_uploader("Upload CSV File", type=['csv'])
if data_file is not None:
    df = pd.read_csv(data_file)

    with st.form('Editor form'):
        edited_df = st.data_editor(df)
        save = st.form_submit_button('Save Data')

    if save:
        new_filename = f'{data_file.name}_{timestamp}.csv'
        final_df = edited_df.to_csv(index=False)

        st.download_button(label='Download data as CSV',data=final_df,file_name=new_filename,mime='text/csv')



st.title('Data Editor App | Overwrite CSV')

data2_file = st.file_uploader("Upload CSV File", type=['csv'],key="data2")
if data2_file is not None:
    df2 = pd.read_csv(data2_file)

    with st.form('Editor form2'):
        edited2_df = st.data_editor(df2)
        save2 = st.form_submit_button('Save Data')

    if save2:
        new_filename2 = f'{data2_file.name}_{timestamp}.csv'
        edited2_df.to_csv(new_filename2, index=False)
        os.remove(data2_file.name)
        os.rename(new_filename2, data2_file.name)
        os.remove(data2_file.name)
        st.success("Data saved successfully to the original file.")
