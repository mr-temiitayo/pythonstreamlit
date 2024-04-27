import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

st.title('Invoice Generator')

# Function to generate PDF
def generate_pdf(data):
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=12)

    # Define the positions for the columns
    column1_x = 10
    column2_x = 70
    column3_x = 120
    column4_x = 170

    # Define the width of each column
    column_width = 50  # Adjust this value as needed

    # Add headers
    pdf.set_xy(column1_x, 20)
    pdf.cell(column_width, 10, txt="DESCRIPTION", ln=True, align="L")

    pdf.set_xy(column2_x, 20)
    pdf.cell(column_width, 10, txt="QTY", ln=True, align="L")

    pdf.set_xy(column3_x, 20)
    pdf.cell(column_width, 10, txt="PRICE", ln=True, align="L")

    pdf.set_xy(column4_x, 20)
    pdf.cell(column_width, 10, txt="AMOUNT", ln=True, align="L")

    # Add data
    row_height = 10
    y_position = 30
    for item in data:
        pdf.set_xy(column1_x, y_position)
        pdf.cell(column_width, row_height, txt=item['Description'], ln=True, align="L")

        pdf.set_xy(column2_x, y_position)
        pdf.cell(column_width, row_height, txt=str(item['Quantity']), ln=True, align="L")

        pdf.set_xy(column3_x, y_position)
        pdf.cell(column_width, row_height, txt=str(item['Price']), ln=True, align="L")

        pdf.set_xy(column4_x, y_position)
        pdf.cell(column_width, row_height, txt=str(item['Amount']), ln=True, align="L")

        y_position += row_height

    # Save the PDF
    pdf_file = "example.pdf"
    pdf.output(pdf_file)
    return pdf_file


lenght = [n for n in range(1,11)]
items_no = st.sidebar.selectbox("Enter Number of Items", lenght)

# Create lists to store the inputs
describe_list = []
quantity_list = []
amount_list = []

#st.header("Fill in Your Invoice")
col1a, colb, col1c = st.columns([2,1,1])
with col1c:
    st.header("INVOICE")

# logo = Image.open(r'C:/Users/USER/Downloads/logo2.png')
with col1a:
    image1, image2, image3 = st.columns(3)
    with image1:
        st.image('fb.png', use_column_width=True) #to use full width

col2a, col2b, col2c = st.columns(3)
if col2a:
    st.write('eduSTEMlab')
    st.write('327a, Corporation Drive, Ikoyi')
    st.write('Lagos. Nigeria')

st.write('')
st.write('')
col3a, col3b, col3c = st.columns([4,1,2])
with col3a:
    st.write('**Bill To:**')
    customer = st.text_input('w', placeholder='Customer name', label_visibility='collapsed')        
    address = st.text_input('s', placeholder='Enter Address', label_visibility='collapsed')

with col3b:
    st.write('**Invoice#**')
    st.write('**Invoice Date**')
    st.write('')
    st.write('**Due Date**')

with col3c:
    invoice_number = st.text_input('invoice_number', label_visibility='collapsed')
    invoice_date = st.date_input('invoice_date', label_visibility='collapsed')
    due_date = st.date_input('due_date', label_visibility='collapsed')

st.write('')
st.write('')
st.write('')

for i in range(items_no):
    col4a, col4b, col4c = st.columns([3,1,1])
    with col4a:
        st.write('**Description**')
        describe = st.text_input('t', placeholder='Enter Description', label_visibility='collapsed', key=f"describe_input_{i}")
        describe_list.append(describe)
    with col4b:
        st.write('**Quantity**')
        quantity = st.number_input('s', value=0, label_visibility='collapsed', key=f"quantity_input_{i}")
        quantity_list.append(quantity)
    with col4c:
        st.write('**Amount**')
        amount = st.number_input('t', value=0, step=1000, label_visibility='collapsed', key=f"amount_input_{i}")
        amount_list.append(amount)

st.divider()
col5a, col5b, col5c = st.columns(3)
with col5a:
    st.write('**Payment Info**')
    st.write('Acc name: eduSTEMlab')
    st.write('Acc number: 0097593992')
    st.write('Bank name: StanbiC IBTC')
with col5b:
    pass
with col5c:
    st.write('**Payment Due:**')
    st.subheader(f'#{sum(amount_list):,}')

# Create a DataFrame from the collected inputs
data = []
for desc, qty, amt in zip(describe_list, quantity_list, amount_list):
    data.append({'Description': desc, 'Quantity': qty, 'Price': amt / qty, 'Amount': amt})

# Display the DataFrame
st.table(pd.DataFrame(data))

# Generate the PDF
if st.button("Generate PDF"):
    pdf_file_path = generate_pdf(data)
    st.success(f"PDF generated successfully! You can download it from [here]({pdf_file_path}).")

# Display the download button
st.download_button(label='Download PDF', data=pdf_file_path, file_name='pdfexample.pdf', mime='application/pdf')

