# TECHIE SMART TEST 
# create an app to:
# upload any csv file  DONE
# use a multiselectbox to get and display subjects users want to choose to plot (use st.multiselect) DONE
# use a radio  button to choose if to view the chart as a barchart or piechart #CLASSWORK


import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')


st.title("Upload Data to Plot Chart")

upload1,upload2 = st.columns(2)

with upload1:
    upload_csv = st.file_uploader('Upload CSV File', type = 'csv')

if upload_csv:
    csv_file = pd.read_csv(upload_csv)

    with st.expander("Open to View Database"):
        st.table(csv_file)

    csv_columns = csv_file.columns.tolist()

    choosesubjects = st.multiselect('Choose Subjects to Plot',csv_columns)

    subjects_ave = csv_file[choosesubjects].mean().reset_index()
    rename_subjects = subjects_ave.rename(columns = {'index':'Subject', 0:'Average'})

    barchart = px.bar(rename_subjects, x='Subject', y='Average')
    st.plotly_chart(barchart)

    piechart = px.pie(rename_subjects, names='Subject', values='Average')
    st.plotly_chart(piechart)