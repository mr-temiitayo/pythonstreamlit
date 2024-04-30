import streamlit as st
import pandas as pd


find = st.text_input("Enter User ID to delete")
def delete():
    df = pd.read_csv('employee.csv')
    df = df.drop(df[df['User ID'] == find].index)
    df.to_csv('employee.csv', index=False)



if st.button('Delete User',on_click=delete):
        st.success("User deleted successfully.")


# Display the CSV file
df = pd.read_csv('employee.csv')
st.write(df)