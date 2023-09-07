import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv')

st.dataframe(df, use_container_width=True)

st.title('Students Database Chart')

Xcolumns = ['Gender','ParentMaritalStatus'] 

Ycolumns = ['Maths','Reading','Writing']

st.write('')
chart1,chart2,chart3 = st.columns([1,1,2])
# Use the multiselect widget to select the Scores to draw
with chart1:
    selectedY = st.multiselect('**Select Grades To Plot**', Ycolumns) #, default=['Male']

with chart2:
    selectedX = st.radio('**Select Categories to plot**',Xcolumns,horizontal = True)

# Create a line chart
fig = px.bar(df, x=selectedX, y=selectedY, orientation='v',color = selectedX)

# Show the chart
st.plotly_chart(fig)