import streamlit as st
import pandas as pd

# Sample DataFrame
data = {'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# Convert the DataFrame to an HTML table and remove the index column
df_html = df.to_html(index=False)

# Display the HTML table using Streamlit
st.write(df_html, unsafe_allow_html=True)
