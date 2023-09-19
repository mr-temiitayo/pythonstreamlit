# A boy went to the supermarket to get a list of items, ask the user for the 5 items he wants to get
# Put the items in the customer’s list
# Display the customer’s list

import streamlit as st
st.title('Welcome to the Mart')

if 'items' not in st.session_state:
    st.session_state.items = ''

if 'itemslist' not in st.session_state:
    st.session_state.itemslist = []


items = st.text_input('Enter items to purchase',key='items')

select = st.button('Select',key='select')

if select:
    st.session_state.itemslist.append(items)
    st.write(st.session_state.itemslist)
    #joins all elements in the list as aand sep with a , and space 
    items_text = ", ".join(st.session_state.itemslist) 
    st.write("Customer's List:")
    st.write(items_text)