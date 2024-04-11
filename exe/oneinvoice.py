import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from streamlit.components.v1 import html
import time  # Import time module
from PIL import Image
import pandas as pd
import os
from fpdf import FPDF
import base64



#st.set_page_config(layout="wide")
total=0

csv_filename = "user_data.csv"
df = pd.read_csv(csv_filename)  # Load the CSV file

menu = ['Create Invoice','Download Invoice']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create Invoice":
    #st.header("Fill in Your Invoice")
    col1a,colb,col1c = st.columns([2,1,1])
    with col1c:
        st.header("INVOICE")
    
    with col1a:
        logo = Image.open('employee.png')
        # Image.open(r'image/logo.png')
        st.image(logo,50,50) #to use full width

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

    col4a,col4b,col4c = st.columns([3,1,1])
    with col4a:
        st.write('**Description**')
        describe1 = st.text_input('t',placeholder='Enter Description',label_visibility='collapsed')
    with col4b:
        st.write('**Quantity**')
        quantity1 = st.number_input('s',value=10,label_visibility='collapsed')
    with col4c:
        st.write('**Amount**')
        amount1 = st.number_input('t',value=20,label_visibility='collapsed')
        total1 = quantity1 * amount1
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
        st.subheader(f'#{total1:,}')

    # Button to save the information to the CSV file--------------------
    if st.button("Save Information"):
        # Create a DataFrame with the user's information
        data = {'Customer': [customer], 'Address': [address], 'Invoice Number': [invoice_number],
                'Invoice Date':[invoice_date], 'Due Date':[due_date],'Description':[describe1],
                'Quantity':[quantity1],'Amount':[amount1],'Total':total1}
        df = pd.DataFrame(data)

        # Save the DataFrame to the CSV file
        df.to_csv(csv_filename, index=False)

        st.success(f"Receipt Information saved")


#--------------------------Download Invoice Page---------------------------------------------
if choice == "Download Invoice":
    loaded_data = pd.read_csv(csv_filename)
    if not loaded_data.empty:
        extracted_customer = loaded_data['Customer'].iloc[0] #wxtract from the first row
        extracted_address = loaded_data['Address'].iloc[0]
        extracted_invoice_number = loaded_data['Invoice Number'].iloc[0]
        extracted_invoice_date = loaded_data['Invoice Date'].iloc[0]
        extracted_due_date = loaded_data['Due Date'].iloc[0]
        extracted_descibe1 = loaded_data['Description'].iloc[0]
        extracted_quantity1 = loaded_data['Quantity'].iloc[0]
        extracted_amount1 = loaded_data['Amount'].iloc[0]
        extracted_total1 = loaded_data['Total'].iloc[0]
    else:
        st.write("No data saved yet.")


    col1a,colb,col1c = st.columns([2,1,1])
    with col1c:
        st.header("INVOICE")
    
    with col1a:
        logo = Image.open('employee.png')
        st.image(logo,50,50) #to use full width

    col2a,col2b,col2c = st.columns(3)
    if col2a:
        st.write('eduSTEMlab')
        st.write('327a,coporation drive, Ikoyi')
        st.write('Lagos. Nigeria')

    st.write('')
    st.write('')
    col3a,col3b,col3c = st.columns([4,1,1])
    with col3a:
        #st.write('')
        #st.write('')
        st.write('**Bill To:**')
        #st.write('')
        st.write(extracted_customer)
        #st.write('')
        st.write(extracted_address)
        #st.write("")

    with col3b:
        #st.write('')
        #st.write('')
        st.write('**Invoice#**')
        #st.write('')
        #st.write('')
        #st.write("")
        st.write('**Invoice Date**')
        #st.write('')
        #st.write('')
        #st.write('')
        st.write('**Due Date**')

    with col3c:
        #st.write('')
        st.write(str(extracted_invoice_number))
        st.write(str(extracted_invoice_date))
        st.write(str(extracted_due_date))


    st.write('')
    st.write('')
    st.write('')

    col4a,col4b,col4c = st.columns([4,1,1])
    with col4a:
        st.write('**Description**')
        st.write(extracted_descibe1)
    with col4b:
        st.write('**Quantity**')
        st.write(str(extracted_quantity1))
    with col4c:
        st.write('**Amount**')
        st.write((f'{extracted_amount1:,}'))
    st.divider()
    col5a,col5b,col5c = st.columns(3)
    with col5a:
        st.write('**Payment Info**')
        st.write('Acc name: eduSTEMlab')
        st.write('Acc number: 00298673992')
        st.write('Bank name: StanbiC IBTC')
    with col5b:
        pass
    with col5c:
        st.write('**Payment Due:**')
        st.subheader(f'#{extracted_total1:,}')



# Function to generate PDF
# Define the folder path where the PDF file will be stored
PDF_folder = "pdf_folder/"

# Create the folder if it doesn't exist
if not os.path.exists(PDF_folder):
    os.makedirs(PDF_folder)

# Concatenate folder path with PDF filename to get the full path
full_pdf_path = PDF_folder + "invoice.pdf"

# Offer link to view the PDF in the browser
st.markdown(f"View [invoice PDF]({full_pdf_path})")

# Function to generate PDF
def generate_pdf(customer, address, invoice_number, invoice_date, due_date, description, quantity, amount, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Adding content to the PDF
    pdf.cell(200, 10, txt="INVOICE", ln=True, align="C")
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Bill To:", ln=True)
    pdf.cell(200, 10, txt=f"Customer: {customer}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True)
    pdf.cell(200, 10, txt=f"Invoice #: {invoice_number}", ln=True)
    pdf.cell(200, 10, txt=f"Invoice Date: {invoice_date}", ln=True)
    pdf.cell(200, 10, txt=f"Due Date: {due_date}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Description", ln=True)
    pdf.cell(200, 10, txt=description, ln=True)
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Quantity", ln=True)
    pdf.cell(200, 10, txt=str(quantity), ln=True)
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Amount", ln=True)
    pdf.cell(200, 10, txt=str(amount), ln=True)
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Payment Info", ln=True)
    pdf.cell(200, 10, txt="Acc name: eduSTEMlab", ln=True)
    pdf.cell(200, 10, txt="Acc number: 00298673992", ln=True)
    pdf.cell(200, 10, txt="Bank name: StanbiC IBTC", ln=True)
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt="Payment Due:", ln=True)
    pdf.cell(200, 10, txt=f"#{total:,}", ln=True)
    
    # Save the PDF
    pdf_file = full_pdf_path  # Use the full path
    pdf.output(pdf_file)

    return pdf_file

# Button to download the PDF
if choice == "Download Invoice" and st.button("Download PDF"):
    # Generate PDF
    pdf_file = generate_pdf(extracted_customer, extracted_address, extracted_invoice_number, extracted_invoice_date, extracted_due_date, extracted_descibe1, extracted_quantity1, extracted_amount1, extracted_total1)



         
     


