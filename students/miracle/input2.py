import streamlit as st
name =st.text_input('please enter your  name')
favourite_sport =st.text_input('please enter your favourite sport')
favourite_team =st.text_input('please enter your favourite team')
favourite_player =st.text_input('please enter your favourite player')
st.write ('hi',name,'your favourite sport is' ,favourite_sport,'your favourite team is', favourite_team,'and your favourite player is', favourite_player)
