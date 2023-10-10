import streamlit as st #this is used to design the page for your python program

# ---------------STREAMLIT TEXT----------
# st.header('Welcome')

# st.subheader('Here is my new project')

# st.write('Welcome once again')

st.title('Age Calculator')

name = st.text_input('Enter your name')

yob = st.number_input('Enter your year of birth',1950,2023)

curr = st.number_input('Enter your current year',2023)

age = curr - yob

if st.button('Check My Age'):
    st.warning(f'{name} you are {age} years old in {curr}') 
    #f-string will output all as string, you can indicate variables with {}
    # st.success,error,info,warning