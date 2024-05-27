# Mia is excited to explore the Minecraft store and purchase some exciting items for her gameplay. 
# She wants to download the game itself, choose a world to play in, buy some costumes, and maybe even get a farm! Additionally, she’s eyeing some gems to enhance her gameplay. 
# Write a Python program to help Mia calculate the total cost of her Minecraft adventure.

# Mia’s journey through the Minecraft store involves several steps:

# First, she needs to download the game itself, which costs $200.
# Mia will then enter her username and password to access the store.
# Next, she can choose between two worlds: the Survival world for $20 or the Creative world for $100.
# Mia can also browse through three different costume options, each with its own price tag.
# Additionally, Mia has the option to add a farm to her gameplay for an additional $25.
# Finally, she can purchase gems: diamonds for $45, silver for $20, or gold for $30.
# After making her selections, Mia wants to see the total cost of her Minecraft adventure. Let’s create a Python program to help her out.



import streamlit as st

cost = 0
minecraftcost = 200
survival = 20
creative = 100

download = st.selectbox("Download Minecraft to Start?",['No (Exit)','Yes $200'])

if download == 'Yes $200':
    cost += 200
    st.write("You got Minecraft for $200")
    st.balloons()
    st.write("Okay good. Now we need to setup your username and your password")
    username = st.text_input("Please enter your username")
    password = st.text_input('Please enter your password',type='password')
    world = st.selectbox("Choose your world to purchase",['None','Creative: $100', 'Survival: $20'])

    if world == 'Creative: $100':
        cost += 100
        st.write("You got creative world for $100")

    elif world == 'Survival: $20':
        cost += 20
        st.write("You got survival for $20")
