import streamlit as st
from PIL import Image
import pandas as pd
#st.set_page_config(layout="wide")
total=0

csv_filename = "user_data.csv"
df = pd.read_csv(csv_filename)  # Load the CSV file

lenght = [n for n in range(1,11)]
items_no=st.sidebar.selectbox("Enter Number of Items",lenght)

# Create lists to store the inputs
describe_list = []
quantity_list = []
amount_list = []

#st.header("Fill in Your Invoice")
col1a,colb,col1c = st.columns([2,1,1])
with col1c:
    st.header("INVOICE")

# logo = Image.open(r'C:/Users/USER/Downloads/logo2.png')
with col1a:
    image1, image2,image3 = st.columns(3)
    with image1:
        st.image('fb.png',use_column_width=True) #to use full width

col2a,col2b,col2c = st.columns(3)
if col2a:
    st.write('eduSTEMlab')
    st.write('327a,coporation drive, Ikoyi')
    st.write('Lagos. Nigeria')

st.write('')
st.write('')
col3a,col3b,col3c = st.columns([4,1,2])
with col3a:
    #st.write('')
    #st.write('')
    st.write('**Bill To:**')
    customer = st.text_input('w',placeholder='Customer name',label_visibility= 'collapsed')        
    #st.write('')
    address=st.text_input('s',placeholder='Enter Address',label_visibility= 'collapsed')
    #st.write("")

with col3b:
    #st.write('')
    st.write('')
    st.write('**Invoice#**')
    #st.write('')
    #st.write('')
    st.write("")
    st.write('**Invoice Date**')
    #st.write('')
    #st.write('')
    st.write('')
    st.write('**Due Date**')

with col3c:
    st.write('')
    invoice_number = st.text_input('invoice_number',label_visibility= 'collapsed')
    invoice_date = st.date_input('invoice_date',label_visibility= 'collapsed')
    due_date = st.date_input('due_date',label_visibility= 'collapsed')


st.write('')
st.write('')
st.write('')

for i in range(items_no):
    col4a,col4b,col4c = st.columns([3,1,1])
    with col4a:
        st.write('**Description**')
        describe = st.text_input('t',placeholder='Enter Description',label_visibility='collapsed',key=f"describe_input_{i}")
        describe_list.append(describe)
    with col4b:
        st.write('**Quantity**')
        quantity = st.number_input('s',value=0,label_visibility='collapsed',key=f"quantity_input_{i}")
        quantity_list.append(quantity)
    with col4c:
        st.write('**Amount**')
        amount = st.number_input('t',value=0,step=1000,label_visibility='collapsed',key=f"amount_input_{i}")
        amount_list.append(amount)

st.divider()
col5a,col5b,col5c = st.columns(3)
with col5a:
    st.write('**Payment Info**')
    st.write('Acc name: eduSTEMlab')
    st.write('Acc number: 0097593992')
    st.write('Bank nmae: StanbiC IBTC')
with col5b:
    pass
with col5c:
    st.write('**Payment Due:**')
    st.subheader(f'#{sum(amount_list):,}')

# Button to save the information to the CSV file--------------------
# Create a DataFrame from the collected inputs
data = {
    'Description': describe_list,
    'Quantity': quantity_list,
    'Amount': amount_list
}
df = pd.DataFrame(data)

st.table(df)