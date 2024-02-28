import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide')
st.title('Student Scores Database')

df = pd.read_csv('codingscores.csv')

st.table(df.head(5))

sub = ['Python','Sql','ML','Tableau','Excel']
sub_score = df[sub].mean().reset_index()
sub_new = sub_score.rename(columns={'index':'Subjects', 0:'Average'})

barchart = px.bar(sub_new, x = 'Subjects', y ='Average')
st.plotly_chart(barchart)
