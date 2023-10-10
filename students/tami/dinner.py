"""
-Create a dinner app that welcomes users and shows them the food selections
-Add a restaurant picture
-If they choose/select their meals, show them the total amount
-Then ask how many students want to share the bill
-Then show the amount each person must contribute to pay the bill
"""
import streamlit as st
st.set_page_config(layout="wide")
total = 0
st.title("Pay and Eat Restaurant")
st.image("https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg")
st.subheader("We have:")
st.title("Fruits")
f1,f2,f3 = st.columns(3)


with f1:
    if st.checkbox("Apple:$55"):
        st.success("You Bought an Apple")
        total += 55
   
with f2:    
    if st.checkbox("Orange:$55"):
        st.success("You Bought an Orange")
        total += 55


with f3:
    if st.checkbox("Banana:$55"):
        st.success("You brought a banana")
        total +=55




st.title("Drinks")
d1,d2,d3=st.columns(3)
with d1:
    if st.checkbox("Coco Cola:$60"):
        st.success("You bought coca cola")
        total+=60
       
with d2:
    if st.checkbox("Fanta:$40"):
        st.success("You bought fanta")
        total+=40


with d3:
    if st.checkbox("Sprite:$56"):
        st.success("You bought sprite")
        total+=56






st.title("Meals")
m1,m2,m3,m4=st.columns(4)


with m1:
    if st.checkbox("Jollof Rice:$70"):
        st.success("You bought jollof rice")
        total+=70
   
with m2:
    if st.checkbox("Seafood boil:$100"):
        st.success("You bought seafood boil")
        total+=100




with m3:
    if st.checkbox("Pasta:$50"):
        st.success("You bought pasta")
        total+=50


with m4:
    if st.checkbox("Chicken noodles:$65"):
        st.success("You bought chicken noodles")
        total+=60


if st.button("Show me the cost"):
  st.subheader(f"The cost of all you bought is ${total}")

sl1,sl2 = st.columns(2)
with sl1:
    if st.checkbox("Click to share the bill"):
        people = st.slider("How many people in total",2,100)
        person = total / people
        st.subheader(f'The cost per person is ${person}')