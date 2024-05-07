# create a simple page for a school. 
# Show on the page the Elementary fee is 300,000 naira and the college fee is 500,000 naira

# Ask the parent name
# Ask how many kids the parent have for elementary and ask if how many they have for college

# Then show them their total tuition fee


import streamlit as st

elementaryfee = 300_000
collegefee = 500_000

st.write("Elementary fee is",elementaryfee,'and College fee is',collegefee)
parentname = st.text_input("Enter parent name")

kids1,kids2 = st.columns(2)
with kids1:
    elementarykids = st.number_input("How many kids in Elementary?",0)
with kids2:
    collegekids = st.number_input('How many kids in College?',0)

totalelementary = elementarykids * elementaryfee
totalcollege = collegekids * collegefee
totalfees = totalelementary + totalcollege

if st.button("Check School Fees"):
    st.write("Elementary fee for",elementarykids,'students is',totalelementary,'while College fee for',collegekids,'students is',totalcollege)
    st.write("Your total school fees is",totalfees)