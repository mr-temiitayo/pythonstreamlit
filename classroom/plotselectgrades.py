import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv')

st.dataframe(df, use_container_width=True)

# Create a list of the gender columns you want to display
gender_columns = ['Male', 'Female']

# Use the multiselect widget to select the gender columns
gender_choices = st.selectbox('Choose genders', gender_columns) #, default=['Male']

# Filter the DataFrame to include only the selected columns
gender_df = df[gender_choices]

st.line_chart(gender_df)