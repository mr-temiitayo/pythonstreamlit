import streamlit as st
import pandas as pd #for tables and viz
import numpy as np #for computations and arrays
import plotly.express as px #for data visualizations, including charts, graphs, and dashboards.


def code():
    st.title("Plotting In Streamlit With Plotly")
    df = pd.read_csv(r"C:/Users/USER/Desktop\streamlipython/pythonstreamlit/employees_database.csv")
    st.dataframe(df)

    piechart = px.pie(df,values='Salary',names='Name',title='Pie Chart Of Salaries')
    st.plotly_chart(piechart)

    barchart = px.bar(df,x='Name',y='Salary')
    st.plotly_chart(barchart)
code()
