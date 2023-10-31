import streamlit as st
import pandas as pd

dict = {'a': ['first'], 'b':[2]}

st.write(dict)

df = pd.DataFrame(dict)
st.dataframe(df)