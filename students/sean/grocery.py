import streamlit as st
total = 0
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))


st.write('You selected:', option)


st.title("Fruits")
st.image("https://cdn.pixabay.com/photo/2017/05/11/19/44/fresh-fruits-2305192_1280.jpg")
Fruits1,Fruits2 = st.columns(2)




with Fruits1:
    if st.checkbox("Apple: $15"):
        st.success("You added Apple")
        total += 15
    if st.checkbox("Orange: $15"):
        st.success("You added Orange")
        total +=15


with Fruits2:
    if st.checkbox("Banana: $15"):
        st.success("You added Banana")
        total += 15
    if st.checkbox("Grapes:$15"):
        st.success("You added Grapes")
        total +=15


st.title("Icecreams")
st.image("https://cdn.pixabay.com/photo/2014/10/06/15/24/ice-cream-476361_1280.jpg")
Ice1,Ice2 = st.columns(2)




with Ice1:
    if st.checkbox("Chocolate Icream: $50"):
        st.success("You added Chocolate IcecreamA")
        total += 50
    if st.checkbox("Vanila Icecream: $55"):
        st.success("You added Vanila Icecream ")
        total += 55


with Ice2:
    if st.checkbox("Strawberry Icecream: $50"):
        st.success("You added Strawberry ICecream")
        total += 50


    if st.checkbox("Mint Icecream:$50"):
        st.success("You added Mint Icecream")
        total += 50




st.title("Drinks")
st.image("https://cdn.pixabay.com/photo/2016/12/20/21/43/orange-1921548_1280.jpg")
Drinks1,Drinks2 = st.columns(2)




with Drinks1:
    if st.checkbox("Fanta: $15"):
        st.success("You added Fanta")
        total += 15
    if st.checkbox("Cola: $15"):
        st.success("You added Cola")
        total +=15


with Drinks2:
    if st.checkbox("Pepsi: $25"):
        st.success("You added Pepsi")
        total += 25
    if st.checkbox("7up: $25"):
        st.success("You added 7up")
        total +=25


st.title("Sweets")
st.image("https://cdn.pixabay.com/photo/2017/01/07/20/40/candies-1961536_1280.jpg")
sw1,sw2 = st.columns(2)




with sw1:
 if st.checkbox("Donut:$23"):
     st.success("You added a Donut")
     total += 23


 if st.checkbox("Cupcake: $50"):
     st.success("You added a Cupcake")
     total += 50


with sw2:
  if  st.checkbox("Bagel:$23"):
       st.success("You added a Bagel ")
       total +=23
 
  if st.checkbox("Puf-Puf: $25"):
      st.success ("You added Puf-Puf")
      total += 25
if st.button("Show me how much i have to pay"):
  st.subheader(f"The cost of all you bought is ${total}")
