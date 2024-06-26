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
menu = st.sidebar.selectbox('Menu',['Submit Scores','Database'])


if menu == 'Submit Scores':
    colu1,colu2,colu3=st.columns([1,2,1])
    with colu2:
        st.header("Submit Student Scores")

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

    averageround = str(round(averagescore, 2))  #round to 2 dp


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


    # Name,Mathematics,English,Geography,History,Science,Arabic,Total,Average,Grade
    if st.button("Submit Scores"):
        success1,success2 = st.columns(2)
        with success1:
            st.success('Student scores submitted')
        studentsdict = {'Name':[name],'Mathematics':[mathscore],'English':[englishscore],
                        'Geography':[geoscore],'History':[histscore],'Science':[sciscore],
                        'Arabic':[arabscore],'Total':[combinescore],'Average':[averagescore],
                        'Grade':[grade]}
        
        students_table = pd.DataFrame(studentsdict)
        new_table = pd.concat([csvlink,students_table],ignore_index=True) #this will merge the two dataframes together
        new_table.to_csv("scores.csv",index=False)#both should ignore index positions in the table

if menu == 'Database':
    colu1,colu2,colu3=st.columns([1,2,1])
    with colu2:
        st.header("Students Database")
    st.table(csvlink) #streamlit displays as a table