import streamlit as st
import pandas as pd #this will help us with our csv files (read, add to it etc)

st.set_page_config(layout='wide')
database = pd.read_csv('scores.csv')
st.dataframe(database) #dataframe means a table


name = st.text_input("My name is: ")

left , right = st.columns(2)

with left:
    pe = st.number_input("My PE grade is :" ,0,100)
    Science = st.number_input("My Science grade is: ",0,100)


with right:
    Maths = st.number_input("My math grades are :",0,100)
    English = st.number_input("My english grade is :",0,100)


totalscore = pe+Science+Maths+English
average = totalscore/4


if average >= 90:
    grade = 'A+'

elif average >= 80:
    grade = "A"

elif average >= 70:
    grade = "B"

elif average >= 60:
    grade = "C"

elif average >= 50:
    grade = "D"

elif average < 50:
    grade = 'F'

# Name,Maths,English,Science,Physical Ed,Total,Average,Grade
if st.button("Submit Students Scores"):
    st.subheader(f"{name} Total score is: {totalscore}, Average is: {average}, Grade is: {grade} ")

    #this is the dictionary
    student_dict = {'Name':[name],'Maths':[Maths],'English':[English],'Science':[Science],
                        'Physical Ed':[pe],'Total':[totalscore],'Average':[average],'Grade':[grade]}
    #pandas converts the dictionary to a table
    student_dataframe = pd.DataFrame(student_dict)
    new_database = pd.concat([database,student_dataframe],ignore_index=True)
    new_database.to_csv('scores.csv',index=False)
