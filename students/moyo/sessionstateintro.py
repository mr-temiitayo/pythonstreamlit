import streamlit as st
#session state is a feature used in streamlit 
# to create, update and keep your variables in a permanent sessionstate dictionary


#reminder: UPLOAD LIVE PROJECT 
# number = 5

# st.write(number)

# if st.button("Add 1"):
#     number+=1
#     st.write(number)


#to create variables in sessionstate

#stopped with sessionstate needs a refresh or rerun to show current value

st.write(st.session_state)

if 'number' not in st.session_state:
    st.session_state.number = 5

st.write(st.session_state.number)

if st.button("Add 1"):
    st.session_state.number +=1

if st.button("Subtract 1"):
    st.session_state.number -=1
