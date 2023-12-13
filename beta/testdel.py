import streamlit as st
colour=['Pink','Red','Yellow','White']
st.write(colour)

desserts= st.selectbox('Desserts', ['Chocolate','Ice cream','Rice'])

drinks=st.radio('Drinks',['Pepsi','Coke','Fanta'])
st.write('You choose',drinks)

menu = st.sidebar.selectbox('Meals',['Pizza','Chicken','Pasta'])

