"""
-Create a dinner app that welcomes users and shows them the food selections
-Add a restaurant picture
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""
import streamlit as st
st.set_page_config(layout="wide") #makes your page full width


people = 0
total = 0


st.title("Welcome To Pay N Eat Restaurant")
st.image("https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg")




st.subheader("We have these meals available. Pick your choice")




st.title("Rice")
rice1,rice2,rice3,rice4 = st.columns(4)




with rice1:
    if st.checkbox("Ofada rice: $20"):
     st.write("You have added Ofada rice")
     total += 20
    if st.checkbox("Jollof rice: $20"):
     st.write("You have added  Jollof Rice")
     total += 20




with rice2:
    if st.checkbox("Rice and beans: $20"):
     st.write("You have added Rice and beans")
     total += 20
    if st.checkbox("Fried rice: $20"):
     st.write("You have added Fried rice")
     total += 20


with rice3:
    if st.checkbox("Basmati Rice: $20"):
     st.write("You have added Basmati Rice")
     total += 20
    if st.checkbox("Biryani: $20"):
     st.write("You have added Biryani")
     total += 20




with rice4:
    if st.checkbox("Risotto: $20"):
     st.write("You have added Risotto")
     total += 20
    if st.checkbox("Hyderabadi biryani: $20"):
     st.write("You have added Hyderabadi biryani")
     total += 20
   
 








st.title("Fruits")
fruits1,fruits2,fruit3 = st.columns(3)
with fruits1:
    if st.checkbox("Apple: $10"):
     st.write("You have added Apple")
     total += 10
    if st.checkbox("Banana: $10"):
     st.write("You have added Banana")
     total += 10


with fruits2:
    if st.checkbox("Dragonfruit: $10"):
     st.write("You have added Dragonfruit")
     total += 10
    if st.checkbox("Cherry: $10"):
     st.write("You have added Cherry")
     total += 10






with fruit3:
    if st.checkbox("Avocados: $10"):
     st.write("You have added Avocados")
     total += 10
    if st.checkbox("Pineapple: $10"):
     st.write("You have added Pineapple")
     total += 10














st.title("Drinks")
drink1,drink2,drink3 = st.columns(3)




with drink1:
    if st.checkbox("Fanta: $10"):
     st.write("You have added Fanta")
     total += 10
    if st.checkbox("cola: $10"):
     st.write("You have added cola")
     total += 10


with drink2:
    if st.checkbox("pepsi: $10"):
     st.write("You have added pepsi")
     total += 10
    if st.checkbox("7 Up: $10"):
     st.write("You have added 7 Up")
     total += 10


with drink3:
    if st.checkbox("sprit: $10"):
     st.write("You have added sprit")
     total += 10
    if st.checkbox("Mountain Dew: $10"):
     st.write("You have added Mountain Dew")
     total += 10






st.title("Desert")
desert1,desert2,desert3 = st.columns(3)
with desert1:
    if st.checkbox("chocolate cake: $70"):
     st.write("You have added chocolate cake")
     total += 70
    if st.checkbox("strawberry cupcake: $30"):
     st.write("You have added strawberry cupcake")
     total += 30






with desert2:
    if st.checkbox("Muffins: $20"):
     st.write("You have added Muffins")
     total += 20
    if st.checkbox("Brownies: $20"):
     st.write("You have added Brownies")
     total += 25


with desert3:
    if st.checkbox("Cheesecakes: $70"):
     st.write("You have added Cheesecakes")
     total += 70
    if st.checkbox("Biscuits: $25"):
     st.write("You have added Biscuits")
     total += 25




st.title("Icecream")
cream1,cream2,cream3 = st.columns(3)
with cream1:
    if st.checkbox("Sundae: $5"):
     st.write("You have added Sundae")
     total += 5
    if st.checkbox("Mint chocolate chip ice cream: $5"):
     st.write("You have added Mint chocolate chip ice cream")
     total += 5




with cream2:
    if st.checkbox("strawberry ice cream: $5"):
     st.write("You have added strawberry ice cream")
     total += 5
    if st.checkbox("chocolate chip cookie dough ice cream: $5"):
     st.write("You have added chocolate chip cookie dough ice cream")
     total += 5


with cream3:
    if st.checkbox("Vanilla ice cream: $5"):
     st.write("You have added Vanilla ice cream")
     total += 5
    if st.checkbox("Chocolate ice cream: $5"):
     st.write("You have added Chocolate ice cream")
     total += 5




st.title("Pizza")
Pizza1,Pizza2,Pizza3 = st.columns(3)
with Pizza1:
    if st.checkbox("Pepperoni Pizza: $15"):
     st.write("You have added Pepperoni Pizza")
     total += 15
    if st.checkbox("Meat Pizza: $15"):
     st.write("You have added Meat Pizza")
     total += 15




with Pizza2:
    if st.checkbox("BBQ Chicken Pizza: $15"):
     st.write("You have added BBQ Chicken Pizza")
     total += 15
    if st.checkbox("Pineapple Pizza: $15"):
     st.write("You have added Pineapple Pizza")
     total += 15


with Pizza3:
    if st.checkbox("Veggie Pizza: $15"):
     st.write("You have added Veggie Pizza")
     total += 15
    if st.checkbox("Pizza with cheese: $15"):
     st.write("You have added Pizza with cheese")
     total += 15




if st.button("Show the bill"):
  st.write("Your total is",total,"dollars")


if st.checkbox("Click to share your bill with others"):
  slider1,slider2 = st.columns(2)
  with slider1:
      people += st.slider("How many people in total ",2,100,value= 2)
      eachperson = int(total/int(people))
      st.write("Your total price per person is",eachperson)

