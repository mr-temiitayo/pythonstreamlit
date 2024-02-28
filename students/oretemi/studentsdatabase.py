#Project Objective
# Create a student scores database which can
# -get the name of the student
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -save in a CSV file
# -update your csv file when we add new students


#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

import streamlit as st
import pandas as pd #will help to read and write csv files, convert to a table

csvfile = pd.read_csv('scores.csv')
st.table(csvfile)


st.subheader("Fill in the form below to get your grade")
user_name = st.text_input("Enter your name here")

colm1,colm2 = st.columns(2)


with colm1:
    English = st.number_input("Enter your grade for English",0,100)
with colm2:
    Math = st.number_input("Enter your grade for Math",0,100)


colm3,colm4 = st.columns(2)


with colm3:
    Science = st.number_input("Enter your grade for Science",0,100)
with colm4:
    History = st.number_input("Enter your grade for History",0,100)


colm5,colm6 = st.columns(2)


with colm5:
    Geo = st.number_input("Enter your grade for geography",0,100)


#---#
total = English + Math + Geo + History + Science
avr = total / 5
grade = ""
if avr > -1 and avr < 50:
    grade = "F"
elif avr > 49 and avr < 60:
    grade = "E"
elif avr > 59 and avr < 70:
    grade = "D"
elif avr > 69 and avr < 80:
    grade = "C"
elif avr > 79 and avr < 90:
    grade = "B"
elif avr > 89 and avr < 101:
    grade = "A"
#---#
with colm6:
    st.write("")
    st.write("")
    Checkbutton = st.button("Get Result")


if Checkbutton:
    st.write(user_name," total score was",total,". The average is",avr,", and there grade is",grade,".")
    