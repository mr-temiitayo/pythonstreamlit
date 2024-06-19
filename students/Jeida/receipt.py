import streamlit as st


cl,cl2,cl3 = st.columns([2,1,1])
with cl3:
    st.header(':blue[**RECEIPT**]')


with cl:
    img,img2,img3 = st.columns(3)
    with img:
        st.image('fb.png',use_column_width=True) #to use full width
    
    st.write('')
    st.write(':blue[FaceBook]')
    st.write(':blue[1 Hacker Way, Menlo Park, CA 94025]')
    st.write(':blue[California, USA]')


st.header('')
st.header('')


ft,ft2,ft3 = st.columns([2,0.7,1])


with ft:
    name = st.text_input(':blue[**Bill To:**]',placeholder='Customer Name')
    st.write('')
    email = st.text_input('Enter email address',placeholder='Enter Email Address',label_visibility='collapsed')


with ft2:
    st.write(':blue[**Receipt #**]')
    st.write('')
    st.write(':blue[**Receipt Date**]')
    st.write('')
    st.write(':blue[**Due Date**]')


with ft3:
   inv = st.text_input('receipt',label_visibility='collapsed')
   invdt = st.date_input('receipt date',label_visibility='collapsed')
   duedt = st.date_input('due date',label_visibility='collapsed')


st.header('')




st.divider()
st.header('')


c,c2,c3,c4 = st.columns([3,3,3,3])


with c:
    desc = st.text_input(':blue[**Description**]',placeholder='Enter Description')
with c2:
    qua = st.number_input(':blue[**Quantity**]',value=0,step=1)
with c3:
    pri = st.number_input(':blue[**Price | Item**]',value=0,step=1)
with c4:
    total = qua * pri
    amo = st.text_input(':blue[**Amount**]',placeholder=0, disabled=True, value=total)






st.header('')
st.divider()


py,py2 = st.columns([2,2])


with py:
    st.write(':blue[**Payment Info**]')
    st.write('Account Name: FaceBook')
    st.write('Account Number: 00919900001')
    st.write('Bank Name: Meta Pay')


with py2:
    ppy,ppy2 = st.columns([1,5])
    with ppy2:
     st.write(':blue[**Payment Due:**]')


     st.subheader(f'{total:,} AED')



