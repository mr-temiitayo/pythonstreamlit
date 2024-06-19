import streamlit as st
name=st.text_input('please enter your name')
flour_bag_cost=st.number_input('please enter the bag cost of a flour')
num_flour_bags=st.number_input('please enter the number of flour bags')
egg_carton_cost=st.number_input('please enter the cost of carton of egg')
num_egg_cartons=st.number_input('please enter the number of cartons of egg')
chocholate_chip_pack_cost=st.number_input('please enter the cost of chocholate pack')
num_chocholate_chip_pack=st.number_input('please enter the number of chocholate pack')
discount=st. number_input('please enter the discount amount')
total_cost_flour=flour_bag_cost*num_flour_bags
total_cost_egg=egg_carton_cost*num_egg_cartons
total_cost_chocholate=chocholate_chip_pack_cost*num_chocholate_chip_pack
#calculate the total amount of everything
#subtract discount from total amount
total_spent=('discount subtracted from total amount')
st.write("hi",name,'after using your discountyou spent a total of $',total_spent,'on your baking supply')



