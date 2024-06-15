import streamlit as st
one = st.number_input("Please type a number:")
two = st.number_input("Please type another number:")
(addition, multiplication, division, subtraction) = st.columns(4)
with addition:
    if st.button("ADD"):
        ans = (one+two)
        st.write(ans)
with multiplication:
    if st.button("MULTIPLY"):
        ans = (one*two)
        st.write(ans)
with division:
    if st.button("DIVIDE"):
        ans = (one/two)
        st.write(ans)
with subtraction:
    if st.button("SUBTRACT"):
        ans = (one-two)
        st.write(ans)