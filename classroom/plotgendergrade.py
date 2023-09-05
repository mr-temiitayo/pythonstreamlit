import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv')

st.dataframe(df, use_container_width=True)

# Create a bar chart for gender vs. math scores
gender_math_scores = df[['Gender', 'Maths']].groupby('Gender').mean().reset_index()

#LINE CHART---------------

# Display the line chart with the selected columns

chart1,chart2 = st.columns(2)


with chart1:
    # Create a vertical bar chart using Plotly Express #title='Math Scores by Gender',
    figbar = px.bar(gender_math_scores, x='Gender', y='Maths', 
                    orientation='v',
                    color_discrete_map={'Male': 'red', 'Female': 'blue'})

    # Display the vertical bar chart in Streamlit
    st.plotly_chart(figbar)

with chart2:
    #------PIECHART -----------------
    figpie = px.pie(gender_math_scores,
                    names='Gender', values='Maths',
                    color_discrete_sequence=['red', 'blue'])

    # Display the pie chart in Streamlit
    st.plotly_chart(figpie)