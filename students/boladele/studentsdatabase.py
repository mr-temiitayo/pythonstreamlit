# Creating students scores database
# -Get info of each student (name, 4 subjects score)
# -Calculate the average of total score of each student
# -Grade the student with (A,B,C,D,E,F) -----
# -Save all data in a csv file
# -Show current csv database file

import streamlit as st
import pandas as pd #this is used to create dataframes
st.title('Students Database')


#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)
df = pd.read_csv('scores.csv') #same folder that is why it as no address
st.dataframe(df)

name = st.text_input('Enter your name')
maths = st.number_input('Enter Maths score',0,100,value=0)
science = st.number_input('Enter Science score',0,100,value=0)
history = st.number_input('Enter History score',0,100,value=0)
total = maths + science + history
average = total/3

#function to add new student values to the Dataframe
def new_student(name,maths,science,history,total,average,df):
    student_dict = {'Name':name,'Maths':maths,'Science':science,'History':history,'Total':total,'Average':average}
    #the above is used to save the values gotten to a key with is the same as the CSV columns variables
    new_df = pd.DataFrame([student_dict]) #convert the dict into a dataframe
    df = pd.concat([df,new_df],ignore_index=True) #this will join the old df to the new df
    return df


if st.button("Add Student Scores"):
    df = new_student(name,maths,science,history,total,average,df) #add this to df
    df.to_csv('scores.csv',index=False) #save new student data to dataframe
    st.success('Student score added')