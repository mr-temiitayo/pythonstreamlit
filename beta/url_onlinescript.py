import streamlit as st
import requests as req
st.header("Registration form")
fullNum=st.text_input("Full Name : ")
fatherName = st.text_input("Father name : ")
motherName = st.text_input("Mother name : ")
age=st.slider("Age(in years) : ",1,100)
gender=st.radio("Gender :",["Male","Female"])
nationality=st.selectbox("Nationality :",["Indian","other"])
adress=st.text_area(" Full Address : ")
email=st.text_input("E-mail : ")
mno=st.text_input("Mobile No : ")
submit=st.button("submit")
if submit==True:
    if len(fullNum)==0 or len(fatherName)==0 or len(motherName)==0 or len(email)==0:
        st.error("Fill all feilds above")
        mail=email
        if len(mail)>0 and mail.find("@")<0:
                st.error("Enter a valid email")
    else:
         url="https://script.google.com/macros/s/AKfycbzsHJ5paT0EguvW4cYxpTtGGoY3MyO4qd7_7pzIfMbNHb6WjJLz9xzJNcABTWa97K6_YQ/exec?fname="+str(fullNum)+"&faname="+str(fatherName)+"&mname="+str(motherName)+"&age="+str(age)+"&gender="+str(gender)+"&nlty="+str(nationality)+"&add="+str(adress)+"&mail="+str(email)+"&mob="+str(mno)
         req.get(url)
         st.balloons()
         st.success("submitted sucessfully")