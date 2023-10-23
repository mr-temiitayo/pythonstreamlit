import streamlit as st
#st.set_page_config(layout="wide")
menu = ['Create Invoice','Download Invoice']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create Invoice":
    st.header("Fill in Your Invoice")
    with st.form(key='create',clear_on_submit=True):
        col1a,colb,col1c = st.columns([2,1,1])
        with col1c:
            st.header("INVOICE")
        
        with col1a:
            image_file = st.file_uploader("Upload Logo", type = ["png","jpg","jpeg"])
            if image_file is not None:
                st.write(image_file.name)
            if st.form_submit_button('Generate Invoice'):
                st.write('yes')
        
        col2a,col2b,col2c = st.columns(3)
        if col2a:
            st.write('eduSTEMlab')
            st.write('327a,coporation drive, Ikoyi')
            st.write('Lagos. Nigeria')

        col3a,col3b,col3c = st.columns(3)
        with col3a:
            st.write('Bill To:')
            st.write('eduSTEMlab')

        with col3b:
            st.write('Invoice#')
            st.write('Invoice Date')
            st.write('Due Date')

        with col3c:
            invoice_number = st.text_input('invoice_number',label_visibility= 'hidden')
            invoice_date = st.date_input('invoice_date',label_visibility= 'hidden')
            due_date = st.date_input('due_date',label_visibility= 'hidden')