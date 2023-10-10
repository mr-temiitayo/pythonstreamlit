

#Project Objective
# Create a student scores database which can
# -get the name done
# -4 subjects done
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file




#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)




import streamlit as st




import pandas as pd #this is used to read csv files and convert to a table (dataframe)




st.set_page_config(layout='wide')
N,E,M,S,C,B = st.columns(6)
with N:
    n = st.text_input("Name:")
with E:
    e = st.number_input("English Score",0,100)
with M:
    m = st.number_input("Math Score",0,100)
with S:
    s = st.number_input("Science Score",0,100)
with C:
    c = st.number_input("Computer Score",0,100)
with B:
    st.write(" ")
    st.write(" ")
    submit = st.button("Submit")
total = e+m+s+c
average = total/4
if average <=100 and average >90:
    grade = ("A")
if average <=90 and average >80:
    grade = ("B")
if average <=80 and average >70:
    grade = ("C")
if average <=70 and average >60:
    grade = ("D")
if average <=60 and average >50:
    grade = ("E")
if average <=50:
    grade = ("Fail")


st.title('Students Scores Database')

#REVISE DICTIONARY,LIST, APPEND
#read a csv file
df=pd.read_csv('score.csv') #pandas should read this csv file
st.dataframe(df,use_container_width=True) #streamlit should display as dataframe

# Name,English,Math,Science,Computer,Total,Average,Grade
def new_student(n,e,m,s,c,total,average,grade,df):
    student_dict = {'Name':n,'English':e,'Maths':m,'Science':s,'Computer':c,
                    'Total':total,'Average':average,'Grade':grade}
    student_df = pd.DataFrame([student_dict]) #converts student dict into a dataframe with columns and data
    new_df = pd.concat([df,student_df],ignore_index=True)
    return new_df


if submit:
    st.success(f'Your total is {total} mark, average is {average} mark, your grade is {grade}')
    new_df = new_student(n,e,m,s,c,total,average,grade,df)
    new_df.to_csv('score.csv',index=False)
