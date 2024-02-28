import streamlit as st #this is the webpage for our python projects
import pandas as pd #this helps to read, write CSV files, and convert them to a table 

# submit students information (student name, scores) DONE
# The computer will calc the (total, average, grade of student) DONE
# save each submitted info into a CSV file 
# create a database with chart and with filter
# teacher can edit the database
# search students file
# download the database
# computer send a mail

#CSV file is a text file that has all it's data separated by a comma (COMMA SEPARETED VALUES)

readcsv = pd.read_csv('scores.csv') #pandas reads CSV file


menu = st.sidebar.selectbox('Menu',['Submit Scores', 'Search Student', 'Students Database', 'Edit Database'])


if menu == 'Submit Scores':
    st.header('Submit Students Scores Here')
    name = st.text_input("Enter the student's name")




    subject1, subject2 = st.columns(2)




    with subject1:
        maths = st.number_input("Enter student's score for Maths",0,100,step=10,value=50)
        science = st.number_input("Enter student's score for Science",0,100,step=10,value=50)
        art = st.number_input("Enter student's score for Art",0,100,step=10,value=50)




    with subject2:
        english = st.number_input("Enter student's score for English",0,100,step=10,value=50)
        history = st.number_input("Enter student's score for History",0,100,step=10,value=50)
        geography = st.number_input("Enter student's score for Geography",0,100,step=10,value=50)




    totalscore = maths + science + art + english + history + geography




    average = totalscore /6
    average = round(average,2)



    #st.success, error, warning, info
    if average >= 90:
        grade = ("A+")
    elif average >= 85:
        grade = ("A")
    elif average >= 80:
        grade = ("A-")
    elif average >= 75:
        grade = ("B+")
    elif average >= 70:
        grade = ("B")
    elif average >= 65:
        grade = ("C+")
    else:
        grade = ("FAIL")


    savebutton = st.button("Save Students Scores")


    if savebutton:
        if grade != ("FAIL"):
            st.success(f"{name}'s total score is {totalscore} points, their average is: {average}%, and their grade is: {grade}.")
        else:
            st.error(f"{name}'s total score is {totalscore} points, their average is: {average}%, and their grade is: {grade}.")
        
    
        #Here we create the dictionary to store the key and the data, then we convert to a df using pandas
        studentsdict = {'Name':[name],'Maths': [maths],'English':[english],'Science':[science],'Art':[art],
                        'Geography':[geography],'History':[history],'Total Score':[totalscore],'Average':[average],'Grade':[grade]}
        # st.write(studentsdict)
        studentsdf = pd.DataFrame(studentsdict) #converts to dataframe
        st.table(studentsdf)

        #Next we join the existing df with the new df and save it on the csv file
        
    firstname = 'Jason'

    lastname = 'Todd'

    st.write(firstname+lastname) #the comma is the separator, str+str with strings is concatenate

if menu == "Students Database":
    st.table(readcsv) #streamlit displays the csv file



# eduSTEMlab
#Classwork: create a dictionary of any 5 cars 
# with their car names, country made, year, transmission and convert it to a table