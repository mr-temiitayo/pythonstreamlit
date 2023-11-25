""""
-title
-image
-categories
Men's Fashion

Women's Fashion

Children's Fashion

(each category must havedifferent types of unique items and the prices 
like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)

Show the total bill
"""  
import streamlit as st
st.set_page_config(layout="wide")
total=0
st.title("Welcome to the fashion store")
st.image("https://cdn.pixabay.com/photo/2021/04/05/12/39/shop-6153302_1280.png")

st.subheader("We have")

st.title("Men fashion")
st.image("https://cdn.pixabay.com/photo/2017/11/02/14/27/model-2911332_1280.jpg")
mf1,mf2 = st.columns(2)

with mf1:
  if st.checkbox("T shirt: $40"):
     st.success("You bought a T shirt")
     total +=40
  if st.checkbox("Shirt: $35"):   
     st.success("You bought a Shirt")
     total +=35
  if st.checkbox("Jacket: $40"):
      st.success("You bought a Jacket")
      total += 40

with mf2:
   if st.checkbox("Sweater: $39"):  
      st.success("You bought a Sweater")
      total += 39
   if st.checkbox("Jeans: $25"):
      st.success("You bought Jeans") 
      total += 25
  
   if st.checkbox("Trousers: $25"):
      st.success("You bought Trousers")
      total += 25



st.title("Women fashion")
st.image("https://cdn.pixabay.com/photo/2016/10/15/05/02/girls-1741925_1280.jpg")
wmf1,wmf2 = st.columns(2)

with wmf1:
   if st.checkbox("Skirt: $24"):
      st.success("You bought a Skirt")
      total += 24
   
   if st.checkbox("Coat: $20"):
      st.success("You bought a Coat")
      total += 20

with wmf2:
   if st.checkbox("Dress: $55"):
      st.success("You bought a Dress")
      total += 55

   if st.checkbox("Shorts: $23"):
      st.success("You bought Shorts")
      total += 23    

st.title("Children fashion")
st.image("https://cdn.pixabay.com/photo/2015/06/22/08/38/children-817368_1280.jpg")
c1,c2 = st.columns(2)

with c1:
  if st.checkbox("Shorts: $10"):
     st.success("You bought Shorts")
     total += 10

  if st.checkbox("Pants: $10"):
     st.success("You bought Pants")
     total += 10

with c2:
  if st.checkbox("T shirt: $25"):
     st.success("You bought a T shirt")
     total += 25

  if st.checkbox("Sweater: $25"):
     st.success("You bought a Sweater")
     total += 25

if st.button("Show me how much i need to pay"):
   st.subheader(f"You must pay ${total}")     

