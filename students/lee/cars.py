import streamlit as st
import pandas as pd


carlink = pd.read_csv('cars.csv')
st.table(carlink)

st.header("Car Dealer Shop")
st.subheader("Enter the new car specifications")




carname = st.text_input("Enter car name")




caryear = st.text_input('Enter the year of the car')




carbrand = st.text_input("Enter the brand of the car")




transmission = st.radio("Enter car transmision",['Automatic','Manual'])




if st.button("Add New Car Specifications"):
   car_dict = {'Car Name':[carname],'Car Year':[caryear],'Car Brand':[carbrand],'Transmission':[transmission]}

   st.write(car_dict)

   car_dataframe = pd.DataFrame(car_dict)
   car_database = pd.concat([carlink,car_dataframe],ignore_index=True)
   car_database.to_csv('cars.csv',index=False)
