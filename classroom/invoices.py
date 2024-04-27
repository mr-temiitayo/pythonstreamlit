import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

#st.set_page_config(layout="wide")
total=0

csv_filename = "user_data.csv"
df = pd.read_csv(csv_filename)  # Load the CSV file

lenght = [n for n in range(1,11)]
items_no=st.sidebar.selectbox("Enter Number of Items",lenght)

# Create lists to store the inputs
describe_list = []
quantity_list = []
price_list = []
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
    st.write('**Bill To:**')
    customer = st.text_input('w',placeholder='Customer name',label_visibility= 'collapsed')        

    address=st.text_input('s',placeholder='Enter Address',label_visibility= 'collapsed')
   

with col3b:

    st.write('')
    st.write('**Invoice#**')
    st.write("")
    st.write('**Invoice Date**')
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
    col4a,col4b,col4c,col4d = st.columns([2.5,2,2,2])
    with col4a:
        st.write('**Description**')
        describe = st.text_input('t',placeholder='Enter Description',label_visibility='collapsed',key=f"describe_input_{i}")
        describe_list.append(describe)
    with col4b:
        st.write('**Quantity**')
        quantity = st.number_input('s',value=0,label_visibility='collapsed',key=f"quantity_input_{i}")
        quantity_list.append(quantity)

    with col4c:
        st.write('**Price**')
        price = st.number_input('s',value=0,label_visibility='collapsed',key=f"price_input_{i}")
        price_list.append(price)

    with col4d:
        st.write('**Amount**')
        amount = st.text_input('s',value=quantity*price,label_visibility='collapsed',key=f"amount_input_{i}",disabled=True)
        amount_list.append(int(amount))

        # amount = (quantity*price) #,key=f"amount_input_{i}"
        # st.write("")
        # st.write(f'**{amount}**')

st.divider()
st.write(amount_list)
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
    'Price': price_list,
    'Amount': amount_list
}
df = pd.DataFrame(data)

st.table(df)


def generate_pdf():
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=12)

    # Define the positions for the columns
    column1_x = 10
    column2_x = 100 # Adjust this value based on the width of column 1 and any padding desired
    column3_x = 130
    column4_x = 170

    column_y = 35  # Specify the desired line height
    


    # Define the width of each column
    column_width = 100  # Adjust this value as needed

    # Add content to the PDF in different columns
    pdf.set_font(family='Arial', size=15, style='B')
    pdf.set_xy(column1_x, 15)
    pdf.cell(column_width, 10, txt="DESCRIPTION", ln=True, align="L") #width/height
    
    pdf.set_xy(column2_x, 15)
    pdf.cell(column_width, 10, txt="QTY", ln=True, align="L")

    pdf.set_xy(column3_x, 15)
    pdf.cell(column_width, 10, txt="PRICE", ln=True, align="L")

    pdf.set_xy(column4_x, 15)
    pdf.cell(column_width, 10, txt="AMOUNT", ln=True, align="L")

    # pdf.set_xy(column2_x, 40)
    # pdf.cell(column_width, 10, txt="Column 2, Row 2", ln=True, align="L")
    # st.write(f"**Description:** {row['Description']}, **Quantity:** {row['Quantity']}, **Amount:** {row['Amount']}")
    st.write("**Invoice Details:**")
    for index, row in df.iterrows():
        pdf.set_font(family='Arial', size=12, style='')
        pdf.set_xy(column1_x, column_y)
        pdf.cell(column_width, 10, txt=row['Description'], ln=True, align="L") #width/height

        pdf.set_xy(column2_x, column_y)
        pdf.cell(column_width, 10, txt=str(row['Quantity']), ln=True, align="L")

        pdf.set_xy(column3_x, column_y)
        pdf.cell(column_width, 10, txt=str(row['Price']), ln=True, align="L")

        pdf.set_xy(column4_x, column_y)
        pdf.cell(column_width, 10, txt=str(row['Amount']), ln=True, align="L")

        # Add a divider
        pdf.set_line_width(0.5)  # Set the width of the line
        pdf.line(column1_x, column_y-5, column4_x+20, column_y-5)  # Draw a line from start x,y stop x,y


        column_y +=10
#          SPACES
        pdf.set_xy(column1_x, column_y) #space
        pdf.cell(column_width, 10, '', ln=True, align="L") #space

        pdf.set_xy(column2_x, column_y) #space
        pdf.cell(column_width, 10, '', ln=True, align="L") #space

        pdf.set_xy(column3_x, column_y) #space
        pdf.cell(column_width, 10, '', ln=True, align="L") #space      

        pdf.set_xy(column4_x, column_y) #space
        pdf.cell(column_width, 10, '', ln=True, align="L") #space

        column_y +=10

    # Add content to the PDF in different columns
    pdf.set_font(family='Arial', size=15, style='B')
    pdf.set_xy(column1_x, column_y)
    pdf.cell(column_width, 10, txt="Bank Name", ln=True, align="L") #width/height

    pdf.set_xy(column4_x, column_y)
    pdf.cell(column_width, 10, txt="Amount Due", ln=True, align="L")

    # Save the PDF
    pdf_file = "example.pdf"
    pdf.output(pdf_file)
    return pdf_file


# Generate the PDF
pdf_file_path = generate_pdf()

# Read the generated PDF as binary data
with open(pdf_file_path, "rb") as f: #properly open and closed using the read binary mode
    pdf_data = f.read() #reads as binary to be processed/downloaded


if st.button("View"):


    # Encode the PDF data using base64
    pdf_data_base64 = base64.b64encode(pdf_data).decode('utf-8')

    # Generate an HTML tag to embed the PDF
    pdf_embedded_html = f'<embed src="data:application/pdf;base64,{pdf_data_base64}" type="application/pdf" width="100%" height="600px" />'

    # Display the embedded PDF in Streamlit
    st.markdown(pdf_embedded_html, unsafe_allow_html=True)


# Display the download button
st.download_button(label='Download PDF', data=pdf_data, file_name='pdfexample.pdf', mime='application/pdf')


