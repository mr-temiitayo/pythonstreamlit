import streamlit as st
st.set_page_config (layout="wide")
total = 0
st.title("CULINARY CAFE")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYqU-_1lsJZpZckpY0s3SrHVLSf9Ri_OFrC8Ia32qU4g&s",width=1150)  
st.subheader ("OUR MENU IS:")
st.title ("Appetizers")
A1,A2,A3,A4 = st.columns(4)




with A1:
    st.image("https://tastesbetterfromscratch.com/wp-content/uploads/2020/05/Hummus-3.jpg",width= 171)
    if st.checkbox("Hummus and Bread:$10"):
        st.success("You bought Hummus and Bread✅")
        total += 10




with A2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5lfCZd8Y5mBljp3xizS5f23RpBGPItXzQhcjuEEvPSg&s",width= 153)
    if st.checkbox("Hors d'oeuvre:$40"):
        st.success("You bought Hors d'oeuvre👍")
        total += 40
with A3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSx1saZP9aUuCJYuQ_ZSY-CZBkzgaiyruYbRHFSuAWTg&s",width=171)
    if st.checkbox("Canape:$20"):
        st.success("You bought Canape✅")
        total += 20
   
with A4:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuQoV7PYiz6v6St7Msmh_JA07NlwtZskcel_J-vtcBuQ&s",width=171)
    if st.checkbox("Mozzarella sticks:$50"):
        st.success("You bought Mozzarella sticks👍")
        total += 50


st.title ("Main Meal")
M1,M2,M3,M4= st.columns(4)


with M1:
    st.image("https://www.africanbites.com/wp-content/uploads/2018/03/IMG_9302.jpg",width=177)
    if st.checkbox ("Mac and Cheese:$100"):
      st.success("You bought Mac and Cheese✅")
      total += 100


with M2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnF3Yr9oqZg47eE5iv2TLltjmVH3V5OJnhIL98u7rktw&s",width=150)
        if st.checkbox ("Pasta and Meatballs:$120"):
          st.success("You bought Pasta and Meatballs👍")
          total += 120


with M3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFcwk_GrvMalT9GzU9Jj_6NKYItLeKzbsiR7roAdOFqQ&s",width=157)
    if st.checkbox ("Braciole:$105"):
      st.success("You bought Braciole✅")
      total += 105
     
with M4:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_GizoanG-hj8qxWh2eKiM6glJiMdxSCqMUuhNZEB4Sw&s",width=150)
    if st.checkbox ("Lasagna:$129"):
        st.success("You bought Lasagna👍")
        total += 129


st.title ("Dessert")
D1,D2,D3,D4= st.columns(4)


with D1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4DypGJG6Nm4kdUBgxjxtJtqDfYoVmtvD963S3YlPG-w&s",width=150)
    if st.checkbox ("Coffee Toffee Ice cream:$30"):
        st.success("You bought Icecream✅")
        total += 30


with D2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRN04BbgbAk8AwM32LwLEHzoddmQel4iFtuZOrqWEGwDg&s",width=160)
    if st.checkbox ("Macha:$20"):
        st.success("You bought Macha👍")
        total += 20


with D3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvGnhw0A-YAi91E0BYLwA6NYPCWXpjpsGW2vNYvyKN9g&s",width=147)
    if st.checkbox ("Bubble tea(Boba):$50"):
        st.success("You bought Bubble tea(Boba)✅")
        total += 50


with D4:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2siSAgueA4MV_52jHeXprUxTYuWDFj8nfws5MWYxXAw&s",width=150)
    if st.checkbox("Jello:$40"):
        st.success("You bought Jello👍")
        total += 40


if st.button("Show me the cost"):
    st.subheader(f"The cost of items purchased is ${total}")


sl1,sl2=st.columns(2)
with sl1:
    if st.checkbox("Click to share the bill"):
        People= st.slider("How many people in total",2,100)
        Person =total/People
        st.subheader(f"The cost per person is ${Person}")
       

