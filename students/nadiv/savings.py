import streamlit as st
import pandas as pd


st.subheader("Weekly Savings Calculator")


database = pd.read_csv('savings.csv')
st.dataframe(database,use_container_width=True)


date = st.date_input('Enter the first date of the week')


day1,day2= st.columns(2)
with day1:
   monday = st.number_input("how much money would you like to save for monday:",0,1000,step = 20)
   wednesday = st.number_input("how much money would you like to save for wednesday",0,1000,step = 20)
   friday = st.number_input("how much money would you like to save for friday:",0,1000,step = 20)
   sunday = st.number_input("how much money would you like to save for sunday",0,1000,step = 20)


with day2:
   tuesday = st.number_input("how much money would you like to save for tuesday:",0,1000,step = 20)
   thursday = st.number_input("how much money would you like to save for thursday:",0,1000,step = 20)
   saturday = st.number_input("how much money would you like to save for saturday",0,1000,step = 20)


total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
with day2:
   st.write("")
   st.write("")
   if st.button("Click to save"):
       savings_dict = {'Date':[date],'Monday':[monday],'Tuesday':[tuesday],'Wednesday':[wednesday],'Thursday':[thursday],'Friday':[friday],
               'Saturday':[saturday],'Sunday':[sunday],'Total':[total]}
      
       savings_database = pd.DataFrame(savings_dict)
       new_database = pd.concat([database,savings_database],ignore_index=True)
       new_database.to_csv('savings.csv',index=False)
       st.success(f"This week you have saved {total}")

