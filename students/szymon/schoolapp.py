import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

countrylink = pd.read_csv('countries.csv')
st.title("private School application form")
left,right = st.columns(2)




#left
with left:
    FName = st.text_input("Enter Parent full name",placeholder="First Name")
    AgeVar = [i for i in range(1,19)]
    Age = st.select_slider("Choose age", AgeVar)
    CFName = st.text_input("Enter Child Name",placeholder="first Name")
    Contact = st.text_input("Enter contact number:",placeholder="### ### ####")






#right
with right:
    Lname = st.text_input("last name",placeholder="Last Name", label_visibility= "hidden")
    Gender = st.radio("Enter gender",["Male","Female"])
    CLName = st.text_input("Enter child name",label_visibility="hidden",placeholder="last name")
    Gmail = st.text_input("Enter G mail")


school = st.text_input("Enter Child school:")


#Address


N1 , N2 , N3,N4 = st.columns(4)


with N1:
    street = st.text_input("Enter street:")
   
with N2:
    continent = st.selectbox("Choose continent",["Asia","Africa","North America","South America","Europ","Astralia"])
    


with N3:
    country = st.selectbox("Choose country",countrylink['Country'].tolist()) #show me country column as a list

with N4:
    Zip = st.text_input("Enter Zip code:")

