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


# Calculate the mean values for the selected grades
mean_values = df.groupby(selectedX)[selectedY].mean().reset_index()

# Create a line chart
fig = px.bar(mean_values, x=selectedX, y=selectedY, orientation='v',color = selectedX)

# Customize the y-axis tick labels format (e.g., as integers)
# fig.update_yaxes(title_text='')

# Show the chart
st.plotly_chart(fig)

#fig= px.pie(df,values='Sum',names='lang)