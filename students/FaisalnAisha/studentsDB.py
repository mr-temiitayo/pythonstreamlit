#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)

#----Teacher-------------
#create a CSV file
# -update your csv file

#what is csv file?
#csv file is a text file that each data is separated by a comma (comma separated values)

import streamlit as st
import pandas as pd #helps to read,write CSV files and display as a table
st.set_page_config(layout='wide')

csvlink = pd.read_csv('scores.csv') #pd helps to read the csv file/link
st.table(csvlink) #streamlit displays as a table

colu1,colu2,colu3=st.columns([1,2,3])
with colu2:
    st.header("Pupil Database")


name=st.text_input("Enter The Pupil's Name")
colu4,colu5=st.columns(2)
with colu4:
    mathscore=st.number_input("Pupil's Maths Score: ",0,100,value=70)
    englishscore=st.number_input("Pupil's English Score: ",0,100,value=70)
    geoscore=st.number_input("Pupil's Geography Score: ",0,100,value=70)
with colu5:
    histscore=st.number_input("Pupil's History Score: ",0,100,value=70)
    sciscore=st.number_input("Pupil's Science Score: ",0,100,value=70)
    arabscore=st.number_input("Pupil's Arabic Score: ",0,100,value=70)


combinescore=mathscore+englishscore+geoscore+histscore+sciscore+arabscore
averagescore= combinescore / 6

averageround = round(averagescore, 2)  #round to 2 dp


if averagescore >= 90:
    grade="A+"
elif averagescore >= 80:
    grade="A"
elif averagescore >= 70:
    grade="B"
elif averagescore >= 60:
    grade="C"
elif averagescore >= 50:
    grade="D"
elif averagescore <  50:
    grade="F"


if st.button("Submit Scores"):
    st.write(name,"your Total Score: ",combinescore,"Average Score: ",averageround,"Grade: ",grade)




