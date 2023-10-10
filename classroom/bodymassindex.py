import streamlit as st



st.header('Body Mass Index')
st.write('BMI (Body Mass Index) is a measure that uses your height and weight to work out if your weight is healthy.')
st.write('')

with st.form(key='form',clear_on_submit=True):
    st.subheader('Enter Your Height')
    h1,h2,h3 = st.columns(3)
    with h1:
        meters = st.number_input('Enter Height In Meters')
    with h2:
        inches = st.number_input('Enter Height In Inches')

    st.write('')
    st.subheader('Enter Your Weight')
    w1,w2,w3 = st.columns(3)
    with w1:
        kg = st.number_input('Enter Weight In Kilograms')
    with w2:
        pounds = st.number_input('Enter Weight In Pounds')

    st.write('')

    submit = st.form_submit_button('Check My Mass')
    if submit:
        if kg and meters: #calc for metrics
            mass=kg/(meters**2)
            
    
        elif pounds and inches:
            mass=703*(pounds/(inches**2)) #calc for imperial
        #<18.5 underweight, 18.5-24.9 healthy weight, 25-29.9 overweight, 30+ obese
        if mass < 18.5:
            st.warning(f'Your BMI is {mass} and you are **UNDERWEIGHT**')
        elif mass >=18.5 and mass < 25:
            st.success(f'Your BMI is {mass} and you have a **HEALTHY WEIGHT**')
        elif mass >= 25 and mass <30:
            st.warning(f'Your BMI is {mass} and you are **OVERWEIGHT**')
        elif mass >=30:
            st.error(f'Your BMI is {mass} and you are **OBESE**')