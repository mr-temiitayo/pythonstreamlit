"""
-Add a restaurant picture
-Create a restaurant app that shows users the food selections
-After they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""
import streamlit as st
st.set_page_config(layout= "wide") #Makes your screen larger
Menu = ['Food', 'Drinks', 'Appetizers']
select = st.sidebar.selectbox('select menu', Menu)












bill = 0
st.header("Des conneries trop chères")
if select == 'Food':




    st.subheader("MainCourse")
    MainCourse1, MainCourse2, MainCourse3, MainCourse4 = st.columns(4)


    with MainCourse1:
      st.image("https://media.thepeakmagazine.com.sg/public/2022/05/Fat-Cow_Set-Lunch_A4-Miyazaki-Wagyu-Donburi-1.jpg")
      if st.checkbox(" Wagyu Beef| Cavier: $1000"):
        bill += 1000
        st.write("Added")


    with MainCourse2:
      st.image("https://www.foodandwine.com/thmb/puk7KHHQCipYTP7qBYGWKyJDeGk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1K-Lobster-Roll-Kit-FT-2-BLOG1121-6b8e1eb6592846aca88f5292d214ae6a.jpg")
      if st.checkbox("Lobster roll| Cavier |Wagyu Beef: $600"):
        bill += 600
        st.write("Added")


    with MainCourse3:
      st.image("https://hips.hearstapps.com/delish/assets/cm/15/10/54f939f9a8f20_-_fleurburger.jpg")
      if st.checkbox("Fleurburger: $5,000"):
        bill += 5000
        st.write("Added")


    with MainCourse4:
      st.image("https://i0.wp.com/dashofsavory.com/wp-content/uploads/2017/10/IMG_63151.jpg?ssl=1")
      if st.checkbox("Squid Ink Pasta with Buttery Lobster: $2000"):
        bill+= 2000
        st.write("Added")






elif select == 'Drinks':


    st.subheader("Drinks")
    Drinks1, Drinks2, Drinks3, Drinks4 = st.columns(4)


    with Drinks1:
      st.image("https://discover.luxury/wp-content/uploads/2017/04/Billionaires-Margarita-1024x731.jpg")
      if st.checkbox("Billionaire’s Margarita Glass(Drink A): $1,100"):
        bill += 1100
        st.write("Added")
     
      if st.checkbox("Billionaire’s Margarita bottle(Drink B): $1,330"):
        bill+= 1330
        st.write("Added")


    with Drinks2:
      st.image("https://assets.entrepreneur.com/slideshow/20181004152548-Most-Expensive-Alcoholic-Drinks-in-the-World-7-Bombay-Sapphire--Revelation-200000.jpeg?auto=webp&quality=95&&width=675")
      if st.checkbox("Bowmore (Drink A): $165,000"):
        bill += 165000
        st.write("Added")
     
      if st.checkbox("Bowmore bottle (Drink B): $200,000"):
        bill+= 200000
        st.write("Added")


    with Drinks3:
      st.image("https://live.staticflickr.com/3287/2497200674_99b8aecf61_c.jpg")
      if st.checkbox(" Mendis Coconut Brandy Glass (Drink A): $1,500,500"):
        bill += 1500500
        st.write("Added")
     
      if st.checkbox(" Mendis Coconut Brandy Bottke (Drink B): $2,000,000"):
        bill+= 2000000
        st.write("Added")


    with Drinks4:
      st.image("https://img.huffingtonpost.com/asset/5d013574250000ae13dd232f.jpeg?ops=scalefit_720_noupscale")
      if st.checkbox("Rent the whole Bar: 4,000,000 "):
        bill += 4000000
        st.write("Added")




st.subheader("Appetizers")
App1, App2, App3, App4 = st.columns(4)


with App1:
  st.image("https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com//content/6e/3c/f821602d4aaf99715525002b9f76/4-small-bites-guaranteed-to-impress._TTW_._CR0,0,1560,1170_._SR1000,750_._QL100_.png")
  if st.checkbox("Blinis with Caviar: $15"):
    bill+= 15
    st.write("Added")


with App2:
  st.image("https://www.myparisiankitchen.com/wp-content/uploads/2022/02/roule-concombre-saumon-fume-mpk-716x537.jpg")
  if st.checkbox("Cucumber and Smoked Salmon Rolls: $20"):
    bill+= 20
    st.write("Added")


with App3:
 st.image("https://www.foodandwine.com/thmb/YElkX-hxobMFXRqqn4QZ3VNWX9U=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/deviled-egg-crisps-FT-RECIPE1018-0c611a46d8c44156870f292e42b8a9a3.jpg")
 if st.checkbox("Deviled Egg Crisps(Appetizer A): $16"):
  bill+= 16
  st.write("Added")


 if st.checkbox("Deviled Egg Crisps| Wine(Appetizer B): $23"):
  bill+= 23
  st.write("Added")


with App4:
  st.image("https://www.southernliving.com/thmb/KRfYgFfV40uNDd8zu3hHC77V_gc=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sl_seo_121119_5603-2000-68309888c6a24f97bc242874312c1a95.jpg")
  if st.checkbox("Slow-Cooker Grape Jelly Meatballs: $12"):
    bill+= 12
    st.write("Added")


st.subheader("Desserts")
Dess1, Dess2, Dess3, Dess4 = st.columns(4)


with Dess1:
  st.image("https://img.delicious.com.au/OIFg-hzU/del/2021/07/hazelnut-panna-cotta-with-chocolate-ganache-155378-2.jpg")
  if st.checkbox("Hazelnut panna cotta with chocolate ganache: $200"):
   bill += 200
   st.write("Added")


with Dess2:
  st.image("https://assets.londonist.com/uploads/2016/10/i875/millefeuille.jpg")
  if st.checkbox("Chocolate Millefeuille at Roux at The Landau: $100"):
   bill += 100
   st.write("Added")


with Dess3:
  st.image("https://farm2.staticflickr.com/1612/26295189042_a9ef17bb7a_b.jpg")
  if st.checkbox("Sakura Mousse cake: $300"):
    bill += 300
    st.write("Added")


with Dess4:
  st.image("https://www.happyveggiekitchen.com/wp-content/uploads/2016/02/1-baileys-chocolate-pots-130-1200x800.jpg")
  if st.checkbox("Chocolate Dessert Pots: $150"):
    bill += 200
    st.write("Added")






st.subheader(f"Total cost: ${bill}")
if st.button("Checkout"):
  st.write(f"Your total amounts to", bill,"Your transfer has been successful")

