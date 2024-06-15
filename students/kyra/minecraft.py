import streamlit as st
pay = 0
game = 200
survival = 20
creative = 100
downloadstart = st.selectbox("Do you want to download Minecraft",["Choose", "Yes (pay 200)","No(Exit)"])
if downloadstart == "Yes (pay 200)":
    pay +=200
    st.write("You successfully downloaded Minecraft!")
    st.balloons()


    name = st.text_input("What's your name?")
    password = st.text_input("Enter a password:",type = "password")
    selectworld = st.selectbox("Choose a world to buy:",["none","Survival World : $20", "Creative World: $100"])


    if selectworld == "Survival World : $20":
        st.write("You got Survival World!")
        pay +=20
        st.balloons()
    elif selectworld == "Creative World: $100":
        st.write("You got Creative World!")
        pay +=100
        st.balloons()
    else:
        st.write("You've selected default world.")
    skins = st.selectbox("Choose a skin!",["Choose","Princess : $20", "Zombie : $25", "Robot : $ 27"])


    if skins == "Princess : $20":
        st.write("You got the princess skin!")
        pay +=20
        st.balloons()
    elif skins == "Zombie : $25":
        st.write("You got the zombie skin!")
        pay+=25
        st.balloons()
    else:
        st.write("You got the robot skin!")
        pay+=27
        st.balloons()
    farm = st.selectbox("Do you want an additional farm for $25?", ["choose","yes", "no"])
    if farm == "yes":
        st.write("You got a additional farm!")
        pay+=25
        st.balloons()
    else:
        st.write("You didn't purchase a farm!")
   
    gems = st.selectbox("Choose a Gem to buy:", ["choose","Diamond : $45", "Silver : $20", "Gold : $30"])
    if gems == "Diamond : $45":
        st.write(" You got the Diamonds!")
        pay +=45
        st.balloons()
    elif gems == "Silver : $20":
        st.write(" You got the Silver!")
        pay+=20
        st.balloons()
    else:
        st.write("You got the Gold!")
        pay+=30
        st.balloons()
    
    
st.button("Click to see total amount")
if st.button:
    st.write('You need to pay:',str(pay),'dollars')
